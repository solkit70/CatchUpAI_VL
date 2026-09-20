#!/usr/bin/env python3
"""Live #27 사고 7·8·9·10·11 재현 테스트 — 수정 전 실패 / 수정 후 통과 대조.

M8 원칙: *"게이트를 꺼도 같은 결과가 나온다면 아무것도 확인하지 않은 것이다."*
고쳤다는 주장에는 **고치기 전에 실패하고 후에 통과하는 대조**가 있어야 한다.
그래서 이 파일은 수정 전 코드(git stash)와 수정 후 코드로 각각 한 번씩 돌린다.

LLM 을 부르지 않는다. ②⑤⑥ 과 데몬의 파트 전환은 전부 규칙·파일이라 결정적이다.
사고 8·9·10 의 ④ 프롬프트 변경은 확률을 옮기는 것이라 여기서 재지 않는다 — 그 하한은
⑤ 가 만들고, 이 테스트는 그 하한을 잰다.

실행:
    python test_live27_incidents.py --live 28
"""
from __future__ import annotations

import argparse
import importlib.util
import io
import json
import sys
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path

HERE = Path(__file__).resolve().parent
TOPIC = HERE.parents[1]
M7 = TOPIC / "07-CoMC-Engine-POC" / "src"
M9 = TOPIC / "09-Desktop-Shell-and-Overlay" / "examples" / "engine"
sys.path.insert(0, str(M7))

from common import out, read_json, write_json  # noqa: E402


def load(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def run_main(mod, argv: list[str]) -> int:
    saved = sys.argv
    sys.argv = [mod.__name__, *argv]
    try:
        with redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
            return mod.main() or 0
    except SystemExit as e:
        return e.code if isinstance(e.code, int) else (0 if e.code is None else 1)
    finally:
        sys.argv = saved


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--live", default="28")
    ap.add_argument("--part", default="2")
    args = ap.parse_args()
    live, part = args.live, args.part

    m01 = load(M7 / "01_parse_rundown.py", "t_01")
    m02 = load(M7 / "02_resolve_context.py", "t_02")
    m04 = load(M7 / "04_compose_answer.py", "t_04")
    m05 = load(M7 / "05_verify_and_gate.py", "t_05")
    m06 = load(M7 / "06_render_output.py", "t_06")
    results: list[tuple[str, bool, str]] = []

    def check(name, cond, detail=""):
        results.append((name, bool(cond), detail))

    run_main(m01, ["--live", live])
    code = run_main(m02, ["--live", live, "--part", part])
    ctx = read_json(out(f"broadcast_context.{live}.json"))
    quotes = [e["quote"] for e in ctx["evidence_pool"]]

    # ── 사고 8 — 근거 풀에 확정이 있고 「후보」 제목이 없는가 ───────────────
    has_confirmed = any(q.startswith("[확정]") for q in quotes)
    bare_candidate = any(q.strip() == "후보" or q.startswith("후보 (") for q in quotes)
    check("사고8 근거 풀에 [확정] 커버리지 줄", has_confirmed, f"{sum(q.startswith('[확정]') for q in quotes)}건")
    check("사고8 근거 풀에 「후보」 제목 없음", not bare_candidate)
    check("사고9 확정 항목의 현재 상태 행", any(q.startswith("[확정 항목 현재 상태]") for q in quotes))

    policy = read_json(TOPIC / "03-Data-Contracts-and-Safety" / "examples" / "safety_policy.json")
    ev0 = ctx["evidence_pool"][0]
    item = ctx["coverage_items"][-1]

    def draft(sentences):
        return {"provider": "test", "sentences": sentences,
                "claim_map": [{"sentence_idx": i, "evidence_path": ev0["path"],
                               "evidence_quote": ev0["quote"]} for i in range(len(sentences))],
                "coverage_state": ctx["coverage_state"], "length_sentences": len(sentences),
                "created_at": "2026-09-17T00:00:00", "_length_level": "default"}

    # ── 사고 10 — 다른 파트 질문 → 전부 cross_part ────────────────────────
    other = next((p for p in ctx.get("other_parts", []) if "주간 영상" in p["title"]), None)
    q10 = "주간 영상은 뭐예요?"
    v = m05.verify(draft([f"이번 주 영상은 {item} 입니다."]), ctx, policy, question=q10)
    check("사고10 다른 파트 질문 → 전부 드롭(cross_part)",
          not v["kept_sentences"] and any(d["reason"] == "cross_part" for d in v["dropped_sentences"]),
          f"kept={len(v['kept_sentences'])} other_parts={'있음' if other else '없음'}")
    v = m05.verify(draft([f"이번 방송에서는 {item} 을 다룹니다."]), ctx, policy, question="2부에서 뭐 해요?")
    check("사고10 현재 파트 질문은 통과", v["kept_sentences"] == [0], f"kept={v['kept_sentences']}")

    # ── 사고 9 — 상태 질문에 이름만 → content_empty ───────────────────────
    q9 = "CoMC 앱 어디까지 왔나요?"
    v = m05.verify(draft([f"{item} 을 다룹니다."]), ctx, policy, question=q9)
    check("사고9 상태 질문에 이름만 → content_empty", not v["pass"]
          and any(x["rule_id"] == "content_empty" for x in v["violations"]))
    v = m05.verify(draft([f"{item} 은 이번 방송 확정으로 진행 중입니다."]), ctx, policy, question=q9)
    check("사고9 상태 어휘가 있으면 통과", v["pass"], f"pass={v['pass']}")

    # ── 사고 11 — 침묵·거절 뒤 overlay 가 비는가 ───────────────────────────
    write_json(out("overlay.json"), {"text": "옛 초안이 남아 있다", "part_id": part,
                                     "updated_at": "2026-09-13T05:00:00"})
    write_json(out("verdict.json"), {"pass": False, "absence_by_closure": [], "final_text": "",
                                     "kept_sentences": [], "dropped_sentences": [
                                         {"sentence_idx": 0, "reason": "no_evidence"}],
                                     "violations": [], "length_after": 0,
                                     "verified_at": "2026-09-17T00:00:00"})
    run_main(m06, ["--live", live])
    ov = read_json(out("overlay.json"))
    check("사고11 ⑥ 침묵 → overlay text 비움", ov.get("text") == "", f"text={ov.get('text')!r}")

    write_json(out("overlay.json"), {"text": "옛 초안이 남아 있다", "part_id": part,
                                     "updated_at": "2026-09-13T05:00:00"})
    write_json(out("intent.json"), {"intent": "unknown", "confidence": 0.0, "slots": {},
                                    "ambiguity_flags": [], "transcript": "음 그러니까 저기",
                                    "classified_at": "2026-09-17T00:00:00"})
    run_main(m04, ["--live", live])
    ov = read_json(out("overlay.json"))
    check("사고11 ④ 거절(unknown) → overlay text 비움", ov.get("text") == "", f"text={ov.get('text')!r}")

    # ── 사고 7 — 데몬이 파트 전환을 스스로 반영하는가 ─────────────────────
    ss_path = out("session_state.json")
    ss_backup = ss_path.read_text(encoding="utf-8") if ss_path.exists() else None
    try:
        sys.path.insert(0, str(M9))
        dm = load(M9 / "engine_daemon.py", "t_daemon")
        with redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
            eng = dm.Engine()
            write_json(ss_path, {"current_part_id": part})
            pre = eng.prewarm(live, part=part)
            other_id = next((p["id"] for p in ctx.get("other_parts", [])
                             if p["coverage_state"] == "defined"), None) or "1"
            write_json(ss_path, {"current_part_id": other_id})
            # ④ 가 LLM 을 부르기 전에 멈추도록 다른 파트를 묻는 문장을 넣는다.
            r = eng.utter(live, "주간 영상은 뭐예요?")
        # 전환 대상 파트가 undefined 면 ② 가 (옳게) 거절한다 — 그래도 「② 를 다시 돌렸다」는
        # 사실이 사고 7 의 수정이다. 성공/거절 어느 쪽이든 ② 가 다시 불렸는지를 본다.
        switched = "②" in r.get("per_stage", {}) and (
            "part_switch" in r.get("per_stage", {}) or r.get("part_switch"))
        ctx_after = read_json(out(f"broadcast_context.{live}.json")) if pre.get("ok") else {}
        check("사고7 파트 전환 뒤 발화 → ② 재실행", switched,
              f"per_stage={list(r.get('per_stage', {}).keys())} ctx.part={ctx_after.get('current_part_id')}")
    finally:
        if ss_backup is not None:
            ss_path.write_text(ss_backup, encoding="utf-8")
        run_main(m02, ["--live", live, "--part", part])

    ok = sum(1 for _, c, _ in results if c)
    print(f"\n=== Live #27 사고 재현 테스트 — Live{live} {part}부 · {ok}/{len(results)} 통과 ===\n")
    for name, cond, detail in results:
        print(f"  {'✅' if cond else '❌'} {name}" + (f"   ({detail})" if detail else ""))
    return 0 if ok == len(results) else 1


if __name__ == "__main__":
    sys.exit(main())
