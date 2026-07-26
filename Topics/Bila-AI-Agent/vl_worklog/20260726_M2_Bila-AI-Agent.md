---
title: M2 WorkLog - 2026-07-26
module: M2 - 데이터 소스 연결 & Phase 1 구현
session: 3
date: 2026-07-26
tags:
  - bila-ai-agent
  - m2
  - worklog
---

## 세션 정보

| 항목 | 내용 |
|------|------|
| 날짜 | 2026-07-26 (일) |
| 상황 | Google Drive 연결 버그 fix 이후 재개 |
| 모듈 | M2 - 데이터 소스 연결 & Phase 1 구현 |
| 참조 로드맵 | [[Ingest/CatchUpAI_VL/Topics/Bila-AI-Agent/vl_roadmap/20260628_RoadMap_Bila-AI-Agent]] |
| 이전 세션 | [[Ingest/CatchUpAI_VL/Topics/Bila-AI-Agent/vl_worklog/20260705_M2_Bila-AI-Agent]] |

## 오늘의 목표

- [x] 이전 M2 상태 확인: GitHub 연결과 시스템 프롬프트 정리는 완료, Google Drive 폴더 저장 버그가 블로커였음.
- [x] 사용자 입력 반영: Google Drive 연결 버그가 수정됐다는 최신 상태를 세션 전제로 채택.
- [x] post-fix Drive 재검증 절차 문서화.
- [x] Drive 포함 system prompt v2.2 적용본을 산출물 폴더에 분리 저장.
- [x] Phase 1 최종 10문항 테스트 시트 작성.
- [x] Slack 연결 시작 화면부터 이메일 코드 입력 대기 화면까지의 과정을 문서화.
- [ ] GobiSpace 웹 UI에서 Drive 폴더 재연결 및 persistence 확인.
- [ ] Slack 이메일 코드 입력 후 Gobi Slack app 설치/승인 → 블로킹: 이메일 코드 미수신.
- [ ] Gobi bot을 Builders Lounge public Slack 채널에 초대.
- [ ] Bila에게 marker 질문을 실행해 `DRIVE-TEST-7749` 응답 확인.
- [ ] Phase 1 최종 10문항 테스트 실행 및 점수 기록.

## 현재 학습 상태

M2는 6개 DoD 중 3개가 이미 완료된 상태다. GitHub 레포 연결, GitHub 기반 응답 확인, 시스템 프롬프트 v2.2 정리는 이전 세션에서 완료됐고, 남은 핵심 블로커는 Google Drive 폴더 선택이 저장되지 않는 UI/백엔드 상태 문제였다. 사용자가 2026-07-26에 "Google Drive 연결 버그는 fix됐다"고 알려줬으므로, 오늘의 실습 범위는 버그 분석이 아니라 fix 이후 재검증으로 전환한다.

## 진행 내용

### 실습2 재개: Google Drive 연결 post-fix 검증 준비

Drive 연결 검증은 동일한 marker 테스트를 재사용한다. 테스트 폴더는 `My Drive / 2025 Vibe Coding Bootcamp`, 테스트 파일은 [[Ingest/CatchUpAI_VL/Topics/Bila-AI-Agent/vl_materials/drive-test-marker|drive-test-marker]], 기대 정답은 `DRIVE-TEST-7749`다. 이전 실패는 Drive 전용 `Glob "/gdrive/2025 Vibe Coding Bootcamp/**/*"` 호출은 있었지만 파일이 0건으로 반환된 케이스였으므로, 이번에는 "폴더 선택이 UI에 유지되는지"와 "Bila가 실제 파일을 찾는지"를 분리해서 기록해야 한다.

산출물: [[Ingest/CatchUpAI_VL/Topics/Bila-AI-Agent/02-DataSource-Phase1/guides/google-drive-connection-guide|Google Drive Connection Guide]]

### Prompt iteration 정리

이전 WorkLog에는 v2.2 적용 내용이 기록돼 있었지만, M2 산출물 폴더의 `prompt-iterations/`에는 독립 파일이 없었다. Google Drive fix 이후에는 시스템 프롬프트가 GitHub와 Drive를 모두 데이터 소스로 명시해야 하므로, GobiSpace 입력용 v2.2 prompt를 별도 산출물로 정리했다.

산출물: [[Ingest/CatchUpAI_VL/Topics/Bila-AI-Agent/02-DataSource-Phase1/prompt-iterations/prompt_v2_2_after_drive_fix|System Prompt v2.2 after Drive fix]]

### Phase 1 최종 테스트 준비

최종 테스트는 10문항 중 7문항 이상이 2점 이상이면 통과로 둔다. 첫 문항은 Drive marker 검증으로 고정하고, 나머지는 GitHub, Space posts, Drive 회의록을 골고루 확인하도록 구성했다. 실제 Bila 응답은 아직 실행하지 않았으므로 모든 Result는 Pending으로 남겼다.

산출물: [[Ingest/CatchUpAI_VL/Topics/Bila-AI-Agent/02-DataSource-Phase1/test-results/qa-test-phase1-final|Phase 1 Final Q&A Test]]

### Slack 연결 과정 기록

사용자 제공 스크린샷 기준으로 GobiSpace `Settings -> Agents -> Slack` 섹션에는 `No Slack workspace connected` 상태가 표시됐다. 설명 문구는 Slack workspace를 연결하면 agent가 초대된 public channel 메시지를 읽을 수 있고, read-only라 Slack에 직접 post하지 못한다고 안내한다. `Connect Slack`을 누르면 Slack의 `Sign in to your workspace` 화면으로 이동하며, 여기서 workspace URL을 입력해야 한다.

Slack 앱의 workspace 메뉴에서 Changbal workspace URL은 `changbal.slack.com`으로 확인됐다. 입력 중 `changbal.slack.com.slack.com`처럼 중복 suffix가 생긴 화면도 있었으므로, 실제 제출 전에는 `changbal.slack.com`만 남기는 것이 안전하다. 다음 화면에서는 Slack이 `douggy.park@yahoo.com`으로 이메일 코드를 보냈다고 표시했고, 6자리 코드를 입력하라는 상태에서 사용자가 중단했다.

산출물: [[Ingest/CatchUpAI_VL/Topics/Bila-AI-Agent/02-DataSource-Phase1/guides/slack-connection-guide|Slack Connection Guide]]

### Slack 이메일 코드 미수신

사용자가 `douggy.park@yahoo.com`으로 Slack 인증 코드가 도착하지 않는다고 보고했다. 이 문제는 Gobi Slack app 설치 전 단계의 인증 블로커이므로, 우선 Slack 자체 이메일 delivery와 workspace URL 입력 상태를 확인한다. `Request a new code`는 한 번만 재시도하고, `changbal.slack.com.slack.com`처럼 잘못된 workspace URL로 요청한 기록이 있으면 `Try entering a workspace URL`로 돌아가 `changbal.slack.com`만 입력해 다시 진행한다.

추가 대응은 [[Ingest/CatchUpAI_VL/Topics/Bila-AI-Agent/02-DataSource-Phase1/guides/slack-connection-guide#Email Code Not Arriving - Triage|Slack email code triage]]에 정리했다.

### Slack authorization error: invalid_team_for_non_distributed_app

이후 사용자가 이메일 코드를 입력하자 Slack authorization 단계에서 `invalid_team_for_non_distributed_app` 에러가 발생했다. Slack OAuth 문서 기준 이 에러는 distributed 설정이 되지 않은 Slack API app을 app이 생성된 workspace가 아닌 다른 workspace에 설치/승인하려고 할 때 발생한다. 따라서 사용자의 PIN 입력 실패라기보다, Gobi Slack app이 Changbal workspace에 설치 가능한 distribution 상태가 아니거나 workspace-specific install 설정이 누락된 것으로 보는 것이 타당하다.

이 이슈는 Changbal admin이 UI에서 해결할 수 있는 범위를 넘어설 가능성이 높다. GOBI 개발자에게 Gobi Slack app distribution 설정 또는 Changbal workspace 대상 설치 가능 여부를 확인 요청해야 한다.

상세 리포트 초안은 [[Ingest/CatchUpAI_VL/Topics/Bila-AI-Agent/02-DataSource-Phase1/guides/slack-connection-guide#Authorization Error - invalid_team_for_non_distributed_app|Slack authorization error]]에 정리했다.

## DoD 체크리스트

- [x] GitHub 레포 연결 완료 + 기록 참조 답변 확인.
- [x] 시스템 프롬프트 v2.2 정리.
- [ ] Google Drive 회의록 폴더 연결 완료.
- [ ] Slack workspace 연결 완료 → 블로킹: `invalid_team_for_non_distributed_app`.
- [ ] Gobi bot을 필요한 Builders Lounge public Slack 채널에 초대.
- [ ] Phase 1 최종 테스트: 10개 질문 중 7개 이상 적절한 답변.
- [ ] 데이터 연결 전후 비교 문서 작성.
- [ ] Daily Retrospective 완료.

## Daily Retrospective

### What went well?

이전 세션의 블로커와 오늘의 사용자 업데이트를 연결해 M2의 다음 실험 범위를 명확히 좁혔다. 특히 Drive 문제를 "폴더 선택 persistence"와 "retrieval/indexing"으로 분리해, fix 이후에도 실패할 경우 어느 계층 문제인지 빠르게 판별할 수 있게 했다.

### What could be improved?

GobiSpace Agents 설정은 현재 웹 UI 전용이라 이 세션에서 직접 Drive attach를 완료하지 못했다. 다음 실행 때는 사용자가 웹 UI에서 폴더 persistence와 marker 질문 결과를 확인한 뒤, 그 원문 응답과 tool call을 그대로 테스트 시트에 기록해야 한다.

### Insights

M2의 핵심 학습은 단순 연결 성공이 아니라 "연결 UI, 시스템 프롬프트, retrieval tool call, 실제 답변"이 모두 같은 상태를 가리키는지 검증하는 것이다. Google Drive fix가 실제로 완료됐다면 이번 marker 테스트는 M2를 막고 있던 가장 큰 리스크를 닫고, 바로 Phase 1 최종 10문항 테스트로 넘어갈 수 있다.

### Tomorrow's Focus

GobiSpace 웹 UI에서 Google Drive 폴더를 다시 선택하고, Agents 탭 재진입 후에도 연결 상태가 유지되는지 확인한다. Slack은 먼저 이메일 코드 미수신 문제를 해결한 뒤 Gobi Slack app 승인까지 진행하고, 필요한 public channel에 Gobi bot을 초대한다. 두 데이터 소스 연결이 확인되면 Bila에게 Drive marker 질문과 Slack-only 질문을 각각 던진 뒤, 성공하면 [[Ingest/CatchUpAI_VL/Topics/Bila-AI-Agent/02-DataSource-Phase1/test-results/qa-test-phase1-final|Phase 1 Final Q&A Test]]의 10문항을 순서대로 실행한다.

## 참고 및 산출물

- M2 module README: [[Ingest/CatchUpAI_VL/Topics/Bila-AI-Agent/02-DataSource-Phase1/README]]
- Drive 재검증 가이드: [[Ingest/CatchUpAI_VL/Topics/Bila-AI-Agent/02-DataSource-Phase1/guides/google-drive-connection-guide]]
- Slack 연결 가이드: [[Ingest/CatchUpAI_VL/Topics/Bila-AI-Agent/02-DataSource-Phase1/guides/slack-connection-guide]]
- Prompt v2.2: [[Ingest/CatchUpAI_VL/Topics/Bila-AI-Agent/02-DataSource-Phase1/prompt-iterations/prompt_v2_2_after_drive_fix]]
- Phase 1 최종 테스트 시트: [[Ingest/CatchUpAI_VL/Topics/Bila-AI-Agent/02-DataSource-Phase1/test-results/qa-test-phase1-final]]
