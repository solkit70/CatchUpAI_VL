"""Local title-card/effects demo. Preserves source speech; no upload, music or TTS.
Usage: python render_effects.py --source HIGHLIGHT.mp4 --output NEW_DIRECTORY
Pillow generates typography assets; FFmpeg inserts silent cards and section labels.
"""
import argparse
import json
import subprocess
import time
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

from PIL import Image, ImageDraw, ImageFont

WIDTH, HEIGHT = 1280, 720
BOUNDARY = 62.5
FPS = "30000/1001"


def probe(path):
    return json.loads(subprocess.check_output([
        "ffprobe", "-v", "error", "-show_format", "-show_streams", "-of", "json", str(path)
    ]))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--font", type=Path, default=Path("C:/Windows/Fonts/malgun.ttf"))
    args = parser.parse_args()
    source, directory = args.source.resolve(), args.output.resolve()
    if not source.is_file() or not args.font.is_file():
        parser.error("Source and installed font must exist.")
    if directory.exists() or source.parent == directory:
        parser.error("Use a new output directory to preserve all previous artifacts.")
    info = probe(source)
    duration = float(info["format"]["duration"])
    if duration <= BOUNDARY:
        parser.error("This source-specific demo requires the existing two-part highlight.")
    video = next(s for s in info["streams"] if s["codec_type"] == "video")
    if (video["width"], video["height"]) != (WIDTH, HEIGHT):
        parser.error("Expected 1280x720 highlight.")
    before = (source.stat().st_size, source.stat().st_mtime_ns)
    directory.mkdir(parents=True)

    def font(size):
        return ImageFont.truetype(str(args.font), size)

    def card(name, eyebrow, title, subtitle):
        im = Image.new("RGB", (WIDTH, HEIGHT), "#101a2b")
        draw = ImageDraw.Draw(im)
        draw.rectangle((0, 0, 18, HEIGHT), fill="#42d7c7")
        draw.rectangle((80, 157, 208, 163), fill="#42d7c7")
        draw.text((80, 95), eyebrow, font=font(25), fill="#a7b9cf")
        draw.text((76, 260), title, font=font(68), fill="#f5f8ff")
        draw.text((80, 365), subtitle, font=font(36), fill="#cad6e6")
        draw.text((80, 627), "로컬 편집 데모 · 실제 발표 발췌", font=font(23), fill="#9badc3")
        path = directory / name
        im.save(path)
        return path

    def lower(name, title, subtitle):
        im = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
        draw = ImageDraw.Draw(im)
        draw.rounded_rectangle((42, 567, 665, 675), radius=12, fill=(16, 26, 43, 230))
        draw.rectangle((42, 583, 48, 657), fill="#42d7c7")
        draw.text((68, 577), title, font=font(34), fill="white")
        draw.text((68, 628), subtitle, font=font(22), fill="#c2d2e5")
        path = directory / name
        im.save(path)
        return path

    intro = card("intro.png", "SKILL HIGHLIGHTS", "Skill 활용", "PR 리뷰와 Q&A")
    section = card("qa-card.png", "QUESTIONS & ANSWERS", "질의응답", "Skill의 범위와 구성")
    outro = card("outro.png", "END OF EXCERPT", "발표 발췌 요약", "원본 발언을 보존한 로컬 편집 데모")
    pr_label = lower("pr-label.png", "핵심 설명", "PR 리뷰에 Skill 활용하기")
    qa_label = lower("qa-label.png", "질의응답", "Skill의 범위와 구성")
    filters = [
        "[0:v]split=2[p0][q0]",
        "[0:a]asplit=2[pa0][qa0]",
        "[1:v]trim=duration=5,setpts=PTS-STARTPTS,setsar=1,format=yuv420p,fade=t=in:d=0.3,fade=t=out:st=4.5:d=0.5[v0]",
        "anullsrc=r=48000:cl=stereo,atrim=duration=5,asetpts=PTS-STARTPTS[a0]",
        f"[p0]trim=end={BOUNDARY},setpts=PTS-STARTPTS[p1]",
        "[p1][4:v]overlay=0:0:eof_action=repeat:enable='lt(t,4)',setsar=1,format=yuv420p[v1]",
        f"[pa0]atrim=end={BOUNDARY},asetpts=PTS-STARTPTS[a1]",
        "[2:v]trim=duration=1.5,setpts=PTS-STARTPTS,setsar=1,format=yuv420p,fade=t=in:d=0.15,fade=t=out:st=1.3:d=0.2[v2]",
        "anullsrc=r=48000:cl=stereo,atrim=duration=1.5,asetpts=PTS-STARTPTS[a2]",
        f"[q0]trim=start={BOUNDARY},setpts=PTS-STARTPTS[q1]",
        "[q1][5:v]overlay=0:0:eof_action=repeat:enable='lt(t,4)',setsar=1,format=yuv420p[v3]",
        f"[qa0]atrim=start={BOUNDARY},asetpts=PTS-STARTPTS[a3]",
        "[3:v]trim=duration=3,setpts=PTS-STARTPTS,setsar=1,format=yuv420p,fade=t=in:d=0.2,fade=t=out:st=2.5:d=0.5[v4]",
        "anullsrc=r=48000:cl=stereo,atrim=duration=3,asetpts=PTS-STARTPTS[a4]",
        "[v0][a0][v1][a1][v2][a2][v3][a3][v4][a4]concat=n=5:v=1:a=1[v][a]",
    ]
    output = directory / "talk-B-effects-demo-v1.mp4"
    command = ["ffmpeg", "-hide_banner", "-loglevel", "warning", "-n", "-i", str(source)]
    for path, seconds in [(intro, 5), (section, 1.5), (outro, 3)]:
        command += ["-loop", "1", "-framerate", FPS, "-t", str(seconds), "-i", str(path)]
    for path in [pr_label, qa_label]:
        command += ["-i", str(path)]
    command += ["-filter_complex_threads", "1", "-filter_complex", ";".join(filters),
                "-map", "[v]", "-map", "[a]", "-map_metadata", "-1", "-c:v", "libx264",
                "-threads", "2", "-preset", "veryfast", "-crf", "20", "-pix_fmt", "yuv420p",
                "-r", FPS, "-c:a", "aac", "-ar", "48000", "-ac", "2", "-b:a", "160k",
                "-movflags", "+faststart", str(output)]
    started = time.monotonic()
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode:
        raise RuntimeError(result.stderr)
    rendered = probe(output)
    check = subprocess.run(["ffmpeg", "-v", "error", "-i", str(output), "-f", "null", "-"],
                           capture_output=True, text=True)
    if check.returncode or check.stderr.strip():
        raise RuntimeError(check.stderr)
    assert before == (source.stat().st_size, source.stat().st_mtime_ns)
    manifest = {
        "created": datetime.now(ZoneInfo("America/Los_Angeles")).isoformat(),
        "source": str(source), "output": str(output), "command": command,
        "source_duration": duration, "actual_duration": float(rendered["format"]["duration"]),
        "expected_duration": duration + 9.5, "streams": rendered["streams"],
        "source_size_mtime_unchanged": True, "full_decode": "OK",
        "ffmpeg_warnings": result.stderr.strip(), "elapsed_seconds": round(time.monotonic() - started, 3),
        "design": "5s silent intro; section labels for 4s each; 1.5s silent Q&A card; 3s silent outro",
        "speech_subtitles": False, "music": False, "new_speech": False,
    }
    (directory / "render-manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({k: manifest[k] for k in ["actual_duration", "expected_duration", "full_decode", "ffmpeg_warnings", "elapsed_seconds"]}))


if __name__ == "__main__":
    main()
