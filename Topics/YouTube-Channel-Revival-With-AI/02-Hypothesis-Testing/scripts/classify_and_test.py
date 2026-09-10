#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""가설 검증 — YouTube Studio CSV 를 그룹으로 나눠 비교한다 (M2)

    python scripts/classify_and_test.py

입력: `01-Data-Pipeline/data/youtube-analytics/content-*/Table data.csv`
      (Studio 고급 모드 → Content → CSV export)

**판정 기준을 데이터를 보기 전에 정해 둔다** — 아래 THRESHOLD 상수가 그것이다.
숫자를 보고 기준을 맞추면 검증이 아니라 사후 해석이 된다.

⚠️ **구독자 수치의 한계** — Studio 의 `Subscribers` 열도 Analytics API 와 같이
「그 영상의 시청 페이지에서 구독을 누른 횟수」다. **기여의 하한선**으로만 읽는다.
"""
from __future__ import annotations

import csv
import io
import re
import statistics as st
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

HERE = Path(__file__).resolve().parent.parent            # 02-Hypothesis-Testing/
DATA = HERE.parent / "01-Data-Pipeline" / "data" / "youtube-analytics"

# ─── 데이터를 보기 전에 정한 판정 기준 ────────────────────────────────────
#
# 「구독 전환율」= 조회 1,000회당 시청 페이지 구독 수. 조회수가 다른 그룹을
# 공평하게 비교하려면 절대 구독 수가 아니라 전환율로 봐야 한다.
RATIO_STRONG = 2.0     # 전환율이 2배 이상 차이 → 「맞다」
RATIO_WEAK = 1.3       # 1.3배 미만 → 「차이 없다」
MIN_N = 5              # 표본이 이보다 작으면 판정하지 않고 「알 수 없다」

SHORTS_MAX_SEC = 180   # YouTube Shorts 기준 (2026 현재 최대 3분)
SPLIT_MAX_SEC = 30 * 60  # 「분할 편집」 목표였던 편당 30분


def load() -> list[dict]:
    cands = sorted(DATA.glob("content-*/Table data.csv"))
    if not cands:
        raise SystemExit(f"CSV 를 못 찾았다: {DATA}/content-*/Table data.csv")
    path = cands[-1]
    print(f"입력: {path.relative_to(HERE.parent)}\n")
    out = []
    with io.open(path, encoding="utf-8-sig", newline="") as f:
        for r in csv.DictReader(f):
            if r.get("Content") in (None, "", "Total"):
                continue
            try:
                r["_views"] = int(r["Views"] or 0)
                r["_subs"] = int(r["Subscribers"] or 0)
                r["_dur"] = int(r["Duration"] or 0)
                r["_imp"] = int(r["Thumbnail impressions"] or 0)
                r["_ctr"] = float(r["Thumbnail click-through rate (%)"] or 0)
            except (TypeError, ValueError):
                continue                     # 값이 비어 있는 행은 버린다
            r["_title"] = r.get("Video title") or ""
            r["_pub"] = r.get("Video publish time") or ""
            out.append(r)
    return out


def conv(rows: list[dict]) -> float:
    """조회 1,000회당 시청 페이지 구독 수."""
    v = sum(r["_views"] for r in rows)
    return (sum(r["_subs"] for r in rows) / v * 1000) if v else 0.0


def describe(name: str, rows: list[dict]) -> dict:
    v = sum(r["_views"] for r in rows)
    s = sum(r["_subs"] for r in rows)
    ctrs = [r["_ctr"] for r in rows if r["_imp"] > 0]
    return {
        "name": name, "n": len(rows), "views": v, "subs": s,
        "conv": conv(rows),
        "med_views": st.median([r["_views"] for r in rows]) if rows else 0,
        "ctr": st.median(ctrs) if ctrs else 0.0,
    }


def show(rows_desc: list[dict]) -> None:
    print(f"  {'그룹':<26}{'편수':>5}{'조회':>10}{'구독':>7}"
          f"{'1천뷰당구독':>12}{'CTR중앙':>9}")
    for d in rows_desc:
        print(f"  {d['name']:<26}{d['n']:>5}{d['views']:>10,}{d['subs']:>7}"
              f"{d['conv']:>12.2f}{d['ctr']:>8.1f}%")


def verdict(a: dict, b: dict) -> str:
    """a 가 b 보다 나은가. 판정 기준은 위에서 미리 정해 뒀다."""
    if a["n"] < MIN_N or b["n"] < MIN_N:
        return f"⏳ 알 수 없다 — 표본이 작다 (n={a['n']} vs {b['n']}, 기준 {MIN_N})"
    if b["conv"] == 0:
        return "⏳ 알 수 없다 — 비교군의 전환율이 0"
    ratio = a["conv"] / b["conv"]
    if ratio >= RATIO_STRONG:
        return f"✅ 맞다 — 전환율 {ratio:.1f}배"
    if ratio <= 1 / RATIO_STRONG:
        return f"❌ 반대다 — 오히려 {1/ratio:.1f}배 낮다"
    if RATIO_WEAK > ratio > 1 / RATIO_WEAK:
        return f"➖ 차이 없다 — {ratio:.2f}배 (기준 {RATIO_WEAK}배 미만)"
    return f"🔶 약한 차이 — {ratio:.2f}배 (2배 기준에는 못 미친다)"


# ─── 분류 ─────────────────────────────────────────────────────────────────
def is_short(r) -> bool:
    return 0 < r["_dur"] <= SHORTS_MAX_SEC


def has_engsub(r) -> bool:
    return "ENG SUB" in r["_title"].upper()


def is_live_archive(r) -> bool:
    """라이브 방송 아카이브. 제목 규칙이 「AI in Action」 계열이다."""
    t = r["_title"]
    return ("AI in Action" in t) or bool(re.search(r"Live\s*#?\d", t))


def main() -> None:
    rows = load()
    longform = [r for r in rows if not is_short(r)]
    shorts = [r for r in rows if is_short(r)]

    print(f"전체 {len(rows)}편 · 롱폼 {len(longform)} · Shorts {len(shorts)}\n")

    # ── 가설 0 (M1 에서 새로 나온 것): Shorts 는 구독으로 이어지는가
    print("■ 가설 0 — Shorts 는 조회는 되는데 구독으로 이어지는가")
    a, b = describe("Shorts (≤3분)", shorts), describe("롱폼", longform)
    show([a, b])
    print(f"  → {verdict(a, b)}")
    print("  ⭐ M1 에서 «최대 유입원인데 몇 달째 손대지 않았다» 로 나온 그 항목이다\n")

    # ── 가설 1: 자막
    print("■ 가설 1 — 자막(ENG SUB)을 단 영상이 구독 전환이 나은가")
    sub_yes = [r for r in longform if has_engsub(r)]
    sub_no = [r for r in longform if not has_engsub(r)]
    a, b = describe("[ENG SUB] 있음", sub_yes), describe("없음", sub_no)
    show([a, b])
    print(f"  → {verdict(a, b)}")
    print("  ⚠️ 제목에 표기된 것만 센다. 표기 없이 자막만 올린 영상은 여기 안 잡힌다\n")

    # ── 가설 2: 사람이 나오는 영상 (오프라인 발표) vs 라이브 아카이브
    print("■ 가설 2 — 사람이 나오는 발표 영상 vs 라이브 방송 아카이브")
    live = [r for r in longform if is_live_archive(r)]
    notlive = [r for r in longform if not is_live_archive(r)]
    a, b = describe("발표·제작 영상", notlive), describe("라이브 아카이브", live)
    show([a, b])
    print(f"  → {verdict(a, b)}")
    print("  ⚠️ 「사람 등장」의 대리 지표다. 정확히는 M3 인벤토리에서 눈으로 분류해야 한다\n")

    # ── 가설 3: 분할 편집 (30분 이내)
    print("■ 가설 3 — 30분 이내로 자른 영상이 나은가")
    short_cut = [r for r in longform if r["_dur"] <= SPLIT_MAX_SEC]
    long_cut = [r for r in longform if r["_dur"] > SPLIT_MAX_SEC]
    a, b = describe("30분 이내", short_cut), describe("30분 초과", long_cut)
    show([a, b])
    print(f"  → {verdict(a, b)}\n")

    # ── 회복기(2026-08 이후) 롱폼만
    print("■ 참고 — 회복기(2026-08 이후) 공개 롱폼")
    rec = [r for r in longform if _pubkey(r) >= "2026-08"]
    if rec:
        show([describe("2026-08 이후 롱폼", rec)])
    print()

    # ── CTR 상·하위
    print("■ 썸네일 클릭률 — 노출 1만 이상인 영상만")
    big = sorted([r for r in rows if r["_imp"] >= 10000], key=lambda r: -r["_ctr"])
    for r in big[:5]:
        print(f"  {r['_ctr']:>5.1f}%  노출 {r['_imp']:>8,}  {r['_title'][:44]}")
    print("  ...")
    for r in big[-3:]:
        print(f"  {r['_ctr']:>5.1f}%  노출 {r['_imp']:>8,}  {r['_title'][:44]}")


def _pubkey(r) -> str:
    """'Aug 22, 2026' → '2026-08' 로 정렬 가능한 키."""
    m = re.match(r"([A-Za-z]{3}) \d+, (\d{4})", r["_pub"])
    if not m:
        return ""
    mon = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
           "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"].index(m.group(1)) + 1
    return f"{m.group(2)}-{mon:02d}"


if __name__ == "__main__":
    main()
