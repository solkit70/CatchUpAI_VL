---
title: "Routines 기본 — 트리거 · 환경 · 알림 · 비용"
created: 2026-09-27 16:00:00
author:
  - "Claude Code"
tags:
  - claude-artifacts-routines
  - m4
  - concepts
---

## 한 줄

**루틴은 내 PC 가 꺼져 있어도 클라우드에서 도는 Claude Code 세션이다. 그 세션이 무엇에 닿을 수 있는지는 레포 · 환경의 네트워크 · 커넥터 세 가지로 정해진다.** 근거는 [공식 문서 클리핑](../../vl_materials/2026-09-27%20Routines%20공식%20문서%20클리핑.md)(2026-09-27, research preview).

## 다섯 가지

| 항목 | 내용 | 우리 실물에서 |
|---|---|---|
| **트리거** | 일정(반복 · 일회성) · API · GitHub 이벤트. 반복은 최소 1시간 간격, 정각은 몇 분 늦을 수 있어 「9:07」처럼 잡으라고 권함. 일회성은 한 번 돌고 꺼진다(**Ran**) | WBLP: 매주 월 15:00 UTC(08:00 PDT) — 실제로는 15:07 전후 시작 |
| **닿는 곳 ① 레포** | 매 실행마다 GitHub 레포를 새로 clone. 변경은 `claude/` 브랜치로 | WBLP 는 레포 없음. **볼트는 GitHub 에 없으므로 루틴이 볼트를 직접 못 읽는다** (공개 레포 CatchUpAI_VL 은 가능) |
| **닿는 곳 ② 환경 네트워크** | `Default` 환경 = **Trusted**: 패키지 저장소 · 클라우드 API 등 허용 목록만. 밖은 `403 host_not_allowed` | 9/21 WBLP 3주 실패의 원인. amazon.jobs 를 허용 목록에 넣어 복구 |
| **닿는 곳 ③ 커넥터** | claude.ai 에 연결한 커넥터만 (Gmail · Google Calendar · Claude Docs). 네트워크 허용 목록과 **무관하게** Anthropic 서버를 거쳐 닿는다. **기본으로 전부 포함되고 쓰기도 묻지 않고 한다** → 필요한 것만 남긴다. 로컬 `claude mcp add` 서버는 못 쓴다 | WBLP: Gmail 하나만 연결 |
| **알림 · 관측** | 결과는 실행마다 새 세션으로 남는다. **초록색 상태 = 인프라 오류 없음일 뿐, 할 일이 성공했다는 뜻이 아니다** — 기록을 열어 봐야 한다 | WBLP 3주 실패도 매번 「정상 종료」였다. 세션 안에서 `list_runs` · `get_run_log` 로 읽을 수 있다 |
| **비용 · 한도** | 대화형 세션과 같이 구독 사용량을 쓴다 + 계정별 하루 실행 횟수 한도. **일회성 실행은 하루 한도에 안 들어간다** | 주 1회라 부담 없음 |

## 헷갈리기 쉬운 것

- 루틴이 실행하는 프롬프트는 **미리 저장된 할 일**로 취급되어 그대로 수행된다. 반면 API 로 넘긴 `text` 는 「믿을 수 없는 데이터」로 포장되어 온다 — 프롬프트가 그 내용을 처리하라고 명시해야 쓴다
- 루틴이 하는 일(메일 발송, 커밋)은 **내 이름으로** 나간다
- 로컬에서 되던 것이 클라우드에서 안 되면 첫 의심은 **환경의 네트워크**다 → [troubleshooting](../troubleshooting/routine-did-not-run.md)


English companion: [routines-basics_en](routines-basics_en.md)
