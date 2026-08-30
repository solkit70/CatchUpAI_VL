#!/usr/bin/env python3
"""M8 — 게이트 새 규칙의 결정적 테스트.

## 왜 시나리오만으로 부족한가

`run_scenarios.py` 는 실제 LLM 을 부른다. 실물을 통과시키는 검증이라 값지지만,
**모델이 매번 같은 문장을 만들지 않는다.** absence-claim 시나리오는 어떤 회차에는
"…포함되어 있지 않습니다"를 만들고 어떤 회차에는 그냥 커버리지만 나열한다.

그러면 규칙이 깨져도 그날 우연히 부재 문장이 안 나오면 초록불이 켜진다.
**우연히 통과하는 테스트는 회귀를 못 잡는다.**

여기서는 초안을 손으로 만들어 규칙만 본다. LLM 을 부르지 않으므로 빠르고 결정적이다.
둘 다 필요하다 — 시나리오는 실물과의 접점을, 이 테스트는 규칙의 불변성을 지킨다.

실행:
    python test_gate_rules.py
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE.parent.parent / "07-CoMC-Engine-POC" / "src"
sys.path.insert(0, str(SRC))

import importlib.util  # noqa: E402

_spec = importlib.util.spec_from_file_location("_gate", SRC / "05_verify_and_gate.py")
gate = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(gate)

POLICY = gate.load_safety_policy(warn=False)

# ── 고정 컨텍스트 ─────────────────────────────────────────────────────
# 실물 Live21 3부를 본떴다. 값을 줄여 무엇이 검사되는지 눈으로 보이게 했다.
CTX = {
    "current_part_id": "3",
    "coverage_state": "defined",
    "coverage_items": ["AI로 라방 보조 MC 앱 만들기",
                       "기존 스킬을 OpenAI 신규 Transcribe 모델로 업데이트"],
    "evidence_pool": [
        {"path": "R.md#오늘의 실험", "quote": "★ 실험 1 — AI로 라이브 방송 보조 MC 앱 만들기"},
        {"path": "R.md#오늘의 실험", "quote": "★ 실험 2 — 기존 스킬을 OpenAI 신규 Transcribe 모델로 업데이트"},
        {"path": "R.md#오늘의 실험", "quote": "5개 스킬에 반영 완료"},
    ],
    "status_map": {}, "forbidden_removed": True, "assembled_at": "2026-08-30T00:00:00Z",
}


def draft(sentences: list[str], claims: list[tuple[int, str]]) -> dict:
    return {
        "sentences": sentences,
        "claim_map": [{"sentence_idx": i, "evidence_path": "R.md#오늘의 실험",
                       "evidence_quote": q} for i, q in claims],
        "coverage_state": "defined",
        "length_sentences": len(sentences),
    }


EV1 = "★ 실험 1 — AI로 라이브 방송 보조 MC 앱 만들기"
EV2 = "★ 실험 2 — 기존 스킬을 OpenAI 신규 Transcribe 모델로 업데이트"
EV3 = "5개 스킬에 반영 완료"

CASES = [
    # ── 부재 주장 ─────────────────────────────────────────────────────
    ("부재 주장 · 화이트리스트 밖 → 닫힘 근거로 허용",
     draft(["데이터센터 인력 프로그램은 오늘 방송 범위에 포함되어 있지 않습니다."],
           [(0, EV1)]),
     lambda v: v["absence_by_closure"] == [0] and not v["dropped_sentences"],
     "주제가 화이트리스트에 없다 → '없다'가 참임을 목록만으로 확정할 수 있다. "
     "다만 근거는 인용이 아니라 닫힘이므로 그렇게 기록돼야 한다"),

    ("부재 주장 · 화이트리스트 안 → 모순이므로 드롭",
     draft(["AI로 라방 보조 MC 앱 만들기는 오늘 다루지 않습니다."], [(0, EV1)]),
     lambda v: [d["reason"] for d in v["dropped_sentences"]] == ["absence_contradicts_coverage"],
     "화이트리스트에 있는 항목을 없다고 말한다 → 화이트리스트와 정면으로 어긋난다"),

    # ── 사실 검사 ─────────────────────────────────────────────────────
    ("숫자 환각 → 드롭",
     draft(["총 47건이 반영 완료되었습니다."], [(0, EV3)]),
     lambda v: [d["reason"] for d in v["dropped_sentences"]] == ["fact_not_in_evidence"],
     "근거에는 5개라고 적혀 있는데 47을 말한다"),

    ("근거에 있는 숫자 → 통과",
     draft(["5개 스킬에 반영이 완료되었습니다."], [(0, EV3)]),
     lambda v: v["pass"],
     "같은 숫자 검사라도 근거에 있으면 막지 않는다 — 막는 것만 잘하면 앱이 쓸모를 잃는다"),

    ("파트 번호는 근거에 없어도 통과 (권위값)",
     draft(["3번 파트는 AI로 라이브 방송 보조 MC 앱 만들기를 다룹니다."], [(0, EV1)]),
     lambda v: v["pass"],
     "'3'은 current_part_id 다. M7 권위값이고 근거 풀보다 믿을 수 있다"),

    ("고유명사 환각 → 드롭",
     # ⚠️ 주제와 무관한 문장을 쓰면 ③ 화이트리스트 검사가 먼저 잡아
     #    fact_not_in_evidence 에 도달하지 못한다. 실제 환각은 **맞는 문장에 섞여**
     #    들어오므로, 근거와 겹치는 문장에 인명만 얹어 시험한다.
     draft(["실험 1은 Minsoo Son 님이 맡았습니다."], [(0, EV1)]),
     lambda v: [d["reason"] for d in v["dropped_sentences"]] == ["fact_not_in_evidence"],
     "근거에 없는 인명. 문장 나머지는 근거와 겹쳐 ③을 통과한다"),

    ("근거에 있는 고유명사 → 통과",
     draft(["기존 스킬을 OpenAI 신규 Transcribe 모델로 업데이트합니다."], [(0, EV2)]),
     lambda v: v["pass"],
     "OpenAI·Transcribe 는 근거에 있다"),

    # ── M7 규칙 회귀 ─────────────────────────────────────────────────
    ("근거 없는 문장 → 드롭 (M7 규칙 유지)",
     draft(["오늘은 날씨가 좋습니다."], []),
     lambda v: [d["reason"] for d in v["dropped_sentences"]] == ["no_evidence"],
     "M8 검사를 추가하면서 M7 규칙이 깨지지 않았는지 본다"),

    ("위조 인용 → 드롭 (M7 규칙 유지)",
     draft(["실험 1을 다룹니다."], [(0, "근거 풀에 없는 위조 인용입니다")]),
     lambda v: [d["reason"] for d in v["dropped_sentences"]] == ["evidence_not_found"],
     "인용이 근거 풀에 없다"),
]


def main() -> int:
    ok = 0
    for title, d, check, why in CASES:
        v = gate.verify(d, CTX, POLICY)
        passed = bool(check(v))
        ok += passed
        print(f"\n{'✅' if passed else '❌'} {title}")
        print(f"   {why}")
        print(f"   문장  {d['sentences'][0][:64]}")
        print(f"   결과  pass={v['pass']} · 드롭={[x['reason'] for x in v['dropped_sentences']] or '-'}"
              f" · 닫힘근거={v.get('absence_by_closure') or '-'}")
        if not passed:
            for x in v["violations"]:
                print(f"        ⚠ {x['rule_id']}: {x.get('detail','')}")

    print(f"\n{'═'*66}\n  {ok}/{len(CASES)} 통과")
    return 0 if ok == len(CASES) else 1


if __name__ == "__main__":
    sys.exit(main())
