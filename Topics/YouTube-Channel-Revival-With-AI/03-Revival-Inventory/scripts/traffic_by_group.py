#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""작전 2 전·후 그룹의 **유입 경로**를 따로 받아 본다 (M3 보강)

왜 필요한가 — 작전 2 뒤에 편당 조회는 2.36배 늘었는데 **1천뷰당 구독은 0.55배로 떨어졌다.**
숫자만으로는 두 가지 설명이 다 가능하다.

  ① 새 사람이 많이 들어왔다 → 모수가 커져 전환율이 희석됐다 (좋은 신호)
  ② 영상이 구독을 덜 만들게 됐다 (나쁜 신호)

**유입 경로가 이 둘을 가른다.**

실측 결과는 **둘 중 어느 쪽도 아니었다** — 늘어난 조회의 대부분이 **구독 피드(3.17배)와
외부 링크(2.78배)** 에서 왔다. 이미 구독한 사람은 구독을 또 누를 수 없으니 전환율은
당연히 떨어진다. 그리고 **유튜브 검색만 0.76배로 줄었다.**

    python scripts/traffic_by_group.py
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent.parent / "01-Data-Pipeline" / "scripts"))

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

import youtube_analytics as ya_mod          # noqa: E402  인증·채널 확인을 그대로 쓴다
from operations import groups                # noqa: E402  그룹 정의는 여기 한 곳

START, END = "2026-04-01", "2026-09-10"
# 사람이 읽을 이름
KO = {
    "SUBSCRIBER": "구독 피드",
    "YT_SEARCH": "유튜브 검색",
    "RELATED_VIDEO": "추천 영상",
    "YT_CHANNEL": "채널 페이지",
    "EXT_URL": "외부 링크",
    "NOTIFICATION": "알림",
    "PLAYLIST": "재생목록",
    "NO_LINK_OTHER": "직접·기타",
    "YT_OTHER_PAGE": "기타 유튜브",
    "SHORTS": "Shorts 피드",
}


def fetch(ya, ids: list[str]) -> dict:
    """영상 묶음의 유입 경로. filters=video== 는 200개까지."""
    out: dict[str, int] = {}
    for i in range(0, len(ids), 200):
        chunk = ids[i:i + 200]
        resp = ya.reports().query(
            ids="channel==MINE", startDate=START, endDate=END,
            metrics="views", dimensions="insightTrafficSourceType",
            filters="video==" + ",".join(chunk), sort="-views",
        ).execute()
        for r in ya_mod.rows_of(resp):
            out[r["insightTrafficSourceType"]] = out.get(r["insightTrafficSourceType"], 0) + int(r["views"])
    return out


def show(name: str, d: dict) -> dict:
    tot = sum(d.values())
    print(f"\n■ {name} — 조회 {tot:,}회")
    for k, v in sorted(d.items(), key=lambda x: -x[1])[:7]:
        print(f"    {KO.get(k, k):<12}{v:>7,}회  {v/tot*100:5.1f}%")
    return {k: v / tot * 100 for k, v in d.items()} if tot else {}


def main() -> None:
    before, after = groups()          # 🔴 그룹 정의는 operations.py 한 곳에만 둔다

    ya, yt = ya_mod.services()
    ya_mod.channel_info(yt)                   # 🔴 엉뚱한 채널이면 여기서 멈춘다

    ra = fetch(ya, [r["video"] for r in before])
    rb = fetch(ya, [r["video"] for r in after])
    a = show(f"전환 전 · 라이브 파생 {len(before)}편", ra)
    b = show(f"전환 후 · 단일 주제 {len(after)}편", rb)

    print("\n■ 무엇이 달라졌나 (비중 %p)\n")
    print(f"    {'경로':<12}{'전환 전':>8}{'전환 후':>8}{'차이':>9}")
    print("    " + "-" * 38)
    for k in sorted(set(a) | set(b), key=lambda k: -(b.get(k, 0))):
        d = b.get(k, 0) - a.get(k, 0)
        mark = "  ⬆" if d > 3 else ("  ⬇" if d < -3 else "")
        print(f"    {KO.get(k, k):<12}{a.get(k,0):>7.1f}%{b.get(k,0):>7.1f}%{d:>+8.1f}{mark}")

    # 🔴 비중만 보면 틀린다 — 구독 유입이 급증하면 다른 경로의 「비중」은 저절로 줄어든다.
    #    편수도 다르므로 **편당 절대 조회수**로 견주는 것이 맞다.
    print("\n■ 🔴 편당 절대 조회수로 다시 — 비중은 착시를 만든다\n")
    print(f"    {'경로':<12}{'전환 전':>9}{'전환 후':>9}{'배수':>9}")
    print("    " + "-" * 41)
    na, nb = len(before), len(after)
    for k in sorted(set(ra) | set(rb), key=lambda k: -(rb.get(k, 0) / nb)):
        x, y = ra.get(k, 0) / na, rb.get(k, 0) / nb
        if x < 0.5 and y < 0.5:
            continue
        rt = f"{y/x:.2f}배" if x else "—"
        mark = "  ⬇ 유일하게 줄었다" if x and y / x < 1 else ""
        print(f"    {KO.get(k, k):<12}{x:>8.1f}회{y:>8.1f}회{rt:>9}{mark}")


if __name__ == "__main__":
    main()
