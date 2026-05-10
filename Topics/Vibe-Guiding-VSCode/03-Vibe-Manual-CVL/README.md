---
title: "M3 - Vibe Manual and CVL Design"
created: 2026-05-10 06:52:12
tags:
  - vibe-guiding
  - vibe-manual
  - cvl
  - m3
  - vibelearn-ai
sources:
  - "[[Ingest/CatchUpAI_VL/Topics/Vibe-Guiding-VSCode/vl_roadmap/20260426_RoadMap_Vibe-Guiding-VSCode#M3 - Vibe Manual과 CVL 설계|M3 Roadmap]]"
  - "[[Ingest/CatchUpAI_VL/Topics/Vibe-Guiding-VSCode/02-Architecture-Design/component-responsibilities#M4 구현으로 넘길 결정|Component Responsibilities]]"
---

## 모듈 정보

**모듈**: M3 - Vibe Manual과 CVL 설계  
**상태**: 완료  
**예상 학습 시간**: 7h  
**목표**: GOBI CLI v2.0.12 문서를 Guiding Engine이 검색하고 조합할 수 있는 Vibe Manual 구조로 바꾸고, CVL 업데이트 기준을 정의한다.

## 학습 순서

1. [vibe-manual-schema.md](vibe-manual-schema.md)  
   사람이 읽는 Markdown과 AI가 읽는 metadata를 함께 갖는 Atomic Guide Unit 스키마를 정의한다.

2. [retrieval-metadata-design.md](retrieval-metadata-design.md)  
   M4 POC에서 사용할 `manual_index.json`과 retrieval metadata 필드를 설계한다.

3. [sample-manual/gobi-cli-getting-started.md](sample-manual/gobi-cli-getting-started.md)  
   GOBI CLI Space Post 생성 흐름을 Vibe Manual 스키마에 맞춰 샘플 매뉴얼로 작성한다.

4. [cvl-update-rules.md](cvl-update-rules.md)  
   CLI 명령어, UI label, config path, error message 변경이 매뉴얼 업데이트를 요구하는 기준을 정리한다.

## 현재 DoD 진행

- [x] Vibe Manual Schema 작성
- [x] Retrieval Metadata 설계 작성
- [x] Sample Manual 최소 1개 작성
- [x] CVL Update Rules 작성
- [x] `03-Vibe-Manual-CVL/README.md` 작성
- [x] WorkLog 작성 및 Daily Retrospective 완료

## 이전/다음 모듈

**이전 모듈**: M2 - Two-Component Architecture 설계  
관련 문서: [../02-Architecture-Design/README.md](../02-Architecture-Design/README.md)

**다음 모듈**: M4 - Guiding Engine POC 개발  
다음 모듈에서는 이 폴더의 schema와 sample manual을 바탕으로 `manual_index.json`, `trigger_rules.json`, `user_context.json`, `guide_response.md` 파일 흐름을 실제로 구현한다.
