---
title: "WorkLog - M5: GOBI 시나리오 검증"
created: 2026-05-10 07:22:45
tags:
  - vibe-guiding
  - vibelearn-ai
  - worklog
  - m5
sources:
  - "[[Ingest/CatchUpAI_VL/Topics/Vibe-Guiding-VSCode/vl_roadmap/20260426_RoadMap_Vibe-Guiding-VSCode#M5 - GOBI 시나리오 검증|M5 Roadmap]]"
  - "[[Ingest/CatchUpAI_VL/Topics/Vibe-Guiding-VSCode/04-Guiding-Engine-POC/README|M4 Guiding Engine POC]]"
---

## 오늘의 학습 목표

- [x] `05-GOBI-Scenario-Tests/` 폴더 생성
- [x] guide quality checklist 작성
- [x] GOBI CLI auth / Space Post 시나리오 작성 및 검증
- [x] GOBI Desktop Custom Homepage/Applet 시나리오 작성 및 검증
- [x] Version/Environment mismatch 시나리오 작성 및 검증
- [x] 실패 원인을 context, trigger, retrieval, manual, compose로 분류하는 표 작성

## 진행 내용

### 1. M5 범위 확인

Roadmap과 M4 WorkLog를 읽고 M5의 핵심이 "새 엔진 개발"이 아니라 "실제 GOBI 사용 문제를 테스트 시나리오로 변환하고 guide response 품질을 평가하는 것"임을 확인했다. M4 POC가 이미 rule, retrieval, compose 경계를 갖고 있었기 때문에 M5는 같은 runner를 확장하는 방식으로 진행했다.

### 2. M4 POC 시나리오 확장

`data/test_contexts.json`에 `desktop_custom_homepage_blocked`와 `version_mismatch`를 추가했다. 이에 맞춰 `trigger_rules.json`, `retrieval_index.json`, `compose_guide.py`, `tests/run_scenarios.py`를 업데이트해 Desktop/Applet context check와 environment version check manual을 선택할 수 있게 했다.

### 3. 자동 테스트 실행

`python tests/run_scenarios.py`를 실행했고 5개 시나리오가 모두 통과했다. 결과는 `04-Guiding-Engine-POC/output/test_results.json`과 각 시나리오별 `output/scenarios/<id>/guide_response.md`에 저장됐다.

| 시나리오 | 선택 rule | 선택 manual | 결과 |
|---|---|---|---|
| `cli_missing` | `cli_missing` | `gobi-cli-install` | 통과 |
| `auth_required` | `auth_required` | `gobi-cli-auth-status` | 통과 |
| `space_post_blocked` | `old_thread_command_used` | `gobi-cli-space-create-post` | 통과 |
| `desktop_custom_homepage_blocked` | `desktop_applet_context_missing` | `gobi-desktop-applet-context-check` | 통과 |
| `version_mismatch` | `environment_version_mismatch` | `gobi-cli-environment-version-check` | 통과 |

### 4. M5 산출물 문서화

`05-GOBI-Scenario-Tests/`에 README, guide quality checklist, 세 시나리오 문서, test results를 작성했다. 각 문서는 입력 context, 기대 guide, 검증 결과, 실패 시 수정 위치를 포함하도록 구성했다.

## 문제 해결 로그

### 문제: Desktop/Applet은 CLI 명령어만으로 검증되지 않음

**증상**: M4 POC는 GOBI CLI 중심으로 만들어져 있었기 때문에 Desktop Custom Homepage/Applet 막힘을 기존 manual로 표현하기 어려웠다.

**해결**: Desktop 안내를 제품 절차가 아니라 상태 확인 guide로 정의했다. `gobi-desktop-applet-context-check` manual은 확인되지 않은 메뉴명을 단정하지 않고 Desktop 버전, Vault Path, Applet 경로, 실제 Settings 메뉴를 먼저 확인하게 한다.

### 문제: Version mismatch는 기존 auth/space rule과 겹칠 수 있음

**증상**: 구 CLI 버전 사용자는 auth나 space 문제도 함께 겪을 수 있으므로, 곧바로 auth 또는 space manual을 선택하면 환경 차이를 놓칠 수 있다.

**해결**: `environment_version_mismatch` rule을 추가하고 `gobi-cli-environment-version-check` manual을 별도 guide type으로 분리했다. compose 단계에서는 `node --version`, `npm --version`, `gobi --version`을 제품 작업보다 먼저 실행하도록 했다.

## DoD 체크리스트

- [x] GOBI Desktop 시나리오 작성 및 테스트
- [x] GOBI CLI 시나리오 작성 및 테스트
- [x] Version/Environment Mismatch 시나리오 작성 및 테스트
- [x] Guide Quality Checklist 작성
- [x] 실패 원인 분류표 작성
- [x] `05-GOBI-Scenario-Tests/README.md` 작성
- [x] WorkLog 작성 및 Daily Retrospective 완료

**완료율**: 7/7 (100%)

## Daily Retrospective

### What went well

M4에서 파일 기반으로 context, trigger, retrieval, compose를 분리해 둔 덕분에 M5 시나리오 확장이 단순했다. 특히 Desktop/Applet처럼 실제 통합이 아직 없는 대상도 "확인 우선 guide"로 모델링하니 무리하게 제품 절차를 지어내지 않는 테스트가 가능했다.

### What could be improved

현재 품질 평가는 대부분 문서와 사람이 읽는 checklist에 의존한다. 다음 단계에서는 guide response에 포함되어야 하는 필수 문구나 금지 문구를 자동 검사하는 작은 validator를 추가하면 회귀 테스트 품질이 더 좋아진다.

### Insights

Vibe Guiding의 테스트는 "정답 안내문"을 맞히는 방식보다 "어느 단계에서 판단했는지 추적 가능한가"가 더 중요하다. context가 부족하면 물어보고, 버전이 다르면 확인하고, manual이 오래됐으면 변환 규칙을 적용하는 구조가 있어야 실제 사용자 막힘을 줄일 수 있다.

### Tomorrow's focus

- M6 시작: `06-Integration-Demo/` 생성
- 통합 후보 비교: VS Code CLI, VS Code Extension, GOBI Desktop Applet, GOBI CLI command, docs companion
- 5분 demo flow 작성
- MVP backlog와 GOBI 팀 협업 노트 작성

## 참조 및 산출물

**생성된 파일/폴더**:
- `05-GOBI-Scenario-Tests/README.md`: M5 산출물 학습 순서와 실행 결과 요약
- `05-GOBI-Scenario-Tests/guide-quality-checklist.md`: guide response 품질 평가 기준
- `05-GOBI-Scenario-Tests/scenario-gobi-cli-auth.md`: CLI 설치, 인증, Space/Post 검증 시나리오
- `05-GOBI-Scenario-Tests/scenario-gobi-desktop-custom-homepage.md`: Desktop/Applet 상태 확인 시나리오
- `05-GOBI-Scenario-Tests/scenario-version-mismatch.md`: 환경 버전 불일치 시나리오
- `05-GOBI-Scenario-Tests/test-results.md`: 5개 시나리오 테스트 결과와 실패 원인 분류표

**업데이트된 파일**:
- `04-Guiding-Engine-POC/data/test_contexts.json`
- `04-Guiding-Engine-POC/data/trigger_rules.json`
- `04-Guiding-Engine-POC/data/retrieval_index.json`
- `04-Guiding-Engine-POC/src/compose_guide.py`
- `04-Guiding-Engine-POC/tests/run_scenarios.py`
- `04-Guiding-Engine-POC/tests/test_scenarios.md`
- `04-Guiding-Engine-POC/README.md`
- `vl_roadmap/20260426_RoadMap_Vibe-Guiding-VSCode.md`
- `vl_prompts/daily_learning_prompt.md`

**다음 세션 준비사항**:
- M6에서 통합 후보별 비용과 데모 가치를 비교한다.
- M5 테스트 결과 중 `desktop_custom_homepage_blocked` 또는 `version_mismatch`를 5분 demo 후보로 선택한다.

**작성자**: Codex
**방법론**: VibeLearn AI
