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


# ── 부재 주장 (M8) ────────────────────────────────────────────────────
#
# "X 는 오늘 다루지 않습니다" 같은 문장에는 그것을 지지하는 인용이 **존재할 수 없다.**
# 근거 풀은 문서에 있는 것의 모음이고, 없다는 사실은 거기 적혀 있지 않다.
# 그런데 모델은 아무 인용이나 붙이고, 인용이 실재하므로 게이트는 통과시킨다.
#
# M8 실측 (2026-08-30, absence-claim 시나리오):
#   문장  "따라서 데이터센터 인력 프로그램은 오늘 실험 항목에 포함되어 있지 않습니다."
#   근거  "★ 실험 1 — AI로 라이브 방송 보조 MC 앱 만들기"
#   결과  통과. 인용은 실재하지만 그 인용은 데이터센터에 대해 아무 말도 하지 않는다.
#
# 이때 결론이 우연히 참이었다는 점이 더 위험하다 — 같은 메커니즘이 거짓을 만들 때도
# 똑같은 확신으로 통과한다.
RE_ABSENCE = re.compile(
    r"(?:포함되어\s*있지\s*않|들어\s*있지\s*않|명시되어\s*있지\s*않|"
    r"언급되어\s*있지\s*않|다루지\s*않|하지\s*않습니다|없습니다|없어요|"
    r"아닙니다|해당(?:하지|되지)\s*않)")

# 숫자 환각 검사 대상 — 아라비아 숫자만 본다.
# 한글 수사('두 가지')는 근거를 **세어서** 나오는 값이라 인용에 없는 것이 정상이다.
# 그것까지 잡으면 정상 문장을 떨어뜨린다 — 말해도 되는 것을 못 말하게 하는 실패다.
RE_DIGITS = re.compile(r"\d[\d,.:/-]*")

# 고유명사 후보 — 라틴 문자 3자 이상. 한글 고유명사는 일반 명사와 형태로 구분되지 않아
# 규칙으로 가려낼 수 없다. 잡히는 것만 확실히 잡는다.
RE_LATIN = re.compile(r"[A-Za-z][A-Za-z0-9_.\-]{2,}")

# 도메인 일반어. 근거에 없어도 환각이 아니다.
LATIN_OK = {"api", "app", "json", "url", "ai", "the", "and", "for"}


def normalize(text: str) -> str:
    """대조 전 표기 흔들림을 흡수한다 — 하이픈·공백·대소문자."""
    return re.sub(r"[\s\-_]", "", text).lower()


def check_facts(sent: str, own_quotes: list[str],
                trusted_extra: list[str] | None = None) -> list[str]:
    """문장의 숫자·고유명사가 신뢰 가능한 출처 안에 실재하는가.

    ## 대조 대상은 근거 인용만이 아니다

    처음에는 자기 근거 인용하고만 대조했다. 그랬더니 정상 문장이 떨어졌다 —

        문장  "오늘 3번 파트는 'AI로 라이브 방송 보조 MC 앱 만들기'를 다룹니다."
        드롭  숫자 '3' 이 근거에 없음

    맞는 말이다. 그런데 그 3은 환각이 아니라 **current_part_id** 다.
    M7 실습 5에서 권위값으로 확정한 세션 상태이고, 근거 풀보다 더 믿을 수 있다.

    **근거 풀은 신뢰 출처의 전부가 아니라 하나다.** 좁게 잡으면 말해도 되는 것을
    말하지 못하게 되고, 그것도 방송 사고다 (M7 인사이트).

    신뢰 출처:
      · 그 문장이 인용한 근거      — 문서에 적힌 것
      · 커버리지 화이트리스트       — 발화 허용 목록. 정의상 말해도 되는 것
      · current_part_id            — M7 권위값
      · 항목·근거 개수             — 세어서 나오는 값

    ## 왜 근거 풀 '전체'와는 대조하지 않는가

    다른 문장의 근거에서 숫자를 빌려 올 수 있게 된다.
    '어느 근거에든 5가 있으니 5를 말해도 된다'가 되면 검사가 무의미하다.
    """
    trusted = " ".join(own_quotes) + " " + " ".join(trusted_extra or [])
    hay = normalize(trusted)
    # 근거 안의 라틴 문자 조각들. 약칭 표기를 흡수하는 데 쓴다.
    hay_frags = [f.lower() for f in RE_LATIN.findall(trusted) if len(f) >= 4]

    bad: list[str] = []
    for tok in RE_DIGITS.findall(sent):
        t = tok.rstrip(".,:/-")
        if t and normalize(t) not in hay:
            bad.append(f"숫자 {t!r}")

    for tok in RE_LATIN.findall(sent):
        if tok.lower() in LATIN_OK:
            continue
        nt = normalize(tok)
        if nt in hay:
            continue
        # ⚠️ 약칭 ↔ 전개형을 같은 것으로 본다 (M8 어려운 질문 스윕에서 오탐).
        #
        #   근거   "5개 스킬(video-add-chapters/cleaning/full-process/subtitles, …)"
        #   문장   "video-subtitles 포함해 업데이트가 완료됐습니다"
        #
        # Rundown 은 목록을 압축해 쓴다. 모델이 'subtitles' 를 정식 이름
        # 'video-subtitles' 로 **복원한 것이 오히려 드롭 사유가 됐다.**
        # 정확하게 말한 쪽을 벌하는 검사는 잘못된 검사다.
        #
        # 4자 이상 조각만 본다. 짧은 조각을 허용하면 아무 이름이나 통과한다.
        if any(normalize(f) in nt for f in hay_frags):
            continue
        bad.append(f"고유명사 {tok!r}")
    return bad


def quote_found(quote: str, pool_quotes: list[str]) -> bool:
    """인용이 근거 풀 안에 실재하는가 — 부분 인용을 허용한다.

    LLM 은 근거를 그대로 옮기기도 하고 앞뒤를 잘라 오기도 한다. 양방향 포함을
    허용하되, 짧은 조각이 우연히 걸리지 않도록 최소 길이를 둔다.
    """
    q = (quote or "").strip()
    if len(q) < 4:
        return False
    return any(q in full or full in q for full in pool_quotes)


def verify(draft: dict, ctx: dict, policy: dict) -> dict:
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
    absence_basis: list[int] = []   # 인용이 아니라 화이트리스트 닫힘에 근거한 문장

    # 근거 인용 밖의 신뢰 출처. 여기 있는 값은 환각이 아니다.
    trusted_extra = [
        *ctx["coverage_items"],
        str(ctx.get("current_part_id") or ""),
        str(len(ctx["coverage_items"])),
        str(len(ctx["evidence_pool"])),
    ]

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

        # ④ 부재 주장 — 근거로 지지될 수 없는 종류의 문장 (M8)
        #
        # 앱이 "그건 오늘 안 다룹니다"라고 말하는 것 자체는 옳고 유용하다.
        # 다만 그 근거는 **인용이 아니라 화이트리스트가 닫힌 집합이라는 사실**이다.
        # 커버리지에 없다는 것은 커버리지 목록을 다 보면 확정할 수 있다.
        #
        #   주제가 화이트리스트 밖  →  화이트리스트 닫힘으로 참. 근거 표기만 바로잡는다
        #   주제가 화이트리스트 안  →  화이트리스트와 모순. 드롭한다
        if RE_ABSENCE.search(sent):
            # 부재 주장의 **주어**가 화이트리스트 항목인지를 본다.
            #
            # 처음에는 '문장에 커버리지 어휘가 겹치고 남는 토큰이 없으면 모순'으로
            # 판정했다. 틀렸다 — 부재 문장에는 '다루지', '않습니다' 같은 토큰이
            # 항상 남으므로 모순이 한 번도 잡히지 않았다.
            #
            # 겹침의 유무가 아니라 **한 항목이 얼마나 통째로 들어왔는가**를 본다.
            # 커버리지 항목의 어휘 대부분이 문장에 있으면 그 항목을 지목한 것이다.
            sent_toks = tokens(sent)
            contradicts = False
            for item in ctx["coverage_items"]:
                it = tokens(item)
                if it and len(it & sent_toks) / len(it) >= 0.6:
                    contradicts = True
                    break
            if contradicts:
                dropped.append({"sentence_idx": i, "reason": "absence_contradicts_coverage"})
                violations.append({"rule_id": "claim.absence_needs_closure",
                                   "detail": f"문장 {i}: 화이트리스트에 있는 항목을 없다고 말함"})
                continue
            absence_basis.append(i)

        # ⑤ 숫자·고유명사가 자기 근거 안에 실재하는가 (M8)
        own_quotes = [c.get("evidence_quote", "") for c in claims]
        bad_facts = check_facts(sent, own_quotes, trusted_extra)
        if bad_facts:
            dropped.append({"sentence_idx": i, "reason": "fact_not_in_evidence"})
            violations.append({"rule_id": "claim.facts_must_be_quoted",
                               "detail": f"문장 {i}: " + " / ".join(bad_facts[:3])})
            continue

        kept.append(i)

    # ⑥ 길이 하드컷 — 반드시 마지막. 뒤에서부터 자른다.
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
    absence_kept = [i for i in absence_basis if i in kept]
    return {
        "pass": not dropped,
        # 어느 문장이 인용이 아니라 화이트리스트 닫힘에 기대고 있는지 남긴다.
        # 남기지 않으면 사후 분석에서 "이 문장은 무엇으로 뒷받침됐나"에 답할 수 없다.
        "absence_by_closure": absence_kept,
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


def tamper_facts(draft: dict) -> dict:
    """숫자·고유명사를 인위적으로 틀리게 만들어 사실 검사가 잡는지 확인한다 (M8 실습 3).

    근거를 위조하는 `--tamper` 와는 다른 종류의 공격이다. 여기서는 **근거를 그대로 두고
    문장만 틀리게** 만든다. 인용은 실재하고 경로도 맞으므로 M7 게이트는 전부 통과시킨다 —
    그것이 이 검사를 만든 이유다.

    3종:
      (1) 숫자       존재하지 않는 수치
      (2) 사람 이름   근거에 없는 인명
      (3) Topic 이름  근거에 없는 제품·프로젝트 이름
    """
    import copy
    d = copy.deepcopy(draft)
    inject = [" 총 47건이 처리되었습니다.",
              " 이 작업은 Minsoo Son 님이 맡았습니다.",
              " DatacenterWorkforce 프로젝트와 함께 진행합니다."]
    for i, frag in enumerate(inject):
        if i < len(d["sentences"]):
            d["sentences"][i] = d["sentences"][i].rstrip() + frag
    return d


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--live", required=True)
    ap.add_argument("--tamper", action="store_true", help="근거를 위조해 게이트 동작 확인")
    ap.add_argument("--tamper-facts", action="store_true",
                    help="근거는 그대로 두고 숫자·고유명사만 틀리게 만든다 (M8 실습 3)")
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

    if args.tamper_facts:
        draft = tamper_facts(draft)
        print("⚠ 사실 위조 모드 — 근거는 그대로, 숫자·고유명사만 틀리게 넣습니다")
        print("   인용은 실재하므로 M7 게이트만으로는 전부 통과한다\n")

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
          tamper_facts=args.tamper_facts,
          absence_by_closure=v.get("absence_by_closure", []),
          kept=len(v["kept_sentences"]), dropped=len(v["dropped_sentences"]),
          reasons=[d["reason"] for d in v["dropped_sentences"]], output=path.name)
    print(f"   → {path.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
