#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""YouTube Analytics / Data API 수집기 — YouTube-Channel-Revival-With-AI M1

한 번 뚫어 두면 **다음 분기에도 다시 돌릴 수 있는 자산**이 된다.
Task Board 백로그 「유튜브 채널 관리 애플리케이션」의 첫 조각이기도 하다.

    python -m pip install google-api-python-client google-auth-oauthlib

사용법 (PowerShell, 이 폴더 기준):

    python scripts/youtube_analytics.py --check              # 인증만 확인
    python scripts/youtube_analytics.py --probe-impressions  # 노출/CTR 이 API 에 있나
    python scripts/youtube_analytics.py --daily              # ① 일 단위 시계열
    python scripts/youtube_analytics.py --videos             # ② 영상별 성과
    python scripts/youtube_analytics.py --traffic            # ③ 유입 경로
    python scripts/youtube_analytics.py --all                # ①②③ 한 번에

기간은 기본이 `--start 2026-01-01 --end (오늘)` 이다. P5 만 보려면 `--start 2026-06-01`.

⚠️ 토큰은 `.secrets/youtube_token.json` 에 저장된다. **캘린더 MCP 의 tokens.json 과 다른
파일이다** — 그쪽을 건드리면 달력 연결이 깨진다.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import sys
from pathlib import Path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

# ⚠️ 구글이 동의 후 `openid` 같은 스코프를 **자동으로 얹어서** 돌려주는 경우가 있다.
# 그러면 oauthlib 가 «Scope has changed from ... to ...» 로 인증을 실패시킨다.
# 우리가 요청한 것보다 넓어졌을 뿐 좁아진 게 아니므로 이 검사를 푼다.
os.environ.setdefault("OAUTHLIB_RELAX_TOKEN_SCOPE", "1")

# ─── 경로 ─────────────────────────────────────────────────────────────────
HERE = Path(__file__).resolve().parent.parent          # 01-Data-Pipeline/
SECRETS = HERE / ".secrets"
TOKEN = SECRETS / "youtube_token.json"
RAW = HERE / "data" / "raw"

# ─── OAuth 클라이언트 찾는 순서 ───────────────────────────────────────────
#
# 🔴 **캘린더 MCP 의 클라이언트를 재사용하려던 계획은 접었다** (2026-09-10).
# 그 클라이언트가 속한 프로젝트 `gen-lang-client-0588975117` 는 **다른 구글 계정 소유**라,
# 유튜브 계정(`seochang2011@gmail.com`)으로 콘솔에 들어가면
# *"You need additional access"* 가 뜨고 스코프를 추가할 수 없다.
#
# 그래서 **유튜브 계정이 소유한 프로젝트에 클라이언트를 새로 만든다.**
# 오히려 이쪽이 안전하다 — 캘린더 MCP 프로젝트를 아예 건드리지 않으므로
# 달력 연결이 깨질 여지가 없다.
#
# 찾는 순서:
#   ① 환경변수 YT_CLIENT_SECRETS
#   ② .secrets/client_secret.json      ← **여기에 내려받은 파일을 두면 된다**
#   ③ C:\Users\dougg\gcp-oauth.keys.json (캘린더용 — 접근 권한이 있을 때만 동작)
def _find_client_secrets() -> Path:
    env = os.environ.get("YT_CLIENT_SECRETS")
    if env:
        return Path(env)
    local = SECRETS / "client_secret.json"
    if local.exists():
        return local
    return Path(r"C:\Users\dougg\gcp-oauth.keys.json")


CLIENT_SECRETS = _find_client_secrets()

SCOPES = [
    "https://www.googleapis.com/auth/yt-analytics.readonly",           # 성과 지표
    "https://www.googleapis.com/auth/yt-analytics-monetary.readonly",  # 수익 (2026-09-10 추가)
    "https://www.googleapis.com/auth/youtube.readonly",                # 영상 메타데이터
]

# 🔒 **수익 데이터는 로컬에만 둔다.**
# `Ingest/CatchUpAI_VL` 은 공개 깃헙 레포이고, `data/` 는 .gitignore 로 제외해 뒀다.
# 발표나 글에 어떤 수익 숫자를 넣을지는 **별도 판단**이다 —
# 데이터를 갖는 것과 공개하는 것은 다른 결정이다.

# ─── 🔴 채널이 5개다 ──────────────────────────────────────────────────────
#
# 구글 계정 `seochang2011@gmail.com` 아래에 채널이 다섯 개 있다.
#   Wild Forager(기본, 1,010명) · 미생 영어 · AI Madang · Joosik Investment
#   그리고 **Catch Up AI (@catchupai, 4,320명)** ← 우리가 분석할 채널
#
# `ids="channel==MINE"` 은 **인증된 신원의 채널**로 풀린다. OAuth 동의 화면에서
# 계정을 고른 뒤 **채널 선택 화면에서 Catch Up AI 를 고르지 않으면**, 기본 채널인
# Wild Forager 의 지표를 가져와 놓고 그걸 모른 채 분석하게 된다.
#
# 그래서 **매 실행마다 어떤 채널로 인증됐는지 확인하고, 다르면 멈춘다.**
EXPECT_HANDLE = "@catchupai"
EXPECT_TITLE = "Catch Up AI"


# ─── 인증 ─────────────────────────────────────────────────────────────────
def get_credentials() -> Credentials:
    """토큰이 있으면 재사용하고, 없거나 만료면 브라우저 동의를 연다."""
    SECRETS.mkdir(parents=True, exist_ok=True)
    creds = None
    if TOKEN.exists():
        creds = Credentials.from_authorized_user_file(str(TOKEN), SCOPES)
    if creds and creds.valid:
        return creds
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        if not CLIENT_SECRETS.exists():
            raise SystemExit(
                f"OAuth 클라이언트 파일이 없다: {CLIENT_SECRETS}\n\n"
                "Google Cloud Console 에서 «데스크톱 앱» 클라이언트를 만들어 JSON 을 받고\n"
                f"  {SECRETS / 'client_secret.json'}\n"
                "에 두면 된다. 자세한 순서는 troubleshooting/oauth-setup.md 참조.")
        # 어느 프로젝트의 클라이언트인지 눈으로 확인할 수 있게 찍어 준다.
        try:
            _cs = json.loads(CLIENT_SECRETS.read_text(encoding="utf-8"))
            _k = next(iter(_cs))
            print(f"OAuth 클라이언트: {CLIENT_SECRETS}")
            print(f"  종류 {_k} · 프로젝트 {_cs[_k].get('project_id', '?')}")
        except Exception:
            pass
        flow = InstalledAppFlow.from_client_secrets_file(str(CLIENT_SECRETS), SCOPES)
        # 데스크톱 앱 클라이언트라 로컬 서버 방식이 그대로 된다.
        creds = flow.run_local_server(port=0, prompt="consent")
    TOKEN.write_text(creds.to_json(), encoding="utf-8")
    return creds


def services():
    creds = get_credentials()
    return (build("youtubeAnalytics", "v2", credentials=creds),
            build("youtube", "v3", credentials=creds))


# ─── 저장 ─────────────────────────────────────────────────────────────────
def save(name: str, payload) -> Path:
    RAW.mkdir(parents=True, exist_ok=True)
    p = RAW / f"{name}.json"
    p.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    return p


def rows_of(resp) -> list:
    """Analytics 응답을 [{열이름: 값}, ...] 로 편다."""
    heads = [h["name"] for h in resp.get("columnHeaders", [])]
    return [dict(zip(heads, r)) for r in resp.get("rows", [])]


# ─── ① 일 단위 시계열 ─────────────────────────────────────────────────────
def daily(ya, start: str, end: str) -> list:
    """dimensions=day. 여기서 **횡보 시작과 마이너스 전환 시점**이 나온다."""
    resp = ya.reports().query(
        ids="channel==MINE", startDate=start, endDate=end,
        metrics="views,subscribersGained,subscribersLost,estimatedMinutesWatched",
        dimensions="day", sort="day",
    ).execute()
    save("daily", resp)
    return rows_of(resp)


def weekly_from_daily(rows: list) -> list:
    """브레인덤프의 «횡보부터는 일주일 단위로 뽑아야 할 것 같음» 을 따른다.

    주의 — 여기서 내는 것은 **주간 순증(gained - lost)** 이지 구독자 총수가 아니다.
    총수는 Data API 의 `statistics.subscriberCount`(현재값)에서 거꾸로 누적해야 한다.
    """
    from collections import OrderedDict
    buckets: "OrderedDict[str, dict]" = OrderedDict()
    for r in rows:
        d = dt.date.fromisoformat(r["day"])
        wk = (d - dt.timedelta(days=d.weekday())).isoformat()   # 그 주 월요일
        b = buckets.setdefault(wk, {"week": wk, "views": 0,
                                    "subscribersGained": 0, "subscribersLost": 0})
        for k in ("views", "subscribersGained", "subscribersLost"):
            b[k] += int(r.get(k, 0) or 0)
    out = []
    for b in buckets.values():
        b["net"] = b["subscribersGained"] - b["subscribersLost"]
        out.append(b)
    return out


# ─── ② 영상별 성과 ────────────────────────────────────────────────────────
def videos(ya, start: str, end: str, limit: int = 200) -> list:
    """dimensions=video.

    ⚠️ **여기 나오는 subscribersGained 는 「그 영상의 시청 페이지에서 구독을 누른 횟수」뿐이다.**
    채널 페이지나 홈에서 구독하면 이 숫자에 안 잡힌다. 그래서 이 값은 언제나
    **기여의 하한선**으로만 읽는다. 감소(subscribersLost)는 원인 추적에 쓰지 않는다.
    """
    resp = ya.reports().query(
        ids="channel==MINE", startDate=start, endDate=end,
        metrics=("views,estimatedMinutesWatched,averageViewDuration,"
                 "averageViewPercentage,subscribersGained,subscribersLost"),
        dimensions="video", sort="-views", maxResults=limit,
    ).execute()
    save("videos", resp)
    return rows_of(resp)


def video_meta(yt, video_ids: list) -> dict:
    """Data API 로 제목·공개일·길이를 붙인다. 50개씩 끊어 부른다."""
    meta = {}
    for i in range(0, len(video_ids), 50):
        chunk = video_ids[i:i + 50]
        resp = yt.videos().list(part="snippet,contentDetails,statistics",
                                id=",".join(chunk), maxResults=50).execute()
        for it in resp.get("items", []):
            meta[it["id"]] = {
                "title": it["snippet"]["title"],
                "publishedAt": it["snippet"]["publishedAt"],
                "duration": it["contentDetails"]["duration"],
                "viewCount": it.get("statistics", {}).get("viewCount"),
            }
    save("video_meta", meta)
    return meta


# ─── ③ 유입 경로 ──────────────────────────────────────────────────────────
def traffic(ya, start: str, end: str) -> list:
    resp = ya.reports().query(
        ids="channel==MINE", startDate=start, endDate=end,
        metrics="views,estimatedMinutesWatched",
        dimensions="insightTrafficSourceType", sort="-views",
    ).execute()
    save("traffic", resp)
    return rows_of(resp)


# ─── ④ 수익 ───────────────────────────────────────────────────────────────
def revenue(ya, start: str, end: str) -> list:
    """월 단위 수익. `yt-analytics-monetary.readonly` 스코프가 있어야 한다.

    🔒 결과는 `data/raw/revenue.json` 에 남고 **그 폴더는 깃에서 제외**돼 있다.
    수익화가 안 된 기간은 0 이 나오거나 행 자체가 없다.

    ⚠️ **`dimensions=month` 는 시작도 끝도 「그 달 1일」이어야 한다.**
    2026-09-10 같은 달 중간은 물론이고, **말일(2026-08-31)도 거부당한다** —
    *"Date range does not align to chosen date dimension"* 400 이 난다.
    실제로 쳐 보고 확인했다 (2026-09-10): `~2026-08-31` ❌ / `~2026-08-01` ✅.

    그래서 양쪽 다 **그 달 1일**로 스냅한다. 끝은 진행 중인 이번 달을 빼고
    **마지막으로 끝난 달의 1일**을 쓴다.
    """
    s = dt.date.fromisoformat(start).replace(day=1)
    e = dt.date.fromisoformat(end)
    # 이번 달 1일 - 1일 = 지난달 말일 → 다시 1일로 → 「마지막으로 끝난 달의 1일」
    e = (e.replace(day=1) - dt.timedelta(days=1)).replace(day=1)
    if e < s:
        print("  (수집할 완료된 달이 없다)")
        return []
    print(f"  월 경계로 맞춤: {s} ~ {e}")
    resp = ya.reports().query(
        ids="channel==MINE", startDate=s.isoformat(), endDate=e.isoformat(),
        metrics="estimatedRevenue,estimatedAdRevenue,estimatedRedPartnerRevenue",
        dimensions="month", sort="month",
    ).execute()
    save("revenue", resp)
    return rows_of(resp)


# ─── 노출·CTR 확인 ────────────────────────────────────────────────────────
def probe_impressions(ya, start: str, end: str) -> None:
    """🔴 **확인 대상이지 확정 사실이 아니다.**

    「노출·노출 클릭률은 YouTube Studio 전용이고 Analytics API 에는 없다」고 알려져 있는데,
    그건 들은 이야기다. 직접 쳐 보고 결과를 문서에 적는다.
    안 되면 → **CSV 를 버리면 안 되는 이유**가 확인된 것이다.
    """
    print("\n[노출·CTR 확인] metrics=impressions,impressionClickThroughRate")
    try:
        resp = ya.reports().query(
            ids="channel==MINE", startDate=start, endDate=end,
            metrics="impressions,impressionClickThroughRate",
        ).execute()
        print("  ✅ 응답이 왔다 — API 로도 노출·CTR 을 얻을 수 있다")
        print("  ", json.dumps(resp, ensure_ascii=False)[:400])
        save("probe_impressions_OK", resp)
    except HttpError as e:
        detail = e.content.decode("utf-8", "replace") if e.content else str(e)
        print(f"  ❌ 실패 (HTTP {e.resp.status}) — Studio 전용 지표로 보인다")
        print("  ", detail[:400])
        save("probe_impressions_FAIL", {"status": e.resp.status, "detail": detail})


# ─── 채널 확인 ────────────────────────────────────────────────────────────
def channel_info(yt, allow_any: bool = False) -> dict:
    resp = yt.channels().list(part="snippet,statistics,contentDetails", mine=True).execute()
    items = resp.get("items", [])
    if not items:
        raise SystemExit(
            "내 채널을 못 찾았다.\n"
            "  · 로그인 계정이 seochang2011@gmail.com 인지\n"
            "  · 동의 화면에서 채널을 골랐는지 확인할 것.")
    it = items[0]
    handle = it["snippet"].get("customUrl", "")
    info = {
        "channelId": it["id"],
        "title": it["snippet"]["title"],
        "handle": handle,
        "subscriberCount": it["statistics"].get("subscriberCount"),
        "videoCount": it["statistics"].get("videoCount"),
        "viewCount": it["statistics"].get("viewCount"),
        "uploadsPlaylist": it["contentDetails"]["relatedPlaylists"]["uploads"],
    }
    save("channel", info)

    # 🔴 엉뚱한 채널로 인증됐으면 여기서 멈춘다. 잘못된 채널의 지표로 발표를 만들면
    # 그때는 되돌릴 방법이 없다.
    ok = (handle.lower() == EXPECT_HANDLE.lower()) or (info["title"] == EXPECT_TITLE)
    if not ok and not allow_any:
        raise SystemExit(
            "\n🔴 엉뚱한 채널로 인증됐다.\n"
            f"   받은 채널  : {info['title']} ({handle or '핸들 없음'})\n"
            f"   기대한 채널: {EXPECT_TITLE} ({EXPECT_HANDLE})\n\n"
            "   이 계정에는 채널이 5개 있다. 기본 채널(Wild Forager)로 인증된 것 같다.\n"
            f"   토큰을 지우고 다시 인증하면서 **채널 선택 화면에서 {EXPECT_TITLE} 를 고를 것**:\n"
            f"     Remove-Item {TOKEN}\n"
            "     python scripts/youtube_analytics.py --check\n\n"
            "   (의도한 것이면 --allow-any-channel 을 붙인다)")
    return info


# ─── main ─────────────────────────────────────────────────────────────────
def main() -> None:
    today = dt.date.today()
    ap = argparse.ArgumentParser(description="YouTube 지표 수집기 (M1)")
    ap.add_argument("--start", default="2026-01-01", help="시작일 YYYY-MM-DD")
    ap.add_argument("--end", default=today.isoformat(), help="종료일 YYYY-MM-DD")
    ap.add_argument("--check", action="store_true", help="인증과 채널만 확인")
    ap.add_argument("--probe-impressions", action="store_true", help="노출·CTR 이 API 에 있나 확인")
    ap.add_argument("--daily", action="store_true", help="① 일 단위 시계열")
    ap.add_argument("--videos", action="store_true", help="② 영상별 성과 + 메타데이터")
    ap.add_argument("--traffic", action="store_true", help="③ 유입 경로")
    ap.add_argument("--revenue", action="store_true", help="④ 월 단위 수익 (로컬 전용)")
    ap.add_argument("--all", action="store_true", help="①②③④ 전부")
    ap.add_argument("--allow-any-channel", action="store_true",
                    help="Catch Up AI 가 아닌 채널이어도 진행 (기본은 멈춘다)")
    args = ap.parse_args()

    ya, yt = services()

    info = channel_info(yt, allow_any=args.allow_any_channel)
    print(f"채널   : {info['title']}  {info.get('handle','')}")
    print(f"구독자 : {info['subscriberCount']}   영상 {info['videoCount']}편")
    print(f"기간   : {args.start} ~ {args.end}")
    print(f"토큰   : {TOKEN}")

    if args.check:
        print("\n✅ 인증 확인 완료.")
        return

    if args.probe_impressions:
        probe_impressions(ya, args.start, args.end)
        return

    run_all = args.all or not (args.daily or args.videos or args.traffic or args.revenue)

    if args.daily or run_all:
        rows = daily(ya, args.start, args.end)
        wk = weekly_from_daily(rows)
        save("weekly", wk)
        print(f"\n① 일 단위 {len(rows)}일 · 주 단위 {len(wk)}주")
        neg = [w for w in wk if w["net"] < 0]
        print(f"   순증이 마이너스인 주: {len(neg)}주")
        for w in wk[-8:]:
            print(f"   {w['week']}  net {w['net']:+5d}  (가입 {w['subscribersGained']}, 해지 {w['subscribersLost']})")

    if args.videos or run_all:
        vids = videos(ya, args.start, args.end)
        ids = [v["video"] for v in vids]
        meta = video_meta(yt, ids)
        merged = [{**v, **meta.get(v["video"], {})} for v in vids]
        save("videos_merged", merged)
        print(f"\n② 영상 {len(merged)}편")
        for v in merged[:5]:
            print(f"   {v.get('publishedAt','?')[:10]}  조회 {v.get('views',0):>6}  "
                  f"구독 +{v.get('subscribersGained',0):<4} {str(v.get('title',''))[:40]}")

    if args.traffic or run_all:
        tr = traffic(ya, args.start, args.end)
        print(f"\n③ 유입 경로 {len(tr)}종")
        for t in tr[:8]:
            print(f"   {t.get('insightTrafficSourceType','?'):<24} 조회 {t.get('views',0)}")

    if args.revenue or run_all:
        rv = revenue(ya, args.start, args.end)
        print(f"\n④ 수익 {len(rv)}개월  🔒 로컬 전용 — data/ 는 깃에서 제외돼 있다")
        for r in rv[-6:]:
            print(f"   {r.get('month','?')}  추정수익 {r.get('estimatedRevenue', 0)}")

    print(f"\n원본 JSON → {RAW}")


if __name__ == "__main__":
    main()
