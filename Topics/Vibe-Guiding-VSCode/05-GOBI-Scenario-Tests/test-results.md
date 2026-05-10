---
title: "M5 Scenario Test Results"
created: 2026-05-10 07:22:45
tags:
  - vibe-guiding
  - test-results
  - gobi
sources:
  - "[[Ingest/CatchUpAI_VL/Topics/Vibe-Guiding-VSCode/04-Guiding-Engine-POC/tests/test_scenarios|M4 Test Scenarios]]"
  - "[[Ingest/CatchUpAI_VL/Topics/Vibe-Guiding-VSCode/05-GOBI-Scenario-Tests/guide-quality-checklist|Guide Quality Checklist]]"
---

## 실행 명령

M5 검증은 M4 POC의 자동 시나리오 runner로 수행했다.

```powershell
python tests/run_scenarios.py
```

실행 결과는 `Scenarios passed: 5/5`였다. 결과 JSON은 `04-Guiding-Engine-POC/output/test_results.json`에 저장되었고, 각 시나리오별 guide response는 `04-Guiding-Engine-POC/output/scenarios/<scenario_id>/guide_response.md`에 생성되었다.

## 자동 테스트 결과

| 시나리오 | 기대 manual | 실제 manual | 선택 rule | 결과 |
|---|---|---|---|---|
| `cli_missing` | `gobi-cli-install` | `gobi-cli-install` | `cli_missing` | 통과 |
| `auth_required` | `gobi-cli-auth-status` | `gobi-cli-auth-status` | `auth_required` | 통과 |
| `space_post_blocked` | `gobi-cli-space-create-post` | `gobi-cli-space-create-post` | `old_thread_command_used` | 통과 |
| `desktop_custom_homepage_blocked` | `gobi-desktop-applet-context-check` | `gobi-desktop-applet-context-check` | `desktop_applet_context_missing` | 통과 |
| `version_mismatch` | `gobi-cli-environment-version-check` | `gobi-cli-environment-version-check` | `environment_version_mismatch` | 통과 |

## Guide 품질 평가

| 시나리오 | 상태 요약 | Manual 적합성 | 실행 가능성 | 완료 신호 | Fallback | 평가 |
|---|---|---|---|---|---|---|
| CLI 미설치 | 통과 | 통과 | 통과 | 통과 | 통과 | 통과 |
| CLI 인증 필요 | 통과 | 통과 | 통과 | 통과 | 통과 | 통과 |
| Space/Post 막힘 | 통과 | 통과 | 통과 | 통과 | 통과 | 통과 |
| Desktop/Applet 막힘 | 통과 | 통과 | 통과 | 통과 | 통과 | 통과 |
| Version mismatch | 통과 | 통과 | 통과 | 통과 | 통과 | 통과 |

## 실패 원인 분류표

| 잠재 실패 | 1차 분류 | 수정 위치 |
|---|---|---|
| Desktop 버전, Vault Path, Applet 경로가 context에 없다. | context | `collect_context.py` 또는 Desktop 연동 collector |
| `desktop_custom_homepage_blocked`가 CLI fallback으로 간다. | trigger | `trigger_rules.json`의 match type, keyword, priority |
| `version_mismatch`인데 auth manual이 선택된다. | retrieval | `retrieval_index.json`의 problem signal, guide type, priority |
| 올바른 manual을 골랐지만 존재하지 않는 메뉴를 안내한다. | compose | `compose_guide.py`의 `desktop_applet` 단계와 fallback |
| v2.0.12 기준 변경 용어가 누락된다. | manual | retrieval entry의 `deprecated_terms`, `replacement_terms` |

## 결론

M5 기준에서 M4 POC는 CLI 인증, Space/Post 명령어 변경, Desktop/Applet 상태 확인, 환경 버전 불일치 상황을 모두 구분했다. 다음 모듈에서는 이 검증 결과를 바탕으로 실제 통합 후보와 데모 흐름을 선택하면 된다.
