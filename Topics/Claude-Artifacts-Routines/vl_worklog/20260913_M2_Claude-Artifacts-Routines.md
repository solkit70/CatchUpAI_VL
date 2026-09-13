---
title: "M2 — 페이지와 데이터의 공개 범위가 다르다 · 이 계정은 댓글이 안 된다"
created: 2026-09-13 07:15:00
author:
  - "Claude Code"
topic: "Claude-Artifacts-Routines"
module: "M2"
tags:
  - vibelearn-ai
  - worklog
  - claude-artifacts-routines
---

## 세션 개요

| 항목 | 값 |
|---|---|
| 날짜 | 2026-09-13 (일) — Live #27 2부 ② 방송 중, M1 에 이어 |
| 시작 · 종료 | 07:15 · 08:10 |
| **실소요** | **55분.** 그중 사용자 대기 약 12분 (Share 메뉴 스크린샷 2회 · 공개 전환 + 시크릿 창 1회). 예상 2.5h |
| 직전 WorkLog 「개선할 점」 체크 | M1: *"사례 인덱스가 갤러리를 안 보고 볼트만 뒤졌다"* → 이번엔 문서·스킬·실물 세 출처를 다 봤다. 지켰다 |
| 모듈 | **M2 — Artifacts 공식 문서 · 공개 범위 · 버전** |
| 결과 | **질문 1 답 완료.** 공식 문서·스킬 클리핑 2건. 실험 페이지 2개 발행 · 2×2 실측. 부수: 이 계정은 Pro/Max → 댓글·편집자 불가 |

## 오늘의 학습 목표

- [x] 공개 범위 종류와 조건을 공식 문서 인용으로 (3종 — 나만·조직·공개)
- [x] 「db 페이지는 왜 공유가 안 되나」 답 — 문서엔 없었고 **실험 + 플랫폼 대화상자 문구**로 답했다
- [x] 버전·watch 실측 / [x] 댓글 — 해당 없음(플랜) 으로 닫음

## 진행 내용

### 실습 1 — 공식 문서 클리핑

WebSearch → `code.claude.com/docs/en/artifacts` 전문 fetch → 인용 발췌 저장. **db 에 대한 공유 문장은 문서에 없다.** mcp 는 "어떤 플랜에서도 공개 불가", 세션 스킬에서 assets 는 "never public". 댓글은 Team/Enterprise 조직 공유에서만.

### 실습 2 — 2×2 실험

같은 디자인·`db` 선언만 다른 페이지 둘을 발행(정적 `3f864d29` · db `a3bb593a`). 결과:

| | 정적 | db |
|---|---|---|
| 소유자 | 열림 | 열림 · `use("db")` namespace · count 1 · 세션 `read_db` 로 같은 값 확인 |
| Share 메뉴 | Only you / people with access / **Anyone with the link** | **동일** — db 가 메뉴를 막지 않는다 |
| 공개 전환 대화상자 | — | *"Anyone with this link can view … **People who sign in to Claude will also be able to read its data.**"* |
| 시크릿 창(공개 후) | — | **페이지 열림 · `use("db")` = null · 토스트 "Sign in to see this artifact's data"** |

→ **답: 페이지 층과 데이터 층의 공개 범위가 다르다.** 부스 매니저는 내용 전부가 db 라 익명에겐 빈 껍데기 → "공유가 안 된다"의 정체. 익명에게 데이터를 열 설정은 없다(구조).

### 실습 3 — 버전·댓글·watch

- 댓글·편집자: **이 계정(Pro/Max)에서 불가** — Share 메뉴에 조직 선택지가 없는 것으로 플랜 확정 `[실측+문서]`. 실습은 「해당 없음」
- watch: `status` → **세션당 5개 한도**, db 실험 페이지는 watch 실패 `[실측]`
- 버전: 9/12 부스 현황판 v11 이 이미 실측. "Always share latest version" 토글은 공개 전 메뉴엔 안 보임 ⬜

## 문제 해결 로그

| 문제 | 처리 |
|---|---|
| 문서에 db 공유 문장이 없음 | 실험으로 대체 — 로드맵이 예정한 경로 |
| Share 버튼이 첫 스크린샷에 안 보임 | 우측 끝에 있었다 (스크린샷 폭). 사용자 재캡처 |
| watch 한도 | 실측으로 기록. 대응은 편집 전 `read` |

## Insights (인사이트)

### "공유가 안 된다"는 세 단어가 세 층을 뭉개고 있었다

9/3 의 문장은 페이지·메뉴·데이터를 구분하지 않았다. 실제로는 **메뉴는 열리고, 페이지는 공개되고, 데이터만 로그인 벽 뒤에 남는다.** 질문을 한 층씩 쪼개 실험하니 "설정인가 구조인가"가 "층마다 다르다"로 바뀌었다. 답이 이분법이 아닐 때 이분법 질문은 답을 못 찾는다.

### 플랫폼 대화상자가 문서보다 정확했다

공식 문서에 없는 db 공유 규칙이 **공개 전환 확인 대화상자 한 문장**에 있었다. 실측을 하면서 UI 문구를 캡처한 것이 결정적이었다 — UI 문구도 `[문서]` 급 근거다. M5 패턴: **공개로 바꿀 때 대화상자를 읽는다.**

### 이 계정에서 안 되는 것을 아는 것도 학습이다

댓글·편집자·조직 공유가 Team/Enterprise 전용이라는 것은 문서에 있었지만, 이 계정이 Pro/Max 라는 것은 Share 메뉴가 알려 줬다. 9/1 설명 페이지(A6)의 "댓글을 남길 수 있다"는 **내가 남에게 한 말 중 이 계정에선 틀린 첫 문장**이다. 영상에서 고쳐야 한다.

## DoD 체크리스트 (M2)

- [x] 공식 문서 클리핑 2건 (`vl_materials/`)
- [x] 질문 1 — 실험 결과 + 대화상자 문구로 답 (문서엔 없음 명시)
- [x] 🔴 실물 1건: 2×2 실험용 아티팩트 2개 발행 · URL 기록
- [x] 댓글 read→reply→resolve — **해당 없음(Pro/Max)** 으로 근거와 함께 닫음
- [x] README · 링크 검사 통과
- [x] WorkLog(실소요) · Daily Retrospective · 직전 「개선할 점」 체크

**완료율**: 6/6 (100%) — 댓글 항목은 실행이 아니라 「불가 확정」으로 충족

## Daily Retrospective

**What went well**: 문서 → 스킬 → 실험 순서. 문서에 답이 없다는 것을 먼저 확정하고 실험에 들어가서, 실험 결과가 곧 답이 됐다.
**What could be improved**: 실험 페이지의 표에 "실측" 칸을 넣어 두고 채우지 않았다 — 페이지 안의 빈 표는 시청자에게 미완으로 보인다. 다음엔 페이지에는 결과 표를 두지 않거나, 결과가 나오면 republish 한다.
**Insights**: 위 세 절.
**Tomorrow's focus**: ① M3 실습 2 — 로그인한 다른 계정(가족)으로 db 페이지 열어 데이터가 보이는지 ② 공개 후 Share 메뉴의 "Always share latest version" 확인(사용자) ③ M3 5종 최소 예제 — `artifact`(republish) 부터. 부스 매니저를 `artifact` 로 바꿀지 판단

## 참조 및 산출물

- `02-Artifacts-Sharing-and-Versions/` — README · concepts/{sharing-scopes,capabilities-roster}.md · guides/sharing-matrix.md · examples/minimal-{static,db}.html · troubleshooting/shared-link-shows-old-version.md
- `vl_materials/2026-09-13 Claude Code Artifacts 공식 문서 발췌 (code.claude.com).md` · `2026-09-13 artifact-capabilities 스킬 발췌 (contract 0.2.46).md`
- 실물: 정적 `3f864d29-c5c5-4d6c-b696-37fcc798ee62` · db `a3bb593a-c879-42c2-b996-e11cc167ec1d` (공개 링크 ON)
