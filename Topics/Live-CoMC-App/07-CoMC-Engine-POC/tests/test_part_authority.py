#!/usr/bin/env python3
"""M7 실습 5 검증 — 시각 추정이 틀려도 권위값은 변하지 않음을 증명한다.

로드맵 검증 기준: "시각 기반 추정이 틀려도 current_part_id 는 변하지 않음을 테스트로 증명"

증명 방식이 중요하다. "안 바뀌더라"를 한 번 확인하는 것으로는 부족하다 —
**추정이 틀린 상황을 일부러 만들고**, 그 상태에서 여러 번 갱신해도 권위값이 그대로인지 본다.
M4에서 에코 게이트를 off/on 으로 나눠 잰 것과 같은 이유다. 게이트가 일한다는 것은
게이트를 껐을 때 다른 결과가 나와야 증명된다.

실행: python tests/test_part_authority.py
"""
from __future__ import annotations

import sys
from pathlib import Path

SRC = Path(__file__).resolve().parents[1] / "src"
sys.path.insert(0, str(SRC))

from session_state import (AUTHORITY_SOURCES, estimate,  # noqa: E402
                           init_state, refresh_suggestion, set_current_part)

FAILS: list[str] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    print(f"  {'OK  ' if ok else 'FAIL'} {name}" + (f"  — {detail}" if detail else ""))
    if not ok:
        FAILS.append(name)


def main() -> int:
    print("M7 실습 5 — 권위값/추정값 분리 검증\n")

    # ── 1. 추정이 권위값과 어긋난 상태를 만든다 ────────────────────────
    # 진행자는 아직 1부에 있는데(계획 초과), 시계는 이미 3부를 가리킨다.
    st = init_state("21", "1")
    st = refresh_suggestion(st, elapsed_min=45.0)
    check("추정이 권위값과 다른 상황 생성",
          st["suggested_part_id"] not in (None, "1"),
          f"current=1 / suggested={st['suggested_part_id']}")

    # ── 2. 갱신을 반복해도 권위값은 그대로 ────────────────────────────
    before = st["current_part_id"]
    for minute in (12.0, 25.0, 33.0, 45.0, 90.0, 200.0):
        st = refresh_suggestion(st, elapsed_min=minute)
        if st["current_part_id"] != before:
            check(f"{minute}분 갱신 후 권위값 유지", False,
                  f"{before} → {st['current_part_id']}")
            break
    else:
        check("6회 반복 갱신 후에도 권위값 불변", True, f"current={before!r} 그대로")

    # ── 3. 추정이 틀려도 응답에 쓰이는 값은 권위값 ────────────────────
    st = refresh_suggestion(st, elapsed_min=45.0)
    check("불일치 상태에서 권위값이 응답 기준",
          st["current_part_id"] == "1" and st["suggested_part_id"] != "1",
          f"응답은 {st['current_part_id']}부 근거로 나가야 한다")

    # ── 4. 권위값은 사람의 동작으로만 바뀐다 ──────────────────────────
    st = set_current_part(st, "2", by="hotkey")
    check("핫키로는 권위값 변경 가능", st["current_part_id"] == "2")

    # 'clock' 은 허용 목록에 없다 → set_current_part 가 종료시켜야 한다
    check("'clock' 은 권위 소스가 아니다", "clock" not in AUTHORITY_SOURCES)
    try:
        set_current_part(st, "3", by="clock")
        check("시계발 변경은 거부된다", False, "거부되지 않았다")
    except SystemExit:
        check("시계발 변경은 거부된다", True, "SystemExit")

    # ── 5. refresh_suggestion 은 권위값에 대입하지 않는다 (소스 검사) ──
    # 실수로 넣기 어렵게 만드는 것이 문서로 금지하는 것보다 낫다.
    src = (SRC / "session_state.py").read_text(encoding="utf-8")
    body = src.split("def refresh_suggestion")[1].split("\ndef ")[0]
    check("refresh_suggestion 안에 current_part_id 대입 없음",
          'st["current_part_id"] =' not in body and "st['current_part_id'] =" not in body)

    # ── 6. 추정 불가는 None (틀린 추정보다 낫다) ──────────────────────
    pid, conf, why = estimate(-5.0)
    check("구간 밖 경과 시간은 추정하지 않는다", pid is None, why)

    print()
    if FAILS:
        print(f"실패 {len(FAILS)}건: {', '.join(FAILS)}")
        return 1
    print("전부 통과 — 시각 추정은 권위값을 바꿀 수 없다")
    return 0


if __name__ == "__main__":
    sys.exit(main())
