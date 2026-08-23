#!/usr/bin/env python3
"""M7 실습 5 — 파트 판정 권위값/추정값 분리.

M2에서 확정한 "자동 전환 금지" 원칙을 코드로 만든 것이다.

```
current_part_id     권위값. 핫키·음성 명령·클릭으로만 바뀐다. 응답에 쓰이는 유일한 값
suggested_part_id   추정값. 시각으로 계산한다. 화면 배지로만 알리고 아무것도 바꾸지 않는다
```

## 왜 자동 전환을 막는가

방송은 계획대로 흐르지 않는다. 1부가 20분으로 잡혀 있어도 실제로는 35분이 될 수 있다.
그때 앱이 혼자 2부로 넘어가면 **진행자는 1부 이야기를 하는데 AI 는 2부 근거로 답한다.**
어긋난 것을 시청자가 먼저 알아챈다.

추정이 틀리는 것 자체는 문제가 아니다. 틀린 추정이 **권위를 갖는 것**이 문제다.
그래서 이 모듈에는 추정값이 권위값을 쓰는 경로가 아예 없다 —
`refresh_suggestion()` 은 `current_part_id` 에 손대지 않고, 바꾸는 함수는
`set_current_part()` 하나뿐이며 그것은 사람의 동작으로만 호출된다.

## 추정할 수 없으면 하지 않는다

Live20 은 전 파트가 '시간 미정'이라 타임라인을 만들 수 없다. 이때 추정값은 null 이다.
틀린 추정을 표시하는 것보다 아무것도 표시하지 않는 것이 낫다 —
배지가 떠 있으면 진행자는 그것을 믿는다.

실행:
    python session_state.py --init --live 21 --part 1
    python session_state.py --suggest --elapsed 25      # 25분 경과 시점 추정
    python session_state.py --set-part 2 --by hotkey    # 권위값 변경 (사람 동작)
    python session_state.py --show
"""
from __future__ import annotations

import argparse
import sys
import uuid
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from common import (DATA, now_iso, out, read_json, rel_to_vault, trace,  # noqa: E402
                    validate_or_die, write_json)

STATE = out("session_state.json")
TIMELINE = DATA / "part_timeline.sample.json"

# 권위값을 바꿀 수 있는 경로. 전부 사람의 동작이다.
# 'clock' 은 여기에 없다 — 그것이 이 모듈의 요점이다.
AUTHORITY_SOURCES = ("hotkey", "voice", "click")


def init_state(live: str, part_id: str | None) -> dict:
    st = {
        "session_id": f"live{live}-{uuid.uuid4().hex[:8]}",
        "started_at": now_iso(),
        "current_part_id": part_id,
        "suggested_part_id": None,
        "suggested_confidence": None,
        "wake_gate": "open",
        "active_provider": "openai",
        "trace_path": rel_to_vault(out("session_trace.jsonl")),
        "remaining_seconds": None,
        "hitl_pending": False,
    }
    return st


def estimate(elapsed_min: float) -> tuple[str | None, float | None, str]:
    """경과 분 → (추정 파트 id, 신뢰도, 사유). 추정 불가면 (None, None, 사유)."""
    if not TIMELINE.exists():
        return None, None, "타임라인 파일 없음 — 추정하지 않는다"
    tl = read_json(TIMELINE)
    parts = tl.get("parts", [])
    if not parts:
        return None, None, "타임라인에 파트 없음"

    # 계획 시간이 하나도 없으면 추정 자체가 성립하지 않는다 (Live20 이 그런 경우다)
    if all(p.get("planned_minutes") is None and not p.get("is_remainder")
           for p in parts):
        return None, None, "전 파트 시간 미정 — 추정 불가"

    for p in parts:
        start = p.get("offset_start_min")
        end = p.get("offset_end_min")
        if start is None:
            continue
        if end is None:                       # is_remainder — 끝을 모른다
            if elapsed_min >= start:
                # 끝 시각을 계산할 수 없으므로 신뢰도를 낮춘다
                return p["id"], 0.5, "나머지 시간 파트 — 종료 시각 미상"
            continue
        if start <= elapsed_min < end:
            return p["id"], 0.8, f"계획 구간 {start}~{end}분"
    return None, None, f"{elapsed_min}분은 어느 계획 구간에도 들지 않는다"


def refresh_suggestion(st: dict, elapsed_min: float) -> dict:
    """추정값만 갱신한다. current_part_id 는 건드리지 않는다.

    이 함수가 current_part_id 에 대입하는 줄은 존재하지 않는다.
    실수로 넣기 어렵게 만드는 것이 문서로 금지하는 것보다 낫다.
    """
    pid, conf, why = estimate(elapsed_min)
    st["suggested_part_id"] = pid
    st["suggested_confidence"] = conf
    st["_suggestion_note"] = why          # 스키마 밖 — 저장 전에 뺀다
    return st


def set_current_part(st: dict, part_id: str, by: str) -> dict:
    """권위값 변경. 사람의 동작으로만 호출된다."""
    if by not in AUTHORITY_SOURCES:
        sys.exit(f"권위값은 {'/'.join(AUTHORITY_SOURCES)} 로만 바꿀 수 있습니다. "
                 f"'{by}' 는 허용되지 않습니다 — 시각 추정은 권위가 없습니다.")
    st["current_part_id"] = part_id
    return st


def save(st: dict) -> Path:
    body = {k: v for k, v in st.items() if not k.startswith("_")}
    validate_or_die("session_state", body, "session_state")
    return write_json(STATE, body)


def load() -> dict:
    if not STATE.exists():
        sys.exit("session_state.json 없음. 먼저 --init 을 실행하세요.")
    return read_json(STATE)


def show(st: dict) -> None:
    cur, sug = st.get("current_part_id"), st.get("suggested_part_id")
    print(f"\n   current_part_id   {cur!r}   ← 권위값 (응답에 쓰이는 유일한 값)")
    conf = st.get("suggested_confidence")
    conf_s = f"{conf:.1f}" if conf is not None else "—"
    print(f"   suggested_part_id {sug!r}   신뢰도 {conf_s}   ← 표시 전용")
    if st.get("_suggestion_note"):
        print(f"                     ({st['_suggestion_note']})")
    if sug is not None and cur is not None and sug != cur:
        print(f"   ⚠ 불일치 배지: 추정 {sug}부 / 실제 {cur}부 — "
              f"**자동 전환하지 않는다.** 진행자가 판단한다")
    print(f"   wake_gate={st.get('wake_gate')} · hitl_pending={st.get('hitl_pending')}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--init", action="store_true")
    ap.add_argument("--live", default="21")
    ap.add_argument("--part")
    ap.add_argument("--suggest", action="store_true")
    ap.add_argument("--elapsed", type=float, help="방송 시작 후 경과 분")
    ap.add_argument("--set-part")
    ap.add_argument("--by", default="hotkey", help=f"{'/'.join(AUTHORITY_SOURCES)}")
    ap.add_argument("--show", action="store_true")
    args = ap.parse_args()

    if args.init:
        st = init_state(args.live, args.part)
        save(st)
        print(f"세션 시작 · {st['session_id']}")
        show(st)
        trace("session_state", ok=True, action="init", part=args.part)
        return 0

    st = load()

    if args.set_part:
        before = st.get("current_part_id")
        set_current_part(st, args.set_part, args.by)
        save(st)
        print(f"권위값 변경 ({args.by}): {before!r} → {st['current_part_id']!r}")
        trace("session_state", ok=True, action="set_current_part",
              by=args.by, before=before, after=st["current_part_id"])
        show(st)
        return 0

    if args.suggest:
        if args.elapsed is None:
            sys.exit("--elapsed 가 필요합니다 (방송 시작 후 경과 분)")
        before = st.get("current_part_id")
        refresh_suggestion(st, args.elapsed)
        save(st)
        after = read_json(STATE)["current_part_id"]
        assert before == after, "추정이 권위값을 바꿨다 — 있어서는 안 되는 일"
        print(f"경과 {args.elapsed}분 기준 추정 갱신")
        show(st)
        trace("session_state", ok=True, action="refresh_suggestion",
              elapsed_min=args.elapsed, suggested=st["suggested_part_id"],
              current_unchanged=before)
        return 0

    show(st)
    return 0


if __name__ == "__main__":
    sys.exit(main())
