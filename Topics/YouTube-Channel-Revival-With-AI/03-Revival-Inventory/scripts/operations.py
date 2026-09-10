#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""작전 1·2를 개입 시점 기준으로 본다 (M3 보강)

사용자 증언 (2026-09-10):
  · 라이브 방송 요약은 **Live #17 (2026-07-10, F50yRfFhyIw) 까지만** 만들었다
  · *"단순히 라이브 방송을 요약하는 것은 별로 유용한 정보가 아니라서
     시청률이 많이 올라가지 않는다고 판단했다"*
  · 그래서 다음 영상부터 **요약을 없애고 단일 주제 영상**으로 갔다
  · 작전 1 = 자막(한↔영)을 영상에 굽는다 · 작전 2 = **콘텐츠 퀄리티를 올린다**

여기서 확인하는 것:
  ① 「요약은 안 먹힌다」는 그때의 판단이 데이터로 맞았나
  ② 작전 2(단일 주제 전환) 뒤에 실제로 나아졌나

⚠️ **최근 영상일수록 쌓인 기간이 짧다.** 이 편향은 「전환 후」 그룹에 불리하게 작동하므로,
「전환 후가 더 낫다」는 결과가 나오면 그건 **보수적인 결론**이다. 반대 결과는 해석하지 않는다.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

DATA = Path(__file__).resolve().parent.parent.parent / "01-Data-Pipeline" / "data" / "raw" / "all_videos.json"

# ─── 작전 2 의 경계 ───────────────────────────────────────────────────────
# 마지막 라이브 파생 영상. 이 날짜 「이후」가 단일 주제 시대다.
LAST_RECAP_ID = "F50yRfFhyIw"          # Live #17 Recap (KO)
LAST_RECAP_EN = "_S82H5EVTnc"          # 같은 날 영어판 — 제목에 "AI in Action" 이 없어 제목 검색에 안 걸린다
OP2_BOUNDARY = "2026-07-10"

# 라이브 파생 영상 중 **제목이 「요약/Recap/실험들」인 것** = 순수 요약본
# 🔴 영어판은 표기가 제각각이다 — Recap · Summary · Highlights · Experiments from …
RECAP_MARKS = [
    "요약", "실험들", "이번 주 실험", "실전 실험",
    "Recap", "Summary", "Highlights", "Today's Experiments", "Experiments from",
]
# 🔴 짝인데 한쪽만 안 걸리는 것 — 한국어판은 「Live #17 Recap」인데 영어 제목엔 표시가 없다.
#    제목 규칙으로는 절대 못 잡으므로 손으로 적어 둔다.
RECAP_IDS = {LAST_RECAP_EN}


def load() -> list[dict]:
    rows = [r for r in json.loads(DATA.read_text(encoding="utf-8")) if r.get("hasData")]
    return [r for r in rows if r["durationSec"] > 180]


def is_live_spinoff(r: dict) -> bool:
    """라이브 방송에 딸려 나온 짧은 영상인가"""
    if r["video"] in (LAST_RECAP_ID, LAST_RECAP_EN):
        return True
    return "AI in Action" in r.get("title", "") and r["durationSec"] < 3600


def is_pure_recap(r: dict) -> bool:
    if r["video"] in RECAP_IDS:
        return True
    return any(m in r.get("title", "") for m in RECAP_MARKS)


def stats(rs: list[dict]) -> tuple:
    v = sum(int(r.get("views", 0)) for r in rs)
    s = sum(int(r.get("subscribersGained", 0)) for r in rs)
    n = len(rs)
    return n, v, s, (v / n if n else 0), (s / v * 1000 if v else 0), (s / n if n else 0)


def line(label: str, rs: list[dict]) -> None:
    n, v, s, av, c, sp = stats(rs)
    print(f"  {label:<26}{n:>4}편{v:>8,}회{s:>6}명{av:>9.0f}{sp:>9.2f}{c:>9.2f}")


def groups() -> tuple[list[dict], list[dict]]:
    """작전 2 의 전·후 그룹. **다른 스크립트도 이 함수만 쓴다** (정의를 두 곳에 두지 않는다)."""
    from classify_tracks import track_of

    rows = load()
    # 라이브 «원본»(60분 이상)은 비교 대상이 아니다 — 편집 없이 올린 것이라 제작물이 아니다
    short = [r for r in rows if r["durationSec"] < 3600]

    before = [r for r in short if is_live_spinoff(r) and r["publishedAt"][:10] >= "2026-04-01"]
    after = [r for r in short
             if r["publishedAt"][:10] > OP2_BOUNDARY
             and not is_live_spinoff(r)
             and "AI in Action" not in r.get("title", "")
             # 🔴 사과는 사과와 견준다 — 양쪽 다 **Remotion 제작물**만 남긴다.
             #    행사 녹화(세미나·자체 행사)는 작전 1(자막)의 산물이라 섞으면 안 된다.
             and track_of(r) == "AI제작"]
    return before, after


def main() -> None:
    spin, after = groups()

    hdr = f"  {'그룹':<26}{'편수':>6}{'조회':>9}{'구독':>7}{'편당조회':>9}{'편당구독':>9}{'1천뷰당':>9}"
    print("■ 작전 2 — 라이브 요약을 그만두고 단일 주제로 (경계 2026-07-10)\n")
    print(hdr); print("  " + "-" * 75)
    line("전환 전 · 라이브 파생", spin)
    line("전환 후 · 단일 주제", after)
    _, _, _, av1, c1, sp1 = stats(spin)
    _, _, _, av2, c2, sp2 = stats(after)
    if av1 and c1 and sp1:
        print(f"\n  → 편당 조회 {av2/av1:.2f}배 · **편당 구독 {sp2/sp1:.2f}배** · 1천뷰당 구독 {c2/c1:.2f}배")
        print("\n  🔴 1천뷰당 구독이 떨어진 것은 나빠진 게 아니다 —")
        print("     늘어난 조회의 상당수가 **이미 구독한 사람**이고(구독 피드 편당 2.98배),")
        print("     구독자는 구독을 또 누를 수 없다. `traffic_by_group.py` 참조.")
        print("     **한 편을 만들었을 때 몇 명이 새로 들어오나 = 편당 구독**이 이 결정의 지표다.")

    print("\n■ 그때의 판단이 맞았나 — 라이브 파생 영상 안에서 갈라 본다\n")
    print(hdr); print("  " + "-" * 75)
    pure = [r for r in spin if is_pure_recap(r)]
    solo = [r for r in spin if not is_pure_recap(r)]
    line("순수 요약본", pure)
    line("단일 주제 스핀오프", solo)
    _, _, _, av3, c3, sp3 = stats(pure)
    _, _, _, av4, c4, sp4 = stats(solo)
    if av3 and c3:
        print(f"\n  → 같은 시기·같은 형식인데 편당 조회 {av4/av3:.2f}배 · 편당 구독 {sp4/sp3:.2f}배")
        print("  ⚠️ 평균으로는 근소하다. **판단의 근거는 평균이 아니라 최고점이었다** — 아래 참조.")

    print("\n■ 전환 전 상위 5편 (무엇이 판단의 근거가 됐나)\n")
    for r in sorted(spin, key=lambda x: -int(x.get("views", 0)))[:5]:
        tag = "요약 " if is_pure_recap(r) else "단일주제"
        print(f"  {r['publishedAt'][:10]} [{tag}] 조회{int(r['views']):5d} 구독{int(r['subscribersGained']):3d}  {r['title'][:52]}")


if __name__ == "__main__":
    main()
