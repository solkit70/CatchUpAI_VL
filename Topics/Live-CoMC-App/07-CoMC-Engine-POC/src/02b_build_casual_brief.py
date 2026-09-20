#!/usr/bin/env python3
"""CVL 4 ②-b — 주간 맥락 + 날씨 → casual_brief.{live}.json (캐주얼 레인의 근거 풀).

## 왜 따로 만드나

②(`02_resolve_context.py`)가 만드는 broadcast_context 는 **오늘 방송 내용**(A 등급)의 근거다.
그것만으로는 「이번 주 뭐 했어요?」「시애틀 날씨 어때요?」「잠깐 물 마실게요, 얘기 좀 해 주세요」에
답할 수 없다 — 근거가 없으니 침묵하는 것이 맞고, 실제로 침묵했다 (9/17 실사용).

M1 원칙 「근거 없으면 말하지 않는다」를 버리지 않고 **근거의 종류를 넓힌다.**
이 파일은 방송 전에 한 번 만들어 두는 두 번째 근거 풀이다. ④ 는 캐주얼 의도일 때 이 풀만 보고,
⑤ 는 이 풀에 대해 같은 인용 검사를 한다. 틀린 말을 막는 층은 그대로다.

| 등급 | 출처 | kind |
|---|---|---|
| B 주간 맥락 | Weekly Progress and Planning 「Weekly Summary」 | recap |
| B | 이번 주 Daily Roundup 「Summary」·「Today's Work」 제목 | recap |
| B | 이번 주 Daily Roundup 「Interpretation」 제목 | insight |
| B | Journal 「Thoughts」 구술 원문 | insight (사용자 말 그대로) |
| B | 지난 회차 Rundown 「방송 후 기록」 | last_live |
| B | 오늘 Rundown 「코엠씨 잡담 소재」 섹션 (있으면) | filler |
| C 외부 사실 | Open-Meteo 현재 날씨 — 서울 · 시애틀 (무료 · 키 없음) | weather |

## 지키는 것

- **개인정보는 넣지 않는다** — 이메일·전화번호 패턴은 지우고, 인용은 200자로 자른다.
- 출력은 `output/private/` 에 둔다 — 공개 레포에 올라가지 않는 폴더다 (.gitignore). 주간 기록에는
  사람 이름과 일정이 있다.
- 날씨 조회 실패는 실패로 남긴다 — 어제 값을 오늘 것처럼 말하지 않는다.

실행:
    python 02b_build_casual_brief.py --live 28
    python 02b_build_casual_brief.py --live 28 --no-weather --days 7
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from common import VAULT, now_iso, out, trace, write_json  # noqa: E402

PRIVATE = out("private")
MAX_QUOTE = 260

RE_WIKI = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|([^\]]+))?\]\]")
RE_MDLINK = re.compile(r"\[([^\]]+)\]\([^)]+\)")
RE_EMAIL = re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+")
RE_PHONE = re.compile(r"\b\d{3}[-.\s]\d{3,4}[-.\s]\d{4}\b")
RE_MARK = re.compile(r"[*_`>#]+")
RE_EMOJI = re.compile("[\U0001F300-\U0001FAFF☀-➿⬀-⯿️]")

# ── 텍스트 정리 ───────────────────────────────────────────────────────

def clean(s: str) -> str:
    s = RE_WIKI.sub(lambda m: m.group(2) or m.group(1).split("/")[-1], s)
    s = RE_MDLINK.sub(r"\1", s)
    s = RE_EMAIL.sub("[이메일]", s)
    s = RE_PHONE.sub("[전화번호]", s)
    s = RE_MARK.sub("", s)
    s = RE_EMOJI.sub("", s)
    s = s.replace("사용자", "창수님")            # 기록은 3인칭 「사용자」로 쓴다 — 방송에서는 이름이다
    return re.sub(r"\s+", " ", s).strip()


def sentences(text: str) -> list[str]:
    """한국어 문장 분리 — 종결 뒤 공백 기준. 숫자 소수점(1.5)은 안 자른다."""
    parts = re.split(r"(?<=[.!?。])\s+(?=[^\d])", text)
    return [p.strip() for p in parts if len(p.strip()) >= 8]


def section(md: str, heading: str, level: int = 2) -> str:
    """`## heading` 아래 본문(다음 같은/상위 레벨 헤딩 전까지)."""
    mark = "#" * level
    m = re.search(rf"^{re.escape(mark)}\s+{re.escape(heading)}[^\n]*\n(.*?)(?=^#{{1,{level}}}\s|\Z)",
                  md, re.S | re.M)
    return m.group(1) if m else ""


def subheadings(body: str, level: int = 3) -> list[str]:
    return [clean(h) for h in re.findall(rf"^{'#' * level}\s+(.+)$", body, re.M)]


def subsections(body: str, level: int = 3) -> list[tuple[str, str]]:
    """(제목, 본문 첫 문장) — 제목만 주면 추상어(「검증 층」「운영 철학」)만 남아 방송에서 못 알아듣는다 (9/18 실청).
    첫 문장이 「무슨 일이 있었나」를 준다."""
    mark = "#" * level
    outl = []
    for m in re.finditer(rf"^{mark}\s+(.+?)\s*\n(.*?)(?=^{mark}\s|\Z)", body, re.S | re.M):
        title = clean(m.group(1))
        paras = paragraphs(m.group(2))
        first = sentences(paras[0])[0] if paras and sentences(paras[0]) else ""
        outl.append((title, first))
    return outl


def bullets(body: str) -> list[str]:
    return [clean(l.lstrip("-*• ").strip()) for l in body.splitlines()
            if l.strip().startswith(("-", "*", "•")) and not l.strip().startswith("- [")]


def paragraphs(body: str) -> list[str]:
    return [clean(p) for p in re.split(r"\n\s*\n", body)
            if p.strip() and not p.strip().startswith(("|", "#", ">", "```", "- [", "!["))]


def add(pool: list[dict], path: str, quote: str, kind: str, seen: set[str]) -> None:
    q = quote.strip()
    if len(q) < 8:
        return
    if len(q) > MAX_QUOTE:
        q = q[:MAX_QUOTE].rsplit(" ", 1)[0] + "…"
    key = q[:60]
    if key in seen:
        return
    seen.add(key)
    pool.append({"path": path, "quote": q, "kind": kind})


# ── 출처별 추출 ───────────────────────────────────────────────────────

def from_weekly(pool, seen, week_file: Path, limit: int) -> int:
    md = week_file.read_text(encoding="utf-8")
    rel = f"AI/Roundup/{week_file.name}#Weekly Summary"
    n = 0
    for p in paragraphs(section(md, "Weekly Summary")):
        for s in sentences(p):
            if n >= limit:
                return n
            add(pool, rel, s, "recap", seen)
            n += 1
    return n


def from_daily(pool, seen, day_file: Path, per_file: int) -> int:
    md = day_file.read_text(encoding="utf-8")
    base = f"AI/Roundup/{day_file.name}"
    day = day_file.name[:10]
    n = 0
    # Summary 첫 문단 — 그날 한 일의 한 줄 요약들
    for p in paragraphs(section(md, "Summary"))[:1]:
        for s in sentences(p)[:per_file]:
            add(pool, f"{base}#Summary", f"{day}: {s}", "recap", seen)
            n += 1
    # Today's Work 제목 = 한 일 이름 (+ 첫 줄로 무엇을 했는지)
    for h, first in subsections(section(md, "Today's Work"))[:per_file]:
        h = re.sub(r"^\d+[.)]\s*", "", h)
        q = f"{day} 한 일: {h}" + (f" — {first[:120]}" if first else "")
        add(pool, f"{base}#Today's Work", q, "recap", seen)
        n += 1
    # Interpretation 제목 + 본문 첫 문장 = 그날의 인사이트와 그 배경
    for h, first in subsections(section(md, "Interpretation"))[:per_file]:
        q = f"{day} 인사이트: {h}" + (f" — 배경: {first[:140]}" if first else "")
        add(pool, f"{base}#Interpretation", q, "insight", seen)
        n += 1
    return n


def from_journal(pool, seen, j_file: Path, per_file: int) -> int:
    md = j_file.read_text(encoding="utf-8")
    body = section(md, "Thoughts")
    if not body:
        return 0
    day = j_file.name[:10]
    n = 0
    for m in re.finditer(r"^###\s+(.+?)\s*\n(.*?)(?=^###\s|\Z)", body, re.S | re.M):
        title, text = clean(m.group(1)), m.group(2)
        if "구술" not in title:
            continue
        sents = [s for p in paragraphs(text) for s in sentences(p)]
        for s in sents[:per_file]:
            add(pool, f"Journal/{j_file.name}#Thoughts", f"{day} 창수님 말: {s}", "insight", seen)
            n += 1
    return n


def from_last_live(pool, seen, rundown: Path) -> int:
    md = rundown.read_text(encoding="utf-8")
    body = section(md, "방송 후 기록")
    n = 0
    for line in body.splitlines():
        if not line.startswith("|") or "---" in line:
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 2 or cells[0] in ("항목",):
            continue
        for s in sentences(clean(cells[1]))[:4]:
            add(pool, f"AI/Roundup/{rundown.name}#방송 후 기록", f"지난 방송 {cells[0]}: {s}", "last_live", seen)
            n += 1
    return n


def from_filler_section(pool, seen, rundown: Path) -> int:
    md = rundown.read_text(encoding="utf-8")
    body = section(md, "코엠씨 잡담 소재")
    n = 0
    for b in bullets(body):
        add(pool, f"AI/Roundup/{rundown.name}#코엠씨 잡담 소재", b, "filler", seen)
        n += 1
    return n


# ── 날씨 (Open-Meteo, 무료·키 없음) ──────────────────────────────────

CITIES = {"서울": (37.5665, 126.9780, "Asia/Seoul"),
          "시애틀": (47.6062, -122.3321, "America/Los_Angeles")}
WMO = {0: "맑음", 1: "대체로 맑음", 2: "구름 조금", 3: "흐림", 45: "안개", 48: "안개",
       51: "이슬비", 53: "이슬비", 55: "이슬비", 61: "약한 비", 63: "비", 65: "강한 비",
       71: "약한 눈", 73: "눈", 75: "폭설", 80: "소나기", 81: "소나기", 82: "강한 소나기",
       95: "뇌우", 96: "뇌우", 99: "뇌우"}


def fetch_weather(city: str) -> dict | None:
    lat, lon, tz = CITIES[city]
    url = ("https://api.open-meteo.com/v1/forecast"
           f"?latitude={lat}&longitude={lon}&current=temperature_2m,weather_code,wind_speed_10m"
           f"&daily=temperature_2m_max,temperature_2m_min&timezone={tz}&forecast_days=1")
    try:
        with urllib.request.urlopen(url, timeout=6) as r:
            d = json.load(r)
    except Exception as e:
        return {"city": city, "ok": False, "error": f"{type(e).__name__}: {str(e)[:80]}"}
    cur, day = d["current"], d["daily"]
    local = dt.datetime.fromisoformat(cur["time"])
    return {"city": city, "ok": True, "temp_c": round(cur["temperature_2m"]),
            "sky": WMO.get(cur["weather_code"], "날씨 코드 " + str(cur["weather_code"])),
            "wind_kmh": round(cur["wind_speed_10m"]),
            "max_c": round(day["temperature_2m_max"][0]), "min_c": round(day["temperature_2m_min"][0]),
            "local_time": local.strftime("%m/%d %H:%M"), "tz": tz}


def weather_quotes(pool, seen, w: dict) -> None:
    if not w.get("ok"):
        return
    q = (f"{w['city']} 지금 날씨({w['local_time']} 현지): {w['sky']}, {w['temp_c']}도, "
         f"바람 시속 {w['wind_kmh']}km, 오늘 최고 {w['max_c']}도 최저 {w['min_c']}도")
    add(pool, f"open-meteo.com#{w['city']}", q, "weather", seen)


# ── 조립 ──────────────────────────────────────────────────────────────

def build(live: str, days: int, want_weather: bool) -> dict:
    today = dt.date.today()
    since = today - dt.timedelta(days=days)
    roundup = VAULT / "AI" / "Roundup"
    journal = VAULT / "Journal"
    pool: list[dict] = []
    seen: set[str] = set()
    sources: list[dict] = []

    weekly = sorted(roundup.glob("* - Weekly Progress and Planning.md"))
    weekly = [w for w in weekly if w.name[:10] >= since.isoformat()][-1:]
    for w in weekly:
        sources.append({"file": w.name, "n": from_weekly(pool, seen, w, limit=8)})

    for d in sorted(roundup.glob("* - Daily Roundup.md")):
        if since.isoformat() <= d.name[:10] <= today.isoformat():
            sources.append({"file": d.name, "n": from_daily(pool, seen, d, per_file=4)})

    for j in sorted(journal.glob("2026-*.md")):
        if since.isoformat() <= j.name[:10] <= today.isoformat():
            n = from_journal(pool, seen, j, per_file=4)
            if n:
                sources.append({"file": j.name, "n": n})

    rundowns = sorted(roundup.glob("* - Live* Weekly Rundown.md"))
    this = next((r for r in rundowns if f"Live{live} " in r.name), None)
    prev = None
    if this:
        idx = rundowns.index(this)
        prev = rundowns[idx - 1] if idx > 0 else None
        sources.append({"file": this.name + " (잡담 소재)", "n": from_filler_section(pool, seen, this)})
    if prev:
        sources.append({"file": prev.name + " (방송 후 기록)", "n": from_last_live(pool, seen, prev)})

    weather = {}
    if want_weather:
        for city in CITIES:
            w = fetch_weather(city)
            weather[city] = w
            weather_quotes(pool, seen, w)

    kinds: dict[str, int] = {}
    for e in pool:
        kinds[e["kind"]] = kinds.get(e["kind"], 0) + 1
    return {"live": live, "generated_at": now_iso(),
            "window": {"from": since.isoformat(), "to": today.isoformat()},
            "persona": {"name": "코엠씨", "host": "창수님", "show": "Catch Up AI 라이브"},
            "weather": weather, "sources": sources, "kinds": kinds,
            "topics": sorted({e["quote"].split(":")[0] for e in pool if e["kind"] == "recap"})[:20],
            "evidence_pool": pool}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--live", required=True)
    ap.add_argument("--days", type=int, default=7, help="오늘 포함 며칠치 (기본 7)")
    ap.add_argument("--no-weather", action="store_true")
    args = ap.parse_args()

    brief = build(args.live, args.days, not args.no_weather)
    PRIVATE.mkdir(parents=True, exist_ok=True)
    path = write_json(PRIVATE / f"casual_brief.{args.live}.json", brief)

    print(f"\n── 캐주얼 브리프 · Live #{args.live} · {brief['window']['from']} ~ {brief['window']['to']}")
    for s in brief["sources"]:
        print(f"   {s['n']:>2}건  {s['file']}")
    for city, w in brief["weather"].items():
        print(f"   날씨 {city}: " + (f"{w['sky']} {w['temp_c']}도 ({w['local_time']})" if w.get("ok")
                                   else f"⛔ 조회 실패 — {w.get('error')}"))
    print(f"   근거 {len(brief['evidence_pool'])}건 {brief['kinds']}")
    print(f"   → {path.relative_to(out(''))}")
    trace("02b_build_casual_brief", ok=True, live=args.live, evidence=len(brief["evidence_pool"]),
          kinds=brief["kinds"], weather={c: w.get("ok") for c, w in brief["weather"].items()},
          output=str(path.name))
    return 0


if __name__ == "__main__":
    sys.exit(main())
