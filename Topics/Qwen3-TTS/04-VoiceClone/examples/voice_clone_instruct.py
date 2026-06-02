"""
voice_clone_instruct.py — Instructions 방식 목소리 튜닝 (다음 세션)

qwen3-tts-instruct-flash 모델에 목소리를 등록하고,
instructions 파라미터로 속도·톤·감정을 자연어로 제어한다.

실행:
    python voice_clone_instruct.py --sample samples/changsoo_sample.mp3
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

dashscope.base_http_api_url = "https://dashscope-intl.aliyuncs.com/api/v1"
ENROLL_URL    = "https://dashscope-intl.aliyuncs.com/api/v1/services/audio/tts/customization"
INSTRUCT_MODEL = "qwen3-tts-instruct-flash-2026-01-26"
# instruct 모델은 enrollment target으로 미지원 → M3에서 발급받은 VC voice_id 재사용
VC_MODEL       = "qwen3-tts-vc-2026-01-22"
PREFERRED_NAME = "changsoo"
OUT_DIR        = Path(__file__).parent

CLONE_TEXT = (
    "안녕하세요, 여러분. 저는 창수입니다. "
    "오늘 AI in Action 라이브 방송에서 보이스 클론 기술을 직접 실험해 보고 있습니다. "
    "이 목소리가 제 목소리와 얼마나 비슷한지 들어보세요."
)

INSTRUCTION_VARIANTS = [
    {
        "label": "느리고 차분",
        "out": "tune_slow.wav",
        "instructions": "천천히, 또렷하게, 차분하고 신뢰감 있는 목소리로 말해주세요. 문장 사이에 충분한 여유를 두세요.",
    },
    {
        "label": "자연스러운 속도",
        "out": "tune_natural.wav",
        "instructions": "자연스럽고 편안한 속도로, 강조할 부분에서 살짝 천천히 말해주세요. 억양을 부드럽게 유지해주세요.",
    },
    {
        "label": "방송 톤",
        "out": "tune_broadcast.wav",
        "instructions": "방송 진행자처럼 명확하고 활기차게, 적당한 속도로 말해주세요. 자신감 있고 친근한 톤으로 해주세요.",
    },
]


def enroll_voice_vc(sample_path: str) -> str:
    """VC 모델로 등록 (instruct 모델은 enrollment 미지원)."""
    path = Path(sample_path)
    mime = "audio/mpeg" if path.suffix.lower() == ".mp3" else "audio/wav"
    b64  = base64.b64encode(path.read_bytes()).decode()

    payload = {
        "model": "qwen-voice-enrollment",
        "input": {
            "action": "create",
            "target_model": VC_MODEL,
            "preferred_name": PREFERRED_NAME,
            "audio": {"data": f"data:{mime};base64,{b64}"},
        },
    }
    headers = {
        "Authorization": f"Bearer {os.environ['DASHSCOPE_API_KEY']}",
        "Content-Type": "application/json",
    }

    print(f"[등록] {path.name} → target_model: {VC_MODEL}")
    t = time.time()
    resp = requests.post(ENROLL_URL, json=payload, headers=headers, timeout=60)
    elapsed = round(time.time() - t, 2)

    if resp.status_code != 200:
        raise RuntimeError(f"등록 실패 {resp.status_code}: {resp.text}")

    voice_id = resp.json()["output"]["voice"]
    print(f"  ✅ voice_id: {voice_id}  ({elapsed}s)\n")
    return voice_id


def synthesize_with_instructions(voice_id: str, instructions: str, out_name: str) -> dict:
    print(f"  instructions: {instructions[:50]}...")
    t = time.time()
    response = dashscope.MultiModalConversation.call(
        model=INSTRUCT_MODEL,
        api_key=os.environ["DASHSCOPE_API_KEY"],
        text=CLONE_TEXT,
        voice=voice_id,
        instructions=instructions,
        stream=False,
    )
    elapsed = round(time.time() - t, 2)

    if response.status_code != 200:
        raise RuntimeError(f"합성 실패 {response.status_code}: {response.message}")

    out_path = OUT_DIR / out_name
    urllib.request.urlretrieve(response.output.audio.url, str(out_path))
    size_kb = round(out_path.stat().st_size / 1024, 1)
    print(f"  ✅ 저장: {out_name} ({size_kb} KB)  ({elapsed}s)")
    return {"elapsed": elapsed, "size_kb": size_kb, "path": out_path}


def main():
    parser = argparse.ArgumentParser()
    # --sample: 새 등록용 mp3. --voice-id: 기존 voice_id 직접 지정 (재등록 불필요)
    parser.add_argument("--sample", default=None)
    parser.add_argument("--voice-id", default=None,
                        help="기존 VC voice_id 직접 지정 (등록 생략)")
    args = parser.parse_args()

    if not os.environ.get("DASHSCOPE_API_KEY"):
        raise EnvironmentError("DASHSCOPE_API_KEY 환경변수가 설정되지 않았습니다.")

    print("=" * 55)
    print("Qwen3-TTS Voice Clone + Instructions 튜닝")
    print("=" * 55 + "\n")

    if args.voice_id:
        voice_id = args.voice_id
        print(f"[기존 voice_id 사용] {voice_id}\n")
    elif args.sample:
        voice_id = enroll_voice_vc(args.sample)
    else:
        raise ValueError("--sample 또는 --voice-id 중 하나를 지정해야 합니다.")

    print(f"3종 instructions 비교 실험")
    print(f"  합성 모델: {INSTRUCT_MODEL}")
    print(f"  voice_id : {voice_id}\n")
    for v in INSTRUCTION_VARIANTS:
        print(f"[{v['label']}]")
        synthesize_with_instructions(voice_id, v["instructions"], v["out"])

    print(f"\n완료! 각 파일을 재생하고 가장 마음에 드는 버전을 선택하세요.")
    print(f"voice_id: {voice_id}")


if __name__ == "__main__":
    main()
