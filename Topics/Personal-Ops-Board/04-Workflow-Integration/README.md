---
title: "M4 — Workflow Integration"
created: 2026-10-02 20:00:00 -07:00
tags:
  - personal-ops-board
  - vibelearn-ai
---

## M4 — Workflow Integration

**상태**: 완료 (2026-10-03). 조건부 GDR/GWR 동작, 실제 POST-HANDOFF 변경 4건, 다음 날 GDR 후 지속성·재생성을 검증했다. 다음 날에도 네 변경 task가 유지됐고 인덱스 71/71 유효·오류 0, renderer 정상이다. 이 모듈은 라운드업이 확정한 task 변경만 canonical `items/`에 반영하고, 그 결과로 view를 재생성하는 운영 경계를 다룬다.

## 학습 순서

1. [프롬프트 변경 절차](guides/prompt-change-procedure.md)에서 요청·승인·적용·검증 순서를 확인한다.
2. [문제 해결 가이드](troubleshooting/troubleshooting.md)에서 실패 시 중단·복구 기준을 따른다.
3. [M3 migration checklist](../03-Migration/guides/migration-checklist.md)에서 소유권 상태와 보존·rollback 조건을 확인한다.
4. [GDR 프롬프트](../../../../../_Settings_/Prompts/Generate%20Daily%20Roundup%20%28GDR%29.md), [GWR 프롬프트](../../../../../_Settings_/Prompts/Generate%20Weekly%20Roundup%20%28GWR%29.md), [전환 원장](../../../../../AI/Tasks/migration-review.md)을 함께 읽는다.

## 운영 계약

POST-HANDOFF에서 승인된 task 변화는 `items/`에 기록한다. 이후 index를 생성하고 문제가 없을 때 priority Board를 갱신한다. 프롬프트는 모호한 변경을 추측해 반영하지 않고 사용자 확인을 기다린다. 입력 오류, 미분류 경고 또는 렌더 오류가 있으면 새 view를 정상 결과로 간주하지 말고 이전 정상 결과와 원본을 보존한다.

10/2 첫 Roundup은 task 상태 변화가 없는 PRE-HANDOFF no-op이었다. 이후 별도 Roundup에서 사용자가 확인한 시연 준비를 네 item에 반영했다. 10/3 새 Daily Roundup의 POST-HANDOFF 검증에서 네 변경이 파일에 유지됨을 확인하고 index와 Board를 다시 만들었다. 71/71 유효·오류 0이며 허용 목록의 정보성 warning 11건 외 미분류 문제는 없었다.

## 완료 기준 상태

- [x] GDR/GWR의 PRE/POST 조건과 승인 경계 반영
- [x] 합성 shadow 회귀 및 POST-HANDOFF 전환 기록
- [x] 실제 task 변경 4건을 포함한 POST-HANDOFF Roundup에서 items→index→view 확인
- [x] 다음 날 GDR 결과 확인 후 운영 가이드와 architecture 상태 최종 갱신
- [x] M4 Module Retrospective · WorkLog 및 통합 Daily Retrospective 링크

이전 모듈: [M3 — Migration](../03-Migration/README.md). 다음 모듈은 [로드맵의 M5 — Deadline 에이전트](../vl_roadmap/20260927_RoadMap_Personal-Ops-Board.md#M5---Deadline-에이전트)다.
