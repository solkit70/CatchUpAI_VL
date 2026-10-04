---
title: "M2 — Board 에이전트"
created: 2026-10-02 11:32:31
tags:
  - personal-ops-board
  - vibelearn-ai
---

## M2 — Board 에이전트

**상태**: 구현·합성 검증·실제 입력 렌더링 완료. M2는 M1 인덱스를 결정적 규칙으로 비공개 우선순위 view로 만든다. 실제 task와 생성 view는 비공개 볼트 `AI/Tasks/`에만 있다.

## 테스트 순서

1. [lane과 정렬 규칙](concepts/board-levels.md)에서 네 tier와 완료/닫음 구분을 확인한다.
2. [합성 사례와 기대 결과](examples/README.md)로 분류, 정렬, 점검 영역을 확인한다.
3. [수동 실행 안내](guides/run-board.md)에 따라 인덱서 다음 Board renderer를 실행한다.
4. [AI4PKM 노드 등록 안내](guides/register-node.md)에서 자동 실행 설정과 현재 검증 한계를 확인한다.
5. [ADR 010](../architecture/decisions/010-M2-보드는-비공개-view만-생성.md#결정)과 [M2 WorkLog](../vl_worklog/20261002_M2_Personal-Ops-Board.md#검증)에서 소유권 경계 및 결과를 읽는다.

## 생성물과 권한

생성되는 파일은 `AI/Tasks/views/priority-board.md`다. Board는 `items/`와 루트 `AI/Tasks/Task Board.md`를 읽기만 한다. 기존 Task Board를 보드 view로 전환하는 일은 M3에서 별도로 다룬다. 공개 예제는 합성 데이터만 사용한다.
