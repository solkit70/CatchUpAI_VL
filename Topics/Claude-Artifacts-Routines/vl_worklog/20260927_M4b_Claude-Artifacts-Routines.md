---
title: "M4b — 공식 문서 · 두 번째 루틴(일회성 + 커넥터) · 로컬 vs 클라우드 판단표"
created: 2026-09-27 16:20:00
author:
  - "Claude Code"
topic: "Claude-Artifacts-Routines"
module: "M4"
tags:
  - vibelearn-ai
  - worklog
  - claude-artifacts-routines
---

## 세션 개요

| 항목 | 값 |
|---|---|
| 날짜 | 2026-09-27 (일) 오후 — M3 를 마친 직후 같은 세션, 사용자 「예 M4 를 진행 해 주세요」 |
| 실소요 | 약 45분 (그중 루틴 실행 대기 약 30분) |
| 도구 | VS Code Claude Code 확장 · `schedule` 스킬 → `RemoteTrigger` (list · list_runs · create · get_run_log · get) · WebFetch |
| 직전 WorkLog(M4a) 개선할 점 | 「환경 설정 위치를 추정으로 안내하지 말고 먼저 확인한다」 → 이번에는 공식 문서를 먼저 읽고 안내했다. 환경 설정은 바꿀 일이 없었다 |
| 결과 | **M4 ✅ 6/6** |

## 진행 내용

### 1. WBLP 루틴 상태 (5분)

`list_runs`: 9/7 · 9/14 · 9/21(정기) · 9/21(복구 뒤 수동) 4회. cron `0 15 * * 1` = **매주 월 08:00 PDT** (9/21 WorkLog 의 「일요일」 표현은 월요일이 맞다). 마지막 실행 성공, 다음 **9/28 08:12 PDT** — 환경을 고친 뒤 첫 정기 실행.

### 2. 공식 문서 클리핑 (10분)

`code.claude.com/docs/en/routines` (research preview) → [클리핑](../vl_materials/2026-09-27%20Routines%20공식%20문서%20클리핑.md) · [routines-basics](../04-Routines-Lab/concepts/routines-basics.md). 새로 확인: 커넥터는 네트워크 허용 목록과 무관 · 커넥터는 기본으로 전부 포함되고 쓰기도 묻지 않음 · 초록색 상태 ≠ 할 일 성공 · 일회성은 하루 한도 밖.

### 3. 판단표 (5분)

[local-vs-cloud](../04-Routines-Lab/concepts/local-vs-cloud.md) — 볼트를 읽거나 쓰면 로컬(GDR · TIU · POB 에이전트), 외부만 보면 클라우드(WBLP · 두 번째 루틴). 이 볼트는 GitHub 에 없어서 루틴이 못 읽는다.

### 4. 두 번째 루틴 — 사용자 승인 뒤 발행 (5분 + 대기 30분)

「내일 일정 미리보기 (1회)」 `trig_01TyCwrfL1H3vsmdkmcDS8xk` — 일회성 16:07 PDT · 레포 없음 · Calendar + Gmail 만. **23:08:11 UTC 시작(1분 늦음) → 캘린더 4개 · 일정 0건 → 메일 발송 → 25초에 성공** → 스스로 꺼짐(`run_once_fired`) → [second-routine](../04-Routines-Lab/guides/second-routine.md).

## 문제 해결 로그

| 상황 | 처리 |
|---|---|
| 기다리는 동안 `sleep` 이 막힘 | 백그라운드 `until` 루프로 16:12 까지 대기 → 알림 받고 로그 읽기 (M4a 와 같은 방식) |
| 실행 뒤 `get` 에 `next_run_at` 이 하루 뒤로 남아 보임 | `enabled: false` · `ended_reason: run_once_fired` 라 돌지 않음 — 표시 잔재로 기록 |

## DoD 체크리스트 (M4)

- [x] 공식 문서 클리핑 1건 이상
- [x] WBLP 루틴 실행 이력 실측 + 개선 여부 결정 (9/21 · 오늘 재확인)
- [x] 🔴 두 번째 루틴 발행 + 첫 실행 결과 (로그 · 메일)
- [x] 로컬 vs 클라우드 판단표
- [x] README · 링크 검사
- [x] WorkLog(실소요) · Daily Retrospective · 직전 개선점 체크

## Daily Retrospective

### What went well
- 두 번째 루틴을 WBLP 와 **반대 축**(일회성 · 커넥터만 · 결과 없어도 메일)으로 골라, 판단표의 축을 실물 두 개로 설명할 수 있게 됐다
- 30분 뒤로 잡아 **오늘 안에** 결과까지 확인했다 — 「내일 아침에 보자」로 미루지 않았다

### What could be improved
- 9/21 WorkLog 에 WBLP 실행 요일을 잘못 이해할 여지가 있었다(월요일 실행) — 요일은 cron 에서 바로 옮겨 적는다

### Insights
- 알림 루틴의 두 설계: **「조건이 맞을 때만」(WBLP)** 은 알림 피로를 막지만 실패가 조용해지고, **「항상 보낸다」(두 번째)** 는 실행 여부가 메일함에서 바로 보인다. 앞쪽을 쓸 때는 실패를 다른 채널로 알려야 한다
- 루틴에 넣을 커넥터는 「무엇을 읽고 무엇을 쓰나」로 고른다 — 넣은 커넥터는 쓰기까지 묻지 않고 한다

### Tomorrow's focus
1. 9/28 08:12 WBLP 정기 실행 결과를 `list_runs` 로 확인 (환경 수정 후 첫 정기 실행)
2. M5 — 사용 패턴 가이드
3. M6 — Remotion 영상

## 참조 및 산출물

- 신규: [routines-basics](../04-Routines-Lab/concepts/routines-basics.md) · [local-vs-cloud](../04-Routines-Lab/concepts/local-vs-cloud.md) · [second-routine](../04-Routines-Lab/guides/second-routine.md) · [공식 문서 클리핑](../vl_materials/2026-09-27%20Routines%20공식%20문서%20클리핑.md)
- 수정: [04-Routines-Lab/README](../04-Routines-Lab/README.md) · 로드맵 진행표
- 루틴: https://claude.ai/code/routines/trig_01TyCwrfL1H3vsmdkmcDS8xk (Ran)
