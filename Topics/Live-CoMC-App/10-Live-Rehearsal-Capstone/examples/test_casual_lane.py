#!/usr/bin/env python3
"""CVL 4 회귀 — 캐주얼 레인이 방송 내용 레인을 침범하지 않는가, 그리고 길게 말하는가.

두 단계다.

  1. 분류 (LLM 없음, 1초) — 진행자가 실제로 할 말 14개가 맞는 의도로 가는지. 특히
     「오늘 2부에서 뭘 다루나요」가 캐주얼로 새면 안 되고, 「이번 주 뭐 했어요」가 방송 레인으로
     가서 침묵하면 안 된다. 규칙을 넓힐 때마다 여기서 잡는다.
  2. --llm — 엔진을 인프로세스로 띄워 4개 발화를 끝까지 돌린다 (LLM 4회, 약 40초). filler ·
     broadcast_status 가 **30초(≈230자) 이상** 말하는지, 날씨가 브리프 값 그대로인지, 방송 질문이
     여전히 broadcast 레인인지 본다. 모드는 건드리지 않는다 (REVIEW 면 소리 없음).

실행:
    python test_casual_lane.py
    python test_casual_lane.py --llm --live 28
"""
from __future__ import annotations

import argparse
import importlib.util
import io
import sys
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path

HERE = Path(__file__).resolve().parent
TOPIC = HERE.parents[1]
M7 = TOPIC / "07-CoMC-Engine-POC" / "src"
M9 = TOPIC / "09-Desktop-Shell-and-Overlay" / "examples" / "engine"
for p in (M7, M9):
    sys.path.insert(0, str(p))

from common import out, read_json  # noqa: E402

CASES = [
    # (발화, 기대 의도)
    ("오늘 2부에서 뭘 다루나요?", "answer_question"),
    ("2부 첫 항목이 뭐죠?", "answer_question"),
    ("CoMC 앱은 어디까지 왔나요?", "answer_question"),
    ("Chrome Remote Desktop 에 대해 설명해 주세요", "answer_question"),
    ("주간 영상은 뭐예요?", "answer_question"),
    ("오늘 서울 날씨는 어때요?", "small_talk"),
    ("코엠씨 자기소개 해 주세요", "small_talk"),
    ("이번 주에 뭘 했어요?", "weekly_recap"),
    ("이번 주 인사이트가 뭐예요?", "insight"),
    ("내가 잠깐 물 마시고 있을 동안 시청자분들께 재미있는 얘기 해 주세요", "filler"),
    ("내가 쉬는 동안 재밌는 얘기 해줘", "filler"),
    ("잠깐 볼 일 보고 올테니까 니가 진행하고 있어", "filler"),
    ("내가 잠깐 볼일 보고 올테니 시청자 분들께 지금까지 한 일과 앞으로 남은 일에 대해 설명해주세요", "broadcast_status"),
    ("멈춰", "stop"),
]

LLM_CASES = [
    ("오늘 시애틀 날씨는 어때요?", "small_talk", 0),
    ("내가 잠깐 물 마시고 있을 동안 시청자분들께 재미있는 얘기 해 주세요", "filler", 230),
    ("내가 잠깐 볼일 보고 올테니 시청자 분들께 지금까지 한 일과 앞으로 남은 일에 대해 설명해주세요", "broadcast_status", 230),
    ("오늘 2부에서 뭘 다루나요?", "answer_question", 0),
]


def load(name):
    spec = importlib.util.spec_from_file_location(name.replace(".py", ""), M7 / name)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def test_classify() -> int:
    m3 = load("03_classify_intent.py")
    bad = 0
    for text, want in CASES:
        got = m3.classify(text)[0]
        mark = "✅" if got == want else "❌"
        bad += got != want
        print(f"  {mark} {got:<17} {text}" + ("" if got == want else f"   ← 기대 {want}"))
    return bad


def test_llm(live: str) -> int:
    import engine_daemon as dm
    with redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
        eng = dm.Engine()
        eng.prewarm(live, part="2")
    brief = read_json(out("private") / f"casual_brief.{live}.json")
    weather = brief.get("weather", {}).get("시애틀", {})
    bad = 0
    for text, want, min_chars in LLM_CASES:
        for f in ("verdict.json", "intent.json", "answer_draft.json"):
            if out(f).exists():
                out(f).unlink()
        with redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
            r = eng.utter(live, text)
        vd = read_json(out("verdict.json")) if out("verdict.json").exists() else {}
        ft = vd.get("final_text", "")
        ok = r.get("ok") and r.get("intent") == want and len(ft) >= min_chars
        if want == "small_talk" and weather.get("ok"):
            ok = ok and str(weather["temp_c"]) in ft
        if want == "answer_question":
            ok = ok and r.get("lane") == "broadcast"
        bad += not ok
        print(f"  {'✅' if ok else '❌'} {r.get('intent')} lane={r.get('lane')} {len(ft)}자≈{round(len(ft)/7.7)}초 "
              f"{r.get('total_ms')}ms  {text[:28]}")
        print(f"       {ft[:120]}")
    return bad


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--llm", action="store_true")
    ap.add_argument("--live", default="28")
    args = ap.parse_args()
    print("── 1. 분류 (규칙, LLM 없음)")
    bad = test_classify()
    print(f"   {len(CASES) - bad}/{len(CASES)}")
    if args.llm:
        print("\n── 2. 끝까지 (LLM)")
        b2 = test_llm(args.live)
        print(f"   {len(LLM_CASES) - b2}/{len(LLM_CASES)}")
        bad += b2
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
