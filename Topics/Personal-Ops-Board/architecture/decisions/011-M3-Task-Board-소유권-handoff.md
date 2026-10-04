---
title: "ADR 011 — M3 Task Board 소유권 handoff"
created: 2026-10-02 20:00:00 -07:00
tags:
  - personal-ops-board
  - architecture-decision
---

## 결정

2026-10-02 사용자 승인에 따라 POST-HANDOFF로 전환한다. task 원본은 `AI/Tasks/items/`, 생성 Board는 `AI/Tasks/views/priority-board.md`로 한다. 과거 수동 `AI/Tasks/Task Board.md`는 세 섹션과 이력을 잇는 읽기 전용 진입점으로 보존한다.

## 근거와 선행 확인

기존 Task Board의 처리 중 71행·완료 32행·Backlog 65행을 확인했다. 완료 이력 archive 및 전체 Board snapshot 링크가 열리고, 스냅샷이 전환 직전 원본과 바이트 단위로 일치했다. 인덱서 70개 유효·오류 0·수용된 정보성 warning 11건, POB 회귀 33건 통과를 확인했다. 10/2 실제 GDR은 cutover 전에 PRE-HANDOFF로 실행했고 당일 task 상태 변경이 없어 item 쓰기가 없는 정상 no-op이었다. Weekly Progress, Dashboard JSON, Live30 Rundown 파싱도 확인했다.

## 경계

이 결정은 모든 task의 마이그레이션 완료를 뜻하지 않는다. 보류 48건과 검토 대기 41개 제안은 승인된 task로 간주하지 않고 원본 snapshot·판정표·inbox 상태에 남긴다. 2026-10-02 Daily Roundup에서 실제 task 변경 4건으로 POST 경로 `items → index → priority-board`를 확인했다. 2026-10-03 다음 날 GDR에서 네 task 변경이 지속되고 index 71/71·오류 0, Board 재생성이 성공해 M4 운영 안정성 DoD를 충족했다.

## 복구

index/render 오류나 task 누락이 발생하면 migration ledger를 PRE-HANDOFF로 되돌리고 snapshot을 기준으로 수동 Task Board를 복구한다. 원인을 수정하고 회귀 검증을 통과할 때까지 이중 동기화를 재개한다. 적용 상태와 해시는 [전환 원장](../../../../../../AI/Tasks/migration-review.md)에 기록한다.

## 상태

2026-10-02 사용자 승인 후 적용. POB 회귀 33건 통과. 10/2 실제 변경 4건 기반 POST 경로와 10/3 다음 날 지속성 검증 완료. M3 전체 미이관 task 범위는 별도로 진행 중.
