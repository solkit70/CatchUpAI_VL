#!/usr/bin/env python3
"""M4 실습 1/3 — openWakeWord 호출어 감지 프로브.

사전학습 모델(alexa / hey_jarvis / hey_mycroft 등)로 감지·지연·오탐을 측정한다.
한국어 커스텀 호출어("코엠씨")는 별도 학습이 필요하므로, 이 프로브는 방법론·하네스를
검증하고 오탐률로 "wake word vs 핫키" 결정을 돕는 것이 목적. (concepts/wake-vad-concepts.md)

모드:
  record   : N초 녹음 → WAV 저장 → 오프라인 프레임 채점(권장, 결정론적). 실습 1에 사용.
  detect   : 실시간 스트림 감지(사용자가 직접 터미널에서 실행해 라이브 피드백을 볼 때).
  falsepos : 실시간 스트림으로 오탐만 기록. 실습 3(30분 배경 녹음).

  ※ 백그라운드 실행 시 stdout 버퍼링으로 라이브 피드백이 안 보이므로, 배경 실행에는
    record 모드(고정 창)를 쓴다. 감지 이벤트는 probe_log.jsonl에 append.

사용법:
  python wake_probe.py --list-devices
  python wake_probe.py --mode record   --seconds 120 --device 1      # 실습 1
  python wake_probe.py --mode detect   --seconds 60  --device 1      # 라이브(직접 실행)
  python wake_probe.py --mode falsepos --seconds 1800 --device 1     # 실습 3
"""
import argparse, json, sys, time
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

import numpy as np
import sounddevice as sd

SR = 16000            # openWakeWord 고정 샘플레이트
FRAME = 1280          # 80ms 프레임(권장)
COOLDOWN_S = 1.0      # 같은 발화 중복 카운트 방지
LOG = Path(__file__).parent / "probe_log.jsonl"
DEFAULT_MODELS = ["hey_jarvis", "alexa", "hey_mycroft"]


def log(rec: dict):
    rec["logged_at"] = time.strftime("%Y-%m-%dT%H:%M:%S")
    with LOG.open("a", encoding="utf-8") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")


def list_devices():
    print("=== 입력 장치 (max_input_channels>0) ===")
    for i, d in enumerate(sd.query_devices()):
        if d["max_input_channels"] > 0:
            print(f"  [{i}] {d['name']}  ({d['max_input_channels']}ch, {int(d['default_samplerate'])}Hz)")


def resolve_device(spec):
    """장치 번호 또는 이름 일부를 실제 인덱스로 해석한다.

    ⚠ 이 환경에서 인덱스는 불안정하다. USB 마이크를 옮기거나 재열거될 때마다 밀리며,
      같은 세션에서 연속 조회해도 달라졌다(2026-08-15: MV7 이 1→22→3→1).
      30분짜리 측정을 엉뚱한 마이크로 날리지 않도록 이름으로 지정한다.
    """
    if spec is None:
        return None
    if isinstance(spec, int) or str(spec).isdigit():
        return int(spec)
    want = str(spec).lower()
    for i, d in enumerate(sd.query_devices()):
        if d["max_input_channels"] < 1 or want not in d["name"].lower():
            continue
        try:
            sd.check_input_settings(device=i, samplerate=SR, channels=1, dtype="int16")
        except Exception:
            continue
        print(f"  [장치] '{spec}' → [{i}] {d['name']}")
        return i
    raise SystemExit(f"'{spec}' 에 맞는 입력 장치를 {SR}Hz 로 열 수 없습니다. --list-devices 로 확인하세요.")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=["record", "detect", "falsepos", "file"],
                    default="record")
    ap.add_argument("--audio", help="mode=file 일 때 채점할 오디오/영상 파일 (ffmpeg 디코드)")
    ap.add_argument("--seconds", type=float, default=120.0)
    ap.add_argument("--device", default=None,
                    help="입력 장치 번호 또는 이름 일부(예: MV7). 인덱스가 불안정하므로 이름 권장")
    ap.add_argument("--models", nargs="+", default=DEFAULT_MODELS)
    ap.add_argument("--threshold", type=float, default=0.5)
    ap.add_argument("--list-devices", action="store_true")
    args = ap.parse_args()

    if args.list_devices:
        list_devices(); return 0

    args.device = resolve_device(args.device)   # 스트림 열기 직전에 해석

    # record 모드는 모델 로드 전에 녹음부터 시작해야 초반 발화가 유실되지 않는다.
    prerecorded = None
    if args.mode == "record":
        print(f"[mode=record] 지금부터 {args.seconds:.0f}초 녹음합니다. "
              f"후보 호출어를 또박또박 발화하세요. (device={args.device})", flush=True)
        prerecorded = sd.rec(int(args.seconds * SR), samplerate=SR, channels=1,
                             dtype="int16", device=args.device)
        sd.wait()
        prerecorded = prerecorded[:, 0]

    from openwakeword.model import Model
    from openwakeword.utils import download_models
    download_models()
    # Model()은 wakeword_models 리스트를 전체 경로로 in-place 변형한다.
    # predict()가 반환하는 키는 짧은 이름이므로 oww.models에서 키를 가져온다.
    oww = Model(wakeword_models=list(args.models), inference_framework="onnx")
    model_names = list(oww.models.keys())

    counts = {m: 0 for m in model_names}
    cooldown_until = {m: 0.0 for m in model_names}
    proc_ms_samples = []

    def process_frame(frame_i16: np.ndarray, clock: float):
        """한 프레임 채점 + 감지 카운트/로그. clock은 초 단위(실시간=wall, 오프라인=가상)."""
        t0 = time.perf_counter()
        scores = oww.predict(frame_i16)
        proc_ms_samples.append((time.perf_counter() - t0) * 1000)
        for m, s in scores.items():
            if s >= args.threshold and clock >= cooldown_until[m]:
                counts[m] += 1
                cooldown_until[m] = clock + COOLDOWN_S
                log({"event": "wake", "mode": args.mode, "model": m,
                     "score": round(float(s), 3), "clock_s": round(clock, 2)})
                tag = "⚠️오탐" if args.mode in ("falsepos", "file") else "감지"
                print(f"  {tag}  {m:14} score={s:.3f}  @{clock:6.2f}s")

    print(f"[mode={args.mode}] models={model_names} thr={args.threshold} "
          f"seconds={args.seconds} device={args.device}")

    if args.mode == "record":
        # 미리 녹음한 창을 오프라인 채점 (결정론적, 백그라운드 실행에 적합)
        audio = prerecorded
        try:
            import soundfile as sf
            wav = Path(__file__).parent / "wake_record.wav"
            sf.write(str(wav), audio, SR)
        except Exception:
            wav = None
        peak = int(np.abs(audio).max())
        print(f"[레벨] peak={peak}/32767 ({peak/32767*100:.1f}pct)"
              + (f"  → {wav.name} 저장" if wav else ""))
        # 가상 시계로 프레임별 오프라인 채점
        for i in range(0, len(audio) - FRAME, FRAME):
            process_frame(audio[i:i + FRAME], clock=i / SR)
    elif args.mode == "file":
        # ── 파일 오프라인 채점 (M4 이월 과제, 2026-09-06 추가) ──────────────
        #
        # M4 실습 3은 30분 배경 녹음으로 오탐 0회를 재고 **3시간으로 환산**했다.
        # 환산은 측정이 아니다 — 30분에 안 나온 것이 3시간에도 안 나온다는 보장은 없다.
        # 그래서 README 가 *"실측 오탐률 확보"* 를 이월로 남겼다.
        #
        # 마이크로는 실측할 수 없다. 3시간을 실시간으로 앉아 있어야 하고,
        # 그렇게 재도 매번 다른 소리라 재현이 안 된다. **파일이어야 결정적이다.**
        #
        # 전체를 메모리에 올리지 않고 ffmpeg 파이프에서 프레임 단위로 흘린다 —
        # 3시간 16kHz mono int16 은 약 345MB 라 올려도 되지만, 더 긴 소스에서도
        # 같은 코드가 돌아야 한다.
        import subprocess
        src = Path(args.audio)
        if not src.exists():
            print(f"파일 없음: {src}", file=sys.stderr)
            return 1
        cmd = ["ffmpeg", "-v", "error", "-i", str(src),
               "-f", "s16le", "-acodec", "pcm_s16le",
               "-ar", str(SR), "-ac", "1", "-"]
        print(f"[file] {src.name} 디코드 시작 (16kHz mono)")
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                                stderr=subprocess.DEVNULL)
        nbytes = FRAME * 2                      # int16
        n_frames, peak = 0, 0
        t_start = time.perf_counter()
        while True:
            buf = proc.stdout.read(nbytes)
            if len(buf) < nbytes:
                break
            frame = np.frombuffer(buf, dtype=np.int16)
            peak = max(peak, int(np.abs(frame).max()))
            process_frame(frame, clock=n_frames * FRAME / SR)
            n_frames += 1
            if n_frames % 4500 == 0:            # 약 6분마다
                mins = n_frames * FRAME / SR / 60
                print(f"    …{mins:.0f}분 채점 · 누적 감지 {sum(counts.values())}회",
                      flush=True)
        proc.stdout.close()
        proc.wait()
        args.seconds = n_frames * FRAME / SR    # 요약의 환산 분모를 실제 길이로
        wall = time.perf_counter() - t_start
        print(f"[file] {args.seconds/60:.1f}분 채점 완료 "
              f"(소요 {wall/60:.1f}분 · {args.seconds/max(wall,1e-9):.0f}x 실시간) "
              f"peak={peak}/32767")
    else:
        # 실시간 스트림 (직접 터미널 실행 권장 — 라이브 피드백)
        if args.mode == "detect":
            print("→ 각 후보 호출어를 또박또박 10회씩 발화하세요.")
        else:
            print("→ 일반 작업(타이핑·잡담·배경음악)을 하세요. 감지=오탐입니다.")
        t_end = time.time() + args.seconds
        with sd.InputStream(samplerate=SR, channels=1, dtype="int16",
                            blocksize=FRAME, device=args.device) as stream:
            while time.time() < t_end:
                data, _ = stream.read(FRAME)
                process_frame(data[:, 0], clock=time.time())

    avg_proc = sum(proc_ms_samples) / max(1, len(proc_ms_samples))
    print("\n=== 요약 ===")
    for m in model_names:
        print(f"  {m:16} 감지 {counts[m]}회")
    print(f"  평균 프레임 처리시간 {avg_proc:.2f}ms (80ms 프레임 대비 실시간 여유)")
    if args.mode in ("falsepos", "file"):
        ratio3h = {m: round(counts[m] * (3 * 3600 / args.seconds), 1) for m in model_names}
        print("  3시간 환산 오탐:", ratio3h)
    log({"event": "summary", "mode": args.mode, "seconds": args.seconds,
         "counts": counts, "avg_proc_ms": round(avg_proc, 2)})
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
