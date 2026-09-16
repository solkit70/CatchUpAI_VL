#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""언어 축 — 시간 추세와 시청자 국가 (M3 추가분 2, 2026-09-13)

사용자 가설(9/13): "최근에 AI 로 만든 영상 중 영어 버전의 뷰수가 조금씩 많아지는 것 같다."

lifetime 조회로는 못 본다 — 오래된 영상이 더 많이 쌓였을 뿐이다. 그래서 **월별로 발생한 조회**를 본다:
    ① 월 구간(6·7·8·9월)마다 dimensions=video + filters=video==30편 → 그 달에 발생한 영상별 조회·구독
    ② 언어별로 합쳐 「그 달에 EN 판이 차지한 비율」의 추세
    ③ 시청자 국가 — dimensions=country (되살리기 구간) → 「한국인 중심」의 직접 증거

    python scripts/language_trend.py          # API 호출 (토큰: 01-Data-Pipeline/.secrets)
    python scripts/language_trend.py --cached # 저장된 JSON 으로만

출력 JSON: 01-Data-Pipeline/data/raw/lang_monthly.json · country.json
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
TOPIC = HERE.parent.parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(TOPIC / "01-Data-Pipeline" / "scripts"))
from classify_tracks import load, track_of  # noqa: E402

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

RAW = TOPIC / "01-Data-Pipeline" / "data" / "raw"
HANGUL = re.compile(r"[가-힣]")
START, END = "2026-06-01", "2026-09-10"


def ai_videos() -> list[dict]:
    rows = [r for r in load() if r.get("publishedAt", "")[:7] >= "2026-06" and track_of(r) == "AI제작"]
    for r in rows:
        r["lang"] = "KR" if HANGUL.search(r.get("title", "")) else "EN"
    return rows


MONTHS = [("2026-06", "2026-06-01", "2026-06-30"), ("2026-07", "2026-07-01", "2026-07-31"),
          ("2026-08", "2026-08-01", "2026-08-31"), ("2026-09", "2026-09-01", "2026-09-10")]


def fetch(rows: list[dict]) -> tuple[dict, list]:
    """월 구간마다 dimensions=video + filters=video==id,id,... 한 번씩 (4회). 영상별 day 조회는 500 이 났다."""
    from youtube_analytics import services, rows_of  # noqa: E402
    ya, _ = services()
    ids = ",".join(r["video"] for r in rows)
    monthly: dict[str, list] = {r["video"]: [] for r in rows}
    for label, s, e in MONTHS:
        resp = ya.reports().query(
            ids="channel==MINE", startDate=s, endDate=e,
            metrics="views,subscribersGained", dimensions="video", filters=f"video=={ids}",
            maxResults=200,
        ).execute()
        for m in rows_of(resp):
            monthly[m["video"]].append({"month": label, "views": m["views"], "subscribersGained": m["subscribersGained"]})
    (RAW / "lang_monthly.json").write_text(json.dumps(monthly, ensure_ascii=False, indent=1), encoding="utf-8")
    resp = ya.reports().query(
        ids="channel==MINE", startDate=START, endDate=END,
        metrics="views,subscribersGained,estimatedMinutesWatched", dimensions="country",
        sort="-views", maxResults=15,
    ).execute()
    country = rows_of(resp)
    (RAW / "country.json").write_text(json.dumps(country, ensure_ascii=False, indent=1), encoding="utf-8")
    return monthly, country


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--cached", action="store_true")
    args = ap.parse_args()
    rows = ai_videos()
    if args.cached:
        monthly = json.loads((RAW / "lang_monthly.json").read_text(encoding="utf-8"))
        country = json.loads((RAW / "country.json").read_text(encoding="utf-8"))
    else:
        monthly, country = fetch(rows)

    lang = {r["video"]: r["lang"] for r in rows}
    agg: dict[str, dict] = defaultdict(lambda: {"KR": [0, 0], "EN": [0, 0]})
    for vid, mrows in monthly.items():
        for m in mrows:
            a = agg[m["month"]][lang[vid]]
            a[0] += int(m["views"]); a[1] += int(m["subscribersGained"])

    print(f"■ AI 제작 {len(rows)}편 (KR {sum(1 for r in rows if r['lang']=='KR')} · EN {sum(1 for r in rows if r['lang']=='EN')}) — 월별 발생 조회·구독\n")
    print(f"  {'월':<9}{'KR 조회':>8}{'EN 조회':>8}{'EN 비율':>8}   {'KR 구독':>7}{'EN 구독':>7}")
    for m in sorted(agg):
        k, e = agg[m]["KR"], agg[m]["EN"]
        tot = k[0] + e[0]
        print(f"  {m:<9}{k[0]:>8,}{e[0]:>8,}{(e[0]/tot*100 if tot else 0):>7.0f}%   {k[1]:>7}{e[1]:>7}")

    print("\n■ 시청자 국가 — 채널 전체, 되살리기 구간 (상위)\n")
    tot_v = sum(int(c["views"]) for c in country) or 1
    print(f"  {'국가':<6}{'조회':>8}{'비율':>7}{'구독':>6}")
    for c in country[:10]:
        print(f"  {c['country']:<6}{int(c['views']):>8,}{int(c['views'])/tot_v*100:>6.0f}%{int(c['subscribersGained']):>6}")
    print("\n⚠️ 국가 = 시청 위치. 한국어 사용자 ≠ KR 국가 (미국 거주 한국인은 US 로 잡힌다).")


if __name__ == "__main__":
    main()
