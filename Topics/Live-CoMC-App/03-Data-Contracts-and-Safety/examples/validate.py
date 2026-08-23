#!/usr/bin/env python3
"""M3 7종 JSON Schema 유효성 검사.

두 가지를 검증한다:
  A. 7종 스키마가 그 자체로 유효한 JSON Schema(Draft 2020-12)인가  (check_schema)
  B. grounded 샘플 인스턴스가 각 스키마를 통과하는가 (양성) + 위반 인스턴스가 거부되는가 (음성)

샘플은 M1 case-table.md(Live21/Live14 실측)의 변동성 케이스를 그대로 담아,
"M1 케이스 표의 모든 변동성이 스키마 필드로 표현 가능"함을 함께 확인한다.

실행: python validate.py
"""
import json
import sys
from pathlib import Path
from jsonschema import Draft202012Validator
from jsonschema.exceptions import ValidationError

# Windows 콘솔(cp1252)에서 한글 print가 깨지지 않도록 UTF-8 강제
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

SCHEMA_DIR = Path(__file__).parent / "schemas"


def load(name):
    return json.loads((SCHEMA_DIR / name).read_text(encoding="utf-8"))


# ── grounded 양성 샘플 ────────────────────────────────────────────────
# rundown_index: M1 case-table 케이스 1~8을 parts로 모두 표현
SAMPLE_RUNDOWN_INDEX = {
    "source_path": "AI/Roundup/2026-07-26 - Live21 Weekly Rundown.md",
    "frontmatter_status": "✅ 최종본 (2026-07-26)",
    "is_final": True,
    "parts": [
        {  # 케이스 1: 정수 파트 + 분 단위
            "id": "1", "sort_key": 1.0, "title": "지난 주 활동",
            "time_raw": "20분", "time_minutes": 20, "is_remainder": False,
            "coverage_state": "defined", "coverage_items": ["지난 주 방송 회고"],
            "directive_note": None,
        },
        {  # 케이스 2: 정수 파트 + 시간 미정 → null
            "id": "1b", "sort_key": 1.5, "title": "지난 주 활동(미정본)",
            "time_raw": "시간 미정", "time_minutes": None, "is_remainder": False,
            "coverage_state": "defined", "coverage_items": ["회고"],
            "directive_note": None,
        },
        {  # 케이스 3: '나머지 시간 전부' → is_remainder
            "id": "3", "sort_key": 3.0, "title": "오늘의 실험",
            "time_raw": "나머지 시간 전부", "time_minutes": None, "is_remainder": True,
            "coverage_state": "directive",
            "coverage_items": ["AI로 라방 보조 MC 앱 만들기", "두 번째 항목"],
            # 케이스 7: 커버리지 줄 끝 운영 지시문 분리 보존
            "directive_note": "이 두 개를 메인으로 진행하고, 시간이 남으면 아래 대기 목록에서 이어간다",
        },
        {  # 케이스 4: 소수 파트(.5부) → sort_key float
            "id": "4.5", "sort_key": 4.5, "title": "방송 인사이트 — 기록은 어떻게 시작하나",
            "time_raw": None, "time_minutes": None, "is_remainder": False,
            "coverage_state": "undefined", "coverage_items": [],  # 케이스 8: undefined
            "directive_note": None,
        },
    ],
    "excluded_sections": [
        {"heading": "## 보류된 인사이트 후보 (이번 방송 미편성)", "reason": "unscheduled"},
        {"heading": "## 주간 영상 후보 (이번 방송 코너 미편성)", "reason": "unscheduled"},
    ],
    "conditional_sections": [
        {"heading": "### 대기 목록 (시간이 남으면)", "condition": "시간이 남으면"},
    ],
    "parsed_at": "2026-08-09T05:40:00Z",
}

SAMPLE_BROADCAST_CONTEXT = {
    "current_part_id": "3",
    "coverage_state": "directive",
    "coverage_items": ["AI로 라방 보조 MC 앱 만들기", "두 번째 항목"],
    "evidence_pool": [
        {"path": "AI/Roundup/2026-07-26 - Live21 Weekly Rundown.md",
         "quote": "①AI로 라방 보조 MC 앱 만들기"},
    ],
    "status_map": {"rundown": "final", "dashboard": "stale"},
    "forbidden_removed": True,
    "assembled_at": "2026-08-09T05:41:00Z",
}

SAMPLE_SESSION_STATE = {
    "session_id": "live21-20260726",
    "started_at": "2026-07-26T18:00:00Z",
    "current_part_id": "3",
    "wake_gate": "closed",
    "active_provider": "claude",
    "trace_path": "runtime/session_trace.jsonl",
    "remaining_seconds": 900,
    "hitl_pending": False,
}

SAMPLE_INTENT = {
    "transcript": "3부 커버리지 요약해줘",
    "intent": "summarize_part",
    "slots": {"part_id": "3"},
    "ambiguity_flags": [],
    "confidence": 0.92,
    "created_at": "2026-08-09T05:42:00Z",
}

SAMPLE_ANSWER_DRAFT = {
    "provider": "claude",
    "sentences": [
        "오늘 3부에서는 AI로 라이브 방송 보조 MC 앱을 만듭니다.",
        "두 번째 항목도 함께 다룹니다.",
    ],
    "claim_map": [
        {"sentence_idx": 0, "evidence_path": "AI/Roundup/2026-07-26 - Live21 Weekly Rundown.md",
         "evidence_quote": "①AI로 라방 보조 MC 앱 만들기"},
        {"sentence_idx": 1, "evidence_path": "AI/Roundup/2026-07-26 - Live21 Weekly Rundown.md",
         "evidence_quote": "두 번째 항목"},
    ],
    "coverage_state": "directive",
    "length_sentences": 2,
    "created_at": "2026-08-09T05:43:00Z",
}

SAMPLE_VERDICT = {
    "pass": False,
    "final_text": "오늘 3부에서는 AI로 라이브 방송 보조 MC 앱을 만듭니다.",
    "kept_sentences": [0],
    "dropped_sentences": [{"sentence_idx": 1, "reason": "evidence_not_found"}],
    "violations": [{"rule_id": "claim.evidence_required", "detail": "sentence 1 근거 문자열 미발견"}],
    "length_after": 1,
    "verified_at": "2026-08-09T05:44:00Z",
}

SAMPLE_OUTPUT = {
    "overlay": {"text": "오늘 3부에서는 AI로 라이브 방송 보조 MC 앱을 만듭니다.",
                "part_id": "3", "updated_at": "2026-08-09T05:45:00Z"},
    # provider 는 2026-08-23 M7 착수 시 추가된 필수 필드다.
    # M6 서킷 브레이커가 런타임에 프로바이더를 교체하므로 voice id 로 역추정하면 안 된다.
    "spoken": {"text": "오늘 3부에서는 AI로 라이브 방송 보조 MC 앱을 만듭니다.",
               "provider": "edge", "voice": "ko-KR-SunHiNeural", "audio_path": None,
               "spoken_at": "2026-08-09T05:45:01Z"},
    "source_verdict_pass": False,
}

POSITIVE = [
    ("rundown_index.schema.json", SAMPLE_RUNDOWN_INDEX),
    ("broadcast_context.schema.json", SAMPLE_BROADCAST_CONTEXT),
    ("session_state.schema.json", SAMPLE_SESSION_STATE),
    ("intent.schema.json", SAMPLE_INTENT),
    ("answer_draft.schema.json", SAMPLE_ANSWER_DRAFT),
    ("verdict.schema.json", SAMPLE_VERDICT),
    ("output.schema.json", SAMPLE_OUTPUT),
]

# ── 음성 샘플 (계약이 실제로 나쁜 데이터를 거부하는지) ──────────────────
NEGATIVE = [
    # answer_draft: claim_map 누락 → 문장별 근거 강제 위반
    ("answer_draft.schema.json",
     {k: v for k, v in SAMPLE_ANSWER_DRAFT.items() if k != "claim_map"},
     "claim_map 누락"),
    # broadcast_context: forbidden_removed=false → 금칙 제거 불변식 위반(const true)
    ("broadcast_context.schema.json",
     {**SAMPLE_BROADCAST_CONTEXT, "forbidden_removed": False},
     "forbidden_removed=false"),
    # rundown_index: coverage_state 오탈자 → enum 위반
    ("rundown_index.schema.json",
     {**SAMPLE_RUNDOWN_INDEX,
      "parts": [{**SAMPLE_RUNDOWN_INDEX["parts"][0], "coverage_state": "defiend"}]},
     "coverage_state enum 위반"),
    # output: spoken 누락 → 봉투 필수 항목 위반
    ("output.schema.json",
     {k: v for k, v in SAMPLE_OUTPUT.items() if k != "spoken"},
     "spoken 누락"),
    # answer_draft: coverage_state=undefined → ⑥ 도달 불가 상태(enum defined/directive만)
    ("answer_draft.schema.json",
     {**SAMPLE_ANSWER_DRAFT, "coverage_state": "undefined"},
     "coverage_state=undefined"),
]


def main():
    ok = True
    print("=== A. 스키마 자체 유효성 (Draft 2020-12 check_schema) ===")
    for name, _ in POSITIVE:
        try:
            Draft202012Validator.check_schema(load(name))
            print(f"  [OK] {name}")
        except Exception as e:
            ok = False
            print(f"  [FAIL] {name}: {e}")

    print("\n=== B1. 양성 샘플 (통과해야 정상) ===")
    for name, sample in POSITIVE:
        v = Draft202012Validator(load(name))
        errors = sorted(v.iter_errors(sample), key=lambda e: e.path)
        if errors:
            ok = False
            print(f"  [FAIL] {name}: {errors[0].message}")
        else:
            print(f"  [OK] {name}  (샘플 통과)")

    print("\n=== B2. 음성 샘플 (거부돼야 정상) ===")
    for name, bad, label in NEGATIVE:
        v = Draft202012Validator(load(name))
        errors = list(v.iter_errors(bad))
        if errors:
            print(f"  [OK] {name}  거부됨 <- {label}")
        else:
            ok = False
            print(f"  [FAIL] {name}: '{label}' 인스턴스가 거부되지 않음")

    print("\n" + ("ALL PASSED ✅" if ok else "SOME FAILED ❌"))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
