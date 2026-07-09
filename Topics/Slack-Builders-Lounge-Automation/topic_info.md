---
title: "Slack Builders Lounge Automation"
created: 2026-07-05 23:21:11
tags:
  - vibelearn-ai
  - slack
  - builders-lounge
  - automation
  - markdown
---

## Topic Overview

Slack Builders Lounge Automation은 `changbal.slack.com`의 `#club-sg-ai` 채널에 올라오는 Builders Lounge 관련 대화를 자동으로 가져와 `AI/Initiatives/Builders Lounge/slack/` 아래의 Markdown 문서로 정리하는 방법을 연구하고 구현하는 VibeLearn AI Topic입니다. 현재는 Slack 글을 수동으로 가져와 날짜별 문서로 정리하고 있으므로, 이 Topic의 핵심은 Slack API 접근, 메시지/스레드/작성자/링크 보존, Markdown 변환, 공개 GitHub 공유 전 검토 흐름을 하나의 반복 가능한 자동화로 만드는 것입니다.

## Learning Purpose

이번 Topic의 목적은 Slack API와 OAuth scope, channel history pagination, thread retrieval, user mapping, permalink generation, secret management를 AI에게 정확히 지시할 수 있을 정도로 이해하는 것입니다. 동시에 실제 자동화 스크립트를 개발하여 [[Initiatives/Builders Lounge/slack/2026-06-23 Builders Lounge 창발 발표 커피챗 확정 Build with AI 공유 Slack|기존 수동 정리 문서]]와 호환되는 Markdown 산출물을 만들고, GitHub에 공유하기 전에 개인정보와 비공개 맥락을 점검할 수 있는 운영 절차를 포함합니다.

## Target Outputs

| Output | Purpose | Location |
|---|---|---|
| Slack API Research Brief | Slack API 접근 방식, scope, rate limit, export 대안, 보안 조건 정리 | `01-Research-Brief/` |
| Markdown Schema | 기존 Builders Lounge Slack 문서와 호환되는 출력 형식 정의 | `02-Markdown-Schema/` |
| API Prototype | `conversations.history`, thread, user, permalink 수집 검증 | `03-API-Prototype/` |
| Sync Automation | 증분 수집, 상태 저장, Markdown 생성 스크립트 구현 | `04-Sync-Automation/` |
| Review & Publish Flow | 공개 공유 전 검토, redaction, GitHub 반영 기준 정리 | `05-Review-Publish-Flow/` |
| WorkLog | VibeLearn AI 학습 및 개발 진행 기록 | `vl_worklog/` |

## Source Materials

- [[Initiatives/Builders Lounge/README|Builders Lounge README]]
- [[Initiatives/Builders Lounge/slack/2026-03-25 Builders Lounge 초기 논의 Slack|Builders Lounge 초기 논의 Slack]]
- [[Initiatives/Builders Lounge/slack/2026-06-23 Builders Lounge 창발 발표 커피챗 확정 Build with AI 공유 Slack|최근 Builders Lounge Slack 정리 예시]]
- Slack API `conversations.history`: https://docs.slack.dev/reference/methods/conversations.history/
- Slack API `conversations.replies`: https://docs.slack.dev/reference/methods/conversations.replies/
- Slack API scopes: https://docs.slack.dev/reference/scopes/
- Slack workspace export guide: https://slack.com/help/articles/201658943-Export-your-workspace-data

## Learning Constraints

이 Topic은 실제 Slack 워크스페이스의 비공개 대화를 다룰 수 있으므로 토큰, 사용자 이메일, 비공개 파일 URL, 초대 링크 같은 민감 정보는 문서와 GitHub에 남기지 않습니다. 자동화 산출물은 `#club-sg-ai`의 Builders Lounge 공개 공유 가능 범위 안에서만 사용하며, GitHub에 올라갈 문서는 수집 직후 바로 공개하지 않고 검토 단계 또는 redaction 단계를 거치도록 설계합니다.
