"""
hello_qwen.py — Qwen3-TTS DashScope Intl API 첫 합성 테스트 (M2)

목적: qwen3-tts-flash 모델로 한국어/영어 mp3를 생성하고
     응답 시간(Latency)을 측정한다.

참고: OpenAI 호환 모드(/compatible-mode/v1)는 TTS 미지원 — LLM 전용.
     TTS는 반드시 DashScope 네이티브 SDK를 사용해야 한다.

실행:
    python hello_qwen.py

완료 신호:
    hello_ko.wav / hello_en.wav 생성 + 재생 확인
"""

import os
import time
import urllib.request
from pathlib import Path

import dashscope

# ── 설정 ──────────────────────────────────────────────────────────────────
dashscope.base_http_api_url = "https://dashscope-intl.aliyuncs.com/api/v1"
MODEL   = "qwen3-tts-flash"
OUT_DIR = Path(__file__).parent

SAMPLES = [
    {
        "text": "안녕하세요. 저는 큐원 삼 티티에스입니다. 다섯 주차 방송에서 여러분과 함께 음성 합성을 테스트하고 있습니다.",
        "voice": "Cherry",
        "language_type": "Korean",
        "out": "hello_ko.wav",
        "label": "Korean",
    },
    {
        "text": "Hello. This is Qwen3-TTS first synthesis test. Testing the DashScope International API from Seattle.",
        "voice": "Cherry",
        "language_type": "English",
        "out": "hello_en.wav",
        "label": "English",
    },
]

# ── 실행 ──────────────────────────────────────────────────────────────────
def synthesize(sample: dict) -> dict:
    t_start = time.time()
    response = dashscope.MultiModalConversation.call(
        model=MODEL,
        api_key=os.environ["DASHSCOPE_API_KEY"],
        text=sample["text"],
        voice=sample["voice"],
        language_type=sample["language_type"],
        stream=False,
    )
    elapsed = round(time.time() - t_start, 2)

    if response.status_code != 200:
        raise RuntimeError(f"API 오류 {response.status_code}: {response.message}")

    audio_url = response.output.audio.url
    out_path = OUT_DIR / sample["out"]
    urllib.request.urlretrieve(audio_url, str(out_path))

    size_kb = round(out_path.stat().st_size / 1024, 1)
    return {"path": out_path, "elapsed": elapsed, "size_kb": size_kb, "url": audio_url}


def main():
    if not os.environ.get("DASHSCOPE_API_KEY"):
        raise EnvironmentError("DASHSCOPE_API_KEY 환경변수가 설정되지 않았습니다.")

    print(f"모델: {MODEL}")
    print(f"엔드포인트: {dashscope.base_http_api_url}\n")

    for s in SAMPLES:
        print(f"[{s['label']}] 합성 시작...")
        print(f"  텍스트: {s['text'][:45]}...")
        result = synthesize(s)
        print(f"  ✅ 저장: {result['path'].name} ({result['size_kb']} KB)")
        print(f"  ⏱  응답 시간: {result['elapsed']}s\n")

    print("완료! 생성된 파일:")
    for s in SAMPLES:
        print(f"  {OUT_DIR / s['out']}")


if __name__ == "__main__":
    main()
