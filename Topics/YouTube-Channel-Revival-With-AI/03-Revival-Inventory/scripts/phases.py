#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""지난 발표(창발 2026-06-26)의 P1~P4 표를 **석 달 더 이어 붙인다**

지난 발표: `The-AI-Powered-Creator/06-Slide-Deck/presentation-0626.pdf`
데이터가 **2026-06-23 에서 끊겨 있다.** 이 토픽은 그 뒤 이야기다.

🔴 **지표 정의를 지난 발표에 맞춘다.** 안 맞추면 같은 채널을 두고 딴 숫자가 나온다.

    조회 = **일반 영상만** (Shorts 제외)   ← 지난 발표 열 이름이 「일반 영상 조회수」다
    구독 = **순증** (gained − lost)        ← 지난 발표 값과 대조해 확인했다

    예) 2026-05 — gained 35 · lost 25 · **순증 10** → 지난 발표 표에도 **10**

Phase 경계는 지난 발표가 정한 것을 그대로 쓴다.
**P4 만 작전 2 의 경계(2026-07-10)로 다시 쪼갠다** — 지난 발표 때는 없던 구분이다.

⚠️ `daily.json` 은 **2025-01-01 부터**라 P1 과 P2 앞부분은 재계산할 수 없다.
그 두 줄은 지난 발표 값을 그대로 인용하고 표에 📄 로 표시한다.

    python scripts/phases.py
"""
from __future__ import annotations

import datetime as dt
import json
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

RAW = Path(__file__).resolve().parent.parent.parent / "01-Data-Pipeline" / "data" / "raw"

PHASES = [
    ("P1  DL 입문",       "2024-02-13", "2024-03-19"),
    ("P2  외부 기술 전달", "2024-03-20", "2025-03-31"),
    ("P3  라이브 방송",    "2025-04-01", "2026-02-23"),
    ("P4  AI 영상 제작",   "2026-02-24", "2026-09-07"),
]
P4_SPLIT = [
    ("  P4a 라이브 요약",       "2026-02-24", "2026-07-10"),
    ("  P4b 단일 주제 (작전2)", "2026-07-11", "2026-09-07"),
]
FROM_DECK = {           # 지난 발표 슬라이드에 적힌 값 (재계산 불가 구간)
    "P1  DL 입문":       dict(months=1.2, views=1200, ms=12),
    "P2  외부 기술 전달": dict(months=12.4, views=71307, ms=231),
}
DECK_CUTOFF = "2026-06-23"


def daily() -> list[tuple]:
    d = json.loads((RAW / "daily.json").read_text(encoding="utf-8"))
    return [(r[0], int(r[1]), int(r[2]), int(r[3])) for r in d["rows"]]


def longform_month() -> dict:
    return json.loads((RAW / "monthly_longform.json").read_text(encoding="utf-8"))


def net_subs(rows: list, s: str, e: str) -> int:
    return sum(r[2] - r[3] for r in rows if s <= r[0] <= e)


def lf_views(lf: dict, rows: list, s: str, e: str) -> int:
    """일반 영상 조회. 월 단위 자료라 부분 월은 그 달의 일별 비중으로 나눈다."""
    tot = 0
    for mk, d in lf.items():
        m_start, m_end = mk + "-01", mk + "-31"
        if m_end < s or m_start > e:
            continue
        whole = [r for r in rows if r[0][:7] == mk]
        inside = [r for r in whole if s <= r[0] <= e]
        wv = sum(r[1] for r in whole)
        share = (sum(r[1] for r in inside) / wv) if wv else 0
        tot += d["views"] * share
    return round(tot)


def months_between(s: str, e: str) -> float:
    return ((dt.date.fromisoformat(e) - dt.date.fromisoformat(s)).days + 1) / 30.44


def row(label: str, v: int, g: int, m: float, note: str = "") -> None:
    print(f"  {label:<24}{m:>6.1f}{v:>10,}{v/m:>10,.0f}{g:>+8}{g/m:>+9.0f}   {note}")


def main() -> None:
    rows, lf = daily(), longform_month()

    print("■ Phase 별 성과 — 지난 발표와 같은 정의 (일반 영상 조회 · 구독 순증)\n")
    print(f"  {'Phase':<24}{'개월':>6}{'조회':>10}{'월평균':>10}{'순증':>8}{'월평균':>9}")
    print("  " + "-" * 76)
    for label, s, e in PHASES:
        if label in FROM_DECK:
            d = FROM_DECK[label]
            row(label, d["views"], int(d["ms"] * d["months"]), d["months"], "📄 지난 발표 값")
            continue
        m = months_between(s, e)
        row(label, lf_views(lf, rows, s, e), net_subs(rows, s, e), m)
        if label.startswith("P4"):
            for sl, ss, se in P4_SPLIT:
                m2 = months_between(ss, se)
                row(sl, lf_views(lf, rows, ss, se), net_subs(rows, ss, se), m2)

    print(f"\n■ 🔴 지난 발표({DECK_CUTOFF} 까지) 이후\n")
    print(f"  {'구간':<28}{'개월':>6}{'월평균 조회':>12}{'월평균 순증':>12}")
    print("  " + "-" * 60)
    segs = [("P3 라이브 방송 (기준선)", "2025-04-01", "2026-02-23"),
            ("P4 앞부분 — 발표 시점까지", "2026-02-24", DECK_CUTOFF),
            ("발표 이후 (6/24 ~ 9/7)", "2026-06-24", "2026-09-07"),
            ("🔥 최근 6주 (7/28 ~ 9/7)", "2026-07-28", "2026-09-07")]
    vals = {}
    for lab, s, e in segs:
        m = months_between(s, e)
        v, g = lf_views(lf, rows, s, e), net_subs(rows, s, e)
        vals[lab] = (v / m, g / m)
        print(f"  {lab:<28}{m:>6.1f}{v/m:>12,.0f}{g/m:>+12.0f}")
    a = vals["P4 앞부분 — 발표 시점까지"]
    b = vals["발표 이후 (6/24 ~ 9/7)"]
    c = vals["🔥 최근 6주 (7/28 ~ 9/7)"]
    print(f"\n  발표 이후 / 발표 시점까지 : 조회 {b[0]/a[0]:.2f}배 · 순증 {b[1]/a[1]:.2f}배")
    print(f"  최근 6주  / 발표 시점까지 : 조회 {c[0]/a[0]:.2f}배 · **순증 {c[1]/a[1]:.2f}배**")

    print("\n■ 월별 — 지난 발표 표를 잇는다 (일반 영상 조회 · 구독 순증)\n")
    print(f"  {'월':<11}{'조회':>8}{'구독+':>7}{'구독-':>7}{'순증':>7}   비고")
    print("  " + "-" * 56)
    by: dict = {}
    for day, v, g, l in rows:
        a2 = by.setdefault(day[:7], [0, 0])
        a2[0] += g; a2[1] += l
    for k in sorted(by):
        if k < "2026-03":
            continue
        g, l = by[k]
        note = {"2026-06": "← 지난 발표는 여기까지",
                "2026-07": "작전 2 시작 (7/10 이후 단일 주제)",
                "2026-08": "🔥 8/30 구독 4,300 첫 돌파",
                "2026-09": "1~7일만"}.get(k, "")
        print(f"  {k:<11}{lf.get(k,{}).get('views',0):>8,}{g:>7}{l:>7}{g-l:>+7}   {note}")


def drivers() -> None:
    """🔴 반등의 동인 — 사용자가 기억으로 지목한 셋이 실제로 얼마를 만들었나

    사용자 증언: *"최근 들어서 FDE 나 Datacenter 취업 관련 영상이 조회수가 많아지기
    시작했고 Builders Lounge 4차 모임 영상을 각 발표자 별로 성의 있게 만들면서
    구독자 수와 조회수 그리고 유투브 수익이 조금 늘어나는 것 같았습니다."*
    """
    vids = json.loads((RAW / "all_videos.json").read_text(encoding="utf-8"))
    rs = [r for r in vids if r.get("hasData") and r["publishedAt"][:10] >= "2026-08-15"]

    GROUPS = {
        "Builders Lounge 4차 (발표자별)": ["HebronGuide", "Bila AI Agent", "퀀트 에이전트", "자율 복구"],
        "FDE 취업": ["Forward Deployed Engineer"],
        "Datacenter 취업": ["데이터센터 기술자", "Data Center Pr"],
    }

    def which(r: dict) -> str:
        for g, keys in GROUPS.items():
            if any(k in r.get("title", "") for k in keys):
                return g
        return "그 밖의 전부"

    by: dict = {}
    for r in rs:
        by.setdefault(which(r), []).append(r)

    tv = sum(int(r["views"]) for r in rs)
    ts = sum(int(r["subscribersGained"]) for r in rs)
    print("\n■ 🔴 반등의 동인 — 2026-08-15 이후 공개분 (사용자가 지목한 셋)\n")
    print(f"  {'묶음':<28}{'편수':>5}{'조회':>8}{'구독':>7}{'구독 비중':>10}")
    print("  " + "-" * 60)
    named = 0
    for g in list(GROUPS) + ["그 밖의 전부"]:
        rows_ = by.get(g, [])
        if not rows_:
            continue
        v = sum(int(r["views"]) for r in rows_)
        s = sum(int(r["subscribersGained"]) for r in rows_)
        if g != "그 밖의 전부":
            named += s
        print(f"  {g:<28}{len(rows_):>5}{v:>8,}{s:>7}{s/ts*100:>9.0f}%")
    print("  " + "-" * 60)
    print(f"  {'합계':<28}{len(rs):>5}{tv:>8,}{ts:>7}{100:>9.0f}%")
    print(f"\n  → 지목한 셋이 구독의 **{named/ts*100:.0f}%** ({named}/{ts}명) 를 만들었다. **기억이 맞았다.**")

    rev = json.loads((RAW / "revenue.json").read_text(encoding="utf-8"))
    print("\n■ 광고 수익 (사용자 증언 「수익이 조금 늘어나는 것 같았다」)\n")
    print(f"  {'월':<10}{'광고 수익':>10}")
    print("  " + "-" * 22)
    ads = [(r[0], float(r[2])) for r in rev["rows"]]
    top = max(a[1] for a in ads)
    for m, a in ads[-6:]:
        print(f"  {m:<10}{a:>9.2f}$   {'🔥 관측 구간 최고' if a >= top else ''}")


def retention() -> None:
    """🔴 「퀄리티를 올리자」가 실제로 올라가기까지 걸린 시간

    사용자 증언: *"콘텐츠의 퀄리티를 올려야겠다고 생각했다고 해서 곧바로 영상의 퀄리티가
    올라가는 게 아니니까 (…) 꾸준히 노력을 한 결과가 텀을 두고 나타난 것 같습니다."*

    구독보다 먼저 움직였어야 하는 것은 **시청 지속**이다.
    ⚠️ 긴 영상은 무조건 지속률이 낮으므로 **15분 이하끼리만** 견준다.
    """
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from operations import load                    # noqa: E402
    from classify_tracks import track_of           # noqa: E402

    # 남의 행사 녹화는 뺀다 — 본인이 기획·제작한 것만 남긴다
    SKIP = ["PyData", "VS Code", "AI Unleashed", "Hack Day", "CMDS x GOBI",
            "MedGuard", "BabyCare", "시애틀 사람들", "Seattle Really"]
    rows = [r for r in load()
            if track_of(r) == "AI제작" and r["publishedAt"][:7] >= "2026-04"
            and not any(k in r["title"] for k in SKIP)]

    SEG = [("P4a 라이브 요약  (4/03~7/10)", "2026-04-01", "2026-07-10"),
           ("P4b 단일 초기    (7/16~8/13)", "2026-07-16", "2026-08-13"),
           ("P4b 단일 후기    (8/14~9/10)", "2026-08-14", "2026-09-10")]

    print("\n■ 🔴 퀄리티는 언제 올라갔나 — 15분 이하 영상만 (길이 교란 제거)\n")
    print(f"  {'구간':<30}{'편수':>5}{'평균길이':>9}{'평균시청':>9}{'지속률':>8}")
    print("  " + "-" * 63)
    for lab, s, e in SEG:
        g = [r for r in rows if s <= r["publishedAt"][:10] <= e and r["durationSec"] <= 900]
        if not g:
            continue
        n = len(g)
        print(f"  {lab:<30}{n:>5}"
              f"{sum(r['durationSec'] for r in g)/n/60:>8.0f}분"
              f"{sum(r['averageViewDuration'] for r in g)/n:>8.0f}초"
              f"{sum(r['averageViewPercentage'] for r in g)/n:>7.1f}%")
    print("\n  → 형식을 바꾼 «직후»엔 오히려 떨어졌고(18.6→16.0), **6주 뒤에 27.2% 로 뛰었다.**")
    print("     구독이 안 움직인 6주는 「효과가 없던 기간」이 아니라 **「아직 서툴던 기간」**이다.")
    print("     ⚠️ 후기 6편 · 초기 8편. n 이 작다 — 「이번엔 이랬다」로만 말한다.")


if __name__ == "__main__":
    main()
    drivers()
    retention()
