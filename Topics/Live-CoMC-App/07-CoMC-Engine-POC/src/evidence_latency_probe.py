#!/usr/bin/env python3
"""M7 실습 6 보조 — 근거 풀 크기가 ④ 지연에 영향을 주는가.

파이프라인 실측에서 ④ 단계 LLM 호출이 5.7~7.7초로 나왔다. 그런데 M5 마이크로벤치마크
(근거 2건, 2~3문장)에서는 같은 프로바이더·같은 effort 로 2.6초였다.
어디서 차이가 나는지 후보는 둘이다 — **입력(근거 풀) 크기**와 **출력(문장 수)**.

한 조건에 한 번씩 재면 LLM 편차에 묻힌다. 조건당 여러 번 재고 중앙값으로 본다.
프로세스 기동 비용을 빼기 위해 **한 프로세스 안에서** 반복한다 —
subprocess 로 재면 2.4초의 import 비용이 매번 섞인다.

실행:
    python evidence_latency_probe.py --repeats 3
"""
from __future__ import annotations

import argparse
import copy
import statistics
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from common import TOPIC, out, read_json, trace, write_json  # noqa: E402

sys.path.insert(0, str(TOPIC / "05-STT-LLM-Harness" / "examples"))

LLM_RUNTIME = TOPIC / "05-STT-LLM-Harness" / "guides" / "llm_registry.runtime.json"

CONDITIONS = [
    ("근거 2건 / 3문장", 2, 3),      # M5 마이크로벤치마크 조건
    ("근거 2건 / 5문장", 2, 5),
    ("근거 15건 / 3문장", 15, 3),
    ("근거 15건 / 5문장", 15, 5),    # 파이프라인 실제 조건
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--live", default="21")
    ap.add_argument("--repeats", type=int, default=3)
    args = ap.parse_args()

    import importlib.util
    spec = importlib.util.spec_from_file_location("compose", HERE / "04_compose_answer.py")
    compose = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(compose)

    from llm_providers import SchemaViolation, build     # noqa: E402

    ctx0 = read_json(out(f"broadcast_context.{args.live}.json"))
    intent = read_json(out("intent.json"))
    rt = read_json(LLM_RUNTIME)
    name = rt["fallback_order"][0]
    cfg = rt["providers"][name]

    # 프로바이더는 한 번만 만든다 — 클라이언트 생성 비용(약 2.1초)을 측정에서 뺀다.
    p = build(name, cfg["model"], cfg.get("cost_per_1k_tokens"),
              effort=cfg.get("default_effort"))
    print(f"프로바이더 {name} ({cfg['model']}, effort={cfg.get('default_effort')}) · "
          f"조건당 {args.repeats}회 · 프로세스 기동 비용 제외\n")

    rows = []
    for label, n_ev, n_sent in CONDITIONS:
        ctx = copy.deepcopy(ctx0)
        ctx["evidence_pool"] = ctx0["evidence_pool"][:n_ev]
        prompt = compose.build_prompt(ctx, intent, n_sent)
        lat, toks = [], []
        for i in range(args.repeats):
            t0 = time.time()
            try:
                r = p.complete(compose.SYSTEM, prompt, max_retries=0)
            except (SchemaViolation, Exception) as e:      # noqa: B014
                print(f"  {label:<18} #{i+1} 실패 {type(e).__name__}")
                continue
            lat.append(round((time.time() - t0) * 1000))
            toks.append((r.usage.get("input_tokens"), r.usage.get("output_tokens")))
        if not lat:
            continue
        med = round(statistics.median(lat))
        rows.append({"condition": label, "evidence": n_ev, "max_sentences": n_sent,
                     "latency_med_ms": med, "latency_min_ms": min(lat),
                     "latency_max_ms": max(lat), "usage": toks})
        print(f"  {label:<18} 중앙 {med:>6}ms   범위 {min(lat)}~{max(lat)}ms   "
              f"토큰 in{toks[0][0]}/out{toks[0][1]}")

    print(f"\n{'조건':<20} {'중앙':>9} {'최악':>9}")
    print("-" * 42)
    for r in rows:
        print(f"{r['condition']:<20} {r['latency_med_ms']:>7}ms {r['latency_max_ms']:>7}ms")

    if len(rows) == 4:
        ev_effect = rows[3]["latency_med_ms"] - rows[1]["latency_med_ms"]
        sent_effect = rows[1]["latency_med_ms"] - rows[0]["latency_med_ms"]
        print(f"\n근거 2건→15건 효과 (문장 5 고정): {ev_effect:+,}ms")
        print(f"문장 3개→5개 효과 (근거 2 고정): {sent_effect:+,}ms")

    path = write_json(out("evidence_latency.json"), {"provider": name, "rows": rows})
    trace("evidence_latency_probe", ok=True, repeats=args.repeats, rows=rows)
    print(f"\n원자료: {path.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
