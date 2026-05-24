"""
voice_design.py — Qwen3-TTS 음색 디자인 실습 (M3)

자연어 프롬프트로 원하는 목소리 스타일을 생성한다.
Voice Clone과 동일한 customization 엔드포인트를 사용.
응답에 preview_audio(base64 WAV)가 포함되어 별도 합성 불필요.

실행:
    python voice_design.py

출력:
    vd_news.wav / vd_tutor.wav / vd_lively.wav
"""

import base64
import os
import sys
import time
from pathlib import Path

import requests

sys.stdout.reconfigure(encoding="utf-8")

# ── 설정 ──────────────────────────────────────────────────────────────────
ENROLL_URL   = "https://dashscope-intl.aliyuncs.com/api/v1/services/audio/tts/customization"
TARGET_MODEL = "qwen3-tts-vd-realtime-2026-01-15"
OUT_DIR      = Path(__file__).parent

PREVIEW_TEXT = (
    "안녕하세요. 오늘 AI 기술의 최신 트렌드를 함께 살펴보겠습니다. "
    "보이스 디자인 기술로 만들어진 이 목소리를 들어보세요."
)

VOICE_DESIGNS = [
    {
        "name": "뉴스 진행자",
        "preferred_name": "news",
        "out": "vd_news.wav",
        "language": "zh",
        "prompt": (
            "A composed middle-aged male announcer with a deep, rich and magnetic voice, "
            "a steady speaking speed and clear articulation, suitable for news broadcasting."
        ),
    },
    {
        "name": "AI 튜터",
        "preferred_name": "tutor",
        "out": "vd_tutor.wav",
        "language": "zh",
        "prompt": (
            "A warm and friendly male voice in his 30s, speaking at a moderate pace "
            "with a calm and encouraging tone, suitable for educational content and online courses."
        ),
    },
    {
        "name": "활기찬 캐릭터",
        "preferred_name": "lively",
        "out": "vd_lively.wav",
        "language": "zh",
        "prompt": (
            "A young, energetic voice in their mid-20s with a bright and cheerful tone, "
            "slightly fast-paced, suitable for entertainment and social media content."
        ),
    },
]


def design_voice(design: dict) -> dict:
    print(f"\n[{design['name']}] 음색 생성 중...")
    print(f"  프롬프트: {design['prompt'][:60]}...")

    headers = {
        "Authorization": f"Bearer {os.environ['DASHSCOPE_API_KEY']}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": "qwen-voice-design",
        "input": {
            "action": "create",
            "target_model": TARGET_MODEL,
            "voice_prompt": design["prompt"],
            "preview_text": PREVIEW_TEXT,
            "preferred_name": design["preferred_name"],
            "language": design["language"],
        },
        "parameters": {
            "sample_rate": 24000,
            "response_format": "wav",
        },
    }

    t = time.time()
    resp = requests.post(ENROLL_URL, json=payload, headers=headers, timeout=60)
    elapsed = round(time.time() - t, 2)

    if resp.status_code != 200:
        raise RuntimeError(f"실패 {resp.status_code}: {resp.text}")

    result = resp.json()
    voice_id = result["output"]["voice"]

    # preview_audio는 base64 인코딩된 WAV
    audio_b64 = result["output"]["preview_audio"]["data"]
    audio_bytes = base64.b64decode(audio_b64)

    out_path = OUT_DIR / design["out"]
    out_path.write_bytes(audio_bytes)

    size_kb = round(out_path.stat().st_size / 1024, 1)
    print(f"  ✅ 저장: {out_path.name} ({size_kb} KB)  ({elapsed}s)")
    print(f"  voice_id: {voice_id}")
    return {"name": design["name"], "voice_id": voice_id, "elapsed": elapsed, "size_kb": size_kb}


def main():
    if not os.environ.get("DASHSCOPE_API_KEY"):
        raise EnvironmentError("DASHSCOPE_API_KEY 환경변수가 설정되지 않았습니다.")

    print("=" * 50)
    print("Qwen3-TTS Voice Design — 3종 실험")
    print("=" * 50)

    results = []
    for d in VOICE_DESIGNS:
        r = design_voice(d)
        results.append(r)

    print("\n─── 결과 요약 ──────────────────────────")
    for r in results:
        print(f"  {r['name']:12s}  {r['size_kb']:6.1f} KB  {r['elapsed']}s")
    print("\n각 파일을 재생하고 WorkLog Quality Harness 표를 채워주세요.")


if __name__ == "__main__":
    main()
