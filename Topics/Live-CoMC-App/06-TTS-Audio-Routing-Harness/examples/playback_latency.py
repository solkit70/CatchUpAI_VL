#!/usr/bin/env python3
"""M6 실습 3 — 합성부터 **실제로 소리가 나기까지** 재는 도구.

## 왜 따로 재야 하는가

`tts_compare.py` 가 잰 588ms 는 **파일이 만들어지기까지**다.
스피커나 방송에서 소리가 나기까지는 그 뒤로 더 있다.

    합성 요청 ──[ latency_ms ]──> 파일 완성 ──[ ? ]──> 소리 남

오른쪽 구간을 아무도 재지 않았다. 이 값이 대기 필러의 트리거 시각(`T_filler`)에
직접 들어가므로, 모르면 필러를 언제 넣을지 정할 수 없다.

## 어떻게 재는가

VB-CABLE 은 드라이버 루프백이다. `CABLE Input` 으로 재생하면 `CABLE Output` 에서
그대로 나온다. 그러니 **재생하면서 동시에 캡처**하면 소리가 실제로 흐르기 시작한
시각을 샘플 단위로 잡을 수 있다. 사람 귀나 눈금이 아니라 파형으로 재는 것이다.

    t_play_call  : sd.play() 를 부른 시각
    t_audible    : 캡처 쪽에서 임계값을 처음 넘은 시각
    cable_ms     : t_audible - t_play_call   ← 오디오 스택 + 케이블 버퍼

전체 체감 지연은 `latency_ms + cable_ms` 다.

실행:
    python playback_latency.py                    # 기본 문장 5회
    python playback_latency.py --repeats 3 --provider edge
    python playback_latency.py --text "직접 넣은 문장"

산출:
    playback_latency.json · tts_log.jsonl 에 playback_latency 이벤트
"""
from __future__ import annotations

import argparse
import json
import statistics
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

import numpy as np
import sounddevice as sd
import soundfile as sf

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from audio_routing_probe import find                      # noqa: E402
from tts_providers import TTSUnavailable, build           # noqa: E402

RUNTIME = HERE / "voice_registry.runtime.json"
REGISTRY = HERE / "voice_registry.json"
LOG = HERE / "tts_log.jsonl"
RESULT = HERE / "playback_latency.json"
AUDIO_DIR = HERE / "audio" / "playback"

# 방송에서 실제로 나갈 법한 길이. 한 호흡에 읽는 두 문장.
DEFAULT_TEXT = ("네, 3번 파트에서는 FDE 영상 제작 과정을 다룹니다. "
                "한국어와 영어 두 편을 공개했습니다.")

# 무음과 소리를 가르는 임계값. VB-CABLE 은 잡음이 거의 없어 낮게 잡아도 된다.
THRESHOLD = 0.01


def log(ev: dict):
    ev["ts"] = datetime.now(timezone.utc).isoformat()
    with LOG.open("a", encoding="utf-8") as f:
        f.write(json.dumps(ev, ensure_ascii=False) + "\n")


def load_provider(name: str | None):
    src = RUNTIME if RUNTIME.exists() else REGISTRY
    reg = json.loads(src.read_text(encoding="utf-8"))
    providers = reg["providers"]
    if name is None:
        name = reg.get("default") or reg.get("fallback_order", ["edge"])[0]
    if name not in providers:
        sys.exit(f"'{name}' 은 레지스트리에 없습니다. 가능: {list(providers)}")
    return name, build(name, providers[name])


def measure_once(prov, text: str, idx: int, cable_out_idx: int, cable_in_idx: int,
                 target_sr: int):
    """합성 → 재생 → 캡처로 실제 발성 시각을 잡는다."""
    AUDIO_DIR.mkdir(parents=True, exist_ok=True)
    path = AUDIO_DIR / f"pb_{idx:02d}.mp3"

    # ── ① 합성 ────────────────────────────────────────────────────────
    r = prov.synth(text, path)

    # ── ② 파일 로드 (재생 준비 시간도 실제 비용이다) ─────────────────
    # edge-tts 는 24kHz mp3 를 준다. WASAPI 공유 모드는 장치 믹스 포맷을 요구하므로
    # 리샘플링이 필요하다. **이 변환 비용도 실제 파이프라인에 존재하는 비용**이라
    # 로드 구간에 포함해 잰다 — 빼면 실측이 아니라 이상치가 된다.
    t_load0 = time.perf_counter()
    data, sr = sf.read(str(path), dtype="float32", always_2d=True)
    if sr != target_sr:
        n_out = int(round(len(data) * target_sr / sr))
        x_old = np.linspace(0.0, 1.0, num=len(data), endpoint=False)
        x_new = np.linspace(0.0, 1.0, num=n_out, endpoint=False)
        data = np.stack([np.interp(x_new, x_old, data[:, c])
                         for c in range(data.shape[1])], axis=1).astype(np.float32)
        sr = target_sr
    load_ms = round((time.perf_counter() - t_load0) * 1000)

    # ── ③ 재생하며 동시에 캡처 ───────────────────────────────────────
    cap = []
    t_first = {"v": None}
    t_play = {"v": None}

    def cb(indata, frames, tinfo, status):
        cap.append(indata.copy())
        if t_first["v"] is None and t_play["v"] is not None:
            if float(np.abs(indata).max()) > THRESHOLD:
                t_first["v"] = time.perf_counter()

    with sd.InputStream(device=cable_out_idx, channels=1,
                        samplerate=sr, callback=cb, blocksize=128):
        time.sleep(0.25)                       # 캡처 안정화
        t_play["v"] = time.perf_counter()
        sd.play(data, samplerate=sr, device=cable_in_idx)
        sd.wait()
        time.sleep(0.15)

    if t_first["v"] is None:
        return {"ok": False, "reason": "캡처에서 소리를 감지하지 못함",
                "synth_ms": r.latency_ms}

    cable_ms = round((t_first["v"] - t_play["v"]) * 1000)
    buf = np.concatenate(cap).flatten() if cap else np.array([])
    return {
        "ok": True,
        "synth_ms": r.latency_ms,              # 합성 요청 → 파일 완성
        "first_chunk_ms": r.first_chunk_ms,    # 첫 오디오 바이트 (스트리밍 시)
        "load_ms": load_ms,                    # 파일 → 메모리
        "cable_ms": cable_ms,                  # 재생 호출 → 실제 발성
        "total_ms": r.latency_ms + load_ms + cable_ms,
        "audio_sec": round(len(data) / sr, 2),
        "captured_peak": round(float(np.abs(buf).max()), 4) if len(buf) else 0.0,
        "chars": len(text),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--provider", help="기본값은 레지스트리의 default")
    ap.add_argument("--repeats", type=int, default=5)
    ap.add_argument("--text", default=DEFAULT_TEXT)
    a = ap.parse_args()

    ci = find(["CABLE Input"], "out")
    co = find(["CABLE Output"], "in")
    if not ci or not co:
        sys.exit("VB-CABLE 이 없습니다. audio_routing_probe.py --check 로 확인하세요.")
    cable_in_idx, cin = ci[0]
    cable_out_idx, cout = co[0]

    # 두 엔드포인트의 믹스 포맷이 같아야 한다. 캡처 쪽 기본값을 기준으로 맞춘다.
    target_sr = int(cout["default_samplerate"])

    name, prov = load_provider(a.provider)
    print(f"프로바이더 : {name}")
    print(f"재생 →      [{cable_in_idx}] {cin['name']}")
    print(f"캡처 ←      [{cable_out_idx}] {cout['name']}  ({target_sr}Hz)")
    print(f"문장       : {a.text[:48]}...  ({len(a.text)}자)\n")

    rows = []
    for i in range(a.repeats):
        try:
            r = measure_once(prov, a.text, i + 1, cable_out_idx, cable_in_idx,
                             target_sr)
        except TTSUnavailable as e:
            sys.exit(f"프로바이더 사용 불가: {e}")
        rows.append(r)
        if r["ok"]:
            print(f"  #{i+1}  합성 {r['synth_ms']:>5}ms + 로드 {r['load_ms']:>3}ms "
                  f"+ 케이블 {r['cable_ms']:>4}ms = {r['total_ms']:>5}ms   "
                  f"(오디오 {r['audio_sec']}s, 피크 {r['captured_peak']})")
        else:
            print(f"  #{i+1}  실패 — {r['reason']}")

    good = [r for r in rows if r["ok"]]
    if not good:
        print("\n전부 실패했습니다.")
        return 1

    def med(k):
        return round(statistics.median(r[k] for r in good))

    print(f"\n{'구간':<26}{'중앙값':>9}")
    print("-" * 36)
    print(f"{'① 합성 (요청→파일)':<24}{med('synth_ms'):>9}ms")
    print(f"{'② 로드 (파일→메모리)':<24}{med('load_ms'):>9}ms")
    print(f"{'③ 케이블 (재생→발성)':<24}{med('cable_ms'):>9}ms")
    print("-" * 36)
    print(f"{'전체 (요청→소리)':<24}{med('total_ms'):>9}ms")

    summary = {"provider": name, "repeats": a.repeats, "chars": len(a.text),
               "median": {k: med(k) for k in
                          ("synth_ms", "load_ms", "cable_ms", "total_ms")},
               "runs": rows}
    RESULT.write_text(json.dumps(summary, ensure_ascii=False, indent=2),
                      encoding="utf-8")
    log({"event": "playback_latency", **{k: v for k, v in summary.items() if k != "runs"}})
    print(f"\n원자료: {RESULT.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
