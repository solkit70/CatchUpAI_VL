# Live-CoMC-App 학습 로드맵

**생성일**: 2026-08-02
**방법론**: VibeLearn AI
**버전**: 1.0

---

## 📊 학습 기간 적정성 분석

**사용자 입력 기간**: 약 3개월 — 12주 (주당 7~8시간, 총 약 90시간)
**Topic 복잡도**: 복잡 — 실시간 음성 파이프라인(Wake Word/VAD/STT/LLM/TTS) + 3사 LLM·4사 TTS 멀티 프로바이더 추상화 + Electron 데스크톱 앱 + 되돌릴 수 없는 라이브 방송 환경의 안전장치 설계
**권장 기간**: 1~3개월

**분석 결과**: ✅ **적정함**(권장 범위 상한). 원래 추정치(6~8주/59시간, 7모듈)도 이미 권장 범위 안이었으나, 2026-08-02 HITL-1에서 사용자가 "완성도 우선" 방침에 맞춰 상한인 3개월을 선택했다. 이에 따라 아래처럼 재구성했다:
- 원 M4(음성 I/O 하네스, 10h 단일 모듈)를 **3개 모듈로 분리**(Wake/VAD, STT+LLM, TTS+오디오 라우팅)해 각 프로바이더군을 개별 검증
- 원 M5(엔진 POC, 13h)에서 **안전 검증 게이트를 별도 모듈로 분리**해 시나리오를 5개→더 확장 가능하게 함
- M9(데스크톱 셸)과 M10(리허설)에 여유 시간을 추가해 실제 방송 투입 전 안정성을 높임

**조치 제안**: 계획대로 10모듈 / 90시간으로 진행한다. M7(엔진 POC, 16h)이 최대 단일 모듈이므로 `app-boundary.md`(M2 산출물)를 하드 게이트로 유지한다.

---

## 📚 학습 개요

### Topic 소개

매주 일요일 3시간 라이브 방송(AI in Action Live)을 함께 진행할 로컬 데스크톱 보조 MC 앱을 만드는 프로젝트형 Topic이다. 진행자가 호출어로 깨워 목소리로 지시하면, 이 앱이 매주 축적되는 방송 문서(Rundown, Daily Roundup, Weekly Progress, Weekly Dashboard)를 읽고 화면 텍스트 + 음성으로 공동 MC처럼 방송을 진행한다.

### 학습 목표

- [ ] 매주 형식이 조금씩 달라지는 Rundown 문서를 안정적으로 파싱하는 계약(스키마)을 설계할 수 있다
- [ ] 근거 없는 발화를 구조적으로 차단하는 안전 검증 파이프라인(Claim-Evidence 강제, 커버리지 화이트리스트)을 구현할 수 있다
- [ ] Wake Word → VAD → STT → LLM → TTS로 이어지는 실시간 음성 파이프라인을 직접 구현할 수 있다
- [ ] LLM(OpenAI/Claude/Gemini)과 TTS(Edge-TTS/Qwen3-TTS/OpenAI/ElevenLabs)를 프로바이더 교체 가능한 구조로 추상화할 수 있다
- [ ] Electron 셸 + Python 사이드카로 데스크톱 앱을 만들고 OBS와 연동할 수 있다
- [ ] 실제 방송 환경에서 리허설을 거쳐 라이브 투입 가능 여부를 스스로 판단할 수 있다

### 예상 학습 기간

약 3개월 — 12주 (주당 7~8시간, 총 약 90시간)

### 학습 환경

- **OS**: Windows 11 — i7-1355U (15W), 16GB RAM, GPU 없음 (클라우드 API 우선)
- **도구**: VS Code(Claude Code + Codex Extension), Python 3.13, Node.js 22/Electron, ffmpeg, OpenAI/Anthropic/Google Gemini API, Edge-TTS/Qwen3-TTS/OpenAI TTS/ElevenLabs, OBS Studio(VoiceMeeter Banana, VB-CABLE)
- **사전 지식**: Python 파일·JSON 처리, Markdown 구조 파싱, VS Code 기본 사용 (권장: Vibe-Guiding-VSCode Topic, Node/Electron 기초, 실시간 오디오 개념)

---

## 🗺️ 전체 로드맵 구조

| 모듈 | 모듈명 | 난이도 | 예상 시간 | 산출물 폴더 |
|------|--------|--------|----------|------------|
| M1 | 개념 정의와 Rundown 파싱 계약 | ⭐⭐ | 6h | `01-Concept-and-Rundown-Contract/` |
| M2 | 파이프라인 아키텍처와 App Boundary 확정 | ⭐⭐ | 7h | `02-Architecture-and-Boundary/` |
| M3 | 데이터 계약과 안전 정책 스펙 | ⭐⭐ | 9h | `03-Data-Contracts-and-Safety/` |
| M4 | Wake Word / VAD 하네스 | ⭐⭐⭐ | 7h | `04-WakeWord-VAD-Harness/` |
| M5 | STT + 멀티 LLM 하네스 | ⭐⭐⭐ | 8h | `05-STT-LLM-Harness/` |
| M6 | 멀티 TTS 하네스 + 오디오 라우팅 | ⭐⭐⭐ | 7h | `06-TTS-Audio-Routing-Harness/` |
| M7 | Co-MC 엔진 POC (파일 기반 6단계) | ⭐⭐⭐ | 16h | `07-CoMC-Engine-POC/` |
| M8 | 안전 검증 게이트 심화 & 시나리오 확장 | ⭐⭐⭐ | 8h | `08-Safety-Gate-Scenarios/` |
| M9 | 데스크톱 셸 + OBS 오버레이 통합 | ⭐⭐⭐ | 12h | `09-Desktop-Shell-and-Overlay/` |
| M10 | 리허설 검증과 라이브 Demo (Capstone) | ⭐⭐⭐ | 10h | `10-Live-Rehearsal-Capstone/` |

**총 예상 시간**: 90시간

**리듬**: M1~M3 설계(22h, 24%) → M4~M6 실측 하네스(22h, 24%) → M7~M8 구현(24h, 27%) → M9 통합(12h, 13%) → M10 검증·Capstone(10h, 11%)

---

## 📖 모듈별 상세 계획

### M1 - 개념 정의와 Rundown 파싱 계약

**난이도**: ⭐⭐
**예상 시간**: 6h
**산출물 폴더**: `01-Concept-and-Rundown-Contract/`

#### 학습 목표
- [ ] 공동 MC 앱의 핵심 개념(Wake Word, 커버리지, Claim-Evidence)을 남에게 설명할 수 있다
- [ ] `AI/Roundup/` 4종 문서(Rundown, Daily Roundup, Weekly Progress, Dashboard)의 관계를 그림으로 그릴 수 있다
- [ ] Rundown의 파트 헤딩·커버리지 줄 정규식을 실제 문서 2개에 대입해 검증할 수 있다
- [ ] "말해도 되는 것"과 "말하면 안 되는 것" 섹션을 케이스 표로 분류할 수 있다

#### 주요 개념
1. **커버리지 줄(Coverage Line)**: 방송에서 실제로 말할 항목만 `①②③`으로 명시한 blockquote 한 줄. 파트 본문 전체가 아니라 이 줄만이 발화 허용 범위다.
2. **파트(Part)**: `## N부: 제목 (시간)` 헤딩으로 구분된 방송 구간. 개수·이름·시간 표기가 매주 달라진다.
3. **Rundown 정본 원칙**: `.md`가 정본이고 `.canvas`는 시각화 사본이라 표기가 다를 수 있다. 파서는 md만 신뢰한다.
4. **status: 최종본**: Rundown frontmatter의 이 값이 방송 투입 가능 여부의 1차 신호다.

#### 실습 과제

**실습 1: 4종 문서 관계 지도 그리기** ⭐
- **목적**: 앱이 참조할 문서 생태계를 눈으로 확인한다
- **단계**:
  1. `AI/Roundup/2026-07-26 - Live21 Weekly Rundown.md`의 frontmatter `links:`를 확인한다
  2. 그 링크가 가리키는 Daily Roundup·Weekly Progress·Dashboard 파일을 모두 연다
  3. 4종 문서의 관계를 Mermaid 다이어그램으로 그린다
- **예상 시간**: 60분
- **검증**: `01-Concept-and-Rundown-Contract/concepts/document-map.md`에 다이어그램 존재

**실습 2: 파트 헤딩·커버리지 정규식 대조** ⭐⭐
- **목적**: 문서 변동성이 실제로 어느 정도인지 손으로 확인한다
- **단계**:
  1. Live20과 Live21 Rundown을 나란히 열어 `## N부:` 헤딩 형식을 비교한다
  2. 커버리지 줄 3가지 형태(정의됨/미정/운영지시문 첨부)를 각각 찾아 인용한다
  3. `4.5부` 같은 소수 파트, `나머지 전부`/`시간 미정` 같은 자유형 시간을 찾아 표로 정리한다
- **예상 시간**: 90분
- **검증**: `case-table.md`에 두 회차 대조표 완성, 최소 6개 케이스 등재

**실습 3: 금칙 섹션 목록화** ⭐⭐
- **목적**: 안전장치 1(컨텍스트 진입 차단)의 입력이 될 목록을 만든다
- **단계**:
  1. Rundown에서 `## 보류된 인사이트 후보`, `## 주간 영상 후보`, `### 대기 목록` 섹션을 모두 찾는다
  2. 각 섹션이 왜 발화되면 안 되는지 1줄로 근거를 쓴다
  3. `forbidden-sections.md`로 정리한다
- **예상 시간**: 45분
- **검증**: 최소 3종 금칙 섹션 패턴 확보

#### 산출물
```
01-Concept-and-Rundown-Contract/
├── README.md
├── concepts/
│   ├── document-map.md
│   └── coverage-and-parts.md
├── examples/
│   └── case-table.md
└── guides/
    └── forbidden-sections.md
```

#### Definition of Done
- [ ] 문서 관계 지도 완성 (Mermaid)
- [ ] 파트 헤딩·커버리지 정규식이 Live20·Live21 두 회차 모두에서 검증됨
- [ ] 금칙 섹션 패턴 3종 이상 확보
- [ ] `case-table.md`에 최소 6개 변동성 케이스 등재
- [ ] README 작성 완료
- [ ] WorkLog 작성 완료

#### Self-Assessment
**개념 이해** (5분):
- [ ] 커버리지 줄과 파트 본문의 차이를 1문장으로 설명 가능
- [ ] `.canvas`를 파싱 대상에서 제외하는 이유를 설명 가능

**실무 활용** (5분):
- [ ] 새 회차 Rundown이 와도 같은 정규식이 통할지 판단 가능

#### 예상 시간 배분
- 개념 학습: 60분 (17%)
- 실습 1: 60분
- 실습 2: 90분
- 실습 3: 45분
- 문서화: 45분
- **합계**: 6h (버퍼 20% 포함)

#### 참조 자료
- [`AI/Roundup/2026-07-26 - Live21 Weekly Rundown.md`]: 파서 검증 1차 대상
- [`_Settings_/Skills/rundown-writer/SKILL.md`]: 커버리지 줄 작성 규약 원본

---

### M2 - 파이프라인 아키텍처와 App Boundary 확정

**난이도**: ⭐⭐
**예상 시간**: 7h
**산출물 폴더**: `02-Architecture-and-Boundary/`

#### 학습 목표
- [ ] Wake Word부터 TTS 출력까지 6단계 파이프라인을 다이어그램으로 그릴 수 있다
- [ ] 각 컴포넌트의 "절대 하지 말아야 할 일"을 명시적으로 나열할 수 있다
- [ ] MVP 포함/제외 범위를 문서(`app-boundary.md`)로 확정할 수 있다
- [ ] Electron+Python 하이브리드 구조를 선택한 이유를 대안과 비교해 설명할 수 있다

#### 주요 개념
1. **App Boundary**: 첫 버전에서 반드시 뺄 기능의 목록과 이유. Vibe-Guiding-VSCode의 `poc-boundary.md`를 본뜬 안전장치.
2. **Electron 셸 + Python 사이드카**: UI·핫키·안전은 Electron이, 파싱·LLM 호출은 Python이 맡는 프로세스 분리 구조.
3. **wake word 이후에만 동작**: 3시간 내내 클라우드 STT를 스트리밍하지 않는다는 비용·안정성 원칙.

#### 실습 과제

**실습 1: 파이프라인 다이어그램 작성** ⭐
- **목적**: 전체 데이터 흐름을 한 장으로 정리한다
- **단계**:
  1. Wake→VAD→STT→Intent→Context→LLM→Verify→Overlay/TTS 9단계를 나열한다
  2. 각 화살표에 무슨 데이터가 흐르는지 적는다
  3. Mermaid로 그린다
- **예상 시간**: 60분
- **검증**: `pipeline-diagram.md` 완성

**실습 2: app-boundary.md 작성** ⭐⭐⭐
- **목적**: 범위 팽창을 막는 하드 게이트를 만든다
- **단계**:
  1. 포함 범위 11개 항목을 표로 정리한다 (M1~M10 산출물과 매핑)
  2. 제외 범위 11개 항목과 각각의 이유를 표로 정리한다 (RAG 영구 제외, barge-in 영구 제외 등)
  3. "이 표에 없는 기능 요청이 오면 v2로 미룬다"는 원칙을 README에 명시한다
- **예상 시간**: 120분
- **검증**: 승인된 설계안(`ethereal-puzzling-seahorse.md`)의 MVP 경계 표와 대조해 누락 없음 확인

**실습 3: 기술 선택 비교표 작성** ⭐⭐
- **목적**: Electron vs Tauri vs 순수 Python 결정을 근거로 남긴다
- **단계**:
  1. 볼트 파일 접근·오디오 I/O·OBS 연동·개발 속도 4개 기준으로 비교표를 만든다
  2. Electron 채택, Tauri 기각 사유를 각 2문장으로 쓴다
- **예상 시간**: 60분
- **검증**: `tech-choice.md`에 비교표와 결론 존재

#### 산출물
```
02-Architecture-and-Boundary/
├── README.md
├── concepts/
│   └── pipeline-diagram.md
├── guides/
│   ├── app-boundary.md      ← 하드 게이트 (M7·M9 팽창 억제용)
│   └── tech-choice.md
```

#### Definition of Done
- [ ] 9단계 파이프라인 다이어그램 완성
- [ ] `app-boundary.md`에 포함 11개 + 제외 11개 항목 전부 등재
- [ ] 기술 선택 비교표 완성 (Electron 채택 근거 명시)
- [ ] "컴포넌트별 절대 하지 말아야 할 일" 목록 작성
- [ ] README 작성 완료
- [ ] WorkLog 작성 완료

#### Self-Assessment
**개념 이해**:
- [ ] Electron+Python 사이드카 구조를 채택한 이유를 설명 가능
- [ ] RAG를 영구 제외한 이유를 커버리지 원칙과 연결해 설명 가능

**실무 활용**:
- [ ] 새 기능 요청이 왔을 때 `app-boundary.md`로 즉시 포함/제외 판단 가능

#### 예상 시간 배분
- 개념 학습: 60분 (14%)
- 실습 1: 60분
- 실습 2: 120분
- 실습 3: 60분
- 문서화: 60분
- **합계**: 7h (버퍼 20% 포함)

#### 참조 자료
- [`Topics/Vibe-Guiding-VSCode/02-Architecture-Design/poc-boundary.md`]: App Boundary 문서의 직접 템플릿
- [`ethereal-puzzling-seahorse.md`]: 승인된 설계안 원본 (MVP 경계·리스크 표 포함)

---

### M3 - 데이터 계약과 안전 정책 스펙

**난이도**: ⭐⭐
**예상 시간**: 9h
**산출물 폴더**: `03-Data-Contracts-and-Safety/`

#### 학습 목표
- [ ] 7종 중간 JSON(`rundown_index`~`spoken`)의 스키마를 정의할 수 있다
- [ ] `live-broadcast` 스킬의 4대 원칙과 모호성 3규칙을 기계 검증 가능한 규칙으로 번역할 수 있다
- [ ] `claim_map` 구조로 문장별 근거를 강제하는 스키마를 설계할 수 있다
- [ ] LLM 3사(OpenAI/Claude/Gemini) 간 Structured Output 방식 차이를 흡수하는 정규화 전략을 설명할 수 있다

#### 주요 개념
1. **claim_map**: 생성된 문장마다 `{sentence_idx, evidence_path, evidence_quote}`를 강제하는 필드. 안전장치의 근간.
2. **coverage_state**: `defined`/`undefined`/`directive` 3분류. `undefined`는 응답 생성 자체를 차단하는 신호.
3. **스키마 정규화**: OpenAI(JSON Schema)·Claude(Tool use)·Gemini(responseSchema) 세 가지 방식이 같은 최종 JSON을 내도록 흡수하는 어댑터 계층.

#### 실습 과제

**실습 1: 7종 JSON 스키마 초안 작성** ⭐⭐
- **목적**: M5~M8 구현의 계약을 미리 확정한다
- **단계**:
  1. `rundown_index.json`, `broadcast_context.json`, `session_state.json`, `intent.json`, `answer_draft.json`, `verdict.json`, `overlay.json`/`spoken.json` 7종을 JSON Schema로 정의한다
  2. 각 필드에 타입과 1줄 설명을 붙인다
  3. M1의 케이스 표(4.5부, 미정 커버리지 등)가 스키마로 표현 가능한지 검증한다
- **예상 시간**: 180분
- **검증**: 7종 스키마 파일이 `jsonschema` 라이브러리로 유효성 검사를 통과

**실습 2: safety_policy.json 작성** ⭐⭐⭐
- **목적**: SKILL.md의 원칙을 코드가 읽을 수 있는 규칙으로 바꾼다
- **단계**:
  1. 4대 원칙(추측 금지/최신성/상태 동기화/Vault≠오늘)을 각각 규칙 ID로 나눈다
  2. 모호성 3규칙(수량 불일치/커버리지 없음/완료 오인)을 조건-액션 쌍으로 작성한다
  3. 길이 하드컷(3/5/7문장) 값을 포함한다
- **예상 시간**: 120분
- **검증**: `safety_policy.json`이 M8 실습에서 그대로 로드되어 사용됨

**실습 3: LLM 프로바이더 스키마 정규화 설계** ⭐⭐⭐
- **목적**: M5에서 실제로 구현할 어댑터의 설계를 먼저 문서로 확정한다
- **단계**:
  1. OpenAI `response_format`, Claude tool use, Gemini `responseSchema` 3방식의 샘플 요청을 각각 작성한다
  2. 세 응답이 같은 내부 스키마로 매핑되는 변환 규칙을 표로 정리한다
  3. 스키마 위반 시 재시도→폴백 순서를 흐름도로 그린다
- **예상 시간**: 90분
- **검증**: `llm-schema-normalization.md`에 3사 비교표 + 폴백 흐름도

#### 산출물
```
03-Data-Contracts-and-Safety/
├── README.md
├── concepts/
│   └── claim-evidence-model.md
├── examples/
│   ├── schemas/  (rundown_index.schema.json 등 7개)
│   └── safety_policy.json
└── guides/
    └── llm-schema-normalization.md
```

#### Definition of Done
- [ ] 7종 JSON Schema 전부 작성 및 유효성 검사 통과
- [ ] `safety_policy.json`에 4대 원칙 + 모호성 3규칙 + 길이 하드컷 반영
- [ ] LLM 3사 스키마 정규화 설계 문서 완성
- [ ] M1 케이스 표의 모든 변동성이 스키마 필드로 표현 가능함을 확인
- [ ] README 작성 완료
- [ ] WorkLog 작성 완료

#### Self-Assessment
**개념 이해**:
- [ ] `claim_map`이 왜 안전장치의 근간인지 설명 가능
- [ ] `coverage_state: undefined`가 왜 차단 신호인지 설명 가능

**실무 활용**:
- [ ] 새 안전 규칙이 추가될 때 `safety_policy.json`에 규칙을 추가하는 방법을 알고 있다

**문제 해결**:
- [ ] 스키마 검증 실패 시 어느 프로바이더로 폴백할지 흐름도로 답할 수 있다

#### 예상 시간 배분
- 개념 학습: 90분 (17%)
- 실습 1: 180분
- 실습 2: 120분
- 실습 3: 90분
- 문서화: 60분
- **합계**: 9h (버퍼 20% 포함)

#### 참조 자료
- [`_Settings_/Skills/live-broadcast/SKILL.md`]: 4대 원칙·모호성 3규칙 원본
- [JSON Schema 공식 문서](https://json-schema.org/): 스키마 정의 표준

---

### M4 - Wake Word / VAD 하네스

**난이도**: ⭐⭐⭐
**예상 시간**: 7h
**산출물 폴더**: `04-WakeWord-VAD-Harness/`

#### 학습 목표
- [ ] openWakeWord로 커스텀 호출어 감지를 구현할 수 있다
- [ ] Silero VAD로 발화 종료를 800ms 무음 기준으로 판정할 수 있다
- [ ] 3시간 환산 오탐률을 실측하고 기준치 초과 여부를 판단할 수 있다
- [ ] TTS 재생 중 wake 게이트를 닫아 에코 루프를 차단할 수 있다

#### 주요 개념
1. **오탐(False Positive)**: 호출어를 말하지 않았는데 깨어나는 것. 3시간 환산 수치로 측정해야 방송 리스크를 가늠할 수 있다.
2. **에코 루프**: TTS가 자기 음성을 마이크로 다시 들어 wake word로 오인하는 무한 루프. 방송 사고의 대표 원인.
3. **VAD 무음 임계값**: 발화가 끝났다고 판정하는 무음 지속 시간. 너무 짧으면 문장 중간에 끊기고, 너무 길면 반응이 느려진다.

#### 실습 과제

**실습 1: openWakeWord 설치와 커스텀 호출어 테스트** ⭐⭐
- **목적**: 방송에서 절대 자연 발화하지 않을 호출어를 찾는다
- **단계**:
  1. `openwakeword` 설치, 기본 모델로 동작 확인
  2. 후보 호출어 3개("코엠씨" 등)를 정하고 각각 10회 발화 테스트
  3. `wake_probe.py`로 감지 지연(ms)을 `probe_log.jsonl`에 기록
- **예상 시간**: 120분
- **검증**: 3개 후보 중 오탐 0회인 것이 최소 1개 확보됨

**실습 2: Silero VAD 발화 구간 검출** ⭐⭐
- **목적**: STT로 넘길 발화 구간을 정확히 잘라낸다
- **단계**:
  1. `silero-vad` 설치 후 800ms 무음 기준 발화 종료 판정 구현
  2. 짧은 발화("3부 시작")와 긴 발화(5문장 질문)로 각각 테스트
  3. 결과를 `vad_probe.py` → `probe_log.jsonl`에 기록
- **예상 시간**: 90분
- **검증**: 두 발화 유형 모두 종료 시점이 육안 판단과 500ms 이내로 일치

**실습 3: 3시간 환산 오탐률 실측** ⭐⭐⭐
- **목적**: 실제 방송 환경(BGM·타이핑 소리 포함)에서의 리스크를 수치화한다
- **단계**:
  1. 30분간 일반 작업(타이핑, 잡담, 배경음악)을 하며 wake word 감지를 로깅한다
  2. 오탐 횟수를 3시간으로 환산한다
  3. 임계치(예: 3시간당 2회 이하)와 비교해 판정한다
- **예상 시간**: 60분(녹음 30분 + 분석 30분)
- **검증**: `false-positive-report.md`에 환산 수치와 판정 결과 기록

**실습 4: 에코 루프 차단 검증** ⭐⭐⭐
- **목적**: TTS 재생 중 wake 게이트가 실제로 닫히는지 확인한다
- **단계**:
  1. TTS 음성 재생 중 동시에 호출어를 스피커로 재생한다
  2. wake word 감지기가 이 기간 동안 게이트 폐쇄 상태인지 로그로 확인한다
  3. 재생 종료 후 게이트가 다시 열리는 지연을 측정한다
- **예상 시간**: 45분
- **검증**: TTS 재생 중 wake 이벤트 0건, 재생 종료 후 500ms 이내 게이트 재개방

#### 산출물
```
04-WakeWord-VAD-Harness/
├── README.md
├── examples/
│   ├── wake_probe.py
│   ├── vad_probe.py
│   └── probe_log.jsonl
├── guides/
│   └── false-positive-report.md
└── troubleshooting/
    └── echo-loop-notes.md
```

#### Definition of Done
- [ ] openWakeWord로 오탐 0회 호출어 최소 1개 확보
- [ ] Silero VAD 발화 종료 판정이 육안 판단과 500ms 이내 일치
- [ ] 3시간 환산 오탐률 실측 및 임계치 판정 완료
- [ ] TTS 재생 중 wake 이벤트 0건 검증 (에코 루프 차단)
- [ ] README 작성 완료
- [ ] WorkLog 작성 완료

#### Self-Assessment
**개념 이해**:
- [ ] 에코 루프가 왜 방송 사고로 이어지는지 설명 가능

**실무 활용**:
- [ ] 오탐률이 기준치를 넘으면 어떤 대안(핫키 전용 전환)으로 갈지 판단 가능

**문제 해결**:
- [ ] wake word가 감지되지 않을 때 어디부터 디버깅할지 순서를 말할 수 있다

#### 예상 시간 배분
- 개념 학습: 45분 (11%)
- 실습 1: 120분
- 실습 2: 90분
- 실습 3: 60분
- 실습 4: 45분
- 문서화: 60분
- **합계**: 7h (버퍼 20% 포함)

#### 참조 자료
- [openWakeWord](https://github.com/dscripka/openWakeWord): 커스텀 호출어 학습·감지
- [Silero VAD](https://github.com/snakers4/silero-vad): 경량 VAD 모델
- [`Topics/Qwen3-TTS/03-Setup-API/harness/connection_probe.py`]: probe 스크립트 패턴 선례

---

### M5 - STT + 멀티 LLM 하네스

**난이도**: ⭐⭐⭐
**예상 시간**: 8h
**산출물 폴더**: `05-STT-LLM-Harness/`

#### 학습 목표
- [ ] GPT-Live-Transcribe로 한국어 발화를 실시간 전사하고 WER을 실측할 수 있다
- [ ] STT 3단 폴백(Live-Transcribe → Transcribe → 로컬 whisper)을 구현할 수 있다
- [ ] OpenAI/Claude/Gemini 3사 LLM을 공통 인터페이스로 호출할 수 있다
- [ ] 3사 API 키 유효성을 사전에 확인하고, 실패한 프로바이더를 MVP에서 제외 판단할 수 있다

#### 주요 개념
1. **WER(Word Error Rate)**: 전사 오류율. 공개 수치는 영어 기준이 많아 한국어는 반드시 재측정해야 한다.
2. **LLMProvider 어댑터**: `complete()`/`stream()`/`cost_per_1k_tokens` 공통 인터페이스로 3사를 갈아 끼우는 구조.
3. **소비자 구독 ≠ API 접근권**: ChatGPT Plus·Claude Pro 구독은 API 키와 별개로 과금된다.

#### 실습 과제

**실습 1: GPT-Live-Transcribe 한국어 WER 실측** ⭐⭐
- **목적**: 공개 WER이 아니라 실제 조건에서의 정확도를 확인한다
- **단계**:
  1. 진행자 본인 목소리로 20개 발화 샘플(질문형·명령형 각 10개)을 녹음한다
  2. GPT-Live-Transcribe로 전사하고 정답과 대조해 WER을 계산한다
  3. BGM이 섞인 조건에서 동일 테스트를 반복한다
- **예상 시간**: 120분
- **검증**: `stt-wer-report.md`에 조건별 WER 수치 기록

**실습 2: STT 3단 폴백 구현** ⭐⭐⭐
- **목적**: 클라우드 장애 시에도 방송이 끊기지 않게 한다
- **단계**:
  1. `stt_probe.py`에 GPT-Live-Transcribe → GPT-Transcribe → 로컬 faster-whisper 순서로 폴백 로직을 구현한다
  2. 첫 번째 프로바이더를 강제로 실패시켜 폴백이 동작하는지 확인한다
  3. 각 단계의 지연을 `probe_log.jsonl`에 기록한다
- **예상 시간**: 90분
- **검증**: 강제 실패 시 자동으로 다음 단계로 전환됨을 로그로 확인

**실습 3: LLMProvider 어댑터 구현** ⭐⭐⭐
- **목적**: M3에서 설계한 정규화 전략을 코드로 구현한다
- **단계**:
  1. `LLMProvider` 추상 클래스와 OpenAI/Claude/Gemini 3개 구현체를 작성한다
  2. 동일한 프롬프트+스키마를 3사에 각각 보내 응답을 정규화해 비교한다
  3. 스키마 위반 시 재시도 1회 → 실패하면 다음 프로바이더로 폴백하는 로직을 구현한다
- **예상 시간**: 150분
- **검증**: 동일 입력에 대해 3사 모두 같은 내부 스키마의 JSON을 반환

**실습 4: API 키 유효성 프리플라이트** ⭐
- **목적**: 방송 전 3사 API가 모두 살아있는지 사전 확인하는 절차를 만든다
- **단계**:
  1. `llm_probe.py`에 3사 키 유효성 확인 함수를 추가한다
  2. 키가 없거나 만료된 프로바이더는 자동으로 목록에서 제외되게 한다
- **예상 시간**: 30분
- **검증**: 키 3개 중 1개를 일부러 무효화해도 나머지 2개로 정상 동작

#### 산출물
```
05-STT-LLM-Harness/
├── README.md
├── examples/
│   ├── stt_probe.py
│   ├── llm_probe.py
│   ├── llm_providers/{openai_provider.py, claude_provider.py, gemini_provider.py}
│   └── probe_log.jsonl
└── guides/
    ├── stt-wer-report.md
    └── llm_registry.json
```

#### Definition of Done
- [ ] 한국어 WER 실측 완료 (일반 조건 + BGM 조건)
- [ ] STT 3단 폴백이 강제 실패 테스트에서 정상 동작
- [ ] LLMProvider 어댑터로 3사 모두 같은 스키마 응답 확보
- [ ] 스키마 위반 시 재시도→폴백 로직 검증
- [ ] API 키 유효성 프리플라이트 함수 동작 확인
- [ ] README 작성 완료
- [ ] WorkLog 작성 완료

#### Self-Assessment
**개념 이해**:
- [ ] WER을 재측정해야 하는 이유를 설명 가능

**실무 활용**:
- [ ] 특정 LLM 프로바이더 API가 막혔을 때 앱이 어떻게 반응하는지 설명 가능

**문제 해결**:
- [ ] 3사 응답이 서로 다른 형식일 때 어디를 고쳐야 하는지 판단 가능

#### 예상 시간 배분
- 개념 학습: 60분 (12%)
- 실습 1: 120분
- 실습 2: 90분
- 실습 3: 150분
- 실습 4: 30분
- 문서화: 30분
- **합계**: 8h (버퍼 20% 포함)

#### 참조 자료
- OpenAI Realtime/Transcribe API 문서: Structured Output, 스트리밍 방식
- Anthropic Tool Use 문서: 스키마 강제 방식
- Google Gemini `responseSchema` 문서: `generationConfig` 사용법

---

### M6 - 멀티 TTS 하네스 + 오디오 라우팅

**난이도**: ⭐⭐⭐
**예상 시간**: 7h
**산출물 폴더**: `06-TTS-Audio-Routing-Harness/`

#### 학습 목표
- [ ] Edge-TTS/Qwen3-TTS/OpenAI TTS/ElevenLabs 4종을 공통 인터페이스로 호출할 수 있다
- [ ] 4종의 지연·비용·한국어 품질을 실측표로 비교할 수 있다
- [ ] VoiceMeeter+VB-CABLE로 마이크·TTS·OBS 오디오 경로를 분리할 수 있다
- [ ] 세션 비용 상한 초과 시 자동으로 무료 프로바이더로 강등되는 서킷 브레이커를 구현할 수 있다

#### 주요 개념
1. **TTSProvider 어댑터**: `synth()`/`stream()`/`cost_per_1k_chars` 공통 인터페이스.
2. **오디오 트랙 분리**: TTS를 마이크와 다른 OBS 트랙에 두면, 앱이 폭주해도 그 트랙만 뮤트할 수 있다.
3. **클론 보이스 회피 원칙**: 본인 클론 보이스를 기본값으로 쓰지 않는다 — 진행자와 AI 목소리 구분을 위해.

#### 실습 과제

**실습 1: TTSProvider 어댑터 구현** ⭐⭐⭐
- **목적**: 4종 프로바이더를 런타임에 갈아 끼울 수 있게 한다
- **단계**:
  1. `TTSProvider` 추상 클래스와 4개 구현체(Edge-TTS/Qwen3-TTS/OpenAI/ElevenLabs)를 작성한다
  2. 동일 문장을 4종 모두로 합성해 결과 파일을 저장한다
  3. `voice_registry.json`에 프로바이더·보이스ID·비용을 등재한다
- **예상 시간**: 150분
- **검증**: 4종 모두 동일 문장의 mp3/wav 파일 생성 성공

**실습 2: 지연·비용·품질 실측표 작성** ⭐⭐
- **목적**: 기본값을 데이터로 정한다
- **단계**:
  1. 각 프로바이더의 첫 청크 도착 지연을 측정한다
  2. 1000자 기준 비용을 계산한다
  3. 한국어 발음 품질을 3점 척도로 주관 평가한다
- **예상 시간**: 90분
- **검증**: `tts-comparison.md`에 4종 비교표 완성, 기본값 프로바이더 결정 근거 명시

**실습 3: VoiceMeeter/VB-CABLE 오디오 라우팅 구성** ⭐⭐⭐
- **목적**: 마이크·TTS·OBS가 서로 간섭하지 않게 한다
- **단계**:
  1. VoiceMeeter Banana로 마이크를 앱과 OBS에 동시 분배한다
  2. VB-CABLE로 TTS 출력을 OBS 별도 트랙에 연결한다
  3. OBS에서 TTS 트랙만 뮤트해도 마이크는 살아있는지 확인한다
- **예상 시간**: 90분
- **검증**: OBS 오디오 믹서에서 TTS 트랙 개별 뮤트 성공

**실습 4: 비용 서킷 브레이커 구현** ⭐⭐
- **목적**: 방송 중 비용 폭주를 막는다
- **단계**:
  1. 세션 호출 횟수·누적 비용 카운터를 구현한다
  2. 상한 초과 시 자동으로 Edge-TTS(무료)로 강등되는 로직을 만든다
- **예상 시간**: 45분
- **검증**: 강제로 상한을 낮춰 강등이 실제로 발생하는지 확인

#### 산출물
```
06-TTS-Audio-Routing-Harness/
├── README.md
├── examples/
│   ├── tts_providers/{edge_tts.py, qwen3_tts.py, openai_tts.py, elevenlabs_tts.py}
│   ├── voice_registry.json
│   └── circuit_breaker.py
└── guides/
    ├── tts-comparison.md
    └── audio-routing-setup.md
```

#### Definition of Done
- [ ] 4종 TTS 모두 동일 문장 합성 성공
- [ ] 지연·비용·품질 실측표 완성 및 기본값 결정
- [ ] VoiceMeeter+VB-CABLE 라우팅 구성 완료, OBS 트랙 개별 뮤트 검증
- [ ] 비용 서킷 브레이커 강등 동작 확인
- [ ] README 작성 완료
- [ ] WorkLog 작성 완료

#### Self-Assessment
**개념 이해**:
- [ ] 클론 보이스를 기본값으로 쓰지 않는 이유를 설명 가능

**실무 활용**:
- [ ] 방송 중 비용이 치솟을 때 앱이 어떻게 반응하는지 설명 가능

#### 예상 시간 배분
- 개념 학습: 45분 (11%)
- 실습 1: 150분
- 실습 2: 90분
- 실습 3: 90분
- 실습 4: 45분
- 문서화: 30분
- **합계**: 7h (버퍼 20% 포함)

#### 참조 자료
- [Qwen3-TTS 기존 자산]: `AI/RemotionStudio/public/*/gen_audio_qwen.py` — preset 보이스·클론 보이스 재사용
- VoiceMeeter/VB-CABLE 공식 문서: 가상 오디오 장치 설정

---

### M7 - Co-MC 엔진 POC (파일 기반 6단계)

**난이도**: ⭐⭐⭐
**예상 시간**: 16h
**산출물 폴더**: `07-CoMC-Engine-POC/`

#### 학습 목표
- [ ] `01_parse_rundown.py`~`06_render_output.py` 6개 스크립트를 순차 실행해 `overlay.json`/`spoken.json`을 생성할 수 있다
- [ ] `current_part_id`(권위)와 `suggested_part_id`(추정)를 분리해 파트 판정 오작동을 방지할 수 있다
- [ ] `session_trace.jsonl`로 전 단계 흐름을 추적할 수 있다
- [ ] 컨텍스트 사전 캐시로 응답 지연을 목표치(발화종료→화면 2.5s) 이내로 맞출 수 있다

#### 주요 개념
1. **파일 기반 계약**: 각 단계가 JSON을 읽고 JSON을 쓰는 구조. 어느 단계가 잘못됐는지 파일만 봐도 추적 가능하다.
2. **권위값/추정값 분리**: `current_part_id`만 응답에 쓰이고, 시각 기반 추정은 배지로만 표시된다. 자동 전환하지 않는다.
3. **컨텍스트 사전 캐시**: 방송 시작 전 `rundown_index`+`broadcast_context`를 미리 빌드해 실시간 응답 지연을 줄인다.

#### 실습 과제

**실습 1: 6단계 POC 폴더/스크립트 골격 생성** ⭐
- **목적**: M5(엔진) 개발을 시작할 최소 구조를 만든다
- **단계**:
  1. `data/`, `src/`, `output/`, `tests/` 폴더를 만든다
  2. `rundown_samples/`에 Live20·Live21 파일 사본을 넣는다
  3. 6개 스크립트 파일과 `common.py`를 빈 함수로 만든다
- **예상 시간**: 60분
- **검증**: 모든 파일 생성, README에 실행 순서 기록

**실습 2: 01_parse_rundown + 02_resolve_context 구현** ⭐⭐⭐
- **목적**: M1의 파싱 계약을 실제 코드로 만든다
- **단계**:
  1. `01_parse_rundown.py`가 Rundown md를 읽어 `rundown_index.json`을 생성한다 (M1 정규식 적용)
  2. `02_resolve_context.py`가 Daily Roundup `## Status Summary`와 Weekly `## Priority Summary`를 크로스 조회해 `broadcast_context.json`을 만든다
  3. Live20·Live21 두 회차 모두 파싱 성공하는지 확인한다
- **예상 시간**: 240분
- **검증**: 두 회차 모두 `status_map`에 최소 5개 항목 채워짐

**실습 3: 03_classify_intent + 04_compose_answer 구현** ⭐⭐⭐
- **목적**: 사용자 발화를 의도로 분류하고 답변 초안을 만든다
- **단계**:
  1. `03_classify_intent.py`가 STT 텍스트에서 `intent`, `slots`, `ambiguity_flags`를 추출한다
  2. `04_compose_answer.py`가 M5의 LLMProvider를 호출해 `sentences[]`와 `claim_map[]`을 생성한다
  3. 프롬프트에 M1의 금칙 섹션이 애초에 포함되지 않는지 확인한다
- **예상 시간**: 240분
- **검증**: 5개 샘플 발화에 대해 `claim_map`의 `evidence_quote`가 실제 원문과 일치

**실습 4: 05_verify_and_gate + 06_render_output 구현** ⭐⭐⭐
- **목적**: 안전 검증과 최종 출력을 완성한다
- **단계**:
  1. `05_verify_and_gate.py`가 M3의 `safety_policy.json`으로 문장을 검증하고 `verdict.json`을 만든다
  2. `06_render_output.py`가 `overlay.json`(화면용)과 `spoken.json`(음성용, TTS 프로바이더 포함)을 생성한다
  3. 전 단계가 `session_trace.jsonl`에 append되는지 확인한다
- **예상 시간**: 180분
- **검증**: end-to-end 실행으로 `overlay.json`/`spoken.json`까지 생성, trace 파일에 6단계 모두 기록

**실습 5: 파트 판정 권위값/추정값 구현** ⭐⭐
- **목적**: M2에서 설계한 "자동 전환 금지" 원칙을 코드화한다
- **단계**:
  1. `session_state.json`에 `current_part_id`(핫키/음성/클릭으로만 변경)와 `suggested_part_id`(시각 자동 계산) 필드를 구현한다
  2. 두 값이 다를 때 배지 표시만 하고 자동 전환하지 않는지 확인한다
- **예상 시간**: 90분
- **검증**: 시각 기반 추정이 틀려도 `current_part_id`는 변하지 않음을 테스트로 증명

**실습 6: 응답 지연 측정과 사전 캐시 적용** ⭐⭐
- **목적**: 실시간 체감 지연을 목표치 이내로 맞춘다
- **단계**:
  1. 캐시 없이 전체 파이프라인 지연을 측정한다
  2. 방송 전 컨텍스트 사전 빌드를 적용한 뒤 다시 측정한다
  3. 목표(발화종료→화면 2.5s, →음성 4s) 대비 결과를 기록한다
- **예상 시간**: 60분
- **검증**: 사전 캐시 적용 후 목표치 달성 또는 격차 원인 문서화

#### 산출물
```
07-CoMC-Engine-POC/
├── README.md
├── data/
│   ├── rundown_samples/  (Live20, Live21 사본)
│   ├── safety_policy.json  (M3 사본)
│   └── part_timeline.sample.json
├── src/
│   ├── common.py
│   ├── 01_parse_rundown.py
│   ├── 02_resolve_context.py
│   ├── 03_classify_intent.py
│   ├── 04_compose_answer.py
│   ├── 05_verify_and_gate.py
│   └── 06_render_output.py
├── output/
│   └── (7종 JSON + session_trace.jsonl)
└── guides/
    └── latency-report.md
```

#### Definition of Done
- [ ] 6개 스크립트 순차 실행으로 `overlay.json`/`spoken.json` 생성 성공
- [ ] Live20·Live21 두 회차 모두 파싱·컨텍스트 조회 성공
- [ ] 5개 샘플 발화의 `claim_map`이 원문과 일치
- [ ] 파트 판정 권위값/추정값 분리 동작 검증
- [ ] `session_trace.jsonl`에 6단계 전부 기록
- [ ] 응답 지연 실측 및 목표 대비 결과 문서화
- [ ] README 작성 완료
- [ ] WorkLog 작성 완료

#### Self-Assessment
**개념 이해**:
- [ ] 파일 기반 계약이 왜 "방송 사고 사후 분석"에 유리한지 설명 가능

**실무 활용**:
- [ ] 특정 단계 출력이 이상할 때 `output/` 폴더만 보고 원인 단계를 좁힐 수 있다

**문제 해결**:
- [ ] `claim_map`이 근거 없이 생성될 때 어느 단계를 의심해야 하는지 안다

#### 예상 시간 배분
- 개념 학습: 90분 (9%)
- 실습 1: 60분
- 실습 2: 240분
- 실습 3: 240분
- 실습 4: 180분
- 실습 5: 90분
- 실습 6: 60분
- 문서화: 60분
- **합계**: 16h (버퍼 20% 포함)

#### 참조 자료
- [`Topics/Vibe-Guiding-VSCode/04-Guiding-Engine-POC/`]: 6단계 파일 계약의 직접 선례
- M3 산출물(`03-Data-Contracts-and-Safety/examples/schemas/`): 이 모듈이 구현할 스키마 원본

---

### M8 - 안전 검증 게이트 심화 & 시나리오 확장

**난이도**: ⭐⭐⭐
**예상 시간**: 8h
**산출물 폴더**: `08-Safety-Gate-Scenarios/`

#### 학습 목표
- [ ] 5개 이상 시나리오(정상/미정 커버리지/금칙 섹션 요청/수량 불일치/완료 항목 오인)로 안전장치를 검증할 수 있다
- [ ] 금칙 섹션이 LLM 프롬프트에 애초에 포함되지 않았음을 `session_trace.jsonl`로 증명할 수 있다
- [ ] 숫자·날짜·고유명사가 `evidence_quote`에 실제 존재하는지 문자열 대조로 검증하는 규칙을 구현할 수 있다
- [ ] 패닉 스톱과 REVIEW 모드 전환 조건을 설계할 수 있다

#### 주요 개념
1. **사후 검증(Post-hoc Verification)**: LLM 자기평가에 의존하지 않고, 생성된 문장의 사실 요소를 규칙으로 대조하는 것.
2. **시나리오 테스트**: 실제 발화 패턴을 재현해 안전장치가 설계대로 동작하는지 자동으로 확인하는 방식.
3. **모드 전환(LIVE/REVIEW/MUTE)**: 리허설에서 사고가 나면 REVIEW(승인 후 발화)로 낮추는 안전 밸브.

#### 실습 과제

**실습 1: 5개 시나리오 테스트 스크립트 작성** ⭐⭐⭐
- **목적**: 안전장치를 반복 가능하게 검증한다
- **단계**:
  1. 정상 / 커버리지 미정 / 금칙 섹션 요청 / 수량 불일치 / 완료 항목을 미래형으로 요청 5개 시나리오를 정의한다
  2. `run_scenarios.py`가 각 시나리오를 M7 엔진에 입력하고 결과를 검증한다
  3. 5개 전부 기대한 대로(차단/확인질문/정상응답) 동작하는지 확인한다
- **예상 시간**: 180분
- **검증**: 5개 시나리오 전부 통과, 결과가 `output/scenarios/{시나리오명}/`에 저장

**실습 2: 금칙 섹션 미노출 증명** ⭐⭐
- **목적**: "말하지 마"가 아니라 "애초에 못 봄"을 증명한다
- **단계**:
  1. 금칙 섹션 요청 시나리오의 `session_trace.jsonl`을 열어 LLM에 실제 전달된 프롬프트를 확인한다
  2. 금칙 섹션 텍스트가 프롬프트 어디에도 없음을 확인한다
- **예상 시간**: 45분
- **검증**: 금칙 섹션 문자열이 trace의 LLM 입력 페이로드에 0회 등장

**실습 3: 사후 검증 규칙 강화** ⭐⭐⭐
- **목적**: 숫자·고유명사 환각을 잡아낸다
- **단계**:
  1. 의도적으로 잘못된 숫자가 포함된 답변 초안을 넣고 `05_verify_and_gate.py`가 걸러내는지 테스트한다
  2. 고유명사(사람 이름, Topic 이름) 오기도 같은 방식으로 테스트한다
  3. 걸러진 문장이 `dropped_sentences[]`에 이유와 함께 기록되는지 확인한다
- **예상 시간**: 90분
- **검증**: 인위적 오류 3종 모두 검출 및 드롭

**실습 4: 모드 전환 로직 구현** ⭐⭐
- **목적**: LIVE/REVIEW/MUTE 3모드를 코드로 구현한다
- **단계**:
  1. 기본 LIVE 모드(즉시 발화)를 구현한다
  2. REVIEW 모드(오버레이 표시 → 승인 핫키 대기 → 발화)를 구현한다
  3. 사고 발생 시 LIVE→REVIEW 수동 전환이 즉시 반영되는지 확인한다
- **예상 시간**: 60분
- **검증**: 모드 전환이 다음 발화부터 즉시 적용됨

#### 산출물
```
08-Safety-Gate-Scenarios/
├── README.md
├── examples/
│   ├── run_scenarios.py
│   └── scenarios/{normal, undefined-coverage, forbidden-request, count-mismatch, completed-item}/
└── guides/
    └── verification-rules.md
```

#### Definition of Done
- [ ] 5개 시나리오 전부 기대 동작과 일치
- [ ] 금칙 섹션이 LLM 입력에 0회 등장함을 trace로 증명
- [ ] 숫자·고유명사 오류 3종 모두 검출
- [ ] LIVE/REVIEW/MUTE 모드 전환 동작 확인
- [ ] README 작성 완료
- [ ] WorkLog 작성 완료

#### Self-Assessment
**개념 이해**:
- [ ] 사후 검증이 LLM 자기평가보다 신뢰할 수 있는 이유를 설명 가능

**실무 활용**:
- [ ] 새 사고 유형이 발견되면 시나리오를 어떻게 추가할지 안다

**문제 해결**:
- [ ] 시나리오가 실패할 때 M7의 어느 스크립트를 먼저 확인할지 안다

#### 예상 시간 배분
- 개념 학습: 45분 (9%)
- 실습 1: 180분
- 실습 2: 45분
- 실습 3: 90분
- 실습 4: 60분
- 문서화: 60분
- **합계**: 8h (버퍼 20% 포함)

#### 참조 자료
- M3 `safety_policy.json`: 이 모듈이 검증할 규칙 원본
- M1 `case-table.md`: 시나리오 설계의 입력 데이터

---

### M9 - 데스크톱 셸 + OBS 오버레이 통합

**난이도**: ⭐⭐⭐
**예상 시간**: 12h
**산출물 폴더**: `09-Desktop-Shell-and-Overlay/`

#### 학습 목표
- [ ] Electron 셸이 Python 사이드카를 구동하고 JSON+stdout으로 통신할 수 있다
- [ ] 글로벌 핫키(파트 전환, 패닉 스톱)를 구현할 수 있다
- [ ] `localhost:PORT/overlay`를 OBS Browser Source로 렌더링할 수 있다
- [ ] 패닉 스톱이 200ms 이내에 무음 상태에 도달함을 실측할 수 있다

#### 주요 개념
1. **프로세스 분리**: Python이 죽어도 Electron 셸(오버레이·패닉 스톱)은 살아있어야 한다는 원칙.
2. **JSON 파일 = IPC 프로토콜**: M7의 파일 계약이 그대로 Electron↔Python 통신 방식이 된다.
3. **패닉 스톱**: TTS 큐 flush + 재생 중단 + 마이크 게이트 폐쇄 + MUTE 전환을 한 핫키로 묶은 최종 방어선.

#### 실습 과제

**실습 1: Electron 셸 골격과 Python 사이드카 구동** ⭐⭐⭐
- **목적**: 두 프로세스가 통신하는 최소 구조를 만든다
- **단계**:
  1. Electron 앱이 시작 시 Python 프로세스를 child_process로 구동한다
  2. Python이 `output/overlay.json`을 쓰면 Electron이 파일 변경을 감지해 UI를 갱신한다
  3. Python 프로세스를 강제 종료해도 Electron 창이 살아있는지 확인한다
- **예상 시간**: 180분
- **검증**: Python 강제 종료 후에도 Electron 창과 오버레이 서버가 계속 응답

**실습 2: 글로벌 핫키 구현** ⭐⭐
- **목적**: 방송 중 손이 키보드에 있을 때의 주력 제어 수단을 만든다
- **단계**:
  1. 파트 전환(다음/이전/특정 파트) 핫키를 구현한다
  2. `current_part_id`가 핫키 입력으로만 바뀌는지 확인한다 (M7 원칙 재확인)
  3. 모드 전환(LIVE/REVIEW/MUTE) 핫키를 추가한다
- **예상 시간**: 90분
- **검증**: 핫키 입력이 `session_state.json`에 즉시 반영

**실습 3: OBS Browser Source 오버레이 렌더** ⭐⭐
- **목적**: 화면 텍스트가 실제 방송 화면에 나오게 한다
- **단계**:
  1. Electron이 `localhost:PORT/overlay`를 서빙하는 HTTP 서버를 띄운다
  2. OBS에 Browser Source로 이 URL을 추가한다
  3. `overlay.json`이 갱신될 때 화면이 실시간으로 바뀌는지 확인한다
- **예상 시간**: 90분
- **검증**: OBS 미리보기에서 오버레이 텍스트 갱신 확인

**실습 4: 패닉 스톱 200ms 검증** ⭐⭐⭐
- **목적**: 최종 안전장치의 성능을 실측으로 보증한다
- **단계**:
  1. 패닉 스톱 핫키에 TTS 큐 flush, 재생 중단, 마이크 게이트 폐쇄, MUTE 전환을 연결한다
  2. TTS 재생 중 핫키를 눌러 오디오가 무음이 되는 시각까지의 지연을 측정한다
  3. 10회 반복 측정해 최대값이 200ms를 넘지 않는지 확인한다
- **예상 시간**: 60분
- **검증**: 10회 측정 중 최대 지연 200ms 이내

**실습 5: 볼트 읽기 전용 접근 구현** ⭐⭐
- **목적**: 안전장치 12(볼트 쓰기 금지)를 코드로 보장한다
- **단계**:
  1. Node `fs`로 볼트 파일을 읽기 전용 모드로만 접근하도록 제한한다
  2. 실수로 쓰기를 시도하면 예외가 발생하는지 테스트한다
- **예상 시간**: 45분
- **검증**: 볼트 경로에 쓰기 시도 시 명시적 오류 발생

#### 산출물
```
09-Desktop-Shell-and-Overlay/
├── README.md
├── examples/
│   ├── shell/  (Electron 앱: main.js, overlay-server.js, hotkeys.js)
│   └── engine/  (M7 스크립트 이식본)
└── guides/
    ├── ipc-protocol.md
    └── panic-stop-benchmark.md
```

#### Definition of Done
- [ ] Python 강제 종료 후에도 Electron 셸 생존 확인
- [ ] 글로벌 핫키(파트 전환·모드 전환) 동작 확인
- [ ] OBS Browser Source에서 오버레이 실시간 갱신 확인
- [ ] 패닉 스톱 10회 측정 최대 지연 200ms 이내
- [ ] 볼트 쓰기 시도 시 예외 발생 확인
- [ ] README 작성 완료
- [ ] WorkLog 작성 완료

#### Self-Assessment
**개념 이해**:
- [ ] 안전장치가 엔진과 다른 프로세스에 있어야 하는 이유를 설명 가능

**실무 활용**:
- [ ] 방송 중 문제가 생기면 `output/` 폴더의 어떤 파일부터 볼지 안다

**문제 해결**:
- [ ] 패닉 스톱 지연이 200ms를 넘으면 어느 컴포넌트를 의심할지 안다

#### 예상 시간 배분
- 개념 학습: 60분 (8%)
- 실습 1: 180분
- 실습 2: 90분
- 실습 3: 90분
- 실습 4: 60분
- 실습 5: 45분
- 문서화: 75분
- **합계**: 12h (버퍼 20% 포함)

#### 참조 자료
- Electron 공식 문서 — `child_process`, IPC
- OBS Browser Source 공식 문서

---

### M10 - 리허설 검증과 라이브 Demo (Capstone)

**난이도**: ⭐⭐⭐
**예상 시간**: 10h
**산출물 폴더**: `10-Live-Rehearsal-Capstone/`

#### 학습 목표
- [ ] 실제 Rundown으로 30분 무관중 리허설을 5회 진행하고 사고를 유형별로 분류할 수 있다
- [ ] 프리플라이트 체크리스트를 완성해 방송 30분 전 루틴으로 만들 수 있다
- [ ] 리허설 결과를 근거로 LIVE 투입 여부를 스스로 판단할 수 있다
- [ ] Topic 전체를 통해 VibeLearn AI 방법론의 효과를 프로젝트형 Topic 관점에서 평가할 수 있다

#### 주요 개념
1. **무관중 리허설**: 실제 방송 없이 동일 조건(OBS 켜짐, 3시간 부하 일부)에서 진행하는 최종 검증.
2. **사고 유형 분류**: 근거 없는 발화 / 지연 / 오탐 / 장치 충돌 등으로 사고를 분류해 재발 방지에 쓴다.
3. **프리플라이트**: 방송 30분 전 9개 항목을 확인하는 고정 루틴. 앱이 아니라 운영으로 리스크를 줄이는 지점.

#### 실습 과제

**실습 1: 프리플라이트 체크리스트 완성 및 자동화** ⭐⭐
- **목적**: 방송 직전 루틴을 반복 가능하게 만든다
- **단계**:
  1. STT/LLM/TTS probe 3종 성공, 오디오 장치, Rundown 최종본 여부, 커버리지 미정 파트 수, `part_timeline.json` 입력, 컨텍스트 사전 빌드, OBS 렌더, 패닉 스톱, 모드 확인 9개 항목을 스크립트로 자동 점검한다
  2. 실패 항목이 있으면 명확히 표시한다
- **예상 시간**: 90분
- **검증**: 9개 항목 자동 점검 스크립트가 통과/실패를 정확히 구분

**실습 2: 30분 무관중 리허설 1~2회** ⭐⭐⭐
- **목적**: 실제 조건에서 처음으로 전체 시스템을 돌려본다
- **단계**:
  1. 실제 최신 Rundown으로 프리플라이트를 통과한 뒤 30분간 진행자 역할을 하며 앱과 상호작용한다
  2. 모든 발화·화면 출력·사고를 기록한다
  3. 사고가 있으면 즉시 REVIEW 모드로 전환해 지속한다
- **예상 시간**: 90분 (리허설 60분 + 기록 30분)
- **검증**: 리허설 로그와 사고 기록 완성

**실습 3: 사고 유형 분류 및 개선** ⭐⭐⭐
- **목적**: 1~2회차에서 발견된 문제를 고친다
- **단계**:
  1. 발생한 사고를 근거없는 발화/지연/오탐/장치충돌로 분류한다
  2. 각 유형별로 M3~M9 중 어느 모듈을 수정해야 하는지 매핑한다
  3. 수정 후 재현 테스트로 해결을 확인한다
- **예상 시간**: 120분
- **검증**: 발견된 사고 유형이 재현 테스트에서 재발하지 않음

**실습 4: 30분 무관중 리허설 3회차 (최종 검증)** ⭐⭐⭐
- **목적**: 개선 후 무사고를 확인해 LIVE 투입을 판단한다
- **단계**:
  1. 동일 조건으로 3회차 리허설을 진행한다
  2. 사고 0건이면 LIVE 투입 판단, 사고가 있으면 원인을 기록하고 재리허설 여부를 결정한다
- **예상 시간**: 90분
- **검증**: 사고 0건 또는 명확한 원인·재발 방지책 기록

**실습 5: Topic Retrospective 작성** ⭐⭐
- **목적**: 방법론 관점에서 전체를 회고한다
- **단계**:
  1. 전체 90시간 대비 실제 소요 시간을 비교한다
  2. VibeLearn AI 방법론(파일 기반 계약, HITL 게이트, 모듈 리듬)이 실제 제품 개발에 얼마나 효과적이었는지 평가한다
  3. `vl_worklog/YYYYMMDD_Live-CoMC-App_Final_Retrospective.md`를 작성한다
- **예상 시간**: 90분
- **검증**: Retrospective 문서 완성, 방법론 개선 제안 최소 2개 포함

#### 산출물
```
10-Live-Rehearsal-Capstone/
├── README.md
├── examples/
│   └── preflight_check.py
├── guides/
│   ├── rehearsal-log-1.md
│   ├── rehearsal-log-2.md
│   ├── incident-classification.md
│   └── rehearsal-log-3-final.md
└── troubleshooting/
    └── known-issues.md
```

#### Definition of Done
- [ ] 프리플라이트 자동 점검 스크립트 완성
- [ ] 무관중 리허설 3회 완료 (1~2회차 문제 발견, 3회차 검증)
- [ ] 사고 유형 분류표 완성, 각 유형이 해당 모듈에 매핑됨
- [ ] 3회차 리허설 사고 0건 또는 명확한 원인·재발 방지책 기록
- [ ] LIVE 투입 가능 여부에 대한 최종 판단 문서화
- [ ] Topic Retrospective 작성 완료
- [ ] WorkLog 작성 완료

#### Self-Assessment
**개념 이해**:
- [ ] 프리플라이트가 "앱이 아니라 운영으로 푸는 문제"인 이유를 설명 가능

**실무 활용**:
- [ ] 리허설 결과만으로 이번 주 방송에 투입할지 스스로 판단 가능

**문제 해결**:
- [ ] 리허설 중 사고가 나면 REVIEW 모드로 즉시 전환하는 절차를 안다

#### 예상 시간 배분
- 개념 학습: 30분 (5%)
- 실습 1: 90분
- 실습 2: 90분
- 실습 3: 120분
- 실습 4: 90분
- 실습 5: 90분
- 문서화: 90분
- **합계**: 10h (버퍼 20% 포함)

#### 참조 자료
- M1~M9의 모든 산출물 (Capstone은 이들의 통합)
- `_Settings_/Skills/live-broadcast/SKILL.md`: 실제 방송 중 AI 보조 동작 원칙 최종 재확인

---

## 📝 WorkLog 작성 가이드

각 학습 세션마다 WorkLog를 작성하여 진행 상황을 추적합니다.

**파일명 규칙**: `vl_worklog/YYYYMMDD_MX_Live-CoMC-App.md`
- 예: `vl_worklog/20260803_M1_Live-CoMC-App.md`
- 같은 모듈이 여러 날 걸리면 `YYYYMMDD_MX_DayN_Live-CoMC-App.md`로 이어간다

**WorkLog 필수 섹션**:
1. 오늘의 학습 목표 (체크리스트)
2. 진행 내용 (실습별 상세 기록)
3. 문제 해결 로그
4. DoD 체크리스트 (모듈 완료 기준, 완료율 n/n)
5. Daily Retrospective (What went well / could be improved / Insights / Tomorrow's focus)
6. 참조 및 산출물

---

## 🔍 Retrospective 가이드

### Daily Retrospective (매일, 5-10분)
WorkLog 내에 작성 — What went well? / What could be improved? / Insights / Tomorrow's focus

### Module Retrospective (모듈 완료 시, 15-20분)
`vl_worklog/YYYYMMDD_MX_Retrospective.md` — 계획 대비 실제 비교, 핵심 학습 내용, 발생한 문제와 해결, Roadmap 정확도 평가, 다음 모듈 준비사항

### Topic Retrospective (전체 완료 시, 30-60분)
`vl_worklog/YYYYMMDD_Live-CoMC-App_Final_Retrospective.md` — 전체 여정 통계, VibeLearn AI 방법론 효과성 평가(특히 프로젝트형 Topic으로서), 산출물 품질 평가, 실제 방송 투입 결과, 향후 개선 사항 (M10 실습 5와 동일)

---

## 📂 전체 폴더 구조

```
Live-CoMC-App/
├── topic_starter.md
├── vl_prompts/
│   ├── roadmap_prompt.md
│   └── daily_learning_prompt.md
├── vl_roadmap/
│   └── 20260802_RoadMap_Live-CoMC-App.md
├── vl_worklog/
│   └── (세션별 WorkLog 누적)
├── vl_materials/
│   └── (Rundown 사본, 안전 규약 사본 등)
├── 01-Concept-and-Rundown-Contract/
├── 02-Architecture-and-Boundary/
├── 03-Data-Contracts-and-Safety/
├── 04-WakeWord-VAD-Harness/
├── 05-STT-LLM-Harness/
├── 06-TTS-Audio-Routing-Harness/
├── 07-CoMC-Engine-POC/
├── 08-Safety-Gate-Scenarios/
├── 09-Desktop-Shell-and-Overlay/
└── 10-Live-Rehearsal-Capstone/
```

> **참고**: 실제 배포용 데스크톱 앱(`live-comc-app/` — Electron shell + Python engine 통합 빌드)은
> Remotion-VideoCreation 선례를 따라 이 Topic 폴더 루트에 별도 프로젝트로 둘 수 있다.
> M9에서 만든 `examples/shell`·`examples/engine`이 그 기반이 된다.

---

## 📊 학습 진행 상황 추적

| 모듈 | 시작일 | 종료일 | 상태 | DoD 달성률 | 비고 |
|------|--------|--------|------|-----------|------|
| M1 | 2026-08-02 | 2026-08-02 | ✅ | 100% | 미정 커버리지 실물 미관찰 등 실측 인사이트 2건 M3로 전달 |
| M2 | 2026-08-02 | 2026-08-02 | ✅ | 100% | app-boundary.md 하드 게이트 확정, Electron 채택 |
| M3 | 2026-08-09 | 2026-08-09 | ✅ | 100% | 7종 스키마+양성/음성 검증 통과, safety_policy.json, LLM 3사 정규화 설계 완료 |
| M4 | 2026-08-09 | 2026-08-15 | ✅ | 100% (6/6) | 실습3 오탐 0회(최대점수 0.1953, 임계값 2.6배 여유)·실습4 에코차단 검증(gate off 5건 vs on 0건). 하네스 함정 4건 발견·수정. 이월: 실제 방송 3시간 오디오 실측 채점 |
| M5 | | | ⏳ | 0% | |
| M6 | | | ⏳ | 0% | |
| M7 | | | ⏳ | 0% | |
| M8 | | | ⏳ | 0% | |
| M9 | | | ⏳ | 0% | |
| M10 | | | ⏳ | 0% | |

**범례**: ⏳ 대기 · 🔄 진행 중 · ✅ 완료

---

## 🎯 성공 기준

전체 Topic 완료 기준:
- [ ] 모든 모듈 완료 (DoD 100%)
- [ ] 최소 10개 산출물 폴더 생성 (M1~M10)
- [ ] Topic Retrospective 작성
- [ ] Self-Assessment 평균 ⭐⭐⭐⭐ 이상
- [ ] Capstone(M10) — 무관중 리허설 3회, 최종 사고 0건 또는 명확한 대응책 확보
- [ ] 실제 라이브 방송(AI in Action Live) 투입 여부에 대한 근거 있는 판단 완료

---

**생성자**: Claude with VibeLearn AI
**Roadmap 버전**: 1.0
**방법론 버전**: VibeLearn AI 2.0
