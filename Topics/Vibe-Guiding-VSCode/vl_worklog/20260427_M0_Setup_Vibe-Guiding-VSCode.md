---
title: "WorkLog - M0: VibeLearn AI Topic 구조 보정"
created: 2026-04-27 00:00:00
tags:
  - vibe-guiding
  - vibelearn-ai
  - worklog
  - setup
sources:
  - "[[VibeGuiding_BrainDump]]"
  - "[[2026-04-03 GOBI Vibe Guiding 시스템 맵]]"
  - "[[2026-04-05 Vibe Guiding 구현 계획]]"
  - "[[2026-04-09 - Proposal - Vibe Guiding Architecture for Gobi]]"
  - "[[2026-04-13 Gobi Desktop Vibe Guiding 기능 수준 테스트]]"
---

## 오늘의 학습 목표

- [x] `Vibe-Guiding-VSCode` Topic 폴더를 VibeLearn AI 방법론의 표준 구조에 맞게 보정한다.
- [x] `vl_prompts/roadmap_prompt.md`와 `vl_prompts/daily_learning_prompt.md`를 생성한다.
- [x] Roadmap을 `roadmap_prompt.md`의 형식에 맞게 다시 작성한다.
- [x] 다음 학습 세션에서 바로 M1을 시작할 수 있도록 현재 상태를 정리한다.

## 진행 내용

### 1. 기존 Roadmap 문제 확인

처음 작성된 Roadmap은 Vibe Guiding 학습과 개발 방향을 담고 있었지만, VibeLearn AI 방법론의 실행 구조를 충분히 따르지 않았다. 특히 `vl_prompts/` 폴더와 Topic 전용 `roadmap_prompt.md`, `daily_learning_prompt.md`가 없었고, 실제 Roadmap도 `roadmap_prompt_template.md`의 9개 필수 항목 구조를 완전히 반영하지 못했다.

### 2. VibeLearn AI 기준 문서 재확인

다음 문서를 기준으로 Topic 구조와 Roadmap 요구사항을 다시 확인했다.

- `CLAUDE.md`: VibeLearn AI 워크플로우와 Phase 1-4 규칙 확인
- `README.md`: Topic 폴더 구조, `vl_` 접두사, WorkLog/Retrospective 규칙 확인
- `GETTING_STARTED.md`: Topic 생성 후 `vl_prompts`를 통해 Roadmap과 Daily Learning을 진행하는 흐름 확인
- `Topics/Claude-Skills/02-Skill-A-CUA-VL/examples/cua-vl-skill/SKILL.md`: Skill 기반 CUA_VL/VibeLearn AI 실행 방식 확인

### 3. Topic 폴더 구조 보정

`Vibe-Guiding-VSCode` Topic 폴더를 아래 구조로 맞췄다.

```text
Vibe-Guiding-VSCode/
├── topic_info.md
├── vl_prompts/
│   ├── roadmap_prompt.md
│   └── daily_learning_prompt.md
├── vl_roadmap/
│   └── 20260426_RoadMap_Vibe-Guiding-VSCode.md
├── vl_worklog/
└── vl_materials/
```

`vl_materials/`는 Substack 본문 캡처, GOBI docs/specs export, 테스트 로그, 샘플 JSON 등을 저장할 위치로 추가했다. 아직 자료 파일은 넣지 않았다.

### 4. Topic 전용 Prompt 생성

`templates/roadmap_prompt_template.md`를 기반으로 `vl_prompts/roadmap_prompt.md`를 생성했다. `[1단계] Topic 정보` 섹션에는 `Vibe-Guiding-VSCode`의 Topic 설명, 학습 목적, 기간, 환경, 사전 지식, 학습 목표, 참조 자료, `vl_materials` 사용 계획을 주입했다. 나머지 `[2단계]`, `[3단계]` 지시 섹션은 템플릿 구조를 유지했다.

`templates/daily_learning_prompt.md`를 기반으로 `vl_prompts/daily_learning_prompt.md`도 생성했다. 첫 학습 세션 기준으로 Topic 이름, Topic 폴더 경로, Roadmap 경로, 현재 모듈 `M1 - Vibe Guiding 개념과 Source Map`, 최근 WorkLog `없음 - 첫 학습 세션`을 반영했다.

### 5. Roadmap 재작성

`vl_roadmap/20260426_RoadMap_Vibe-Guiding-VSCode.md`를 VibeLearn AI Roadmap 형식으로 다시 작성했다. 주요 변경점은 다음과 같다.

- 학습 기간 적정성 분석 추가
- 전체 Roadmap 구조를 M1-M6로 정리
- 각 모듈마다 9개 필수 항목 포함
  - 모듈 기본 정보
  - 학습 목표
  - 주요 개념
  - 실습 과제
  - 산출물
  - Definition of Done
  - Self-Assessment
  - 예상 시간 배분
  - 참조 자료
- WorkLog 작성 가이드와 Retrospective 가이드 추가
- 전체 폴더 구조와 진행 상황 추적 표 추가
- 첫 Daily Learning 시작 정보 추가

## 생성 및 수정한 산출물

- `topic_info.md`: 기존 Topic 정보 유지
- `vl_prompts/roadmap_prompt.md`: Topic 정보가 주입된 Roadmap 생성 프롬프트
- `vl_prompts/daily_learning_prompt.md`: 첫 세션 정보가 반영된 Daily Learning 프롬프트
- `vl_roadmap/20260426_RoadMap_Vibe-Guiding-VSCode.md`: VibeLearn AI 형식으로 재작성된 Roadmap
- `vl_materials/`: 참조 자료 저장용 폴더
- `vl_worklog/20260427_M0_Setup_Vibe-Guiding-VSCode.md`: 오늘 WorkLog

## 문제 해결 로그

### 문제 1: Roadmap이 VibeLearn AI 구조를 따르지 않음

**증상**: Roadmap 내용은 있었지만 `vl_prompts` 기반 흐름이 없었고, Roadmap이 `roadmap_prompt_template.md`의 표준 형식으로 생성된 결과물이라고 보기 어려웠다.

**원인**: 초기 작업에서 Vibe Guiding의 내용 정리에 집중하면서 VibeLearn AI의 Phase 1 구조 생성 절차를 생략했다.

**해결**: 방법론 문서와 Skill 예시를 다시 읽고, `vl_prompts`, `vl_materials`를 포함한 Topic 표준 구조를 만든 뒤 Roadmap을 다시 작성했다.

### 문제 2: Daily Learning 시작 정보와 Roadmap 모듈명이 불일치

**증상**: `daily_learning_prompt.md`의 현재 모듈명이 Roadmap의 M1 제목과 다르게 들어갔다.

**원인**: Roadmap 재작성 전의 임시 모듈명을 사용했다.

**해결**: Daily prompt의 현재 모듈을 `M1 - Vibe Guiding 개념과 Source Map`으로 수정했다.

## DoD 체크리스트

- [x] VibeLearn AI 기준 문서 확인
- [x] `vl_prompts/` 폴더 생성
- [x] `vl_materials/` 폴더 생성
- [x] `roadmap_prompt.md` 생성
- [x] `daily_learning_prompt.md` 생성
- [x] Roadmap을 VibeLearn AI 표준 형식으로 재작성
- [x] Roadmap 내 모듈 6개 구성 확인
- [x] wiki link 대상 존재 확인
- [x] WorkLog 작성

**완료율**: 9/9 (100%)

## Daily Retrospective

### What went well

Vibe Guiding의 내용 방향은 유지하면서도 VibeLearn AI가 요구하는 실행 구조로 Topic을 바로잡았다. 특히 `roadmap_prompt.md`를 만든 뒤 Roadmap을 다시 작성했기 때문에 다음 세션부터는 방법론의 정상 흐름인 Daily Learning으로 이어갈 수 있다.

### What could be improved

처음부터 `CLAUDE.md`, `README.md`, `GETTING_STARTED.md`, Skill 예시를 확인하고 시작했어야 했다. 앞으로 VibeLearn AI Topic을 새로 만들 때는 내용 Roadmap을 쓰기 전에 반드시 `vl_prompts` 생성 여부부터 확인한다.

### Insights

VibeLearn AI에서 `vl_prompts`는 단순 보조 파일이 아니라 학습 세션의 재현성과 지속성을 보장하는 핵심 인터페이스다. Roadmap 자체보다 Roadmap을 생성하게 만든 Prompt가 남아 있어야 다음 AI 세션에서도 같은 방법론과 같은 의도를 복원할 수 있다.

### Tomorrow's focus

- M1 시작: `01-Vision-and-Architecture/source-map.md` 작성
- 핵심 Source 5개를 Source Map으로 정리
- `Vibe Guiding 30초 설명`과 `Vibe Learning vs Vibe Guiding 비교표` 작성
- POC 대상 후보를 `GOBI CLI`와 `GOBI Desktop Custom Homepage/Applet` 중심으로 평가

## 다음 세션 준비사항

다음 세션은 아래 프롬프트를 사용해서 시작한다.

```text
Topics/Vibe-Guiding-VSCode/vl_prompts/daily_learning_prompt.md 파일을 읽고
오늘의 학습을 도와주세요.

현재 상황:
- Roadmap 파일: Topics/Vibe-Guiding-VSCode/vl_roadmap/20260426_RoadMap_Vibe-Guiding-VSCode.md
- 현재 모듈: M1 - Vibe Guiding 개념과 Source Map
- 최근 WorkLog: Topics/Vibe-Guiding-VSCode/vl_worklog/20260427_M0_Setup_Vibe-Guiding-VSCode.md
- 사용 가능한 시간: [다음 세션에서 입력]
```

## 참조 및 산출물

**참조 자료**:
- `CLAUDE.md`: VibeLearn AI Phase 1-4 워크플로우
- `README.md`: Topic 폴더 구조와 WorkLog/Retrospective 규칙
- `GETTING_STARTED.md`: `vl_prompts` 기반 Roadmap/Daily Learning 사용 흐름
- `Topics/Claude-Skills/02-Skill-A-CUA-VL/examples/cua-vl-skill/SKILL.md`: CUA_VL Skill 실행 절차

**작성자**: Codex with VibeLearn AI  
**방법론**: VibeLearn AI
