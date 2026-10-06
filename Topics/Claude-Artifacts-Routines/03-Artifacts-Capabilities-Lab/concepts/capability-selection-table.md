---
title: "어떤 일에 어떤 Artifact 기능을 쓰나 — 선택표"
created: 2026-09-27 15:55:00
author:
  - "Claude Code"
tags:
  - claude-artifacts-routines
  - m3
  - concepts
---

## 한 줄 기준

**「누가 볼 수 있어야 하나」로 고른다.** 나만 기억하면 되는 것은 브라우저, 페이지 자체가 기록이면 `artifact`, 여러 사람과 Claude 가 함께 읽고 쓰면 `db` 다. runtime contract 0.2.60 기준, 2026-09-27 실습으로 확인한 것은 ✅ 로 표시했다.

## 선택표

| 하고 싶은 일 | 쓸 기능 | 누가 보나 | 실습 |
|---|---|---|---|
| 마지막으로 연 탭, 접은 섹션 기억 | 브라우저 저장 (localStorage) | 그 사람의 그 브라우저만. 다른 사람·Claude 는 못 봄 | — |
| 투표·체크리스트처럼 **페이지가 곧 기록** | `artifact` (페이지가 새 버전을 스스로 발행) | 페이지를 여는 모든 사람 | — |
| 여러 사람이 같은 데이터를 실시간으로 보고 고침 · Claude 가 나중에 읽거나 채움 | `db` | 조직 안에서 접근 권한이 있는 사람 · Claude 세션 | ✅ ① 카운터 · 실습 2 왕복 |
| 사람마다 비공개로 저장 (내 메모, 비공개 투표) | `db` 의 `data/users/<id>/` + `user` | 그 사람만 (작성자도 못 봄) | — |
| 누가 보고 있는지, 편집 권한이 있는지 | `user` | — | ✅ ② |
| 이미지·PDF·배치도 | `assets` | 아티팩트를 볼 수 있는 사람 (조직 안) | ✅ ③ 세션 업로드 → 페이지 표시 |
| 문단·항목마다 의견 받기, Claude 에게 보내기 | `comments` (`composer_only` 가 가장 가벼움) | 댓글 목록은 claude.ai 화면이 보여 줌 | ✅ ④ 문단 3개 · Send to Claude 자동 답 |
| CSS·JS·데이터를 나눠 관리 | `files` 매개변수로 함께 발행 (capability 아님) | 페이지와 같음 | ✅ ⑤ |
| 지금 같이 보고 있는 사람에게 커서·신호 | `room` (저장 안 됨) | 지금 열어 둔 사람만 | — |
| 페이지에서 Claude 에게 묻기 | `sample` (보는 사람 비용) | — | — |

## 공유 범위에 주의

| 선언 | 공개 링크 |
|---|---|
| `db` · `assets` · `user` | ❌ 조직 안에서만 |
| `comments` 를 `composer_only` 로만 | ✅ 가능 |
| capability 없음 (⑤) | ✅ 가능 |

## 10초 고르기 연습 — 「회의 중 현황판 만들어 줘」

여러 사람이 동시에 보고 고치고, 회의가 끝나면 Claude 가 결과를 읽어 정리해야 한다 → **`db`**. 누가 바꿨는지 남기려면 **`user`** 를 더하고, 세션이 고칠 때는 **`if_version`** 을 붙인다.


English companion: [capability-selection-table_en](capability-selection-table_en.md)
