"""
register_female_vd.py — 한국어 여성 Voice Design 신규 등록 (M3 연장)

M3 교훈: 영어 프롬프트 → 일본 억양 발생. 이번은 language="ko" + 한국어 프롬프트.
두 가지 스타일(차분·따뜻 / 활기·전문)을 등록하고 최적 버전을 선택한다.

실행:
    python register_female_vd.py

출력:
    vd_female_v1.wav (차분·따뜻), vd_female_v2.wav (활기·전문)
    각 voice_id 출력 → VOICE_MAP VD_FEMALE에 채우기
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
    "안녕하세요, 여러분. 오늘 Catch Up AI 라이브 방송에 오신 것을 환영합니다. "
    "이번 주 가장 흥미로운 AI 소식과 커뮤니티 이야기를 함께 나눠보겠습니다."
)

FEMALE_DESIGNS = [
    {
        "name": "female_v1 (차분·따뜻)",
        "preferred_name": "fwarm",
        "out": "vd_female_v1.wav",
        "language": "ko",
        "prompt": (
            "30대 여성의 차분하고 따뜻한 목소리. 명확하고 친근한 발음으로 "
            "커뮤니티 방송 진행자처럼 부드럽게 말합니다. "
            "적당한 속도로 신뢰감 있게 이야기합니다."
        ),
    },
    {
        "name": "female_v2 (활기·전문)",
        "preferred_name": "fbright",
        "out": "vd_female_v2.wav",
        "language": "ko",
        "prompt": (
            "30대 여성의 밝고 활기찬 목소리. 전문적이면서도 친근한 톤으로 "
            "AI와 기술 정보를 생동감 있게 전달합니다. "
            "명확한 발음과 자연스러운 억양으로 활기차게 말합니다."
        ),
    },
]


def design_female_voice(design: dict) -> dict:
    print(f"\n[{design['name']}] 음색 등록 중...")
    print(f"  언어: {design['language']}")
    print(f"  프롬프트: {design['prompt'][:50]}...")

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
        raise RuntimeError(f"등록 실패 {resp.status_code}: {resp.text}")

    result = resp.json()
    voice_id = result["output"]["voice"]

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

    print("=" * 55)
    print("Qwen3-TTS 여성 Voice Design 등록 (language=ko)")
    print("=" * 55)

    results = []
    for d in FEMALE_DESIGNS:
        r = design_female_voice(d)
        results.append(r)

    print("\n─── 결과 요약 ───────────────────────────────────────")
    for r in results:
        print(f"  {r['name']:22s}  voice_id: {r['voice_id']}")

    print("\n📌 다음 단계:")
    print("  1. vd_female_v1.wav, vd_female_v2.wav 재생 후 품질 평가")
    print("  2. 더 나은 버전의 voice_id를 gen_audio_qwen.py의 VD_FEMALE에 입력")
    print("  3. WorkLog 결과표 채우기 (품질 /5)")


if __name__ == "__main__":
    main()
