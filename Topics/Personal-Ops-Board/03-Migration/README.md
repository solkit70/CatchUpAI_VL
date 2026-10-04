---
title: "M3 — Migration"
created: 2026-10-02 20:00:00 -07:00
tags:
  - personal-ops-board
  - vibelearn-ai
---

## M3 — Migration

**상태**: 소유권 handoff 적용, 전체 이관은 진행 중. 기존 Task Board의 행을 `items/`와 대조하고, 사람이 승인한 변경만 반영하는 모듈이다. Board 소유권은 2026-10-02에 POST-HANDOFF로 바뀌었지만 보류 48건과 검토 대기 제안 41건이 남아 M3 전체 DoD는 완료되지 않았다.

## 학습 순서

1. [승인 게이트 개념](concepts/approval-gate.md)에서 후보·판정·승인·원본의 권한 경계를 익힌다.
2. [합성 대조 사례](examples/README.md)에서 연결·중복·보류·제외 판정을 확인한다.
3. [마이그레이션 체크리스트](guides/migration-checklist.md)를 따라 백업, 대조, 보존, handoff, 복구를 점검한다.
4. [M3 작업 기록](../vl_worklog/20261002_M3_Personal-Ops-Board.md#M3-현재-준비-상태와-다음-작업)에서 실제 적용 결과와 남은 항목을 확인한다.
5. [전환 원장](../../../../../AI/Tasks/migration-review.md)과 [생성 Board](../../../../../AI/Tasks/views/priority-board.md)를 비교해 현재 운영 상태를 확인한다.

## 현재 운영 결과

기존 Task Board 세 섹션과 처리·보류 기록의 보존 경로를 확인했다. 전체 원본은 날짜가 붙은 snapshot에, 처리 완료 이력은 archive에, 행별 판정과 미승인 제안은 migration ledger 및 inbox에 남아 있다. `Task Board.md`는 생성 Board와 원본 기록으로 연결하는 읽기 전용 진입점이다. 실제 Roundup은 cutover 전에 PRE-HANDOFF로 실행했고, 당일 task 변경이 없어 task 쓰기는 발생하지 않았다. 다음 실제 task 변경에서 POST-HANDOFF `items → index → board` 경로를 운영 검증한다.

## 완료 기준 상태

- [x] 136개 행의 판정과 보존 경로 확인
- [x] 원본 snapshot 및 복구 절차 점검
- [x] 승인된 handoff를 적용하고 상태를 ledger에 기록
- [ ] 보류·미승인 항목을 사용자 결정에 따라 처리 (10/6 검토 포함)
- [ ] 실제 변경을 포함한 POST-HANDOFF 운영 실행 확인

다음 모듈: [M4 — Workflow Integration](../04-Workflow-Integration/README.md). M4 workflow 변경은 M3 전체 task 이관이 끝났다는 뜻이 아니며, 남은 후보를 별도 승인 없이 원본 task로 만들지 않는다.
