#!/usr/bin/env python3
"""M4 진단 — 마이크 캡처 + openWakeWord 오프라인 감지 점검.

실시간 타이밍 변수를 제거하기 위해: N초 녹음 → WAV 저장 → 레벨(peak/RMS) 출력 →
저장한 오디오를 openWakeWord로 오프라인 재생하며 모델별 최고 점수를 본다.
오프라인에서 점수가 뜨면 파이프라인 정상(실시간 0회는 타이밍/레벨), 안 뜨면 캡처/피딩 문제.

사용법:  python mic_check.py --seconds 8 --device 1
"""
import argparse, sys, time
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

import numpy as np
import sounddevice as sd
import soundfile as sf

SR = 16000
FRAME = 1280
OUT_WAV = Path(__file__).parent / "mic_check.wav"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seconds", type=float, default=8.0)
    ap.add_argument("--device", type=int, default=None)
    ap.add_argument("--models", nargs="+", default=["hey_jarvis", "alexa", "hey_mycroft"])
    args = ap.parse_args()

    print(f"[녹음] {args.seconds}s @ device={args.device}  — 지금 'alexa'를 5회 정도 말하세요.")
    audio = sd.rec(int(args.seconds * SR), samplerate=SR, channels=1,
                   dtype="int16", device=args.device)
    sd.wait()
    audio = audio[:, 0]
    sf.write(str(OUT_WAV), audio, SR)

    peak = int(np.abs(audio).max())
    rms = float(np.sqrt(np.mean((audio.astype(np.float32)) ** 2)))
    print(f"[레벨] peak={peak}/32767 ({peak/32767*100:.1f}%)  rms={rms:.0f}  → {OUT_WAV.name} 저장")
    if peak < 500:
        print("  ⚠️ 레벨이 매우 낮음 — 마이크가 소리를 거의 못 받고 있습니다(장치 번호/음소거 확인).")

    print("[오프라인 감지] 저장 오디오를 openWakeWord로 재생...")
    from openwakeword.model import Model
    from openwakeword.utils import download_models
    download_models()
    oww = Model(wakeword_models=list(args.models), inference_framework="onnx")
    names = list(oww.models.keys())
    best = {n: 0.0 for n in names}
    for i in range(0, len(audio) - FRAME, FRAME):
        scores = oww.predict(audio[i:i + FRAME])
        for n, s in scores.items():
            best[n] = max(best[n], float(s))
    print("  모델별 최고 점수:")
    for n in names:
        flag = "  ✅ 감지됨(>0.5)" if best[n] >= 0.5 else ""
        print(f"    {n:14} {best[n]:.3f}{flag}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
