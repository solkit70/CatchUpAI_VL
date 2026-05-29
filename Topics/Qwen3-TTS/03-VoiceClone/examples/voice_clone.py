"""
voice_clone.py — Qwen3-TTS 보이스 클론 실습 (M3)

두 단계:
  1. 음성 등록 (qwen-voice-enrollment) → voice_id 발급
  2. 클론 음성으로 합성 (qwen3-tts-vc-2026-01-22)

실행:
    python voice_clone.py --sample samples/changsoo_sample.mp3

출력:
    clone_result.wav — 창수 목소리로 합성된 음성
"""

import argparse
import base64
import os
import sys
import time
import urllib.request
from pathlib import Path

import dashscope
import requests

sys.stdout.reconfigure(encoding="utf-8")

# ── 설정 ──────────────────────────────────────────────────────────────────
dashscope.base_http_api_url = "https://dashscope-intl.aliyuncs.com/api/v1"
ENROLL_URL   = "https://dashscope-intl.aliyuncs.com/api/v1/services/audio/tts/customization"
CLONE_MODEL  = "qwen3-tts-vc-2026-01-22"
PREFERRED_NAME = "changsoo"

CLONE_TEXT = (
    "안녕하세요, 여러분. 저는 창수입니다. "
    "오늘 AI in Action 라이브 방송에서 보이스 클론 기술을 직접 실험해 보고 있습니다. "
    "이 목소리가 제 목소리와 얼마나 비슷한지 들어보세요."
)

OUT_DIR = Path(__file__).parent


# ── Step 1: 음성 등록 ─────────────────────────────────────────────────────
def enroll_voice(sample_path: str) -> str:
    """mp3/wav 파일을 base64로 인코딩해 등록. voice_id를 반환."""
    path = Path(sample_path)
    if not path.exists():
        raise FileNotFoundError(f"샘플 파일 없음: {sample_path}")

    mime = "audio/mpeg" if path.suffix.lower() == ".mp3" else "audio/wav"
    b64  = base64.b64encode(path.read_bytes()).decode()
    data_uri = f"data:{mime};base64,{b64}"

    payload = {
        "model": "qwen-voice-enrollment",
        "input": {
            "action": "create",
            "target_model": CLONE_MODEL,
            "preferred_name": PREFERRED_NAME,
            "audio": {"data": data_uri},
        },
    }
    headers = {
        "Authorization": f"Bearer {os.environ['DASHSCOPE_API_KEY']}",
        "Content-Type": "application/json",
    }

    print(f"[Step 1] 음성 등록 중... ({path.name}, {round(path.stat().st_size/1024,1)} KB)")
    t = time.time()
    resp = requests.post(ENROLL_URL, json=payload, headers=headers, timeout=60)
    elapsed = round(time.time() - t, 2)

    if resp.status_code != 200:
        raise RuntimeError(f"등록 실패 {resp.status_code}: {resp.text}")

    voice_id = resp.json()["output"]["voice"]
    print(f"  ✅ 등록 완료  voice_id: {voice_id}  ({elapsed}s)")
    return voice_id


# ── Step 2: 클론 합성 ─────────────────────────────────────────────────────
def synthesize_clone(voice_id: str, text: str, out_name: str = "clone_result.wav") -> Path:
    print(f"\n[Step 2] 클론 합성 중...")
    print(f"  voice_id: {voice_id}")
    print(f"  텍스트: {text[:50]}...")

    t = time.time()
    response = dashscope.MultiModalConversation.call(
        model=CLONE_MODEL,
        api_key=os.environ["DASHSCOPE_API_KEY"],
        text=text,
        voice=voice_id,
        stream=False,
    )
    elapsed = round(time.time() - t, 2)

    if response.status_code != 200:
        raise RuntimeError(f"합성 실패 {response.status_code}: {response.message}")

    audio_url = response.output.audio.url
    out_path = OUT_DIR / out_name
    urllib.request.urlretrieve(audio_url, str(out_path))

    size_kb = round(out_path.stat().st_size / 1024, 1)
    print(f"  ✅ 저장: {out_path.name} ({size_kb} KB)  ({elapsed}s)")
    return out_path


# ── Main ──────────────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(description="Qwen3-TTS 보이스 클론")
    parser.add_argument("--sample", default=None, help="참조 음성 파일 경로 (mp3/wav)")
    parser.add_argument("--voice-id", default=None, help="기존 voice_id 직접 지정 (등록 생략)")
    parser.add_argument("--text", default=CLONE_TEXT, help="합성할 텍스트")
    parser.add_argument("--out", default="clone_result.wav", help="출력 파일명")
    args = parser.parse_args()

    if not os.environ.get("DASHSCOPE_API_KEY"):
        raise EnvironmentError("DASHSCOPE_API_KEY 환경변수가 설정되지 않았습니다.")

    print("=" * 50)
    print("Qwen3-TTS Voice Clone")
    print("=" * 50)

    if args.voice_id:
        voice_id = args.voice_id
        print(f"[기존 voice_id 사용] {voice_id}")
    elif args.sample:
        voice_id = enroll_voice(args.sample)
    else:
        raise ValueError("--sample 또는 --voice-id 중 하나를 지정해야 합니다.")

    out_path = synthesize_clone(voice_id, args.text, args.out)

    print(f"\n완료! 출력 파일: {out_path}")
    print(f"voice_id를 WorkLog에 기록하세요: {voice_id}")


if __name__ == "__main__":
    main()
