---
title: "WorkLog - M1: Vibe Guiding 개념과 Source Map"
created: 2026-05-03 07:32:15
tags:
  - vibe-guiding
  - vibelearn-ai
  - worklog
  - m1
sources:
  - "[[Ingest/CatchUpAI_VL/Topics/Vibe-Guiding-VSCode/vl_roadmap/20260426_RoadMap_Vibe-Guiding-VSCode#M1 - Vibe Guiding 개념과 Source Map|20260426_RoadMap_Vibe-Guiding-VSCode]]"
  - "[[Ingest/CatchUpAI_VL/Topics/Vibe-Guiding-VSCode/vl_worklog/20260427_M0_Setup_Vibe-Guiding-VSCode#Tomorrow's focus|20260427_M0_Setup_Vibe-Guiding-VSCode]]"
---

## 오늘의 학습 목표

- [x] M1 산출물 폴더 `01-Vision-and-Architecture/` 생성
- [x] 핵심 Source 5개를 읽고 `source-map.md` 초안 작성
- [x] `what-is-vibe-guiding.md`에 30초 설명과 3분 설명 초안 작성
- [x] Vibe Learning vs Vibe Guiding 비교표 작성
- [x] POC 대상 후보 평가 문서 작성
- [x] M1 README 작성

## 진행 내용

### 1. Daily Learning 상태 확인

**목적**: CUA_VL/VibeLearn AI 방식에 따라 Roadmap과 최신 WorkLog를 먼저 확인하고 오늘의 작업 범위를 정한다.

**과정**:
1. `vl_prompts/daily_learning_prompt.md`를 확인했다.
2. `vl_roadmap/20260426_RoadMap_Vibe-Guiding-VSCode.md`에서 M1의 DoD와 산출물을 확인했다.
3. 최신 WorkLog인 `20260427_M0_Setup_Vibe-Guiding-VSCode.md`에서 Tomorrow's focus를 확인했다.

**결과**:
- M0는 Topic 구조 보정 단계였고, M1 실제 산출물은 아직 없음을 확인했다.
- 오늘은 Source Map과 Vibe Guiding 설명문을 우선 작성하기로 했다.

### 2. 핵심 Source 5개 읽기

**목적**: M1 Source Map에 사용할 근거 문서의 역할과 핵심 인사이트를 추출한다.

**확인한 Source**:
- `VibeGuiding_BrainDump.md`
- `2026-04-03 GOBI Vibe Guiding 시스템 맵.md`
- `2026-04-05 Vibe Guiding 구현 계획.md`
- `2026-04-09 - Proposal - Vibe Guiding Architecture for Gobi.md`
- `2026-04-13 Gobi Desktop Vibe Guiding 기능 수준 테스트.md`

**결과**:
- Vibe Guiding은 Vibe Learning으로 생성한 최신 매뉴얼을 사용자 상황에 맞게 활성화하는 시스템으로 정리했다.
- GOBI 적용에서는 전체 제품군 통합보다 VS Code 파일 기반 POC를 먼저 검증하는 것이 적절하다고 판단했다.

### 3. M1 산출물 작성

**목적**: 이후 M2-M5에서 재사용할 수 있는 교과서 품질의 M1 초안 산출물을 만든다.

**생성한 파일**:
- `01-Vision-and-Architecture/source-map.md`
- `01-Vision-and-Architecture/what-is-vibe-guiding.md`
- `01-Vision-and-Architecture/README.md`

**결과**:
- Source별 역할, 원문 인용, 핵심 인사이트, 다음 모듈 사용처를 정리했다.
- 30초 설명, 3분 설명, Vibe Learning vs Vibe Guiding 비교표를 작성했다.
- M1 README에 학습 순서와 DoD 진행 상황을 기록했다.

### 4. POC 대상 후보 평가 완료

**목적**: M4 Guiding Engine POC의 1차 대상을 확정한다.

**과정**:
1. 사용자가 POC 대상을 GOBI CLI로 확정했다.
2. 기존 `GOBI-CLI` Topic의 Setup/Auth, Space/Thread, Capstone 자료를 확인했다.
3. GOBI CLI와 Gobi Desktop Custom Homepage/Applet을 로컬 재현 가능성, 사용자 상태 수집 가능성, 테스트 난이도, 기존 자료 재사용성, GOBI 팀 설득력 기준으로 비교했다.

**결과**:
- `01-Vision-and-Architecture/poc-target-selection.md`를 작성했다.
- M4 1차 POC 대상은 GOBI CLI로 확정했다.
- Gobi Desktop Custom Homepage/Applet은 M5 Scenario Test 대상으로 보류했다.

## 문제 해결 로그

### 문제 1: 기존 M1 산출물 폴더가 없음

**증상**: `01-Vision-and-Architecture/` 폴더가 존재하지 않았다.

**원인**: 지난 세션은 M0 Topic 구조 보정까지 완료했고, M1 실제 학습은 아직 시작하지 않은 상태였다.

**해결**: M1 표준 산출물 폴더를 생성하고, Roadmap의 산출물 목록에 맞춰 `source-map.md`, `what-is-vibe-guiding.md`, `README.md`부터 작성했다.

### 문제 2: POC 대상 후보 평가는 사용자 결정이 필요했음

**증상**: M1 DoD 중 `poc-target-selection.md`는 사용자의 POC 대상 확정 전까지 완료할 수 없었다.

**원인**: GOBI CLI와 Desktop/Applet은 각각 장단점이 있어, 실제로 어떤 앱으로 작업할지 사용자의 방향 확인이 필요했다.

**해결**: 사용자가 GOBI CLI를 1차 POC 대상으로 확정했고, 이를 기준으로 `poc-target-selection.md`를 작성했다.

## DoD 체크리스트

로드맵 M1의 Definition of Done:

- [x] 핵심 Source 5개를 읽고 Source Map 작성
- [x] Vibe Guiding 30초 설명 작성
- [x] Vibe Learning vs Vibe Guiding 비교표 작성
- [x] 첫 POC 대상 후보 평가 완료
- [x] `01-Vision-and-Architecture/README.md` 작성
- [x] WorkLog 작성 및 Daily Retrospective 완료

**완료율**: 6/6 (100%)

## Daily Retrospective

### What went well

M0에서 남긴 Tomorrow's focus를 그대로 이어받아 M1의 핵심 산출물부터 만들었다. Source Map을 먼저 작성하면서 Vibe Guiding이 "문서 검색 챗봇"이 아니라 "최신 매뉴얼을 사용자 상태에 맞게 활성화하는 시스템"이라는 기준이 명확해졌다.

### What could be improved

오늘 M1을 완료하면서 M2로 넘어갈 준비가 끝났다. 다음 세션에서는 새 Source를 넓게 읽기보다, GOBI CLI를 기준으로 컴포넌트 책임과 POC boundary를 구체화해야 한다.

### Insights

Vibe Guiding의 핵심 구현 위험은 LLM 응답 품질보다 사용자 상태 수집과 완료 신호 검증에 있다. Gobi Desktop 테스트 기록에서 드러난 실패도 "AI가 설명을 못함"이 아니라 "현재 설정 상태와 실제 UI를 정확히 모름"에 가까웠다.

### Tomorrow's focus

- GOBI-CLI Topic New 버전 업데이트를 Continuous Vibe Learning 프로세스로 먼저 진행
- GOBI-CLI 업데이트 완료 후 M1 문서 중 수정 필요한 항목 재검토
- 특히 `poc-target-selection.md`, `source-map.md`, `what-is-vibe-guiding.md`에서 GOBI CLI 관련 전제와 참조 자료 업데이트
- M2 시작: `02-Architecture-Design/` 생성
- `component-responsibilities.md` 작성
- `architecture-diagrams.md` 작성
- `poc-boundary.md` 작성
- GOBI CLI 기준으로 Vibe Manual/CVL 컴포넌트와 Guiding Engine 컴포넌트 분리
- 관련 문서 작성이 모두 완료되면 GitHub에 push

## 참조 및 산출물

**생성된 파일/폴더**:
- `01-Vision-and-Architecture/`: M1 산출물 폴더
- `01-Vision-and-Architecture/source-map.md`: 핵심 Source 5개 근거 지도
- `01-Vision-and-Architecture/what-is-vibe-guiding.md`: Vibe Guiding 설명문
- `01-Vision-and-Architecture/poc-target-selection.md`: GOBI CLI POC 대상 확정
- `01-Vision-and-Architecture/README.md`: M1 학습 순서와 DoD 현황
- `vl_worklog/20260503_M1_Vibe-Guiding-VSCode.md`: 오늘 WorkLog
- `vl_worklog/20260503_M1_Retrospective.md`: M1 Retrospective

**다음 세션 준비사항**:
- GOBI-CLI Topic이 old 버전이므로 New 버전으로 CVL 업데이트 진행
- GOBI-CLI CVL 결과를 반영해 M1 산출물의 GOBI CLI 관련 내용 업데이트
- M1 문서 업데이트 후 M2 Architecture Design 시작
- `02-Architecture-Design/` 폴더 생성
- GOBI CLI 기준 컴포넌트 책임표 작성
- Architecture Diagram과 POC Boundary 문서 작성
- 전체 문서 작성 완료 후 GitHub push 진행

**작성자**: Codex with VibeLearn AI
**방법론**: VibeLearn AI
