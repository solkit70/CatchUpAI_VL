---
title: "WorkLog - M4: Guiding Engine POC"
created: 2026-05-10 07:11:33
tags:
  - vibe-guiding
  - vibelearn-ai
  - worklog
  - m4
sources:
  - "[[Ingest/CatchUpAI_VL/Topics/Vibe-Guiding-VSCode/vl_roadmap/20260426_RoadMap_Vibe-Guiding-VSCode#M4 - Guiding Engine POC 개발|M4 Roadmap]]"
  - "[[Ingest/CatchUpAI_VL/Topics/Vibe-Guiding-VSCode/03-Vibe-Manual-CVL/retrieval-metadata-design#M4로 넘길 결정|M3 Retrieval Metadata Design]]"
---

## 오늘의 학습 목표

- [x] `04-Guiding-Engine-POC/` 폴더 구조 생성
- [x] `user_context.sample.json`, `trigger_rules.json`, `retrieval_index.json` 작성
- [x] `collect_context.py`, `evaluate_trigger.py`, `retrieve_manual.py`, `compose_guide.py` 구현
- [x] 기본 sample context로 `guide_response.md` 생성
- [x] 최소 3개 테스트 시나리오 실행
- [x] M4 README와 test scenarios 작성

## 진행 내용

### 1. POC 파일 구조 생성

M4 Roadmap에 맞춰 `data`, `src`, `output`, `tests` 폴더를 만들었다. `data`에는 context, trigger rule, retrieval index를 두고, `src`에는 네 단계 실행 스크립트를 분리했다.

### 2. 데이터 계약 작성

`data/user_context.sample.json`에는 GOBI CLI v2.0.12, 인증 상태, 활성 Space, problem signal을 담았다. `data/trigger_rules.json`에는 `cli_missing`, `auth_required`, `old_thread_command_used`, `space_post_blocked`, `vault_publish_blocked` 5개 규칙을 작성했다. `data/retrieval_index.json`에는 GOBI CLI 문서 6개를 manual entry로 등록했다.

### 3. Guiding Engine 구현

`collect_context.py`는 sample context를 output으로 복사하고, `--system` 옵션 사용 시 실제 `gobi --version`, `gobi auth status`, `gobi space list`를 시도할 수 있게 했다. `evaluate_trigger.py`는 problem signal과 keyword 기반 점수로 trigger rule을 고르고, `retrieve_manual.py`는 guide type, problem signal, deprecated terms, command match를 점수화해 manual을 선택한다. `compose_guide.py`는 선택된 manual을 바탕으로 현재 상태, 판단 근거, 실행 단계, 완료 신호, fallback, source attribution을 포함한 `guide_response.md`를 만든다.

### 4. 테스트 실행

`tests/run_scenarios.py`를 추가해 `data/test_contexts.json`의 3개 시나리오를 자동 실행했다. 결과는 `output/test_results.json`에 저장됐고 3개 모두 통과했다.

| 시나리오 | 선택 rule | 선택 manual | 결과 |
|---|---|---|---|
| `cli_missing` | `cli_missing` | `gobi-cli-install` | 통과 |
| `auth_required` | `auth_required` | `gobi-cli-auth-status` | 통과 |
| `space_post_blocked` | `old_thread_command_used` | `gobi-cli-space-create-post` | 통과 |

## 문제 해결 로그

### 문제: sandbox에서 Python 실행 실패

**증상**: 처음 Python 스크립트를 실행할 때 Windows sandbox setup refresh 오류가 발생했다.

**해결**: 사용 승인 후 escalated 실행으로 POC 스크립트를 실행했다. 이후 `collect_context.py`, `evaluate_trigger.py`, `retrieve_manual.py`, `compose_guide.py`, `tests/run_scenarios.py`가 정상 실행됐다.

### 문제: 구 Thread 표현 처리

**증상**: 사용자가 `create-thread`나 Thread라는 표현을 쓸 수 있지만, GOBI CLI v2.0.12에서는 Post 명령어를 사용해야 한다.

**해결**: `deprecated_terms`와 `replacement_terms`를 retrieval index에 넣고, `old_thread_command_used` trigger가 `gobi-cli-space-create-post` manual을 선택하도록 했다.

## DoD 체크리스트

- [x] POC 폴더 구조 생성
- [x] `collect_context.py` 실행 성공
- [x] `trigger_rules.json` 기반 Trigger 판정 성공
- [x] `retrieval_index.json` 기반 문서 선택 성공
- [x] `guide_response.md` 자동 생성 성공
- [x] 최소 3개 테스트 시나리오 통과
- [x] `04-Guiding-Engine-POC/README.md` 작성
- [x] WorkLog 작성 및 Daily Retrospective 완료

**완료율**: 8/8 (100%)

## Daily Retrospective

### What went well

M3에서 만든 metadata 설계가 M4 구현으로 자연스럽게 이어졌다. 특히 `deprecated_terms`와 `replacement_terms`를 index에 포함한 덕분에, 구 `Thread` 표현을 현재 `Post` 명령어로 바꾸는 Vibe Guiding의 핵심 동작을 작은 rule-based POC로 검증할 수 있었다.

### What could be improved

현재 POC는 rule-based matching이므로 표현이 조금만 달라져도 점수가 흔들릴 수 있다. 다만 첫 POC 목적은 제품 통합이 아니라 경계 검증이므로, 다음 단계에서는 실제 GOBI 시나리오로 guide response 품질을 평가한 뒤 retrieval 방식을 확장하는 편이 낫다.

### Insights

Vibe Guiding의 핵심은 LLM 응답 생성이 아니라 입력 계약과 출력 계약이다. `user_context`, `trigger_decision`, `retrieval_result`, `guide_response`가 파일로 분리되니 어느 단계에서 잘못된 안내가 생기는지 추적할 수 있다.

### Tomorrow's focus

- M5 시작: `05-GOBI-Scenario-Tests/` 생성
- guide quality checklist 작성
- GOBI CLI auth / Space Post / version mismatch 시나리오를 M4 POC 출력으로 검증
- 실패 원인을 manual, trigger, retrieval, compose 중 하나로 분류하는 표 작성
