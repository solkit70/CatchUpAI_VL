---
title: "Scenario - GOBI CLI Auth and Space Post"
created: 2026-05-10 07:22:45
tags:
  - vibe-guiding
  - gobi-cli
  - scenario-test
sources:
  - "[[Ingest/CatchUpAI_VL/Topics/GOBI-CLI/01-Setup-Auth/concepts/installation-guide#Step 2: 인증 (device-code flow)|GOBI CLI 설치 & 인증 가이드]]"
  - "[[Ingest/CatchUpAI_VL/Topics/GOBI-CLI/03-Space-Thread/guides/thread-management#v2.0 명령어 변환 빠른 참조|Post & Reply 관리 가이드]]"
---

## 시나리오 목적

이 시나리오는 GOBI CLI 사용자가 설치, 인증, Space/Post 작업에서 막히는 상황을 검증한다. M4 POC에서는 `cli_missing`, `auth_required`, `space_post_blocked` 세 입력으로 나누어 실행했고, M5에서는 세 결과를 하나의 CLI 사용 흐름으로 묶어 품질을 평가한다.

> **v2.0 변경**: 구 Google OAuth 브라우저 팝업 → **device-code flow**

이 문장은 인증 안내에서 반드시 반영되어야 하는 최신성 기준이다. 사용자가 로그인에 막힌 경우 예전 OAuth 팝업을 안내하면 안 되고, `gobi auth login`이 출력하는 URL과 user code를 완료하도록 안내해야 한다.

## 입력 context

| 항목 | 값 |
|---|---|
| OS | Windows 11 |
| 사용자 수준 | beginner 또는 intermediate |
| GOBI CLI 버전 | 없음, 또는 `2.0.12` |
| 인증 상태 | `unknown`, `logged_out`, `authenticated` |
| 주요 problem signal | `cli_missing`, `auth_required`, `space_post_blocked` |

## 기대 guide

CLI 미설치 상황에서는 `gobi-cli-install` manual이 선택되어야 한다. 안내에는 전역 설치 명령, 새 터미널 열기, `gobi --version` 확인이 포함되어야 한다.

인증 필요 상황에서는 `gobi-cli-auth-status` manual이 선택되어야 한다. 안내에는 `gobi auth login`, device-code flow 완료, `gobi auth status` 확인이 포함되어야 한다.

Space/Post 막힘 상황에서는 `gobi-cli-space-create-post` manual이 선택되어야 한다. 안내에는 `create-thread`가 `create-post`로 바뀌었다는 변환, `gobi space list`, `gobi space create-post`, `gobi space get-post` 확인이 포함되어야 한다.

## 검증 결과

| 입력 | 선택 rule | 선택 manual | 평가 |
|---|---|---|---|
| `cli_missing` | `cli_missing` | `gobi-cli-install` | 통과 |
| `auth_required` | `auth_required` | `gobi-cli-auth-status` | 통과 |
| `space_post_blocked` | `old_thread_command_used` | `gobi-cli-space-create-post` | 통과 |

## 실패 시 수정 위치

`gobi --version`이나 `gobi auth status` 같은 확인 명령이 빠지면 compose를 수정한다. `create-thread` 표현이 Post manual로 연결되지 않으면 trigger 또는 retrieval을 수정한다. v2.0.12 용어가 아닌 `BRAIN.md`, `thread`, `gobi init`이 guide에 그대로 나오면 manual metadata를 먼저 고친다.
