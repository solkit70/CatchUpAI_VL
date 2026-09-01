#!/usr/bin/env python3
"""M9 실습 1 — 단일 장기 실행 프로세스.

## 왜 만드는가

M7 지연 리포트의 결론이 하나였다.

    발화당 6.7초 중  프로세스 기동 3.7초 + 연결 설정 3.0초 + LLM 2.1~3.5초

LLM 자체보다 **껍데기가 두 배**를 먹는다. 6단계를 매번 `subprocess` 로 띄우기
때문이다. 파이썬이 여섯 번 뜨고, `openai` SDK 를 여섯 번 import 하고, TLS
핸드셰이크를 매번 새로 한다.

## 무엇을 바꾸는가 — 프로세스 경계만

**파일 계약은 그대로 둔다.** 각 단계가 JSON 을 읽고 쓰는 구조는 사고 추적에
필수적이라 손대지 않는다. 바꾸는 것은 *프로세스 경계*이지 *파일 경계*가 아니다.

    이전  [py] ① → [py] ② → [py] ③ → [py] ④ → [py] ⑤ → [py] ⑥     프로세스 6개
    이후  [py ─── ① → ② → ③ → ④ → ⑤ → ⑥ ─── 계속 살아 있음]      프로세스 1개

## 어떻게 아끼는가

세 군데다.

1. **파이썬 기동** — 데몬 시작 시 한 번. 발화당 0
2. **모듈 import** — 6개 스테이지 + `openai` SDK 를 시작 시 한 번
3. **LLM 클라이언트 재사용** — `llm_providers.build` 를 메모이즈한다.
   `OpenAI()` 객체가 살아 있으면 httpx 커넥션 풀이 유지돼 **TLS 핸드셰이크를
   건너뛴다.** 3.0초의 실체가 대부분 여기다

## 왜 main() 을 그대로 부르는가

각 스테이지를 함수로 쪼개 다시 쓰는 방법도 있다. 그러나 그건 **6개 파일을
전부 개편**하는 일이고, M7·M8 에서 검증한 동작이 바뀔 위험이 있다.

여기서는 `sys.argv` 를 갈아끼우고 `main()` 을 부른다. 지저분하지만
**검증된 코드 경로를 한 줄도 건드리지 않는다.** M9 의 목적은 지연 절감이지
리팩터링이 아니다.

실행:
    python engine_daemon.py --live 21 --repeats 5          # 벤치 모드
    python engine_daemon.py --live 21 --serve              # stdin 대기 모드

산출:
    ../../output/daemon_latency.json
"""
from __future__ import annotations

import argparse
import importlib.util
import io
import json
import statistics
import sys
import time
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path

HERE = Path(__file__).resolve().parent
M7_SRC = HERE.parents[2] / "07-CoMC-Engine-POC" / "src"
M5_EXAMPLES = HERE.parents[2] / "05-STT-LLM-Harness" / "examples"

if str(M7_SRC) not in sys.path:
    sys.path.insert(0, str(M7_SRC))
if str(M5_EXAMPLES) not in sys.path:
    sys.path.insert(0, str(M5_EXAMPLES))

# 파일명이 숫자로 시작해 일반 import 가 안 된다. importlib 로 직접 로드한다.
STAGES = {
    "①": "01_parse_rundown.py",
    "②": "02_resolve_context.py",
    "③": "03_classify_intent.py",
    "④": "04_compose_answer.py",
    "⑤": "05_verify_and_gate.py",
    "⑥": "06_render_output.py",
}


def load_stage(filename: str):
    """스테이지 스크립트를 모듈로 올린다. 한 번만 부른다."""
    name = "stage_" + filename.replace(".py", "").replace("-", "_")
    spec = importlib.util.spec_from_file_location(name, M7_SRC / filename)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def install_provider_cache() -> dict:
    """`llm_providers.build` 를 메모이즈해 LLM 클라이언트를 재사용한다.

    ⚠️ 이것이 이 파일에서 가장 중요한 세 줄이다.
       `OpenAIProvider.__init__` 이 매번 `OpenAI()` 를 새로 만들면 커넥션 풀도
       매번 새로 생기고, 첫 요청마다 TLS 핸드셰이크를 다시 한다.
       같은 객체를 돌려주면 풀이 살아 있어 그 비용이 사라진다.

    반환값은 통계 dict 로, 캐시가 실제로 먹히는지 확인하는 용도다.
    """
    import llm_providers

    stats = {"calls": 0, "misses": 0}
    cache: dict[tuple, object] = {}
    original = llm_providers.build

    def cached_build(name, model, cost_per_1k_tokens=None, effort=None, **kw):
        stats["calls"] += 1
        key = (name, model, effort, json.dumps(kw, sort_keys=True, default=str))
        if key not in cache:
            stats["misses"] += 1
            cache[key] = original(name, model, cost_per_1k_tokens, effort, **kw)
        return cache[key]

    llm_providers.build = cached_build
    # 04 는 main() 안에서 `from llm_providers import build` 를 하므로,
    # 모듈 속성을 갈아두면 그 시점에 캐시판을 가져간다.
    return stats


class Engine:
    """상주 엔진. 시작 시 한 번 데우고, 그 뒤로는 발화만 처리한다."""

    def __init__(self, quiet: bool = True):
        self.quiet = quiet
        t0 = time.time()
        self.mods = {k: load_stage(v) for k, v in STAGES.items()}
        self.provider_stats = install_provider_cache()
        # openai SDK 를 미리 import 해 둔다 — 첫 발화가 이 비용을 물지 않도록
        try:
            import openai  # noqa: F401
        except Exception:
            pass
        self.warmup_ms = round((time.time() - t0) * 1000)

    def call(self, label: str, argv: list[str]) -> tuple[bool, int]:
        """스테이지 하나를 인프로세스로 실행. (성공여부, 소요 ms)"""
        mod = self.mods[label]
        saved = sys.argv
        sys.argv = [STAGES[label], *argv]
        buf_o, buf_e = io.StringIO(), io.StringIO()
        t0 = time.time()
        ok = True
        try:
            if self.quiet:
                with redirect_stdout(buf_o), redirect_stderr(buf_e):
                    mod.main()
            else:
                mod.main()
        except SystemExit as e:               # main() 이 sys.exit 를 부를 수 있다
            ok = (e.code in (0, None))
        except Exception as e:
            ok = False
            self.last_error = f"{type(e).__name__}: {e}"
        finally:
            sys.argv = saved
        return ok, round((time.time() - t0) * 1000)

    def prewarm(self, live: str, part: str = "3", max_evidence: int | None = None) -> dict:
        """①② 는 방송 전에 끝내 둔다 (M7 warm 조건과 동일).

        max_evidence 를 주면 근거 풀을 좁힌다 — M7 리포트의 2번 대책 실측용.
        """
        ev = ["--max-evidence", str(max_evidence)] if max_evidence else []
        per = {}
        for label, argv in (("①", ["--live", live]),
                            ("②", ["--live", live, "--part", part, *ev])):
            ok, ms = self.call(label, argv)
            per[label] = ms
            if not ok:
                return {"ok": False, "failed_at": label, "per_stage": per}
        return {"ok": True, "per_stage": per}

    def utter(self, live: str, text: str) -> dict:
        """발화 하나를 처리한다 — ③④⑤⑥."""
        per, total = {}, 0
        for label, argv in (("③", ["--live", live, "--text", text]),
                            ("④", ["--live", live]),
                            ("⑤", ["--live", live]),
                            ("⑥", ["--live", live])):
            ok, ms = self.call(label, argv)
            per[label] = ms
            total += ms
            if not ok:
                return {"ok": False, "failed_at": label, "per_stage": per,
                        "total_ms": total, "error": getattr(self, "last_error", None)}
        return {"ok": True, "per_stage": per, "total_ms": total}


def bench(live: str, text: str, repeats: int, max_evidence: int | None = None) -> dict:
    eng = Engine()
    print(f"  데몬 기동(모듈·SDK import)  {eng.warmup_ms}ms  ← 한 번만 낸다\n")

    pre = eng.prewarm(live, max_evidence=max_evidence)
    if not pre["ok"]:
        print(f"  ⛔ 사전 캐시 실패: {pre['failed_at']}")
        return {"ok": False, "stage": "prewarm", "detail": pre}
    print(f"  사전 캐시 ①② {sum(pre['per_stage'].values())}ms  (방송 전에 끝내는 구간)\n")

    runs = []
    for i in range(repeats):
        r = eng.utter(live, text)
        runs.append(r)
        mark = "✅" if r["ok"] else "❌"
        stage_s = " ".join(f"{k}{v}" for k, v in r["per_stage"].items())
        print(f"  {mark} {i+1}회  {r['total_ms']:>5}ms   {stage_s}"
              + ("" if r["ok"] else f"   ← {r.get('failed_at')} {r.get('error','')}"))

    good = [r for r in runs if r["ok"]]
    if not good:
        return {"ok": False, "stage": "utter", "runs": runs}
    tot = [r["total_ms"] for r in good]
    stages = sorted({k for r in good for k in r["per_stage"]})
    return {
        "ok": True,
        "max_evidence": max_evidence,
        "warmup_ms": eng.warmup_ms,
        "prewarm_ms": sum(pre["per_stage"].values()),
        "n": repeats, "n_ok": len(good),
        "total_med_ms": round(statistics.median(tot)),
        "total_max_ms": max(tot),
        "total_min_ms": min(tot),
        "stage_med_ms": {s: round(statistics.median(
            [r["per_stage"][s] for r in good if s in r["per_stage"]])) for s in stages},
        "provider_build": dict(eng.provider_stats),
        "runs": runs,
    }


def serve(live: str):
    """stdin 한 줄 = 발화 하나. M9 실습 2(핫키)·Electron 셸이 붙을 자리."""
    eng = Engine()
    pre = eng.prewarm(live)
    print(json.dumps({"event": "ready", "warmup_ms": eng.warmup_ms,
                      "prewarm": pre}, ensure_ascii=False), flush=True)
    for line in sys.stdin:
        text = line.strip()
        if not text:
            continue
        if text in ("__quit__", "__exit__"):
            break
        r = eng.utter(live, text)
        print(json.dumps({"event": "utterance", "text": text, **r},
                         ensure_ascii=False), flush=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--live", default="21")
    ap.add_argument("--text", default="오늘 3번 파트에서 뭘 다루나요?")
    ap.add_argument("--repeats", type=int, default=5)
    ap.add_argument("--max-evidence", type=int,
                    help="근거 풀 상한 — M7 리포트 2번 대책(근거 축소) 실측용")
    ap.add_argument("--serve", action="store_true", help="stdin 대기 모드")
    args = ap.parse_args()

    if args.serve:
        serve(args.live)
        return

    print(f"\n=== M9 상주 엔진 벤치 — Live{args.live} · {args.repeats}회 ===\n")
    res = bench(args.live, args.text, args.repeats, args.max_evidence)
    if res.get("ok"):
        print(f"\n  중앙값 {res['total_med_ms']}ms · 최악 {res['total_max_ms']}ms "
              f"· 최선 {res['total_min_ms']}ms")
        pb = res["provider_build"]
        print(f"  프로바이더 build 호출 {pb['calls']}회 중 실제 생성 {pb['misses']}회"
              f"  → {'✅ 클라이언트 재사용됨' if pb['misses'] < pb['calls'] else '⚠️ 캐시 미작동'}")
    from common import out, write_json
    p = write_json(out("daemon_latency.json"), res)
    print(f"\n  기록: {p}")


if __name__ == "__main__":
    main()
