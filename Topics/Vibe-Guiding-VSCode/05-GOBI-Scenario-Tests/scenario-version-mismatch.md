---
title: "Scenario - Version and Environment Mismatch"
created: 2026-05-10 07:22:45
tags:
  - vibe-guiding
  - environment-check
  - version-mismatch
  - scenario-test
sources:
  - "[[Ingest/CatchUpAI_VL/Topics/GOBI-CLI/01-Setup-Auth/concepts/installation-guide#사전 요구사항|GOBI CLI 설치 & 인증 가이드]]"
  - "[[Ingest/CatchUpAI_VL/Topics/GOBI-CLI/04-Capstone/guides/quick-reference#Space 명령어 (구 Thread → Post)|GOBI CLI Quick Reference]]"
---

## 시나리오 목적

이 시나리오는 사용자의 Node, npm, GOBI CLI 버전이 매뉴얼 기준과 다를 때 guide가 먼저 환경을 확인하는지 검증한다. 사용자가 `gobi 0.6.15`와 Node 16 환경에 있는데 v2.0.12 기준 명령어를 바로 안내하면 실패 가능성이 높으므로, 제품 작업보다 버전 확인과 업데이트 판단이 먼저 나와야 한다.

> Node.js | 18+ | `node --version`

이 기준은 version mismatch 시나리오의 최소 환경 확인 항목이다. guide가 Node 18+ 요구사항을 확인하지 않고 GOBI CLI 명령어만 안내하면 환경 차이를 놓친 것이다.

## 입력 context

| 항목 | 값 |
|---|---|
| OS | Windows 11 |
| 사용자 수준 | beginner |
| GOBI CLI 버전 | `0.6.15` |
| Node 버전 | `16.20.0` |
| npm 버전 | `8.19.4` |
| 매뉴얼 기준 | GOBI CLI `2.0.12`, Node `18+` |
| problem signal | `version_mismatch` |

## 기대 guide

`environment_version_mismatch` rule과 `gobi-cli-environment-version-check` manual이 선택되어야 한다. guide는 `node --version`, `npm --version`, `gobi --version` 확인을 먼저 요구하고, GOBI CLI가 2.0.12 미만이면 업데이트 전에는 v2 전용 명령어를 단정하지 않아야 한다.

## 검증 결과

| 입력 | 선택 rule | 선택 manual | 평가 |
|---|---|---|---|
| `version_mismatch` | `environment_version_mismatch` | `gobi-cli-environment-version-check` | 통과 |

생성된 guide는 버전 확인을 첫 단계에 두었고, `gobi init` → `gobi vault init`, `BRAIN.md` → `PUBLISH.md`, `thread` → `post` 변환을 함께 보여줬다. 이 결과는 환경 mismatch 상황에서 최신 매뉴얼을 무조건 적용하지 않고 확인 우선으로 전환한다는 점에서 통과로 판단했다.

## 실패 시 수정 위치

버전 정보가 context에 들어오지 않으면 collector를 수정한다. `version_mismatch`가 Space/Post나 auth rule로 잘못 분류되면 trigger priority를 조정한다. 환경 확인 manual이 선택됐는데도 guide가 바로 제품 작업을 지시하면 compose 단계의 guide type별 실행 단계를 수정한다.
