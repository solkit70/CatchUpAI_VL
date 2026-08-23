#!/usr/bin/env python3
"""M5 이월 과제 — LLM 지연 원인 분석 (effort 스윕).

M5에서 3사 지연이 10.8~21.6초로 나왔다. STT는 1.2초였으니 병목은 전적으로 ⑥ 단계다.
M7(파일 기반 6단계 POC)의 목표 지연이 여기에 달려 있어서, "왜 느린가"와
"낮추면 얼마나 줄고 무엇을 잃는가"를 먼저 재야 한다.

가설: 3사 모두 추론(thinking/reasoning)이 기본 ON 상태로 호출되고 있다.
  - Claude Opus 5 는 thinking 이 기본 adaptive (파라미터를 생략해도 켜진다)
  - OpenAI 는 reasoning_effort 기본값
  - Gemini 는 thinking_level 기본값

측정 항목은 셋이다.
  ① 총 지연        — 이 파이프라인에서 유일하게 의미 있는 지연 지표
  ② 추론 토큰 비중 — 지연의 원인을 직접 설명하는 숫자
  ③ 계약 준수      — effort 를 낮췄을 때 스키마·근거 검증이 깨지는지

TTFT(첫 토큰 지연)는 재지 않는다. ⑦ 안전 검증 게이트가 JSON 전체를 받아
검증한 뒤에야 발화가 가능하므로, 첫 토큰이 빨라도 말할 수 없다.
스트리밍으로 TTFT 를 줄여봐야 이 파이프라인에서는 아무것도 앞당기지 못한다.

실행:
    python llm_latency_sweep.py                      # 3사 × 지원 effort × 2회
    python llm_latency_sweep.py --repeats 3
    python llm_latency_sweep.py --provider openai    # 한 곳만
    python llm_latency_sweep.py --levels low,high    # 수준 좁히기

산출:
    latency_sweep.json        — 원자료
    probe_log.jsonl           — llm_latency_sweep 이벤트
"""
from __future__ import annotations

import argparse
import json
import statistics
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from llm_compare import SYSTEM, USER, evidence_ok  # noqa: E402  동일 입력을 재사용한다
from llm_providers import EFFORT_LEVELS, SchemaViolation, build, native_effort  # noqa: E402

RUNTIME = HERE.parent / "guides" / "llm_registry.runtime.json"
PROBE_LOG = HERE / "probe_log.jsonl"
RESULT = HERE / "latency_sweep.json"

# baseline = effort 를 보내지 않은 상태. M5 측정이 이 조건이었으므로 비교 기준이 된다.
BASELINE = "(기본값)"


def log(event: dict):
    event["ts"] = datetime.now(timezone.utc).isoformat()
    with PROBE_LOG.open("a", encoding="utf-8") as f:
        f.write(json.dumps(event, ensure_ascii=False) + "\n")


def load_runtime():
    if not RUNTIME.exists():
        sys.exit("llm_registry.runtime.json 이 없습니다. 먼저 python llm_probe.py 를 실행하세요.")
    return json.loads(RUNTIME.read_text(encoding="utf-8"))


def one_call(name: str, cfg: dict, effort: str | None) -> dict:
    """한 번 호출하고 지연·토큰·계약 준수를 기록한다.

    재시도는 끄고(max_retries=0) 잰다. 재시도가 섞이면 '한 번 호출의 지연'이
    아니라 '재시도 포함 지연'이 되어 effort 비교가 흐려진다.
    스키마 위반은 실패가 아니라 **측정 대상**이다 — 낮은 effort 의 대가가 그것이다.
    """
    p = build(name, cfg["model"], cfg.get("cost_per_1k_tokens"), effort=effort)
    t0 = time.time()
    try:
        r = p.complete(SYSTEM, USER, max_retries=0)
    except SchemaViolation as e:
        return {"ok": False, "reason": "schema", "latency_ms": round((time.time() - t0) * 1000),
                "errors": e.errors[:3]}
    except Exception as e:
        return {"ok": False, "reason": "call", "latency_ms": round((time.time() - t0) * 1000),
                "errors": [f"{type(e).__name__}: {e}"[:200]]}

    wall = round((time.time() - t0) * 1000)
    ok, problems = evidence_ok(r.draft)
    u = r.usage
    return {
        "ok": True,
        "latency_ms": wall,
        "input_tokens": u.get("input_tokens"),
        "output_tokens": u.get("output_tokens"),
        "reasoning_tokens": u.get("reasoning_tokens"),
        "effort_sent": u.get("effort_sent"),
        "est_cost_usd": r.est_cost_usd,
        "sentences": r.draft.get("length_sentences"),
        "evidence_ok": ok,
        "problems": problems,
    }


def summarize(runs: list[dict]) -> dict:
    good = [r for r in runs if r.get("ok")]
    lat = [r["latency_ms"] for r in good]
    out = [r["output_tokens"] or 0 for r in good]
    rsn = [r["reasoning_tokens"] for r in good if r.get("reasoning_tokens") is not None]
    return {
        "n": len(runs),
        "n_ok": len(good),
        "latency_med_ms": round(statistics.median(lat)) if lat else None,
        "latency_min_ms": min(lat) if lat else None,
        "latency_max_ms": max(lat) if lat else None,
        "output_tokens_med": round(statistics.median(out)) if out else None,
        "reasoning_tokens_med": round(statistics.median(rsn)) if rsn else None,
        "evidence_ok_all": all(r["evidence_ok"] for r in good) if good else None,
        "schema_fail": sum(1 for r in runs if r.get("reason") == "schema"),
        "call_fail": sum(1 for r in runs if r.get("reason") == "call"),
    }


def fmt_ms(v):
    return f"{v/1000:.1f}s" if v is not None else "—"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--provider", help="한 프로바이더만")
    ap.add_argument("--repeats", type=int, default=2, help="수준당 반복 횟수 (기본 2)")
    ap.add_argument("--levels", help="쉼표 구분. 기본은 지원되는 전 수준")
    ap.add_argument("--no-baseline", action="store_true", help="기본값 조건을 건너뛴다")
    args = ap.parse_args()

    rt = load_runtime()
    providers = rt["providers"]
    targets = [args.provider] if args.provider else rt["fallback_order"]
    levels = args.levels.split(",") if args.levels else list(EFFORT_LEVELS)

    results = {}
    for name in targets:
        if name not in providers:
            print(f"  ! {name} 은 런타임 레지스트리에 없습니다 (프리플라이트에서 제외됨)")
            continue
        cfg = providers[name]
        results[name] = {"model": cfg["model"], "levels": {}}

        plan = ([] if args.no_baseline else [(BASELINE, None)])
        for lv in levels:
            nat = native_effort(name, lv)
            if nat is None:
                continue                      # 이 프로바이더에 없는 수준은 건너뛴다
            plan.append((lv, lv))

        print(f"\n═══ {name} ({cfg['model']}) ═══")
        for label, effort in plan:
            runs = []
            for i in range(args.repeats):
                r = one_call(name, cfg, effort)
                runs.append(r)
                mark = "✓" if r.get("ok") else "✗"
                extra = ""
                if r.get("ok"):
                    rt_ = r.get("reasoning_tokens")
                    extra = f"out {r['output_tokens']}tok"
                    if rt_ is not None:
                        extra += f" (추론 {rt_})"
                else:
                    extra = r["reason"] + ": " + (r["errors"][0][:70] if r.get("errors") else "")
                print(f"  {label:<10} #{i+1} {mark} {fmt_ms(r['latency_ms']):>7}  {extra}")
            results[name]["levels"][label] = {"runs": runs, "summary": summarize(runs)}

    # ── 요약표 ────────────────────────────────────────────────────────
    print()
    print(f"{'프로바이더':<9} {'effort':<10} {'지연(중앙)':>10} {'범위':>15} "
          f"{'출력tok':>8} {'추론tok':>8} {'계약':>6}")
    print("-" * 76)
    for name, r in results.items():
        base_med = (r["levels"].get(BASELINE, {}).get("summary", {}) or {}).get("latency_med_ms")
        for label, d in r["levels"].items():
            s = d["summary"]
            if s["n_ok"] == 0:
                print(f"{name:<9} {label:<10} {'전부 실패':>10} "
                      f"{'(' + str(s['schema_fail']) + '건 스키마/' + str(s['call_fail']) + '건 호출)':>15}")
                continue
            delta = ""
            if base_med and label != BASELINE and s["latency_med_ms"]:
                pct = (s["latency_med_ms"] - base_med) / base_med * 100
                delta = f" {pct:+.0f}%"
            contract = "통과" if s["evidence_ok_all"] and s["schema_fail"] == 0 else "위반"
            print(f"{name:<9} {label:<10} {fmt_ms(s['latency_med_ms']):>10}"
                  f"{delta:<6} {fmt_ms(s['latency_min_ms']) + '~' + fmt_ms(s['latency_max_ms']):>9} "
                  f"{str(s['output_tokens_med'] or '—'):>8} "
                  f"{str(s['reasoning_tokens_med'] if s['reasoning_tokens_med'] is not None else '—'):>8} "
                  f"{contract:>6}")

    RESULT.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    log({"event": "llm_latency_sweep", "repeats": args.repeats,
         "summary": {n: {lv: d["summary"] for lv, d in r["levels"].items()}
                     for n, r in results.items()}})
    print(f"\n원자료: {RESULT.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
