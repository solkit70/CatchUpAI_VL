---
title: "M3 실습 1 — 런타임 기능 5종 최소 예제 기록"
created: 2026-09-27 15:30:00
author:
  - "Claude Code"
tags:
  - claude-artifacts-routines
  - m3
  - lab-log
---

## 무엇을 했나

런타임 기능 5종을 가장 작은 예제로 하나씩 발행했다. 발행은 VS Code 의 Claude Code 확장에서 `Artifact` 도구로 했고(브라우저 조작 없음), 기능 규칙은 `artifact-capabilities` 스킬(runtime contract **0.2.60**)의 타입 정의를 기준으로 삼았다. 화면 확인은 사용자가 발행된 URL 을 열어 한다.

## 발행 결과

| # | 예제 | 선언한 capability | URL | 발행 결과가 알려 준 것 |
|---|---|---|---|---|
| ① | [01-counter-db.html](../examples/01-counter-db.html) | `{db: {}}` | https://claude.ai/artifact/8p4xaEhHXB6PQyzDZfy3os | contract 0.2.60 · readable by only you |
| ② | [02-hello-user.html](../examples/02-hello-user.html) | `{user: {scopes: ["profile"]}}` | https://claude.ai/artifact/2ofKVvCX9eW1dyoXYcPpdD | 〃 |
| ③ | [03-image-assets.html](../examples/03-image-assets.html) | `{assets: {}}` | https://claude.ai/artifact/EXRfAfWCLDNE89HG5jqc6s | 〃 · 세션에서 이미지 1장 업로드 → `/_blob/8bba69ce…` |
| ④ | [04-comments.html](../examples/04-comments.html) | `{comments: {composer_only: true}}` | https://claude.ai/artifact/AaVvLju4haYcDktsR9StFA | 〃 |
| ⑤ | [05-multi-file/](../examples/05-multi-file/index.html) (`index.html` + `app.css` + `data.json`) | 없음 (`files` 매개변수로 함께 발행) | https://claude.ai/artifact/J5KcHHynLoAd3MRkorftTR | capability 줄이 없다 — 런타임 기능을 선언하지 않은 페이지 |

## 화면 확인 (사용자)

| # | 확인할 것 | 내 창 (owner) | 다른 계정 · 시크릿 창 |
|---|---|---|---|
| ① | 숫자 **11** 이 보이는가 (세션이 쓴 값) · +1 을 누르면 12 가 되는가 | ✅ 22:28 +1 두 번 → 13 (v4, `by: page`) → 세션이 읽음 → [db-roundtrip](db-roundtrip.md) | ⏳ |
| ② | 「안녕하세요, ○○ 님」 · owner 예 · 편집 예 | ✅ 기대대로 (사용자 확인) | 생략 |
| ③ | QR 이미지 1장이 보이는가 · 업로드 칸이 보이는가 | ✅ 기대대로 — 세션에서 올린 QR 이 페이지 목록에 보임 | 생략 |
| ④ | 버튼을 누르면 그 문단에 댓글 창이 열리는가 | ✅ 22:24 — 1번 문단(`#c1`)에 댓글 2건이 그 문단에 붙었다. 「Send to Claude」로 보내자 이 세션이 **자동으로 답했다**(auto-reply). 확인 후 두 스레드를 세션에서 resolve. 22:25 2번 문단 댓글은 문단(`#c2`)이 아니라 **버튼(`#c2 > button`)에** 붙었다 — 페이지 버튼이 연 창은 넘긴 요소(문단)에, 댓글 모드로 직접 누른 곳은 그 요소(버튼)에 붙는 것으로 보인다. 22:26 3번 문단(`#c3 > button`) 도 확인 — 문단 3개 모두 댓글이 붙었다. ⚠️ 자동 답의 **언어가 일정하지 않았다**: 1·2번 스레드는 한국어, 3번 스레드는 영어로 답했다 (댓글이 영어 「test」 한 단어라서로 보임) | ⏳ |
| ⑤ | 「여러 파일 발행 성공」 · data.json 읽기 「예」 | ✅ 기대대로 | 생략 |

> 다른 계정 확인은 생략했다 (사용자 판단: 「간단하게 테스트하고 넘어갈 수 있는 것으로」). 공유 범위 차이는 발행 결과와 문서 규칙으로만 기록한다.

> 모든 예제가 지금은 「나만 볼 수 있음」(private) 이다. 시크릿 창(로그아웃 상태)에서는 **열리지 않는 것이 정상**이다. 다른 사람 화면을 보려면 Share 메뉴에서 공유해야 하며, db · user · assets 를 선언한 아티팩트는 **조직 안에서만** 공유할 수 있다(공개 링크 불가). `composer_only` 댓글과 capability 없는 ⑤ 는 공개 링크가 가능하다 — 이 차이를 Share 메뉴에서 확인한다.

## 발견 — 세션의 아티팩트 감시(watch)는 10개까지

예제 5개를 연달아 발행하자, 이 세션이 감시하던 기존 아티팩트 둘(부스 매니저 · 부스 현황판)의 감시가 **자동으로 끊겼다.** 알림 원문: *"this session reached its limit of 10 artifact watches and made room to watch a newer one; it was auto-replying to comments, and that stops until its next publish."* 발행할 때마다 그 아티팩트를 감시 목록에 올리고, 한 세션의 한도는 10개다. 댓글 자동 답을 걸어 둔 아티팩트가 있으면, 실습용 발행을 여러 개 할 때 그쪽 감시가 밀려난다 → [troubleshooting](../troubleshooting/cdn-and-storage-gotchas.md)


English companion: [lab-log_en](lab-log_en.md)
