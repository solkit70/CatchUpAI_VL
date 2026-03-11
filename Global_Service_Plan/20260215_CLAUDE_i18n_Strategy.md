# CUA_VL 다국어 지원 전략 (Claude Code 설계)

**작성일**: 2026-02-15
**작성자**: Claude Code (Opus 4.6)
**버전**: 1.0
**목적**: 한국어 전용 CUA_VL 프로젝트를 영어 사용자에게도 제공하기 위한 i18n 전략

---

## 1. 현재 상태 분석

### 1.1 번역 대상 파일 (8개, 총 3,832줄)

| 구분 | 파일 | 줄 수 | 역할 |
|------|------|------:|------|
| **루트 문서** | README.md | 746 | 방법론 소개 (진입점) |
| | GETTING_STARTED.md | 666 | 빠른 시작 가이드 |
| | CLAUDE.md | 124 | AI 시스템 프롬프트 (정본) |
| **템플릿** | topic_starter.md | 279 | Topic 시작 템플릿 |
| | roadmap_prompt_template.md | 628 | 로드맵 생성 프롬프트 |
| | daily_learning_prompt.md | 690 | 일일 학습 프롬프트 |
| | quick_start_prompt.md | 356 | 빠른 시작 프롬프트 |
| | workflow_guide.md | 343 | 워크플로우 참조 |

> **자동 생성 파일** (별도 번역 불필요): GEMINI.md, AGENTS.md → CLAUDE.md에서 sync-prompts.ps1로 생성

### 1.2 기존 인프라

- **sync-prompts.ps1**: CLAUDE.md → GEMINI.md, AGENTS.md 동기화 (이미 `.en.md` 설정 포함)
- **프로젝트 구조**: 명확한 역할 분리 (문서 / 템플릿 / 스크립트 / Topics)
- **Git**: 버전 관리 활성, Topics/ 폴더는 .gitignore

---

## 2. 접근 방식 비교

### Option A: 파일 접미사 방식 (`파일명.en.md`)

```
/
├── README.md          (한국어)
├── README.en.md       (영어)
├── CLAUDE.md          (한국어)
├── CLAUDE.en.md       (영어)
├── templates/
│   ├── topic_starter.md        (한국어)
│   ├── topic_starter.en.md     (영어)
│   └── ...
```

| 장점 | 단점 |
|------|------|
| 구현이 간단하고 직관적 | 같은 디렉토리에 파일 수가 2배로 증가 |
| 한국어/영어 파일이 나란히 위치하여 비교 용이 | 파일 목록이 길어져 가독성 저하 |
| 기존 구조 변경 최소화 | 3개 이상 언어 추가 시 혼잡 |
| sync-prompts.ps1에 이미 설정 존재 | GitHub에서 README.en.md 자동 표시 안됨 |
| 상대 링크 유지 용이 | |

### Option B: 로캘 폴더 방식 (`/en/`, `/ko/`)

```
/
├── README.md          (언어 선택 안내만)
├── ko/
│   ├── README.md
│   ├── GETTING_STARTED.md
│   ├── CLAUDE.md
│   └── templates/
│       └── ...
├── en/
│   ├── README.md
│   ├── GETTING_STARTED.md
│   ├── CLAUDE.md
│   └── templates/
│       └── ...
```

| 장점 | 단점 |
|------|------|
| 언어별 완전 분리, 깔끔한 구조 | 기존 구조 대폭 변경 필요 |
| 3개 이상 언어 확장 용이 | 모든 내부 링크 경로 수정 필요 |
| 표준 i18n 패턴 | CLAUDE.md, GEMINI.md 등 루트 필수 파일 위치 문제 |
| 각 언어가 독립적 | AI 도구들이 루트의 CLAUDE.md를 찾으므로 충돌 |

### Option C: 하이브리드 방식 (추천)

```
/
├── README.md           (한국어 + 상단 언어 전환 링크)
├── README.en.md        (영어 + 상단 언어 전환 링크)
├── GETTING_STARTED.md  (한국어)
├── GETTING_STARTED.en.md (영어)
├── CLAUDE.md           (한국어, 정본)
├── CLAUDE.en.md        (영어, 정본)
├── GEMINI.md           (자동생성, 한국어)
├── GEMINI.en.md        (자동생성, 영어)
├── AGENTS.md           (자동생성, 한국어)
├── AGENTS.en.md        (자동생성, 영어)
├── templates/
│   ├── topic_starter.md          (한국어)
│   ├── topic_starter.en.md       (영어)
│   ├── roadmap_prompt_template.md
│   ├── roadmap_prompt_template.en.md
│   ├── daily_learning_prompt.md
│   ├── daily_learning_prompt.en.md
│   ├── quick_start_prompt.md
│   ├── quick_start_prompt.en.md
│   ├── workflow_guide.md
│   └── workflow_guide.en.md
└── scripts/
    └── sync-prompts.ps1   (양 언어 동기화)
```

| 장점 | 단점 |
|------|------|
| 기존 구조 유지하면서 영어 추가 | 파일 수 증가 (8 → 16) |
| sync-prompts.ps1 인프라 재활용 | 디렉토리 내 파일이 많아 보임 |
| AI 도구 호환성 유지 (CLAUDE.md 루트 위치) | 한국어/영어 동기화 관리 필요 |
| README.md 언어 전환으로 GitHub UX 확보 | |
| 상대 링크가 자연스럽게 작동 | |
| 미래 언어 확장도 가능 (`.ja.md`, `.zh.md`) | |

---

## 3. 추천안: Option C (하이브리드 방식)

### 3.1 추천 이유

1. **최소 변경 원칙**: 기존 한국어 파일과 구조를 그대로 유지하면서 영어 파일만 추가
2. **AI 도구 호환성**: CLAUDE.md, GEMINI.md, AGENTS.md가 루트에 남아있어 Claude Code, Gemini CLI, Codex CLI 모두 정상 작동
3. **기존 인프라 활용**: sync-prompts.ps1에 이미 `.en.md` 동기화 설정이 존재
4. **GitHub UX**: README.md 상단에 언어 전환 배지를 추가하여 직관적 탐색
5. **실용적 확장성**: 일본어, 중국어 등 추가 시 동일 패턴 적용 가능 (`.ja.md`, `.zh.md`)

### 3.2 핵심 설계 원칙

#### 원칙 1: 한국어가 정본 (Source of Truth)

```
한국어 (정본)          영어 (번역본)
README.md       →    README.en.md
CLAUDE.md       →    CLAUDE.en.md
templates/*.md  →    templates/*.en.md
```

- 콘텐츠 변경은 **항상 한국어 파일에서 먼저** 발생
- 영어 파일은 한국어의 번역본으로 관리
- 구조적 변경(섹션 추가/삭제)은 양쪽 동시 반영

#### 원칙 2: 언어별 독립 링크 체계

```markdown
# 한국어 파일 내 링크
[빠른 시작](GETTING_STARTED.md)

# 영어 파일 내 링크
[Quick Start](GETTING_STARTED.en.md)
```

- 각 언어의 문서는 같은 언어의 다른 문서로 링크
- 언어 간 이동은 상단 언어 전환 링크로만

#### 원칙 3: 시스템 프롬프트는 언어별 독립 정본

```
CLAUDE.md    → GEMINI.md, AGENTS.md     (한국어 계통)
CLAUDE.en.md → GEMINI.en.md, AGENTS.en.md (영어 계통)
```

- CLAUDE.md와 CLAUDE.en.md 각각이 해당 언어 계통의 정본
- 시스템 프롬프트는 단순 번역이 아닌 **언어에 맞는 자연스러운 지시문**으로 작성
- sync-prompts.ps1이 양쪽 계통 모두 처리 (이미 구현됨)

---

## 4. 구현 계획

### Phase 1: 핵심 문서 번역 (MVP)

**목표**: 영어 사용자가 CUA_VL을 이해하고 시작할 수 있는 최소 경로 확보

**대상 파일 (3개, 1,536줄)**:
1. `README.en.md` ← README.md 번역 (746줄)
2. `GETTING_STARTED.en.md` ← GETTING_STARTED.md 번역 (666줄)
3. `CLAUDE.en.md` ← CLAUDE.md 번역 (124줄)

**추가 작업**:
- README.md / README.en.md 상단에 **언어 전환 배지** 추가
- GETTING_STARTED.md / GETTING_STARTED.en.md 상단에도 언어 전환 링크 추가
- sync-prompts.ps1 실행으로 GEMINI.en.md, AGENTS.en.md 자동 생성

**언어 전환 배지 예시 (README.md 상단)**:
```markdown
🌐 **Language / 언어**: [한국어](README.md) | [English](README.en.md)
```

**언어 전환 배지 예시 (README.en.md 상단)**:
```markdown
🌐 **Language / 언어**: [한국어](README.md) | [English](README.en.md)
```

### Phase 2: 템플릿 번역

**목표**: 영어 사용자가 학습 세션을 실제로 진행할 수 있도록 템플릿 완비

**대상 파일 (5개, 2,296줄)**:
1. `templates/topic_starter.en.md` (279줄)
2. `templates/roadmap_prompt_template.en.md` (628줄)
3. `templates/daily_learning_prompt.en.md` (690줄)
4. `templates/quick_start_prompt.en.md` (356줄)
5. `templates/workflow_guide.en.md` (343줄)

**추가 작업**:
- CLAUDE.en.md 내 템플릿 참조 경로를 `.en.md`로 업데이트
- 각 템플릿 내부의 cross-reference 링크도 `.en.md`로 업데이트

### Phase 3: 동기화 체계 강화

**목표**: 한국어 변경 시 영어 번역 필요성을 감지하고 관리하는 체계 구축

**구현 항목**:

#### 3-1. 번역 상태 추적 파일
```
scripts/translation_status.json
```

```json
{
  "source_lang": "ko",
  "translations": {
    "en": {
      "README.md": {
        "source_hash": "abc123...",
        "translated_hash": "def456...",
        "last_synced": "2026-02-15",
        "status": "synced"
      },
      "CLAUDE.md": { ... },
      "templates/topic_starter.md": { ... }
    }
  }
}
```

#### 3-2. 동기화 검증 스크립트 확장
`sync-prompts.ps1`에 번역 상태 확인 기능 추가:
- 한국어 파일 변경 감지 (git diff 기반)
- 변경된 파일의 영어 버전 존재 여부 확인
- "번역 필요" 경고 출력

#### 3-3. git pre-commit hook (선택)
- 한국어 파일 변경 시 해당 영어 파일의 `translation_status`를 `needs_update`로 변경
- 번역 누락 방지

### Phase 4: 사용자 경험 최적화

**목표**: 영어 사용자의 완전한 학습 여정 지원

**구현 항목**:

#### 4-1. Topic 생성 시 언어 인식
- `topic_starter.md` / `topic_starter.en.md` 템플릿에 언어 설정 필드 추가
- Topic 생성 시 사용자 언어에 맞는 템플릿 자동 선택

#### 4-2. CLAUDE.md 언어 매칭 강화
- 기존 "언어 매칭" 규칙을 확장:
  - 영어 사용자 → `*.en.md` 템플릿 참조
  - 한국어 사용자 → `*.md` 템플릿 참조

#### 4-3. 학습 산출물 언어
- Topics/ 폴더 내 산출물은 사용자 언어로 생성
- topic_info.md에 `language: en` 또는 `language: ko` 필드 추가

---

## 5. 번역 가이드라인

### 5.1 번역 품질 기준

| 항목 | 기준 |
|------|------|
| **정확성** | 원문의 의미를 정확히 전달 |
| **자연스러움** | 영어 원어민이 읽기 자연스러운 문체 |
| **용어 일관성** | CUA_VL 고유 용어는 통일된 영어 표현 사용 |
| **구조 보존** | 마크다운 구조, 링크, 코드 블록 동일하게 유지 |
| **문화 적응** | 한국어 특유의 표현은 영어 맥락에 맞게 조정 |

### 5.2 CUA_VL 핵심 용어 번역 테이블

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
| 완료 기준 (DoD) | Definition of Done (DoD) | 그대로 사용 |
| 자기 평가 | Self-Assessment | |
| 시간 배분 | Time Allocation | |
| 선수지식 | Prerequisites | |
| 활성화 조건 | Activation Conditions | |
| 폴더 구조 | Folder Structure | |
| vl_prompts | vl_prompts | 폴더명 불변 |
| vl_roadmap | vl_roadmap | 폴더명 불변 |
| vl_worklog | vl_worklog | 폴더명 불변 |
| vl_materials | vl_materials | 폴더명 불변 |

> **중요**: `vl_` 접두사 폴더명, `YYYYMMDD` 날짜 형식, `MX` 모듈 번호 등 **시스템 네이밍은 언어와 무관하게 통일**

### 5.3 번역 워크플로우

```
1. 한국어 원본 읽기
2. 섹션 단위로 번역 (구조 유지)
3. 내부 링크를 .en.md 경로로 변환
4. CUA_VL 용어 테이블 준수 확인
5. 영어 네이티브 관점에서 자연스러움 검토
6. 마크다운 렌더링 확인
```

---

## 6. 파일별 번역 시 주의사항

### README.md → README.en.md
- 상단에 언어 전환 배지 추가
- `GETTING_STARTED.md` 링크 → `GETTING_STARTED.en.md`로 변경
- 방법론 철학 부분은 의역 허용 (직역하면 부자연스러울 수 있음)

### GETTING_STARTED.md → GETTING_STARTED.en.md
- 상단에 언어 전환 배지 추가
- Step-by-step 가이드의 파일 경로 참조 시 `.en.md` 버전 안내
- PowerShell / Bash 명령어 예시는 그대로 유지
- AI 도구 이름 (Claude, ChatGPT, Gemini) 그대로 유지

### CLAUDE.md → CLAUDE.en.md
- **단순 번역이 아닌 영어용 시스템 프롬프트로 재작성**
- AI가 영어로 응답하도록 지시
- 템플릿 참조 경로를 `.en.md`로 변경
- "언어 매칭" 규칙: 영어 사용자에게는 영어로 응답

### Templates (5개)
- 플레이스홀더 변수명 유지: `{TOPIC_NAME}`, `{DURATION}` 등
- 마크다운 구조 (헤더, 리스트, 테이블) 동일하게 유지
- 프롬프트 지시문은 영어 AI 도구에서 자연스럽게 작동하도록 조정

---

## 7. GitHub에서의 다국어 경험

### 7.1 진입점 설계

GitHub 저장소 방문 시 보이는 README.md에 언어 선택을 제공:

```markdown
# VibeLearn AI (CUA_VL)

🌐 **Language / 언어**: [한국어](README.md) | [English](README.en.md)

**Version**: 2.0
...
```

### 7.2 영어 사용자 여정

```
1. GitHub 저장소 방문
2. README.md 상단의 "English" 클릭
3. README.en.md에서 방법론 이해
4. GETTING_STARTED.en.md로 이동하여 실습 시작
5. AI 도구에 CLAUDE.en.md (또는 해당 도구의 .en.md) 로드
6. templates/*.en.md 활용하여 학습 진행
```

---

## 8. 장기 유지보수 계획

### 8.1 변경 추적 프로세스

```
한국어 파일 수정
    ↓
git commit 시 pre-commit hook 발동
    ↓
translation_status.json에서 해당 영어 파일 상태를 "needs_update"로 변경
    ↓
다음 번역 세션에서 "needs_update" 파일만 번역
    ↓
번역 완료 후 상태를 "synced"로 변경
```

### 8.2 버전 동기화 규칙

1. **구조적 변경** (섹션 추가/삭제/재배치): 양쪽 즉시 반영
2. **내용 수정** (기존 섹션 내 텍스트 변경): 한국어 먼저, 영어는 다음 번역 주기에
3. **오타/링크 수정**: 해당 언어 파일만 수정
4. **새 파일 추가**: 한국어 + 영어 동시 생성 권장

### 8.3 품질 유지

- 정기적 번역 리뷰 (방법론 버전 업데이트 시)
- 영어 사용자 피드백 수집 채널 운영
- AI 번역 활용 시 반드시 사람의 검토 거침

---

## 9. 구현 우선순위 요약

| 순서 | 작업 | 파일 수 | 예상 범위 |
|:----:|------|:------:|----------|
| **1** | README.en.md + 언어 전환 배지 | 2 | 746줄 번역 + 배지 |
| **2** | GETTING_STARTED.en.md | 1 | 666줄 번역 |
| **3** | CLAUDE.en.md (영어 시스템 프롬프트) | 1 | 124줄 재작성 |
| **4** | sync-prompts.ps1 실행 (GEMINI.en.md, AGENTS.en.md 생성) | 0 | 스크립트 실행만 |
| **5** | templates/*.en.md (5개) | 5 | 2,296줄 번역 |
| **6** | translation_status.json + 동기화 검증 | 2 | 새 파일 |
| **합계** | | **11** | **3,832줄 + 자동화** |

---

## 10. 미래 확장 고려

### 추가 언어 지원 시

동일한 패턴을 반복 적용:
- 일본어: `*.ja.md`
- 중국어: `*.zh.md`
- 스페인어: `*.es.md`

```markdown
🌐 **Language**: [한국어](README.md) | [English](README.en.md) | [日本語](README.ja.md) | [中文](README.zh.md)
```

sync-prompts.ps1 설정에 해당 언어 추가:
```powershell
@{
    Source = "CLAUDE.ja.md"
    Targets = @("GEMINI.ja.md", "AGENTS.ja.md")
    Header = "<!-- AUTO-GENERATED -->"
}
```

---

## 부록: Option B (로캘 폴더) 비채택 사유

Option B(`/en/`, `/ko/` 폴더 방식)가 i18n의 표준 패턴이지만, CUA_VL 프로젝트에서는 다음 이유로 비채택:

1. **AI 도구 충돌**: Claude Code는 루트의 `CLAUDE.md`를, Gemini CLI는 `GEMINI.md`를, Codex는 `AGENTS.md`를 탐색. `/ko/CLAUDE.md`로 이동하면 이 도구들이 자동으로 인식하지 못함.

2. **사용자 혼란**: CUA_VL은 학습 방법론이므로 사용자가 `templates/daily_learning_prompt.md`처럼 **직접 파일 경로를 참조**하는 경우가 많음. `/ko/templates/...`로 변경하면 기존 가이드와 불일치.

3. **과도한 구조 변경**: 이미 운영 중인 프로젝트의 전체 파일 구조를 변경하는 것은 리스크가 큼. 기존 Topics/ 내 참조 경로도 모두 수정 필요.

4. **실질적 필요**: 현재 2개 언어(한국어/영어)만 지원하므로 폴더 분리의 이점이 크지 않음. 3개 이상 언어 추가 시 재검토.

---

*이 문서는 Claude Code (Opus 4.6)가 프로젝트 구조, 기존 인프라, AI 도구 호환성을 분석하여 작성한 다국어 지원 전략입니다.*
