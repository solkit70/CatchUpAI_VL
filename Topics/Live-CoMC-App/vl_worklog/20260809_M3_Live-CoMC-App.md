# WorkLog - M3: 데이터 계약과 안전 정책 스펙

**날짜**: 2026-08-09
**Topic**: Live-CoMC-App
**모듈**: M3 - 데이터 계약과 안전 정책 스펙
**학습 시간**: 2026-08-09 오전(05:24 시작). 개념 + 실습 1·2·3 전부 한 세션에 완료. ※ 아래 활동별 시각(05:30~ 등)은 승인된 계획의 시간 블록(추정)이며 실측 벽시계가 아님 — 실제로는 AI 보조로 설계·문서가 빠르게 진행돼 로드맵 예상 9h보다 훨씬 짧게 완료됨

---

## 🎯 오늘의 학습 목표

- [x] 개념: claim_map · coverage_state · 스키마 정규화 정리
- [x] 실습 1: 7종 JSON Schema 작성 + jsonschema 유효성 검사 통과
- [x] 실습 2: safety_policy.json 작성 (계획상 '착수'였으나 완료까지 진행)
- [x] 실습 3: LLM 3사 스키마 정규화 설계 (시간 여유로 같은 세션에서 완료)

---

## 📚 진행 내용

### 1. 개념 학습 — claim-evidence-model.md

**시간**: 05:30 – 06:30

**목적**: 7종 스키마를 왜 그렇게 설계하는지 근거를 먼저 확정한다.

**과정**:
1. M1 산출물(case-table, coverage-and-parts, forbidden-sections)과 M2 pipeline-diagram, M1·M2 WorkLog를 읽어 grounding
2. `claim_map`(문장별 근거 강제), `coverage_state` 3분류(defined/directive/undefined), 3사 스키마 정규화 어댑터 개념을 정리
3. 각 개념을 M2 9단계 파이프라인의 구체적 지점(⑤/⑥/⑦)에 박아 연결

**결과**: `concepts/claim-evidence-model.md`. "범위 판정(coverage)"과 "문장별 근거(claim_map)"가 별개 층위이며 둘 다 있어야 환각이 발화로 이어지지 않는다는 점을 명문화했다.

**메모/인사이트**: `coverage_state=undefined`가 "정보가 볼트에 있으니 적당히 말한다"가 아니라 "허용 범위가 없으면 침묵한다"를 기본값으로 만든다는 것이 M1의 커버리지 화이트리스트 개념과 정확히 맞물린다.

### 2. 실습 1 — 7종 JSON Schema 작성 + 유효성 검사

**시간**: 06:40 – 09:00

**목적**: M5~M8 구현의 계약을 미리 확정한다.

**과정**:
1. 7종 스키마를 파이프라인 단계에 1:1 대응해 작성: `rundown_index`(M1 파서 출력) · `broadcast_context`(⑤) · `session_state`(런타임) · `intent`(④) · `answer_draft`(⑥, claim_map) · `verdict`(⑦) · `output`(⑧⑨ 봉투)
2. 각 필드에 타입 + 1줄 한국어 설명, `additionalProperties: false`로 계약 엄격화
3. `validate.py`로 (A) 스키마 자체 유효성(`check_schema`), (B1) grounded 양성 샘플 통과, (B2) 위반 인스턴스 거부까지 3중 검사
4. 양성 샘플의 `rundown_index`에 M1 case-table 케이스 1~8을 parts로 모두 표현해, "M1 변동성이 스키마 필드로 표현 가능"함을 함께 실증

**결과**: `examples/schemas/` 7개 파일 + `examples/validate.py` → **ALL PASSED**. 음성 테스트 5종(claim_map 누락 / forbidden_removed=false / coverage_state 오탈자 / spoken 누락 / answer_draft coverage_state=undefined)이 모두 정상 거부됨을 확인.

**메모/인사이트**: 로드맵은 "overlay.json/spoken.json"을 7번째 한 슬롯으로 적었는데, 파이프라인상 ⑧⑨가 같은 `verdict.final_text`에서 **동시 출력**되므로 `output.schema.json` 하나의 봉투(overlay+spoken)로 묶어 정확히 7종을 유지했다. 이 설계 결정을 README에 명시.

### 3. 실습 2 — safety_policy.json 작성

**시간**: 09:00 – 09:35

**목적**: `live-broadcast` SKILL.md의 사람이 읽는 원칙을 코드가 로드·집행하는 규칙으로 번역한다.

**과정**:
1. SKILL.md(v1.2.0) 원본을 읽어 4대 원칙(추측 금지/최신성/상태 동기화/Vault≠오늘)을 규칙 ID로 분해
2. 모호성 3규칙(수량 불일치/커버리지 없음/완료 오인)을 `when`-`action`-`prompt`-`block_generation` 구조의 조건-액션 쌍으로 작성
3. 길이 하드컷(brief 3 / default 5 / detailed 7)을 트리거 문구와 함께 포함
4. 검증 규칙 5종(claim.evidence_required 등)을 stage·on_violation·llm_self_eval=false로 추가

**결과**: `examples/safety_policy.json` (principles 4 / ambiguity_rules 3 / length levels [3,5,7] / verification_rules 5). JSON 파싱 검증 통과. M8이 그대로 로드할 수 있는 형태.

### 4. 실습 3 — LLM 3사 스키마 정규화 설계

**시간**: 09:35 – 10:20 (시간 여유로 같은 세션에서 진행)

**목적**: M5에서 구현할 어댑터 계층을 문서로 먼저 확정한다.

**과정**:
1. Claude 구조화 출력 사양을 정확히 반영하려고 `claude-api` 스킬을 로드해 실측 확인 — ① Tool use(`input_schema`+`strict`+`tool_choice` 강제) ② 네이티브 `output_config.format`(구 `output_format`은 deprecated)
2. OpenAI(`response_format` json_schema strict) · Gemini(`responseSchema`, OpenAPI 서브셋) 방식과 3사 비교표 작성
3. 내부 스키마(`answer_draft.schema.json`)로의 필드 매핑표 + 스키마 제약 서브셋 차이 정리
4. 스키마 위반 시 재시도→폴백 흐름도(Mermaid) 작성, 전부 실패 시 HITL 통보로 귀결

**결과**: `guides/llm-schema-normalization.md`. 핵심 설계 결정 — 프로바이더에는 각 사가 받는 서브셋 스키마로 "대략 유도"하고, **진짜 합격/불합격 판정은 어댑터 뒤단의 `answer_draft.schema.json` 재검증**(M3 validate.py 재사용)에서 한다는 이중 구조를 명문화.

**메모/인사이트**: 3사 스키마 제약이 제각각(Claude 네이티브는 `minimum/minLength` 미지원, Gemini는 `additionalProperties` 무시)이라 "프로바이더 강제 스키마 = 최종 계약"으로 두면 깨진다. 검증을 프로바이더 밖 한 곳으로 몰아야 M2의 "게이트는 프로바이더 무관" 원칙이 실제로 성립함을 확인했다.

---

## 🐛 문제 해결 로그

### 문제 1: Windows 콘솔 cp1252에서 한글 print UnicodeEncodeError

**증상**: `validate.py` 첫 실행 시 검사 로직 진입 전 한글 print에서 `'charmap' codec can't encode` 오류.

**원인**: Windows Python 기본 stdout 인코딩이 cp1252.

**해결**: 1차로 `PYTHONIOENCODING=utf-8`로 재실행해 결과 확인. 이후 스크립트 상단에 `sys.stdout.reconfigure(encoding="utf-8")`를 추가해 재실행 시에도 항상 안전하도록 고정.

---

## 📊 DoD 체크리스트

로드맵 M3의 Definition of Done:

- [x] 7종 JSON Schema 전부 작성 및 유효성 검사 통과
- [x] `safety_policy.json`에 4대 원칙 + 모호성 3규칙 + 길이 하드컷 반영
- [x] LLM 3사 스키마 정규화 설계 문서 완성 (실습 3)
- [x] M1 케이스 표의 모든 변동성이 스키마 필드로 표현 가능함을 확인
- [x] README 작성 완료
- [x] WorkLog 작성 완료

**완료율**: 6/6 (100%) — M3 DoD 전체 달성

---

## 💡 Daily Retrospective

### What went well (잘된 점)
- 스키마를 추상적으로 짓지 않고 M2 9단계 파이프라인의 각 지점에 1:1로 못박아, 계약이 실제 데이터 흐름과 어긋날 여지를 줄였다
- 양성뿐 아니라 음성 테스트(위반 인스턴스 거부)까지 넣어, 계약이 "나쁜 데이터를 실제로 막는지"를 실증했다

### What could be improved (개선할 점)
- `output.schema.json`을 봉투로 묶은 것은 7종을 맞추기 위한 선택이기도 하다 — M9 오버레이 통합에서 overlay/spoken을 분리 폴링해야 하면 두 파일로 쪼갤 가능성을 열어둔다
- 날짜/시간 format은 annotation 수준으로만 검증했다(format-assertion 미적용). 런타임에서 date-time 강제가 필요하면 format checker 의존성을 추가해야 한다

### Insights (인사이트)
- `safety_policy.json`을 만들며, SKILL.md의 "확인 질문을 던진다"가 곧 `block_generation: true` + `hitl_ask`라는 걸 알았다 — 사람 원칙과 기계 규칙이 1:1로 맞아떨어지는 지점이 명확해졌다
- claim_map의 evidence_quote를 "부분 문자열 대조"로 검증한다는 계약 덕분에, M8 게이트가 LLM 없이도 구현 가능하다는 것이 스키마 수준에서 확정됐다

### Tomorrow's focus (다음에 할 것)
- **M4 - Wake Word / VAD 하네스** (⭐⭐⭐/7h) 시작 — openWakeWord 커스텀 호출어, Silero VAD 발화 종료, 3시간 환산 오탐률 실측, 에코 루프 차단
- M4는 실측 하네스 단계라 실제 오디오 녹음·측정이 필요 — 마이크/스피커 환경 준비 필요. M3 설계(안전 정책·스키마)는 M5~M8에서 소비되니 그때 재확인

---

## 🧭 Module Retrospective (M3 완료)

### 계획 대비 실제
- 계획: 오늘 개념 + 실습 1 완료 + 실습 2 착수. 실제: **개념 + 실습 1·2·3 전부 완료** — M3 한 세션 완주. 로드맵 예상 9h(사람 기준)보다 훨씬 빠르게 끝났는데, 스키마를 M1·M2 산출물에서 역산했고 설계·문서 중심이라 실행 대기가 없었기 때문(AI 보조 진행).

### 핵심 학습 내용
- "범위 판정(coverage_state)"과 "문장별 근거(claim_map)"는 별개 층위이며 둘 다 있어야 환각이 발화로 안 이어진다.
- 검증은 규칙(문자열 대조)이지 LLM 자기평가가 아니다 → M8 게이트가 LLM 없이 구현 가능함이 스키마 수준에서 확정.
- 3사 구조화 출력 제약이 제각각이라, 검증을 프로바이더 밖 한 곳(`answer_draft.schema.json` 재검증)으로 몰아야 "게이트는 프로바이더 무관" 원칙이 실제로 성립.

### 발생한 문제와 해결
- Windows cp1252 한글 print 오류 → `sys.stdout.reconfigure(utf-8)`로 스크립트에 영구 고정.
- 로드맵의 "overlay/spoken 7종" 표기 모호 → ⑧⑨ 동시 출력 특성을 반영해 `output.schema.json` 봉투 1개로 7종 유지(설계 결정 명문화).

### Roadmap 정확도 평가
- 실습 구성·DoD는 정확했음. 다만 시간 추정(9h, 사람 기준)이 실제 소요보다 크게 컸다 — 설계형 모듈은 실행 대기가 없고 AI 보조라 빠르게 완료. M4~M6 실측 하네스는 반대로 측정·녹음 대기가 생겨 추정이 더 맞거나 초과할 가능성.

### 다음 모듈 준비사항
- M4(Wake Word/VAD)는 실측 단계 — `openwakeword`·`silero-vad` 설치, 마이크/스피커, 3시간 환산 오탐률용 30분 녹음 환경 필요.

## 📎 참조 및 산출물

**생성된 파일/폴더**:
- `03-Data-Contracts-and-Safety/concepts/claim-evidence-model.md`: 핵심 개념 3종
- `03-Data-Contracts-and-Safety/examples/schemas/` (7개): rundown_index, broadcast_context, session_state, intent, answer_draft, verdict, output
- `03-Data-Contracts-and-Safety/examples/validate.py`: 스키마 유효성 + 양성/음성 샘플 검사
- `03-Data-Contracts-and-Safety/examples/safety_policy.json`: 4대 원칙 + 모호성 3규칙 + 길이 하드컷 + 검증 규칙 5종
- `03-Data-Contracts-and-Safety/guides/llm-schema-normalization.md`: 3사 Structured Output 비교표 + 내부 스키마 매핑 + 재시도→폴백 흐름도
- `03-Data-Contracts-and-Safety/README.md`: 모듈 개요·스키마↔파이프라인 대응표

**참조 자료**:
- `_Settings_/Skills/live-broadcast/SKILL.md` (v1.2.0): 4대 원칙·모호성 3규칙·길이 하드컷 원본
- M1: `01-Concept-and-Rundown-Contract/examples/case-table.md` (변동성 케이스), `guides/forbidden-sections.md`
- M2: `02-Architecture-and-Boundary/concepts/pipeline-diagram.md` (단계별 데이터)
- [JSON Schema 공식 문서](https://json-schema.org/)

**다음 세션 준비사항**:
- M4(Wake Word/VAD)는 실측 하네스 — `openwakeword`·`silero-vad` 설치, 마이크/스피커, 3시간 환산 오탐률 측정용 30분 녹음 환경 준비

---

**작성자**: solkit70
**방법론**: VibeLearn AI
