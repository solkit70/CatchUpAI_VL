# CODEX's English Language Service Expansion Plan

**Date:** 2026-02-15
**Author:** CODEX
**Status:** Proposed

## 1. Goal and Design Principle

This plan targets a practical global rollout of CUA_VL for English-speaking users.
The key difference from a translation-only approach is operational design:
- keep Korean and English consistently synchronized,
- make English onboarding first-class,
- prevent language drift through automation and quality gates.

## 2. Design Summary (How I Would Design It)

### 2.1 Localization Model

Use a **paired-file model** in the same directory:
- `*.md` -> Korean
- `*.en.md` -> English

But define clear ownership:
- Source of truth for methodology logic: Korean (`*.md`)
- Source of truth for global onboarding UX: English (`README.en.md`, `GETTING_STARTED.en.md`)

Rationale:
- Korean-first authoring remains natural for current maintainers.
- English users get dedicated onboarding quality instead of literal translation tone.

### 2.2 Entry Point Strategy

Provide explicit language selection at all major entry points:
- Root `README.md` top section: link to `README.en.md`
- Root `README.en.md` top section: link to `README.md`
- Same pattern for `GETTING_STARTED*`, `AGENTS*`, `CLAUDE*`, `GEMINI*`

Optional improvement:
- add a small `INDEX.md` (language hub) with two buttons/links: Korean / English.

### 2.3 Content Tiering

Manage translation by impact tier, not by file count.

Tier 1 (must be native-quality English first):
- `README.en.md`
- `GETTING_STARTED.en.md`
- `templates/quick_start_prompt.en.md`
- `templates/topic_starter.en.md`

Tier 2 (high-value operational docs):
- `AGENTS.en.md`
- `CLAUDE.en.md`
- `GEMINI.en.md`
- `templates/roadmap_prompt_template.en.md`
- `templates/daily_learning_prompt.en.md`
- `templates/workflow_guide.en.md`

Tier 3 (topic artifacts and historical materials):
- generated Topic docs and archive materials

Rationale:
- Most user drop-off happens in first 10 minutes. Tier 1 quality determines adoption.

### 2.4 Prompt/Template Generation Architecture

Refactor `scripts/sync-prompts.ps1` into language-aware behavior:
- input: base template + language code (`ko`, `en`)
- output: topic prompt set in matching language
- enforce naming rule:
  - `roadmap_prompt.md` from Korean template
  - `roadmap_prompt.en.md` from English template

Also enforce UTF-8 output explicitly to avoid mojibake.

### 2.5 Quality Gates (Important)

Add CI or pre-commit checks:
1. Pair check: every required Korean doc has an English pair.
2. Placeholder check: variable placeholders are identical between language files.
3. Structure check: required headings exist in both files.
4. Anti-fake-translation check: detect if `.en.md` still contains mostly Korean text.
5. Encoding check: ensure UTF-8 readable output.

This prevents "file exists but not truly localized" issues.

### 2.6 Terminology and Style Governance

Create a single glossary file:
- `templates/translation_glossary.en-ko.md`

Include:
- fixed translations for core concepts (e.g., WorkLog, Roadmap, DoD, Module Retrospective)
- tone rules (instructional, concise, action-oriented)
- non-translation rules for product terms (e.g., keep `CUA_VL`, `VibeLearn AI`)

Outcome:
- consistent vocabulary across all AI-generated or human-edited docs.

## 3. Execution Plan

### Phase A (1-2 days): Baseline Stabilization
- define tiered scope
- clean top-level bilingual links
- fix encoding policy (UTF-8)

### Phase B (2-4 days): Core English UX
- rewrite Tier 1 in natural English (not literal translation)
- usability pass from "new English user" perspective

### Phase C (2-3 days): Automation and Safety
- language-aware `sync-prompts.ps1`
- add validation script/checklist (pair/placeholders/encoding)

### Phase D (ongoing): Operations
- glossary updates
- monthly language consistency review
- track adoption metrics (English doc views, time-to-first-topic)

## 4. Suggested Repository Additions

- `Global_Service_Plan/20260215_CODEX_Plan.md` (this document)
- `templates/translation_glossary.en-ko.md`
- `scripts/validate-localization.ps1` (checks listed above)

## 5. Risks and Mitigations

Risk 1: English docs diverge from Korean updates
- Mitigation: pair check + update checklist in PR template

Risk 2: English feels machine-translated and loses trust
- Mitigation: Tier 1 human-quality rewrite standard

Risk 3: Broken prompt generation between languages
- Mitigation: language parameterization + automated validation

Risk 4: Encoding corruption in mixed tooling
- Mitigation: enforce UTF-8 write/read in scripts

## 6. Definition of Done

This global service expansion is "done" when:
1. Tier 1 and Tier 2 documents are fully usable in English.
2. Every critical Korean file has a validated English pair.
3. Prompt sync script can generate language-specific outputs reliably.
4. Localization validation runs automatically and blocks regressions.
5. A new English user can start a Topic without Korean references.

## 7. Why This Differs from the Existing Gemini Plan

Gemini plan is a good start for file-based translation structure.
My plan adds the missing operational layer:
- onboarding-first prioritization,
- script architecture for language-aware generation,
- automated quality gates,
- glossary governance,
- measurable completion criteria.

This is the minimum structure needed to run bilingual documentation as a sustainable service, not a one-time translation task.

---

# CODEX의 영어 서비스 확장 설계안 (한국어 설명)

**날짜:** 2026-02-15  
**작성자:** CODEX  
**상태:** 제안

## 1. 목표와 설계 원칙

이 설계의 목표는 CUA_VL을 영어 사용자도 실제로 사용할 수 있는 수준으로 확장하는 것입니다.  
핵심은 단순 번역이 아니라 운영 가능한 다국어 체계를 만드는 것입니다.

- 한국어/영어 문서 동기화 유지
- 영어 사용자 온보딩 품질 강화
- 자동 검증으로 품질 저하와 언어 드리프트 방지

## 2. 내가 제안한 설계 핵심

### 2.1 로컬라이제이션 모델

동일 디렉터리 내 페어 파일 구조를 유지합니다.
- `*.md`: 한국어
- `*.en.md`: 영어

또한 책임을 분리합니다.
- 방법론 로직의 기준 문서: 한국어(`*.md`)
- 글로벌 온보딩 UX의 기준 문서: 영어(`README.en.md`, `GETTING_STARTED.en.md`)

### 2.2 진입점 전략

주요 문서 상단에서 언어를 명확히 선택할 수 있게 합니다.
- `README.md` -> `README.en.md` 링크
- `README.en.md` -> `README.md` 링크
- `GETTING_STARTED`, `AGENTS`, `CLAUDE`, `GEMINI`도 동일 패턴 적용

선택적으로 `INDEX.md` 언어 허브를 둘 수 있습니다.

### 2.3 작업 우선순위(Tier)

파일 수 기준이 아니라 사용자 영향도 기준으로 번역/개선을 진행합니다.

- Tier 1: 영어 온보딩 핵심 (가장 먼저 고품질 작성)
- Tier 2: 운영 문서 및 템플릿
- Tier 3: Topic 산출물/아카이브

이유: 신규 사용자는 초반 10분 경험에서 이탈이 많이 발생하므로 Tier 1 품질이 가장 중요합니다.

### 2.4 프롬프트 생성 구조

`scripts/sync-prompts.ps1`를 언어 인지형으로 바꿉니다.
- 입력: 템플릿 + 언어 코드(`ko`, `en`)
- 출력: 언어별 prompt 세트
- 파일명 규칙 고정:
  - 한국어: `roadmap_prompt.md`
  - 영어: `roadmap_prompt.en.md`

또한 UTF-8 강제로 인코딩 깨짐(모지바케) 문제를 방지합니다.

### 2.5 품질 게이트(자동 검증)

CI 또는 사전 검증 단계에서 다음을 체크합니다.
1. 페어 체크: 필수 한국어 문서에 영어 짝 파일 존재 여부
2. 플레이스홀더 체크: 변수 토큰 일치 여부
3. 구조 체크: 필수 헤더 섹션 존재 여부
4. 가짜 번역 체크: `.en.md`에 한국어 비율이 비정상적으로 높은지
5. 인코딩 체크: UTF-8 정상 여부

### 2.6 용어집/스타일 가이드

`templates/translation_glossary.en-ko.md`를 두고 핵심 용어를 통일합니다.
- 고정 번역어(WorkLog, Roadmap, DoD 등)
- 문체 규칙(간결/지시형/실행 중심)
- 비번역 제품명(`CUA_VL`, `VibeLearn AI`)

## 3. 실행 단계

- Phase A: 기준선 정리(범위, 상단 링크, UTF-8 정책)
- Phase B: Tier 1 영어 사용자 경험 개선
- Phase C: 자동화/검증 체계 도입
- Phase D: 운영(월간 점검, 용어집 관리, 지표 추적)

## 4. 완료 기준(DoD)

다음 조건을 만족하면 글로벌 확장 1차 완료로 봅니다.
1. Tier 1/2 영어 문서가 실제 사용 가능 수준
2. 필수 한국어 문서에 영어 페어가 모두 존재
3. 언어별 prompt 생성이 안정적으로 동작
4. 검증 자동화가 회귀를 차단
5. 영어 사용자 단독으로 Topic 시작 가능

## 5. GEMINI 안과의 차이

GEMINI 안은 파일 기반 번역 구조를 잘 제시했습니다.  
내 설계는 여기에 운영 관점(우선순위, 자동 검증, 용어 거버넌스, 명확한 완료 기준)을 추가해 장기적으로 유지 가능한 체계로 확장한 점이 차별점입니다.
