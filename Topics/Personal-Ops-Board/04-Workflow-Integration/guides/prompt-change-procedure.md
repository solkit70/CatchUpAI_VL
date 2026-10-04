---
title: "M4 — GDR/GWR 프롬프트 변경 절차"
created: 2026-10-02 20:00:00 -07:00
tags:
  - personal-ops-board
  - workflow-integration
---

## GDR/GWR 프롬프트 변경 절차

### 1. 변경 범위 확정

GDR의 task 동기화 단계와 GWR의 주간 계획 반영 단계 중 어떤 동작을 바꿀지 먼저 적는다. 생성할 파일, 수정할 item 필드, index/render 조건, 사용자 확인이 필요한 모호성, 실패 시 복구를 명시한다. 변경 대상 문서와 기존 문구를 사용자에게 보여 주고 승인을 받는다.

### 2. 안전한 시험

합성 `items/` fixture를 사용해 새 status가 index와 Board에 반영되는지 검사한다. 시험 전후 실제 Task Board 및 실제 item 원본의 해시가 불변인지 확인한다. 오류·누락·허용 범위 밖 경고를 성공으로 해석하지 않는다.

### 3. 운영 기록 반영

승인된 프롬프트 변경을 저장한 뒤 전환 원장과 WorkLog에 상태·날짜·검사 결과·미확인 항목을 적는다. PRE-HANDOFF 동안은 Task Board와 `items/` 양쪽에 변경을 반영한다. POST-HANDOFF에서는 확인된 변경만 `items/`에 기록하고 Board는 index를 거쳐 재생성한다.

### 4. 운영 실행 확인

다음 실제 GDR/GWR에서 변경 대상 task와 resulting item을 대조한다. 이어 인덱서와 renderer 출력, item/Board 링크, 보류·완료 상태 보존을 확인한다. 해당 실행에 task 변경이 없으면 no-op이라고 기록하며 변경 경로 통과로 계산하지 않는다.

### 5. rollback

실패 시 새 view를 정상 운영 결과로 취급하지 않는다. [M3 복구 체크리스트](../../03-Migration/guides/migration-checklist.md#실패-시-복구)를 따라 ledger·원본 Board를 복구하고, 필요한 경우 PRE-HANDOFF 이중 동기화로 돌아간다.
