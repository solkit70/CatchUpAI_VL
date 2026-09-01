#!/usr/bin/env python3
"""M9 실습 4 — 패닉 스톱 지연 실측.

## 무엇을 재는가

로드맵 목표: **핫키를 누른 순간부터 무음이 되기까지 200ms 이내** (10회 최대값 기준)

그런데 시작 전부터 걸리는 것이 하나 있다. M6 실측에서 **가상 케이블 재생 지연이
314ms**로 나왔다. 재생을 *시작*하는 데 314ms가 걸린다면, *멈추는* 데도 비슷한
시간이 든다면 200ms 목표는 구조적으로 불가능하다.

**이 스크립트는 그 질문에 답한다.**

## stop 이 아니라 abort 다

여기가 갈림길이다.

    stream.stop()    이미 버퍼에 들어간 소리를 **다 내보내고** 멈춘다
    stream.abort()   버퍼를 **버리고** 즉시 멈춘다

패닉 스톱에 필요한 것은 `abort()` 다. `stop()` 을 쓰면 버퍼에 남은 만큼
AI 목소리가 계속 나간다 — 끊으려고 눌렀는데 안 끊긴다.

## 어떻게 재는가

VB-CABLE 은 드라이버 루프백이다. `CABLE Input` 으로 재생하면서 동시에
`CABLE Output` 을 캡처하면 **실제로 소리가 흐른 구간**을 샘플 단위로 볼 수 있다.

    t_abort      : abort() 를 부른 시각
    t_silent     : 캡처 쪽에서 신호가 임계값 아래로 떨어진 마지막 시각
    panic_ms     : t_silent - t_abort

⚠️ **이 값은 상한이다.** 캡처 자체에도 입력 버퍼 지연이 있어, 청취자 쪽에서
실제로 무음이 되는 시각은 이보다 조금 이르다. 상한으로 보고하는 편이 안전하다.

같은 실행에서 **시작 지연**(재생 호출 → 첫 소리)도 함께 재서, 계측기 지연이
어느 정도인지 가늠할 수 있게 한다.

실행:
    python panic_stop.py --repeats 10
    python panic_stop.py --repeats 10 --method stop   # 대조군

산출:
    ../../output/panic_stop.json
"""
from __future__ import annotations

import argparse
import json
import statistics
import sys
import time
from pathlib import Path

import numpy as np
import sounddevice as sd

HERE = Path(__file__).resolve().parent
M7_SRC = HERE.parents[2] / "07-CoMC-Engine-POC" / "src"
if str(M7_SRC) not in sys.path:
    sys.path.insert(0, str(M7_SRC))

TONE_HZ = 880
TARGET_MS = 200          # 로드맵 목표
THRESH = 0.02            # 무음 판정 임계 (피크 0.4 기준 약 -26dB)


def find_device(prefix: str, output: bool) -> int:
    ha = {i: a["name"] for i, a in enumerate(sd.query_hostapis())}
    cands = [d for d in sd.query_devices()
             if d["name"].startswith(prefix)
             and (d["max_output_channels"] if output else d["max_input_channels"]) > 0]
    for d in cands:                                  # WASAPI 우선 — 지연이 가장 낮다
        if "WASAPI" in ha[d["hostapi"]]:
            return d["index"]
    if not cands:
        raise SystemExit(f"장치를 찾을 수 없습니다: {prefix}")
    return cands[0]["index"]


def one_trial(spk: int, mic: int, sr: int, hold_sec: float, method: str) -> dict:
    """한 번의 패닉 스톱 측정."""
    blocksize = 128                                  # 작을수록 버퍼가 얕다
    phase = {"t": 0.0}

    def out_cb(outdata, frames, tinfo, status):
        t = (np.arange(frames) + phase["t"]) / sr
        phase["t"] += frames
        sig = (0.4 * np.sin(2 * np.pi * TONE_HZ * t)).astype(np.float32)
        outdata[:] = np.column_stack([sig, sig])

    captured: list[tuple[float, np.ndarray]] = []

    def in_cb(indata, frames, tinfo, status):
        captured.append((time.perf_counter(), indata[:, 0].copy()))

    ostream = sd.OutputStream(device=spk, samplerate=sr, channels=2,
                              dtype="float32", blocksize=blocksize,
                              latency="low", callback=out_cb)
    istream = sd.InputStream(device=mic, samplerate=sr, channels=1,
                             dtype="float32", blocksize=blocksize,
                             latency="low", callback=in_cb)

    istream.start()
    time.sleep(0.25)                                  # 캡처 안정화
    t_play = time.perf_counter()
    ostream.start()
    time.sleep(hold_sec)                              # 소리를 충분히 흘린다

    t_abort = time.perf_counter()
    if method == "abort":
        ostream.abort()                               # 버퍼를 버린다
    else:
        ostream.stop()                                # 버퍼를 다 내보낸다
    time.sleep(1.0)                                   # 잔향까지 담는다
    istream.stop()
    ostream.close(); istream.close()

    # ── 분석 ──────────────────────────────────────────────────────────
    if not captured:
        return {"ok": False, "reason": "캡처 없음"}
    t0 = captured[0][0]
    sig = np.concatenate([c[1] for c in captured])
    # 캡처 콜백 시각을 기준으로 샘플 인덱스 → 절대시각 매핑
    def idx_to_t(i: int) -> float:
        return t0 + i / sr

    env = np.abs(sig)
    # 이동 최대 — 사인파의 영교차를 무음으로 오판하지 않도록
    w = int(sr * 0.005)
    env = np.maximum.reduceat(env, np.arange(0, len(env), w))
    tt = np.array([idx_to_t(i * w) for i in range(len(env))])

    loud = env > THRESH
    if not loud.any():
        return {"ok": False, "reason": "신호가 잡히지 않음 — 케이블 라우팅 확인"}

    t_first = float(tt[np.argmax(loud)])
    after = tt >= t_abort
    idx_after = np.where(after & loud)[0]
    t_last = float(tt[idx_after[-1]]) if len(idx_after) else t_abort

    return {
        "ok": True,
        "start_ms": round((t_first - t_play) * 1000),
        "panic_ms": round((t_last - t_abort) * 1000),
        "peak": round(float(env.max()), 4),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repeats", type=int, default=10)
    ap.add_argument("--hold", type=float, default=1.2, help="중단 전 재생 시간(초)")
    ap.add_argument("--method", choices=["abort", "stop"], default="abort")
    args = ap.parse_args()

    spk = find_device("CABLE Input", output=True)
    mic = find_device("CABLE Output", output=False)
    sr = int(sd.query_devices(spk)["default_samplerate"])
    print(f"\n=== M9 실습 4 — 패닉 스톱 ({args.method}) · {args.repeats}회 ===\n")
    print(f"  재생 [{spk}] {sd.query_devices(spk)['name']}")
    print(f"  캡처 [{mic}] {sd.query_devices(mic)['name']}   {sr}Hz\n")

    trials = []
    for i in range(args.repeats):
        r = one_trial(spk, mic, sr, args.hold, args.method)
        trials.append(r)
        if r["ok"]:
            flag = "✅" if r["panic_ms"] <= TARGET_MS else "⚠️"
            print(f"  {flag} {i+1:>2}회  중단 {r['panic_ms']:>4}ms   "
                  f"(시작 지연 {r['start_ms']:>4}ms · peak {r['peak']})")
        else:
            print(f"  ❌ {i+1:>2}회  {r['reason']}")

    good = [t for t in trials if t["ok"]]
    if not good:
        print("\n  측정 실패 — 케이블 경로를 확인하세요")
        return
    pm = [t["panic_ms"] for t in good]
    sm = [t["start_ms"] for t in good]
    res = {
        "method": args.method, "n": args.repeats, "n_ok": len(good),
        "target_ms": TARGET_MS,
        "panic_med_ms": round(statistics.median(pm)),
        "panic_max_ms": max(pm), "panic_min_ms": min(pm),
        "start_med_ms": round(statistics.median(sm)),
        "pass": max(pm) <= TARGET_MS,
        "trials": trials,
    }
    print(f"\n  중단 지연  중앙 {res['panic_med_ms']}ms · "
          f"최악 {res['panic_max_ms']}ms · 최선 {res['panic_min_ms']}ms")
    print(f"  시작 지연  중앙 {res['start_med_ms']}ms  ← 계측기 지연 가늠용")
    print(f"\n  【목표 {TARGET_MS}ms】 "
          + ("✅ 달성 (10회 최대값 기준)" if res["pass"]
             else f"❌ 미달 — 최악값 {res['panic_max_ms']}ms"))

    from common import out, write_json
    p = write_json(out(f"panic_stop.{args.method}.json"), res)
    print(f"\n  기록: {p}")


if __name__ == "__main__":
    main()
