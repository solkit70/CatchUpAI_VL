#!/usr/bin/env python3
"""M4 실습 2 — Silero VAD 발화 구간/종료 프로브 (ONNX 직구동).

torch/torchaudio를 우회하고 silero_vad.onnx를 onnxruntime로 직접 돌린다
(이 PC는 GPU 없음 + torchaudio DLL 로드 실패). 마이크 발화의 시작·종료를
800ms 무음 기준으로 판정하고, 육안 판단과의 오차를 눈으로 비교할 수 있게 로그한다.

사용법:
  python vad_probe.py --seconds 30 --device 1
  python vad_probe.py --seconds 30 --device 1 --silence-ms 800 --threshold 0.5

발화 종료 이벤트는 probe_log.jsonl에 append. 콘솔에 시작/종료 실시간 라인 출력.
"""
import argparse, json, sys, time
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

import numpy as np
import onnxruntime as ort
import sounddevice as sd

SR = 16000
FRAME = 512  # Silero VAD 16kHz 권장 프레임(32ms)
LOG = Path(__file__).parent / "probe_log.jsonl"
VAD_ONNX = Path(r"C:/Users/dougg/AppData/Roaming/Python/Python313/site-packages/silero_vad/data/silero_vad.onnx")


CONTEXT = 64  # Silero VAD v5 16kHz: 512샘플 프레임 앞에 64샘플 context를 prepend(총 576)


class SileroVAD:
    """silero_vad.onnx 상태 유지 래퍼. 512샘플 float32 프레임 → speech 확률.

    ⚠️ 공식 OnnxWrapper와 동일하게 context 64샘플을 prepend해야 한다.
    (512만 넣으면 모델이 에러 없이 항상 ~0을 반환한다 — 실측으로 확인한 함정)
    """
    def __init__(self, model_path: Path):
        self.sess = ort.InferenceSession(str(model_path), providers=["CPUExecutionProvider"])
        self.reset()

    def reset(self):
        self._state = np.zeros((2, 1, 128), dtype=np.float32)
        self._context = np.zeros((1, CONTEXT), dtype=np.float32)

    def __call__(self, frame_f32: np.ndarray) -> float:
        x = np.concatenate([self._context, frame_f32.reshape(1, -1)], axis=1).astype(np.float32)
        out, self._state = self.sess.run(
            ["output", "stateN"],
            {"input": x, "state": self._state, "sr": np.array(SR, dtype=np.int64)},
        )
        self._context = x[:, -CONTEXT:]
        return float(out[0, 0])


def log(rec: dict):
    rec["logged_at"] = time.strftime("%Y-%m-%dT%H:%M:%S")
    with LOG.open("a", encoding="utf-8") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")


def segment(frames_iter, vad, threshold, silence_ms, frame_ms):
    """(clock_s, prob) 프레임 스트림 → 발화 구간 리스트. clock은 초 단위."""
    silence_frames_needed = max(1, round(silence_ms / frame_ms))
    utterances, speaking, start_t, silence_run = [], False, None, 0
    for clock, prob in frames_iter:
        if prob >= threshold:
            silence_run = 0
            if not speaking:
                speaking, start_t = True, clock
                print(f"  [{clock:6.2f}s] 발화 시작  (prob={prob:.2f})")
        elif speaking:
            silence_run += 1
            if silence_run >= silence_frames_needed:
                end_t = clock - silence_ms / 1000  # 마지막 발화 프레임 = 실제 종료
                dur = end_t - start_t
                print(f"  [{end_t:6.2f}s] 발화 종료  (길이 {dur:.2f}s, 무음 {silence_ms}ms 확인 후 확정)")
                rec = {"event": "utterance", "start_s": round(start_t, 2),
                       "end_s": round(end_t, 2), "duration_s": round(dur, 2),
                       "silence_ms": silence_ms, "threshold": threshold}
                log(rec); utterances.append(rec)
                speaking, silence_run = False, 0
    return utterances


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=["record", "stream"], default="record")
    ap.add_argument("--seconds", type=float, default=30.0)
    ap.add_argument("--device", type=int, default=None)
    ap.add_argument("--threshold", type=float, default=0.5, help="speech 확률 임계값")
    ap.add_argument("--silence-ms", type=int, default=800, help="발화 종료로 판정할 무음 지속(ms)")
    args = ap.parse_args()

    if not VAD_ONNX.exists():
        print("ERROR: silero_vad.onnx를 찾을 수 없습니다:", VAD_ONNX); return 1

    frame_ms = FRAME / SR * 1000  # 32ms
    print(f"[VAD mode={args.mode}] thr={args.threshold} silence={args.silence_ms}ms "
          f"seconds={args.seconds} device={args.device}")
    print("→ 짧은 발화('3부 시작')와 긴 발화(5문장 질문)를 각각 해보세요.\n")

    vad = SileroVAD(VAD_ONNX)

    if args.mode == "record":
        # 실행 즉시 녹음 → 오프라인 구간 검출(결정론적, 백그라운드 실행에 적합)
        audio = sd.rec(int(args.seconds * SR), samplerate=SR, channels=1,
                       dtype="int16", device=args.device)
        sd.wait()
        audio = audio[:, 0]
        try:
            import soundfile as sf
            sf.write(str(Path(__file__).parent / "vad_record.wav"), audio, SR)
        except Exception:
            pass
        peak = int(np.abs(audio).max())
        print(f"[레벨] peak={peak}/32767 ({peak/32767*100:.1f}pct)")

        def offline_frames():
            for i in range(0, len(audio) - FRAME, FRAME):
                f = audio[i:i + FRAME].astype(np.float32) / 32768.0
                yield (i / SR, vad(f))
        utts = segment(offline_frames(), vad, args.threshold, args.silence_ms, frame_ms)
    else:
        t_start = time.time()
        def live_frames():
            with sd.InputStream(samplerate=SR, channels=1, dtype="int16",
                                blocksize=FRAME, device=args.device) as stream:
                while time.time() < t_start + args.seconds:
                    data, _ = stream.read(FRAME)
                    f = data[:, 0].astype(np.float32) / 32768.0
                    yield (time.time() - t_start, vad(f))
        utts = segment(live_frames(), vad, args.threshold, args.silence_ms, frame_ms)

    print(f"\n=== 요약 === 발화 {len(utts)}개 검출")
    for k, u in enumerate(utts, 1):
        print(f"  발화{k}: {u['start_s']:.2f}s → {u['end_s']:.2f}s  (길이 {u['duration_s']:.2f}s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
