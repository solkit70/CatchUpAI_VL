# gobi-monorepo + gobi-ai/docs Structure Analysis

**Analysis Date**: 2026-04-06
**Method**: Direct exploration after local clone
**Clone Location**: `C:\AI_study\2026\GOBI_VibeGuiding\`

---

## 1. gobi-monorepo Full Structure

### Top-Level Files / Folders

```
gobi-monorepo/
├── CLAUDE.md               ← Full ecosystem guide for Claude Code
├── LINEAR.md               ← AI agent-based development workflow
├── .runner/
│   └── agents/             ← Agent role definitions
├── prompts/
│   └── CODE_TO_SPECS.md    ← AI prompt for generating specs from code
└── specs/
    ├── README.md           ← SSOT Core Concepts + Feature Index
    └── 01~26.md            ← 26 feature spec files
```

### 7 Projects (each managed as an independent repo)

| # | Project | Stack | Role | Deployment |
|---|---------|-------|------|------------|
| 1 | **gobi-web** | Next.js 16, React 19, TypeScript | Gobi Space web app, user Brain home, community | Vercel |
| 2 | **gobi-desktop** | Electron 38, React 19, Vite, Biome | Local file management, Brain-building creator tool | electron-updater |
| 3 | **gobi-cli** | Node.js ≥18, TypeScript, Commander.js | CLI interface, public npm package (`@gobi-ai/cli`) | npm / Homebrew |
| 4 | **gobi-webdrive** | Python, Flask/Quart | File sync + agent infrastructure + Digital Garden | GKE |
| 5 | **gobi-backend** | NestJS 10, PostgreSQL, Redis, Ably | Main REST API + WebSocket + auth + billing | Cloud Run |
| 6 | **gobi-app** | Flutter (Dart ≥3.2.3), Riverpod | iOS/Android mobile app | App Store / Play |
| 7 | **gobi-cloud** | Python ≥3.12, uv, GCP | Wearable data processing, async pipeline | GKE (Helm) |

### Overall Architecture

```
gobi-app (Flutter)   ─────────────────────────────────┐
gobi-web (Next.js)    ──────────────────────────────── │
gobi-desktop (Electron) ── gobi-backend (NestJS) ──────┤──► PostgreSQL / Redis
gobi-cli (Node.js)    ──────────────────────────────── │
                               │
                   gobi-webdrive (file sync/agents) ───┤──► GCS / GKE
                   gobi-cloud (async processing) ───────┘──► GCP Pub/Sub
```

**Real-time**: Ably (pub/sub), WebSocket (voice/chat)
**AI**: Anthropic (Claude), OpenAI, LangChain, vLLM
**Auth**: Google OAuth, Apple Sign-In, JWT, Firebase

---

## 2. specs/ Directory Structure

### Core Characteristics
- **SSOT (Single Source of Truth)**: Aimed to be complete enough to re-implement the entire product from specs alone
- **Feature-centric**: Organized by feature, not by product (a single spec can span multiple products)
- **Implementation-agnostic**: Written around *what* the feature does, not *how* it is built

### File Format (Markdown)

```markdown
# [Feature Name]

## Overview
Feature overview (1-2 paragraphs)

## Product Surfaces
| Product | Capabilities |
|---------|-------------|
...

## Functional Requirements
### [Sub-feature name]
- Specific requirement list

## User Flows
1. Step-by-step user flow

## Relationships
- Relationships with related features
```

### 26 Feature Spec List

| # | File | Related Products | Vibe Guiding Relevance |
|---|------|-----------------|----------------------|
| 01 | authentication-and-onboarding | All | ⭐ Onboarding |
| 02 | vault-management | Desktop, Backend, CLI, WebDrive | ⭐ |
| 03 | file-management | Desktop | - |
| 04 | file-sync | Desktop, CLI, WebDrive | - |
| **05** | **second-brain-agent** | Desktop, Web, Backend, WebDrive | **⭐⭐⭐ Core** |
| **06** | **voice-interaction** | Desktop, Mobile, Backend | **⭐⭐⭐ Core** |
| **07** | **capture** | Desktop, Mobile, Cloud | **⭐⭐⭐ Core** |
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
| **19** | **orchestration-and-automation** | Desktop | **⭐⭐⭐ Core** |
| 20 | terminal | Desktop | - |
| 21 | digital-garden | WebDrive | - |
| 22 | integrations | Backend, Desktop | ⭐ |
| 23 | gemini-live | Desktop | ⭐⭐ |
| 24 | data-processing-pipeline | Cloud | - |
| 25 | settings-and-configuration | Desktop, Web, Mobile | ⭐ |
| 26 | real-time-communication | Backend, Web, Desktop | - |

> M2 will deep-dive into the 4 ⭐⭐⭐ files (05, 06, 07, 19)

---

## 3. gobi-ai/docs Repository Structure

### Framework: Mintlify

```
docs/
├── docs.json           ← Site config (navigation, theme, colors)
├── index.mdx           ← Homepage
├── AGENTS.md           ← AI agent instructions (Mintlify default template)
├── products/
│   ├── desktop.mdx
│   ├── community-space.mdx
│   ├── cli.mdx
│   └── mobile.mdx
├── reference/
│   ├── glossary.mdx
│   └── ecosystem.mdx
└── (other Mintlify example files)
```

### docs.json Navigation Structure

```
Docs tab
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

### Key Finding: Pipeline is Manual

- gobi-monorepo/specs (Markdown) → gobi-ai/docs (MDX) conversion: **Manual**
- gobi-ai/docs push → Mintlify auto build → docs.gobihq.com: **Automatic**
- Even when the dev team writes a spec, a separate MDX authoring step is required to reflect it in docs
- **This manual conversion step is the core opportunity for Vibe Guiding / VibeLearn AI**

---

## 4. AI Agent Workflow (LINEAR.md)

gobi-monorepo already operates an AI agent-based development pipeline:

```
Created (Human)
    ↓
Planner AI → AskUserQuestion or Planned
    ↓
Plan-Reviewer AI → Approved
    ↓
Developer AI → ReviewNeeded (PR created)
    ↓
PR Reviewer Agents → HumanReview
    ↓
Done (Human merge)
```

**Vibe Guiding implication**: Agents are already integrated into the development pipeline. Vibe Guiding can be added as a similar agent role in the documentation pipeline.

---

## 5. CODE_TO_SPECS.md Analysis

**Location**: `gobi-monorepo/prompts/CODE_TO_SPECS.md`

**Purpose**: Prompt for AI to read the entire codebase and generate spec files

**Key Instructions**:
1. Cover all feature specs (10–30)
2. Write in maximum detail from a feature perspective
3. Do not reference code or implementation details (feature definition only)
4. A single feature may span multiple repos
5. Review the codebase at least 10 times before finalizing
6. After completion, cross-check the full codebase against specs to eliminate duplication

**VibeLearn AI implication**: The reverse of CODE_TO_SPECS — **SPECS_TO_GUIDE** (generating user guides from specs). The existence of CODE_TO_SPECS signals the dev team is already aligned with this AI-pipeline approach.
