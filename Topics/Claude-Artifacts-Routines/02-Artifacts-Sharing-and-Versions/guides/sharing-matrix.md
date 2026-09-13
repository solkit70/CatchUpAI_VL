---
title: "공유 범위 실험 2×2 — 정적 vs db · 소유자 vs 시크릿 창 (질문 1 의 답)"
created: 2026-09-13 07:35:00
tags:
  - claude-artifacts-routines
  - m2
  - experiment
---

## 실험

같은 세션에서 같은 디자인의 최소 페이지 두 장을 발행했다 `[실측 09-13 07:30]`. 다른 것은 **capabilities 선언 하나**뿐이다.

| 실물 | capabilities | 발행 결과 | 소스 |
|---|---|---|---|
| [정적 페이지 실험](https://claude.ai/code/artifact/3f864d29-c5c5-4d6c-b696-37fcc798ee62) 🔓 | `{}` | Version 1 · `sharing owner` | [examples/minimal-static.html](../examples/minimal-static.html) |
| [db 페이지 실험](https://claude.ai/code/artifact/a3bb593a-c879-42c2-b996-e11cc167ec1d) 🔐 | `{db: {}}` — 열릴 때마다 `probe/hits.count` +1 | Version 1 · `capabilities db · sharing owner` | [examples/minimal-db.html](../examples/minimal-db.html) |

둘 다 발행 직후 상태는 **`sharing owner`(나만)** — 공식 문서 *"A new artifact is visible only to you"* 와 일치 `[문서]`.

## 2×2 표 — 실측 칸

| | 정적 (`{}`) | db (`{db: {}}`) |
|---|---|---|
| **소유자 브라우저** | ✅ 열림 · `window.claude` 있음(use 만) `[실측 07:43]` | ✅ 열림 · `use("db")` → namespace · **count 1** `[실측 07:43]`. 세션에서 `read_db probe/hits` → `{count:1, last:"2026-09-13T13:43:24Z"}` version 1 `[실측]` — **화면이 쓴 것을 세션이 읽었다** (질문 6 의 절반) |
| **Share 메뉴에 뜨는 선택지** | People with access: Owner(나) · General access: **Only you / Only people with access / Anyone with the link** ("People with the link can view, but not edit") `[실측 07:50 스크린샷]` | **정적과 완전히 같은 메뉴.** "Anyone with the link" 선택지가 **있다** `[실측 07:50]` → 메뉴 수준에서는 db 가 공개 공유를 막지 않는다 |
| **시크릿 창 — 공유 전** | (미실측 — 발행 직후 `sharing owner` 이므로 Sign in 일 것) | (동일) |
| **시크릿 창 — 공개 링크 켠 뒤** | (미실측 — db 쪽으로 충분) | ✅ **페이지는 열림** ("Content is user-generated and unverified" 라벨) · **`use("db")` → `null — 이 뷰에서는 db 를 못 쓴다`** · count `—` · 화면 하단 토스트 **"Sign in to see this artifact's data · Sign in"** `[실측 07:58 스크린샷]` |
| **공개 전환 확인 대화상자** | — | *"Anyone with this link can view this artifact, even without a Claude account or sign-in. This includes people outside your organization. **People who sign in to Claude will also be able to read its data.**"* `[실측 07:57 — 플랫폼 문구]` |
| **다른 계정 (로그인)** | | ⬜ 미실측 — 대화상자 문구대로면 데이터가 보여야 한다 (M3 에서 확인) |

## 문서가 말하는 것 (실험 전에 아는 것)

| 근거 | 내용 |
|---|---|
| 공식 문서 `[문서]` | 커넥터(mcp) 페이지는 **어떤 플랜에서도 공개 불가**. Pro/Max 는 공개 링크가 유일한 공유 수단. **db 에 대한 문장은 없다** |
| 세션 스킬 0.2.46 `[문서]` | `assets` 선언 = "organization-internal (never public)". `mcp` = "bars public sharing". **`db` 는 공유 범위 문장 없음** — `interact/admin/owner` 등급(로그인 사용자) 전제 |
| 9/3 경험 `[실측]` | 부스 매니저(db) 는 링크 공유가 안 됐다고 들었다 |
| 9/13 시크릿 창 `[실측]` | 부스 매니저 → Sign in. 단, 그것이 "공유를 안 켠 것"인지 "켤 수 없는 것"인지는 이 실측만으로 구분 안 됨 |

## 부수 발견 — 이 계정의 플랜

Share 메뉴에 **조직(organization) 선택지가 없다** — "Only people with access / Anyone with the link" 둘뿐 `[실측]`. 공식 문서의 *"On Pro and Max plans, a public link is the only way to share"* 와 맞는다 → **이 계정은 Pro/Max 다** `[문서+실측]`. 따라서:
- **댓글은 이 계정에서 불가능하다** — *"only an artifact you share within your organization takes comments"* (Team/Enterprise). 실습 3 의 댓글 항목은 「해당 없음」으로 닫는다
- 편집자(editor) 지정도 불가 — 같은 이유
- 9/1 설명 페이지 A6 의 "댓글을 남길 수 있다"는 **이 계정에서는 틀린 문장**이다 → 영상(M6)에서 빼거나 플랜 조건을 붙인다

## 질문 1 의 답

> **db 가 있는 아티팩트는 왜 링크 공유가 안 되는가? 설정인가 구조인가?**

**둘 다 반쯤 맞고, 정확한 답은 이것이다 — 페이지와 데이터의 공개 범위가 다르다.** `[실측 09-13 + 플랫폼 대화상자 문구]`

| 층 | 공개 링크를 켜면 | 근거 |
|---|---|---|
| **페이지(HTML)** | 누구나 본다 — 로그인·계정 불요 | 시크릿 창에서 열림 · "Content is user-generated" 라벨 |
| **db 데이터** | **로그인한 Claude 사용자만** 읽는다. 익명 뷰에서는 `use("db")` 가 `null` | 대화상자 *"People who sign in to Claude will also be able to read its data"* · 시크릿 창 토스트 *"Sign in to see this artifact's data"* |

그래서 **부스 매니저처럼 내용 전부가 db 에서 오는 페이지**는 공개 링크를 켜도 익명 시청자에겐 **빈 껍데기**로 보인다 — 9/3 에 "링크 공유가 안 된다"고 한 것은 이 뜻이었다. 설정으로 "익명도 데이터를 보게" 만드는 선택지는 **없다**(대화상자에 그런 옵션 없음) → **구조**. 반면 페이지 공유 자체는 **설정**이고 켤 수 있다.

**실무 결론**: 남에게 보여 줄 것이면 ① db 없이 정적으로 만들거나(부스 현황판 경로) ② db 페이지라도 **핵심 내용은 HTML 에 박고 db 는 부가 상태**에만 쓰거나 ③ 보는 사람이 전부 Claude 로그인 사용자여야 한다. 이것이 M5 패턴 1 이다.

**남은 것**: 로그인한 **다른** 계정이 실제로 데이터를 읽는지(대화상자 문구의 실측) — M3 에서 가족 계정으로.

## 실습 3 — 버전 · 댓글 · watch (이 계정에서 가능한 범위)

| 항목 | 결과 |
|---|---|
| 댓글 | **해당 없음** — Pro/Max 는 조직 공유가 없고, 댓글은 조직 공유에서만 `[문서]`. read→reply→resolve 는 이 계정에서 실행 불가. Team/Enterprise 계정이 생기면 그때 |
| 편집자 | 해당 없음 — 같은 이유 |
| watch | 세션당 **최대 5개** `[실측]`. `status`: 오늘 다룬 아티팩트 4건(resume 때 재무장) + 정적 실험 페이지 = 5 → db 실험 페이지는 **watch 안 됨**. 다른 세션이 고쳐도 이 세션은 모른다 → 편집 전 `read` 가 필요한 이유 |
| 버전 | 정적·db 실험 페이지 각 Version 1. 재발행 시 같은 URL 에 Version 2 — 9/12 부스 현황판 v11 로 이미 실측 `[실측]`. Share 의 "Always share latest version" 토글은 스크린샷의 메뉴엔 안 보였다(공개 전엔 없음?) — 공개 후 메뉴 재확인 필요 ⬜ |

## 부수 실측 — 이 세션에서 나온 것

- 발행 결과 문구에 `sharing owner` 가 찍힌다 → 세션도 공유 상태를 안다 `[실측]`. `action: status` / `list` 로도 확인 가능
- **세션당 아티팩트 watch 한도 5개** — db 페이지를 발행하자 *"watch limit reached — this session already holds its maximum of 5"* 알림 `[실측 07:31]`. 오늘 세션에서 6개를 다뤘기 때문. 실습 3(watch) 의 제약 조건
