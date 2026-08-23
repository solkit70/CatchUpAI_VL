#!/usr/bin/env python3
"""M7 실습 6 — 전체 파이프라인 지연 측정 + 사전 캐시 효과.

## 무엇을 재는가

목표(로드맵): **발화 종료 → 화면 2.5초 / → 음성 4초**

이 스크립트가 재는 것은 **화면까지**다. 음성까지의 지연은 여기서 확정할 수 없다 —
M6 실측(TTS 첫 청크 588ms)은 *파일이 만들어지기까지*이고, 스피커에서 소리가 나기까지는
가상 케이블 버퍼가 더해진다. 그 값은 M6 오디오 라우팅을 구성한 뒤에야 잴 수 있다.
그래서 음성 목표는 '미확정'으로 보고한다. 재지 않은 것을 잰 척하지 않는다.

## 사전 캐시란 무엇인가

①② 단계(Rundown 파싱 + 컨텍스트 조립)는 **방송 전에 끝낼 수 있는 일**이다.
Rundown 은 방송 중에 바뀌지 않고, 파트별 근거 풀도 미리 만들어 둘 수 있다.

  cold  ① ② ③ ④ ⑤ ⑥ 을 전부 발화 시점에 실행   ← 사전 캐시 없음
  warm  ③ ④ ⑤ ⑥ 만 발화 시점에 실행            ← ①② 는 방송 전 완료

두 조건의 차이가 사전 캐시의 값어치다.

## 왜 한 번만 재지 않는가

LLM 호출은 회차마다 흔들린다(M5 실측: openai 기본값 12.2~18.1초). 한 번 재고
"2.4초 달성"이라고 적으면 방송에서 배신당한다. 중앙값과 **최악값**을 함께 본다 —
방송에서 사고를 만드는 것은 최악값이다.

실행:
    python run_pipeline.py --live 21 --repeats 3
    python run_pipeline.py --live 21 --repeats 3 --mode cold
    python run_pipeline.py --live 21 --text "3번 파트에서 뭘 다루나요?"

산출:
    ../guides/latency-report.md 에 붙일 수치 + output/latency_pipeline.json
"""
from __future__ import annotations

import argparse
import statistics
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from common import out, trace, write_json  # noqa: E402

# 로드맵 목표치
TARGET_SCREEN_MS = 2500
TARGET_VOICE_MS = 4000

DEFAULT_TEXT = "오늘 3번 파트에서 뭘 다루나요?"


def run(stage: str, args: list[str]) -> tuple[int, int]:
    """(exit_code, 소요 ms). 출력은 삼킨다 — 측정 중 콘솔 I/O 도 지연이다."""
    t0 = time.time()
    r = subprocess.run([sys.executable, str(HERE / stage), *args],
                       capture_output=True, text=True, encoding="utf-8")
    return r.returncode, round((time.time() - t0) * 1000)


def one_pass(live: str, text: str, warm: bool) -> dict:
    """한 번의 발화 처리. warm 이면 ①② 를 건너뛴다 (방송 전에 끝냈다고 가정)."""
    stages: list[tuple[str, str, list[str]]] = []
    if not warm:
        stages += [("①", "01_parse_rundown.py", ["--live", live]),
                   ("②", "02_resolve_context.py", ["--live", live, "--part", "3"])]
    stages += [
        ("③", "03_classify_intent.py", ["--live", live, "--text", text]),
        ("④", "04_compose_answer.py", ["--live", live]),
        ("⑤", "05_verify_and_gate.py", ["--live", live]),
        ("⑥", "06_render_output.py", ["--live", live]),
    ]

    per: dict[str, int] = {}
    total = 0
    for label, script, a in stages:
        code, ms = run(script, a)
        per[label] = ms
        total += ms
        if code != 0:
            return {"ok": False, "failed_at": label, "per_stage": per, "total_ms": total}
    return {"ok": True, "per_stage": per, "total_ms": total}


def summarize(runs: list[dict]) -> dict:
    good = [r for r in runs if r["ok"]]
    if not good:
        return {"n_ok": 0}
    tot = [r["total_ms"] for r in good]
    stages = sorted({k for r in good for k in r["per_stage"]})
    return {
        "n": len(runs), "n_ok": len(good),
        "total_med_ms": round(statistics.median(tot)),
        "total_max_ms": max(tot),
        "stage_med_ms": {s: round(statistics.median(
            [r["per_stage"][s] for r in good if s in r["per_stage"]])) for s in stages},
    }


def verdict_line(med: int, mx: int) -> str:
    if mx <= TARGET_SCREEN_MS:
        return f"목표 달성 (최악값 {mx}ms ≤ {TARGET_SCREEN_MS}ms)"
    if med <= TARGET_SCREEN_MS:
        return (f"중앙값은 달성, **최악값 초과** ({mx}ms > {TARGET_SCREEN_MS}ms) — "
                f"방송에서는 최악값이 사고를 만든다")
    return f"목표 미달 (중앙값 {med}ms > {TARGET_SCREEN_MS}ms)"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--live", default="21")
    ap.add_argument("--text", default=DEFAULT_TEXT)
    ap.add_argument("--repeats", type=int, default=3)
    ap.add_argument("--mode", choices=["both", "cold", "warm"], default="both")
    args = ap.parse_args()

    modes = ["cold", "warm"] if args.mode == "both" else [args.mode]
    results: dict[str, dict] = {}

    for mode in modes:
        warm = mode == "warm"
        if warm:
            # 사전 캐시 조건을 실제로 만든다 — ①② 를 미리 돌려 둔다.
            print(f"\n[warm] 방송 전 준비: ①② 를 미리 실행합니다")
            for st, a in (("01_parse_rundown.py", ["--live", args.live]),
                          ("02_resolve_context.py", ["--live", args.live, "--part", "3"])):
                code, ms = run(st, a)
                if code != 0:
                    sys.exit(f"사전 준비 실패: {st}")
                print(f"        {st} {ms}ms")

        print(f"\n═══ {mode} — {args.repeats}회 ═══")
        runs = []
        for i in range(args.repeats):
            r = one_pass(args.live, args.text, warm)
            runs.append(r)
            if r["ok"]:
                detail = " · ".join(f"{k}{v}" for k, v in r["per_stage"].items())
                print(f"  #{i+1}  {r['total_ms']:>6}ms   {detail}")
            else:
                print(f"  #{i+1}  실패 at {r['failed_at']} ({r['total_ms']}ms)")
        results[mode] = {"runs": runs, "summary": summarize(runs)}

    # ── 보고 ──────────────────────────────────────────────────────────
    print(f"\n{'조건':<6} {'중앙':>9} {'최악':>9}   단계별 중앙값")
    print("-" * 68)
    for mode, r in results.items():
        s = r["summary"]
        if not s.get("n_ok"):
            print(f"{mode:<6} {'전부 실패':>9}")
            continue
        per = " ".join(f"{k}{v}" for k, v in s["stage_med_ms"].items())
        print(f"{mode:<6} {s['total_med_ms']:>7}ms {s['total_max_ms']:>7}ms   {per}")

    if "cold" in results and "warm" in results:
        c, w = results["cold"]["summary"], results["warm"]["summary"]
        if c.get("n_ok") and w.get("n_ok"):
            gain = c["total_med_ms"] - w["total_med_ms"]
            print(f"\n사전 캐시 효과: {gain:+,}ms "
                  f"({c['total_med_ms']:,} → {w['total_med_ms']:,})")

    if "warm" in results and results["warm"]["summary"].get("n_ok"):
        s = results["warm"]["summary"]
        print(f"\n【화면 목표 {TARGET_SCREEN_MS}ms】 {verdict_line(s['total_med_ms'], s['total_max_ms'])}")
    print(f"【음성 목표 {TARGET_VOICE_MS}ms】 **미확정** — TTS 재생 경로가 아직 없다. "
          f"M6 오디오 라우팅 구성 후 가상 케이블 버퍼를 더해야 확정된다")

    path = write_json(out("latency_pipeline.json"),
                      {"text": args.text, "targets_ms": {"screen": TARGET_SCREEN_MS,
                                                         "voice": TARGET_VOICE_MS},
                       "results": {k: v["summary"] for k, v in results.items()},
                       "raw": results})
    trace("run_pipeline", ok=True, repeats=args.repeats,
          summary={k: v["summary"] for k, v in results.items()}, output=path.name)
    print(f"\n원자료: {path.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
