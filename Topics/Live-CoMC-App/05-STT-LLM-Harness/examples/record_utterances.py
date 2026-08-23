#!/usr/bin/env python3
"""M5 실습 1 — WER 측정용 20문장 녹음기.

guides/utterance-script.md 의 문장을 하나씩 띄우고 고정 창으로 녹음한다.

M4에서 얻은 함정 두 가지를 그대로 반영했다:
  1) 장치는 이름으로 지정한다. 인덱스는 같은 세션에서도 밀린다
     (2026-08-15: MV7 이 1→22→3→1 로 이동).
  2) 스트림은 세션당 한 번만 연다. 문장마다 열고 닫으면 장치 오픈 지연
     4~9초가 20번 붙어서 측정이 아니라 대기가 된다.

실행:
    python record_utterances.py --list-devices
    python record_utterances.py --device "MV7" --condition clean
    python record_utterances.py --device "MV7" --condition bgm
    python record_utterances.py --device "VoiceMeeter Out B1" --condition routed
    python record_utterances.py --device "MV7" --condition clean --only 07,12

산출:
    utterances/{condition}/{id}.wav
    utterances/{condition}/manifest.json   # 정답 문장 + 녹음 메타
"""
import argparse
import json
import sys
import time
import wave
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import sounddevice as sd

from utterances import UTTERANCES, by_id

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

SR = 16000          # M4와 동일. 전사 API도 16k 모노를 그대로 받는다
HERE = Path(__file__).resolve().parent


def resolve_device(spec):
    """장치 번호 또는 이름 일부를 실제 인덱스로 해석한다. (M4 wake_probe.py 와 동일 규약)"""
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


def list_devices():
    print(f"{'idx':>4}  {'in':>3}  이름")
    print("-" * 60)
    for i, d in enumerate(sd.query_devices()):
        if d["max_input_channels"] > 0:
            print(f"{i:>4}  {d['max_input_channels']:>3}  {d['name']}")
    print()
    print("⚠ 인덱스는 재열거될 때마다 바뀝니다. --device 에는 이름 일부를 쓰세요. 예: --device \"MV7\"")


def write_wav(path: Path, audio: np.ndarray):
    with wave.open(str(path), "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)          # int16
        w.setframerate(SR)
        w.writeframes(audio.tobytes())


def peak_dbfs(audio: np.ndarray) -> float:
    peak = int(np.abs(audio).max()) if audio.size else 0
    if peak == 0:
        return -99.0
    return round(20 * np.log10(peak / 32768.0), 1)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--list-devices", action="store_true")
    ap.add_argument("--device", help="입력 장치 이름 일부 (권장) 또는 인덱스")
    # routed: M6 오디오 라우팅(VoiceMeeter 경유) 후 재측정용.
    # clean 으로 다시 녹음하면 M5 기준선(WER 23.3%)을 덮어쓴다 —
    # 조건이 다른 측정은 파일을 분리해야 비교가 가능하다.
    ap.add_argument("--condition", default="clean",
                    choices=["clean", "bgm", "routed"])
    ap.add_argument("--seconds", type=float, default=6.0, help="문장당 녹음 창 (기본 6초)")
    ap.add_argument("--only", default="", help="특정 번호만 재녹음. 예: 07,12")
    args = ap.parse_args()

    if args.list_devices:
        list_devices()
        return 0

    targets = UTTERANCES
    if args.only:
        ids = [s.strip().zfill(2) for s in args.only.split(",") if s.strip()]
        targets = [by_id(i) for i in ids]

    dev = resolve_device(args.device)
    outdir = HERE / "utterances" / args.condition
    outdir.mkdir(parents=True, exist_ok=True)

    print()
    print(f"조건: {args.condition}   문장: {len(targets)}개   창: {args.seconds}초")
    if args.condition == "bgm":
        print("⚠ BGM을 평소 방송 볼륨으로 재생한 상태에서 진행하세요.")
    print("평소 방송하듯 읽으세요. 또박또박 읽으면 WER이 실제보다 좋게 나와 측정 의미가 없어집니다.")
    print()

    frames = int(SR * args.seconds)
    records = []

    # 스트림은 여기서 한 번만 연다 (M4 함정 3: 장치 오픈 지연 4~9초)
    with sd.InputStream(samplerate=SR, channels=1, dtype="int16", device=dev) as stream:
        stream.read(int(SR * 0.3))          # 워밍업 버림
        for idx, (uid, typ, text) in enumerate(targets, 1):
            print(f"[{idx}/{len(targets)}] {uid} ({typ})")
            print(f"    {text}")
            try:
                input("    Enter → 녹음 시작 (Ctrl+C 중단) ")
            except (EOFError, KeyboardInterrupt):
                print("\n중단했습니다.")
                break

            stream.read(stream.read_available)   # 대기 중 쌓인 버퍼 폐기
            print(f"    ● 녹음 중 {args.seconds}초 …", end="", flush=True)
            buf, need = [], frames
            while need > 0:
                chunk, over = stream.read(min(1024, need))
                if over:
                    print(" [overflow]", end="")
                buf.append(chunk[:, 0].copy())
                need -= len(chunk)
            audio = np.concatenate(buf)[:frames]

            path = outdir / f"{uid}.wav"
            write_wav(path, audio)
            pk = peak_dbfs(audio)
            warn = ""
            if pk < -35:
                warn = "  ⚠ 너무 작습니다 — 게인을 올리거나 마이크에 가까이"
            elif pk > -1.5:
                warn = "  ⚠ 클리핑 위험 — 게인을 내리세요"
            print(f" 완료  peak {pk} dBFS{warn}")
            print()

            records.append({"id": uid, "type": typ, "text": text,
                            "wav": path.name, "peak_dbfs": pk,
                            "seconds": args.seconds,
                            "recorded_at": datetime.now(timezone.utc).isoformat()})

    # manifest 는 재녹음분만 갱신하고 나머지는 보존한다
    mpath = outdir / "manifest.json"
    existing = {}
    if mpath.exists():
        existing = {r["id"]: r for r in json.loads(mpath.read_text(encoding="utf-8"))["items"]}
    for r in records:
        existing[r["id"]] = r
    items = [existing[k] for k in sorted(existing)]
    mpath.write_text(json.dumps(
        {"condition": args.condition, "sample_rate": SR,
         "device": args.device, "updated_at": datetime.now(timezone.utc).isoformat(),
         "items": items}, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"저장 {len(records)}건 → {outdir}")
    print(f"manifest: {len(items)}/20 문장 확보")
    missing = [u[0] for u in UTTERANCES if u[0] not in existing]
    if missing:
        print(f"미녹음: {', '.join(missing)}")
    else:
        print("20문장 모두 확보 — 다음: python stt_probe.py --condition " + args.condition)
    return 0


if __name__ == "__main__":
    sys.exit(main())
