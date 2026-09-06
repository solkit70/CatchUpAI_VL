#!/usr/bin/env python3
"""사고 4 — 문장 종결 형태 붕괴 재현율 측정.

## 무엇을 재나

리허설 1회차에서 같은 프롬프트·같은 컨텍스트·같은 모델(`gpt-5`, effort=minimal)로
두 번 돌렸는데 어미가 갈렸다.

    1회  … 선별된 항목들입니다.  / … 사용합니다.   / … 정리해 둘 예정입니다.
    2회  … 추렸다요.            / … 진행한다요.    / … 예정이다요.

게이트 6규칙은 **어미를 보지 않는다.** `REVIEW` 모드였기에 소리가 안 나갔을 뿐,
`LIVE` 였다면 "추렸다요" 가 그대로 방송에 나갔다.

프롬프트로 고칠 수 있는 문제인지, 게이트 규칙이 필요한 문제인지는
**재현율을 재기 전에는 알 수 없다.** 한 번 본 것으로 규칙을 만들면
M8 이 지적한 *"실물 2회차로 만든 규칙은 규칙이 아니라 관찰"* 이 된다.

## 판정 기준

방송에서 그대로 읽을 수 있는 종결인지만 본다. 두 가지로 잡는다.

1. **명시적 붕괴** — 해라체(`~다`)에 `요` 를 붙인 형태 (`추렸다요`, `진행한다요`)
2. **미분류 종결** — 알려진 정상 종결 어느 것에도 안 맞는 문장

2번을 따로 두는 이유는, 붕괴의 형태를 내가 다 알지 못하기 때문이다.
아는 것만 검사하면 처음 보는 형태는 통과한다.

사용:
    python ending_style_probe.py --live 26 --runs 10
    python ending_style_probe.py --live 26 --runs 10 --json
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

HERE = Path(__file__).resolve().parent
TOPIC = HERE.parents[1]
SRC = TOPIC / "07-CoMC-Engine-POC" / "src"
OUTPUT = TOPIC / "07-CoMC-Engine-POC" / "output"

# 방송에서 그대로 읽을 수 있는 종결. 존댓말 서술·의문·청유를 포괄한다.
#
# ⚠️ 첫 판(2026-09-06)에서 `습니다` 만 넣고 `니다` 를 빼먹어 **정상 문장 5건을 미분류로 잡았다**.
#    `다룹니다` 는 `습니다` 로 끝나지 않는다 — 받침이 ㅂ 인 어간에는 `습` 이 붙지 않기 때문이다
#    (다루+ㅂ니다). 종결 어미의 공통부는 `니다` 다.
#
#    M8 이 세운 기준 그대로다 — **오탐이 없어야 검사가 쓸모 있다.**
#    검사기가 정상을 이상이라고 하면 사람이 검사기를 무시하게 되고, 그 순간 검사는 없는 것이 된다.
GOOD_ENDINGS = (
    "니다", "니까",                                    # 합쇼체 전부 (습니다·ㅂ니다·입니다·다룹니다…)
    "어요", "아요", "여요", "해요", "예요", "에요", "네요", "세요", "지요", "죠",
    "게요", "께요", "데요", "고요", "군요", "든요", "나요", "까요", "봐요", "와요",
)

# 해라체 + 요 = 붕괴. `~다요` 계열을 명시적으로 잡는다.
RE_BROKEN = re.compile(r"(?:[가-힣])다\s*요[.!?]?$")


def classify(sentence: str) -> str:
    s = sentence.strip().rstrip(".!?…").strip()
    if not s:
        return "empty"
    if RE_BROKEN.search(sentence.strip()):
        return "broken"          # 확실한 붕괴
    if any(s.endswith(e) for e in GOOD_ENDINGS):
        return "ok"
    return "unknown"             # 아는 정상형이 아님 — 사람이 봐야 한다


def run_once(live: str) -> list[str]:
    r = subprocess.run(
        [sys.executable, "04_compose_answer.py", "--live", live],
        cwd=SRC, capture_output=True, text=True, encoding="utf-8",
        env={**__import__("os").environ, "PYTHONIOENCODING": "utf-8"})
    if r.returncode != 0:
        return []
    try:
        return json.loads((OUTPUT / "answer_draft.json")
                          .read_text(encoding="utf-8"))["sentences"]
    except Exception:
        return []


def main() -> int:
    ap = argparse.ArgumentParser(description="문장 종결 형태 붕괴 재현율 측정")
    ap.add_argument("--live", default="26")
    ap.add_argument("--runs", type=int, default=10)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    runs, tally = [], Counter()
    for i in range(1, args.runs + 1):
        sents = run_once(args.live)
        marks = [classify(s) for s in sents]
        tally.update(marks)
        runs.append({"run": i, "sentences": sents, "marks": marks,
                     "has_broken": "broken" in marks,
                     "has_unknown": "unknown" in marks})
        if not args.json:
            bad = sum(1 for m in marks if m != "ok")
            flag = "❌" if "broken" in marks else ("⚠️ " if "unknown" in marks else "✅")
            print(f"{flag} {i:>2}회  문장 {len(sents)}개 · 비정상 {bad}개")
            for s, m in zip(sents, marks):
                if m != "ok":
                    print(f"        [{m}] {s}")

    runs_broken = sum(1 for r in runs if r["has_broken"])
    runs_unknown = sum(1 for r in runs if r["has_unknown"] and not r["has_broken"])
    total_sent = sum(len(r["sentences"]) for r in runs)

    if args.json:
        print(json.dumps({"live": args.live, "runs": args.runs,
                          "measured_at": datetime.now().isoformat(),
                          "runs_broken": runs_broken, "runs_unknown": runs_unknown,
                          "sentence_tally": dict(tally), "detail": runs},
                         ensure_ascii=False, indent=2))
        return 0

    print("\n" + "=" * 66)
    print(f"  실행 {args.runs}회 · 문장 {total_sent}개")
    print(f"  붕괴 발생 실행     {runs_broken}/{args.runs}"
          f"   ({runs_broken / args.runs * 100:.0f}%)")
    print(f"  미분류 종결 실행   {runs_unknown}/{args.runs}")
    print(f"  문장 단위          정상 {tally['ok']} · 붕괴 {tally['broken']} · "
          f"미분류 {tally['unknown']}")
    print("-" * 66)
    if runs_broken == 0 and runs_unknown == 0:
        print("  ✅ 이번 표본에서 붕괴 없음.")
        print("     다만 0/N 은 '안 난다'가 아니라 '이 표본에서 안 봤다'이다.")
    elif runs_broken:
        print("  ❌ 붕괴 재현됨 — 프롬프트만으로는 보장되지 않는다.")
        print("     게이트에 종결 형태 검사를 넣어야 LIVE 자동 발화가 가능하다.")
    else:
        print("  ⚠️  명시적 붕괴는 없으나 미분류 종결이 있다. 형태를 확인할 것.")
    print("=" * 66)
    return 0


if __name__ == "__main__":
    sys.exit(main())
