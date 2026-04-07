# WorkLog - M1: gobi-monorepo + gobi-ai/docs 전체 구조 파악

**날짜**: 2026-04-06
**Topic**: GOBI-Specs-Pipeline
**모듈**: M1 - gobi-monorepo + gobi-ai/docs 전체 구조 파악
**학습 시간**: 약 3h

---

## 🎯 오늘의 학습 목표

- [x] gobi-monorepo 레포 클론 및 최상위 구조 파악
- [x] specs/ 디렉토리 전체 파일 목록 확인
- [x] specs/README.md SSOT Core Concepts 내용 파악
- [x] prompts/CODE_TO_SPECS.md 파악
- [x] LINEAR.md AI 에이전트 워크플로우 파악
- [x] gobi-ai/docs 레포 클론 및 구조 파악 (Mintlify, MDX, docs.json)
- [x] 산출물 문서 작성 (README.md, repo-structure.md, pipeline-diagram.md)

---

## 📚 진행 내용

### 1. gobi-monorepo 클론 및 구조 탐색

**클론 위치**: `C:\AI_study\2026\GOBI_VibeGuiding\gobi-monorepo`

**발견한 최상위 구조**:
- `CLAUDE.md`: Claude Code용 7개 프로젝트 전체 가이드 (스택, 명령어, 컨벤션)
- `LINEAR.md`: AI 에이전트 기반 Linear 개발 워크플로우
- `.runner/agents/`: 에이전트 역할 정의 파일
- `prompts/CODE_TO_SPECS.md`: AI가 코드에서 스펙을 생성하는 프롬프트
- `specs/`: 26개 feature spec 파일 + README.md

**7개 프로젝트 확인**:
gobi-web (Next.js) / gobi-desktop (Electron) / gobi-cli (Node.js) / gobi-webdrive (Python) / gobi-backend (NestJS) / gobi-app (Flutter) / gobi-cloud (Python/GCP)

### 2. specs/ 심층 탐색

**26개 feature spec 파일** 목록 확인 (01~26, 2026-04-05 기준 최신)

**specs/README.md에서 발견**:
- 4개 제품(Desktop, Space, CLI, Mobile)의 Core Concepts 정의
- PCM(Personal Context Management) 개념 명확히 정의
- Feature Index 테이블 (26개 기능, 관련 제품, 설명)

**spec 파일 포맷 (05-second-brain-agent.md 샘플 분석)**:
- 섹션: Overview / Product Surfaces / Functional Requirements / User Flows / Relationships
- 기능 정의 중심 (구현 방식 없음)
- Second Brain Agent가 Vault 컨텍스트 기반으로 동작하는 방식 파악

### 3. prompts/CODE_TO_SPECS.md 분석

AI가 전체 코드베이스를 읽고 feature spec을 생성하는 프롬프트. 주요 지침:
- 10~30개 기능 커버
- 기능 관점만 (코드/구현 방식 참조 금지)
- 한 번에 완성하지 말고 10회 이상 검토

**Vibe Guiding 인사이트**: 이것의 역방향 = **SPECS_TO_GUIDE** — specs에서 사용자 가이드/Vibe Guiding 컨텍스트를 자동 생성. 개발팀이 이미 이 방향성을 갖고 있음.

### 4. LINEAR.md — AI 에이전트 파이프라인

개발팀이 이미 AI 에이전트 기반 개발 워크플로우 운영:
Created → Planner AI → Plan-Reviewer AI → Developer AI → PR Reviewer AI → HumanReview → Done

**Vibe Guiding 인사이트**: 에이전트가 개발 파이프라인에 통합된 선례가 있음. Vibe Guiding 에이전트도 동일 방식으로 문서화 파이프라인에 통합 가능.

### 5. gobi-ai/docs 클론 및 분석

**클론 위치**: `C:\AI_study\2026\GOBI_VibeGuiding\docs`

**프레임워크**: Mintlify (MDX + docs.json)

**현재 콘텐츠**:
- products/: desktop, community-space, cli, mobile
- reference/: glossary, ecosystem
- 현재 초기 단계 (일부 Mintlify 예시 파일 포함)

**파이프라인 발견**:
- gobi-ai/docs push → Mintlify 자동 빌드 → docs.gobihq.com: **자동 ✅**
- gobi-monorepo/specs → gobi-ai/docs: **수동 ⚠️ (자동화 없음)**

---

## 🐛 문제 해결 로그

없음. 두 레포 모두 클론 성공.

---

## 📊 DoD 체크리스트

- [x] 7개 프로젝트 목록 + 역할 파악
- [x] specs/ 26개 파일 목록 확인
- [x] gobi-ai/docs 프레임워크(Mintlify) 확인
- [x] 파이프라인 수동 변환 필요성 파악
- [x] `01-Monorepo-Overview/README.md` 작성
- [x] `01-Monorepo-Overview/repo-structure.md` 작성
- [x] `01-Monorepo-Overview/pipeline-diagram.md` 작성
- [x] WorkLog 작성

**완료율**: 8/8 (100%) ✅

---

## 💡 Daily Retrospective

### What went well
- 레포를 직접 클론하여 분석하니 훨씬 빠르고 정확하게 파악 가능
- CODE_TO_SPECS.md 발견 → Vibe Guiding 방향과 정확히 역방향 관계임을 파악
- LINEAR.md에서 AI 에이전트가 이미 파이프라인에 있다는 사실 확인

### What could be improved
- gobi-ai/docs의 각 mdx 파일 내용까지 읽지는 못했음 (M2 이후 필요 시 참조)

### Insights (핵심 발견)
1. **수동 변환 갭이 핵심 기회**: specs → docs 변환이 수동이라는 점이 VibeLearn AI의 가장 명확한 가치 제안 포인트
2. **CODE_TO_SPECS의 역방향**: 개발팀이 이미 "코드 → AI → 스펙" 방향 구현. Vibe Guiding은 "스펙 → AI → 사용자 가이드/컨텍스트" 역방향을 담당
3. **에이전트 통합 선례**: LINEAR.md에서 AI 에이전트가 개발 파이프라인에 이미 통합됨 → Vibe Guiding 에이전트 통합에 대한 GOBI 팀의 수용도 높을 것
4. **앱 내 Vibe Guiding**: Second Brain Agent(05)가 System Prompt + Tool Calls 기반으로 동작 → Vibe Guiding을 에이전트의 시스템 프롬프트/컨텍스트로 주입 가능성

### Tomorrow's focus
- M2 시작: 05(Second Brain Agent), 06(Voice), 07(Capture), 19(Orchestration) spec 심층 분석
- 특히 19-orchestration.md에서 Reflex 개념이 Vibe Guiding과 어떻게 연결되는지 집중 분석

---

## 📎 참조 및 산출물

**클론된 레포**:
- `C:\AI_study\2026\GOBI_VibeGuiding\gobi-monorepo\`
- `C:\AI_study\2026\GOBI_VibeGuiding\docs\`

**생성된 파일**:
- `01-Monorepo-Overview/README.md`: M1 모듈 요약
- `01-Monorepo-Overview/repo-structure.md`: 전체 구조 분석
- `01-Monorepo-Overview/pipeline-diagram.md`: 파이프라인 다이어그램 + Vibe Guiding 통합 제안

**참조한 파일**:
- `gobi-monorepo/CLAUDE.md`
- `gobi-monorepo/LINEAR.md`
- `gobi-monorepo/prompts/CODE_TO_SPECS.md`
- `gobi-monorepo/specs/README.md`
- `gobi-monorepo/specs/05-second-brain-agent.md`
- `gobi-ai/docs/docs.json`
- `gobi-ai/docs/AGENTS.md`
- `gobi-ai/docs/index.mdx`

---

**작성자**: Changsoo (Claude Code 활용)
**방법론**: VibeLearn AI (CUA_VL)
