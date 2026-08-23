#!/usr/bin/env python3
"""M7 실습 3 검증 — 5개 샘플 발화의 claim_map 이 원문과 일치하는가.

로드맵 검증 기준: "5개 샘플 발화에 대해 claim_map 의 evidence_quote 가 실제 원문과 일치"

발화는 M5 의 20문장 세트에서 가져온다. 새로 만들지 않는다 —
같은 문장으로 재야 M5·M7 결과를 이어 볼 수 있다.

## 무엇을 확인하는가

문장이 그럴듯한지가 아니라 **인용이 실재하는지**를 본다. LLM 은 근거를 지어낼 수 있고,
지어낸 근거는 문장으로는 완벽해 보인다. 그래서 ⑤ 게이트와 같은 방식으로
`evidence_pool` 안에서 문자열을 대조한다.

M2 App Boundary: *안전 검증 게이트 — 검증을 LLM 자기평가에 위임하는 것*은 금지다.
이 테스트도 같은 원칙을 따른다. LLM 에게 "네 근거 맞니?"라고 묻지 않는다.

실행: python tests/test_claim_evidence.py
      python tests/test_claim_evidence.py --live 21
"""
from __future__ import annotations

import argparse
import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
sys.path.insert(0, str(SRC))

from common import TOPIC, out, read_json  # noqa: E402

sys.path.insert(0, str(TOPIC / "05-STT-LLM-Harness" / "examples"))

# M5 20문장 중 답변 생성 대상(질문형)만 고른다.
# 제어 명령(멈춰/넘어가)은 answer_draft 를 만들지 않으므로 claim_map 검증 대상이 아니다.
SAMPLE_IDS = ["01", "03", "05", "08", "10"]


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--live", default="21")
    args = ap.parse_args()

    classify = load_module("classify", SRC / "03_classify_intent.py")
    compose = load_module("compose", SRC / "04_compose_answer.py")
    gate = load_module("gate", SRC / "05_verify_and_gate.py")

    from llm_providers import SchemaViolation, build   # noqa: E402
    from utterances import UTTERANCES                  # noqa: E402

    ctx = read_json(out(f"broadcast_context.{args.live}.json"))
    pool_quotes = [e["quote"] for e in ctx["evidence_pool"]]
    pool_paths = {e["path"] for e in ctx["evidence_pool"]}

    rt = read_json(TOPIC / "05-STT-LLM-Harness" / "guides" / "llm_registry.runtime.json")
    name = rt["fallback_order"][0]
    cfg = rt["providers"][name]
    p = build(name, cfg["model"], cfg.get("cost_per_1k_tokens"),
              effort=cfg.get("default_effort"))

    texts = {i: t for i, _, t in UTTERANCES}
    print(f"프로바이더 {name} · 근거 풀 {len(pool_quotes)}건 · 샘플 {len(SAMPLE_IDS)}개\n")

    fails, checked = [], 0
    for uid in SAMPLE_IDS:
        text = texts[uid]
        intent = classify.build_intent(text, ctx)
        if intent["intent"] != "answer_question" or intent["ambiguity_flags"]:
            print(f"  [{uid}] 건너뜀 — intent={intent['intent']} "
                  f"flags={intent['ambiguity_flags']}")
            continue

        prompt = compose.build_prompt(ctx, intent, 5)
        try:
            r = p.complete(compose.SYSTEM, prompt, max_retries=1)
        except SchemaViolation as e:
            fails.append(f"{uid}: 계약 위반 {e.errors[:1]}")
            print(f"  [{uid}] FAIL 계약 위반")
            continue
        except Exception as e:
            fails.append(f"{uid}: {type(e).__name__}")
            print(f"  [{uid}] FAIL {type(e).__name__}: {str(e)[:70]}")
            continue

        draft = r.draft
        checked += 1
        bad = []
        for c in draft["claim_map"]:
            if c["evidence_path"] not in pool_paths:
                bad.append(f"경로 위조 {c['evidence_path'][:40]!r}")
            elif not gate.quote_found(c["evidence_quote"], pool_quotes):
                bad.append(f"인용 미발견 {c['evidence_quote'][:36]!r}")

        covered = {c["sentence_idx"] for c in draft["claim_map"]}
        missing = [i for i in range(len(draft["sentences"])) if i not in covered]
        if missing:
            bad.append(f"근거 없는 문장 {missing}")

        status = "OK  " if not bad else "FAIL"
        print(f"  [{uid}] {status} 문장 {len(draft['sentences'])}개 · "
              f"claim {len(draft['claim_map'])}건 · {text[:34]}")
        for b in bad:
            print(f"        ✗ {b}")
            fails.append(f"{uid}: {b}")

    print()
    print(f"검증 {checked}건 · 위반 {len(fails)}건")
    if fails:
        print("실패:")
        for f in fails[:8]:
            print(f"  - {f}")
        return 1
    print("전부 통과 — 모든 evidence_quote 가 evidence_pool 안에 실재한다")
    return 0


if __name__ == "__main__":
    sys.exit(main())
