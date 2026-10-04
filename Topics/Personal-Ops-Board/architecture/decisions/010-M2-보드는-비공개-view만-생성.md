---
title: "ADR 010 — M2 보드는 비공개 view만 생성"
created: 2026-10-02 11:32:31
tags:
  - personal-ops-board
  - architecture-decision
---

## 결정

M2 Board는 M1 `index.json`을 입력으로 받아 `AI/Tasks/views/priority-board.md`만 생성한다. 루트 `AI/Tasks/Task Board.md`는 M2에서 갱신하지 않는다. M3에서 기존 표와 `items/`를 대조하고 사용자 승인 후 소유권 전환을 검토한다.

보드의 분류와 정렬은 결정적 Python 코드가 수행한다. Tier 1은 due 오름차순 → priority P0부터 → NFKC 정규화 title → 상대 경로 순이다. Tier 2~4와 완료/닫음은 priority → due가 있는 항목 우선 → due 오름차순 → 정규화 title → 상대 경로 순이다. 동률도 입력 순서나 모델 판단에 좌우되지 않는다.

`waiting`은 tier 2, `paused`는 tier 4에서 상태를 보존한다. `done`은 활성 lane 밖에서 본문에 실제 `## 닫음` 절이 있으면 「닫음」, 아니면 「완료」에 둔다. 코드 블록 안의 예시 제목은 닫음 절로 보지 않는다. 유효하지 않은 항목과 인덱서 문제는 「점검 필요」에 남긴다.

POB-Board prompt와 AI4PKM 노드는 변경된 item에서 인덱서와 renderer를 실행하는 진입점으로 둔다. prompt는 task를 고치거나 보드 내용을 재작성하지 않으며, 실패하면 이전 정상 view를 보존한다.

## 이유

현재 Task Board 표와 items가 전환기에 함께 존재한다. M2가 일부 파일만으로 기존 표를 덮으면 아직 옮기지 않은 행이 사라질 수 있다. 보드 내용을 일반 LLM에 정렬시키는 것은 같은 입력의 재현성과 검증성을 낮춘다. 각각 M3 범위와 결정적 코드로 경계를 둔다.

## 결과

- M2 결과는 볼트 내부 생성물이며 공개 topic에는 합성 예제만 둔다.
- 런타임과 Python 구현에 의존하므로 AI4PKM 자동 실행은 설치된 CLI에서 별도 확인한다.
- Task Board 소유권 변경은 M3의 대조·승인 전에는 하지 않는다.

## 상태

2026-10-02 사용자 승인 후 구현 완료. AI4PKM CLI 0.1.25를 사용자 Python 환경에 설치했고 registry가 두 POB node를 로드하는 것을 확인했다. 별도 승인으로 수정 trigger를 한 번 실행해 generated view와 completed log를 확인했다. 요청이 단회 실행이므로 두 자동 file trigger는 비활성 상태로 유지한다.
