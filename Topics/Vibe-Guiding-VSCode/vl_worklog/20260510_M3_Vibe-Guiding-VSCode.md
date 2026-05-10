---
title: "WorkLog - M3: Vibe Manual and CVL Design"
created: 2026-05-10 06:52:12
tags:
  - vibe-guiding
  - vibelearn-ai
  - worklog
  - m3
sources:
  - "[[Ingest/CatchUpAI_VL/Topics/Vibe-Guiding-VSCode/vl_roadmap/20260426_RoadMap_Vibe-Guiding-VSCode#M3 - Vibe Manual과 CVL 설계|M3 Roadmap]]"
  - "[[Ingest/CatchUpAI_VL/Topics/Vibe-Guiding-VSCode/02-Architecture-Design/poc-boundary#M4 최소 시나리오|M2 POC Boundary]]"
---

## 오늘의 학습 목표

- [x] `03-Vibe-Manual-CVL/` 폴더 생성
- [x] Vibe Manual Schema 작성
- [x] Retrieval Metadata 설계 작성
- [x] GOBI CLI v2.0.12 기준 Sample Manual 작성
- [x] CVL Update Rules 작성
- [x] M3 README 작성
- [x] Daily Retrospective 작성

## 진행 내용

### 1. M3 Roadmap 확인

M3의 핵심 목표는 일반 문서를 Guiding Engine의 입력으로 바꾸는 것이다. Roadmap에서 요구한 필수 필드는 `goal`, `prerequisites`, `steps`, `completion_signal`, `known_failures`, `related_sources`였고, 이를 Atomic Guide Unit 스키마로 정리했다.

### 2. Vibe Manual Schema 작성

`vibe-manual-schema.md`에서 사람이 읽는 Markdown 구조와 AI가 읽는 metadata 필드를 함께 정의했다. 특히 completion signal과 known failure를 필수 필드로 두어, guide response가 설명에서 멈추지 않고 사용자의 작업 완료까지 이어지도록 했다.

### 3. Retrieval Metadata 설계

`retrieval-metadata-design.md`에서 M4 POC에 사용할 `manual_index.json` 구조를 설계했다. 첫 구현은 vector DB 없이 rule-based matching으로 진행하며, `deprecated_terms`와 `replacement_terms`를 넣어 구 명령어를 새 명령어로 변환할 수 있게 했다.

### 4. Sample Manual 작성

`sample-manual/gobi-cli-getting-started.md`를 작성했다. 실제 내용은 GOBI CLI v2.0.12의 Space Post 생성 흐름이다. 사용자가 "Thread를 만들고 싶다"고 말해도 현재 명령어인 `gobi space create-post`로 안내하도록 설계했다.

### 5. CVL Update Rules 작성

`cvl-update-rules.md`에서 명령어, 파일 이름, 인증 방식, config path, error message 변경의 영향도를 분류했다. GOBI CLI v2.0.12 업데이트에서 확인된 `gobi init` -> `gobi vault init`, `BRAIN.md` -> `PUBLISH.md`, `Thread` -> `Post` 변경을 stale source 감지 규칙으로 정리했다.

## 문제 해결 로그

### 문제: 샘플 매뉴얼 범위 선택

**증상**: Roadmap은 GOBI CLI 인증 또는 GOBI Desktop Custom Homepage/Applet 중 하나를 샘플로 제안했지만, M4 POC는 Space/Post 작업 막힘 시나리오와 직접 연결되어 있었다.

**해결**: 샘플 파일명은 roadmap의 `gobi-cli-getting-started.md`에 맞추되, 실제 내용은 M4에서 가장 재사용성이 높은 GOBI CLI Space Post 생성 흐름으로 작성했다.

## DoD 체크리스트

- [x] Vibe Manual Schema 작성
- [x] Retrieval Metadata 설계 작성
- [x] Sample Manual 최소 1개 작성
- [x] CVL Update Rules 작성
- [x] `03-Vibe-Manual-CVL/README.md` 작성
- [x] WorkLog 작성 및 Daily Retrospective 완료

**완료율**: 6/6 (100%)

## Daily Retrospective

### What went well

M2에서 정의한 두 컴포넌트 경계가 M3 문서 구조를 바로 결정해줬다. Manual/CVL은 최신 지식 기반과 index를 만들고, Guiding Engine은 이를 소비한다는 경계가 명확했기 때문에 schema와 retrieval metadata를 과도하게 복잡하게 만들지 않을 수 있었다.

### What could be improved

이번 세션에서는 sample manual을 1개만 만들었다. M5에서 Desktop/Applet scenario를 다루려면 GOBI Desktop Custom Homepage/Applet용 sample manual도 별도로 추가하는 것이 좋다.

### Insights

Vibe Manual의 핵심은 잘 정리된 설명이 아니라 completion signal이다. 사용자가 무엇을 보면 성공인지 모르면, AI는 친절한 설명을 만들 수는 있어도 작업을 끝내게 하지는 못한다.

### Tomorrow's focus

- M4 시작: `04-Guiding-Engine-POC/` 생성
- `manual_index.json` 실제 파일 작성
- `trigger_rules.json` 작성
- `user_context.sample.json` 3개 작성
- rule-based `guide_response.md` 생성 흐름 설계
