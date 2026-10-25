"""Local review cuts. No upload; originals are opened read-only.
Usage: python split_presentations.py --source SOURCE_DIR --output OUTPUT_DIR
Stream-copy cuts are review drafts: inspect audio/frames before final delivery.
"""
import argparse
import json
import subprocess
import time
from pathlib import Path

CUTS = [
    ("01-opening-draft.mp4", "IMG_5249.MP4", 0, None, "opening"),
    ("02-talk-A-draft.mp4", "IMG_5250.MP4", 0, None, "talk A, includes Q&A"),
    ("03-answer-unplaced-draft.mp4", "IMG_5251.MP4", 0, None, "short answer; placement unconfirmed"),
    ("04-talk-B-draft.mp4", "IMG_5252.MP4", 0, 1652, "talk B"),
    ("05-talk-B-QA-draft.mp4", "IMG_5252.MP4", 1652, None, "talk B Q&A, other speakers may answer"),
    ("06-workshop-C-draft.mp4", "IMG_5253.MP4", 0, 2279, "workshop C, includes earlier questions"),
    ("07-open-QA-and-close-draft.mp4", "IMG_5253.MP4", 2279, None, "open Q&A and close; multiple speakers"),
]

def probe(path):
    return json.loads(subprocess.check_output([
        "ffprobe", "-v", "error", "-show_entries",
        "format=duration:stream=codec_type,width,height", "-of", "json", str(path)
    ]))

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    source, output = args.source.resolve(), args.output.resolve()
    if source == output or source in output.parents:
        parser.error("Use a separate output directory outside the source directory.")
    paths = {name: source / name for _, name, *_ in CUTS}
    for path in paths.values():
        if not path.is_file():
            parser.error(f"Missing input: {path.name}")
    output.mkdir(parents=True, exist_ok=True)
    if any((output / name).exists() for name, *_ in CUTS) or (output / "cut-manifest.json").exists():
        parser.error("Outputs already exist. Choose a new directory to preserve earlier runs.")
    original_stats = {name: (p.stat().st_size, p.stat().st_mtime_ns) for name, p in paths.items()}
    durations = {name: float(probe(p)["format"]["duration"]) for name, p in paths.items()}
    manifest = {"mode": "local stream-copy review drafts", "boundary_basis": "existing ASR plus sampled video frames; no full listening pass", "cuts": []}
    started = time.monotonic()
    for name, src, start, end, label in CUTS:
        end = durations[src] if end is None else end
        command = ["ffmpeg", "-hide_banner", "-loglevel", "warning", "-n", "-ss", str(start),
                   "-i", str(paths[src]), "-t", str(end - start), "-map", "0:v:0", "-map", "0:a:0",
                   "-map_metadata", "-1", "-c", "copy", "-movflags", "+faststart", str(output / name)]
        step = time.monotonic()
        result = subprocess.run(command, capture_output=True, text=True)
        if result.returncode:
            raise RuntimeError(f"Cut failed: {name}: {result.stderr}")
        info = probe(output / name)
        actual = float(info["format"]["duration"])
        # Decode start and end to catch damaged/undecodable boundary frames.
        checks = []
        for seek in [0, max(0, actual - 2)]:
            check = subprocess.run(["ffmpeg", "-v", "error", "-ss", str(seek), "-i", str(output / name),
                                    "-t", "2", "-map", "0:v:0", "-map", "0:a:0", "-f", "null", "-"],
                                   capture_output=True, text=True)
            checks.append({"seek": seek, "exit_code": check.returncode, "messages": check.stderr.strip()})
            if check.returncode or check.stderr.strip():
                raise RuntimeError(f"Boundary decode needs investigation: {name}: {check.stderr}")
        manifest["cuts"].append({"output": name, "source": src, "start": start, "end": end,
            "label": label, "expected_duration": end - start, "actual_duration": actual,
            "duration_delta": actual - (end - start), "bytes": (output / name).stat().st_size,
            "streams": info["streams"], "decode_checks": checks,
            "elapsed_seconds": round(time.monotonic() - step, 3), "ffmpeg_warnings": result.stderr.strip()})
        print(f"{name}: {actual:.3f}s, boundary decode OK", flush=True)
    manifest["elapsed_seconds"] = round(time.monotonic() - started, 3)
    manifest["original_size_and_mtime_unchanged"] = all(
        (p.stat().st_size, p.stat().st_mtime_ns) == original_stats[name] for name, p in paths.items())
    (output / "cut-manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    print("Manifest saved. Final audio/content review remains required.", flush=True)

if __name__ == "__main__":
    main()
