#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""채널의 **모든** 영상 지표를 받는다 — 500편 제한을 넘어서 (M1 보강)

    python scripts/fetch_all_videos.py
    python scripts/fetch_all_videos.py --start 2025-01-01

🔴 **왜 필요한가**

YouTube Studio 의 CSV 내보내기는 **상위 500편에서 잘린다** (파일 마지막 줄
`Showing top 500 results`). 이 채널은 628편이라 **128편이 통째로 빠진다.**
빠지는 쪽은 조회수가 적은 영상들 — 그런데 가설 검증에서는 **그 꼬리가 표본**이다.

`dimensions=video` 리포트도 한 번에 200행까지만 준다.

**그래서 두 API 를 이어 붙인다.**

    ① Data API      업로드 재생목록을 훑어 **전체 영상 ID** 를 얻는다 (페이징)
    ② Analytics API `filters=video==` 로 200개씩 끊어 지표를 묻는다
    ③ Data API      제목·공개일·길이를 50개씩 붙인다

이렇게 하면 **채널 전체**가 나온다.

출력: `data/raw/all_videos.json` (🔒 깃 제외)
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import youtube_analytics as ya_mod          # noqa: E402

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

# Analytics 리포트가 한 번에 주는 최대 행 수. 여기에 맞춰 끊는다.
ANALYTICS_CHUNK = 200
# Data API videos.list 는 한 번에 50개까지
META_CHUNK = 50


def all_upload_ids(yt, uploads_playlist: str) -> list[str]:
    """업로드 재생목록을 끝까지 훑는다. 여기에는 **비공개·미등록도 포함**될 수 있다.

    🔴 **반드시 중복을 제거한다.** `playlistItems.list` 페이징이 **같은 영상을 여러 페이지에
    걸쳐 돌려준다.** 실측(2026-09-10): 654행을 받았는데 고유 ID 는 **532개**였다 — 122행 중복.

    이걸 모른 채 집계하면 **일부 영상이 두 번 세어져** 조회·구독이 부풀려진다.
    편수도 «654편»으로 잘못 보고하게 된다. 실제로 한 번 그렇게 보고했다.
    """
    seen, ids, token, raw = set(), [], None, 0
    while True:
        resp = yt.playlistItems().list(
            part="contentDetails", playlistId=uploads_playlist,
            maxResults=50, pageToken=token,
        ).execute()
        for it in resp.get("items", []):
            vid = it["contentDetails"].get("videoId")
            if not vid:
                continue
            raw += 1
            if vid in seen:          # 중복은 버린다
                continue
            seen.add(vid)
            ids.append(vid)
        token = resp.get("nextPageToken")
        print(f"\r  업로드 목록 수집 중... 고유 {len(ids)}편 (받은 행 {raw})",
              end="", flush=True)
        if not token:
            break
    print()
    if raw != len(ids):
        print(f"  ⚠️ 재생목록이 중복을 돌려줬다 — {raw}행 중 {raw - len(ids)}행 제거")
    return ids


def analytics_for(ya, ids: list[str], start: str, end: str) -> dict:
    """영상별 지표. 200개씩 끊어 묻고 하나로 합친다."""
    out = {}
    metrics = ("views,estimatedMinutesWatched,averageViewDuration,"
               "averageViewPercentage,subscribersGained,subscribersLost")
    for i in range(0, len(ids), ANALYTICS_CHUNK):
        chunk = ids[i:i + ANALYTICS_CHUNK]
        resp = ya.reports().query(
            ids="channel==MINE", startDate=start, endDate=end,
            metrics=metrics, dimensions="video",
            filters="video==" + ",".join(chunk),
            maxResults=ANALYTICS_CHUNK,
        ).execute()
        heads = [h["name"] for h in resp.get("columnHeaders", [])]
        for row in resp.get("rows", []):
            d = dict(zip(heads, row))
            out[d["video"]] = d
        print(f"\r  지표 수집 중... {min(i+ANALYTICS_CHUNK, len(ids))}/{len(ids)}",
              end="", flush=True)
    print()
    return out


def meta_for(yt, ids: list[str]) -> dict:
    out = {}
    for i in range(0, len(ids), META_CHUNK):
        resp = yt.videos().list(
            part="snippet,contentDetails,statistics",
            id=",".join(ids[i:i + META_CHUNK]), maxResults=META_CHUNK,
        ).execute()
        for it in resp.get("items", []):
            out[it["id"]] = {
                "title": it["snippet"]["title"],
                "publishedAt": it["snippet"]["publishedAt"],
                "duration": it["contentDetails"]["duration"],
                "privacy": it.get("status", {}).get("privacyStatus"),
                "lifetimeViews": it.get("statistics", {}).get("viewCount"),
            }
        print(f"\r  메타데이터 수집 중... {len(out)}/{len(ids)}", end="", flush=True)
    print()
    return out


def iso_seconds(iso: str) -> int:
    """ISO 8601 기간(PT20M43S) → 초. Shorts 판정에 쓴다."""
    import re
    m = re.fullmatch(r"P(?:(\d+)D)?T?(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?", iso or "")
    if not m:
        return 0
    d, h, mi, s = (int(x) if x else 0 for x in m.groups())
    return d * 86400 + h * 3600 + mi * 60 + s


def main() -> None:
    ap = argparse.ArgumentParser(description="채널 전체 영상 지표 수집")
    ap.add_argument("--start", default="2025-01-01")
    ap.add_argument("--end", default=dt.date.today().isoformat())
    args = ap.parse_args()

    ya, yt = ya_mod.services()
    info = ya_mod.channel_info(yt)
    print(f"채널 {info['title']} · 공개 영상 {info['videoCount']}편\n")

    ids = all_upload_ids(yt, info["uploadsPlaylist"])
    stats = analytics_for(ya, ids, args.start, args.end)
    meta = meta_for(yt, ids)

    merged = []
    for vid in ids:
        row = {"video": vid}
        row.update(meta.get(vid, {}))
        row.update(stats.get(vid, {}))
        row["durationSec"] = iso_seconds(row.get("duration", ""))
        row["hasData"] = vid in stats      # 기간 내 조회가 0이면 지표가 안 온다
        merged.append(row)

    ya_mod.save("all_videos", merged)

    with_data = [r for r in merged if r["hasData"]]
    shorts = [r for r in with_data if 0 < r["durationSec"] <= 180]
    print()
    print(f"업로드 목록      {len(ids)}편")
    print(f"기간 내 지표 있음 {len(with_data)}편  (없음 {len(merged)-len(with_data)}편 — 조회 0)")
    print(f"  · Shorts(≤3분)  {len(shorts)}편")
    print(f"  · 롱폼          {len(with_data)-len(shorts)}편")
    print()
    print("🔴 Studio CSV 는 상위 500편에서 잘린다. 이 파일은 잘리지 않는다.")
    print(f"→ {ya_mod.RAW / 'all_videos.json'}")


if __name__ == "__main__":
    main()
