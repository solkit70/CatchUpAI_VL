---
title: "WorkLog - M2: Two-Component Architecture Design"
created: 2026-05-10 06:32:59
tags:
  - vibe-guiding
  - vibelearn-ai
  - worklog
  - m2
sources:
  - "[[Ingest/CatchUpAI_VL/Topics/Vibe-Guiding-VSCode/vl_worklog/20260503_M1_Retrospective#다음 모듈 준비사항|M1 Retrospective]]"
  - "[[Ingest/CatchUpAI_VL/Topics/GOBI-CLI/vl_worklog/20260510_CVL_GOBI-CLI#GOBI CLI v2.0 주요 변경사항|GOBI CLI CVL WorkLog]]"
---

## 오늘의 학습 목표

- [x] GOBI-CLI CVL 업데이트 결과 검증
- [x] GOBI-CLI Topic README 계열의 오래된 v0.6.15 진입 문구 보정
- [x] Vibe-Guiding M1 문서의 GOBI CLI 전제를 v2.0.12 기준으로 보정
- [x] M2 산출물 폴더 `02-Architecture-Design/` 생성
- [x] `component-responsibilities.md` 작성
- [x] `architecture-diagrams.md` 작성
- [x] `poc-boundary.md` 작성
- [x] M2 README 작성

## 진행 내용

### 1. GOBI-CLI CVL 검증

`Topics/GOBI-CLI`에서 v0.6.15, `gobi init`, `BRAIN.md`, `create-thread`, `list-threads`, `session reply` 같은 구 표현을 검색했다. 핵심 guide 본문은 v2.0.12로 업데이트되어 있었지만, Topic 진입점인 `README.md`와 각 모듈 README에는 오래된 v0.6.15 기준 설명이 남아 있었다.

### 2. GOBI-CLI 진입 문서 보정

다음 README 파일을 v2.0.12 기준으로 보정했다.

- `Topics/GOBI-CLI/README.md`
- `Topics/GOBI-CLI/01-Setup-Auth/README.md`
- `Topics/GOBI-CLI/02-Brain-Session/README.md`
- `Topics/GOBI-CLI/03-Space-Thread/README.md`
- `Topics/GOBI-CLI/04-Capstone/README.md`

주요 보정은 `gobi init`을 `gobi vault init`으로, `BRAIN.md`를 `PUBLISH.md`로, `Thread`를 `Post`로, `brain post-update`를 `global create-post`로 바꾸는 것이었다.

### 3. Vibe-Guiding M1 보정

`01-Vision-and-Architecture/poc-target-selection.md`에서 POC 시나리오의 구 `Thread` 표현을 GOBI CLI v2.0.12 기준 `Post` 표현으로 바꿨다. 이로써 M2 설계는 GOBI CLI 최신 명령어 체계를 기준으로 이어갈 수 있게 됐다.

### 4. M2 Architecture Design 착수

Roadmap의 M2 DoD에 맞춰 `02-Architecture-Design/` 폴더를 만들고 다음 문서를 작성했다.

- `README.md`
- `component-responsibilities.md`
- `architecture-diagrams.md`
- `poc-boundary.md`

## 문제 해결 로그

### 문제: CVL 업데이트가 본문 가이드에는 반영됐지만 README에는 남아 있음

**증상**: `rg` 검색 결과 `Topics/GOBI-CLI/README.md`, `01-Setup-Auth/README.md`, `02-Brain-Session/README.md`, `03-Space-Thread/README.md`, `04-Capstone/README.md`에서 v0.6.15 기준 설명이 확인됐다.

**해결**: 현재 학습자가 가장 먼저 보는 한국어 README 계열을 v2.0.12 기준으로 정리했다. 과거 WorkLog와 Roadmap의 구 표현은 역사 기록으로 보존했다.

## DoD 체크리스트

- [x] 컴포넌트 책임표 작성
- [x] Vibe Manual/CVL 다이어그램 작성
- [x] Guiding Engine 다이어그램 작성
- [x] POC 범위와 제외 범위 정의
- [x] `02-Architecture-Design/README.md` 작성
- [x] WorkLog 작성

**완료율**: 6/6 (100%)

## Daily Retrospective

### What went well

M2로 바로 넘어가기 전에 GOBI-CLI CVL 결과를 검증한 것이 좋았다. 핵심 가이드 문서는 이미 업데이트되어 있었지만 README 진입점이 오래된 상태였기 때문에, 그대로 M2를 설계했다면 `Thread`와 `Post`가 섞인 아키텍처가 되었을 가능성이 있었다.

### What could be improved

영문 `.en.md` 파일과 과거 WorkLog에는 여전히 v0.6.x 표현이 남아 있다. 과거 WorkLog는 역사 기록으로 보존하는 것이 맞지만, 영문 현재 가이드는 별도 세션에서 같은 기준으로 업데이트할 필요가 있다.

### Insights

Vibe Guiding에서 CVL은 단순 문서 업데이트가 아니라 Retrieval 품질을 지키는 핵심 장치다. 최신 명령어 체계가 README와 index에 반영되지 않으면 Guiding Engine은 사용자가 막힌 순간에 구 명령어를 안내할 수 있다.

### Tomorrow's focus

- M3 시작: `03-Vibe-Manual-CVL/` 생성
- GOBI CLI v2.0.12 문서를 기준으로 `manual_index.json` 스키마 설계
- `trigger_rules.json` 초안 작성
- M4 POC에서 사용할 샘플 `user_context.json` 후보 정의
