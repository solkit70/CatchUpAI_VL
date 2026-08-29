#!/usr/bin/env python3
"""M6 실습 3 — 오디오 라우팅 점검 도구.

라우팅 구성은 GUI 작업이라 자동화할 수 없다. 이 스크립트가 하는 일은
**구성이 실제로 됐는지 기계로 확인하는 것**이다. 눈과 귀로만 확인하면
"된 것 같다"에서 멈추고, 방송 중에 아닌 게 드러난다.

M4 장치 규약을 그대로 따른다 — **이름으로 찾고 인덱스로 고정하지 않는다.**
장치 인덱스는 재부팅·USB 재연결마다 바뀐다.

실행:
    python audio_routing_probe.py --scan          # 장치 목록 + 라우팅 후보 판정
    python audio_routing_probe.py --check         # 라우팅 전제 조건 점검
    python audio_routing_probe.py --shared-test   # 마이크 동시 열기 가능한지 (핵심 판별)
    python audio_routing_probe.py --level "MV7" --seconds 5   # 입력 레벨 확인
"""
from __future__ import annotations

import argparse
import sys
import time

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

import numpy as np
import sounddevice as sd

# ── 찾을 장치들 ───────────────────────────────────────────────────────
# 부분 문자열로 찾는다. 드라이버가 이름 뒤에 (Shure Virtual Audio) 같은 걸 붙인다.
TARGETS = {
    "mic_mv7":      ["MV7", "Shure MV7"],
    "motiv_vin":    ["MOTIV Mix Virtual Input"],     # 출력 장치 — 여기로 TTS 를 재생
    "motiv_vout":   ["MOTIV Mix Virtual Output"],    # 입력 장치 — OBS 가 여기서 캡처
    "vb_cable_in":  ["CABLE Input"],
    "vb_cable_out": ["CABLE Output"],
    "voicemeeter":  ["VoiceMeeter"],
    "mic_builtin":  ["Microphone Array"],
}

# 호스트 API 우선순위. WASAPI 가 공유 모드와 저지연에 유리하다.
HOSTAPI_PREF = ["Windows WASAPI", "Windows DirectSound", "MME"]


def hostapi_name(idx: int) -> str:
    try:
        return sd.query_hostapis(idx)["name"]
    except Exception:
        return f"api{idx}"


def find(patterns, kind="any", prefer_wasapi=True):
    """이름 부분일치로 장치를 찾는다. kind: in | out | any."""
    hits = []
    for i, d in enumerate(sd.query_devices()):
        name = d["name"]
        if not any(p.lower() in name.lower() for p in patterns):
            continue
        if kind == "in" and d["max_input_channels"] < 1:
            continue
        if kind == "out" and d["max_output_channels"] < 1:
            continue
        hits.append((i, d))
    if prefer_wasapi:
        def rank(item):
            api = hostapi_name(item[1]["hostapi"])
            return HOSTAPI_PREF.index(api) if api in HOSTAPI_PREF else 99
        hits.sort(key=rank)
    return hits


def scan():
    print("=== 오디오 장치 전체 ===")
    for i, d in enumerate(sd.query_devices()):
        io = []
        if d["max_input_channels"]:
            io.append(f"in{d['max_input_channels']}")
        if d["max_output_channels"]:
            io.append(f"out{d['max_output_channels']}")
        print(f"  {i:3} [{hostapi_name(d['hostapi'])[:18]:18}] "
              f"{d['name'][:52]:52} {'/'.join(io)}")

    print("\n=== 라우팅 대상 장치 판정 ===")
    for key, pats in TARGETS.items():
        hits = find(pats)
        if hits:
            i, d = hits[0]
            api = hostapi_name(d["hostapi"])
            print(f"  ✓ {key:14} → [{i}] {d['name'][:44]} ({api})"
                  + (f"  외 {len(hits)-1}개" if len(hits) > 1 else ""))
        else:
            print(f"  ✗ {key:14} → 없음")


def check():
    """라우팅 전제 조건을 점검하고 가능한 경로를 판정한다."""
    mv7 = find(TARGETS["mic_mv7"], "in")
    builtin = find(TARGETS["mic_builtin"], "in")
    motiv_in = find(TARGETS["motiv_vin"], "out")
    motiv_out = find(TARGETS["motiv_vout"], "in")
    cable_in = find(TARGETS["vb_cable_in"], "out")
    cable_out = find(TARGETS["vb_cable_out"], "in")
    vm = find(TARGETS["voicemeeter"])

    print("=== 전제 조건 ===")
    rows = [
        ("MV7 마이크", mv7, "라우팅 대상 마이크"),
        ("내장 마이크(대체)", builtin, "MV7 없을 때 구조 검증용"),
        ("MOTIV 가상 입력(재생용)", motiv_in, "TTS 를 여기로 재생"),
        ("MOTIV 가상 출력(캡처용)", motiv_out, "OBS 가 여기서 캡처"),
        ("VB-CABLE Input", cable_in, "설치 시에만"),
        ("VB-CABLE Output", cable_out, "설치 시에만"),
        ("VoiceMeeter", vm, "설치 시에만"),
    ]
    for label, hits, why in rows:
        mark = "✓" if hits else "✗"
        detail = f"[{hits[0][0]}] {hits[0][1]['name'][:40]}" if hits else "없음"
        print(f"  {mark} {label:24} {detail:44} {why}")

    print("\n=== 가능한 라우팅 경로 ===")
    mic = mv7 or builtin
    mic_label = "MV7" if mv7 else ("내장 마이크" if builtin else None)

    if mic and motiv_in and motiv_out:
        print("  ★ 무설치 경로 — 사용 가능")
        print(f"     {mic_label} ──┬─→ OBS 트랙 1 (직접 캡처)")
        print(f"              └─→ 앱 (공유 모드 동시 캡처)  ← --shared-test 로 검증 필요")
        print(f"     TTS ─→ MOTIV Mix Virtual Input ─→ OBS 가 Virtual Output 캡처 ─→ 트랙 2")
        print("     주의: MOTIV 가상 쌍을 TTS 전용으로 쓴다. 마이크까지 보내면 한 트랙에 섞인다")
    else:
        print("  ✗ 무설치 경로 — 불가 (마이크 또는 MOTIV 가상 장치 없음)")

    if cable_in and cable_out and vm:
        print("  ★ 설계 문서 경로(VoiceMeeter+VB-CABLE) — 사용 가능")
    else:
        missing = [n for n, h in (("VoiceMeeter", vm), ("VB-CABLE", cable_in and cable_out)) if not h]
        print(f"  ✗ 설계 문서 경로 — 미설치: {', '.join(missing)}")

    return 0 if mic else 1


def shared_test(name_patterns=None, seconds=3):
    """마이크를 두 스트림이 동시에 열 수 있는지 확인한다.

    이것이 무설치 경로의 성립 여부를 가르는 유일한 관문이다.
    OBS 와 앱이 같은 마이크를 동시에 못 열면 VoiceMeeter 같은 분배기가 필요하다.

    한 프로세스에서 InputStream 을 두 개 여는 것으로 근사한다. 배타 모드라면
    두 번째 열기에서 예외가 난다.
    """
    pats = name_patterns or TARGETS["mic_mv7"]
    hits = find(pats, "in")
    if not hits:
        hits = find(TARGETS["mic_builtin"], "in")
        if not hits:
            print("  ✗ 마이크를 찾지 못했습니다")
            return 1
        print(f"  ! MV7 없음 → 내장 마이크로 대체 테스트")

    idx, dev = hits[0]
    api = hostapi_name(dev["hostapi"])
    sr = int(dev["default_samplerate"])
    print(f"=== 동시 열기 테스트 ===")
    print(f"  장치: [{idx}] {dev['name']}  ({api}, {sr}Hz)")

    peaks = {"A": 0.0, "B": 0.0}

    def mk(tag):
        def cb(indata, frames, t, status):
            p = float(np.abs(indata).max())
            if p > peaks[tag]:
                peaks[tag] = p
        return cb

    try:
        s1 = sd.InputStream(device=idx, channels=1, samplerate=sr, callback=mk("A"))
        s1.start()
        print("  스트림 A 열림")
    except Exception as e:
        print(f"  ✗ 첫 스트림부터 실패: {type(e).__name__}: {e}")
        return 1

    ok = False
    try:
        s2 = sd.InputStream(device=idx, channels=1, samplerate=sr, callback=mk("B"))
        s2.start()
        print("  스트림 B 열림  ← 동시 열기 성공")
        ok = True
    except Exception as e:
        print(f"  ✗ 두 번째 스트림 실패: {type(e).__name__}: {e}")
        print("     → 배타 모드다. 마이크 분배기(VoiceMeeter)가 필요하다")
        s2 = None

    print(f"  {seconds}초간 소리를 내 주세요 (말하기)...")
    t0 = time.time()
    while time.time() - t0 < seconds:
        time.sleep(0.1)

    s1.stop(); s1.close()
    if s2:
        s2.stop(); s2.close()

    print(f"\n  피크 레벨  A={peaks['A']:.4f}   B={peaks['B']:.4f}")
    if ok and peaks["A"] > 0.001 and peaks["B"] > 0.001:
        print("  ✓ 두 스트림 모두 실제 오디오를 받았다 — **무설치 경로 성립**")
        return 0
    if ok:
        print("  ! 열리긴 했으나 한쪽 이상이 무음이다. 마이크 입력을 확인하고 다시 실행")
        return 2
    return 1


def cable_test(seconds=3.0, freq=440.0, which="auto"):
    """가상 케이블이 실제로 소리를 나르는지 확인한다.

    TTS 를 재생할 장치(MOTIV Mix Virtual Input)에 알려진 주파수의 톤을 넣고,
    OBS 가 캡처할 장치(MOTIV Mix Virtual Output)에서 그 톤이 나오는지 본다.

    파일 대신 톤을 쓰는 이유: 주파수를 알고 있으면 **잡음이 아니라 내가 넣은 신호**임을
    스펙트럼으로 증명할 수 있다. 파일 재생은 '뭔가 소리가 났다'까지만 말해 준다.

    OBS 없이도 배선의 물리적 성립 여부를 판정할 수 있다 —
    OBS 는 이 경로를 트랙에 배정할 뿐이다.
    """
    # VB-CABLE 을 먼저 본다 — 드라이버 루프백이라 앱 없이 동작한다.
    # MOTIV 는 앱이 실행 중일 때만 이어지므로 대체 경로다.
    pairs = {
        "vb":    (TARGETS["vb_cable_in"], TARGETS["vb_cable_out"], "VB-CABLE"),
        "motiv": (TARGETS["motiv_vin"], TARGETS["motiv_vout"], "MOTIV Mix"),
    }
    order = [which] if which in pairs else ["vb", "motiv"]

    out_hits = in_hits = None
    for key in order:
        op, ip, label = pairs[key]
        oh, ih = find(op, "out"), find(ip, "in")
        if oh and ih:
            out_hits, in_hits, name = oh, ih, label
            break
    if not out_hits or not in_hits:
        print(f"  ✗ 가상 케이블 장치를 찾지 못했습니다 (시도: {', '.join(order)})")
        return 1
    print(f"  케이블: {name}")

    o_idx, o_dev = out_hits[0]
    i_idx, i_dev = in_hits[0]
    sr = 48000
    print("=== 가상 케이블 통과 시험 ===")
    print(f"  재생 → [{o_idx}] {o_dev['name']}")
    print(f"  캡처 ← [{i_idx}] {i_dev['name']}")
    print(f"  {freq:.0f}Hz 톤 {seconds}초")

    n = int(sr * seconds)
    t = np.arange(n) / sr
    tone = (0.25 * np.sin(2 * np.pi * freq * t)).astype(np.float32).reshape(-1, 1)

    captured = []

    def cb(indata, frames, tinfo, status):
        captured.append(indata.copy())

    try:
        with sd.InputStream(device=i_idx, channels=1, samplerate=sr, callback=cb):
            time.sleep(0.3)                      # 캡처 먼저 열고 안정화
            sd.play(tone, samplerate=sr, device=o_idx)
            sd.wait()
            time.sleep(0.3)
    except Exception as e:
        print(f"  ✗ 스트림 실패: {type(e).__name__}: {e}")
        return 1

    if not captured:
        print("  ✗ 캡처된 데이터 없음")
        return 1

    buf = np.concatenate(captured).flatten()
    peak = float(np.abs(buf).max())
    print(f"\n  캡처 피크 {peak:.4f}  샘플 {len(buf):,}개")

    if peak < 0.001:
        print("  ✗ 무음 — 가상 케이블이 연결돼 있지 않다")
        print("     ShurePlus MOTIV Mix 앱이 실행 중이어야 가상 쌍이 이어지는지 확인할 것")
        return 1

    # 넣은 주파수가 실제로 나왔는지 확인한다 — 잡음과 구별하는 유일한 방법
    seg = buf[: 1 << 16] if len(buf) >= (1 << 16) else buf
    spec = np.abs(np.fft.rfft(seg * np.hanning(len(seg))))
    peak_hz = float(np.fft.rfftfreq(len(seg), 1 / sr)[int(np.argmax(spec))])
    print(f"  최대 성분 {peak_hz:.1f}Hz (넣은 값 {freq:.0f}Hz)")

    if abs(peak_hz - freq) <= 15:
        print("  ✓ 넣은 톤이 그대로 나왔다 — **가상 케이블 성립**")
        return 0
    print("  ! 소리는 있으나 주파수가 다르다 — 다른 소스가 섞였을 수 있다")
    return 2


def level(name_patterns, seconds=5):
    hits = find(name_patterns, "in")
    if not hits:
        print(f"  ✗ '{name_patterns}' 입력 장치 없음")
        return 1
    idx, dev = hits[0]
    sr = int(dev["default_samplerate"])
    print(f"  [{idx}] {dev['name']} — {seconds}초 측정")
    peak = {"v": 0.0}
    rms_acc = {"sum": 0.0, "n": 0}

    def cb(indata, frames, t, status):
        a = np.abs(indata)
        peak["v"] = max(peak["v"], float(a.max()))
        rms_acc["sum"] += float((indata ** 2).mean())
        rms_acc["n"] += 1

    with sd.InputStream(device=idx, channels=1, samplerate=sr, callback=cb):
        t0 = time.time()
        while time.time() - t0 < seconds:
            time.sleep(0.1)

    rms = (rms_acc["sum"] / max(rms_acc["n"], 1)) ** 0.5
    print(f"  피크 {peak['v']:.4f}   RMS {rms:.4f}")
    if peak["v"] < 0.001:
        print("  ✗ 무음 — 장치가 물려 있지 않거나 음소거 상태")
        return 1
    print("  ✓ 신호 있음")
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--scan", action="store_true")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--shared-test", action="store_true")
    ap.add_argument("--cable-test", action="store_true")
    ap.add_argument("--cable", default="auto", choices=["auto", "vb", "motiv"])
    ap.add_argument("--level")
    ap.add_argument("--seconds", type=int, default=5)
    a = ap.parse_args()

    if a.scan:
        scan(); return 0
    if a.check:
        return check()
    if a.shared_test:
        return shared_test(seconds=a.seconds)
    if a.cable_test:
        return cable_test(which=a.cable)
    if a.level:
        return level([a.level], a.seconds)
    scan()
    print()
    return check()


if __name__ == "__main__":
    sys.exit(main())
