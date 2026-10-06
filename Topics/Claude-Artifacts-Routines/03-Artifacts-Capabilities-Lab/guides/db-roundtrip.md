---
title: "M3 실습 2 — 세션에서 db 읽고 쓰기 · if_version 거부 실측"
created: 2026-09-27 15:30:00
author:
  - "Claude Code"
tags:
  - claude-artifacts-routines
  - m3
  - db
---

## 요약

**옛 version 에 고정한 쓰기는 실제로 거부됐고, 아무것도 쓰이지 않았다.** 세션(Claude Code 의 `ArtifactData` 도구)이 db 카운터 아티팩트의 문서 `counter/main` 을 읽고, 버전을 붙여 쓰고, 일부러 옛 버전으로 써서 거부되는 것까지 네 번의 호출로 확인했다.

## 실측 로그 — 2026-09-27, 카운터 https://claude.ai/artifact/8p4xaEhHXB6PQyzDZfy3os

| # | 호출 | 보낸 것 | 결과 | version |
|---|---|---|---|---|
| 1 | `get counter/main` | — | `No document "main" in collection "counter"` — 없는 문서는 오류가 아니라 「없음」 | — |
| 2 | `set` (if_version 없음) | `value: 10` | committed · 「1 of 5000 documents used」 | **1** |
| 3 | `update` + `if_version: 1` | `value: 11` | committed | **2** |
| 4 | `update` + `if_version: 1` (**옛 버전**) | `value: 999` | ❌ `version_mismatch` — *"the document is no longer at version 1 … it is now at version 2; nothing was written"* | 2 그대로 |
| 5 | `list counter` | — | `value: 11` · version 2 — 999 는 쓰이지 않았다 | 2 |
| 6 | `list counter` + `as_level: interact` | — | 같은 문서가 보인다 — 기본 규칙에서 Contributor(interact) 는 공유 문서를 읽는다 | 2 |
| 7 | (사용자) 화면에서 **+1 두 번** | — | 페이지가 쓴 값 | 3 → 4 |
| 8 | `get counter/main` | — | `value: 13` · `by: "page"` · version **4** — **화면이 쓴 것을 세션이 읽었다** | 4 |
| 9 | `update` + `if_version: 2` (세션이 마지막으로 본 버전 — **그 사이 화면이 두 번 씀**) | `value: 12` | ❌ `version_mismatch` — *"it is now at version 4; nothing was written"* — 사람과 AI 가 같은 문서를 고친 **실제 충돌 상황**에서 세션 쪽 쓰기가 막혔다 | 4 그대로 |
| 10 | `update` + `if_version: 4` (다시 읽은 버전) | `value: 14` | committed | **5** |

## 배운 것

- **버전은 문서마다 1 부터 올라간다.** `set` 이 문서를 만들면 version 1, 쓸 때마다 +1
- **`if_version` 은 「그 사이 누가 고쳤나」를 서버가 대신 확인하는 장치다.** 쓰기 전에 다시 읽을 필요가 없다 — 고정해서 쓰고, 거부되면 그때 다시 읽고 다시 계획한다
- **페이지 쪽에는 `if_version` 이 없다.** 페이지의 `set`/`update` 는 마지막에 쓴 사람이 이긴다(last-writer-wins). 카운터처럼 「읽고 +1 해서 쓰기」는 두 사람이 동시에 누르면 한 번이 사라질 수 있다 → 여러 사람이 올리는 숫자는 문서 하나에 +1 하지 말고, 사람마다 문서를 따로 두고 합계를 보여 주거나 `acquire` 로 한 명씩 쓰게 한다 (`db.d.ts` 의 update 설명: *"Do NOT build monotonic counters from read-modify-update"*)
- 에러 메시지가 다음 행동을 알려 준다 — *"Read it back, re-plan the write against what it holds now, and pin to that version"*

## 왕복 완료

- [x] 세션이 쓴 11 을 화면이 봤다 → 사용자가 그 위에서 +1 두 번 (22:28)
- [x] 화면이 쓴 13 · version 4 · `by: "page"` 를 세션이 읽었다
- [x] 옛 버전(v2)으로 쓴 세션 쓰기가 실제 충돌에서 거부됐고, 다시 읽은 v4 로 고정한 쓰기는 통과했다 (→ v5, 값 14)

> **이 실습이 보여 준 것**: 사람이 화면에서 고치는 동안 AI 세션이 같은 데이터를 고치려 하면, `if_version` 이 사람의 변경을 덮어쓰지 않게 막는다. AI 에게 아티팩트 데이터를 맡길 때 가장 먼저 확인할 안전장치다.


English companion: [db-roundtrip_en](db-roundtrip_en.md)
