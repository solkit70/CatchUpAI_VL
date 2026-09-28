---
title: "M4 실습 2 — 두 번째 루틴: 내일 일정 미리보기 (1회)"
created: 2026-09-27 15:40:00
author:
  - "Claude Code"
tags:
  - claude-artifacts-routines
  - m4
  - routine
---

## 왜 이 루틴인가

첫 루틴(WBLP)은 **반복 + 외부 웹 확인**이었다. 두 번째는 겹치지 않게 **일회성 + 커넥터만** 으로 골랐다 — 판단표의 두 축(네트워크 허용 목록 vs 커넥터, 반복 vs 일회성)을 한 번씩 실물로 확인하기 위해서다. 볼트가 필요 없는 일이라 클라우드가 맞다 → [판단표](../concepts/local-vs-cloud.md). 사용자 승인: 「예 승인 하겠습니다. 진행 해 주세요.」 (2026-09-27)

## 설정

| 항목 | 값 |
|---|---|
| 루틴 | 내일 일정 미리보기 (1회) · `trig_01TyCwrfL1H3vsmdkmcDS8xk` · https://claude.ai/code/routines/trig_01TyCwrfL1H3vsmdkmcDS8xk |
| 만든 곳 | VS Code Claude Code 확장 세션 · `schedule` 스킬 → `RemoteTrigger create` |
| 트리거 | `run_once_at: 2026-09-27T23:07:00Z` (16:07 PDT) — 정각을 피해 :07 (공식 문서 권고) |
| 레포 | 없음 |
| 환경 | `Default` (Trusted) — 바꾸지 않음. 커넥터는 허용 목록과 무관하다는 문서 내용을 확인하려는 것 |
| 커넥터 | Google-Calendar(읽기) · Gmail(보내기) — Claude-Docs 는 뺐다 (문서: 「기본으로 전부 포함 · 쓰기도 묻지 않음」 → 필요한 것만) |
| 도구 | Read · Write (Bash · WebFetch 없음) |
| 모델 | claude-sonnet-5 |
| 프롬프트 핵심 | 9/28(월) 일정을 읽어 한국어 한 줄씩 메일 · 설명·참석자 이메일·회의 링크는 옮기지 않는다 · 캘린더를 못 읽으면 **실패도 메일로** 알린다 (WBLP 에서 배운 「조용한 실패」 방지) |

## 실행 결과 — ✅ 성공 (세션 `cse_017Jz54UXyMTvroETg979pEP`)

| 시각 (UTC) | 로그 |
|---|---|
| 23:07:00 | 예정 시각 |
| **23:08:11** | 실제 시작 — **1분 11초 늦게** (:07 로 잡았는데도) |
| 23:08:13 | 샌드박스 · 「No sources configured」 「No setup script configured」 — 레포 없이 도는 루틴 |
| 23:08:20 | 커넥터 도구를 `ToolSearch` 로 불러옴 (`mcp__Google-Calendar__*` · `mcp__Gmail__*`) |
| 23:08:23~32 | `list_calendars` → 캘린더 **4개** 각각 `list_events` (9/28 00:00~23:59 PDT) → 일정 **0건** |
| 23:08:37 | `send_message` → 「9/28(월) 캘린더에 등록된 일정이 없습니다.」 메일 발송 |
| 23:08:42 | `result: success` · 9 turns · **25초** |
| (확인) | 사용자: 「내일 일정 미리 보기 이메일이 왔습니다.」 — 메일함에서 수신 확인 |

실행 뒤 `get`: `enabled: false` · `ended_reason: "run_once_fired"` — 일회성은 한 번 돌고 스스로 꺼졌다 (웹 UI 의 **Ran**). 단, `next_run_at` 에 하루 뒤 값이 남아 보이는데 `enabled: false` 라 돌지 않는다 — 표시만의 잔재로 본다.

## 배운 것

- **커넥터는 `Default`(Trusted) 환경을 그대로 두고도 됐다** — WBLP 처럼 네트워크 허용 목록을 고칠 필요가 없었다 (문서 「Connectors … don't need allowlist changes」 실측 확인)
- 루틴은 캘린더 이름을 몰라도 `list_calendars` 로 먼저 목록을 뽑고 하나씩 읽었다 — 「모든 캘린더」라고만 써도 된다
- 결과가 0건이어도 메일을 보내게 한 덕에 **「실행이 됐다」가 메일함에서 바로 보였다.** WBLP 의 「조건 충족 때만 메일」과 반대 설계 — 알림 루틴은 목적에 따라 둘 중 하나를 고른다
- :07 로 잡아도 약 1분 늦었다 — 분 단위 정확도가 필요한 일에는 맞지 않는다
