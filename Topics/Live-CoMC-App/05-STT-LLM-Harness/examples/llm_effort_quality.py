#!/usr/bin/env python3
"""M5 이월 과제 보조 — effort 를 낮췄을 때 답변 품질이 유지되는지 눈으로 본다.

llm_latency_sweep.py 는 "계약을 지켰는가"만 판정한다. 스키마가 맞고 근거 인용이
근거 목록 안에 있으면 통과다. 그런데 그것은 **형식**의 판정이고, 낮은 effort 의
진짜 위험은 형식이 아니라 내용이다 — 짧아지고, 근거를 하나만 쓰고, 질문의 일부만
답하는 식으로 나빠질 수 있다. 그건 스키마가 절대 잡지 못한다.

그래서 같은 입력에 대한 실제 발화문을 effort 별로 나란히 찍는다.
숫자로 결론 내리기 전에 문장을 읽기 위한 스크립트다.

실행:
    python llm_effort_quality.py --provider openai --levels minimal,low
    python llm_effort_quality.py --provider gemini --levels low
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from llm_compare import EVIDENCE, SYSTEM, USER, evidence_ok  # noqa: E402
from llm_providers import SchemaViolation, build  # noqa: E402

RUNTIME = HERE.parent / "guides" / "llm_registry.runtime.json"


def show(name, cfg, effort):
    label = effort or "(기본값)"
    p = build(name, cfg["model"], cfg.get("cost_per_1k_tokens"), effort=effort)
    try:
        r = p.complete(SYSTEM, USER, max_retries=0)
    except SchemaViolation as e:
        print(f"\n── {name} / {label} ── 계약 위반")
        for m in e.errors[:4]:
            print(f"     ⚠ {m}")
        return
    except Exception as e:
        print(f"\n── {name} / {label} ── 호출 실패: {type(e).__name__}: {e}")
        return

    ok, problems = evidence_ok(r.draft)
    u = r.usage
    print(f"\n── {name} / {label} ──")
    print(f"   출력 {u.get('output_tokens')}tok · 추론 {u.get('reasoning_tokens')} · "
          f"근거대조 {'통과' if ok else '실패'} · 문장 {r.draft['length_sentences']}개")
    for i, s in enumerate(r.draft["sentences"]):
        print(f"   [{i}] {s}")
    # 근거를 몇 개나 실제로 쓰는지 — 낮은 effort 에서 먼저 나빠지는 지점이다
    used = {c.get("evidence_path", "") + "|" + (c.get("evidence_quote") or "")[:30]
            for c in r.draft.get("claim_map", [])}
    print(f"   서로 다른 근거 {len(used)}개 / 제공된 근거 {len(EVIDENCE)}개")
    for prob in problems:
        print(f"   ⚠ {prob}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--provider", required=True)
    ap.add_argument("--levels", default="", help="쉼표 구분. 항상 기본값도 함께 찍는다")
    args = ap.parse_args()

    rt = json.loads(RUNTIME.read_text(encoding="utf-8"))
    cfg = rt["providers"][args.provider]

    print(f"질문: 오늘 3번 파트에서 뭘 다루나요?  (근거 {len(EVIDENCE)}건 제공)")
    show(args.provider, cfg, None)
    for lv in [x for x in args.levels.split(",") if x]:
        show(args.provider, cfg, lv)
    return 0


if __name__ == "__main__":
    sys.exit(main())
