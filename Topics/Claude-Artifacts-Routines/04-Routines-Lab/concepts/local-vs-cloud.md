---
title: "로컬 AI4PKM cron vs 클라우드 루틴 — 판단표"
created: 2026-09-27 16:10:00
author:
  - "Claude Code"
tags:
  - claude-artifacts-routines
  - m4
  - concepts
---

## 30초 기준

**볼트 파일을 읽거나 써야 하면 로컬, PC 가 꺼져 있어도 외부(웹 · 메일 · 캘린더)를 봐야 하면 클라우드.** 이 볼트는 GitHub 에 없으므로 클라우드 루틴은 볼트를 직접 읽지 못한다(공식 문서: 루틴은 선택한 GitHub 레포만 clone 한다). 둘 다 필요하면 **클라우드가 결과를 메일로 보내고, 로컬이 그 결과를 볼트에 옮기는** 식으로 나눈다.

## 축

| 축 | 로컬 AI4PKM cron (`orchestrator.yaml`) | 클라우드 루틴 |
|---|---|---|
| 볼트 파일 읽기 · 쓰기 | ✅ 직접 | ❌ (GitHub 레포에 있는 것만. 공개 레포 CatchUpAI_VL 은 가능) |
| PC 가 꺼져 있을 때 | ❌ 안 돈다 | ✅ 돈다 |
| 외부 웹 | ✅ PC 네트워크 그대로 | ⚠️ 환경 허용 목록 안에서만 (`Default` = Trusted) |
| 메일 · 캘린더 | 로컬 MCP 설정에 따라 | ✅ claude.ai 커넥터 (허용 목록과 무관) |
| 비용 | 로컬 에이전트 실행 비용 | 구독 사용량 + 하루 실행 한도 (일회성은 한도 밖) |
| 실패했을 때 보는 곳 | 로컬 로그 (`_Settings_/Logs/`) | 실행 세션 기록 (`list_runs` · `get_run_log`) — 초록색이 성공을 뜻하지 않는다 |
| 최소 간격 | 제한 없음 | 1시간 |

## 실물을 놓고

| 작업 | 어디 | 이유 한 줄 |
|---|---|---|
| **GDR** Daily Roundup (매일 04:00) | 로컬 | 볼트의 하루 파일을 모두 읽고 Roundup · Task Board 를 **쓴다** |
| **TIU** Topic Index Update (매일 04:30) | 로컬 | 볼트의 Topic 인덱스를 **고친다** |
| **WBLP** AWS 공고 주간 확인 (월 08:00) | 클라우드 | 볼트가 필요 없고, 외부 사이트 확인 + 조건부 메일. PC 가 꺼져 있어도 돌아야 한다 |
| **두 번째 루틴** (실습 2) | 클라우드 | → [second-routine](../guides/second-routine.md) |
| (참고) Personal Ops Board **Deadline** 에이전트 | 로컬 | `items/` 를 읽어 `views/warnings.md` 를 **쓴다** — POB 는 로컬 AI4PKM 노드로 가는 것이 맞다 (POB 결정 003 과 같은 결론) |

## 이 표가 POB 에 주는 것

POB 에이전트 넷(Board · Deadline · Intake · Discovery)은 모두 볼트를 읽고 쓰므로 **로컬**이다. 다만 「PC 가 꺼져 있던 날 아침에도 마감 경고를 받고 싶다」가 요구로 나오면, 로컬이 만든 `warnings.md` 를 공개하지 않는 채로 클라우드가 읽을 방법이 없으므로 **메일 발송만 클라우드로 나누는** 설계를 검토한다 — 그때 POB 결정 기록으로 남긴다.


English companion: [local-vs-cloud_en](local-vs-cloud_en.md)
