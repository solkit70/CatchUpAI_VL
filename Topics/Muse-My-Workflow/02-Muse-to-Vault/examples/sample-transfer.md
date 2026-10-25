# 시험 결과 한 건 — 전 · 후

> 2026-10-25 Live #33 1부. 공개해도 되는 가짜 내용으로 Muse 가 만든 Markdown 파일 하나를 받는 곳 규칙에 맞게 정리하는 시험이다. 정리 단계는 [../guides/vault-cleanup-prompt.md](../guides/vault-cleanup-prompt.md). 이 예시는 시험이라 **실제 볼트의 `_Inbox_/` 에는 넣지 않았다.**

## 전 — Muse 에서 받은 그대로 (397바이트)

```markdown
# Muse 시험 01

- 오늘 날씨: 시애틀 오전 비, 최고 55°F / 최저 47°F, 오후 흐림
- 공개 행사: Seattle AI Week 개막 (Thinkspace, Seattle)
- 방송 이야기: Catch Up AI 방송 준비

| 항목 | 상태 |
|---|---|
| 오늘 날씨 | 확인 완료 |
| 공개 행사 | 확인 완료 |
| 방송 이야기 | 준비 중 |

[Meta](https://www.meta.com)

2026-10-25 시험 파일
```

## 후 — 받는 곳 규칙에 맞춘 것

파일 이름: `2026-10-25 Muse 시험 01 by Muse.md` (위치: `_Inbox_/`)

```markdown
---
title: "Muse 시험 01"
created: 2026-10-25 07:20:00
author:
  - "Muse"
tags:
  - muse-inbox
origin: muse
reviewed: false
---

## Muse 시험 01

- 오늘 날씨: 시애틀 오전 비, 최고 55°F / 최저 47°F, 오후 흐림
- 공개 행사: Seattle AI Week 개막 (Thinkspace, Seattle)
- 방송 이야기: Catch Up AI 방송 준비

| 항목 | 상태 |
|---|---|
| 오늘 날씨 | 확인 완료 |
| 공개 행사 | 확인 완료 |
| 방송 이야기 | 준비 중 |

[Meta](https://www.meta.com)

2026-10-25 시험 파일
```

## 바뀐 것과 안 바뀐 것

| | 전 | 후 |
|---|---|---|
| 머리말 | 없음 | 영어 소문자 키 + 출처 표시(`origin: muse` · `reviewed: false`) |
| 첫 제목 | `# Muse 시험 01` | `## Muse 시험 01` |
| 파일 이름 | `Muse 시험 01.md` | `2026-10-25 Muse 시험 01 by Muse.md` |
| **본문(목록 · 표 · 링크 · 마지막 줄)** | 그대로 | **한 글자도 안 바뀜** |

## 확인한 것

- 「전」은 다운로드한 원본 파일과 일치하고, 「후」의 본문(빈 줄 포함 15줄)은 첫 제목의 `#` → `##` 만 빼면 원본과 같다 — 프로그램으로 비교해 확인했다.
- 링크는 외부 주소라 볼트의 위키 링크 규칙에 걸리지 않는다.
- 이 시험에서 정리 단계는 6개 모두 한 번에 끝났다(내부 내용 없음 · 머리말 · 제목 레벨 · 본문 보존 · `reviewed: false`).
