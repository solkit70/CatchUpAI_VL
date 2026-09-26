---
title: "루틴이 안 돌았을 때 — 확인 순서"
created: 2026-09-21 10:50:00
tags:
  - claude-artifacts-routines
  - m4
  - troubleshooting
---

## 먼저 가를 것

「루틴이 안 돌았다」는 세 가지가 섞인 말이다. 순서대로 가른다.

| 증상 | 뜻 | 어디를 보나 |
|---|---|---|
| **실행 자체가 없다** | 발화(fire)가 안 됐다 — 루틴 비활성 · 일정 오류 · 환경 없음 | 루틴 설정 (`get`): `enabled` · `next_run_at` · `environment_id` |
| **실행은 됐는데 실패했다** | 세션은 떴고 안에서 죽었다 | 실행 로그 (`list_runs` → `get_run_log`) |
| **실행도 성공인데 결과가 없다** | 조건부 알림이라 조용한 것 · 또는 필터가 안 먹어 「없음」으로 끝난 것 | 로그의 마지막 요약 + 응답에 찍힌 실제 검색 조건 |

`schedule` 스킬을 로드하면 `RemoteTrigger` 도구로 이 세 가지를 세션 안에서 다 볼 수 있다 — claude.ai 화면을 열지 않아도 된다.

## 확인 순서

1. **`get`** — `enabled: true` 인가, `next_run_at` 이 미래인가, `last_run.status` 는 무엇인가
2. **`list_runs`** — 최근 실행이 있나. **없으면** 발화 전 단계 문제(일시정지 · 환경 · 레포 접근)이고 로그도 없다
3. **`get_run_log`** — 있으면 로그를 연다. 볼 것:
   - `tool_result ERROR` 줄 — 무엇이 어디서 실패했나
   - `connect_rejected` · `EGRESS_BLOCKED` · `organization policy` → **네트워크 정책** (아래)
   - `InputValidationError` → 도구 인자 형식 (예: PushNotification `status` 값)
   - 마지막 `result:` 줄 — 루틴 자신의 요약
4. **같은 요청을 내 PC 에서** — 실패한 URL 을 로컬에서 `curl` 해 본다. 200 이면 상대 서버 문제가 아니라 **환경** 문제다
5. **환경 네트워크 모드** — claude.ai/code → New → `Default` 칩 → Cloud → 환경 편집 → **Network access**
   - `Trusted` = 패키지 저장소 + Anthropic API 만 허용. 외부 사이트를 읽는 루틴은 여기서 막힌다
   - 필요한 도메인만 추가하거나 Full 로
6. **수동 실행(`run`)으로 검증** — 고친 뒤 다음 주까지 기다리지 말고 바로 돌려 로그를 본다

## 자주 헷갈리는 것

- **WebFetch 는 되는데 curl 이 안 된다 / 둘 다 안 되는데 WebSearch 는 된다** → WebSearch 는 검색 API 라 에이전트 프록시를 안 거친다. WebSearch 결과로 「확인했다」고 하면 안 된다 — 2차 정보다
- **환경 설정이 Settings 메뉴에 없다** → Settings → Claude Code 는 CLI·데스크톱 연결 관리다. 클라우드 환경은 **New 세션 패널의 환경 칩** 안에 있다
- **루틴 API 로 환경을 못 고친다** → `RemoteTrigger update` 는 `environment_id` 를 바꿀 수 있을 뿐 환경의 네트워크 규칙은 웹 UI 전용
- **결과가 「0건」이라고 필터가 먹은 게 아니다** → 응답에 찍힌 실제 검색 조건(예: amazon.jobs 의 `job_posting_search_request.filterFacets`)을 확인한다. 비어 있으면 파라미터가 무시된 것

## 실제 사례

- [../guides/wblp-routine-audit.md](../guides/wblp-routine-audit.md) — 2026-09-07~21, 3주 연속 `EGRESS_BLOCKED` → 환경 Network access 변경으로 복구 + 무시되던 검색 파라미터 발견
