#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Shorts 를 안 올린 뒤에도 Shorts 조회가 계속 나오는가 (M2)

사용자 확인 (2026-09-10): **2026-03-31 이후 Shorts 를 전혀 올리지 않았다.**
그렇다면 4월 이후의 Shorts 조회는 전부 **과거에 올려 둔 것이 알아서 벌어들인 것**이다.
그 양이 줄고 있는지, 유지되는지, 오히려 늘고 있는지를 본다.

    python scripts/shorts_over_time.py

Studio CSV 로 Shorts 영상 목록(길이 ≤ 3분)을 뽑고,
Analytics API 에 `filters=video==...` 로 월별 조회를 묻는다.
"""
from __future__ import annotations

import csv
import io
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE.parent / "01-Data-Pipeline" / "scripts"))
import youtube_analytics as ya_mod          # noqa: E402

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

DATA = HERE.parent / "01-Data-Pipeline" / "data" / "youtube-analytics"
SHORTS_MAX_SEC = 180
VIDEO_ID = re.compile(r"[A-Za-z0-9_-]{11}")
START, END = "2025-01-01", "2026-09-01"     # month 차원은 양쪽 다 「그 달 1일」


def load_ids() -> tuple[list[str], list[str]]:
    path = sorted(DATA.glob("content-*/Table data.csv"))[-1]
    shorts, longform = [], []
    with io.open(path, encoding="utf-8-sig", newline="") as f:
        for r in csv.DictReader(f):
            # ⚠️ Studio CSV 에는 영상이 아닌 행이 섞여 있다.
            #   · ID 앞뒤에 공백  → `Invalid value ( -PeOMp6ekwo)` 400
            #   · 마지막 줄 `Showing top 500 results` → 같은 오류
            # 🔴 그 꼬리표는 **내보내기가 500편에서 잘렸다**는 뜻이기도 하다.
            # 채널 전체는 628편(Data API)이므로 CSV 에는 하위 128편이 빠져 있다.
            cid = (r.get("Content") or "").strip()
            if not VIDEO_ID.fullmatch(cid):
                continue
            try:
                dur = int(r["Duration"] or 0)
            except (TypeError, ValueError):
                continue
            (shorts if 0 < dur <= SHORTS_MAX_SEC else longform).append(cid)
    return shorts, longform


def monthly_views(ya, ids: list[str], label: str) -> dict:
    """영상 목록을 걸어 월별 조회를 받는다. filters 는 500개까지 허용된다."""
    out = {}
    for i in range(0, len(ids), 200):
        chunk = ids[i:i + 200]
        resp = ya.reports().query(
            ids="channel==MINE", startDate=START, endDate=END,
            metrics="views,subscribersGained", dimensions="month", sort="month",
            filters="video==" + ",".join(chunk),
        ).execute()
        heads = [h["name"] for h in resp.get("columnHeaders", [])]
        for row in resp.get("rows", []):
            d = dict(zip(heads, row))
            m = d["month"]
            acc = out.setdefault(m, {"views": 0, "subs": 0})
            acc["views"] += int(d.get("views", 0) or 0)
            acc["subs"] += int(d.get("subscribersGained", 0) or 0)
    ya_mod.save(f"monthly_{label}", out)
    return out


def main() -> None:
    shorts, longform = load_ids()
    print(f"Shorts {len(shorts)}편 · 롱폼 {len(longform)}편\n")

    ya, _ = ya_mod.services()
    s = monthly_views(ya, shorts, "shorts")
    l = monthly_views(ya, longform, "longform")

    months = sorted(set(s) | set(l))
    print("  월        Shorts조회  Shorts구독 |   롱폼조회   롱폼구독 | Shorts 비중")
    print("  " + "-" * 72)
    for m in months:
        sv = s.get(m, {}).get("views", 0)
        ss = s.get(m, {}).get("subs", 0)
        lv = l.get(m, {}).get("views", 0)
        ls = l.get(m, {}).get("subs", 0)
        share = sv / (sv + lv) * 100 if (sv + lv) else 0
        mark = "  ← 마지막 Shorts 업로드" if m == "2026-03" else ""
        print(f"  {m}   {sv:>9,} {ss:>10} | {lv:>9,} {ls:>9} | {share:>8.0f}%{mark}")

    # 업로드 중단 전후 비교
    before = [m for m in months if m <= "2026-03"]
    after = [m for m in months if m >= "2026-04"]
    bv = sum(s.get(m, {}).get("views", 0) for m in before)
    av = sum(s.get(m, {}).get("views", 0) for m in after)
    print()
    print(f"  업로드하던 기간 ({before[0]}~2026-03, {len(before)}개월): "
          f"Shorts 조회 {bv:,}  월평균 {bv/len(before):,.0f}")
    print(f"  중단한 뒤     (2026-04~{after[-1]}, {len(after)}개월): "
          f"Shorts 조회 {av:,}  월평균 {av/len(after):,.0f}")
    if before and after:
        print(f"  → 월평균 {(av/len(after))/(bv/len(before))*100:.0f}% 수준")


if __name__ == "__main__":
    main()
