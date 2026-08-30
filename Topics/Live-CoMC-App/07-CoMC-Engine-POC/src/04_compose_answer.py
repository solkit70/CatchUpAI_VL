#!/usr/bin/env python3
"""M7 ④ broadcast_context + intent → answer_draft.json.

M5 의 LLMProvider 어댑터를 그대로 쓴다. 새로 만들지 않는다 —
스키마 다운그레이드·재검증·재시도가 이미 거기 있고, 두 벌이 되면 반드시 어긋난다.

## 이 단계가 하지 않는 일

**프롬프트에 "말하지 마"라고 쓰지 않는다.** 금칙 섹션은 ① 단계에서 빠졌고
② 단계가 불변식으로 확인했다. LLM 이 볼 수 있는 것은 evidence_pool 뿐이므로
말하지 말라고 지시할 대상이 애초에 없다. 지시로 막는 방어는 지시를 어기면 뚫린다.

**생성을 막아야 할 때는 생성하지 않는다.** safety_policy 의 모호성 3규칙은
`block_generation: true` 다. 일단 만들어 놓고 뒤에서 거르는 것이 아니라,
만들기 전에 멈추고 진행자에게 되묻는다. 만들어 둔 답은 언젠가 새어 나간다.

## 프로바이더 설정은 레지스트리에서 읽는다

2026-08-23 실측으로 폴백 순서는 openai → gemini → claude, 기본 effort 는
openai=minimal / gemini=low 다. 코드에 박지 않는다 —
근거는 05-STT-LLM-Harness/guides/llm-latency-sweep.md.

실행:
    python 04_compose_answer.py --live 21
    python 04_compose_answer.py --live 21 --provider claude
    python 04_compose_answer.py --live 20 --intent-file ../output/intent.json

산출:
    output/answer_draft.json
"""
from __future__ import annotations

import argparse
import hashlib
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from common import (TOPIC, load_safety_policy, out, read_json, trace,  # noqa: E402
                    validate_or_die, write_json)

M5_EXAMPLES = TOPIC / "05-STT-LLM-Harness" / "examples"
LLM_RUNTIME = TOPIC / "05-STT-LLM-Harness" / "guides" / "llm_registry.runtime.json"

# 생성 자체를 막는 의도. 제어 명령은 답변을 만들 일이 없다.
CONTROL_INTENTS = {"advance_part", "stop", "repeat"}

SYSTEM = """너는 라이브 방송의 보조 진행자다.

절대 규칙:
- 아래 근거 목록에 있는 내용만 말한다. 근거에 없으면 추측하지 않는다.
- 모든 문장에 근거를 붙인다. claim_map 의 evidence_quote 는 근거 목록의 원문을 그대로 옮긴다.
- evidence_path 는 근거 목록에 있는 경로만 쓴다.
- 커버리지 화이트리스트 밖의 주제를 꺼내지 않는다.
- 방송 발화체로, 문장당 한 호흡에 읽을 수 있는 길이로 쓴다."""


def build_prompt(ctx: dict, intent: dict, max_sentences: int) -> str:
    ev = "\n".join(f"- path: {e['path']}\n  quote: {e['quote']}"
                   for e in ctx["evidence_pool"])
    cov = "\n".join(f"- {c}" for c in ctx["coverage_items"])
    ask = {"answer_question": "위 근거만 사용해 시청자 질문에 답하는 초안을 만들어라.",
           "summarize_part": "위 근거만 사용해 현재 파트를 요약하는 초안을 만들어라."}[
        intent["intent"]]
    return f"""[커버리지 화이트리스트 — 이 범위 밖은 말하지 않는다]
{cov}

[근거 목록]
{ev}

[커버리지 상태]
{ctx['coverage_state']}

[진행자/시청자 발화]
{intent['transcript']}

{ask} 문장은 최대 {max_sentences}개."""


def max_sentences_for(intent: dict, policy: dict) -> int:
    levels = policy["length_hardcut"]["levels"]
    return levels.get(intent["slots"].get("length_level", "default"), levels["default"])


def refuse(reason: str, detail: str, **fields) -> int:
    trace("04_compose_answer", ok=False, reason=reason, **fields)
    print(f"\n⛔ 생성하지 않습니다 — {detail}")
    print("   만들어 두고 뒤에서 거르는 것이 아니라, 만들기 전에 멈춘다.")
    return 2


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--live", required=True)
    ap.add_argument("--intent-file", help="기본값 output/intent.json")
    ap.add_argument("--provider", help="폴백 무시하고 지정 프로바이더만")
    ap.add_argument("--effort", choices=["minimal", "low", "medium", "high"],
                    help="레지스트리의 default_effort 를 덮어쓴다 (M8 effort 스윕용). "
                         "실전에서는 쓰지 않는다 — 근거는 llm-latency-sweep.md 다")
    ap.add_argument("--dump-prompt", help="LLM 에 보낸 프롬프트 전문을 이 경로에 저장 "
                                          "(M8 실습 2 — 금칙 섹션 미노출 증명)")
    args = ap.parse_args()

    ctx = read_json(out(f"broadcast_context.{args.live}.json"))
    intent = read_json(Path(args.intent_file) if args.intent_file else out("intent.json"))
    policy = load_safety_policy()

    # ── 생성 전 차단 ──────────────────────────────────────────────────
    if intent["intent"] == "out_of_scope":
        return refuse("out_of_scope",
                      intent["slots"].get("boundary_reason", "M2 App Boundary 제외 범위"),
                      rule=intent["slots"].get("boundary_rule"))
    if intent["intent"] == "unknown":
        return refuse("unknown_intent",
                      "의도를 분류하지 못했습니다. 진행자에게 되묻습니다 (HITL)")
    if intent["intent"] in CONTROL_INTENTS:
        return refuse("control_intent",
                      f"'{intent['intent']}' 는 제어 명령이라 답변 생성 대상이 아닙니다")
    if intent["ambiguity_flags"]:
        rules = {r["signal"].split("'")[1]: r for r in policy["ambiguity_rules"]}
        for f in intent["ambiguity_flags"]:
            r = rules.get(f)
            if r and r.get("block_generation"):
                return refuse("ambiguity", f"{f} — 되물을 말: \"{r['prompt']}\"",
                              flag=f, rule=r["id"])

    # ── 생성 ──────────────────────────────────────────────────────────
    sys.path.insert(0, str(M5_EXAMPLES))
    from llm_providers import SchemaViolation, build  # noqa: E402

    rt = read_json(LLM_RUNTIME)
    order = [args.provider] if args.provider else rt["fallback_order"]
    max_s = max_sentences_for(intent, policy)

    prompt = build_prompt(ctx, intent, max_s)

    # ── 프롬프트 지문 ─────────────────────────────────────────────────
    # 전문을 trace 에 매번 넣으면 파일이 불어나고 같은 내용을 두 벌 갖게 된다.
    # 대신 해시만 남긴다. build_prompt 는 (ctx, intent, max_s) 에 대해 결정적이므로
    # 나중에 저장된 컨텍스트로 다시 만들어 해시를 맞춰 보면
    # **그때 보낸 것이 이것임을 증명할 수 있다.**
    # 증명이 성립해야 "금칙 섹션이 프롬프트에 없었다"를 사후에 확인할 수 있다.
    fingerprint = hashlib.sha256(prompt.encode("utf-8")).hexdigest()
    if args.dump_prompt:
        dp = Path(args.dump_prompt)
        dp.parent.mkdir(parents=True, exist_ok=True)
        dp.write_text(prompt, encoding="utf-8")
        print(f"   프롬프트 전문 저장: {dp.name} (sha256 {fingerprint[:16]})")

    attempts: list[dict] = []

    for name in order:
        cfg = rt["providers"].get(name)
        if cfg is None:
            attempts.append({"provider": name, "error": "런타임 레지스트리에 없음"})
            continue
        eff = args.effort or cfg.get("default_effort")
        p = build(name, cfg["model"], cfg.get("cost_per_1k_tokens"), effort=eff)
        t0 = time.time()
        try:
            r = p.complete(SYSTEM, prompt, max_retries=1)
        except SchemaViolation as e:
            attempts.append({"provider": name, "error": "계약 위반", "detail": e.errors[:3],
                             "ms": round((time.time() - t0) * 1000)})
            print(f"  · {name}: 재검증 실패 → 다음 프로바이더로")
            continue
        except Exception as e:
            attempts.append({"provider": name, "error": f"{type(e).__name__}",
                             "detail": str(e)[:160],
                             "ms": round((time.time() - t0) * 1000)})
            print(f"  · {name}: {type(e).__name__} → 다음 프로바이더로")
            continue

        wall = round((time.time() - t0) * 1000)
        draft = r.draft
        validate_or_die("answer_draft", draft, "04_compose_answer")
        path = write_json(out("answer_draft.json"), draft)

        print(f"\n── {name} ({r.model}, effort={eff or '기본값'}) · {wall}ms · 시도 {r.attempts}회")
        print(f"   문장 {draft['length_sentences']}개 (상한 {max_s}) · "
              f"coverage={draft['coverage_state']}")
        for i, s in enumerate(draft["sentences"]):
            print(f"     [{i}] {s}")
        trace("04_compose_answer", ok=True, provider=name, model=r.model,
              prompt_sha256=fingerprint, prompt_chars=len(prompt),
              evidence_paths=sorted({e["path"] for e in ctx["evidence_pool"]}),
              effort=eff, latency_ms=wall, attempts=r.attempts,
              sentences=draft["length_sentences"], max_sentences=max_s,
              fallback_skipped=[a["provider"] for a in attempts], output=path.name)
        print(f"   → {path.name}")
        return 0

    trace("04_compose_answer", ok=False, reason="all_providers_failed", attempts=attempts)
    print("\n⛔ 모든 프로바이더 실패 → HITL 로 넘깁니다. 추측 발화는 하지 않습니다.",
          file=sys.stderr)
    for a in attempts:
        print(f"   - {a['provider']}: {a.get('error')} {a.get('detail','')}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
