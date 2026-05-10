---
title: "M4 Test Scenarios"
created: 2026-05-10 07:12:00
tags:
  - vibe-guiding
  - test-scenarios
  - m4
sources:
  - "[[Ingest/CatchUpAI_VL/Topics/Vibe-Guiding-VSCode/02-Architecture-Design/poc-boundary#M4 최소 시나리오|POC Boundary]]"
---

## 테스트 목적

M4 POC가 기본 3개 problem signal에 대해 적절한 trigger rule, manual entry, guide response를 생성하는지 확인한다. M5에서는 같은 runner를 확장해 Desktop/Applet context missing과 version mismatch 시나리오까지 함께 검증한다.

## 시나리오 목록

| id | problem signal | 기대 trigger | 기대 manual | 완료 기준 |
|---|---|---|---|---|
| `cli_missing` | `gobi` 명령을 찾을 수 없음 | `cli_missing` | `gobi-cli-install` | `npm install -g @gobi-ai/cli`, `gobi --version` 포함 |
| `auth_required` | 인증 상태가 logged out | `auth_required` | `gobi-cli-auth-status` | `gobi auth login`, `gobi auth status` 포함 |
| `space_post_blocked` | `create-thread` 사용 또는 Space Post 작성 막힘 | `old_thread_command_used` 또는 `space_post_blocked` | `gobi-cli-space-create-post` | `create-thread -> create-post` 변환과 `gobi space create-post` 포함 |
| `desktop_custom_homepage_blocked` | Desktop Applet 경로와 메뉴를 모름 | `desktop_applet_context_missing` | `gobi-desktop-applet-context-check` | 확인되지 않은 메뉴를 단정하지 않고 Desktop 버전, Vault Path, Applet 경로 확인을 먼저 제시 |
| `version_mismatch` | 매뉴얼 기준 버전과 사용자 환경이 다름 | `environment_version_mismatch` | `gobi-cli-environment-version-check` | `node --version`, `npm --version`, `gobi --version` 확인을 제품 단계보다 먼저 제시 |

## 수동 테스트 방법

1. `data/test_contexts.json`에서 하나의 scenario를 `data/user_context.sample.json` 형식으로 복사한다.
2. 다음 명령어를 순서대로 실행한다.

```powershell
python src/collect_context.py
python src/evaluate_trigger.py
python src/retrieve_manual.py
python src/compose_guide.py
```

3. `output/trigger_decision.json`, `output/retrieval_result.json`, `output/guide_response.md`를 확인한다.

## 품질 체크리스트

- [ ] guide response에 현재 상태 요약이 있다.
- [ ] 선택된 trigger rule과 판단 이유가 있다.
- [ ] 실행 단계가 있다.
- [ ] completion signal이 있다.
- [ ] fallback이 있다.
- [ ] source attribution이 있다.
- [ ] v2.0.12에서 실행하면 안 되는 구 명령어를 실행 단계로 제시하지 않는다.
