#!/usr/bin/env python3
"""M8 실습 1 — 안전장치 시나리오 러너.

## 무엇을 하는가

M7 의 6단계 파이프라인을 시나리오마다 처음부터 돌리고, **기대한 대로 막혔는지**를
확인한다. 통과 여부가 아니라 *올바른 이유로* 통과·차단됐는지를 본다.

## 왜 통과율을 세지 않는가

안전장치는 통과율이 높다고 잘 도는 것이 아니다. 6개 시나리오 중 4개가 차단되는 것이
정상이고, 그 4개가 **각각 다른 이유로** 차단돼야 한다. 이유가 뭉뚱그려지면
"막히긴 하는데 왜 막히는지 모르는" 상태가 되고, 그때부터는 고칠 수 없다.

## 산출물을 시나리오별로 분리하는 이유

6단계는 `output/` 의 같은 파일 이름을 쓴다(intent.json, answer_draft.json …).
다음 시나리오가 덮어쓰면 사고가 났을 때 볼 것이 남지 않는다.
매 시나리오가 끝나면 `output/scenarios/{name}/` 으로 복사한다.

실행:
    python run_scenarios.py                    # 6개 전부
    python run_scenarios.py --only normal
    python run_scenarios.py --list
"""
from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
MODULE = HERE.parent                                  # 08-Safety-Gate-Scenarios/
TOPIC = MODULE.parent                                 # Topics/Live-CoMC-App/
POC = TOPIC / "07-CoMC-Engine-POC"
SRC = POC / "src"
OUTPUT = POC / "output"
SCEN_OUT = OUTPUT / "scenarios"

sys.path.insert(0, str(HERE))
sys.path.insert(0, str(SRC))

from scenarios import FORBIDDEN_PROBES, SCENARIOS  # noqa: E402

# 각 시나리오가 끝나면 보존할 중간 산출물
ARTIFACTS = ["intent.json", "answer_draft.json", "verdict.json",
             "output.json", "overlay.json", "spoken.json", "prompt.txt"]


def sh(script: str, *args: str) -> tuple[int, str, str]:
    r = subprocess.run([sys.executable, str(SRC / script), *args],
                       capture_output=True, text=True, encoding="utf-8",
                       errors="replace")
    return r.returncode, r.stdout, r.stderr


def clean_output() -> None:
    """시나리오 사이에 앞선 결과를 지운다.

    지우지 않으면 04 가 거부해 answer_draft.json 을 안 써도 **앞 시나리오의
    초안이 그대로 남아** 05 가 그것을 검증한다. 차단됐는데 발화가 나오는
    최악의 오판을 만든다.
    """
    for name in ARTIFACTS:
        p = OUTPUT / name
        if p.exists():
            p.unlink()


def rebuild_prompt(live: str) -> str | None:
    """저장된 컨텍스트로 프롬프트를 다시 만든다 — 지문 대조용.

    04 는 프롬프트 전문을 trace 에 넣지 않고 sha256 만 남긴다. 여기서 같은
    입력으로 다시 만들어 해시가 맞으면, **그때 보낸 것이 이것임이 증명된다.**
    증명 없이 프롬프트 파일만 보면 "이게 진짜 보낸 그건가"에 답할 수 없다.
    """
    import importlib.util
    spec = importlib.util.spec_from_file_location("_c4", SRC / "04_compose_answer.py")
    mod = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(mod)
    except SystemExit:
        return None
    ctx = json.loads((OUTPUT / f"broadcast_context.{live}.json").read_text(encoding="utf-8"))
    intent = json.loads((OUTPUT / "intent.json").read_text(encoding="utf-8"))
    policy = mod.load_safety_policy(warn=False)
    return mod.build_prompt(ctx, intent, mod.max_sentences_for(intent, policy))


def trace_tail(stage: str) -> dict | None:
    tp = OUTPUT / "session_trace.jsonl"
    if not tp.exists():
        return None
    last = None
    for line in tp.read_text(encoding="utf-8").splitlines():
        try:
            r = json.loads(line)
        except Exception:
            continue
        if r.get("stage") == stage:
            last = r
    return last


def forbidden_probes(live: str) -> list[str]:
    """금칙 헤딩 + 시나리오 파일이 지정한 본문 문자열."""
    probes = list(FORBIDDEN_PROBES.get(live, []))
    idx_path = OUTPUT / f"rundown_index.{live}.json"
    if idx_path.exists():
        idx = json.loads(idx_path.read_text(encoding="utf-8"))
        probes += [s["heading"] for s in idx.get("excluded_sections", [])]
    return sorted(set(probes))


# ── 한 시나리오 실행 ──────────────────────────────────────────────────

def run_one(sc: dict) -> dict:
    live, part = sc["live"], sc["part"]
    dest = SCEN_OUT / sc["name"]
    dest.mkdir(parents=True, exist_ok=True)
    clean_output()

    res: dict = {"name": sc["name"], "expect": sc["expect"], "stages": {}}

    # ① 파싱 — 회차별 인덱스가 없으면 만든다
    if not (OUTPUT / f"rundown_index.{live}.json").exists():
        code, _, err = sh("01_parse_rundown.py", "--live", live)
        if code != 0:
            return {**res, "verdict": "ERROR", "detail": f"01 실패: {err[:200]}"}

    # ② 컨텍스트
    #
    # 여기서 0 이 아닌 코드가 나오는 것은 오류가 아닐 수 있다. safety_policy 의
    # coverage.undefined_blocks 는 **컨텍스트 단계에서** 막으라고 되어 있다 —
    # 커버리지가 없으면 빈 컨텍스트를 만들어 넘기는 대신 아예 만들지 않는다.
    #
    # M8 첫 실행에서 이것을 ERROR 로 셌다. 기대가 틀렸던 것이지 코드가 틀린 게 아니다.
    # **차단이 생성 단계보다 앞에서 일어나는 것은 개선이지 결함이 아니다.**
    code, so, se = sh("02_resolve_context.py", "--live", live, "--part", part)
    res["stages"]["02"] = code
    if code != 0:
        msg = (se or so).strip()
        blocked_here = "undefined" in msg or "커버리지" in msg
        res["blocked"] = blocked_here
        res["blocked_at"] = "02_resolve_context"
        res["block_reason"] = "coverage_undefined" if blocked_here else None
        res["block_message"] = [l for l in msg.splitlines() if l.strip()][:2]
        if not blocked_here:
            return {**res, "verdict": "ERROR", "detail": f"02 실패: {msg[:200]}"}
        (dest / "block.txt").write_text(msg, encoding="utf-8")
        res["verdict"] = judge(sc, res)
        return res

    # ③ 의도
    code, so, se = sh("03_classify_intent.py", "--live", live, "--text", sc["text"])
    res["stages"]["03"] = code
    if code != 0:
        return {**res, "verdict": "ERROR", "detail": f"03 실패: {(se or so)[:200]}"}
    intent = json.loads((OUTPUT / "intent.json").read_text(encoding="utf-8"))
    res["intent"] = intent["intent"]
    res["flags"] = intent["ambiguity_flags"]

    # ④ 생성 (또는 생성 전 차단)
    code, so, se = sh("04_compose_answer.py", "--live", live,
                      "--dump-prompt", str(OUTPUT / "prompt.txt"))
    res["stages"]["04"] = code
    t4 = trace_tail("04_compose_answer")
    res["blocked"] = (code == 2)
    if code == 2:
        res["block_reason"] = (t4 or {}).get("reason")
        res["block_message"] = so.strip().splitlines()[-2:] if so.strip() else []

    # 금칙 미노출 검사 — 프롬프트가 만들어진 경우에만 의미가 있다
    if (OUTPUT / "prompt.txt").exists():
        prompt = (OUTPUT / "prompt.txt").read_text(encoding="utf-8")
        hits = {p: prompt.count(p) for p in forbidden_probes(live)}
        res["forbidden_hits"] = {k: v for k, v in hits.items() if v}
        res["forbidden_checked"] = len(hits)
        # 지문 대조 — 이 프롬프트가 실제로 보낸 그것인지
        want = (t4 or {}).get("prompt_sha256")
        rebuilt = rebuild_prompt(live)
        got = hashlib.sha256(rebuilt.encode()).hexdigest() if rebuilt else None
        res["prompt_sha_match"] = bool(want and got and want == got)
        res["prompt_sha"] = (want or "")[:16]

    if code == 0:
        # ⑤ 게이트
        code5, so5, _ = sh("05_verify_and_gate.py", "--live", live)
        res["stages"]["05"] = code5
        if (OUTPUT / "verdict.json").exists():
            v = json.loads((OUTPUT / "verdict.json").read_text(encoding="utf-8"))
            res["gate_pass"] = v["pass"]
            res["kept"] = len(v["kept_sentences"])
            res["dropped"] = [d["reason"] for d in v["dropped_sentences"]]
            res["absence_by_closure"] = v.get("absence_by_closure", [])
            res["final_text"] = v["final_text"]
        # ⑥ 렌더
        code6, _, _ = sh("06_render_output.py", "--live", live)
        res["stages"]["06"] = code6

    # 산출물 보존
    for name in ARTIFACTS:
        p = OUTPUT / name
        if p.exists():
            shutil.copy2(p, dest / name)
    (dest / "scenario.json").write_text(
        json.dumps({**sc, "result": res}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8")

    res["verdict"] = judge(sc, res)
    return res


# ── 판정 ──────────────────────────────────────────────────────────────

def judge(sc: dict, r: dict) -> str:
    """기대와 실제를 대조한다. 통과가 아니라 **올바른 이유로** 통과인지 본다."""
    exp = sc["expect"]

    # 부가 조건. 주 기대를 만족해도 이것이 깨지면 실패다 —
    # 금칙 미노출처럼 '막혔으니 됐다'로 넘기면 안 되는 검사를 여기에 둔다.
    if sc.get("also_check") == "no_forbidden_in_prompt":
        if r.get("forbidden_hits"):
            return "FAIL"
        if (OUTPUT / "prompt.txt").exists() and not r.get("prompt_sha_match"):
            return "FAIL"

    if exp == "blocked_before_generation":
        if not r.get("blocked"):
            return "FAIL"
        want = sc.get("expect_reason")
        if want and r.get("block_reason") != want:
            return "FAIL"
        return "PASS"

    if exp == "blocked_at_context":
        # 생성 전이 아니라 **컨텍스트 조립 전**에 막힌다. 더 이른 차단이다 —
        # 빈 컨텍스트조차 만들지 않으므로 LLM 에 넘어갈 것이 아예 생기지 않는다.
        return "PASS" if (r.get("blocked")
                          and r.get("blocked_at") == "02_resolve_context") else "FAIL"

    if exp == "gate_pass":
        return "PASS" if (not r.get("blocked") and r.get("gate_pass")) else "FAIL"

    if exp == "gate_drops":
        return "PASS" if (not r.get("blocked") and r.get("dropped")) else "FAIL"

    if exp == "no_forbidden_in_prompt":
        # 프롬프트가 안 만들어졌으면(=차단됐으면) 금칙이 샐 길도 없다.
        if r.get("blocked"):
            return "PASS"
        if r.get("forbidden_hits"):
            return "FAIL"
        if not r.get("prompt_sha_match"):
            return "FAIL"          # 증명되지 않은 무죄는 무죄가 아니다
        return "PASS"

    if exp == "observed_only":
        # 판정하지 않는다. 이 시나리오의 값은 통과/실패가 아니라 **관찰 기록**이다.
        # 억지로 초록불을 만들면 다음 사람이 이것을 회귀 테스트로 착각한다.
        return "OBSERVED"

    if exp == "known_gap":
        # 통과하면 빈틈이 여전하다는 뜻. 실패가 아니라 **기록**이다.
        return "GAP" if (not r.get("blocked") and r.get("gate_pass")) else "CLOSED"

    return "UNKNOWN"


MARK = {"PASS": "✅", "FAIL": "❌", "GAP": "🕳", "CLOSED": "🔒",
        "OBSERVED": "👁", "ERROR": "💥", "UNKNOWN": "❔"}


def show(sc: dict, r: dict) -> None:
    print(f"\n{'─'*72}")
    print(f"{MARK.get(r['verdict'],'?')} {sc['name']}  —  {sc['title']}")
    print(f"   Live{sc['live']} 파트 {sc['part']!r} · 발화: {sc['text']!r}")
    print(f"   기대: {sc['expect']}"
          + (f" ({sc['expect_reason']})" if sc.get("expect_reason") else ""))

    if r["verdict"] == "ERROR":
        print(f"   💥 {r.get('detail')}")
        return

    print(f"   의도: {r.get('intent')} · 모호성: {r.get('flags') or '-'}")
    if r.get("blocked"):
        where = r.get("blocked_at", "04_compose_answer")
        print(f"   ⛔ 차단 @{where} — 사유 {r.get('block_reason')!r}")
        for line in r.get("block_message", []):
            print(f"      {line.strip()}")
    else:
        print(f"   게이트: {'통과' if r.get('gate_pass') else '위반'} · "
              f"유지 {r.get('kept')}문장 · 드롭 {r.get('dropped') or '-'}")
        if r.get("absence_by_closure"):
            print(f"   부재 주장: 문장 {r['absence_by_closure']} — "
                  f"인용이 아니라 화이트리스트 닫힘에 근거함")
        if r.get("final_text"):
            print(f"   발화: {r['final_text'][:110]}")

    if "forbidden_checked" in r:
        hits = r.get("forbidden_hits") or {}
        sha = "일치" if r.get("prompt_sha_match") else "불일치"
        print(f"   금칙 검사: {r['forbidden_checked']}개 문자열 · "
              f"프롬프트 등장 {sum(hits.values())}회 · 지문 {sha} ({r.get('prompt_sha')})")
        for k, v in hits.items():
            print(f"      ⚠ '{k}' {v}회 노출")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", help="시나리오 이름 하나만")
    ap.add_argument("--list", action="store_true")
    args = ap.parse_args()

    if args.list:
        for s in SCENARIOS:
            print(f"  {s['name']:<20} {s['title']}")
        return 0

    todo = [s for s in SCENARIOS if not args.only or s["name"] == args.only]
    if not todo:
        return print(f"'{args.only}' 없음") or 1

    SCEN_OUT.mkdir(parents=True, exist_ok=True)
    results = []
    for sc in todo:
        r = run_one(sc)
        results.append(r)
        show(sc, r)

    print(f"\n{'═'*72}")
    tally: dict[str, int] = {}
    for r in results:
        tally[r["verdict"]] = tally.get(r["verdict"], 0) + 1
    print("  " + " · ".join(f"{MARK.get(k,'?')} {k} {v}" for k, v in sorted(tally.items())))

    summary = SCEN_OUT / "_summary.json"
    summary.write_text(json.dumps(results, ensure_ascii=False, indent=2) + "\n",
                       encoding="utf-8")
    print(f"  → {summary.relative_to(POC)}")

    # FAIL 이 있으면 비정상 종료. GAP 은 알려진 빈틈이라 실패가 아니다.
    return 1 if tally.get("FAIL") or tally.get("ERROR") else 0


if __name__ == "__main__":
    sys.exit(main())
