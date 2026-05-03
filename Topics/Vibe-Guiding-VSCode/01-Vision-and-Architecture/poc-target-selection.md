---
title: "POC Target Selection - GOBI CLI"
created: 2026-05-03 07:40:11
tags:
  - vibe-guiding
  - poc
  - gobi-cli
  - m1
sources:
  - "[[Ingest/CatchUpAI_VL/Topics/GOBI-CLI/README#GOBI CLI 학습 — Topic 인덱스|GOBI CLI Topic Index]]"
  - "[[Ingest/CatchUpAI_VL/Topics/GOBI-CLI/01-Setup-Auth/README#M1 — 설치 & 인증 & 핵심 개념|GOBI CLI Setup/Auth]]"
  - "[[Ingest/CatchUpAI_VL/Topics/GOBI-CLI/03-Space-Thread/README#M3 — Space & Thread 협업 기능|GOBI CLI Space/Thread]]"
  - "[[Ingest/CatchUpAI_VL/Topics/GOBI-CLI/04-Capstone/README#M4 — Capstone End-to-End Workflow|GOBI CLI Capstone]]"
  - "[[Ingest/CatchUpAI_VL/Topics/GOBI-Guiding/2026-04-13 Gobi Desktop Vibe Guiding 기능 수준 테스트#1. 테스트 개요|Gobi Desktop Vibe Guiding 기능 수준 테스트]]"
---

## 선택 결론

M4 Guiding Engine POC의 1차 대상은 **GOBI CLI**로 확정한다. Gobi Desktop Custom Homepage/Applet은 사용자 가치와 데모 임팩트가 크지만, 첫 POC에서는 환경 상태 수집과 자동 검증이 쉬운 CLI가 더 적합하다. Desktop/Applet은 M5의 GOBI 시나리오 검증 단계에서 실제 사용자 막힘 사례로 다시 다룬다.

## 평가 기준

| 기준 | 의미 | POC에서 중요한 이유 |
|---|---|---|
| 로컬 재현 가능성 | VS Code와 터미널에서 바로 실행 가능한가 | M4에서 Python 기반 POC를 빠르게 검증해야 한다 |
| 사용자 상태 수집 가능성 | 설치, 인증, 설정, 선택된 Space 등을 기계적으로 확인할 수 있는가 | `collect_context.py`의 입력 품질을 높인다 |
| 테스트 난이도 | 성공/실패를 명확한 출력으로 확인할 수 있는가 | Trigger, Retrieval, Compose를 자동 테스트하기 쉽다 |
| 기존 자료 재사용성 | 이미 구조화된 매뉴얼과 WorkLog가 있는가 | Retrieval Index 초안을 빨리 만들 수 있다 |
| GOBI 팀 설득력 | 데모했을 때 제품 가치가 드러나는가 | 이후 Desktop/Applet 통합 논의의 근거가 된다 |

## 후보 비교

| 후보 | 로컬 재현 가능성 | 사용자 상태 수집 가능성 | 테스트 난이도 | 기존 자료 재사용성 | GOBI 팀 설득력 | 판단 |
|---|---|---|---|---|---|---|
| GOBI CLI | 높음. `gobi --version`, `gobi auth status`, `gobi space list` 같은 명령으로 재현 가능 | 높음. 설치 여부, 인증 상태, Space/Thread 접근을 명령 출력으로 수집 가능 | 낮음. 명령 성공/실패와 JSON 출력으로 검증 가능 | 높음. `GOBI-CLI` Topic에 Setup/Auth, Space/Thread, Capstone 자료가 이미 있음 | 중간-높음. 기술 데모로 명확하고 이후 제품 통합의 기반이 된다 | **1차 POC 대상으로 선택** |
| Gobi Desktop Custom Homepage/Applet | 중간. GUI 상태와 로컬 경로를 재현해야 함 | 중간-낮음. Vault Path, Applet 경로, UI 상태 수집 방식이 더 필요함 | 높음. 실제 UI 적용 성공 여부를 자동 검증하기 어렵다 | 중간. 기능 수준 테스트 기록은 있으나 구조화 매뉴얼은 더 필요함 | 높음. 사용자 가치와 데모 임팩트가 크다 | M5 시나리오 테스트 대상으로 보류 |

## GOBI CLI를 선택한 이유

GOBI CLI는 첫 POC에서 필요한 네 가지 파일 흐름을 가장 선명하게 검증할 수 있다. `user_context.json`에는 OS, CLI 설치 여부, CLI 버전, 인증 상태, 선택된 Space, 명령 실행 가능 여부를 넣을 수 있다. `trigger_rules.json`에는 "gobi 명령을 찾을 수 없음", "인증 상태가 아님", "Space 선택이 안 됨", "Thread 생성 실패" 같은 problem signal을 정의할 수 있다.

이미 [[Ingest/CatchUpAI_VL/Topics/GOBI-CLI/01-Setup-Auth/README#M1 — 설치 & 인증 & 핵심 개념|GOBI CLI Setup/Auth]]와 [[Ingest/CatchUpAI_VL/Topics/GOBI-CLI/03-Space-Thread/README#M3 — Space & Thread 협업 기능|Space/Thread 자료]]가 있으므로 Retrieval Index 초안을 만들기 쉽다. 또한 [[Ingest/CatchUpAI_VL/Topics/GOBI-CLI/04-Capstone/README#M4 — Capstone End-to-End Workflow|Capstone workflow]]가 있어, POC의 end-to-end 테스트 시나리오를 `auth check → Space 확인 → Thread 생성 안내` 흐름으로 잡을 수 있다.

## Desktop/Applet을 보류한 이유

Gobi Desktop Custom Homepage/Applet은 Vibe Guiding의 최종 사용자 가치를 보여주기에 좋은 후보지만, 첫 POC 대상으로는 범위가 크다. [[Ingest/CatchUpAI_VL/Topics/GOBI-Guiding/2026-04-13 Gobi Desktop Vibe Guiding 기능 수준 테스트#⚠️ 발견된 한계점 (Blockers)|기능 수준 테스트]]에서 드러난 문제도 Vault Path, Applet 경로, UI 상태, 메뉴 존재 여부처럼 GUI와 실제 앱 상태를 정밀하게 알아야 해결된다.

따라서 Desktop/Applet은 M4의 파일 기반 엔진이 동작한 뒤, M5에서 Scenario Test로 가져오는 편이 낫다. 이 순서가 되면 CLI POC로 검증한 Context Collector, Trigger Evaluator, Retrieval, Guide Composer 구조를 Desktop/Applet 문제에 확장할 수 있다.

## M4 POC 초기 시나리오

| 시나리오 | problem signal | 필요한 context | 기대 guide response |
|---|---|---|---|
| CLI 설치 확인 실패 | `gobi` 명령을 찾을 수 없음 | OS, Node/npm 설치 여부, PATH | 설치 명령, 버전 확인, PATH 확인, 완료 신호 |
| 인증 상태 불명확 | `gobi auth status` 실패 또는 로그아웃 상태 | CLI 버전, auth status 출력 | 로그인 절차, 브라우저 인증, 인증 완료 확인 |
| Space 작업 막힘 | Space 목록 또는 Thread 생성 실패 | selectedSpaceSlug, `gobi space list`, `list-threads` 결과 | Space 선택, Thread 생성 명령, 실패 시 fallback |

## M2로 넘길 결정

M2의 Architecture Design은 GOBI CLI 기준으로 작성한다. Vibe Manual/CVL 컴포넌트는 기존 `GOBI-CLI` Topic 문서와 CVL 업데이트 기록을 최신 매뉴얼 소스로 본다. Guiding Engine 컴포넌트는 CLI 환경 상태를 수집하고, problem signal에 따라 관련 문서를 찾아, 사용자가 바로 실행할 수 있는 guide response를 생성하는 역할로 설계한다.
