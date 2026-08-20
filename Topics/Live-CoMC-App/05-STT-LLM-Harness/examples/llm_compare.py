#!/usr/bin/env python3
"""M5 실습 3 — 3사 어댑터 비교 + 재시도·폴백 검증.

같은 프롬프트와 같은 계약을 3사에 보내고, 돌아온 결과가 모두 동일한 내부 스키마
(answer_draft.schema.json)로 수렴하는지 확인한다. M3 설계의 실물 검증이다.

실행:
    python llm_compare.py                 # 3사 비교
    python llm_compare.py --provider claude
    python llm_compare.py --fallback-demo # 앞 프로바이더를 강제 실패시켜 폴백 확인

산출:
    probe_log.jsonl 에 llm_compare / llm_fallback 이벤트 누적
"""
from __future__ import annotations

import argparse
import json
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

from llm_providers import SchemaViolation, build  # noqa: E402

RUNTIME = HERE.parent / "guides" / "llm_registry.runtime.json"
PROBE_LOG = HERE / "probe_log.jsonl"

# ── 테스트 입력 ────────────────────────────────────────────────────────
# 실제 방송 상황을 축소한 것. evidence_pool 밖의 내용을 말하면 ⑦ 게이트가 잘라야 하므로,
# 여기서는 "근거 안에서만 답하기"가 지켜지는지도 함께 본다.
EVIDENCE = [
    {"path": "AI/Roundup/2026-08-17 - Live24 Rundown.md#part3",
     "quote": "3번 파트는 FDE 영상 제작 과정을 다룬다. 한국어 28분 1초, 영어 27분 11초 두 편을 공개했다."},
    {"path": "AI/Roundup/2026-08-17 - Live24 Rundown.md#part3",
     "quote": "조사 문서는 42개이며 GitHub에 전부 공개돼 있다."},
]

SYSTEM = """너는 라이브 방송의 보조 진행자다.

절대 규칙:
- 아래 근거 목록에 있는 내용만 말한다. 근거에 없으면 추측하지 않는다.
- 모든 문장에 근거를 붙인다. claim_map 의 evidence_quote 는 근거 목록의 원문을 그대로 옮긴다.
- evidence_path 는 근거 목록에 있는 경로만 쓴다.
- 방송 발화체로, 문장당 한 호흡에 읽을 수 있는 길이로 쓴다."""

USER = """[근거 목록]
""" + "\n".join(f"- path: {e['path']}\n  quote: {e['quote']}" for e in EVIDENCE) + """

[커버리지 상태]
defined

[시청자 질문]
오늘 3번 파트에서 뭘 다루나요?

위 근거만 사용해 2~3문장으로 답하는 초안을 만들어라."""


def log(event: dict):
    event["ts"] = datetime.now(timezone.utc).isoformat()
    with PROBE_LOG.open("a", encoding="utf-8") as f:
        f.write(json.dumps(event, ensure_ascii=False) + "\n")


def load_runtime():
    if not RUNTIME.exists():
        sys.exit("llm_registry.runtime.json 이 없습니다. 먼저 python llm_probe.py 를 실행하세요.")
    return json.loads(RUNTIME.read_text(encoding="utf-8"))


def evidence_ok(draft: dict) -> tuple[bool, list[str]]:
    """claim_map 의 근거가 evidence_pool 안에 실제로 있는지 문자열 대조한다.

    ⑦ 안전 검증 게이트가 할 일의 축소판이다. 스키마는 '문자열이 있다'까지만 보장하고
    '그 문자열이 진짜 근거다'는 보장하지 않는다.
    """
    paths = {e["path"] for e in EVIDENCE}
    quotes = [e["quote"] for e in EVIDENCE]
    problems = []
    for c in draft.get("claim_map", []):
        if c.get("evidence_path") not in paths:
            problems.append(f"경로 위조: {c.get('evidence_path')!r}")
        q = (c.get("evidence_quote") or "").strip()
        if not any(q and (q in full or full in q) for full in quotes):
            problems.append(f"인용 불일치: {q[:40]!r}")
    return (not problems), problems


def run_one(name, cfg, verbose=True):
    p = build(name, cfg["model"], cfg.get("cost_per_1k_tokens"))
    t0 = time.time()
    r = p.complete(SYSTEM, USER, max_retries=1)
    wall = round((time.time() - t0) * 1000)
    ok, problems = evidence_ok(r.draft)
    if verbose:
        cost = f"${r.est_cost_usd}" if r.est_cost_usd is not None else "단가 미확인"
        print(f"\n── {name} ({r.model}) ──")
        print(f"   지연 {wall}ms · 시도 {r.attempts}회 · "
              f"토큰 in {r.usage.get('input_tokens')} / out {r.usage.get('output_tokens')} · {cost}")
        print(f"   문장 {r.draft['length_sentences']}개 · coverage={r.draft['coverage_state']} · "
              f"근거대조 {'통과' if ok else '실패'}")
        for i, s in enumerate(r.draft["sentences"]):
            print(f"     [{i}] {s}")
        for prob in problems:
            print(f"     ⚠ {prob}")
    return r, ok, problems, wall


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--provider")
    ap.add_argument("--fallback-demo", action="store_true",
                    help="첫 프로바이더를 강제 실패시켜 다음으로 넘어가는지 확인")
    args = ap.parse_args()

    rt = load_runtime()
    order = rt["fallback_order"]
    providers = rt["providers"]

    if args.fallback_demo:
        return fallback_demo(order, providers)

    targets = [args.provider] if args.provider else order
    rows = []
    for name in targets:
        if name not in providers:
            print(f"  ! {name} 은 런타임 레지스트리에 없습니다 (프리플라이트에서 제외됨)")
            continue
        try:
            r, ok, problems, wall = run_one(name, providers[name])
            rows.append({"provider": name, "model": r.model, "ok": True,
                         "schema_valid": True, "evidence_ok": ok,
                         "attempts": r.attempts, "latency_ms": wall,
                         "sentences": r.draft["length_sentences"],
                         "usage": r.usage, "est_cost_usd": r.est_cost_usd,
                         "problems": problems})
        except SchemaViolation as e:
            print(f"\n── {name} ── 재검증 실패 (재시도 후에도)")
            for msg in e.errors[:5]:
                print(f"     ⚠ {msg}")
            rows.append({"provider": name, "ok": False, "schema_valid": False,
                         "errors": e.errors[:5]})
        except Exception as e:
            print(f"\n── {name} ── 호출 실패: {type(e).__name__}: {e}")
            rows.append({"provider": name, "ok": False, "error": f"{type(e).__name__}: {e}"[:300]})

    # ── 요약 ──────────────────────────────────────────────────────────
    print()
    print(f"{'프로바이더':<10} {'스키마':<7} {'근거':<6} {'시도':>4} {'지연':>8} {'문장':>4}")
    print("-" * 52)
    for r in rows:
        if r.get("ok"):
            print(f"{r['provider']:<10} {'통과':<7} {'통과' if r['evidence_ok'] else '실패':<6} "
                  f"{r['attempts']:>4} {r['latency_ms']:>6}ms {r['sentences']:>4}")
        else:
            print(f"{r['provider']:<10} {'실패':<7} {'-':<6} {'-':>4} {'-':>8} {'-':>4}")

    good = [r for r in rows if r.get("ok")]
    print()
    print(f"동일 내부 스키마로 수렴: {len(good)}/{len(rows)}개 프로바이더")
    if len(good) == len(rows) and rows:
        print("→ 실습 3 검증 기준 충족: 동일 입력에 3사 모두 같은 내부 스키마의 JSON 반환")

    log({"event": "llm_compare", "results": rows})
    return 0 if good else 1


def fallback_demo(order, providers):
    """첫 프로바이더를 강제로 실패시키고 다음으로 넘어가는지 확인한다.

    실제 폴백 트리거는 ① 호출 실패 ② 재검증 실패 두 가지다. 여기서는 ②를
    '존재하지 않는 모델' 로 만들어 ①을 유발해 흐름만 확인한다.
    """
    print("폴백 데모 — 첫 프로바이더를 강제 실패시킨다\n")
    chain = list(order)
    for i, name in enumerate(chain):
        cfg = dict(providers[name])
        forced = (i == 0)
        if forced:
            cfg["model"] = "definitely-not-a-real-model-000"
        print(f"[{i+1}/{len(chain)}] {name} 시도" + ("  (강제 실패용 모델)" if forced else ""))
        try:
            r, ok, problems, wall = run_one(name, cfg, verbose=not forced)
            print(f"\n→ {name} 성공. active_provider = {name}")
            log({"event": "llm_fallback", "chain": chain, "succeeded_at": name,
                 "skipped": chain[:i]})
            return 0
        except Exception as e:
            print(f"    실패: {type(e).__name__}: {str(e)[:120]}")
            print(f"    → 다음 프로바이더로 폴백\n")
    print("모든 프로바이더 실패 → HITL 로 넘긴다 (추측 발화 금지)")
    log({"event": "llm_fallback", "chain": chain, "succeeded_at": None})
    return 1


if __name__ == "__main__":
    sys.exit(main())
