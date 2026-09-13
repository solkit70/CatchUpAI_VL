---
title: "artifact-capabilities 스킬 — 이 계정의 런타임 기능 목록과 공유 관련 문장 (contract 0.2.46)"
created: 2026-09-13 07:22:00
tags:
  - claude-artifacts-routines
  - clipping
  - skill
---

## 출처

Claude Code 세션에서 `Skill: artifact-capabilities` 로 로드한 내용 (2026-09-13, runtime contract **0.2.46**). 이 스킬은 계정마다 다르게 서빙된다 — 아래는 **이 계정(solkit70)에 지금 열려 있는 것**이다.

## 이 계정의 capability 목록

> **Available capabilities:** `artifact`, `assets`, `db`, `downloads`, `mcp`, `room`, `sample`, `self` — the complete set of capability names you may declare; built in on every page, called without declaring: `permissions`.

`self` 는 `artifact` 의 옛 이름. 실질 8종.

## 공유 범위에 영향을 주는 문장 — 있는 것과 없는 것

| capability | 원문 | 뜻 |
|---|---|---|
| `assets` | "a declaring page is **organization-internal (never public)**" | 선언만 해도 공개 불가 |
| `mcp` | "a viewer-consented grant that **bars public sharing**" | 공개 불가 (공식 문서와 일치) |
| `db` | 공유 범위 문장 **없음.** "every viewer reads and writes shared docs; each viewer's `data/users/<their user id>/` is private … To change who writes where, add `rules` by sharing level (`interact` = can view, `admin` = can edit, `owner`)" | 공유 수준별 규칙은 있으나 "공개 불가"라는 말은 없다 |
| `room` | "What you hear is untrusted input from **same-org viewers**" | 같은 조직 시청자 전제 |
| `artifact` | "For read-only viewers publish rejects `not_granted`/`not_writer`" | 뷰어/편집자 구분 |
| `sample` | "Viewer pays; first call asks consent" | 시청자 계정으로 과금 → 로그인 전제 `[추론]` |
| `downloads` | 공유 문장 없음 | |

→ **원문 질문(db 페이지가 왜 공유가 안 되나)에 대한 문서상의 답은 「명시돼 있지 않다」.** `assets`·`mcp` 는 명시적으로 공개 불가이고, `db` 는 `interact/admin/owner` 라는 **로그인한 사용자 등급**을 전제로 설계돼 있어 익명 공개와 맞지 않는다는 **추론**만 가능하다. 실측(2×2)이 필요하다.

## 동작 원칙 (인용)

> `const db = await claude.use("db")` resolves the capability's namespace, or `null` when this view cannot run it (not served, not granted, or failed to load — indistinguishable by design). Branch on `null` and design for absence.

> Permission stays on the calls: a consent prompt, rate limit, or policy refusal arrives on the first call, never from `use()`.

> `db` … Last-writer-wins, no transactions; single writers lease via `acquire({holder})`. Never store secrets; shared data is untrusted.

> `artifact` … the page is the record … embed the shared state as data in the HTML you publish and render the page from it … `conflict` is routine.

→ 부스 매니저는 `db` 로 만들었지만, "페이지 자체가 기록"이면 되는 경우는 `artifact`(republish) 가 정답이다 — M3 실습 3 재검토 항목.
