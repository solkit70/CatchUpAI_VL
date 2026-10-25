# 받는 곳 문서를 볼트 규칙에 맞추는 단계와 프롬프트

> 밖에서 Muse 로 만든 문서가 받는 곳(Inbox)에 도착한 뒤 집에서 하는 정리다. 받는 곳은 박창수가 **A — 볼트 루트의 `_Inbox_/` 에 바로**로 정했다(2026-10-25). 비교와 후보는 [transfer-comparison.md](transfer-comparison.md), 시험 결과는 [../examples/sample-transfer.md](../examples/sample-transfer.md).

## 정리 단계 (6단계)

| # | 단계 | 이유 |
|---|---|---|
| 1 | **내부 · 비밀 내용이 없는지 먼저 본다** — 연락처 · 금액 · 계정 · 🔒 표시 | 볼트에서도 밖으로 나가는 문서가 될 수 있다 |
| 2 | 파일 이름을 `YYYY-MM-DD 제목 by Muse.md` 로 바꾸고 `_Inbox_/` 에 둔다 | 볼트 산출물 이름 규칙(`YYYY-MM-DD [이름] by [에이전트]`) |
| 3 | frontmatter 를 **영어 소문자 키**로 붙인다 — `title` · `created` · `author` · `tags` + 출처 표시(`origin` · `reviewed`) | 볼트 규칙. Muse 는 한글 키를 만든 적이 있다 |
| 4 | 첫 줄 `# 제목` 을 `## 제목` 으로 내린다 (frontmatter 뒤에는 섹션 제목으로 시작) | 볼트 구조 규칙(「제목을 H1 으로 중복하지 않는다」) |
| 5 | 본문은 **고치지 않는다**. 링크 · 표 · 목록이 깨졌는지만 보고, 깨졌으면 그 자리만 고친다 | Muse 가 쓴 글의 원문을 지킨다 |
| 6 | `reviewed` 는 사람이 읽은 뒤에만 `true` 로 바꾼다 | 「검토 여부」가 거짓이 되면 출처 표시가 쓸모없다 |

## 머리말 규칙

```yaml
---
title: "문서 제목"
created: 2026-10-25 07:00:00
author:
  - "Muse"
tags:
  - muse-inbox
origin: muse
reviewed: false
---
```

- `origin: muse` 와 `reviewed` 가 이 Topic 의 출처 표시다(Muse 에서 만든 것 · 검토 여부). 날짜는 `created` 가 맡는다.
- `created` 는 **볼트에 만든 시각**이다. Muse 가 만든 시각은 모를 때가 많으니 쓰지 않는다.
- `tags` 는 `#` 없이 목록으로 쓴다. 정리가 끝나 제자리로 옮길 때 `muse-inbox` 태그를 뺀다.

## Claude Code / Codex 프롬프트

```text
받는 곳에 도착한 Muse 문서를 볼트 규칙에 맞게 정리해 줘.
대상 파일: {파일 경로}

1. 먼저 연락처 · 금액 · 계정 · 비밀번호 · 🔒 표시가 있는지 보고, 있으면 정리하지 말고 알려 줘.
2. 파일 이름을 `YYYY-MM-DD 제목 by Muse.md` 로 바꿔서 `_Inbox_/` 에 둬.
3. frontmatter 를 아래 형식으로 붙여 줘. 키는 영어 소문자야. 한글 키는 쓰지 마.
   title · created(지금 시각 YYYY-MM-DD HH:MM:SS) · author(- "Muse") · tags(- muse-inbox) · origin: muse · reviewed: false
4. 첫 줄의 `# 제목` 은 `## 제목` 으로 내려.
5. 본문 글자는 한 글자도 고치지 마. 링크 · 표 · 목록이 깨진 곳만 알려 주고, 고쳤으면 어디를 고쳤는지 적어.
6. `reviewed` 는 false 로 둬. 내가 읽고 나서 바꿀게.

끝나면 바꾼 것을 5줄 안으로 보고해 줘.
```

## 밖으로 내보낼 때 꾸러미에 넣을 한 줄

집 → 밖 꾸러미에도 이 규칙을 알려 줘야 Muse 가 처음부터 맞게 만든다.

```text
볼트 frontmatter 는 영어 소문자 키(title · created · author · tags)를 쓰고, 문서 첫 제목은 H2(##)로 시작한다.
```
