---
title: "Component Responsibilities - Vibe Guiding"
created: 2026-05-10 06:32:59
tags:
  - vibe-guiding
  - architecture
  - component-boundary
  - gobi-cli
sources:
  - "[[Ingest/CatchUpAI_VL/Topics/Vibe-Guiding-VSCode/01-Vision-and-Architecture/source-map#M1 기준 핵심 결론|Vibe Guiding Source Map]]"
  - "[[Ingest/CatchUpAI_VL/Topics/Vibe-Guiding-VSCode/01-Vision-and-Architecture/poc-target-selection#M2로 넘길 결정|POC Target Selection]]"
  - "[[Ingest/CatchUpAI_VL/Topics/GOBI-CLI/README#v2.0.12 주요 변경|GOBI CLI v2.0.12 Topic Index]]"
---

## 책임 분리 원칙

Vibe Guiding은 두 컴포넌트로 나눈다. 첫 번째는 **Vibe Manual/CVL 컴포넌트**로, 최신 지식 기반을 만들고 유지한다. 두 번째는 **Guiding Engine 컴포넌트**로, 사용자의 현재 상태와 problem signal을 받아 필요한 문서를 찾아 실행 가능한 안내로 바꾼다.

> "필요한 사람에게 필요한 내용을 필요할 때에 알려주는 Guide"

이 문장은 두 컴포넌트의 경계를 정하는 기준이다. Manual/CVL은 "필요한 내용"을 최신 상태로 준비하고, Guiding Engine은 "필요한 사람"과 "필요할 때"를 판단한다.

## 컴포넌트 책임표

| 컴포넌트 | 입력 | 출력 | 저장 위치 | 절대 하지 말아야 할 일 |
|---|---|---|---|---|
| Vibe Manual/CVL | GOBI CLI Topic 문서, CVL WorkLog, v2.0.12 변경표, 실습 결과 | `manual_index`, 문서 메타데이터, 변경 이력, known failures | `03-Vibe-Manual-CVL/`, 기존 `Topics/GOBI-CLI/` 문서 | 사용자의 현재 문제를 추측해서 안내를 생성하지 않는다 |
| Guiding Engine | `user_context.json`, `problem_signal`, `trigger_rules`, `manual_index` | `guide_response.md`, trigger log, retrieval result | `04-Guiding-Engine-POC/outputs/` | 최신 매뉴얼을 임의로 고치거나 검증되지 않은 명령어를 지어내지 않는다 |

## 하위 모듈 책임

| 하위 모듈 | 소속 컴포넌트 | 책임 | 입력 | 출력 |
|---|---|---|---|---|
| Manual Builder | Vibe Manual/CVL | GOBI CLI v2.0.12 문서를 안내 가능한 단위로 나눈다 | README, guides, CVL WorkLog | `manual_index.json` |
| CVL Updater | Vibe Manual/CVL | 버전 변화와 문서 변경점을 감지해 매뉴얼을 갱신한다 | 새 릴리스 정보, 변경된 Topic 문서 | changelog, stale-source report |
| Context Collector | Guiding Engine | 사용자 환경과 CLI 상태를 수집한다 | OS, `gobi --version`, `gobi auth status`, `gobi space list` | `user_context.json` |
| Trigger Evaluator | Guiding Engine | 안내가 필요한 상황인지 판단한다 | `user_context.json`, `problem_signal`, `trigger_rules.json` | trigger decision |
| Retriever | Guiding Engine | 문제에 맞는 매뉴얼 조각을 고른다 | trigger decision, `manual_index.json` | retrieval result |
| Guide Composer | Guiding Engine | 사용자가 바로 실행할 수 있는 안내를 작성한다 | retrieval result, user level, context | `guide_response.md` |

## GOBI CLI v2.0.12 기준 입력 신호

| 신호 | 수집 방법 | 관련 매뉴얼 |
|---|---|---|
| CLI 설치 여부 | `gobi --version` | `01-Setup-Auth/concepts/installation-guide.md` |
| 인증 상태 | `gobi auth status` | `01-Setup-Auth/concepts/installation-guide.md` |
| Vault 초기화 여부 | `.gobi/settings.yaml`, `gobi vault list` | `01-Setup-Auth/concepts/core-concepts.md` |
| 발행 파일 준비 여부 | `PUBLISH.md` 존재 여부 | `02-Brain-Session/guides/brain-publish-guide.md` |
| Space 접근 가능 여부 | `gobi space list` | `03-Space-Thread/guides/space-navigation.md` |
| Post 작업 가능 여부 | `gobi space list-posts`, `gobi space create-post` | `03-Space-Thread/guides/thread-management.md` |
| Session 이어가기 가능 여부 | `gobi session list/get/create-reply` | `02-Brain-Session/guides/session-management.md` |

## 실패 모드와 fallback

| 실패 모드 | 원인 후보 | fallback |
|---|---|---|
| `gobi` 명령을 찾을 수 없음 | 설치 안 됨, PATH 미반영 | npm 설치 명령과 새 터미널 재시작 안내 |
| 인증 상태 확인 실패 | 로그인 안 됨, 토큰 만료 | `gobi auth login`과 device-code flow 안내 |
| 구 명령어 사용 | v0.6.x 자료를 참고함 | v2.0.12 변환표를 먼저 제시 |
| Space/Post 작업 실패 | Space 미선택, 권한 부족, 잘못된 slug | `gobi space list`, `gobi space warp`, `--space-slug` 확인 |
| 매뉴얼 검색 실패 | index 누락, 키워드 불일치 | Quick Reference와 core concepts를 fallback 문서로 사용 |

## M4 구현으로 넘길 결정

M4의 파일 기반 POC는 Manual/CVL을 직접 갱신하지 않는다. 이미 정리된 GOBI CLI v2.0.12 문서를 `manual_index.json`으로 읽고, Guiding Engine 쪽의 `collect_context.py`, `evaluate_trigger.py`, `retrieve_manual.py`, `compose_guide.py` 흐름만 검증한다.
