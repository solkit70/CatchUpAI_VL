#!/usr/bin/env python3
"""M6 실습 4 — 비용 서킷 브레이커.

방송 중 비용 폭주를 막는다. 상한을 넘으면 무료 프로바이더(edge-tts)로 자동 강등한다.

## 왜 문자 수와 호출 수를 함께 세는가

원래 요구는 "누적 비용이 상한을 넘으면 강등"이다. 그런데 이번 측정에서 비용을
정확히 셀 수 없는 프로바이더가 나왔다.

  · qwen       — 공식 단가 미확인. 3자 출처가 $0.013~$0.028/1k자로 엇갈린다
  · openai     — gpt-4o-mini-tts 는 텍스트 $0.60/1M자 + **오디오 출력 $12/1M 토큰** 이중 요금이고,
                 음성 엔드포인트는 오디오 토큰 수를 돌려주지 않는다

즉 **비용만으로 만든 차단기는 조용히 과소 추정한다.** 단가를 모르는 프로바이더는
비용이 0으로 잡혀 영원히 걸리지 않고, openai 는 실제의 일부만 센다.
방송 중 폭주를 막는 장치가 "폭주해도 안 걸리는" 상태로 존재하는 셈이다.

그래서 상한을 셋으로 둔다. 어느 하나라도 넘으면 강등한다.

  max_calls   호출 수   — 단가와 무관하게 항상 셀 수 있다
  max_chars   문자 수   — 모든 프로바이더 공통. 비용의 대리 지표로 가장 신뢰할 만하다
  max_cost    비용($)   — 단가가 확인된 프로바이더에만 의미가 있다

M5에서 배운 것과 같은 형태의 함정이다. "확인했다는 착각을 주는 검증이 가장 위험하다" —
비용만 보는 차단기가 정확히 그것이다.

## 강등은 되돌리지 않는다

한 번 무료로 내려가면 세션이 끝날 때까지 유지한다. 자동 복귀를 넣으면
상한 근처에서 오르내리며 비용이 계속 새고, 방송 중에 목소리가 왔다 갔다 한다.
시청자에게는 그게 더 이상하게 들린다.

실행:
    python circuit_breaker.py --demo             # 정상 → 상한 초과 → 강등
    python circuit_breaker.py --demo --by chars
    python circuit_breaker.py --demo --dry-run   # 실제 합성 없이 로직만
"""
from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from tts_providers import TTSUnavailable, build  # noqa: E402

RUNTIME = HERE / "voice_registry.runtime.json"
TTS_LOG = HERE / "tts_log.jsonl"


def log(event: dict):
    event["ts"] = datetime.now(timezone.utc).isoformat()
    with TTS_LOG.open("a", encoding="utf-8") as f:
        f.write(json.dumps(event, ensure_ascii=False) + "\n")


@dataclass
class Budget:
    """한 방송 세션의 상한. 셋 중 하나라도 넘으면 강등한다."""
    max_calls: int = 200
    max_chars: int = 40_000
    max_cost_usd: float = 2.0

    def breach(self, calls: int, chars: int, cost: float) -> str | None:
        if calls >= self.max_calls:
            return f"호출 수 {calls}/{self.max_calls}"
        if chars >= self.max_chars:
            return f"문자 수 {chars:,}/{self.max_chars:,}"
        if cost >= self.max_cost_usd:
            # 상한이 아주 작을 수 있으므로 유효숫자를 살려 찍는다.
            # .3f 로 굳히면 $0.000/$0.00 처럼 아무 정보도 없는 문장이 된다.
            return f"비용 ${cost:.6g}/${self.max_cost_usd:.6g}"
        return None


@dataclass
class SessionMeter:
    """세션 누적 사용량. 프로바이더별로도 나눠 본다(사후 분석용)."""
    calls: int = 0
    chars: int = 0
    cost_usd: float = 0.0
    cost_is_lower_bound: bool = False
    by_provider: dict = field(default_factory=dict)

    def add(self, provider: str, chars: int, cost: float | None, incomplete: bool):
        self.calls += 1
        self.chars += chars
        if cost is not None:
            self.cost_usd += cost
        if cost is None or incomplete:
            # 단가를 모르거나 요금 구조가 불완전하면 누적 비용은 하한일 뿐이다.
            # 이 표시를 지우면 "비용을 안다"는 착각이 남는다.
            self.cost_is_lower_bound = True
        p = self.by_provider.setdefault(provider, {"calls": 0, "chars": 0, "cost": 0.0})
        p["calls"] += 1
        p["chars"] += chars
        p["cost"] += cost or 0.0


class TTSCircuitBreaker:
    """예산을 넘으면 무료 프로바이더로 강등하는 라우터."""

    def __init__(self, runtime: dict, budget: Budget, dry_run: bool = False):
        self.rt = runtime
        self.budget = budget
        self.dry_run = dry_run
        self.meter = SessionMeter()
        self.primary = runtime["default_provider"]
        self.degrade_to = runtime["degrade_to"]
        self.active = self.primary
        self.degraded_at: dict | None = None
        self._cache: dict = {}

        if self.degrade_to is None:
            raise RuntimeError(
                "강등 목적지(무료 프로바이더)가 없습니다. 서킷 브레이커가 성립하지 않습니다 — "
                "상한을 넘어도 내려갈 곳이 없으면 차단기가 아니라 경고등일 뿐입니다.")

    def _provider(self, name: str):
        if name not in self._cache:
            cfg = dict(self.rt["providers"][name])
            cfg["replacements"] = {**self.rt["shared_replacements"],
                                   **(cfg.get("replacements") or {})}
            self._cache[name] = build(name, cfg)
        return self._cache[name]

    def _check(self):
        """상한 확인 후 필요하면 강등한다. 강등은 되돌리지 않는다."""
        if self.active == self.degrade_to:
            return
        why = self.budget.breach(self.meter.calls, self.meter.chars, self.meter.cost_usd)
        if why:
            self.degraded_at = {
                "reason": why, "from": self.active, "to": self.degrade_to,
                "at_call": self.meter.calls, "at_chars": self.meter.chars,
                "at_cost_usd": round(self.meter.cost_usd, 6),
                "cost_is_lower_bound": self.meter.cost_is_lower_bound,
            }
            print(f"\n  ⚡ 상한 초과 ({why}) → {self.active} 에서 {self.degrade_to} 로 강등")
            if self.meter.cost_is_lower_bound:
                print("     ※ 누적 비용은 하한값이다 (단가 미확인 또는 이중 요금 프로바이더 포함)")
            self.active = self.degrade_to
            log({"event": "tts_circuit_break", **self.degraded_at})

    def speak(self, text: str, out_path: Path):
        """한 발화를 합성한다. 합성 전에 상한을 확인한다."""
        self._check()
        name = self.active
        cfg = self.rt["providers"][name]

        if self.dry_run:
            chars = len(text)
            unit = cfg.get("cost_per_1k_chars")
            cost = None if unit is None else chars / 1000 * unit
            self.meter.add(name, chars, cost, cfg.get("cost_incomplete", False))
            return {"provider": name, "chars": chars, "est_cost_usd": cost, "dry": True}

        r = self._provider(name).synth(text, out_path)
        self.meter.add(name, r.chars, r.est_cost_usd, cfg.get("cost_incomplete", False))
        return {"provider": name, "chars": r.chars, "latency_ms": r.latency_ms,
                "first_chunk_ms": r.first_chunk_ms, "est_cost_usd": r.est_cost_usd,
                "path": str(r.path.name)}

    def report(self) -> dict:
        return {
            "primary": self.primary, "active": self.active,
            "degraded": self.degraded_at is not None, "degraded_at": self.degraded_at,
            "calls": self.meter.calls, "chars": self.meter.chars,
            "cost_usd": round(self.meter.cost_usd, 6),
            "cost_is_lower_bound": self.meter.cost_is_lower_bound,
            "by_provider": self.meter.by_provider,
            "budget": vars(self.budget),
        }


# ── 데모 ──────────────────────────────────────────────────────────────

DEMO_LINES = [
    "오늘 3번 파트는 FDE 영상 제작 과정을 다룹니다.",
    "한국어 28분 1초, 영어 27분 11초 두 편을 공개했습니다.",
    "조사 문서 42개가 GitHub에 전부 공개돼 있습니다.",
    "네, 확인해 볼게요.",
    "그건 근거를 못 찾았습니다.",
    "관련 링크는 방송 후에 정리해서 올리겠습니다.",
]


def demo(by: str, dry_run: bool, repeats: int):
    rt = json.loads(RUNTIME.read_text(encoding="utf-8"))

    # 상한을 일부러 낮춰 강등이 실제로 일어나는지 본다.
    # 검증 기준이 "강등이 발생하는가"이므로, 발생하지 않는 상한으로는 아무것도 검증하지 못한다.
    budget = Budget(max_calls=10**9, max_chars=10**9, max_cost_usd=10.0**9)
    if by == "calls":
        budget.max_calls = 4
    elif by == "chars":
        budget.max_chars = 120
    else:
        budget.max_cost_usd = 0.00005     # openai 단가 기준으로 몇 번 만에 걸리는 값

    # 1순위가 이미 강등 목적지(무료)면 강등할 곳이 없어 차단기가 동작하지 않는다.
    # 이건 데모의 한계가 아니라 **설계상의 사실**이다 —
    # 기본 프로바이더를 무료로 두면 서킷 브레이커는 존재하되 아무 일도 하지 않는 장치가 된다.
    # 기본값 선택(실습 2)과 비용 차단(실습 4)은 따로 정할 수 없는 한 쌍이다.
    if rt["default_provider"] == rt["degrade_to"]:
        paid = [c for c in rt["providers"]
                if c != rt["degrade_to"]
                and (rt["providers"][c].get("cost_per_1k_chars") or 0) > 0]
        print(f"  ⓘ 1순위({rt['default_provider']})가 강등 목적지와 같다 — 이 상태로는 강등이 성립하지 않는다.")
        if not paid:
            print("    유료 프로바이더가 없어 데모를 진행할 수 없다.")
            return 1
        print(f"    데모를 위해 1순위를 {paid[0]} 로 바꾼다 (실운영 기본값은 실습 2 결과로 정한다).")
        rt = {**rt, "default_provider": paid[0]}

    br = TTSCircuitBreaker(rt, budget, dry_run=dry_run)
    out_dir = HERE / "audio" / "breaker"
    print(f"1순위: {br.primary} · 강등 목적지: {br.degrade_to} · 기준: {by}"
          + ("  (dry-run)" if dry_run else ""))
    print(f"상한: 호출 {budget.max_calls if budget.max_calls < 10**8 else '—'} · "
          f"문자 {budget.max_chars if budget.max_chars < 10**8 else '—'} · "
          f"비용 ${budget.max_cost_usd if budget.max_cost_usd < 10**8 else '—'}")
    print()

    n = 0
    for _ in range(repeats):
        for line in DEMO_LINES:
            n += 1
            r = br.speak(line, out_dir / f"line_{n:02d}")
            cost = f"${r['est_cost_usd']:.6f}" if r.get("est_cost_usd") is not None else "단가미확인"
            print(f"  {n:2d}. [{r['provider']:<6}] {r['chars']:>3}자 · {cost}  {line[:24]}")

    rep = br.report()
    print()
    print(f"총 {rep['calls']}회 · {rep['chars']:,}자 · ${rep['cost_usd']:.6f}"
          + ("  (하한값)" if rep["cost_is_lower_bound"] else ""))
    for p, v in rep["by_provider"].items():
        print(f"    {p:<8} {v['calls']:>3}회 {v['chars']:>5}자 ${v['cost']:.6f}")

    if rep["degraded"]:
        d = rep["degraded_at"]
        print(f"\n✅ 강등 확인: {d['from']} → {d['to']} ({d['reason']}, {d['at_call']}번째 발화)")
    else:
        print("\n❌ 강등이 일어나지 않았다 — 상한이 너무 높거나 로직이 동작하지 않는다")

    log({"event": "tts_circuit_demo", "by": by, "dry_run": dry_run, "report": rep})
    return 0 if rep["degraded"] else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--demo", action="store_true")
    ap.add_argument("--by", choices=["cost", "calls", "chars"], default="cost")
    ap.add_argument("--dry-run", action="store_true", help="실제 합성 없이 계수만")
    ap.add_argument("--repeats", type=int, default=2)
    args = ap.parse_args()

    if not RUNTIME.exists():
        sys.exit("voice_registry.runtime.json 이 없습니다. 먼저 python tts_probe.py 를 실행하세요.")
    if args.demo:
        return demo(args.by, args.dry_run, args.repeats)
    ap.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
