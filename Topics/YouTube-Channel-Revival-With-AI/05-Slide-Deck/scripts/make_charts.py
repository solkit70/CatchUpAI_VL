"""M5 실습 1 — 발표용 그래프 3장.

① 구독자 추이 (2026-02 ~ 09-07) — 횡보 구간 · 첫 마이너스 주 · 전고점 돌파
② 주별 순증 막대 — 작전 1(자막) · 작전 2(단일 주제, 7/19) · 전환점 8/24 주
③ 시청 지속률 — 15분 이하 영상만 · P4a 18.6% → P4b 초기 16.0% → 후기 27.2%

데이터: 01-Data-Pipeline/data/raw/daily.json (일별 gained/lost). 절대값은 2026-09-07 = 4,320 (M1 검증값) — 그 뒤는 순증을 더해 9/13 까지 잇는다
(9/15 갱신. Data API 현재값 4,330 과 Analytics 누적 4,323 의 차이 7 은 9/14~15 미확정분 + 집계 시차)
(phase5-growth-analysis.md 의 역산 기준)에서 거꾸로 뺀다 — M1 과 같은 방식.
지속률 숫자는 03-Revival-Inventory/analysis/phases-continued.md 의 표를 그대로 옮긴다
(여기서 재계산하지 않는다 — 한 출처).

실행:  python make_charts.py   → ../images/chart-1-subscribers.png 등 3장
"""
from __future__ import annotations

import json
from datetime import date, timedelta
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager

HERE = Path(__file__).resolve().parent
TOPIC = HERE.parent.parent
RAW = TOPIC / "01-Data-Pipeline" / "data" / "raw"
OUT = HERE.parent / "images"
OUT.mkdir(exist_ok=True)

# ── 덱 팔레트 (presentation-0626.md 와 같은 계열) ──────────────────────
BG, FG, GREEN, AMBER, BLUE, RED, MUTE = "#1d3a6e", "#e8f0fe", "#22C55E", "#F59E0B", "#60A5FA", "#F87171", "#9fb3d9"
ANCHOR_DATE, ANCHOR_SUBS = date(2026, 9, 7), 4320     # 역산 기준 (M1 검증값 — 바꾸지 않는다)
LAST_DATE = date(2026, 9, 13)                          # Analytics 확정 마지막 날 (9/15 갱신)
NOW_DATE, NOW_SUBS = date(2026, 9, 15), 4330            # Data API 현재값 (채널 화면 숫자) — 점 하나로 표시
FLAT_START, FLAT_END = date(2026, 3, 25), date(2026, 8, 23)   # P5a 횡보
FIRST_NEG_WEEK = date(2026, 3, 25)
OP1 = date(2026, 7, 14)     # 작전 1 (자막) — 첫 자막 세미나 영상 공개일 (9/15 정정: 4/3 은 오기)
OP2 = date(2026, 7, 19)     # 작전 2 단일 주제 첫 편 (자막 자동 생성기, uvR--_klsMg) — 마지막 요약본은 7/10
TURN = date(2026, 8, 24)    # 전환점 주 (phases-continued)
BREAK = date(2026, 8, 30)   # 역산상 전고점 돌파 (4,306)

for cand in ["Malgun Gothic", "NanumGothic", "Noto Sans KR", "Noto Sans CJK KR"]:
    if any(f.name == cand for f in font_manager.fontManager.ttflist):
        plt.rcParams["font.family"] = cand
        break
plt.rcParams["axes.unicode_minus"] = False
plt.rcParams.update({"figure.facecolor": BG, "axes.facecolor": BG, "savefig.facecolor": BG,
                     "text.color": FG, "axes.labelcolor": FG, "xtick.color": FG, "ytick.color": FG,
                     "axes.edgecolor": MUTE, "font.size": 18})


def daily() -> list[tuple[date, int, int]]:
    d = json.loads((RAW / "daily.json").read_text(encoding="utf-8"))
    return [(date.fromisoformat(r[0]), int(r[2]), int(r[3])) for r in d["rows"]]


def subscribers_series(rows) -> list[tuple[date, int]]:
    """앵커에서 거꾸로 빼서 일별 구독자 수를 만든다 (앵커일 포함 이후는 순증 더하기)."""
    net = {d: g - l for d, g, l in rows}
    days = sorted(net)
    out: dict[date, int] = {ANCHOR_DATE: ANCHOR_SUBS}
    cur = ANCHOR_SUBS
    for d in reversed([x for x in days if x < ANCHOR_DATE]):
        nxt = d + timedelta(days=1)
        cur -= net.get(nxt, 0)          # d 의 값 = (d+1) 값 - (d+1) 순증
        out[d] = cur
    cur = ANCHOR_SUBS
    for d in [x for x in days if ANCHOR_DATE < x <= LAST_DATE]:   # 앵커 뒤는 순증을 더해 잇는다
        cur += net.get(d, 0)
        out[d] = cur
    return sorted(out.items())


def weekly_net(rows, start: date, end: date) -> list[tuple[date, int]]:
    net = {d: g - l for d, g, l in rows}
    out = []
    w = start
    while w <= end:
        out.append((w, sum(net.get(w + timedelta(days=i), 0) for i in range(7))))
        w += timedelta(days=7)
    return out


def chart_subscribers(rows):
    series = [(d, v) for d, v in subscribers_series(rows) if d >= date(2026, 2, 1)]
    xs, ys = zip(*series)
    fig, ax = plt.subplots(figsize=(16, 8), dpi=110)
    ax.axvspan(FLAT_START, FLAT_END, color=AMBER, alpha=0.16, lw=0)
    ax.plot(xs, ys, color=BLUE, lw=3.5)
    ax.axhline(4300, color=MUTE, ls="--", lw=1.5)
    ax.text(date(2026, 2, 3), 4302, "4,300", color=MUTE, fontsize=15, va="bottom")
    ax.annotate("횡보 5개월\n4,264 ~ 4,295", xy=(date(2026, 6, 5), 4270), fontsize=20, color=AMBER, ha="center", va="top")
    ax.annotate("첫 마이너스 주\n3/25", xy=(FIRST_NEG_WEEK, dict(series)[FIRST_NEG_WEEK]), xytext=(date(2026, 3, 1), 4230),
                fontsize=16, color=RED, arrowprops=dict(arrowstyle="->", color=RED, lw=2))
    ax.annotate("전고점 돌파\n8/30 · 4,306", xy=(BREAK, dict(series)[BREAK]), xytext=(date(2026, 6, 28), 4340),
                fontsize=18, color=GREEN, arrowprops=dict(arrowstyle="->", color=GREEN, lw=2))
    ax.annotate(f"9/13 · {dict(series)[LAST_DATE]:,}", xy=(LAST_DATE, dict(series)[LAST_DATE]), xytext=(date(2026, 8, 12), 4200),
                fontsize=16, color=FG, arrowprops=dict(arrowstyle="->", color=FG, lw=1.5))
    # 오늘 — Data API 현재값. Analytics 누적선과 별개라 점선으로 잇고 점으로 찍는다
    ax.plot([LAST_DATE, NOW_DATE], [dict(series)[LAST_DATE], NOW_SUBS], color=GREEN, ls=":", lw=2.5)
    ax.scatter([NOW_DATE], [NOW_SUBS], color=GREEN, s=140, zorder=5)
    ax.annotate(f"오늘 9/15 · {NOW_SUBS:,}", xy=(NOW_DATE, NOW_SUBS), xytext=(date(2026, 8, 26), 4348),
                fontsize=19, color=GREEN, fontweight="bold", arrowprops=dict(arrowstyle="->", color=GREEN, lw=2))
    ax.set_ylim(4150, 4360)
    ax.set_title("구독자 수 — 2026년 2월 ~ 9월 15일", fontsize=24, color=FG, pad=16)
    ax.grid(axis="y", color=MUTE, alpha=0.25)
    for s in ("top", "right"): ax.spines[s].set_visible(False)
    fig.text(0.99, 0.01, "YouTube Analytics API · 일별 가입/해지 · 9/7 = 4,320 기준 역산 · 9/13 까지 — 9/15 는 채널 현재값(Data API)", ha="right", fontsize=12, color=MUTE)
    fig.tight_layout()
    fig.savefig(OUT / "chart-1-subscribers.png")
    plt.close(fig)
    return dict(series)


def chart_weekly_net(rows):
    weeks = weekly_net(rows, date(2026, 3, 2), date(2026, 9, 8))   # 마지막 주(9/8~)는 9/13 까지 6일치
    xs = [w for w, _ in weeks]
    ys = [v for _, v in weeks]
    colors = [GREEN if v > 0 else RED for v in ys]
    fig, ax = plt.subplots(figsize=(16, 8), dpi=110)
    ax.bar(xs, ys, width=6, color=colors, alpha=0.9)
    ax.axhline(0, color=MUTE, lw=1)
    for x, label, col in ((OP1, "작전 1·2 · 7/14·19\n자막 + 단일 주제로 전환", AMBER), (TURN, "전환점 · 8/24 주", GREEN)):
        ax.axvline(x, color=col, ls="--", lw=2)
        ax.text(x + timedelta(days=1.5), max(ys) * 0.95, label, color=col, fontsize=17, va="top")
    ax.set_title("주별 순증 구독자 — 작전 시작 후 6주 0, 그다음 2주 급등 (마지막 주는 9/13 까지 6일)", fontsize=24, color=FG, pad=16)
    ax.text(xs[-1], ys[-1] + 0.6, "9/7~13 (6일)", color=MUTE, fontsize=13, ha="center", va="bottom")
    ax.grid(axis="y", color=MUTE, alpha=0.25)
    for s in ("top", "right"): ax.spines[s].set_visible(False)
    fig.text(0.99, 0.01, "YouTube Analytics API · 주 단위 gained - lost", ha="right", fontsize=12, color=MUTE)
    fig.tight_layout()
    fig.savefig(OUT / "chart-2-weekly-net.png")
    plt.close(fig)
    return weeks


def chart_retention():
    labels = ["P4a 라이브 요약\n4/03 ~ 7/10 · 25편", "P4b 단일 주제 초기\n7/19 ~ 8/13 · 8편", "P4b 단일 주제 후기\n8/14 ~ 9/10 · 6편"]
    vals = [18.6, 16.0, 27.2]
    secs = [107, 92, 136]
    cols = [MUTE, RED, GREEN]
    fig, ax = plt.subplots(figsize=(16, 8), dpi=110)
    bars = ax.bar(labels, vals, color=cols, width=0.55)
    for b, v, s in zip(bars, vals, secs):
        ax.text(b.get_x() + b.get_width() / 2, v + 0.6, f"{v:.1f}%\n평균 {s}초", ha="center", fontsize=22, color=FG, fontweight="bold")
    ax.set_ylim(0, 33)
    ax.set_ylabel("평균 시청 지속률 (%)", fontsize=16)
    ax.set_title("시청 지속률 — 15분 이하 영상만 (길이 교란 제거)", fontsize=24, color=FG, pad=16)
    ax.annotate("", xy=(2, 27.2), xytext=(1, 16.0), arrowprops=dict(arrowstyle="->", color=GREEN, lw=3))
    ax.text(1.5, 23.5, "6주 뒤 +11.2%p", color=GREEN, fontsize=20, ha="center", fontweight="bold")
    ax.grid(axis="y", color=MUTE, alpha=0.25)
    for s in ("top", "right"): ax.spines[s].set_visible(False)
    fig.text(0.99, 0.01, "출처: 03-Revival-Inventory/analysis/phases-continued.md (재계산 없음)", ha="right", fontsize=12, color=MUTE)
    fig.tight_layout()
    fig.savefig(OUT / "chart-3-retention.png")
    plt.close(fig)


def main():
    rows = daily()
    series = chart_subscribers(rows)
    weeks = chart_weekly_net(rows)
    chart_retention()
    lo = min(v for d, v in series.items() if FLAT_START <= d <= FLAT_END)
    hi = max(v for d, v in series.items() if FLAT_START <= d <= FLAT_END)
    print(f"횡보 구간 최저 {lo:,} · 최고 {hi:,} | 8/30 {series[BREAK]:,} | 8/24 {series[TURN]:,} | 9/13 {series[LAST_DATE]:,}")
    print("주별 순증 (7/13~):", [(w.isoformat()[5:], v) for w, v in weeks if w >= date(2026, 7, 13)])
    print("→", OUT)


if __name__ == "__main__":
    main()
