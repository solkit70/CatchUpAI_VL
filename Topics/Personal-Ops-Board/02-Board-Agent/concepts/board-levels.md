---
title: "Board lane과 정렬 규칙"
created: 2026-10-02 11:32:31
tags:
  - personal-ops-board
  - board
---

## Board lane과 정렬 규칙

M2는 `items/` frontmatter의 tier를 그대로 사용해 네 lane으로 보여 준다. 스크립트는 tier나 상태를 자동 수정하지 않는다. `waiting`은 tier 2의 상태로 표시하고 `paused`는 tier 4에서 보존한다.

| 영역 | 포함되는 항목 | 정렬 |
|---|---|---|
| Tier 1 — 날짜가 정해진 일 | tier 1, 완료되지 않은 task | due 오름차순 → priority P0~P3 → NFKC 정규화 title → 상대 경로 |
| Tier 2 — 약속·대기 | tier 2, 완료되지 않은 task | priority P0~P3 → due 있는 항목 우선 → due 오름차순 → 정규화 title → 상대 경로 |
| Tier 3 — 프로젝트 | tier 3, 완료되지 않은 task | Tier 2와 같은 고정 규칙 |
| Tier 4 — 멈춤·보류 | tier 4, 완료되지 않은 task | Tier 2와 같은 고정 규칙 |
| 완료 | status `done`, 본문에 `## 닫음` 없음 | Tier 2와 같은 고정 규칙 |
| 닫음 | status `done`, 본문에 실제 `## 닫음` 절 있음 | Tier 2와 같은 고정 규칙 |

동률은 정규화한 상대 경로로 끝까지 풀어 입력 파일의 우연한 열거 순서가 결과를 바꾸지 않게 한다. 본문 fenced code block에 들어 있는 `## 닫음` 예시는 실제 절로 보지 않는다. 유효하지 않은 task와 인덱서 경고·오류는 활성 lane에서 숨기고 「점검 필요」에 파일과 원인 코드를 표시한다.

결정 근거와 예외 범위는 [ADR 010](../../architecture/decisions/010-M2-보드는-비공개-view만-생성.md#결정)에 있다. 생성 view와 메인 Task Board의 경계는 [M2 작업 기록](../../vl_worklog/20261002_M2_Personal-Ops-Board.md#승인된-설계와-구현-결과)에서 확인할 수 있다.
