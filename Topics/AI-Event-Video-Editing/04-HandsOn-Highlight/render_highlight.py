"""Render the local talk-B excerpt draft; no uploads or source modifications.

Usage: python render_highlight.py --source IMG_5252.MP4 --output NEW_FILE.mp4
The source-specific editorial choices below are not an automatic highlight model.
"""
import argparse
import json
import subprocess
import time
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

CUTS = [
    {"start": 1521.5, "end": 1584.0, "purpose": "PR-review skill example"},
    {"start": 1672.0, "end": 1757.2, "purpose": "Question and answer about skill scope"},
]


def probe(path):
    return json.loads(subprocess.check_output([
        "ffprobe", "-v", "error", "-show_format", "-show_streams", "-of", "json", str(path)
    ]))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    source, output = args.source.resolve(), args.output.resolve()
    manifest = output.with_suffix(".json")
    if not source.is_file() or source.name.lower() != "img_5252.mp4":
        parser.error("These source-specific cuts require IMG_5252.MP4.")
    if output.suffix.lower() != ".mp4" or source.parent == output.parent:
        parser.error("Use an MP4 output in a separate directory.")
    if output.exists() or manifest.exists():
        parser.error("Choose a new output name; existing artifacts are preserved.")
    before = (source.stat().st_size, source.stat().st_mtime_ns)
    original = probe(source)
    if float(original["format"]["duration"]) < CUTS[-1]["end"]:
        parser.error("Source is shorter than the selected excerpts.")
    output.parent.mkdir(parents=True, exist_ok=True)
    command = ["ffmpeg", "-hide_banner", "-loglevel", "warning", "-n"]
    filters, labels = [], []
    for index, cut in enumerate(CUTS):
        command += ["-ss", str(cut["start"]), "-t", str(cut["end"] - cut["start"]), "-i", str(source)]
        filters += [
            f"[{index}:v:0]setpts=PTS-STARTPTS,fps=30000/1001,setsar=1[v{index}]",
            f"[{index}:a:0]asetpts=PTS-STARTPTS,aresample=48000[a{index}]",
        ]
        labels.append(f"[v{index}][a{index}]")
    filters.append("".join(labels) + f"concat=n={len(CUTS)}:v=1:a=1[v][a]")
    command += ["-filter_complex", ";".join(filters), "-map", "[v]", "-map", "[a]",
                "-map_metadata", "-1", "-c:v", "libx264", "-preset", "veryfast", "-crf", "20",
                "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "160k",
                "-movflags", "+faststart", str(output)]
    started = time.monotonic()
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode:
        raise RuntimeError(result.stderr)
    rendered = probe(output)
    check = subprocess.run(["ffmpeg", "-v", "error", "-i", str(output), "-f", "null", "-"],
                           capture_output=True, text=True)
    if check.returncode or check.stderr.strip():
        raise RuntimeError("Full decode failed: " + check.stderr)
    unchanged = before == (source.stat().st_size, source.stat().st_mtime_ns)
    if not unchanged:
        raise RuntimeError("Source size or modification timestamp changed.")
    report = {
        "created": datetime.now(ZoneInfo("America/Los_Angeles")).isoformat(),
        "mode": "AI-selected transcript excerpts, local FFmpeg render; human review pending",
        "source": str(source), "cuts": CUTS,
        "selection_basis": "Existing ASR plus nearby low-volume intervals (-32dB, >=0.12s); no listening claim",
        "expected_seconds": sum(c["end"] - c["start"] for c in CUTS),
        "actual_seconds": float(rendered["format"]["duration"]),
        "streams": rendered["streams"], "command": command,
        "ffmpeg_warnings": result.stderr.strip(), "full_decode": "OK",
        "source_size_and_mtime_unchanged": unchanged,
        "elapsed_seconds": round(time.monotonic() - started, 3),
    }
    manifest.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({k: report[k] for k in ["actual_seconds", "full_decode", "source_size_and_mtime_unchanged", "elapsed_seconds", "ffmpeg_warnings"]}))


if __name__ == "__main__":
    main()
