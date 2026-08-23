#!/usr/bin/env python3
"""M7 ⑤ answer_draft → verdict.json (안전 검증 게이트).

**이 단계가 문장을 떨어뜨리는 것이 정상 동작이다.** 통과율이 높다고 잘 도는 게 아니고,
낮다고 고장난 게 아니다. 근거 없는 문장을 잡아내는 것이 존재 이유다.

## 규칙 기반만 쓴다

M2 App Boundary 의 "절대 하지 말아야 할 일": *안전 검증 게이트 — 검증을 LLM
자기평가에 위임하는 것*. 그래서 여기엔 LLM 호출이 없다. 전부 문자열 대조다.
LLM 에게 "네 답이 근거 있니?"라고 묻는 것은 답을 만든 쪽에게 채점을 맡기는 것이다.

## 검사 순서

  1. claim.evidence_required — 모든 문장이 claim_map 에 있는가        → no_evidence
  2. claim.evidence_required — 인용이 evidence_pool 안에 실재하는가   → evidence_not_found
  3. coverage.whitelist_only — 화이트리스트 밖 주제인가              → coverage_violation
  4. length_hardcut          — 남은 문장이 상한을 넘는가             → length_hardcut

1~3 을 먼저 하고 길이 컷을 마지막에 한다. 순서를 바꾸면 **근거 없는 문장이 살아남고
근거 있는 문장이 잘리는** 일이 생긴다 — 길이 컷은 뒤에서부터 자르기 때문이다.

실행:
    python 05_verify_and_gate.py --live 21
    python 05_verify_and_gate.py --live 21 --tamper   # 근거를 위조해 게이트가 잡는지 확인

산출:
    output/verdict.json
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from common import (load_safety_policy, now_iso, out, read_json, trace,  # noqa: E402
                    validate_or_die, write_json)

# 대조에서 버릴 기능어. 남겨 두면 조사만으로 아무 문장이나 '관련 있음'이 된다.
STOP = {"그리고", "또한", "합니다", "입니다", "있습니다", "했습니다", "다룹니다",
        "위해", "관련", "이번", "오늘", "함께", "그것", "이것", "대해", "통해",
        "진행", "확인", "내용", "부분", "경우", "때문", "정도", "가지"}


def tokens(text: str) -> set[str]:
    return {t for t in re.findall(r"[0-9A-Za-z가-힣]{2,}", text) if t not in STOP}


def quote_found(quote: str, pool_quotes: list[str]) -> bool:
    """인용이 근거 풀 안에 실재하는가 — 부분 인용을 허용한다.

    LLM 은 근거를 그대로 옮기기도 하고 앞뒤를 잘라 오기도 한다. 양방향 포함을
    허용하되, 짧은 조각이 우연히 걸리지 않도록 최소 길이를 둔다.
    """
    q = (quote or "").strip()
    if len(q) < 4:
        return False
    return any(q in full or full in q for full in pool_quotes)


def verify(draft: dict, ctx: dict, policy: dict, ) -> dict:
    sentences = draft["sentences"]
    cmap = draft.get("claim_map", [])
    pool_paths = {e["path"] for e in ctx["evidence_pool"]}
    pool_quotes = [e["quote"] for e in ctx["evidence_pool"]]
    cov_tokens = tokens(" ".join(ctx["coverage_items"]))

    by_idx: dict[int, list[dict]] = {}
    for c in cmap:
        by_idx.setdefault(c.get("sentence_idx"), []).append(c)

    dropped: list[dict] = []
    violations: list[dict] = []
    kept: list[int] = []

    for i, sent in enumerate(sentences):
        claims = by_idx.get(i, [])

        # ① 근거가 붙어 있는가
        if not claims:
            dropped.append({"sentence_idx": i, "reason": "no_evidence"})
            violations.append({"rule_id": "claim.evidence_required",
                               "detail": f"문장 {i}: claim_map 항목 없음"})
            continue

        # ② 인용이 실재하는가 (경로 + 문자열 대조)
        bad = []
        for c in claims:
            if c.get("evidence_path") not in pool_paths:
                bad.append(f"경로 위조 {c.get('evidence_path')!r}")
            elif not quote_found(c.get("evidence_quote", ""), pool_quotes):
                bad.append(f"인용 미발견 {str(c.get('evidence_quote'))[:32]!r}")
        if bad:
            dropped.append({"sentence_idx": i, "reason": "evidence_not_found"})
            violations.append({"rule_id": "claim.evidence_required",
                               "detail": f"문장 {i}: " + " / ".join(bad[:2])})
            continue

        # ③ 화이트리스트 범위 안인가
        # 문장이 커버리지와도, 자기가 인용한 근거와도 겹치는 게 없으면 딴소리다.
        # ⚠️ 약한 검사다. 토큰이 겹친다고 같은 주제라는 보장은 없다 —
        #    본격적인 화이트리스트 검증은 M8 과제다.
        own_ev = tokens(" ".join(c.get("evidence_quote", "") for c in claims))
        if not (tokens(sent) & (cov_tokens | own_ev)):
            dropped.append({"sentence_idx": i, "reason": "coverage_violation"})
            violations.append({"rule_id": "coverage.whitelist_only",
                               "detail": f"문장 {i}: 화이트리스트·근거와 공통 어휘 없음"})
            continue

        kept.append(i)

    # ④ 길이 하드컷 — 반드시 마지막. 뒤에서부터 자른다.
    hard = policy["length_hardcut"]
    level = draft.get("_length_level") or "default"
    limit = hard["levels"].get(level, hard["levels"]["default"])
    if len(kept) > limit:
        for i in kept[limit:]:
            dropped.append({"sentence_idx": i, "reason": "length_hardcut"})
        violations.append({"rule_id": "length_hardcut",
                           "detail": f"{len(kept)}문장 → {limit}문장 (level={level})"})
        kept = kept[:limit]

    final_text = " ".join(sentences[i] for i in kept)
    return {
        "pass": not dropped,
        "final_text": final_text,
        "kept_sentences": kept,
        "dropped_sentences": sorted(dropped, key=lambda d: d["sentence_idx"]),
        "violations": violations,
        "length_after": len(kept),
        "verified_at": now_iso(),
    }


def tamper(draft: dict) -> dict:
    """근거를 위조해 게이트가 실제로 잡는지 확인한다.

    통과만 확인하는 검증은 검증이 아니다 — 게이트를 꺼도 같은 결과가 나온다.
    M4에서 에코 게이트를 off/on 으로 나눠 잰 것과 같은 이유다.
    """
    import copy
    d = copy.deepcopy(draft)
    if d["claim_map"]:
        d["claim_map"][0]["evidence_quote"] = "이 문장은 근거 풀에 존재하지 않는 위조 인용이다"
    if len(d["sentences"]) > 1 and len(d["claim_map"]) > 1:
        # 두 번째 문장의 근거를 통째로 제거 → no_evidence 유발
        idx = d["claim_map"][1]["sentence_idx"]
        d["claim_map"] = [c for c in d["claim_map"] if c["sentence_idx"] != idx]
    return d


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--live", required=True)
    ap.add_argument("--tamper", action="store_true", help="근거를 위조해 게이트 동작 확인")
    args = ap.parse_args()

    draft = read_json(out("answer_draft.json"))
    ctx = read_json(out(f"broadcast_context.{args.live}.json"))
    policy = load_safety_policy()

    # intent 의 길이 수준을 draft 에 실어 전달한다 (스키마 밖 필드라 검증 전에 뺀다)
    ipath = out("intent.json")
    if ipath.exists():
        draft["_length_level"] = read_json(ipath)["slots"].get("length_level", "default")

    if args.tamper:
        draft = tamper(draft)
        print("⚠ 위조 모드 — 근거를 조작한 초안으로 게이트를 시험합니다\n")

    v = verify(draft, ctx, policy)
    validate_or_die("verdict", v, "05_verify_and_gate")
    path = write_json(out("verdict.json"), v)

    n = len(draft["sentences"])
    print(f"── 검증 결과: {'통과' if v['pass'] else '위반 있음'} · "
          f"{len(v['kept_sentences'])}/{n} 문장 유지")
    for i, s in enumerate(draft["sentences"]):
        d = next((x for x in v["dropped_sentences"] if x["sentence_idx"] == i), None)
        mark = f"✗ {d['reason']}" if d else "✓"
        print(f"   [{i}] {mark:<22} {s[:52]}")
    for vi in v["violations"]:
        print(f"   ⚠ {vi['rule_id']}: {vi.get('detail','')}")

    print(f"\n   최종 발화: {v['final_text'][:96] or '(없음 — 발화하지 않는다)'}")
    trace("05_verify_and_gate", ok=True, passed=v["pass"], tamper=args.tamper,
          kept=len(v["kept_sentences"]), dropped=len(v["dropped_sentences"]),
          reasons=[d["reason"] for d in v["dropped_sentences"]], output=path.name)
    print(f"   → {path.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
