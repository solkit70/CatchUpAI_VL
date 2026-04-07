# GOBI-Specs-Pipeline 학습 로드맵

**생성일**: 2026-04-06
**업데이트**: 2026-04-06 (M1 탐색 결과 반영, 3모듈로 재편)
**방법론**: CUA_VL (VibeLearn AI)
**버전**: 1.1

---

## 📚 학습 개요

### Topic 소개
GOBI 개발팀이 운영하는 문서화 파이프라인(`gobi-monorepo/specs` → `gobi-ai/docs` → `docs.gobihq.com`)을 분석하고, 이 구조에 VibeLearn AI / Vibe Guiding을 어떻게 접목할지 방향을 결정하는 학습입니다. 단순한 기술 학습을 넘어, **Vibe Guiding 프로젝트의 설계 방향을 결정하는 전략적 인풋**을 만드는 것이 목표입니다.

### 🔑 M1 탐색에서 발견한 핵심 사항 (2026-04-06)
1. **파이프라인이 자동화되어 있지 않음** — specs(Markdown) → gobi-ai/docs(MDX) 변환은 수동 작업 필요. 이것 자체가 Vibe Guiding의 핵심 기회
2. **CODE_TO_SPECS.md 존재** — AI가 코드에서 스펙을 생성하는 프롬프트가 이미 있음. VibeLearn AI 방향과 동일
3. **AI 에이전트가 이미 개발 파이프라인에 있음** (LINEAR.md) — Planner AI, Developer AI, PR Reviewer AI. Vibe Guiding도 에이전트 역할로 추가 가능
4. **gobi-ai/docs는 Mintlify 기반** — MDX 포맷, docs.json 설정, 현재는 초기 단계

### 최종 목표
> **GOBI 팀에 공유 가능한 Vibe Guiding 전략 제안서 완성**
> - 현재 파이프라인에 통합할지 vs 별도 운영할지 결정
> - GOBI Desktop / Gobi Space 앱 내 실시간 Vibe Guiding 구동 방안 포함

### 예상 학습 기간
2주 → **1주로 단축** (M1에서 2개 모듈 분량 선행 완료)

### 학습 환경
- OS: Windows 11
- 로컬 레포: `C:\AI_study\2026\GOBI_VibeGuiding\gobi-monorepo` (Private ✅ 클론 완료)
- 로컬 레포: `C:\AI_study\2026\GOBI_VibeGuiding\docs` (Public ✅ 클론 완료)

---

## 🗺️ 전체 로드맵 구조

| 모듈 | 모듈명 | 난이도 | 예상 시간 | 산출물 폴더 | 상태 |
|------|--------|--------|----------|------------|------|
| M1 | gobi-monorepo + gobi-ai/docs 전체 구조 파악 | ⭐ | 3h | 01-Monorepo-Overview/ | 🔄 진행 중 |
| M2 | Vibe Guiding 핵심 Spec 파일 심층 분석 | ⭐⭐ | 3h | 02-Specs-Deep-Dive/ | ⏳ 대기 |
| M3 | Capstone — Vibe Guiding 전략 제안서 | ⭐⭐⭐ | 3h | 03-Capstone/ | ⏳ 대기 |

**총 예상 시간**: 9시간

---

## 📖 모듈별 상세 계획

---

### M1 - gobi-monorepo + gobi-ai/docs 전체 구조 파악

**난이도**: ⭐
**예상 시간**: 3h
**산출물 폴더**: `01-Monorepo-Overview/`
**상태**: 🔄 진행 중 (2026-04-06 탐색 시작, 주요 구조 파악 완료)

#### 학습 목표
- [x] gobi-monorepo의 7개 프로젝트 목록과 역할 파악
- [x] specs/ 디렉토리 구조 및 26개 feature spec 파일 목록 확인
- [x] specs/README.md SSOT Core Concepts 내용 파악
- [x] prompts/CODE_TO_SPECS.md 존재 및 목적 파악
- [x] LINEAR.md AI 에이전트 워크플로우 파악
- [x] gobi-ai/docs 레포 구조 파악 (Mintlify, MDX, docs.json)
- [ ] spec 파일 포맷 및 내용 구조 샘플 분석 정리
- [ ] `01-Monorepo-Overview/` 산출물 문서 작성

#### gobi-monorepo 핵심 발견 (탐색 결과)

**7개 프로젝트:**

| 프로젝트 | 스택 | 역할 |
|---------|------|------|
| gobi-web | Next.js 16, React 19 | Gobi Space 웹앱, Vercel 배포 |
| gobi-desktop | Electron 38, React 19, Vite | Desktop 창작 도구, 로컬 파일 관리 |
| gobi-cli | Node.js, TypeScript, Commander.js | CLI 인터페이스, npm 공개 패키지 |
| gobi-webdrive | Python, Flask | 파일 싱크 + 에이전트 인프라 |
| gobi-backend | NestJS 10, PostgreSQL, Redis | 메인 백엔드 API, Cloud Run 배포 |
| gobi-app | Flutter | iOS/Android 모바일 앱 |
| gobi-cloud | Python, GCP | 웨어러블 데이터 처리, 비동기 파이프라인 |

**specs/ 구조 (26개 feature spec):**
- 번호 + 기능명 형식 (`01-authentication-and-onboarding.md` ~ `26-real-time-communication.md`)
- 포맷: Markdown (H2 섹션: Overview, Product Surfaces, Functional Requirements, User Flows, Relationships)
- 특징: 제품별이 아닌 **기능별** cross-cutting 스펙 (구현 방식 X, 기능 정의 O)
- SSOT: 이 스펙만 보면 전체 제품을 재구현할 수 있는 수준 목표

**gobi-ai/docs 핵심 발견:**
- 프레임워크: **Mintlify** (MDX 포맷, docs.json 설정)
- 현재 콘텐츠: products/(Desktop, Community Space, CLI, Mobile) + reference/(glossary, ecosystem)
- deploy: gobi-ai/docs 레포에 push → Mintlify 자동 deploy → docs.gobihq.com
- ⚠️ **monorepo/specs → gobi-ai/docs 변환은 자동화 없음** (수동 작업)

#### 실습 과제

**실습 1: 산출물 문서 작성** ⭐
- gobi-monorepo 전체 구조 요약 문서 작성
- spec 파일 포맷 분석 (샘플 1개 섹션 구조 정리)
- gobi-ai/docs 파이프라인 다이어그램 작성
- 산출물: `01-Monorepo-Overview/README.md`, `repo-structure.md`, `pipeline-diagram.md`
- **예상 시간**: 60분

#### Definition of Done
- [x] 7개 프로젝트 목록 + 역할 파악
- [x] specs/ 26개 파일 목록 확인
- [x] gobi-ai/docs 프레임워크(Mintlify) 확인
- [x] 파이프라인 수동 변환 필요성 파악
- [ ] `01-Monorepo-Overview/README.md` 작성
- [ ] 파이프라인 다이어그램 완성
- [ ] WorkLog 작성

---

### M2 - Vibe Guiding 핵심 Spec 파일 심층 분석

**난이도**: ⭐⭐
**예상 시간**: 3h
**산출물 폴더**: `02-Specs-Deep-Dive/`
**상태**: ⏳ 대기

#### 학습 목표
- [ ] Vibe Guiding과 직접 관련된 spec 4개를 깊이 읽고 핵심 내용 정리
- [ ] 각 spec의 "Vibe Guiding 접목 포인트"를 식별한다
- [ ] PCM(Personal Context Management) 개념이 Vibe Guiding과 어떻게 연결되는지 정의한다
- [ ] Gobi 에이전트(Second Brain Agent)가 어떻게 동작하는지 이해한다

#### 분석 대상 Spec 파일 (4개)

| 파일 | 이유 |
|------|------|
| `05-second-brain-agent.md` | Gobi 에이전트 동작 방식 — Vibe Guiding이 에이전트로 통합될 기반 |
| `06-voice-interaction.md` | 음성 인터페이스 — Vibe Guiding의 주요 채널 |
| `07-capture.md` | 캡처 메커니즘 — Ambient Mode와 Vibe Guiding의 접점 |
| `19-orchestration-and-automation.md` | Reflex/자동화 — Vibe Guiding을 Reflex로 구현할 수 있는지 검토 |

#### 실습 과제

**실습 1: Spec 4개 읽기 + Vibe Guiding 접점 분석** ⭐⭐
- 각 spec 파일을 읽고 "Vibe Guiding이 어디에 끼어들 수 있는가?" 관점으로 분석
- 접점 후보를 스펙 섹션 단위로 메모
- 산출물: `02-Specs-Deep-Dive/spec-analysis-[파일명].md` (4개)
- **예상 시간**: 120분

**실습 2: Vibe Guiding 접목 포인트 통합 정리** ⭐⭐⭐
- 4개 spec에서 발견한 접점을 하나의 문서로 통합
- "앱 내 실시간 Vibe Guiding이 가능한가?" 에 대한 초안 답변 작성
- 산출물: `02-Specs-Deep-Dive/vibe-guiding-touchpoints.md`
- **예상 시간**: 60분

#### Definition of Done
- [ ] 4개 spec 파일 각각 분석 문서 작성
- [ ] Vibe Guiding 접점 통합 문서 완성
- [ ] "앱 내 실시간 Vibe Guiding" 가능성 평가 초안
- [ ] WorkLog 작성

#### 참조 자료
- `C:\AI_study\2026\GOBI_VibeGuiding\gobi-monorepo\specs\05-second-brain-agent.md`
- `C:\AI_study\2026\GOBI_VibeGuiding\gobi-monorepo\specs\06-voice-interaction.md`
- `C:\AI_study\2026\GOBI_VibeGuiding\gobi-monorepo\specs\07-capture.md`
- `C:\AI_study\2026\GOBI_VibeGuiding\gobi-monorepo\specs\19-orchestration-and-automation.md`

---

### M3 - Capstone — Vibe Guiding 전략 제안서

**난이도**: ⭐⭐⭐
**예상 시간**: 3h
**산출물 폴더**: `03-Capstone/`
**상태**: ⏳ 대기

#### 학습 목표
- [ ] M1 + M2 내용을 통합하여 Vibe Guiding 접목 옵션을 구체화한다
- [ ] 현재 파이프라인 통합 vs 앱 내 에이전트 vs 별도 운영 장단점을 비교한다
- [ ] GOBI 팀이 기대하는 "앱 내 실시간 Vibe Guiding" 구현 가능성과 접근 방식을 제안한다
- [ ] GOBI 팀에 바로 공유 가능한 전략 제안서를 완성한다

#### 핵심 질문 (제안서가 답해야 할 것)
1. Vibe Guiding을 현재 파이프라인(specs → docs)에 통합할 수 있는가? 어떻게?
2. GOBI Desktop / Gobi Space 앱 내에서 Vibe Guiding이 실시간으로 가동되려면 무엇이 필요한가?
3. VibeLearn AI(CUA_VL)가 specs → 사용자 가이드 자동 생성에 어떻게 기여할 수 있는가?
4. Phase 1에서 가장 빠르게 실증할 수 있는 접근 방식은 무엇인가?

#### 실습 과제

**실습 1: 접목 옵션 비교 분석** ⭐⭐⭐
- 옵션 A: specs → VibeLearn AI → Vibe Guiding 컨텍스트 자동 생성 (파이프라인 통합)
- 옵션 B: Second Brain Agent의 Reflex로 Vibe Guiding 구현 (앱 내 통합)
- 옵션 C: Gobi CLI를 통한 Vibe Guiding 독립 운영
- 옵션 D: 혼합 (Phase 1: CLI → Phase 2: 앱 내 통합)
- 산출물: `03-Capstone/integration-options.md`
- **예상 시간**: 60분

**실습 2: 전략 제안서 작성** ⭐⭐⭐
- 권장 접근 방식 선정 + 근거
- Phase 1 구체적 실행 계획 (2-4주 기준)
- GOBI 팀(Mika, Greg)과 공유 가능한 1-2페이지 문서
- 산출물: `03-Capstone/vibe-guiding-strategy-proposal.md`
- **예상 시간**: 90분

**실습 3: Topic Retrospective** ⭐
- 산출물: `03-Capstone/topic-retrospective.md`
- **예상 시간**: 30분

#### Definition of Done
- [ ] 접목 옵션 4개 비교 분석 완성
- [ ] 권장 접근 방식 1개 선정 + 근거
- [ ] GOBI 팀 공유용 전략 제안서 완성 (1-2페이지)
- [ ] Topic Retrospective 작성
- [ ] WorkLog 작성

---

## 📝 WorkLog 작성 가이드

**파일명 규칙**: `vl_worklog/YYYYMMDD_MX_GOBI-Specs-Pipeline.md`
- 예: `vl_worklog/20260406_M1_GOBI-Specs-Pipeline.md`

---

## 📂 전체 폴더 구조

```
GOBI-Specs-Pipeline/
├── topic_info.md
├── vl_prompts/
├── vl_roadmap/
│   └── 20260406_RoadMap_GOBI-Specs-Pipeline.md
├── vl_worklog/
│   ├── 20260406_M1_GOBI-Specs-Pipeline.md
│   └── ...
├── vl_materials/
├── 01-Monorepo-Overview/
│   ├── README.md
│   ├── repo-structure.md
│   └── pipeline-diagram.md
├── 02-Specs-Deep-Dive/
│   ├── README.md
│   ├── spec-analysis-second-brain-agent.md
│   ├── spec-analysis-voice-interaction.md
│   ├── spec-analysis-capture.md
│   ├── spec-analysis-orchestration.md
│   └── vibe-guiding-touchpoints.md
└── 03-Capstone/
    ├── README.md
    ├── integration-options.md
    ├── vibe-guiding-strategy-proposal.md
    └── topic-retrospective.md

[로컬 클론]
C:\AI_study\2026\GOBI_VibeGuiding\
├── gobi-monorepo/   ← Private, 클론 완료
└── docs/            ← Public, 클론 완료
```

---

## 📊 학습 진행 상황 추적

| 모듈 | 시작일 | 종료일 | 상태 | DoD 달성률 |
|------|--------|--------|------|-----------|
| M1 | 2026-04-06 | 2026-04-06 | ✅ 완료 | 8/8 (100%) |
| M2 | 2026-04-07 | 2026-04-07 | ✅ 완료 | 7/7 (100%) |
| M3 | 2026-04-07 | 2026-04-07 | ✅ 완료 | 6/6 (100%) |

---

## 🎯 성공 기준

- [x] 모든 모듈 DoD 완료
- [x] 전략 제안서 완성 (GOBI 팀 공유 가능 수준)
- [x] Topic Retrospective 작성

---

**생성자**: Claude with CUA_VL
**Roadmap 버전**: 1.1 (2026-04-06 재편)
**방법론 버전**: CUA_VL 2.0
