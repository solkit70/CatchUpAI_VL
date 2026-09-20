#!/usr/bin/env python3
"""4회차 리허설 드라이버 — rehearsal-log-4.md 의 질문 8개를 순서대로 넣는다.

데몬(`engine_daemon.Engine`)을 인프로세스로 띄워 `utter()` 를 부른다. 파트 전환은
`session_state.json` 을 바꾸는 것으로 핫키를 대신한다(핫키도 결국 이 파일만 바꾼다).
패닉 스톱은 `mode.json` → MUTE 로 대신한다(핫키 `panic()` 이 하는 일과 같다).

오버레이 서버·재생기는 **별도 프로세스**로 먼저 떠 있어야 한다.

실행:
    python rehearsal4_driver.py --live 28 --pause 10
"""
from __future__ import annotations

import argparse
import io
import json
import sys
import threading
import time
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path

HERE = Path(__file__).resolve().parent
TOPIC = HERE.parents[1]
M7 = TOPIC / "07-CoMC-Engine-POC" / "src"
M9 = TOPIC / "09-Desktop-Shell-and-Overlay" / "examples" / "engine"
for p in (M7, M9):
    sys.path.insert(0, str(p))

from common import now_iso, out, read_json, write_json  # noqa: E402
import engine_daemon as dm                                # noqa: E402

LOG = out("debug") / "rehearsal4" / "driver_log.jsonl"


def log(rec: dict):
    LOG.parent.mkdir(parents=True, exist_ok=True)
    with LOG.open("a", encoding="utf-8") as f:
        f.write(json.dumps({"ts": now_iso(), **rec}, ensure_ascii=False) + "\n")


def set_part(pid: str):
    ss = out("session_state.json")
    d = read_json(ss) if ss.exists() else {}
    d["current_part_id"] = pid          # 스키마 밖 필드를 넣지 않는다 — 핫키가 검증하다 죽는다 (CVL 2 실사고)
    write_json(ss, d)


def set_mode(mode: str, reason: str):
    write_json(out("mode.json"), {"mode": mode, "reason": reason, "changed_at": now_iso()})


def snapshot() -> dict:
    ov = read_json(out("overlay.json")) if out("overlay.json").exists() else {}
    vd = read_json(out("verdict.json")) if out("verdict.json").exists() else {}
    it = read_json(out("intent.json")) if out("intent.json").exists() else {}
    return {"overlay_text": (ov.get("text") or "")[:160], "overlay_cleared_by": ov.get("cleared_by"),
            "intent": it.get("intent"), "pass": vd.get("pass"),
            "kept": len(vd.get("kept_sentences", [])), "dropped": [d["reason"] for d in vd.get("dropped_sentences", [])],
            "violations": [v["rule_id"] for v in vd.get("violations", [])],
            "final_text": (vd.get("final_text") or "")[:200]}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--live", default="28")
    ap.add_argument("--pause", type=float, default=10.0)
    ap.add_argument("--only", help="예: 1,2,3")
    args = ap.parse_args()
    live = args.live
    only = {int(x) for x in args.only.split(",")} if args.only else None

    with redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
        eng = dm.Engine()
        set_part("2")
        pre = eng.prewarm(live, part="2")
    print(f"엔진 기동 {eng.warmup_ms}ms · prewarm {pre}")
    log({"event": "start", "live": live, "prewarm": pre})

    def ask(n: int, q: str, note: str = "") -> dict:
        t0 = time.time()
        # 옛 결과가 남아 있으면 판독이 헷갈린다 — 질문 전에 지운다 (overlay 는 지우지 않는다: 사고 11 검증 대상)
        for f in ("verdict.json", "intent.json", "answer_draft.json"):
            p = out(f)
            if p.exists():
                p.unlink()
        r = eng.utter(live, q)
        snap = snapshot()
        rec = {"event": "utter", "n": n, "q": q, "note": note, "result": r, **snap,
               "wall_ms": round((time.time() - t0) * 1000)}
        log(rec)
        ok = "✅" if r.get("ok") else f"⛔ {r.get('failed_at')}"
        print(f"\n[{n}] {q}   ({note})")
        print(f"    {ok} {r.get('total_ms')}ms  stages={r.get('per_stage')}")
        print(f"    intent={snap['intent']} pass={snap['pass']} kept={snap['kept']} dropped={snap['dropped']} viol={snap['violations']}")
        print(f"    overlay: {snap['overlay_text'] or '(비어 있음)'}"
              + (f"   [cleared_by {snap['overlay_cleared_by']}]" if snap["overlay_cleared_by"] and not snap["overlay_text"] else ""))
        return rec

    def pause(sec=None):
        time.sleep(args.pause if sec is None else sec)

    def want(n): return only is None or n in only

    if want(1): ask(1, "오늘 2부에서 뭘 다루나요?", "사고 8 — 확정을 확정으로"); pause()
    if want(2): ask(2, "CoMC 앱은 어디까지 왔나요?", "사고 9 — 상태 어휘"); pause()
    if want(3): ask(3, "주간 영상은 뭐예요?", "사고 10 — 침묵 + 빈 화면"); pause()
    if want(4):
        set_part("1")
        ask(4, "지금 파트에서 뭘 하나요?", "사고 7a — 1부(미정)로 전환 → ② 거절·침묵")
        pause(4)
        set_part("2")
        ask(4, "2부 첫 항목이 뭐죠?", "사고 7b — 2부로 복귀 → ② 재실행 후 답")
        pause()
    if want(5): ask(5, "음 그러니까 저기", "사고 11 — unknown 거절 + 빈 화면"); pause()

    if want(6) or want(7) or want(8):
        set_mode("LIVE", "4회차 소리 구간")
        print("\n── 모드 LIVE — 이제부터 소리가 납니다 (Buds · OBS 미터 확인)")
        pause(2)
    if want(6):
        rec = ask(6, "오늘 2부 첫 번째 실험은 뭔가요?", "B — 소리")
        pause(args.pause + 15)                          # 재생 시간
    if want(7):
        # 재생 시작 후 3.5초 뒤 MUTE — 핫키 패닉이 하는 일과 같다
        def panic():
            time.sleep(3.5 + 3.0)                       # 합성 ~2.5s 뒤 재생 시작 → 3.5s 재생 뒤 끊는다
            set_mode("MUTE", "패닉 스톱 (4회차 드라이버 — Ctrl+Alt+Space 대신)")
            log({"event": "panic", "mode": "MUTE"})
        th = threading.Thread(target=panic, daemon=True)
        rec = ask(7, "오늘 2부에서 CoMC 앱은 무엇을 하나요?", "B 패닉 — 재생 중 MUTE")
        th.start()
        pause(args.pause + 8)
        set_mode("LIVE", "패닉 해제 — 4회차 계속")
        pause(2)
    if want(8):
        rec = ask(8, "Chrome Remote Desktop 은 오늘 뭘 보여 주나요?", "사고 4·길이 — 어미·재생 초")
        pause(args.pause + 20)

    set_mode("REVIEW", "4회차 끝 — 기본은 REVIEW")
    print("\n── 끝. 모드 REVIEW 로 복귀. 로그:", LOG)
    return 0


if __name__ == "__main__":
    sys.exit(main())
