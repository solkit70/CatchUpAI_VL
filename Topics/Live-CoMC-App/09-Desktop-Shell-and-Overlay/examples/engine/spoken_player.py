#!/usr/bin/env python3
"""CVL 1 — `spoken.json` 을 소리로 내는 재생기 (사고 6 · go-nogo B 갈래 1번).

## 왜 이제야 만드는가

⑥ 은 LIVE 모드에서 `spoken.json` 을 쓰고 *"합성·재생은 M9 셸의 몫"* 이라 주석해 뒀다.
M9 는 Electron 셸을 「급하지 않음」으로 내렸고, 그 자리가 6주 동안 비어 있었다.
09-12 사전 점검에서 `grep -rn spoken.json` — 쓰는 곳 1, 지우는 곳 1, **읽는 곳 0.**
LIVE 와 REVIEW 의 차이는 파일 이름뿐이었다. 이 파일이 그 빈자리다.

## 무엇을 하는가 — 그리고 하지 않는가

  폴링  `output/spoken.json` 이 새로 생기면 읽는다 (250ms 간격)
  확인  `mode.json` 이 LIVE 인지 **다시** 본다 — ⑥ 이 확인했어도 그 사이 바뀔 수 있다
  합성  M6 `tts_providers.build` (기본 edge-tts, 레지스트리 값 그대로 — 새 어댑터를 만들지 않는다)
  재생  `sounddevice` 로 지정 출력 장치에 (기본: 시스템 기본 장치 → 헤드폰으로 먼저 듣는다)
  소비  재생이 끝나면 `spoken.json` 을 지우고 `spoken_log.jsonl` 에 한 줄 남긴다
  중단  재생 중 `mode.json` 이 LIVE 가 아니게 되면 **abort** — 버퍼를 버리고 즉시 멈춘다
        (M9 패닉 스톱 실측: abort 112ms · stop 은 버퍼만큼 더 나간다)

**하지 않는 것** — 엔진을 부르지 않는다. 텍스트를 고치지 않는다(치환은 M6 provider 가 한다).
같은 파일을 두 번 읽지 않는다(소비가 곧 삭제다). 텍스트가 비어 있으면 아무것도 하지 않는다.

## 안전의 방향

실패는 전부 **침묵 쪽**으로 떨어진다 — 합성 실패·장치 없음·모드 불일치는 로그만 남기고
파일을 소비한다. 재시도로 옛 발화를 뒤늦게 내보내는 것이 소리 안 나는 것보다 나쁘다.

실행:
    python spoken_player.py --list-devices
    python spoken_player.py --text "테스트입니다" --device "헤드폰 이름 일부"   # 합성+재생 1회
    python spoken_player.py --device "CABLE Input"                            # 폴링 (방송)
    python spoken_player.py --once                                             # 파일 1건만

산출:
    ../../output/spoken_log.jsonl · ../../output/debug/audio/spoken_*.mp3
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import threading
import time
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
TOPIC = HERE.parents[2]
M6 = TOPIC / "06-TTS-Audio-Routing-Harness" / "examples"
M7_SRC = TOPIC / "07-CoMC-Engine-POC" / "src"
for p in (M6, M7_SRC):
    if str(p) not in sys.path:
        sys.path.insert(0, str(p))

import numpy as np                                  # noqa: E402
import sounddevice as sd                            # noqa: E402
import soundfile as sf                              # noqa: E402

from common import now_iso, out, read_json, trace, write_json   # noqa: E402
from tts_providers import TTSUnavailable, build     # noqa: E402

REGISTRY = M6 / "voice_registry.runtime.json"
SPOKEN = out("spoken.json")
MODE = out("mode.json")
LOG = out("spoken_log.jsonl")
AUDIO_DIR = out("debug") / "audio"
POLL_S = 0.25
MODE_CHECK_S = 0.05


def log(ev: dict) -> None:
    LOG.parent.mkdir(parents=True, exist_ok=True)
    with LOG.open("a", encoding="utf-8") as f:
        f.write(json.dumps({"ts": now_iso(), **ev}, ensure_ascii=False) + "\n")


def current_mode() -> str:
    """mode.json 을 읽는다. 없으면 LIVE(⑥ 과 같은 기본값), 깨졌으면 REVIEW(침묵 쪽)."""
    if not MODE.exists():
        return "LIVE"
    try:
        return str(read_json(MODE).get("mode", "")).upper() or "REVIEW"
    except Exception:
        return "REVIEW"


def pick_device(pattern: str | None) -> int | None:
    """이름 부분일치로 출력 장치를 고른다. None 이면 시스템 기본 장치."""
    if not pattern:
        return None
    hits = [(i, d) for i, d in enumerate(sd.query_devices())
            if pattern.lower() in d["name"].lower() and d["max_output_channels"] > 0]
    if not hits:
        sys.exit(f"출력 장치 '{pattern}' 을 찾지 못했습니다. --list-devices 로 확인하세요.")
    # WASAPI 를 우선한다 — M6 라우팅 실측과 같은 기준
    apis = {i: a["name"] for i, a in enumerate(sd.query_hostapis())}
    hits.sort(key=lambda x: 0 if "WASAPI" in apis.get(x[1]["hostapi"], "") else 1)
    return hits[0][0]


def load_provider(name: str | None):
    reg = read_json(REGISTRY)
    name = name or reg["default_provider"]
    cfg = dict(reg["providers"][name])
    # 공유 치환표는 provider 별 replacements 앞에 둔다 (tts_probe 와 같은 순서)
    repl = dict(reg.get("shared_replacements", {}))
    repl.update(cfg.get("replacements") or {})
    cfg["replacements"] = repl
    return name, build(name, cfg)


def load_audio(path: Path, device: int | None) -> tuple[np.ndarray, int]:
    data, sr = sf.read(str(path), dtype="float32", always_2d=True)
    info = sd.query_devices(device, "output") if device is not None else sd.query_devices(kind="output")
    target = int(info["default_samplerate"])
    if sr != target:                                      # WASAPI 공유 모드는 장치 포맷을 요구한다
        n = int(round(len(data) * target / sr))
        xo = np.linspace(0.0, 1.0, num=len(data), endpoint=False)
        xn = np.linspace(0.0, 1.0, num=n, endpoint=False)
        data = np.stack([np.interp(xn, xo, data[:, c]) for c in range(data.shape[1])],
                        axis=1).astype(np.float32)
        sr = target
    return data, sr


_COM = threading.local()


def _com_init():
    """WASAPI 콜백 스트림은 **COM 이 초기화된 스레드**에서만 시작된다.

    단독 프로세스(main 스레드)에서는 sounddevice import 때 초기화가 돼 있어 문제가 없었는데,
    comc_console 이 재생기를 **스레드**로 돌리자 `Error starting stream: Unanticipated host error
    (WdmSyncIoctl … GLE=0x490)` 로 죽었다 (CVL 3 실측 · 2026-09-17). 블로킹 write 는 되고 콜백만
    죽는 것도 실측. 스레드마다 한 번 CoInitializeEx 를 부르면 된다 — 이미 돼 있으면 S_FALSE, 다른
    모드면 RPC_E_CHANGED_MODE 를 돌려줄 뿐 해가 없다. Windows 가 아니면 아무것도 하지 않는다.
    """
    if getattr(_COM, "done", False) or sys.platform != "win32":
        return
    try:
        import ctypes
        ctypes.windll.ole32.CoInitializeEx(None, 0x0)     # COINIT_MULTITHREADED
    except Exception:
        pass
    _COM.done = True


def play(data: np.ndarray, sr: int, device: int | None, watch_mode: bool,
         stop_unless: tuple[str, ...] = ("LIVE",)) -> dict:
    """블로킹 재생. 재생 중 모드가 `stop_unless` 밖으로 나가면 abort 한다."""
    pos = {"i": 0}
    aborted = {"v": False, "reason": None}

    def cb(outdata, frames, tinfo, status):
        i = pos["i"]
        chunk = data[i:i + frames]
        if len(chunk) < frames:
            outdata[:len(chunk)] = chunk
            outdata[len(chunk):] = 0
            pos["i"] = len(data)
            raise sd.CallbackStop()
        outdata[:] = chunk
        pos["i"] = i + frames

    _com_init()                                           # 콘솔(스레드)에서 부를 때 필요 — 아래 참조
    t0 = time.perf_counter()
    stream = sd.OutputStream(samplerate=sr, channels=data.shape[1], device=device,
                             callback=cb, blocksize=256)
    with stream:
        while stream.active and pos["i"] < len(data):
            if watch_mode and current_mode() not in stop_unless:
                stream.abort()                            # 버퍼를 버린다 — stop() 이 아니다
                aborted["v"], aborted["reason"] = True, f"mode={current_mode()}"
                break
            time.sleep(MODE_CHECK_S)
    return {"played_ms": round((time.perf_counter() - t0) * 1000),
            "aborted": aborted["v"], "abort_reason": aborted["reason"],
            "progress": round(pos["i"] / max(1, len(data)), 3)}


# ── TTS 용 읽기 정규화 (CVL 4, 2026-09-17) ──────────────────────────
# edge-tts 가 「9/16」을 「16분의 9」로 읽었다 (진행자 실청). 화면 텍스트는 그대로 두고
# **소리로 보내는 문자열만** 바꾼다 — 오버레이·로그·verdict 는 원문이어야 사후 대조가 된다.
_RE_YMD = re.compile(r"(?<!\d)(\d{4})-(\d{1,2})-(\d{1,2})(?!\d)")
_RE_MD = re.compile(r"(?<![\d/])(\d{1,2})/(\d{1,2})(?![\d/])")          # 9/16 · 10/3  (URL 의 a/b 는 앞뒤 조건으로 제외)
_RE_HM = re.compile(r"(?<!\d)(\d{1,2}):(\d{2})(?!\d)")
_RE_RANGE = re.compile(r"(일|시|분|도)\s*[~∼–-]\s*(?=\d)")
_RE_USD = re.compile(r"\$(\d[\d,]*)")
_RE_DEGC = re.compile(r"(\d)\s*°C")
# 「통과 6/9」「커버리지 2/3」 같은 비율은 날짜가 아니다 — 앞에 개수 어휘가 붙으면 건너뛴다
_RE_RATIO_BEFORE = re.compile(r"(통과|시도|성공|완료|실행|커버리지|항목|건|중)\s*$")


# 영어 답변 (CVL 4) — 한국어 목소리(SunHi)가 영어 문장을 읽으면 억양이 무너진다. 문장의 글자 대부분이
# 라틴 문자면 영어 목소리로 합성한다. 레지스트리의 목소리는 건드리지 않고 이 한 번만 바꾼다.
EN_VOICE = {"edge": "en-US-JennyNeural"}
_RE_HANGUL = re.compile(r"[가-힣]")
_RE_LATIN_LETTER = re.compile(r"[A-Za-z]")


def is_english(text: str) -> bool:
    ko, en = len(_RE_HANGUL.findall(text)), len(_RE_LATIN_LETTER.findall(text))
    return en > 0 and ko < en * 0.5          # 영어 문장에 한국어 계정 이름 하나쯤은 섞인다


def normalize_for_tts(text: str) -> str:
    if is_english(text):
        return text                                   # 한국어 날짜 규칙을 영어 문장에 대지 않는다
    t = _RE_YMD.sub(lambda m: f"{int(m[1])}년 {int(m[2])}월 {int(m[3])}일", text)

    def md(m):
        if not (1 <= int(m[1]) <= 12 and 1 <= int(m[2]) <= 31) or _RE_RATIO_BEFORE.search(t[:m.start()]):
            return m[0]
        return f"{int(m[1])}월 {int(m[2])}일"
    t = _RE_MD.sub(md, t)
    t = _RE_HM.sub(lambda m: f"{int(m[1])}시" + (f" {int(m[2])}분" if int(m[2]) else ""), t)
    t = _RE_RANGE.sub(lambda m: m[1] + "부터 ", t)
    t = _RE_USD.sub(lambda m: m[1].rstrip(",") + "달러", t)
    t = _RE_DEGC.sub(lambda m: m[1] + "도", t)
    return t


def speak(text: str, prov, provider_name: str, device: int | None,
          watch_mode: bool, tag: str, stop_unless: tuple[str, ...] = ("LIVE",)) -> dict:
    AUDIO_DIR.mkdir(parents=True, exist_ok=True)
    path = AUDIO_DIR / f"spoken_{tag}.mp3"
    t0 = time.perf_counter()
    voice_backup = prov.voice
    if is_english(text) and provider_name in EN_VOICE:
        prov.voice = EN_VOICE[provider_name]
    try:
        r = prov.synth(normalize_for_tts(text), path)
    finally:
        prov.voice = voice_backup
    synth_ms = round((time.perf_counter() - t0) * 1000)
    data, sr = load_audio(r.path, device)
    pr = play(data, sr, device, watch_mode, stop_unless)
    return {"provider": provider_name, "voice": prov.voice, "audio": str(r.path.name),
            "synth_ms": synth_ms, "audio_s": round(len(data) / sr, 2), **pr}


# ── 시그니처 끝인사 (CVL 4, 2026-09-17) ───────────────────────────────
# 15개 언어로 미리 합성해 둔 mp3 를 순서대로 튼다 (output/private/signoff/*.mp3 · signoff.json).
# LLM 도 게이트도 안 거친다 — 진행자가 승인한 고정 대본이라 징글과 같다. 요청 파일이 트리거이고,
# 언어 하나가 끝날 때마다 오버레이에 그 언어 줄을 띄운다. 패닉(MUTE)이면 즉시 멈춘다.
SIGNOFF_REQ = out("signoff_request.json")
SIGNOFF_JSON = out("private") / "signoff.json"
SIGNOFF_DIR = out("private") / "signoff"
SIGNOFF_GAP_S = 0.6


# 세트가 둘이다 (CVL 4 · 9/18): signoff = 끝인사 · intro = 방송 중간 다국어 자기소개 샘플.
# 요청 파일의 "set" 이 고르고, 대본·mp3 는 output/private/{set}.json · {set}/ 에 있다.
MULTILANG_SETS = {"signoff": "시그니처 끝인사", "intro": "15개 국어 자기소개"}


def trim_silence(data: np.ndarray, sr: int, thresh: float = 0.01, keep_s: float = 0.12) -> np.ndarray:
    """앞뒤 무음을 잘라 낸다 (keep_s 만큼은 남긴다 — 딱 붙이면 숨 쉴 틈이 없다)."""
    a = np.abs(data).max(axis=1) if data.ndim == 2 else np.abs(data)
    idx = np.where(a > thresh)[0]
    if len(idx) == 0:
        return data
    keep = int(sr * keep_s)
    return data[max(0, idx[0] - keep): min(len(data), idx[-1] + keep)]


def consume_signoff(device: int | None) -> bool:
    if not SIGNOFF_REQ.exists():
        return False
    try:
        req = read_json(SIGNOFF_REQ)
    except Exception:
        req = {}
    SIGNOFF_REQ.unlink(missing_ok=True)
    set_name = req.get("set") or "signoff"
    label = MULTILANG_SETS.get(set_name, set_name)
    sj, sd = out("private") / f"{set_name}.json", out("private") / set_name
    if not sj.exists():
        print(f"  ⛔ {label} 대본 없음 — signoff_build.py --set {set_name}")
        return True
    if current_mode() == "MUTE":
        print(f"  ⏸ MUTE — {label} 보류·소비")
        return True
    lines = read_json(sj)["lines"]
    print(f"  🔊 {label} · {len(lines)}개 언어")
    t0 = time.perf_counter()
    done = 0
    for ln in lines:
        mp3 = sd / ln["file"]
        if not mp3.exists():
            print(f"     ⛔ {ln['name']} 파일 없음 — 건너뜀")
            continue
        write_json(out("overlay.json"), {"text": f"{ln['name']} · {ln['text']}", "part_id": set_name,
                                         "updated_at": now_iso()})
        data, sr = load_audio(mp3, device)
        data = trim_silence(data, sr)             # edge-tts 는 앞 0.2초·뒤 0.9초 무음을 붙인다 — 15개면 16초다
        res = play(data, sr, device, watch_mode=True, stop_unless=("LIVE", "REVIEW"))
        if res["aborted"]:
            print(f"     ⛔ 중단 — {ln['name']} 도중 ({res['abort_reason']})")
            log({"event": "multilang", "set": set_name, "aborted_at": ln["code"], "done": done})
            write_json(out("overlay.json"), {"text": "", "part_id": set_name, "updated_at": now_iso(),
                                             "cleared_by": set_name, "reason": "aborted"})
            return True
        done += 1
        time.sleep(SIGNOFF_GAP_S)
    write_json(out("overlay.json"), {"text": "", "part_id": set_name, "updated_at": now_iso(),
                                     "cleared_by": set_name, "reason": "finished"})
    sec = round(time.perf_counter() - t0)
    print(f"     ✅ {label} {done}개 언어 · {sec}초")
    log({"event": "multilang", "set": set_name, "done": done, "seconds": sec})
    return True


def consume_one(prov, provider_name: str, device: int | None) -> bool:
    """spoken.json 한 건을 처리한다. 처리했으면 True."""
    if not SPOKEN.exists():
        return False
    try:
        spoken = read_json(SPOKEN)
    except Exception as e:
        log({"event": "skip", "reason": f"unreadable:{type(e).__name__}"})
        SPOKEN.unlink(missing_ok=True)
        return True
    text = (spoken.get("text") or "").strip()
    mode = current_mode()
    approved = bool(spoken.get("approved"))          # REVIEW 에서 ⑥ --approve 로 승인된 발화
    if mode == "MUTE" or (mode != "LIVE" and not approved):
        # ⑥ 은 LIVE 에서만 spoken.json 을 쓰지만, 쓴 뒤에 모드가 내려갔을 수 있다.
        # 그 사이의 발화는 내보내지 않는다 — 진행자가 내린 모드가 이긴다.
        log({"event": "withheld", "reason": f"mode={mode}", "chars": len(text)})
        SPOKEN.unlink(missing_ok=True)
        print(f"  ⏸ 모드 {mode} — 발화 보류·소비 ({len(text)}자)")
        return True
    if not text:
        log({"event": "skip", "reason": "empty_text"})
        SPOKEN.unlink(missing_ok=True)
        return True
    tag = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S")
    print(f"  🔊 {text[:72]}")
    try:
        # 승인 발화는 REVIEW 상태에서 재생되므로 「LIVE 벗어나면 abort」 감시를 MUTE 기준으로 낮춘다
        res = speak(text, prov, provider_name, device, watch_mode=True, tag=tag,
                    stop_unless=("LIVE",) if not approved else ("LIVE", "REVIEW"))
        log({"event": "played", "text": text, "spoken_at": spoken.get("spoken_at"), **res})
        trace("spoken_player", ok=True, **{k: v for k, v in res.items() if k != "audio"})
        mark = "⛔ 중단" if res["aborted"] else "✅"
        print(f"     {mark} 합성 {res['synth_ms']}ms · 재생 {res['played_ms']}ms"
              + (f" · {res['abort_reason']}" if res["aborted"] else ""))
    except TTSUnavailable as e:
        log({"event": "failed", "reason": f"tts_unavailable:{e}", "text": text})
        print(f"     ⛔ TTS 사용 불가 — 침묵: {e}")
    except Exception as e:
        log({"event": "failed", "reason": f"{type(e).__name__}:{str(e)[:120]}", "text": text})
        print(f"     ⛔ 실패 — 침묵: {type(e).__name__}: {str(e)[:80]}")
    finally:
        SPOKEN.unlink(missing_ok=True)                     # 소비 = 삭제. 같은 말을 두 번 하지 않는다
    return True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--device", help="출력 장치 이름 일부 (예: 'CABLE Input', '헤드폰'). 기본: 시스템 기본")
    ap.add_argument("--provider", help="TTS 프로바이더 (기본: 레지스트리 default_provider)")
    ap.add_argument("--text", help="폴링 대신 이 문장을 바로 합성·재생하고 끝낸다 (헤드폰 테스트)")
    ap.add_argument("--once", action="store_true", help="spoken.json 1건만 처리하고 끝낸다")
    ap.add_argument("--list-devices", action="store_true")
    args = ap.parse_args()

    if args.list_devices:
        apis = {i: a["name"] for i, a in enumerate(sd.query_hostapis())}
        for i, d in enumerate(sd.query_devices()):
            if d["max_output_channels"] > 0:
                print(f"  [{i:>2}] {d['name'][:48]:<50} {apis.get(d['hostapi'],'')}  "
                      f"{int(d['default_samplerate'])}Hz")
        return 0

    device = pick_device(args.device)
    provider_name, prov = load_provider(args.provider)
    dev_name = sd.query_devices(device)["name"] if device is not None else "시스템 기본 출력"
    print(f"── spoken_player · {provider_name}/{prov.voice} → {dev_name}")

    if args.text:
        res = speak(args.text, prov, provider_name, device, watch_mode=False,
                    tag=datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S") + "_test")
        log({"event": "test", "text": args.text, **res})
        print(f"   ✅ 합성 {res['synth_ms']}ms · 오디오 {res['audio_s']}s · 재생 {res['played_ms']}ms")
        return 0

    print(f"   {SPOKEN.name} 폴링 중 ({int(POLL_S*1000)}ms) · 모드 {current_mode()} · Ctrl+C 로 종료")
    try:
        while True:
            if consume_one(prov, provider_name, device) and args.once:
                return 0
            time.sleep(POLL_S)
    except KeyboardInterrupt:
        print("\n   종료")
        return 0


if __name__ == "__main__":
    sys.exit(main())
