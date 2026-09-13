---
title: "아티팩트 공개 범위 — 페이지 층과 데이터 층 (문서 + 실측)"
created: 2026-09-13 08:05:00
tags:
  - claude-artifacts-routines
  - m2
  - concept
---

## 공개 범위는 셋, 이 계정은 둘

| 범위 | 누가 보나 | 어느 플랜 | 이 계정(Pro/Max) |
|---|---|---|---|
| 나만 (Only you) | 소유자 | 전부 | ✅ 기본값 `[실측 발행 결과 sharing owner]` |
| 조직 (Everyone at … / 특정 사람) | 로그인한 조직 구성원 · 편집자 지정 · **댓글** | Team · Enterprise | ❌ 메뉴에 없음 `[실측]` |
| 공개 링크 (Anyone with the link) | 링크를 아는 누구나, 로그인 불요 | Pro/Max 는 이것뿐 · Team/Enterprise 는 Owner 가 켜야 | ✅ |

> *"On Pro and Max plans, a public link is the only way to share an artifact."* — [공식 문서](https://code.claude.com/docs/en/artifacts) `[문서]`

## 페이지 층과 데이터 층은 따로 논다

공개 링크를 켜면 **HTML 은 누구나** 보지만, **런타임 기능이 만드는 데이터는 로그인한 사용자만** 본다 `[실측 09-13 + 플랫폼 대화상자]`.

```
공개 링크 ON
├── 페이지(HTML · 인라인 데이터)  → 익명도 봄. 상단에 "Content is user-generated and unverified"
└── db 데이터                    → 익명: use("db") = null, 토스트 "Sign in to see this artifact's data"
                                 → 로그인 사용자: 읽음 (대화상자 문구 · 실측은 M3)
```

capability 별로 공개 자체를 막는 것도 있다:

| capability | 공개 링크 | 근거 |
|---|---|---|
| 없음 / `artifact`(republish) | 가능 | 실측 |
| `db` | **페이지 가능, 데이터는 로그인 필요** | 실측 + 대화상자 |
| `assets` | 불가 — "organization-internal (never public)" | 세션 스킬 0.2.46 `[문서]` |
| `mcp` | 불가 — "can't be shared to a public link on any plan" | 공식 문서 `[문서]` |
| `room` · `sample` · `downloads` | 미확인 (`room` 은 "same-org viewers" 전제) | ⬜ |

## 이 계정에서 안 되는 것 (플랜)

- 댓글 · 편집자 · 조직 공유 — Team/Enterprise 전용 `[문서]`
- 따라서 "댓글을 AI 에게 보내면 답한다"는 기능은 **지금 계정에선 시연 불가** — 영상(M6)에서 다루려면 플랜 조건을 명시

## 확인 순서 — 남에게 링크를 주기 전에

1. Share 메뉴가 "Only you" 면 아직 나만 본다
2. 공개로 바꾸면 **대화상자 문구**를 읽는다 — 데이터 층 조건이 거기 적혀 있다
3. **시크릿 창**에서 연다 — 소유자 브라우저는 항상 최신·전부를 보여 준다
4. db 페이지면 시크릿 창에서 **내용이 비는지** 본다 — 비면 정적으로 다시 만든다
