---
title: "M3 — 아티팩트 런타임에서 걸리기 쉬운 것"
created: 2026-09-27 15:30:00
author:
  - "Claude Code"
tags:
  - claude-artifacts-routines
  - m3
  - troubleshooting
---

## 실측한 것 (2026-09-27)

| 증상 | 원인 | 대처 |
|---|---|---|
| 예제 여러 개를 발행한 뒤, 댓글 자동 답을 걸어 둔 아티팩트가 조용해졌다 | 한 세션의 아티팩트 감시는 **10개까지**. 새로 발행한 아티팩트가 감시 목록에 올라가면서 오래된 감시(부스 매니저 · 부스 현황판)가 밀려났다. 밀려난 쪽의 댓글 자동 답도 멈춘다 | 실습용 발행은 운영 중인 아티팩트를 감시하는 세션과 **다른 세션**에서 한다. 이미 밀려났으면 필요할 때 `ArtifactComments` 의 `watch` 로 다시 건다 |
| 세션의 db 쓰기가 `version_mismatch` 로 거부됐다 | 읽은 뒤 누군가(페이지나 다른 세션) 문서를 고쳤다 | 정상 동작이다. 다시 읽고 새 version 으로 고정해 다시 쓴다 → [db-roundtrip](../guides/db-roundtrip.md) |
| 셸(Git Bash)에서 heredoc 으로 한국어 HTML 여러 개를 한 번에 쓰다가 `unexpected EOF while looking for matching '` | 긴 한국어 heredoc 묶음에서 따옴표 해석이 꼬였다 (같은 날 두 번) | 파일은 파일 쓰기 도구로 하나씩 쓴다 |

## 문서로 확인한 것 (runtime contract 0.2.60)

| 걸리기 쉬운 것 | 규칙 |
|---|---|
| 외부 스크립트·폰트 | 스크립트는 cdnjs · jsdelivr · unpkg 등 허용 목록에서만, 스타일시트는 Google Fonts 만. 그 밖은 **오류 없이** 막힌다 |
| localStorage | 보는 사람 브라우저에만 남는다. 다른 사람·다른 기기·Claude 에 닿지 않고, 시크릿 창에서는 비거나 예외가 난다 → 편의용(탭 기억)으로만 |
| db · assets · user 를 선언한 아티팩트 | 조직 안에서만 공유된다 (공개 링크 불가). `comments` 를 `composer_only` 로만 켜면 공개 링크 가능 |
| `window.claude.db` 처럼 바로 읽기 | 없다. 항상 `await claude.use("db")` 로 받고, `null` 이면 기능을 숨긴다 |
| 페이지의 카운터 +1 | 마지막에 쓴 사람이 이긴다 — 동시에 누르면 한 번이 사라질 수 있다 |
| `alert()` · `confirm()` · `prompt()` | 화면에 안 뜬다 (`confirm` 은 false, `prompt` 는 null). 확인 단계는 페이지 안에 만든다 |
