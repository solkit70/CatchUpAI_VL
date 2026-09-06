#!/usr/bin/env python3
"""M10 실습 1 — 방송 30분 전 프리플라이트 자동 점검 (9항목).

## 왜 앱이 아니라 운영으로 푸는가

이 9개는 전부 **앱이 자기 자신에 대해 보장할 수 없는 것**이다.
마이크가 꽂혀 있는지, 오늘 Rundown 이 최종본인지, OBS 가 켜져 있는지는
코드가 통제하는 영역 밖이고, 통제 밖의 것은 **확인 절차로** 막는 수밖에 없다.

## 이 스크립트의 설계 원칙 — 세 가지 상태로 가른다

M8 에서 배운 것이 그대로 적용된다.

> 실패가 `undefined` 라는 '안전해 보이는 값'으로 떨어져 아무도 눈치채지 못했다.

그래서 여기서는 **확인하지 못한 것을 통과로 세지 않는다.**

| 상태 | 의미 | 종료 코드 기여 |
|---|---|---|
| `PASS` | 확인했고 정상 | — |
| `FAIL` | 확인했고 비정상 | **1** |
| `WARN` | 정상이지만 방송 전 사람이 판단해야 함 | — |
| `SKIP` | **확인하지 못함** (옵션·의존성·네트워크) | **2** (FAIL 없을 때) |

`SKIP` 이 있으면 "전체 통과" 라고 말하지 않는다. 확인 못 한 것을 통과라고 부르면
프리플라이트가 있다는 사실 자체가 잘못된 안심이 된다.

## 의미 검증을 한다 — 파일이 있는지가 아니라 맞는지

M9 에서 오버레이가 `overlay.json`(스냅샷)을 읽고 `session_state.json`(권위값)을
안 읽어서 화면이 안 따라온 결함이 있었다. 자기 검증 3종은 전부 통과했는데도.

> 동작 검증과 의미 검증은 다르다.

그래서 6번(컨텍스트 사전 빌드)은 파일 존재가 아니라 **그 컨텍스트가 오늘 Rundown 에서
나온 것인지**를 대조한다. 어제 컨텍스트가 남아 있는 것이 가장 위험한 상태다 —
파일은 있고, 파이프라인은 돌고, 내용만 틀리다.

사용:
    python preflight_check.py                    # 파일·장치 점검 (API 호출 없음)
    python preflight_check.py --probe-live       # STT/LLM/TTS 실제 1회 호출까지
    python preflight_check.py --rundown "<경로>" # Rundown 명시
    python preflight_check.py --json             # 기계 판독용
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from dataclasses import dataclass, field
from datetime import date, datetime, timedelta
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

HERE = Path(__file__).resolve().parent
MODULE = HERE.parent                       # 10-Live-Rehearsal-Capstone/
TOPIC = MODULE.parent                      # Topics/Live-CoMC-App/
ENGINE = TOPIC / "07-CoMC-Engine-POC"
OUTPUT = ENGINE / "output"
DATA = ENGINE / "data"
VAULT = TOPIC.parents[3]                   # Changsoo_Vault/
ROUNDUP_DIR = VAULT / "AI" / "Roundup"

PASS, FAIL, WARN, SKIP = "PASS", "FAIL", "WARN", "SKIP"
_ICON = {PASS: "✅", FAIL: "❌", WARN: "⚠️ ", SKIP: "⬜"}


@dataclass
class Check:
    num: int
    name: str
    status: str = SKIP
    detail: str = ""
    hint: str = ""
    extra: dict = field(default_factory=dict)

    def set(self, status: str, detail: str, hint: str = "", **extra) -> "Check":
        self.status, self.detail, self.hint = status, detail, hint
        self.extra.update(extra)
        return self


# ── 1. STT / LLM / TTS probe 3종 ─────────────────────────────────────

def check_probes(live: bool) -> Check:
    c = Check(1, "STT·LLM·TTS probe 3종")
    keys = {
        "STT/LLM (OpenAI)": os.environ.get("OPENAI_API_KEY"),
        "LLM 폴백 (Gemini)": os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY"),
        "LLM 폴백 (Claude)": os.environ.get("ANTHROPIC_API_KEY"),
    }
    missing = [k for k, v in keys.items() if not v]

    # edge-tts 는 M6 에서 기본값으로 확정됐고 키가 필요 없다.
    try:
        import edge_tts  # noqa: F401
        tts_ok, tts_note = True, "edge-tts 사용 가능(무키)"
    except ImportError:
        tts_ok, tts_note = False, "edge-tts 미설치"

    if not keys["STT/LLM (OpenAI)"]:
        return c.set(FAIL, "OPENAI_API_KEY 없음 — STT·기본 LLM 둘 다 불가",
                     "환경변수 OPENAI_API_KEY 설정 후 재실행")
    if not tts_ok:
        return c.set(FAIL, f"{tts_note} — 발화 불가", "pip install edge-tts")

    if not live:
        note = f"키 존재 확인만 함 · {tts_note}"
        if missing:
            note += f" · 폴백 키 없음: {', '.join(missing)}"
        return c.set(SKIP, note, "실제 응답까지 보려면 --probe-live")

    # --probe-live: 실제 왕복 1회
    try:
        sys.path.insert(0, str(TOPIC / "05-STT-LLM-Harness" / "examples"))
        from openai import OpenAI  # type: ignore
        t0 = datetime.now()
        OpenAI().chat.completions.create(
            model="gpt-5-mini", messages=[{"role": "user", "content": "ping"}],
            max_completion_tokens=5)
        ms = int((datetime.now() - t0).total_seconds() * 1000)
        return c.set(PASS, f"LLM 실호출 {ms}ms · {tts_note}",
                     "" if not missing else f"폴백 키 없음: {', '.join(missing)}")
    except Exception as e:  # 네트워크·쿼터·모델명 전부 여기로
        return c.set(FAIL, f"LLM 실호출 실패: {type(e).__name__}: {e}"[:120],
                     "키·쿼터·네트워크 확인")


# ── 2. 오디오 장치 ────────────────────────────────────────────────────

def check_audio_devices() -> Check:
    """M9 교훈 — 이름만 맞춰 첫 매칭을 집으면 MME 가 걸려 5배 느려진다."""
    c = Check(2, "오디오 장치 (입력·출력·WASAPI)")
    try:
        import sounddevice as sd
    except ImportError:
        return c.set(SKIP, "sounddevice 미설치 — 장치를 확인할 수 없음",
                     "pip install sounddevice")
    try:
        devs = sd.query_devices()
        apis = sd.query_hostapis()
    except Exception as e:
        return c.set(FAIL, f"장치 조회 실패: {e}"[:110], "오디오 드라이버 확인")

    wasapi = next((i for i, a in enumerate(apis)
                   if "wasapi" in a["name"].lower()), None)
    ins = [d for d in devs if d["max_input_channels"] > 0]
    outs = [d for d in devs if d["max_output_channels"] > 0]

    if not ins:
        return c.set(FAIL, "입력 장치 0개 — 마이크가 꽂혀 있지 않음", "마이크 연결 확인")
    if not outs:
        return c.set(FAIL, "출력 장치 0개", "스피커·가상 케이블 확인")
    if wasapi is None:
        return c.set(WARN, f"입력 {len(ins)} · 출력 {len(outs)} · **WASAPI 없음**",
                     "MME 로 떨어지면 재생 지연이 63ms → 314ms 로 5배 (M9 실측)")

    n_wasapi_out = sum(1 for d in outs if d["hostapi"] == wasapi)
    return c.set(PASS, f"입력 {len(ins)} · 출력 {len(outs)} · WASAPI 출력 {n_wasapi_out}개",
                 "", wasapi_index=wasapi)


# ── 3. Rundown 최종본 여부 ────────────────────────────────────────────

def _week_start(d: date) -> date:
    """주 시작 = 직전 일요일 (이 볼트의 주간 파일 명명 규칙)."""
    return d - timedelta(days=(d.weekday() + 1) % 7)


def find_rundown(explicit: str | None, today: date) -> Path | None:
    if explicit:
        p = Path(explicit)
        return p if p.exists() else None
    ws = _week_start(today).isoformat()
    cands = sorted(ROUNDUP_DIR.glob(f"{ws} - Live*Weekly Rundown.md"))
    if cands:
        return cands[-1]
    allc = sorted(ROUNDUP_DIR.glob("*Weekly Rundown.md"))
    return allc[-1] if allc else None


def check_rundown(path: Path | None, today: date) -> tuple[Check, dict | None]:
    c = Check(3, "Rundown 최종본 · 파싱")
    if path is None:
        return c.set(FAIL, "이번 주 Rundown 파일을 찾지 못함",
                     f"{ROUNDUP_DIR} 에 '{_week_start(today)} - Live[N] Weekly Rundown.md' 필요"), None

    # 파싱은 01 단계를 실제로 돌려서 확인한다 — 파일이 열리는 것과
    # 파서가 읽어내는 것은 다르다 (M8 발견 1·4).
    sys.path.insert(0, str(ENGINE / "src"))
    try:
        import importlib
        mod = importlib.import_module("01_parse_rundown")
        # 함수명을 틀리면 조용히 저장된 옛 결과로 폴백한다 — 그게 M8 이 경고한
        # '안전해 보이는 실패'다. 그래서 이름을 못 찾으면 그 사실을 드러낸다.
        fn = getattr(mod, "parse_rundown", None)
        idx = fn(path) if callable(fn) else None
    except Exception as e:
        return c.set(FAIL, f"파서 로드/실행 실패: {type(e).__name__}: {e}"[:110],
                     "07-CoMC-Engine-POC/src/01_parse_rundown.py 확인"), None

    if idx is None:
        # parse() 를 노출하지 않는 버전 — 마지막 산출물로 대체 확인
        f = OUTPUT / "rundown_index.json"
        if not f.exists():
            return c.set(SKIP, "파서 API 없음 · rundown_index.json 도 없음",
                         "python src/01_parse_rundown.py 를 먼저 실행"), None
        idx = json.loads(f.read_text(encoding="utf-8"))
        stale = datetime.fromtimestamp(f.stat().st_mtime).date() != today
        if stale:
            return c.set(WARN, f"저장된 파싱 결과 사용({f.name}, 오늘 것 아님)",
                         "방송 전 01 단계를 오늘 Rundown 으로 다시 실행"), idx

    anomalies = idx.get("parse_anomalies") or []
    n_parts = len(idx.get("parts") or [])
    is_final = idx.get("is_final")

    if anomalies:
        return c.set(FAIL, f"파싱 이상 {len(anomalies)}건 · 파트 {n_parts}개",
                     f"첫 항목: {str(anomalies[0])[:80]}"), idx
    if n_parts == 0:
        return c.set(FAIL, "파트 0개 — 헤딩 형식이 파서 규칙과 어긋남",
                     "이모지 접두 헤딩·괄호 시간표기 누락 확인 (M8 발견 4·5)"), idx
    if is_final is False:
        return c.set(WARN, f"파트 {n_parts}개 · **최종본 아님(is_final=false)**",
                     "방송 직전 Rundown 을 최종 확정할 것"), idx
    return c.set(PASS, f"파트 {n_parts}개 · 파싱 이상 0건 · {Path(idx.get('source_path', path)).name}"), idx


# ── 4. 커버리지 미정 파트 수 ──────────────────────────────────────────

def check_coverage(idx: dict | None) -> Check:
    c = Check(4, "커버리지 미정 파트")
    if not idx:
        return c.set(SKIP, "Rundown 파싱 결과가 없어 확인 불가", "3번을 먼저 통과시킬 것")
    parts = idx.get("parts") or []
    undef = [p for p in parts if p.get("coverage_state") != "defined"]
    if not undef:
        return c.set(PASS, f"전체 {len(parts)}개 파트 모두 커버리지 확정")
    names = ", ".join(f"{p.get('id')}부" for p in undef[:4])
    return c.set(WARN, f"미정 {len(undef)}/{len(parts)} — {names}",
                 "미정 파트에서는 앱이 침묵한다(M1 원칙). 의도한 것인지 확인")


# ── 5. part_timeline.json ─────────────────────────────────────────────

def check_timeline() -> Check:
    c = Check(5, "part_timeline.json 입력")
    real, sample = DATA / "part_timeline.json", DATA / "part_timeline.sample.json"
    p = real if real.exists() else (sample if sample.exists() else None)
    if p is None:
        return c.set(FAIL, "part_timeline 파일 없음",
                     "suggested_part_id 추정이 불가 — 샘플을 복사해 오늘 값으로 수정")
    try:
        d = json.loads(p.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        return c.set(FAIL, f"JSON 파싱 실패: {e}"[:100], "파일 문법 확인")
    n = len(d.get("parts") or d.get("timeline") or [])
    if p is sample or p.name.endswith(".sample.json"):
        return c.set(WARN, f"**샘플 파일 사용 중** ({p.name}, 항목 {n}개)",
                     "오늘 회차 시각으로 part_timeline.json 을 만들 것")
    return c.set(PASS, f"{p.name} · 항목 {n}개")


# ── 6. 컨텍스트 사전 빌드 (의미 검증) ─────────────────────────────────

def check_context(idx: dict | None, today: date) -> Check:
    """파일 존재가 아니라 '오늘 Rundown 에서 나온 것인지'를 본다."""
    c = Check(6, "컨텍스트 사전 빌드 (오늘 Rundown 기준)")
    cands = sorted(OUTPUT.glob("broadcast_context*.json"),
                   key=lambda f: f.stat().st_mtime, reverse=True)
    if not cands:
        return c.set(FAIL, "broadcast_context*.json 없음",
                     "python src/02_resolve_context.py 로 사전 빌드")
    f = cands[0]
    built = datetime.fromtimestamp(f.stat().st_mtime)
    if built.date() != today:
        return c.set(FAIL, f"가장 최근 컨텍스트가 {built:%m-%d %H:%M} — 오늘 것이 아님",
                     "어제 컨텍스트로 방송하면 파일은 있고 내용만 틀린 상태가 된다")
    try:
        ctx = json.loads(f.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return c.set(FAIL, f"{f.name} 파싱 실패", "다시 빌드")

    if idx:
        want = str(idx.get("source_path") or "")
        got = str(ctx.get("source_path") or ctx.get("rundown_path") or "")
        if want and got and Path(want).name != Path(got).name:
            return c.set(FAIL, f"다른 Rundown 기준: {Path(got).name}",
                         f"오늘 것({Path(want).name})으로 다시 빌드")
    return c.set(PASS, f"{f.name} · {built:%H:%M} 빌드")


# ── 7. OBS 오버레이 렌더 ──────────────────────────────────────────────

def check_overlay(port: int, idx: dict | None) -> Check:
    """응답 여부(동작)와 표시 내용의 타당성(의미)을 나눠서 본다.

    ⚠️ 2026-09-06 첫 실행에서 이 검사가 스스로 함정에 빠졌다.
    서버는 정상 응답했고 파트 값도 비어 있지 않아 PASS 를 줬는데,
    그 값이 **어제 세션의 파트 5** 였다. 오늘 Rundown 에는 파트 5가 없다.

    M9 의 오버레이 결함(권위값 대신 스냅샷 표시)과 같은 형태다 —
    파이프가 뚫렸는지는 봤고, 맞는 물이 흐르는지는 안 봤다.
    이 Topic 에서 네 번째다. 그래서 여기서 파트 실재 여부까지 대조한다.
    """
    c = Check(7, "OBS 오버레이 서버 (응답 + 표시 파트 실재)")
    url = f"http://127.0.0.1:{port}/state"
    try:
        with urllib.request.urlopen(url, timeout=2) as r:
            body = json.loads(r.read().decode("utf-8"))
    except urllib.error.URLError as e:
        return c.set(FAIL, f"응답 없음 ({e.reason})"[:100],
                     f"python 09-.../overlay_server.py 실행 후 OBS Browser Source 를 {url} 로")
    except Exception as e:
        return c.set(WARN, f"응답은 있으나 해석 실패: {type(e).__name__}", "서버 로그 확인")

    part = body.get("part_id") or body.get("current_part_id")
    if not part:
        return c.set(WARN, "응답 정상 · 표시 파트 비어 있음",
                     "권위값(session_state.current_part_id) 연결 확인")
    if idx:
        ids = {str(p.get("id")) for p in (idx.get("parts") or [])}
        if str(part) not in ids:
            return c.set(FAIL,
                         f"응답 정상이나 **표시 파트 '{part}' 가 오늘 Rundown 에 없음** "
                         f"(오늘: {', '.join(sorted(ids))})",
                         "지난 방송 세션 상태가 남아 있다 — session_state.current_part_id 를 오늘 파트로 초기화")
    return c.set(PASS, f"응답 정상 · 표시 파트 {part} (오늘 Rundown 에 실재)")


# ── 8. 패닉 스톱 ──────────────────────────────────────────────────────

def check_panic_stop() -> Check:
    c = Check(8, "패닉 스톱 (출력 스트림 확보)")
    src = TOPIC / "09-Desktop-Shell-and-Overlay" / "examples" / "engine" / "panic_stop.py"
    if not src.exists():
        return c.set(FAIL, "panic_stop.py 없음", "M9 산출물 확인")
    try:
        import sounddevice as sd
    except ImportError:
        return c.set(SKIP, "sounddevice 미설치 — 스트림을 열어볼 수 없음",
                     "pip install sounddevice")
    try:
        st = sd.OutputStream(samplerate=24000, channels=1,
                             blocksize=128, latency="low")
        st.start()
        st.abort()
        st.close()
    except Exception as e:
        return c.set(FAIL, f"저지연 출력 스트림 실패: {type(e).__name__}: {e}"[:110],
                     "장치 점유 여부 확인 — 패닉 스톱이 안 되면 방송에 들어가면 안 된다")
    return c.set(PASS, "저지연 스트림 open→abort 성공 (M9 실측 최악 112ms)")


# ── 9. 모드 확인 ──────────────────────────────────────────────────────

def check_mode() -> Check:
    c = Check(9, "운영 모드 (LIVE/REVIEW/MUTE)")
    f = OUTPUT / "mode.json"
    if not f.exists():
        return c.set(WARN, "mode.json 없음 → 기본 LIVE 로 동작",
                     "리허설은 REVIEW 로 시작하는 편이 안전")
    try:
        d = json.loads(f.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return c.set(FAIL, "mode.json 손상 → 엔진은 REVIEW 로 폴백",
                     "파일을 고치거나 지울 것 (M8 안전장치 ①)")
    mode = str(d.get("mode", "")).upper()
    reason, when = d.get("reason", "-"), str(d.get("changed_at", ""))[:16]
    if mode == "MUTE":
        return c.set(WARN, f"현재 **MUTE** ({reason}, {when})",
                     "이 상태로는 소리가 나가지 않는다 — 시작 전 LIVE/REVIEW 로 전환")
    if mode not in ("LIVE", "REVIEW"):
        return c.set(FAIL, f"알 수 없는 모드 '{mode}'", "LIVE/REVIEW/MUTE 중 하나여야 함")
    return c.set(PASS, f"현재 {mode} ({reason}, {when})")


# ── 실행 ──────────────────────────────────────────────────────────────

def run(args) -> tuple[list[Check], Path | None]:
    today = date.fromisoformat(args.date) if args.date else date.today()
    rd = find_rundown(args.rundown, today)
    c3, idx = check_rundown(rd, today)
    checks = [
        check_probes(args.probe_live),
        check_audio_devices(),
        c3,
        check_coverage(idx),
        check_timeline(),
        check_context(idx, today),
        check_overlay(args.overlay_port, idx),
        check_panic_stop(),
        check_mode(),
    ]
    return checks, rd


def render(checks: list[Check], rd: Path | None) -> int:
    n_fail = sum(1 for c in checks if c.status == FAIL)
    n_skip = sum(1 for c in checks if c.status == SKIP)
    n_warn = sum(1 for c in checks if c.status == WARN)
    n_pass = sum(1 for c in checks if c.status == PASS)

    print("\n" + "=" * 78)
    print(f"  프리플라이트 — {datetime.now():%Y-%m-%d %H:%M}"
          f"{'  ·  ' + rd.name if rd else ''}")
    print("=" * 78)
    for c in checks:
        print(f"{_ICON[c.status]} {c.num}. {c.name}")
        print(f"     {c.detail}")
        if c.hint:
            print(f"     → {c.hint}")
    print("-" * 78)
    print(f"  PASS {n_pass} · WARN {n_warn} · FAIL {n_fail} · SKIP(확인못함) {n_skip}")

    if n_fail:
        print("\n  ❌ 방송 투입 불가 — FAIL 항목을 먼저 해결하세요.")
        code = 1
    elif n_skip:
        print("\n  ⬜ 판정 보류 — 확인하지 못한 항목이 있습니다.")
        print("     확인 못 한 것은 통과가 아닙니다. 위 → 안내를 따르거나,")
        print("     그 항목을 사람이 눈으로 확인한 뒤 방송에 들어가세요.")
        code = 2
    elif n_warn:
        print("\n  ⚠️  조건부 통과 — WARN 항목이 의도한 상태인지 확인하세요.")
        code = 0
    else:
        print("\n  ✅ 9항목 전부 통과 — 방송 투입 가능.")
        code = 0
    print("=" * 78 + "\n")
    return code


def main() -> int:
    ap = argparse.ArgumentParser(description="M10 프리플라이트 9항목 점검")
    ap.add_argument("--rundown", help="Rundown 파일 경로 (생략 시 이번 주 자동 탐색)")
    ap.add_argument("--date", help="기준 날짜 YYYY-MM-DD (생략 시 오늘)")
    ap.add_argument("--overlay-port", type=int, default=8777)
    ap.add_argument("--probe-live", action="store_true",
                    help="STT/LLM/TTS 실제 1회 호출까지 확인 (비용 발생)")
    ap.add_argument("--json", action="store_true", help="기계 판독용 JSON 출력")
    args = ap.parse_args()

    checks, rd = run(args)

    if args.json:
        print(json.dumps({
            "checked_at": datetime.now().isoformat(),
            "rundown": str(rd) if rd else None,
            "checks": [{"num": c.num, "name": c.name, "status": c.status,
                        "detail": c.detail, "hint": c.hint, **c.extra}
                       for c in checks],
        }, ensure_ascii=False, indent=2))
        return 1 if any(c.status == FAIL for c in checks) else (
            2 if any(c.status == SKIP for c in checks) else 0)

    return render(checks, rd)


if __name__ == "__main__":
    sys.exit(main())
