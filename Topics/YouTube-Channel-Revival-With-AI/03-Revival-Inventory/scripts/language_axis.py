#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""언어 축 — 되살리기 87편을 한국어/영어로 갈라 다시 본다 (M3 추가분, 2026-09-13)

사용자 지적(9/13): 세미나 녹화는 **영어 영상**(한국어 자막)이고 Builders Lounge 는 **한국어 영상**이다.
채널은 아직 한국인 구독자 중심이고, 2026 년부터 AI 제작 영상은 한/영 두 판을 만든다.
→ 갈래(노력)와 언어(청중)가 겹쳐 있으니 언어를 떼어 내야 「세미나 34편 · 구독 3명」을 바로 읽을 수 있다.

언어 판정 (대리 지표 — 메타데이터에 언어 필드가 없다):
    세미나          → EN  (사용자 확인: 발표 음성이 영어, 자막만 한국어)
    오프라인·라이브 → KR  (사용자 확인)
    AI 제작         → 제목에 한글이 있으면 KR, 없으면 EN  (2026 한/영 두 판)

한/영 짝 비교: AI 제작 중 **같은 날 올라간 KR·EN 한 쌍** = 같은 내용, 언어만 다름 → 가장 깨끗한 비교.

    python scripts/language_axis.py
"""
from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from classify_tracks import load, track_of, stats  # noqa: E402

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

HANGUL = re.compile(r"[가-힣]")
SINCE = "2026-06"


def lang_of(r: dict, track: str) -> str:
    if track == "세미나":
        return "EN"
    if track in ("오프라인", "라이브"):
        return "KR"
    return "KR" if HANGUL.search(r.get("title", "")) else "EN"


def fmt(rs: list[dict]) -> str:
    n, v, s, c = stats(rs)
    pv = v / n if n else 0
    ps = s / n if n else 0
    return f"{n:>4}편 {v:>7,} {s:>5} {pv:>8.0f} {ps:>7.2f}"


def main() -> None:
    rows = [r for r in load() if r.get("publishedAt", "")[:7] >= SINCE]
    for r in rows:
        r["track"] = track_of(r)
        r["lang"] = lang_of(r, r["track"])

    print(f"■ 언어 × 갈래 — 롱폼 {len(rows)}편 ({SINCE} 이후)\n")
    print(f"  {'갈래':<8}{'언어':<4}{'편수':>5}{'조회':>8}{'구독':>6}{'편당조회':>9}{'편당구독':>8}")
    print("  " + "-" * 50)
    by: dict[tuple, list] = defaultdict(list)
    for r in rows:
        by[(r["track"], r["lang"])].append(r)
    for tr in ("AI제작", "오프라인", "라이브", "세미나"):
        for lg in ("KR", "EN"):
            if (tr, lg) in by:
                print(f"  {tr:<8}{lg:<4}{fmt(by[(tr, lg)])}")

    print("\n■ 언어만으로 — 갈래 무시")
    for lg in ("KR", "EN"):
        sel = [r for r in rows if r["lang"] == lg]
        print(f"  {lg:<12}{fmt(sel)}")

    # 세미나(EN) 를 빼고 언어를 비교 — 세미나가 EN 을 통째로 끌어내리는지
    print("\n■ AI 제작만 — 같은 종류의 영상에서 언어 차이")
    for lg in ("KR", "EN"):
        sel = [r for r in rows if r["track"] == "AI제작" and r["lang"] == lg]
        print(f"  {lg:<12}{fmt(sel)}")

    # 한/영 짝 (AI 제작, 같은 날짜)
    print("\n■ 한/영 짝 — 같은 날 올라간 같은 내용 (AI 제작)")
    byday: dict[str, dict] = defaultdict(dict)
    for r in rows:
        if r["track"] == "AI제작":
            byday[r["publishedAt"][:10]][r["lang"]] = r
    pairs = [(d, v["KR"], v["EN"]) for d, v in sorted(byday.items()) if "KR" in v and "EN" in v]
    print(f"  {'날짜':<11}{'KR 조회':>7}{'구독':>5} {'EN 조회':>8}{'구독':>5}   제목(KR)")
    tk = tv = ts = ev = es = 0
    for d, k, e in pairs:
        kv, ks = int(k.get("views", 0)), int(k.get("subscribersGained", 0))
        evv, ess = int(e.get("views", 0)), int(e.get("subscribersGained", 0))
        tv += kv; ts += ks; ev += evv; es += ess; tk += 1
        print(f"  {d:<11}{kv:>7}{ks:>5} {evv:>8}{ess:>5}   {k.get('title','')[:40]}")
    if tk:
        print(f"  {'합계 ' + str(tk) + '쌍':<11}{tv:>7}{ts:>5} {ev:>8}{es:>5}")
        print(f"  → 조회 KR/EN = {tv/ev:.2f}배 · 구독 KR/EN = {(ts/es) if es else float('inf'):.2f}배 "
              f"(EN 구독 {es}명)")
    print("\n⚠️ 언어는 제목 문자 기준 대리 지표. 세미나·오프라인·라이브는 사용자 확인값.")


if __name__ == "__main__":
    main()
