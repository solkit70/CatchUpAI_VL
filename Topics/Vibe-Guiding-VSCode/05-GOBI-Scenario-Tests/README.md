---
title: "M5 - GOBI 시나리오 검증"
created: 2026-05-10 07:22:45
tags:
  - vibe-guiding
  - vibelearn-ai
  - scenario-test
  - gobi
sources:
  - "[[Ingest/CatchUpAI_VL/Topics/Vibe-Guiding-VSCode/vl_roadmap/20260426_RoadMap_Vibe-Guiding-VSCode#M5 - GOBI 시나리오 검증|M5 Roadmap]]"
  - "[[Ingest/CatchUpAI_VL/Topics/Vibe-Guiding-VSCode/04-Guiding-Engine-POC/README|M4 Guiding Engine POC]]"
---

## 모듈 개요

M5는 M4에서 만든 파일 기반 Guiding Engine POC를 실제 GOBI 사용 상황에 가까운 시나리오로 검증하는 모듈이다. 핵심은 "어떤 매뉴얼을 골랐는가"만 보는 것이 아니라, 안내가 사용자의 현재 상태를 확인하고, 확인되지 않은 정보를 단정하지 않으며, 실패했을 때 어느 컴포넌트를 고쳐야 하는지 분류할 수 있는지 확인하는 것이다.

## 학습 순서

| 순서 | 문서 | 목적 |
|---|---|---|
| 1 | [guide-quality-checklist.md](guide-quality-checklist.md) | guide response 품질을 평가하는 공통 기준을 정의한다. |
| 2 | [scenario-gobi-cli-auth.md](scenario-gobi-cli-auth.md) | GOBI CLI 설치, 인증, Space/Post 막힘을 하나의 CLI 검증 흐름으로 정리한다. |
| 3 | [scenario-gobi-desktop-custom-homepage.md](scenario-gobi-desktop-custom-homepage.md) | GOBI Desktop Custom Homepage/Applet 안내에서 상태 확인이 왜 먼저 필요한지 검증한다. |
| 4 | [scenario-version-mismatch.md](scenario-version-mismatch.md) | 사용자 환경과 매뉴얼 기준 버전이 다를 때 확인 우선 안내가 나오는지 검증한다. |
| 5 | [test-results.md](test-results.md) | M4 POC 자동 테스트 결과와 실패 원인 분류표를 정리한다. |

## 실행 결과 요약

`04-Guiding-Engine-POC/tests/run_scenarios.py`를 실행해 5개 시나리오를 검증했다. 기존 M4의 3개 시나리오에 M5에서 필요한 Desktop/Applet context missing과 version mismatch 시나리오를 추가했고, 모든 시나리오가 기대 manual을 선택했다.

| 시나리오 | 선택 rule | 선택 manual | 결과 |
|---|---|---|---|
| `cli_missing` | `cli_missing` | `gobi-cli-install` | 통과 |
| `auth_required` | `auth_required` | `gobi-cli-auth-status` | 통과 |
| `space_post_blocked` | `old_thread_command_used` | `gobi-cli-space-create-post` | 통과 |
| `desktop_custom_homepage_blocked` | `desktop_applet_context_missing` | `gobi-desktop-applet-context-check` | 통과 |
| `version_mismatch` | `environment_version_mismatch` | `gobi-cli-environment-version-check` | 통과 |

## 이전/다음 모듈

- 이전 모듈: [../04-Guiding-Engine-POC/README.md](../04-Guiding-Engine-POC/README.md)
- 다음 모듈: `../06-Integration-Demo/README.md` 예정
