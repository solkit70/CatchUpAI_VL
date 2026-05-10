---
title: "M2 - Two-Component Architecture Design"
created: 2026-05-10 06:32:59
tags:
  - vibe-guiding
  - architecture
  - m2
  - vibelearn-ai
sources:
  - "[[Ingest/CatchUpAI_VL/Topics/Vibe-Guiding-VSCode/vl_roadmap/20260426_RoadMap_Vibe-Guiding-VSCode#M2 - Two-Component Architecture 설계|M2 Roadmap]]"
  - "[[Ingest/CatchUpAI_VL/Topics/Vibe-Guiding-VSCode/01-Vision-and-Architecture/poc-target-selection#선택 결론|POC Target Selection]]"
---

## 모듈 정보

**모듈**: M2 - Two-Component Architecture 설계  
**상태**: 진행 중  
**예상 학습 시간**: 6h  
**목표**: GOBI CLI v2.0.12를 기준으로 Vibe Manual/CVL 컴포넌트와 Guiding Engine 컴포넌트의 책임을 분리하고, 파일 기반 POC의 경계를 정한다.

## 학습 순서

1. [component-responsibilities.md](component-responsibilities.md)  
   Vibe Manual/CVL과 Guiding Engine의 입력, 출력, 저장 위치, 금지 책임, 실패 모드를 구분한다.

2. [architecture-diagrams.md](architecture-diagrams.md)  
   최신 매뉴얼 생성/갱신 흐름과 사용자 상태 기반 안내 생성 흐름을 Mermaid로 시각화한다.

3. [poc-boundary.md](poc-boundary.md)  
   M4에서 구현할 파일 기반 Python POC의 포함 범위와 제외 범위를 고정한다.

## 현재 DoD 진행

- [x] 컴포넌트 책임표 작성
- [x] Vibe Manual/CVL 다이어그램 작성
- [x] Guiding Engine 다이어그램 작성
- [x] POC 범위와 제외 범위 정의
- [x] `02-Architecture-Design/README.md` 작성
- [ ] WorkLog 작성 및 Daily Retrospective 완료

## 이전/다음 모듈

**이전 모듈**: M1 - Vibe Guiding 개념과 Source Map  
관련 문서: [../01-Vision-and-Architecture/README.md](../01-Vision-and-Architecture/README.md)

**다음 모듈**: M3 - Vibe Manual과 CVL 설계  
다음 모듈에서는 이 아키텍처를 바탕으로 `manual_index`, `retrieval_index`, `trigger_rules`의 스키마를 구체화한다.
