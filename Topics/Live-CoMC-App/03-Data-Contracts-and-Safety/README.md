# M3 — 데이터 계약과 안전 정책 스펙

**상태**: ✅ 완료 (실습 1·2·3, DoD 6/6)
**예상 학습 시간**: 9h
**Topic**: [[../topic_starter|Live-CoMC-App]]

---

## 이 모듈에서 배우는 것

M1(파싱 계약)·M2(파이프라인)에서 확정한 개념을, 런타임 데이터가 지나가는 **7개 관문의 JSON 계약**과 **기계 집행 가능한 안전 정책**으로 번역한다. 근거 없는 발화를 구조적으로 차단하는 `claim_map`, 발화 허용 범위를 판정하는 `coverage_state`, 3사 LLM 출력을 흡수하는 정규화가 핵심이다.

## 문서 목록 (학습 순서)

1. [concepts/claim-evidence-model.md](concepts/claim-evidence-model.md) — claim_map(문장별 근거 강제) · coverage_state 3분류 · 스키마 정규화의 개념과 근거
2. [examples/schemas/](examples/schemas/) — 7종 JSON Schema (파이프라인 ④~⑨ + 소스). 각 스키마는 M2 9단계의 특정 지점에 대응
3. [examples/validate.py](examples/validate.py) — 7종 스키마 유효성 + grounded 양성/음성 샘플 검사 (`python validate.py`)
4. [examples/safety_policy.json](examples/safety_policy.json) — `live-broadcast` 스킬 4대 원칙 + 모호성 3규칙 + 길이 하드컷(3/5/7)을 코드가 로드 가능한 규칙으로 번역
5. [guides/llm-schema-normalization.md](guides/llm-schema-normalization.md) — LLM 3사(OpenAI/Claude/Gemini) Structured Output 비교표 + 내부 스키마 매핑 + 재시도→폴백 흐름도

## 7종 스키마 ↔ 파이프라인 대응

| 스키마 | 파이프라인 단계 | 역할 |
|---|---|---|
| `rundown_index.schema.json` | 소스 (M1 파서 출력) | 파트/커버리지/금칙·조건부 섹션 구조화 |
| `broadcast_context.schema.json` | ⑤ 컨텍스트 조립 | 화이트리스트 + 근거 풀, 금칙 제거 단언 |
| `session_state.schema.json` | 런타임 공유 | wake 게이트·활성 프로바이더·잔여 시간 |
| `intent.schema.json` | ④ Intent 분류 | 의도·슬롯·모호성 플래그 |
| `answer_draft.schema.json` | ⑥ LLM 응답 | 문장 배열 + claim_map (근거 강제) |
| `verdict.schema.json` | ⑦ 검증 게이트 | 통과/탈락 문장 + 위반 기록 |
| `output.schema.json` | ⑧⑨ 오버레이+TTS | 동시 출력 봉투 |

**설계 결정**: 파이프라인의 ⑧ overlay·⑨ spoken은 같은 `verdict.final_text`에서 동시 출력되므로 하나의 봉투 스키마(`output.schema.json`)로 묶어 로드맵의 "7종"을 유지했다.

## 핵심 결론 (다음 모듈로 넘어가는 것)

- **claim_map = 안전장치 근간**: 검증 게이트(⑦)는 각 문장의 `evidence_quote`가 `evidence_pool`에 실제 존재하는지 문자열 대조로만 판정한다(LLM 자기평가 아님) — M8 게이트 구현의 계약
- **coverage_state=undefined는 차단 신호**: 커버리지 줄이 없으면 생성 자체를 막고 HITL로 되묻는다. M1 실측상 undefined 실물 빈도 0이므로 과도한 엔지니어링은 피한다
- **safety_policy.json은 M8이 그대로 로드**: 규칙 추가는 이 파일에 규칙 객체를 더하는 방식으로 확장
- **정규화 어댑터로 검증 게이트는 프로바이더 무관**: 3사 구조화 출력을 각 사 서브셋으로 유도하되, **진짜 계약 강제는 어댑터 뒤단의 `answer_draft.schema.json` 재검증**에서 한다(이중 구조로 3사 제약 차이 흡수) — M5 어댑터 구현 기준

## 검증 방법

```
cd 03-Data-Contracts-and-Safety/examples
python validate.py   # A: 스키마 자체 유효 / B1: 양성 샘플 통과 / B2: 위반 샘플 거부 → ALL PASSED
```

## 다음 모듈

→ M4 - Wake Word / VAD 하네스 (`04-WakeWord-VAD-Harness/`) — M3 완료(DoD 6/6), 실측 하네스 단계 시작

← 이전: [M2 - 파이프라인 아키텍처와 App Boundary](../02-Architecture-and-Boundary/README.md)
