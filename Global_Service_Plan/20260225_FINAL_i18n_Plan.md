# CUA_VL 글로벌 서비스 확장 최종 계획안

**작성일**: 2026-02-25
**작성자**: Claude Sonnet 4.6 (CLAUDE + CODEX + GEMINI 계획안 종합)
**버전**: 1.0
**목적**: 3개 AI 계획안(Claude, Codex, Gemini)의 장점을 종합하여 실행 가능한 최종 다국어 서비스 계획 수립

---

## 0. 3개 계획안 비교 요약

| 항목 | GEMINI | CLAUDE | CODEX | **최종안 채택** |
|------|--------|--------|-------|----------------|
| 파일 구조 | `.en.md` 접미사 | `.en.md` 접미사 (Option C) | `.en.md` 접미사 | `.en.md` 접미사 ✅ |
| 범위 정의 | 파일 수 기준 (10개) | 단계 기반 (Phase 1-4) | 영향도 기반 (Tier 1-3) | Tier 기반 + 파일 수 명시 ✅ |
| 품질 관리 | 없음 | 번역 가이드라인 + 용어 테이블 | 5가지 자동 검증 게이트 | 가이드라인 + 자동 게이트 ✅ |
| 자동화 | sync-prompts.ps1 수정 언급 | 번역 상태 추적 파일 | 언어 인지형 스크립트 | 언어 파라미터화 + 상태 추적 ✅ |
| 진입점 | 없음 | 언어 전환 배지 | INDEX.md + 배지 | 배지 방식 (간결함) ✅ |
| 완료 기준 | 없음 | 우선순위 요약표 | DoD 5가지 조건 | 측정 가능한 DoD ✅ |
| 리스크 분석 | 없음 | 없음 | 4가지 리스크 + 완화 | 리스크 분석 포함 ✅ |
| 미래 확장 | 없음 | `.ja.md`, `.zh.md` 패턴 | 없음 | 언어 확장 패턴 ✅ |

> **핵심 결론**: 3개 계획안은 모두 `.en.md` 접미사 방식과 기존 폴더 구조 유지에 동의함.
> 최종안은 GEMINI의 단순명쾌함 + CLAUDE의 구조적 설계 + CODEX의 운영 관점을 통합.

---

## 1. 파일 구조 전략

> 출처: GEMINI (기본 방향) + CLAUDE (상세 설계) — 3개 AI 모두 동의

### 1.1 파일 명명 규칙

- 한국어 원본: `파일명.md`
- 영어 번역본: `파일명.en.md`
- 기존 디렉토리 구조 유지, 같은 폴더에 공존

### 1.2 폴더 구조 (최종)

```
/
├── README.md                    (한국어)
├── README.en.md                 (영어)
├── GETTING_STARTED.md           (한국어)
├── GETTING_STARTED.en.md        (영어)
├── CLAUDE.md                    (한국어, AI 시스템 프롬프트)
├── CLAUDE.en.md                 (영어, AI 시스템 프롬프트)
├── GEMINI.md                    (자동생성, 한국어)
├── GEMINI.en.md                 (자동생성, 영어)
├── AGENTS.md                    (자동생성, 한국어)
├── AGENTS.en.md                 (자동생성, 영어)
├── templates/
│   ├── topic_starter.md         (한국어)
│   ├── topic_starter.en.md      (영어)
│   ├── roadmap_prompt_template.md
│   ├── roadmap_prompt_template.en.md
│   ├── daily_learning_prompt.md
│   ├── daily_learning_prompt.en.md
│   ├── quick_start_prompt.md
│   ├── quick_start_prompt.en.md
│   ├── workflow_guide.md
│   ├── workflow_guide.en.md
│   └── translation_glossary.en-ko.md  ← 신규 (용어집)
├── scripts/
│   ├── sync-prompts.ps1          (언어 인지형으로 개선)
│   ├── validate-localization.ps1  ← 신규 (품질 게이트)
│   └── translation_status.json   ← 신규 (번역 상태 추적)
```

### 1.3 Option B (로캘 폴더 방식) 비채택 이유

> 출처: CLAUDE 상세 분석

`/ko/`, `/en/` 폴더로 분리하는 방식은 이론적으로 깔끔하지만, CUA_VL에서는 다음 이유로 부적합:

1. **AI 도구 충돌**: Claude Code(`CLAUDE.md`), Gemini CLI(`GEMINI.md`), Codex(`AGENTS.md`)가 모두 루트에서 해당 파일을 자동 탐색. `/ko/CLAUDE.md`로 이동하면 도구가 인식하지 못함.
2. **사용자 혼란**: 학습자가 `templates/daily_learning_prompt.md`를 직접 참조하는 경우가 많으므로 경로 변경 시 기존 가이드와 불일치 발생.
3. **과도한 리스크**: 운영 중인 프로젝트의 전체 파일 구조 변경은 리스크가 큼.

---

## 2. 소유권 원칙 (Source of Truth)

> 출처: CLAUDE + CODEX

### 2.1 이중 소유권 모델

| 구분 | 정본 | 이유 |
|------|------|------|
| **방법론 로직** | 한국어 (`*.md`) | 현재 유지보수자가 한국어 기반이므로 자연스러운 저작 흐름 유지 |
| **글로벌 온보딩 UX** | 영어 (`README.en.md`, `GETTING_STARTED.en.md`) | 영어 사용자의 첫 경험 품질이 채택률 결정 |

### 2.2 변경 원칙

- 콘텐츠 변경: **항상 한국어 파일에서 먼저** 발생 → 영어 번역 업데이트
- 구조적 변경 (섹션 추가/삭제): 양쪽 동시 반영
- 오타/링크 수정: 해당 언어 파일만 수정
- 새 파일 추가: 한국어 + 영어 동시 생성 권장

---

## 3. 콘텐츠 우선순위 (Tier 분류)

> 출처: CODEX (핵심 기여) — 파일 수 기준이 아닌 사용자 영향도 기준

신규 사용자는 첫 10분 경험에서 이탈이 집중됨. 온보딩 품질이 채택률을 결정하므로 Tier 1을 최우선 처리.

### Tier 1: 영어 온보딩 핵심 (최우선, 고품질 필수)

| 파일 | 현재 줄 수 | 비고 |
|------|----------:|------|
| `README.en.md` | 746줄 | GitHub 진입점, 최고 품질 필요 |
| `GETTING_STARTED.en.md` | 666줄 | 실습 시작 가이드 |
| `templates/quick_start_prompt.en.md` | 356줄 | 빠른 시작 경로 |
| `templates/topic_starter.en.md` | 279줄 | Topic 시작 인터페이스 |

### Tier 2: 운영 문서 및 시스템 프롬프트 (차순위)

| 파일 | 현재 줄 수 | 비고 |
|------|----------:|------|
| `CLAUDE.en.md` | 124줄 | **번역 아닌 영어 재작성** 필요 |
| `AGENTS.en.md` | 자동생성 | sync-prompts.ps1 실행으로 생성 |
| `GEMINI.en.md` | 자동생성 | sync-prompts.ps1 실행으로 생성 |
| `templates/roadmap_prompt_template.en.md` | 628줄 | 로드맵 생성 프롬프트 |
| `templates/daily_learning_prompt.en.md` | 690줄 | 일일 학습 프롬프트 |
| `templates/workflow_guide.en.md` | 343줄 | 워크플로우 참조 |

### Tier 3: Topic 산출물 및 아카이브 (필요 시)

- `Topics/` 내 학습 산출물은 사용자 선택 언어로 생성 (자동)
- 별도 번역 작업 불필요

---

## 4. 번역 품질 기준

> 출처: CLAUDE (상세 가이드라인)

### 4.1 5가지 품질 기준

| 기준 | 내용 |
|------|------|
| **정확성** | 원문의 의미를 정확히 전달 |
| **자연스러움** | 영어 원어민이 읽기 자연스러운 문체 (직역 금지) |
| **용어 일관성** | CUA_VL 고유 용어는 용어집(`translation_glossary.en-ko.md`) 준수 |
| **구조 보존** | 마크다운 구조, 링크, 코드 블록 동일하게 유지 |
| **문화 적응** | 한국어 특유의 표현은 영어 맥락에 맞게 조정 |

### 4.2 파일별 번역 주의사항

> 출처: CLAUDE

**README.md → README.en.md**
- 상단에 언어 전환 배지 추가 (§7 참조)
- `GETTING_STARTED.md` 링크 → `GETTING_STARTED.en.md`로 변경
- 방법론 철학 부분은 의역 허용

**GETTING_STARTED.md → GETTING_STARTED.en.md**
- 상단에 언어 전환 배지 추가
- Step-by-step 가이드의 파일 경로 참조 시 `.en.md` 버전 안내
- PowerShell / Bash 명령어 예시는 그대로 유지

**CLAUDE.md → CLAUDE.en.md** ⚠️ 주의
- **단순 번역이 아닌 영어용 시스템 프롬프트로 재작성**
- AI가 영어로 응답하도록 지시
- 템플릿 참조 경로를 `.en.md`로 변경
- "언어 매칭" 규칙: 영어 사용자에게는 영어로 응답

**Templates (5개)**
- 플레이스홀더 변수명 유지: `{TOPIC_NAME}`, `{DURATION}` 등
- 마크다운 구조 (헤더, 리스트, 테이블) 동일하게 유지
- 프롬프트 지시문은 영어 AI 도구에서 자연스럽게 작동하도록 조정

### 4.3 번역 워크플로우

```
1. 한국어 원본 읽기
2. 섹션 단위로 번역 (구조 유지)
3. 내부 링크를 .en.md 경로로 변환
4. CUA_VL 용어 테이블 준수 확인 (§5 참조)
5. 영어 네이티브 관점에서 자연스러움 검토
6. 마크다운 렌더링 확인
7. 품질 게이트 통과 확인 (§6 참조)
```

---

## 5. CUA_VL 용어 통일 테이블

> 출처: CLAUDE (용어 테이블) + CODEX (glossary 파일 생성 제안)
> 별도 파일 `templates/translation_glossary.en-ko.md`로 관리

### 5.1 핵심 용어

| 한국어 | 영어 | 비고 |
|--------|------|------|
| 학습 방법론 | Learning Methodology | |
| 로드맵 | Roadmap | 그대로 사용 |
| 일일 학습 | Daily Learning Session | |
| 학습 일지 | WorkLog | 영어에서도 WorkLog 유지 |
| 모듈 | Module | 그대로 사용 |
| 산출물 | Deliverable / Output | 맥락에 따라 선택 |
| 교과서 품질 | Textbook Quality | |
| 회고 | Retrospective | 그대로 사용 |
| 핵심 개념 | Key Concepts | |
| 실습 과제 | Hands-on Exercises | |
| 완료 기준 | Definition of Done (DoD) | 그대로 사용 |
| 자기 평가 | Self-Assessment | |
| 시간 배분 | Time Allocation | |
| 선수지식 | Prerequisites | |
| 활성화 조건 | Activation Conditions | |

### 5.2 비번역 고정 용어 (변경 금지)

| 용어 | 이유 |
|------|------|
| `CUA_VL` | 프로젝트/방법론 이름 |
| `VibeLearn AI` | 브랜드명 |
| `vl_prompts`, `vl_roadmap`, `vl_worklog`, `vl_materials` | 폴더명 불변 |
| `YYYYMMDD` | 날짜 형식 불변 |
| `MX` (모듈 번호) | 네이밍 규칙 불변 |
| WorkLog | 고유 용어로 유지 |

### 5.3 문체 규칙

- **톤**: 지시형, 간결함, 실행 중심 (instructional, concise, action-oriented)
- **주어**: 영어 문서에서는 명시적 주어 사용 (한국어 생략 주어 패턴 주의)
- **경어**: 존댓말 없이 직접적 지시문 ("You should..." 또는 명령형)

---

## 6. 품질 게이트 (자동화 검증)

> 출처: CODEX (핵심 기여) — "파일이 있지만 실제로 번역되지 않은" 문제 방지

`scripts/validate-localization.ps1` 스크립트로 다음 5가지를 자동 검증:

### 6.1 5가지 검증 항목

| # | 검증 항목 | 설명 |
|---|-----------|------|
| 1 | **페어 체크** | 필수 한국어 문서에 영어 짝 파일이 존재하는지 확인 |
| 2 | **플레이스홀더 체크** | `{TOPIC_NAME}` 등 변수 토큰이 한/영 파일에서 동일한지 확인 |
| 3 | **구조 체크** | 필수 헤더 섹션이 양쪽 파일에 모두 존재하는지 확인 |
| 4 | **가짜 번역 체크** | `.en.md` 파일에 한국어 비율이 비정상적으로 높은지 감지 |
| 5 | **인코딩 체크** | UTF-8 정상 여부 확인 (모지바케 방지) |

### 6.2 실행 시점

- 수동 실행: 번역 작업 후 검증 시
- 선택적: git pre-commit hook에 연결하여 자동화

---

## 7. 구현 단계

> 출처: CLAUDE (4 Phase 구조) + CODEX (구체적 기간 및 단계별 목표)

### Phase 1: 기준선 정리 (1-2일)

- [ ] 번역 범위 및 Tier 확정
- [ ] `templates/translation_glossary.en-ko.md` 초안 작성
- [ ] `scripts/translation_status.json` 초기 구조 생성
- [ ] README.md / README.en.md 상단 언어 전환 배지 추가 (§8 참조)
- [ ] UTF-8 인코딩 정책 확인

### Phase 2: Tier 1 영어 온보딩 핵심 (2-4일)

- [ ] `README.en.md` 작성 (직역 아닌 고품질 영어로)
- [ ] `GETTING_STARTED.en.md` 작성
- [ ] `templates/quick_start_prompt.en.md` 번역
- [ ] `templates/topic_starter.en.md` 번역
- [ ] 영어 사용자 관점에서 usability 검토

### Phase 3: Tier 2 운영 문서 + 자동화 (2-3일)

- [ ] `CLAUDE.en.md` **영어 시스템 프롬프트로 재작성** (번역 아님)
- [ ] `sync-prompts.ps1` 언어 인지형으로 개선 → `AGENTS.en.md`, `GEMINI.en.md` 자동 생성
- [ ] 나머지 템플릿 3개 번역 (roadmap, daily, workflow)
- [ ] `scripts/validate-localization.ps1` 작성 및 테스트

### Phase 4: 운영 체계 (지속)

- [ ] 월간 언어 일관성 검토
- [ ] 용어집 업데이트
- [ ] 채택 지표 추적 (영어 문서 조회, 최초 Topic 시작까지 시간)
- [ ] 한국어 파일 변경 시 영어 번역 상태 갱신

---

## 8. sync-prompts.ps1 개선

> 출처: CODEX (언어 인지형 구조) + CLAUDE (기존 인프라 활용)

### 8.1 현재 → 목표

| 항목 | 현재 | 목표 |
|------|------|------|
| 입력 | 고정 소스 파일 | 소스 파일 + 언어 코드 (`ko`, `en`) |
| 출력 | 한국어 prompt만 | 언어별 prompt 세트 |
| 파일명 | `roadmap_prompt.md` | `roadmap_prompt.md` (ko) + `roadmap_prompt.en.md` (en) |
| 인코딩 | 기존 | UTF-8 명시적 강제 |

### 8.2 언어 계통 처리

```
한국어 계통: CLAUDE.md → GEMINI.md, AGENTS.md
영어 계통:   CLAUDE.en.md → GEMINI.en.md, AGENTS.en.md
```

---

## 9. 번역 상태 추적

> 출처: CLAUDE

`scripts/translation_status.json` 구조:

```json
{
  "source_lang": "ko",
  "last_updated": "2026-02-25",
  "translations": {
    "en": {
      "README.md": {
        "status": "synced",
        "last_synced": "2026-02-25",
        "source_hash": "abc123..."
      },
      "GETTING_STARTED.md": {
        "status": "not_started"
      },
      "CLAUDE.md": {
        "status": "needs_rewrite",
        "note": "단순 번역 아닌 재작성 필요"
      }
    }
  }
}
```

**상태값**: `not_started` → `in_progress` → `synced` → `needs_update`

---

## 10. GitHub 사용자 경험

> 출처: CLAUDE (언어 전환 배지 설계)

### 10.1 언어 전환 배지 (모든 주요 문서 상단)

```markdown
🌐 **Language / 언어**: [한국어](README.md) | [English](README.en.md)
```

### 10.2 영어 사용자 여정

```
1. GitHub 저장소 방문 → README.md 노출
2. 상단 "English" 링크 클릭 → README.en.md
3. README.en.md에서 방법론 이해
4. GETTING_STARTED.en.md로 이동 → 실습 시작
5. AI 도구에 CLAUDE.en.md (또는 해당 도구의 .en.md) 로드
6. templates/*.en.md 활용하여 학습 진행
7. Topic 폴더 생성 → 영어로 학습 진행
```

---

## 11. 완료 기준 (Definition of Done)

> 출처: CODEX (측정 가능한 5가지 조건)

다음 조건을 모두 만족하면 글로벌 서비스 확장 1차 완료:

- [ ] Tier 1 및 Tier 2 영어 문서가 실제 사용 가능 수준 (품질 게이트 통과)
- [ ] 모든 필수 한국어 파일에 유효한 영어 짝 파일 존재
- [ ] `sync-prompts.ps1`이 언어별 prompt 세트를 안정적으로 생성
- [ ] `validate-localization.ps1`이 자동 검증 수행하고 회귀 차단
- [ ] 영어 사용자가 한국어 파일 참조 없이 단독으로 Topic 시작 가능

---

## 12. 리스크 분석 및 완화

> 출처: CODEX

| 리스크 | 영향도 | 완화 방안 |
|--------|--------|-----------|
| 영어 문서가 한국어 업데이트에서 뒤처짐 | 높음 | 페어 체크 + PR 체크리스트 + translation_status.json |
| 영어가 기계번역 느낌으로 신뢰 저하 | 높음 | Tier 1은 고품질 재작성 기준 적용, 직역 금지 |
| 언어 간 prompt 생성 오작동 | 중간 | sync-prompts.ps1 언어 파라미터화 + 자동 검증 |
| 혼합 도구 환경에서 인코딩 깨짐 | 낮음 | 스크립트에서 UTF-8 명시적 강제 |

---

## 13. 미래 언어 확장

> 출처: CLAUDE (확장 설계)

동일한 패턴을 반복 적용하여 3번째 언어 추가 가능:

```markdown
🌐 **Language**: [한국어](README.md) | [English](README.en.md) | [日本語](README.ja.md) | [中文](README.zh.md)
```

`sync-prompts.ps1` 설정에 언어 추가:
```powershell
@{ Source = "CLAUDE.ja.md"; Targets = @("GEMINI.ja.md", "AGENTS.ja.md") }
```

현재는 한국어/영어 2개 언어만 지원하므로 폴더 분리 불필요. 3개 이상 언어 추가 시 구조 재검토 권장.

---

## 부록: 최종안 신규 파일 목록

| 파일 | 유형 | 설명 |
|------|------|------|
| `templates/translation_glossary.en-ko.md` | 신규 생성 | CUA_VL 용어 한/영 통일 glossary |
| `scripts/validate-localization.ps1` | 신규 생성 | 5가지 품질 게이트 자동 검증 |
| `scripts/translation_status.json` | 신규 생성 | 번역 상태 추적 |
| `scripts/sync-prompts.ps1` | 기존 개선 | 언어 인지형으로 개선 + UTF-8 강제 |
| `README.en.md` 외 `.en.md` 파일들 | 번역 생성 | Phase 1-2-3 순서로 생성 |

---

*이 문서는 Claude Code (Sonnet 4.6)가 CLAUDE(Opus 4.6), CODEX, GEMINI 3개 AI의 계획안을 분석하고 각각의 장점을 종합하여 작성한 최종 다국어 서비스 확장 계획입니다.*
