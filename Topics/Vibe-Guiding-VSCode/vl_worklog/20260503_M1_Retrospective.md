---
title: "M1 Retrospective - Vibe Guiding 개념과 Source Map"
created: 2026-05-03 07:40:11
tags:
  - vibe-guiding
  - retrospective
  - m1
  - vibelearn-ai
sources:
  - "[[Ingest/CatchUpAI_VL/Topics/Vibe-Guiding-VSCode/01-Vision-and-Architecture/source-map#Source Map 목적|source-map]]"
  - "[[Ingest/CatchUpAI_VL/Topics/Vibe-Guiding-VSCode/01-Vision-and-Architecture/what-is-vibe-guiding#30초 설명|what-is-vibe-guiding]]"
  - "[[Ingest/CatchUpAI_VL/Topics/Vibe-Guiding-VSCode/01-Vision-and-Architecture/poc-target-selection#선택 결론|poc-target-selection]]"
---

## 모듈 완료 요약

M1에서는 Vibe Guiding의 철학과 GOBI 적용 근거를 정리하고, 이후 M2-M4에서 사용할 설계 기준을 만들었다. 핵심 결론은 Vibe Guiding이 문서 검색 챗봇이 아니라, Vibe Learning으로 만들어진 최신 매뉴얼을 사용자 상태와 problem signal에 맞게 활성화하는 안내 시스템이라는 점이다.

## 계획 대비 실제

| 항목 | 계획 | 실제 |
|---|---|---|
| Source Map | 핵심 Source 5개 정리 | 완료 |
| Vibe Guiding 설명문 | 30초 설명, 3분 설명, 비교표 | 완료 |
| POC 대상 평가 | GOBI CLI vs Desktop/Applet 비교 | 완료 |
| M1 README | 학습 순서와 DoD 정리 | 완료 |
| WorkLog | Daily Retrospective 포함 | 완료 |

## 핵심 학습 내용

Vibe Guiding의 구현 중심은 좋은 답변을 만드는 것보다 먼저 사용자 상태를 정확히 수집하고, 안내가 필요한 순간을 판단하고, 최신 매뉴얼에서 근거를 찾는 데 있다. GOBI CLI는 이 구조를 파일 기반 POC로 검증하기에 적합하며, Gobi Desktop/Applet은 이후 시나리오 테스트와 제품 통합 논의에서 더 큰 가치를 가진다.

## 발생한 문제와 해결

초기에는 M1 산출물 폴더가 없었기 때문에 지난 세션이 M1 학습이 아니라 M0 구조 보정이었다는 점을 먼저 확인해야 했다. 이를 해결하기 위해 `01-Vision-and-Architecture/`를 생성하고 Source Map, 설명문, POC 대상 평가 문서를 순서대로 작성했다.

## Roadmap 정확도 평가

M1 Roadmap은 적절했다. Source Map을 먼저 만들고 설명문과 POC 대상 평가로 이어지는 흐름이 M2의 Architecture Design으로 자연스럽게 연결된다. 다만 실제 작업에서는 POC 대상 후보 평가가 별도 세션 결정에 의존했으므로, 다음 Topic에서는 후보 선택 기준을 Roadmap 작성 시 더 명시해도 좋다.

## 다음 모듈 준비사항

M2는 GOBI CLI를 기준으로 Two-Component Architecture를 설계한다. 다만 현재 `GOBI-CLI` Topic은 old 버전이므로, 다음 세션에서는 먼저 Continuous Vibe Learning 프로세스로 GOBI-CLI Topic을 New 버전에 맞게 업데이트한다. 그 업데이트가 끝난 뒤 `poc-target-selection.md`, `source-map.md`, `what-is-vibe-guiding.md` 등 M1 문서에서 GOBI CLI 관련 전제와 참조 자료를 보정하고, 그 다음 `02-Architecture-Design/` 폴더를 만들어 `component-responsibilities.md`, `architecture-diagrams.md`, `poc-boundary.md`를 작성한다.

모든 관련 문서 작성과 보정이 완료되면 GitHub에 push한다. 현재는 GOBI-CLI CVL 업데이트와 M1/M2 문서 작업이 남아 있으므로 push는 최종 마감 단계로 보류한다.

## M1 DoD 최종 상태

- [x] 핵심 Source 5개를 읽고 Source Map 작성
- [x] Vibe Guiding 30초 설명 작성
- [x] Vibe Learning vs Vibe Guiding 비교표 작성
- [x] 첫 POC 대상 후보 평가 완료
- [x] `01-Vision-and-Architecture/README.md` 작성
- [x] WorkLog 작성 및 Daily Retrospective 완료

**완료율**: 6/6 (100%)
