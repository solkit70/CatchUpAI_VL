---
title: "20260712 M1 Build with AI WorkLog"
created: 2026-07-12 05:49:58
tags:
  - vibelearn-ai
  - worklog
  - build-with-ai
---

# WorkLog - M1: Build with AI 완독·이해 → Source Map/Thesis

**날짜**: 2026-07-12
**Topic**: Build-with-AI
**모듈**: M1 - Build with AI 완독·이해 → Source Map/Thesis
**학습 시간**: Live18 방송 중 시작, 이후 독립 학습 세션으로 계속 진행
**방법론**: VibeLearn AI
**절차 상태**: 2026-07-12 06:30 사후 절차 복구, 2026-07-12 사용자 Reading notes 검토 게이트 추가

> **중요 정정**: `01-Source-Map/reading-notes.md`는 AI가 원본 자료와 사용자의 기존 문서를 바탕으로 정리한 초안이다. 사용자가 이 문서를 직접 읽고 자신의 생각/동의/반박/수정 사항을 정리하기 전에는 M1을 최종 완료로 처리하지 않는다.

## 오늘의 학습 목표

- [x] VibeLearn AI Daily Learning 프롬프트 기준으로 현재 상태 확인
- [x] Roadmap과 기존 WorkLog를 비교해 정식 진행 위치 확인
- [x] 원본 자료 위치 확인
- [x] M1 읽기 노트 3부 추가
- [x] Part 0, 2부, 4~12부 이해 노트 보강
- [x] `reading-notes.md` 기준으로 Source Map/Thesis 업데이트
- [x] `01-Source-Map/README.md` 학습 순서 업데이트
- [ ] 사용자가 `reading-notes.md`를 직접 읽고 자신의 생각으로 정리했는지 확인

## 진행 내용

### 1. 현재 상태 확인

`vl_prompts/daily_learning_prompt.md`, `vl_roadmap/20260705_RoadMap_Build-with-AI.md`, `vl_worklog/20260705_M1_Build-with-AI.md`를 확인했다. 기존에는 Source Map, 첫 영상 angle, video brief까지 만들어져 있었지만, Roadmap에는 "기존 M1~M3 산출물은 정식 절차 이전 산출물이므로 참고용이고, M1부터 정식 절차로 재시작"한다고 명시되어 있었다.

따라서 오늘의 정식 진행 위치는 M3 스크립트 작성이 아니라 M1의 `reading-notes.md` 보강이다. 방송에서는 이 점을 설명하고, VibeLearn AI 프로세스가 산출물보다 먼저 원문 이해를 요구한다는 것을 보여주는 방식으로 진행했다.

### 2. 원본 자료 위치 확인

Topic 폴더 안에는 PDF/EPUB 원본이 없었지만, source note에 연결된 실제 자료 위치를 확인했다.

- `AI/Initiatives/Builders Lounge/builders/Song-Jae-hee-Build-with-AI/materials/build-with-ai-complete-ko.pdf`
- `AI/Initiatives/Builders Lounge/builders/Song-Jae-hee-Build-with-AI/materials/build-with-ai-complete-ko.epub`
- `AI/Initiatives/Builders Lounge/builders/Song-Jae-hee-Build-with-AI/materials/build-with-ai-complete-en.pdf`
- 하위 챕터 한/영 PDF 자료들

PDF 텍스트 추출 도구는 없었지만, EPUB은 XHTML 구조라 3부 텍스트를 확인할 수 있었다.

### 3. 3부 읽기 노트 추가

`01-Source-Map/reading-notes.md`에 3부 "AI 레고 스택" 이해 노트를 추가했다. 핵심은 AI 솔루션을 `모델 / 오케스트레이션 / 인터페이스` 세 레이어로 나누어 보면 도구 혼란이 줄어든다는 점이다.

내 관점에서는 이 3부가 Builders Lounge와 Bila AI Agent를 설명하기 좋은 bridge가 된다. 모델은 답변과 판단을 만들고, 오케스트레이션은 멤버 자료와 Product 상태를 연결하며, 인터페이스는 GobiSpace, Slack, 이메일, Q&A 화면이 될 수 있다.

### 4. Part 0~12 완독 이해 노트 완성

방송 이후 사용자가 방송 진행은 더 이상 신경 쓰지 말고 VibeLearn AI 학습으로 계속 진행하라고 요청했다. 이에 따라 M1 실습1을 계속 진행했다.

`build-with-ai-complete-ko.epub`에서 Part 0, 2부, 4~12부를 확인하고 `01-Source-Map/reading-notes.md`를 보강했다. 기존에는 1부, 2부, 3부만 있었고 2부도 간단한 메모 수준이었으나, 이제 Part 0~12 전체에 대해 `핵심 주장 (원문)`과 `내 생각`을 남겼다.

핵심적으로 도출된 흐름:

1. Part 0~3: AI를 쓰는 사고 모델과 스택 구조
2. Part 4~6: 데이터, 문제 정의, 프롬프팅이라는 입력 품질
3. Part 7~9: Agent, 바이브 코딩, 코드 어시스턴트라는 구축 방식
4. Part 10~11: 데모에서 프로덕션으로 가기 위한 검증과 책임
5. Part 12: 다음 물결과 도메인 지식의 중요성

### 5. Source Map/Thesis 정식 업데이트

`reading-notes.md`를 기준으로 `01-Source-Map/build-with-ai-source-map.md`를 업데이트했다. 기존 Source Map은 방향은 맞았지만, 정식 M1 이해 노트 이전에 작성된 참고용 산출물이었다. 오늘 업데이트에서는 다음을 보강했다.

- Core Thesis를 `문제 정의·데이터·검증·운영 기준` 중심으로 정교화
- Part 0~12 각각의 `Role in Source`와 `Video Use` 재정리
- Video Thesis Candidates 추가
- Builders Lounge Connection에 Part 4와 Part 7 연결 보강
- Proposed First Video Structure 추가

`01-Source-Map/README.md`도 학습 순서와 M1 상태를 반영해 업데이트했다.

### 6. VibeLearn AI 절차 복구 및 M1 사후 검토

사용자가 지적한 대로, 원래 VibeLearn AI 일일 학습은 오늘의 학습 계획을 먼저 제시하고 사용자 승인을 받은 뒤 실행해야 한다. 이 세션에서는 그 승인 게이트가 생략된 상태로 M1~M3 산출물이 진행되었으므로, 2026-07-12 06:30에 별도 학습 계획을 제시하고 사용자 승인을 받은 뒤 절차 복구를 진행했다.

복구 기준은 다음과 같다. M1은 자료 완독과 이해 노트 작성이 중심이었고 사용자가 요청한 "영상 제작 전에 자료 공부" 의도와 일치하므로, `reading-notes.md`, `build-with-ai-source-map.md`, `README.md`를 사후 검토해 정식 M1 산출물로 인정한다. 반면 M2와 M3는 영상 angle/script starter 단계이므로, 정식 완료가 아니라 승인 전 선행 초안으로 분리한다.

검토 결과 `reading-notes.md`는 Part 0~12 각각에 대해 원문 핵심 주장과 개인 해석을 포함하고 있으며, `build-with-ai-source-map.md`는 그 이해 노트에서 thesis와 Part별 활용 가능성을 도출하고 있다. 따라서 M1의 학습 순서는 "자료 이해 → Source Map/Thesis 정리"로 확인되었다.

### 7. 원본 자료 안내를 M1 산출물로 편입

사용자가 `vl_materials/`에 원본 자료를 찾을 수 없고, Build with AI 설명과 다운로드 정보가 산출물에 빠져 있다고 지적했다. 확인 결과 `Ingest/CatchUpAI_VL/Topics/Build-with-AI/vl_materials/`는 비어 있었고, 실제 다운로드된 원본은 `AI/Initiatives/Builders Lounge/builders/Song-Jae-hee-Build-with-AI/materials/`에 있었다.

처음에는 안내 문서를 `vl_materials/`에 두었지만, 사용자가 이 내용은 M1 산출물에 속한다고 지적했다. 이에 따라 안내 문서를 `01-Source-Map/source-materials.md`로 편입했다. 이 문서에는 Build with AI 설명, 공식 한국어 홈, 다운로드 페이지, Topic 안의 로컬 PDF/EPUB/치트시트 파일 목록, 각 자료의 역할, 학습 전 확인 순서를 정리했다.

또한 Builders Lounge 쪽 `materials/`에 있던 PDF/EPUB/치트시트 원본 파일을 `Ingest/CatchUpAI_VL/Topics/Build-with-AI/vl_materials/`로 복사했다. 이제 `vl_materials/`는 원본 자료 보관 폴더이고, `01-Source-Map/source-materials.md`는 그 자료들을 설명하는 M1 산출물이다. Roadmap도 M1의 실습0 `원본 자료 확인 및 학습 입구 정리`로 수정했다.

## 문제 해결 로그

### 문제: Topic 폴더 안에서 원본 자료가 바로 보이지 않음

**증상**: `Ingest/CatchUpAI_VL/Topics/Build-with-AI` 내부에는 PDF/EPUB 원본이 없었다.

**원인**: 원본 자료는 Topic 폴더가 아니라 Builders Lounge source note 하위 `materials/` 폴더에 저장되어 있었다.

**해결**: `AI/Initiatives/Builders Lounge/builders/Song-Jae-hee-Build-with-AI/2026-06-29 Build with AI source note.md`의 링크를 따라 실제 자료 위치를 확인했다. 이후 원본 파일을 Topic의 `vl_materials/`로 복사하고, M1 산출물인 `01-Source-Map/source-materials.md`에서 원본 위치와 다운로드 정보를 바로 찾을 수 있게 했다.

## DoD 체크리스트

Roadmap M1 Definition of Done:

- [x] AI가 Build with AI 완전판을 읽고 Reading notes 초안을 작성했다.
- [x] `source-materials.md`에 원본 자료 설명, 공식 다운로드 위치, `vl_materials/` 파일 목록이 정리되었다.
- [x] Part 0~12 각각의 핵심 주장이 `reading-notes.md`에 정리되었다.
- [ ] 사용자가 `reading-notes.md`를 직접 읽고 자신의 생각/동의/반박/수정 사항을 반영했다.
- [x] 이해 노트를 바탕으로 Part 0~12가 모두 영상 관점으로 매핑되었다.
- [x] 핵심 thesis가 1개 이상 도출되었다.
- [x] Builders Lounge / Bila AI Agent 연결 지점이 출처 기반으로 정리되었다.
- [x] README.md가 학습 순서(읽기 노트 → Source Map)를 안내한다.
- [x] WorkLog에 M1 진행 내용이 기록되었다.

**현재 완료율**: 8/9 (사용자 직접 읽기·정리 확인 전)

## Daily Retrospective

### What went well

- 기존 산출물과 정식 VibeLearn AI 절차의 차이를 명확히 구분했다.
- 방송 중에도 바로 스크립트로 뛰지 않고, Roadmap 기준으로 현재 위치를 재확인했다.
- 3부의 `모델 / 오케스트레이션 / 인터페이스` 구조를 Builders Lounge와 Bila AI Agent 설명으로 연결할 수 있음을 확인했다.
- Part 0~12 전체를 읽기 노트로 정리하면서 첫 영상의 핵심이 더 선명해졌다.
- Source Map을 기존 참고용 문서에서 정식 M1 산출물로 업데이트했다.

### What could be improved

- 원본 자료가 Topic 폴더 안에 있지 않아 처음 위치 확인에 시간이 걸렸다.
- 다음부터는 Topic 폴더의 `vl_materials/` 또는 README에 원본 자료 위치를 더 명확히 연결하는 편이 좋다.
- 무엇보다 일일 학습 시작 시 오늘의 학습 계획을 먼저 제시하고 사용자 승인을 받는 게이트를 반드시 지켜야 한다.

### Insights

- Build with AI의 "AI 레고 스택"은 단순 도구 소개가 아니라, AI 서비스 설계의 최소 구조를 설명하는 좋은 프레임이다.
- 첫 영상의 핵심 슬라이드 후보로 `Model / Orchestration / Interface` 3단 도식을 사용할 수 있다.
- Bila AI Agent는 단일 모델이 아니라 세 레이어가 결합된 시스템으로 설명하는 편이 정확하다.
- 첫 영상의 최종 thesis는 "데모는 AI가 만들 수 있지만, 서비스는 문제·데이터·검증·운영 기준이 있어야 한다"가 가장 적합하다.
- Builders Lounge는 데모와 프로덕션 사이의 파일럿/검증장으로 설명할 수 있다.
- Bila AI Agent는 Part 4의 데이터 준비와 Part 7의 Agent 구조를 결합한 실험으로 해석할 수 있다.

### Tomorrow's focus

- M2 `Audience and Product Discovery Angle`로 바로 실행하지 않는다.
- 다음 세션은 먼저 사용자가 `01-Source-Map/reading-notes.md`를 직접 읽고 자신의 생각으로 정리했는지 확인한다.
- 아직 정리하지 않았다면 M1 마무리 학습 계획을 제시하고 승인받은 뒤, Reading notes에 대한 사용자 생각/수정/반박을 반영한다.
- 이 확인이 끝난 뒤에만 M1을 최종 완료 처리하고, 그 다음 M2용 오늘의 학습 계획을 제시한다.

## 참조 및 산출물

**업데이트된 파일**:
- `01-Source-Map/reading-notes.md`: Part 0~12 이해 노트 완성
- `01-Source-Map/build-with-ai-source-map.md`: M1 실습2 Source Map/Thesis 업데이트
- `01-Source-Map/README.md`: 학습 순서와 M1 상태 업데이트
- `01-Source-Map/source-materials.md`: M1 원본 자료 안내 산출물
- `vl_roadmap/20260705_RoadMap_Build-with-AI.md`: 원본 자료 확인을 M1 실습0으로 편입하고 M2/M3 상태 정정
- `topic_info.md`: Source Materials Index 산출물 위치를 M1으로 수정

**생성된 파일**:
- `vl_worklog/20260712_M1_Build-with-AI.md`
- `01-Source-Map/source-materials.md`
- `vl_materials/` 내부 PDF/EPUB/치트시트 원본 복사본

**참조 자료**:
- `vl_prompts/daily_learning_prompt.md`
- `vl_roadmap/20260705_RoadMap_Build-with-AI.md`
- `vl_worklog/20260705_M1_Build-with-AI.md`
- `AI/Initiatives/Builders Lounge/builders/Song-Jae-hee-Build-with-AI/materials/build-with-ai-complete-ko.epub`

**작성자**: Codex
**방법론**: VibeLearn AI
