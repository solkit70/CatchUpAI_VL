#!/usr/bin/env python3
"""M4 실습 4 — 에코 루프 차단 프로브 (wake_gate 검증).

TTS가 자기 음성을 마이크로 다시 들어 호출어로 오인하는 에코 루프를,
M3에서 정의한 session_state 계약의 `wake_gate: open|closed`로 차단하는지 실측한다.

핵심 설계 — 게이트가 "실제로 일한다"는 것을 증명하려면 끈 경우도 측정해야 한다:
  --gate off : 게이트 없이 측정. TTS 재생 중 감지가 나와야 에코 루프가 실재함이 증명된다.
  --gate on  : 게이트 적용. 같은 조건에서 감지 0건이어야 차단 성공.
off에서 0건이 나오면 그건 차단 성공이 아니라 **스피커 소리가 마이크에 안 닿은 것**이므로
실험이 무효다. 이 경우 출력을 헤드폰이 아닌 스피커로 바꿔야 한다.

모드:
  echo   : TTS 재생 + 동시 마이크 캡처 → 재생 구간 감지/억제 카운트
  reopen : 재생 종료 후 게이트 재개방 지연 측정 (500ms 이내가 목표)
  level  : 입력 장치 레벨만 빠르게 확인 (장치 번호가 세션마다 바뀌므로 먼저 확인)

사용법:
  python echo_probe.py --list-devices
  python echo_probe.py --make-tts
  python echo_probe.py --mode level  --device 1 --seconds 5
  python echo_probe.py --mode echo   --gate off --device 1 --output-device 6
  python echo_probe.py --mode echo   --gate on  --device 1 --output-device 6
  python echo_probe.py --mode reopen --device 1 --output-device 6
"""
import argparse, json, sys, time
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

import numpy as np
import sounddevice as sd

SR = 16000
FRAME = 1280            # 80ms — wake_probe.py와 동일
COOLDOWN_S = 1.0
HANGOVER_MS = 200       # 재생 종료 후 게이트를 더 닫아 두는 시간(잔향·버퍼 지연 흡수)
HERE = Path(__file__).parent
LOG = HERE / "probe_log.jsonl"
TTS_WAV = HERE / "tts_wake.wav"
DEFAULT_MODEL = "alexa"  # 실습 1에서 채택 (10/10, 교차 오탐 0)

# 호출어를 문장 안에 넣어야 실제 방송 상황(TTS가 말하다가 호출어를 발음)에 가깝다.
TTS_TEXT = ("자, 다음 순서로 넘어가겠습니다. "
            "이때 진행자가 알렉사, alexa 라고 부르면 어떻게 될까요? "
            "바로 이 상황이 에코 루프입니다.")
TTS_VOICE = "ko-KR-SunHiNeural"


def log(rec: dict):
    rec["logged_at"] = time.strftime("%Y-%m-%dT%H:%M:%S")
    with LOG.open("a", encoding="utf-8") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")


def resolve_device(spec, kind: str) -> int | None:
    """장치 지정을 실제 인덱스로 해석한다. 숫자면 그대로, 문자열이면 이름으로 검색.

    ⚠ 이 환경에서 장치 인덱스는 매우 불안정하다. USB 마이크를 옮기거나 재열거될 때마다
      밀리고, 같은 세션 안에서 두 번 조회해도 달라졌다(2026-08-15: MV7 이 1→22→3).
      번호를 하드코딩한 측정은 조용히 엉뚱한 마이크를 쓰게 되므로 이름으로 지정한다.
      16kHz 를 못 여는 호스트 API 변형(WASAPI 등)은 건너뛴다.
    """
    if spec is None:
        return None
    if isinstance(spec, int) or str(spec).isdigit():
        return int(spec)

    want = str(spec).lower()
    ch_key = "max_input_channels" if kind == "input" else "max_output_channels"
    matches = []
    for i, d in enumerate(sd.query_devices()):
        if d[ch_key] < 1 or want not in d["name"].lower():
            continue
        try:
            if kind == "input":
                sd.check_input_settings(device=i, samplerate=SR, channels=1, dtype="int16")
            else:
                sd.check_output_settings(device=i, samplerate=SR, channels=1, dtype="float32")
        except Exception:
            continue
        matches.append((i, d["name"]))
    if not matches:
        sys.exit(f"'{spec}' 에 맞는 {kind} 장치를 {SR}Hz 로 열 수 없습니다. --list-devices 로 확인하세요.")
    idx, name = matches[0]
    print(f"  [장치] {kind}='{spec}' → [{idx}] {name}")
    return idx


def list_devices():
    devs = sd.query_devices()
    print("=== 입력 장치 ===")
    for i, d in enumerate(devs):
        if d["max_input_channels"] > 0:
            print(f"  [{i}] {d['name'][:55]} ({d['max_input_channels']}ch)")
    print("\n=== 출력 장치 ===")
    for i, d in enumerate(devs):
        if d["max_output_channels"] > 0:
            print(f"  [{i}] {d['name'][:55]} ({d['max_output_channels']}ch)")
    print(f"\n기본 입출력: {sd.default.device}")
    print("\n⚠ 에코 테스트는 반드시 **스피커** 출력을 써야 한다. 헤드폰/이어버드로 내보내면\n"
          "  마이크가 TTS를 못 들어 --gate off 에서도 0건이 나오고 실험이 무효가 된다.")


def make_tts():
    """edge-tts로 호출어가 포함된 문장을 합성해 16k mono wav로 저장."""
    import asyncio, subprocess, shutil
    import edge_tts

    mp3 = HERE / "_tts_tmp.mp3"

    async def _run():
        await edge_tts.Communicate(TTS_TEXT, TTS_VOICE).save(str(mp3))

    asyncio.run(_run())

    ffmpeg = shutil.which("ffmpeg") or "ffmpeg"
    subprocess.run([ffmpeg, "-hide_banner", "-loglevel", "error", "-y",
                    "-i", str(mp3), "-ar", str(SR), "-ac", "1", str(TTS_WAV)], check=True)
    mp3.unlink(missing_ok=True)

    import soundfile as sf
    data, sr = sf.read(str(TTS_WAV))
    print(f"✓ TTS 생성: {TTS_WAV.name}  {len(data)/sr:.1f}s @ {sr}Hz")
    print(f"  문장: {TTS_TEXT}")


def load_tts():
    import soundfile as sf
    if not TTS_WAV.exists():
        sys.exit(f"{TTS_WAV.name} 이 없습니다. 먼저 --make-tts 를 실행하세요.")
    data, sr = sf.read(str(TTS_WAV), dtype="float32")
    if sr != SR:
        sys.exit(f"TTS 샘플레이트가 {sr}. --make-tts 로 다시 만드세요.")
    return data


def build_model(model_name: str):
    from openwakeword.model import Model
    from openwakeword.utils import download_models
    download_models()
    # Model()이 리스트를 전체 경로로 in-place 변형하므로 키는 oww.models 에서 얻는다 (M4 문제 1).
    oww = Model(wakeword_models=[model_name], inference_framework="onnx")
    return oww, list(oww.models.keys())[0]


BEEP_HZ = 1000.0
BEEP_S = 0.25
BEEP_GAP_S = 0.25       # 비프와 TTS 사이 간격


def make_beep() -> np.ndarray:
    t = np.arange(int(BEEP_S * SR)) / SR
    tone = 0.6 * np.sin(2 * np.pi * BEEP_HZ * t).astype(np.float32)
    # 클릭 방지용 페이드
    fade = int(0.01 * SR)
    tone[:fade] *= np.linspace(0, 1, fade)
    tone[-fade:] *= np.linspace(1, 0, fade)
    return np.concatenate([tone, np.zeros(int(BEEP_GAP_S * SR), dtype=np.float32)])


def align_by_beep(recorded_i16: np.ndarray) -> tuple[float, float]:
    """녹음본에서 1kHz 비프를 찾아 TTS 시작 시각(초)과 검출 강도를 돌려준다.

    sd.play() 의 출력 장치 오픈 지연은 수 초까지 벌어지고(2026-08-15 측정 ~4.2s),
    스피커→마이크 경로를 거친 TTS는 포락선 상관으로 정렬하기엔 너무 조용하다.
    좁은 대역의 비프는 잡음 속에서도 뾰족하게 검출되므로 정렬이 결정론적이다.
    """
    x = recorded_i16.astype(np.float32)
    win = int(0.05 * SR)                       # 50ms 슬라이딩
    hop = int(0.01 * SR)                       # 10ms 해상도
    n = np.arange(win)
    ref_c = np.cos(2 * np.pi * BEEP_HZ * n / SR)
    ref_s = np.sin(2 * np.pi * BEEP_HZ * n / SR)
    best_v, best_i = 0.0, 0
    goertzel = []
    for i in range(0, len(x) - win, hop):
        seg = x[i:i + win]
        e = np.sqrt((seg ** 2).mean()) + 1e-9
        mag = np.hypot((seg * ref_c).mean(), (seg * ref_s).mean()) / e   # 정규화 톤 비율
        goertzel.append(mag)
        if mag > best_v:
            best_v, best_i = mag, i
    med = float(np.median(goertzel)) if goertzel else 0.0
    beep_start = best_i / SR
    return beep_start + BEEP_S + BEEP_GAP_S, best_v / (med + 1e-9)


def run_echo(args):
    audio = load_tts()
    dur = len(audio) / SR
    oww, key = build_model(args.model)
    gate_on = args.gate == "on"

    print(f"[mode=echo gate={args.gate}] model={key} thr={args.threshold}")
    print(f"  TTS {dur:.1f}s 를 출력장치 {args.output_device} 로 재생하면서 "
          f"입력장치 {args.device} 로 고정 창 녹음합니다.")
    if not gate_on:
        print("  → 기준선 측정: 여기서 감지가 나와야 에코 루프가 실재함이 증명됩니다.")
    else:
        print("  → 게이트 적용: 재생 구간 감지 0건이 목표입니다.")

    # 고정 창 녹음 → 오프라인 채점 (M4 실습 1·2에서 확립한 결정론적 패턴)
    #
    # ⚠ sd.rec() + sd.play() 를 함께 쓰면 안 된다. 두 편의 함수는 모듈 레벨 스트림
    #   하나를 공유하므로 play() 가 진행 중인 rec() 을 중단시켜, 녹음본이 재생 시작
    #   시점의 클릭만 담긴 무음이 된다(2026-08-15 실측으로 확인).
    #   → 입력은 명시적 InputStream(콜백), 출력만 sd.play() 로 분리한다.
    captured_chunks: list[np.ndarray] = []

    def on_audio(indata, frames, time_info, status):
        captured_chunks.append(indata[:, 0].copy())

    beep = make_beep()
    playback = np.concatenate([beep, audio])   # 비프 → 간격 → TTS

    stream = sd.InputStream(samplerate=SR, channels=1, dtype="int16",
                            blocksize=FRAME, device=args.device, callback=on_audio)
    stream.start()
    time.sleep(args.lead)                      # 녹음이 먼저 흐르도록 여유
    sd.play(playback, SR, device=args.output_device)
    # 출력 장치 오픈 지연이 수 초까지 벌어지므로 넉넉히 관측한다.
    time.sleep(len(playback) / SR + args.tail + args.open_latency)
    sd.stop()
    stream.stop(); stream.close()
    captured = np.concatenate(captured_chunks) if captured_chunks else np.zeros(1, dtype=np.int16)

    peak = int(np.abs(captured).max())
    t_start, snr = align_by_beep(captured)     # 녹음 타임라인 기준 TTS 시작 시각
    print(f"  [정렬] 비프 검출 → TTS 시작 = {t_start:.2f}s (톤/잡음비 {snr:.1f}x)")
    if snr < 3.0:
        print("  ⚠ 비프가 뚜렷하지 않습니다. 스피커 볼륨을 올리세요 — 정렬이 부정확할 수 있습니다.")

    try:
        import soundfile as sf
        sf.write(str(HERE / f"echo_{args.gate}.wav"), captured, SR)
    except Exception:
        pass

    emitted, suppressed = [], []
    cooldown_until = -1.0
    for i in range(0, len(captured) - FRAME, FRAME):
        clock = i / SR                          # 녹음 타임라인
        rel = clock - t_start                   # 재생 타임라인(0 = TTS 시작)
        score = float(oww.predict(captured[i:i + FRAME]).get(key, 0.0))
        if score < args.threshold or clock < cooldown_until:
            continue
        cooldown_until = clock + COOLDOWN_S
        playing = 0.0 <= rel <= dur
        gate_closed = gate_on and (0.0 <= rel <= dur + HANGOVER_MS / 1000.0)
        r = {"clock_s": round(clock, 2), "play_rel_s": round(rel, 2),
             "score": round(score, 3), "during_playback": playing}
        if gate_closed:
            suppressed.append(r)
            print(f"  🛡 억제  score={score:.3f} @재생{rel:5.2f}s (gate=closed)")
        else:
            emitted.append(r)
            mark = "⚠️에코" if playing else "감지"
            print(f"  {mark}  score={score:.3f} @재생{rel:5.2f}s (gate=open)")

    during = [r for r in emitted if r["during_playback"]]
    print("\n=== 결과 ===")
    print(f"  입력 peak      : {peak}/32767 ({peak/32767*100:.1f}%)")
    print(f"  재생 구간 감지 : {len(during)}건  ← gate={args.gate}")
    print(f"  억제(게이트)   : {len(suppressed)}건")
    print(f"  재생 후 감지   : {len(emitted) - len(during)}건")

    if peak < 500:
        print("\n  ⚠ 입력 레벨이 거의 0입니다. 마이크 장치 번호를 확인하세요(--mode level).")
    elif not gate_on and len(during) == 0:
        print("\n  ⚠ 기준선인데 감지 0건 — 스피커 소리가 마이크에 닿지 않았을 가능성이 큽니다.")
        print("    출력을 헤드폰이 아닌 스피커로 바꾸고 볼륨을 올린 뒤 다시 측정하세요.")
        print("    이 상태의 gate=on 결과는 '차단 성공'의 근거가 될 수 없습니다.")
    elif gate_on and len(during) == 0:
        print("\n  ✅ 재생 구간 wake 이벤트 0건 — 에코 루프 차단 확인")

    log({"event": "echo_test", "gate": args.gate, "model": key,
         "tts_seconds": round(dur, 2), "peak": peak,
         "detected_during_playback": len(during), "suppressed": len(suppressed),
         "after_playback": len(emitted) - len(during),
         "detections": emitted, "suppressed_detail": suppressed})
    return 0


def run_reopen(args):
    """재생 종료 후 게이트가 다시 열리기까지의 지연을 측정."""
    audio = load_tts()
    dur = len(audio) / SR
    oww, key = build_model(args.model)

    print(f"[mode=reopen] TTS {dur:.1f}s 재생 → 종료 직후 호출어를 발화하세요.")
    print(f"  게이트는 재생 종료 + {HANGOVER_MS}ms 후 열립니다. "
          f"열린 뒤 첫 감지까지의 지연을 측정합니다.")

    sd.play(audio, SR, device=args.output_device)
    t0 = time.time()
    gate_open_at = dur + HANGOVER_MS / 1000.0
    first_after = None
    announced = False

    with sd.InputStream(samplerate=SR, channels=1, dtype="int16",
                        blocksize=FRAME, device=args.device) as stream:
        while True:
            now = time.time() - t0
            if now >= dur + args.tail:
                break
            data, _ = stream.read(FRAME)
            if now >= gate_open_at and not announced:
                print(f"  🔓 게이트 open @{now:5.2f}s — 지금 호출어를 말하세요")
                announced = True
            if now < gate_open_at:
                continue
            score = float(oww.predict(data[:, 0]).get(key, 0.0))
            if score >= args.threshold and first_after is None:
                first_after = now
                print(f"  ✓ 감지 score={score:.3f} @{now:5.2f}s")
                break
    sd.stop()

    print("\n=== 결과 ===")
    print(f"  재생 종료      : {dur:.2f}s")
    print(f"  게이트 재개방  : {gate_open_at:.2f}s (hangover {HANGOVER_MS}ms)")
    reopen_ms = HANGOVER_MS
    print(f"  재개방 지연    : {reopen_ms}ms  {'✅ 500ms 이내' if reopen_ms <= 500 else '❌ 초과'}")
    if first_after is not None:
        print(f"  재개방 후 첫 감지: +{(first_after - gate_open_at)*1000:.0f}ms (게이트 정상 동작 확인)")
    else:
        print("  재개방 후 감지 없음 — 호출어 발화 타이밍을 놓쳤을 수 있습니다.")

    log({"event": "gate_reopen", "tts_seconds": round(dur, 2),
         "hangover_ms": HANGOVER_MS, "reopen_latency_ms": reopen_ms,
         "first_detect_after_open_ms":
             None if first_after is None else round((first_after - gate_open_at) * 1000)})
    return 0


def run_level(args):
    print(f"[mode=level] {args.seconds:.0f}초간 입력장치 {args.device} 레벨을 측정합니다. 아무 말이나 하세요.")
    rec = sd.rec(int(args.seconds * SR), samplerate=SR, channels=1,
                 dtype="int16", device=args.device)
    sd.wait()
    a = rec[:, 0]
    peak = int(np.abs(a).max())
    rms = float(np.sqrt(np.mean((a.astype(np.float32)) ** 2)))
    print(f"  peak={peak}/32767 ({peak/32767*100:.1f}%)  rms={rms:.0f}")
    print("  → " + ("정상" if peak > 2000 else "레벨이 낮습니다. 다른 장치 번호를 시도하세요."))
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=["echo", "reopen", "level"], default="echo")
    ap.add_argument("--gate", choices=["on", "off"], default="on")
    # 인덱스가 불안정하므로 이름 지정을 권장한다. 예: --device MV7 --output-device Realtek
    ap.add_argument("--device", default=None, help="입력(마이크) 장치 번호 또는 이름 일부")
    ap.add_argument("--output-device", default=None, help="출력(스피커) 장치 번호 또는 이름 일부")
    ap.add_argument("--model", default=DEFAULT_MODEL)
    ap.add_argument("--threshold", type=float, default=0.5)
    ap.add_argument("--tail", type=float, default=3.0, help="재생 후 추가 관측 시간(초)")
    ap.add_argument("--lead", type=float, default=1.5, help="재생 전 녹음 선행 시간(초)")
    ap.add_argument("--open-latency", type=float, default=6.0,
                    help="출력 장치 오픈 지연 여유(초). 재생이 잘려 들리면 늘린다")
    ap.add_argument("--seconds", type=float, default=5.0, help="level 모드 측정 시간")
    ap.add_argument("--list-devices", action="store_true")
    ap.add_argument("--make-tts", action="store_true")
    args = ap.parse_args()

    if args.list_devices:
        list_devices(); return 0
    if args.make_tts:
        make_tts(); return 0

    # 스트림을 열기 직전에 해석한다 — 미리 잡아두면 그 사이 인덱스가 밀릴 수 있다.
    args.device = resolve_device(args.device, "input")
    args.output_device = resolve_device(args.output_device, "output")
    if args.mode == "level":
        return run_level(args)
    if args.mode == "reopen":
        return run_reopen(args)
    return run_echo(args)


if __name__ == "__main__":
    raise SystemExit(main())
