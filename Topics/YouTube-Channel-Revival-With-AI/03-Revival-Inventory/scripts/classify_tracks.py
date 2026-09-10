#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""콘텐츠를 세 갈래로 나눈다 — 가설 2 재판정용 (M3)

브레인덤프의 분류를 그대로 쓴다.

    ① AI 제작    VibeLearn AI 로 조사하고 Remotion 으로 만든 영상 — **사람이 안 나온다**
    ② 세미나     시애틀/벨뷰 지역 AI 세미나 녹화 — **발표자가 나온다**
    ③ 오프라인   Builders Lounge 등 자체 행사 — **사람이 나온다**
    ④ 라이브     AI in Action 주간 방송 아카이브 — 화면 공유 위주

    python scripts/classify_tracks.py            # 분류 결과와 판정
    python scripts/classify_tracks.py --list AI제작   # 그 갈래 목록 전부

⚠️ **제목 규칙에 의존한 자동 분류다.** M2 의 「AI in Action 이냐 아니냐」보다는 낫지만
여전히 대리 지표다. **`inventory/track-review.md` 에서 사람이 눈으로 확인한 뒤 확정한다.**
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

HERE = Path(__file__).resolve().parent.parent
DATA = HERE.parent / "01-Data-Pipeline" / "data" / "raw" / "all_videos.json"

# ─── 세미나 주최·시리즈 이름 ──────────────────────────────────────────────
# 이 채널이 녹화해 온 시애틀/벨뷰 지역 행사들. 제목 앞머리에 시리즈명이 붙는다.
SEMINAR = [
    "Seattle AI", "Beyond AI Models", "Women + AI", "Startup425",
    "Bridging Data", "GitHub Copilot Dev Days", "Big Data AI Seattle",
    "Informs", "Spark", "Databricks", "AI & the", "Sebastian Raschka",
    "Bill Kehoe", "Gen AI Zoo", "Mental Health", "Freakquency", "MoM -",
]
# ─── 오프라인 자체 행사 ───────────────────────────────────────────────────
OFFLINE = [
    "Builders Lounge", "ENG SUB", "HebronGuide", "Bila AI",
    "광복절", "페더럴웨이", "한인회", "다시 만나는",
]
LIVE = ["AI in Action"]


# 🔴 제목이 `AI in Action` 인 영상은 두 종류가 섞여 있다.
#   · 174~193분 = 라이브 방송 **원본 아카이브** (본인 얼굴 + 화면 공유)
#   · 10~16분   = 그 방송을 Remotion 으로 **다시 만든 요약 영상** (사람 안 나옴)
# 실물 확인: my-first-video/src/{live13~17-0607-summary, qwen3tts-0529, wa-recording-law-0607}
# 데이터상 두 무리 사이가 16분 ~ 120분으로 뚝 끊겨 있어 60분에서 가른다.
LIVE_RAW_MIN_SEC = 60 * 60


def track_of(r: dict) -> str:
    t = r.get("title", "")
    if any(k in t for k in LIVE) or re.search(r"Live\s*#?\d", t):
        return "라이브" if r["durationSec"] >= LIVE_RAW_MIN_SEC else "AI제작"
    if any(k in t for k in OFFLINE):
        # 자체 행사도 90분 넘는 것은 편집 없는 원본 녹화다
        return "오프라인" if r["durationSec"] < LIVE_RAW_MIN_SEC else "라이브"
    if any(k.lower() in t.lower() for k in SEMINAR):
        return "세미나"
    return "AI제작"


def load() -> list[dict]:
    rows = [r for r in json.loads(DATA.read_text(encoding="utf-8")) if r.get("hasData")]
    return [r for r in rows if r["durationSec"] > 180]      # 롱폼만


def stats(rs: list[dict]) -> tuple:
    v = sum(int(r.get("views", 0)) for r in rs)
    s = sum(int(r.get("subscribersGained", 0)) for r in rs)
    return len(rs), v, s, (s / v * 1000 if v else 0)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--list", help="갈래 이름 (AI제작/세미나/오프라인/라이브)")
    ap.add_argument("--since", default="", help="이 날짜 이후 공개분만 (YYYY-MM)")
    args = ap.parse_args()

    rows = load()
    if args.since:
        rows = [r for r in rows if r.get("publishedAt", "")[:7] >= args.since]

    by: dict[str, list] = {}
    for r in rows:
        by.setdefault(track_of(r), []).append(r)

    if args.list:
        sel = sorted(by.get(args.list, []), key=lambda r: -int(r.get("views", 0)))
        print(f"■ {args.list} — {len(sel)}편\n")
        for r in sel:
            print(f"  {r.get('publishedAt','')[:10]} {r['durationSec']/60:5.0f}분 "
                  f"조회{int(r.get('views',0)):6d} 구독{int(r.get('subscribersGained',0)):4d}  "
                  f"{r.get('title','')[:58]}")
        return

    label = f" ({args.since} 이후)" if args.since else ""
    print(f"■ 콘텐츠 갈래별 성과 — 롱폼 {len(rows)}편{label}\n")
    print(f"  {'갈래':<10}{'편수':>5}{'조회':>9}{'구독':>7}{'1천뷰당':>10}   {'사람':<6}")
    print("  " + "-" * 52)
    order = ["AI제작", "세미나", "오프라인", "라이브"]
    face = {"AI제작": "✗", "세미나": "○", "오프라인": "○", "라이브": "△"}
    res = {}
    for k in order:
        if k not in by:
            continue
        n, v, s, c = stats(by[k])
        res[k] = c
        print(f"  {k:<10}{n:>5}{v:>9,}{s:>7}{c:>10.2f}   {face[k]:<6}")

    # ── 가설 2 재판정: 사람이 나오는 갈래 vs 안 나오는 갈래
    print()
    faces = [r for k in ("세미나", "오프라인") for r in by.get(k, [])]
    nofaces = by.get("AI제작", [])
    n1, v1, s1, c1 = stats(faces)
    n2, v2, s2, c2 = stats(nofaces)
    print("■ 가설 2 재판정 — 사람이 나오는 영상 vs AI 제작 영상")
    print(f"  {'사람 나옴 (세미나+오프라인)':<30}{n1:>4}편  전환 {c1:6.2f}")
    print(f"  {'AI 제작 (사람 없음)':<30}{n2:>4}편  전환 {c2:6.2f}")
    if c1 and c2:
        ratio = c1 / c2
        if ratio >= 2.0:
            verdict = "✅ 맞다"
        elif ratio >= 1.3:
            verdict = "🔶 약한 차이"
        elif ratio > 1 / 1.3:
            verdict = "➖ 차이 없다"
        else:
            verdict = f"❌ 반대다 — AI 제작이 {1/ratio:.2f}배 높다"
        print(f"  → {ratio:.2f}배  {verdict}")

    # ── 진짜로 갈리는 축: 내가 만든 것 vs 남의 행사를 녹화한 것
    mine = [r for k in ("AI제작", "오프라인", "라이브") for r in by.get(k, [])]
    theirs = by.get("세미나", [])
    if mine and theirs:
        n3, v3, s3, c3 = stats(mine)
        n4, v4, s4, c4 = stats(theirs)
        print()
        print("■ 다시 나눠 본 축 — 내 콘텐츠 vs 남의 행사 녹화")
        print(f"  {'내가 만든 것 (제작+자체행사+라이브)':<34}{n3:>4}편  전환 {c3:6.2f}")
        print(f"  {'남의 행사 녹화 (세미나)':<34}{n4:>4}편  전환 {c4:6.2f}")
        if c4:
            print(f"  → {c3/c4:.2f}배")


if __name__ == "__main__":
    main()
