# gobi-monorepo + gobi-ai/docs 구조 분석

**분석일**: 2026-04-06
**방법**: 로컬 클론 후 직접 탐색
**클론 위치**: `C:\AI_study\2026\GOBI_VibeGuiding\`

---

## 1. gobi-monorepo 전체 구조

### 최상위 파일/폴더

```
gobi-monorepo/
├── CLAUDE.md               ← Claude Code용 전체 에코시스템 가이드
├── LINEAR.md               ← AI 에이전트 기반 개발 워크플로우
├── .runner/
│   └── agents/             ← 에이전트 역할 정의
├── prompts/
│   └── CODE_TO_SPECS.md    ← 코드에서 spec을 생성하는 AI 프롬프트
└── specs/
    ├── README.md           ← SSOT Core Concepts + Feature Index
    └── 01~26.md            ← 26개 feature spec 파일
```

### 7개 프로젝트 (각 독립 레포로 분리 관리)

| # | 프로젝트 | 스택 | 역할 | 배포 |
|---|---------|------|------|------|
| 1 | **gobi-web** | Next.js 16, React 19, TypeScript | Gobi Space 웹앱, 사용자 Brain 홈, 커뮤니티 | Vercel |
| 2 | **gobi-desktop** | Electron 38, React 19, Vite, Biome | 로컬 파일 관리, Brain 빌딩 크리에이터 도구 | electron-updater |
| 3 | **gobi-cli** | Node.js ≥18, TypeScript, Commander.js | CLI 인터페이스, npm 공개 패키지 (`@gobi-ai/cli`) | npm / Homebrew |
| 4 | **gobi-webdrive** | Python, Flask/Quart | 파일 싱크 + 에이전트 인프라 + Digital Garden | GKE |
| 5 | **gobi-backend** | NestJS 10, PostgreSQL, Redis, Ably | 메인 REST API + WebSocket + 인증 + 빌링 | Cloud Run |
| 6 | **gobi-app** | Flutter (Dart ≥3.2.3), Riverpod | iOS/Android 모바일 앱 | App Store / Play |
| 7 | **gobi-cloud** | Python ≥3.12, uv, GCP | 웨어러블 데이터 처리, 비동기 파이프라인 | GKE (Helm) |

### 전체 아키텍처

```
gobi-app (Flutter)   ─────────────────────────────────┐
gobi-web (Next.js)    ──────────────────────────────── │
gobi-desktop (Electron) ── gobi-backend (NestJS) ──────┤──► PostgreSQL / Redis
gobi-cli (Node.js)    ──────────────────────────────── │
                               │
                   gobi-webdrive (파일 싱크/에이전트) ──┤──► GCS / GKE
                   gobi-cloud (비동기 처리) ────────────┘──► GCP Pub/Sub
```

**실시간**: Ably (pub/sub), WebSocket (음성/채팅)
**AI**: Anthropic (Claude), OpenAI, LangChain, vLLM
**인증**: Google OAuth, Apple Sign-In, JWT, Firebase

---

## 2. specs/ 디렉토리 구조

### 핵심 특징
- **SSOT (Single Source of Truth)**: 이 스펙만으로 전체 제품을 재구현할 수 있는 수준 목표
- **기능 중심 (Feature-centric)**: 제품별이 아닌 기능별로 구성 (하나의 spec이 여러 제품에 걸침)
- **구현 방식 제외**: "어떻게(How)"가 아닌 "무엇을(What)" 기준으로 작성

### 파일 포맷 (Markdown)

```markdown
# [Feature Name]

## Overview
기능 개요 (1-2 단락)

## Product Surfaces
| Product | Capabilities |
|---------|-------------|
...

## Functional Requirements
### [서브 기능명]
- 구체적 요구사항 목록

## User Flows
1. 단계별 사용자 흐름

## Relationships
- 연관 기능과의 관계
```

### 26개 Feature Spec 목록

| # | 파일 | 관련 제품 | Vibe Guiding 관련도 |
|---|------|----------|-------------------|
| 01 | authentication-and-onboarding | All | ⭐ 온보딩 |
| 02 | vault-management | Desktop, Backend, CLI, WebDrive | ⭐ |
| 03 | file-management | Desktop | - |
| 04 | file-sync | Desktop, CLI, WebDrive | - |
| **05** | **second-brain-agent** | Desktop, Web, Backend, WebDrive | **⭐⭐⭐ 핵심** |
| **06** | **voice-interaction** | Desktop, Mobile, Backend | **⭐⭐⭐ 핵심** |
| **07** | **capture** | Desktop, Mobile, Cloud | **⭐⭐⭐ 핵심** |
| 08 | brain-updates | Web, Backend, CLI, Desktop | ⭐⭐ |
| 09 | spaces | Web, Backend, CLI, Desktop | ⭐⭐ |
| 10 | threads-and-discussions | Web, Backend, CLI, Desktop | ⭐ |
| 11 | search-and-discovery | Web, Backend, CLI | ⭐⭐ |
| 12 | knowledge-graph-visualization | Web, Desktop | - |
| 13 | audio-log-and-meeting-canvas | Web | ⭐ |
| 14 | activity-tracking | Mobile, Backend, Cloud, Desktop, CLI | ⭐ |
| 15 | device-and-wearable-integration | Mobile, Backend, Cloud | - |
| 16 | notifications | Desktop, Mobile, Backend | ⭐ |
| 17 | billing-and-credits | Backend, Desktop, Web | - |
| 18 | managed-voices | Mobile, Backend, Desktop | ⭐ |
| **19** | **orchestration-and-automation** | Desktop | **⭐⭐⭐ 핵심** |
| 20 | terminal | Desktop | - |
| 21 | digital-garden | WebDrive | - |
| 22 | integrations | Backend, Desktop | ⭐ |
| 23 | gemini-live | Desktop | ⭐⭐ |
| 24 | data-processing-pipeline | Cloud | - |
| 25 | settings-and-configuration | Desktop, Web, Mobile | ⭐ |
| 26 | real-time-communication | Backend, Web, Desktop | - |

> M2에서 ⭐⭐⭐ 4개 (05, 06, 07, 19) 심층 분석 예정

---

## 3. gobi-ai/docs 레포 구조

### 프레임워크: Mintlify

```
docs/
├── docs.json           ← 사이트 설정 (내비게이션, 테마, 색상)
├── index.mdx           ← 홈페이지
├── AGENTS.md           ← AI 에이전트 작업 지침 (Mintlify 기본 템플릿)
├── products/
│   ├── desktop.mdx
│   ├── community-space.mdx
│   ├── cli.mdx
│   └── mobile.mdx
├── reference/
│   ├── glossary.mdx
│   └── ecosystem.mdx
└── (기타 Mintlify 예시 파일들)
```

### docs.json 내비게이션 구조

```
Docs 탭
├── Introduction → index
├── Products
│   ├── Desktop
│   ├── Community Space
│   ├── CLI
│   └── Mobile
└── Reference
    ├── Glossary
    └── Ecosystem
```

### 핵심 발견: 파이프라인이 수동

- gobi-monorepo/specs (Markdown) → gobi-ai/docs (MDX) 변환: **수동**
- gobi-ai/docs push → Mintlify 자동 빌드 → docs.gobihq.com: **자동**
- 즉, 개발팀이 spec을 작성해도 docs에 반영하려면 별도 MDX 작업 필요
- **이 수동 변환 단계가 Vibe Guiding/VibeLearn AI의 핵심 기회**

---

## 4. AI 에이전트 워크플로우 (LINEAR.md)

gobi-monorepo는 이미 AI 에이전트 기반 개발 파이프라인을 운영 중:

```
Created (Human)
    ↓
Planner AI → AskUserQuestion 또는 Planned
    ↓
Plan-Reviewer AI → Approved
    ↓
Developer AI → ReviewNeeded (PR 생성)
    ↓
PR Reviewer Agents → HumanReview
    ↓
Done (Human merge)
```

**Vibe Guiding 함의**: 에이전트가 이미 개발 파이프라인에 통합되어 있음. Vibe Guiding도 유사한 에이전트 역할로 문서화 파이프라인에 통합 가능.

---

## 5. CODE_TO_SPECS.md 분석

**위치**: `gobi-monorepo/prompts/CODE_TO_SPECS.md`

**목적**: AI가 전체 코드베이스를 읽고 spec 파일을 생성하는 프롬프트

**주요 지침**:
1. 모든 기능 스펙을 커버할 것 (10~30개)
2. 기능 관점으로 최대한 상세하게 작성
3. 코드/구현 방식 참조 금지 (기능 정의만)
4. 하나의 기능이 여러 레포에 걸칠 수 있음
5. 한 번에 완성하지 말고 최소 10회 코드베이스 재검토
6. 완성 후 전체 코드베이스와 스펙을 대조하여 중복 제거

**VibeLearn AI 함의**: CODE_TO_SPECS와 역방향 — **SPECS_TO_GUIDE** (스펙에서 사용자 가이드 생성). 이미 이 방향의 아이디어가 개발팀에 있음을 시사.
