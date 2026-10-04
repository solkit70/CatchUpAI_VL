---
title: "M3 — 마이그레이션·복구 체크리스트"
created: 2026-10-02 20:00:00 -07:00
tags:
  - personal-ops-board
  - migration
---

## 마이그레이션·복구 체크리스트

### 전환 전

- [ ] 원본 Task Board와 모든 `items/` 변경을 멈추거나 변경 시점을 기록한다.
- [ ] Task Board 전체 스냅샷과 완료 이력 보관본을 만들고 해시를 기록한다.
- [ ] 행별 후보와 확정 판정을 구분한다. 후보 경로는 자동 확정하지 않는다.
- [ ] 미결·보류·미승인 제안의 수와 원본 위치를 기록한다. 그것들을 승인된 task처럼 렌더하지 않는다.
- [ ] 인덱서, renderer, 합성 shadow 회귀를 실행하고 오류 및 허용된 정보성 경고를 확인한다.
- [ ] Roundup 운영 실행 결과와 사용자 cutover 승인을 확인한다.

### 전환 후

- [ ] ledger에 현재 상태, 적용 시각, 원본 경로, snapshot 해시, rollback 방법을 기록한다.
- [ ] `Task Board.md`에서 생성 Board와 보관 원본으로 가는 링크가 열린다.
- [ ] 생성 Board를 다시 렌더하고 미결 기록의 보존 경로를 확인한다.
- [ ] POST-HANDOFF에서 task 변경이 없는 실행은 no-op으로 기록한다.
- [ ] 첫 실제 task 변경 실행에서 `items → index → priority-board` 결과와 링크를 확인한다.

### 실패 시 복구

POST-HANDOFF 실행 중 item 누락, 인덱서 오류 또는 renderer 실패가 확인되면 잘못된 생성물을 운영 완료로 취급하지 않는다. 먼저 ledger를 PRE-HANDOFF로 되돌리고 기록된 snapshot을 이용해 읽기 전용 진입점을 복구한다. 원인을 수정하고 회귀 검증을 통과한 뒤 이중 동기화를 재개하거나 재전환한다. 복구 뒤 snapshot 해시 및 세 섹션·완료 이력·보류 기록을 다시 확인한다.

현재 전환 기록과 해시는 [migration-review.md](../../../../../../AI/Tasks/migration-review.md)에 있다. 실제 POST-HANDOFF task 변경 사례는 2026-10-02에 확인했으며, 다음 날 결과 지속성은 후속 점검으로 남아 있다.
