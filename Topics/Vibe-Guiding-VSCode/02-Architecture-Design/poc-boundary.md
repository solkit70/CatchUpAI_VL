---
title: "POC Boundary - Vibe Guiding"
created: 2026-05-10 06:32:59
tags:
  - vibe-guiding
  - poc
  - boundary
  - gobi-cli
sources:
  - "[[Ingest/CatchUpAI_VL/Topics/Vibe-Guiding-VSCode/01-Vision-and-Architecture/poc-target-selection#선택 결론|POC Target Selection]]"
  - "[[Ingest/CatchUpAI_VL/Topics/Vibe-Guiding-VSCode/02-Architecture-Design/component-responsibilities#M4 구현으로 넘길 결정|Component Responsibilities]]"
---

## POC 목적

첫 POC의 목적은 GOBI 제품 통합이 아니라 **파일 기반 Guiding Engine의 최소 흐름 검증**이다. GOBI CLI v2.0.12 문서를 최신 Vibe Manual로 보고, 사용자의 CLI 상태와 problem signal을 입력으로 받아 적절한 guide response를 생성할 수 있는지만 확인한다.

## 포함 범위

| 범위 | 설명 | 산출물 |
|---|---|---|
| Context 수집 | OS, CLI 설치 여부, CLI 버전, 인증 상태, Space 접근 가능 여부 수집 | `user_context.json` |
| Trigger 평가 | 안내가 필요한 problem signal인지 판단 | `trigger_decision.json` |
| Manual retrieval | GOBI CLI v2.0.12 문서 중 관련 항목 선택 | `retrieval_result.json` |
| Guide 작성 | 사용자가 바로 실행할 수 있는 단계별 안내 생성 | `guide_response.md` |
| 최소 테스트 | 설치 실패, 인증 실패, Space/Post 작업 막힘 시나리오 검증 | `test_results.md` |

## 제외 범위

| 제외 항목 | 제외 이유 | 후속 위치 |
|---|---|---|
| GOBI Desktop/Applet 직접 통합 | GUI 상태 수집과 제품 통합 범위가 크다 | M5/M6 |
| 실시간 백그라운드 감지 | 첫 POC에서는 명시적 입력으로 충분하다 | 후속 Topic |
| 웹 UI 자동 조작 | 안정적인 자동화보다 안내 품질 검증이 먼저다 | M6 이후 |
| CVL 자동 실행 | M4는 Manual/CVL을 소비만 한다 | M3 또는 별도 자동화 |
| LLM API 통합 | 우선 rule + template 기반으로 경계를 검증한다 | 고도화 단계 |

## 입력 파일 계약

```json
{
  "user_context": {
    "os": "Windows 11",
    "gobi_cli_version": "2.0.12",
    "auth_status": "authenticated",
    "active_space": "changbal",
    "available_commands": ["auth", "vault", "space", "global", "session"]
  },
  "problem_signal": {
    "type": "space_post_blocked",
    "message": "Space에 Post를 만드는 명령을 모르겠다"
  }
}
```

## 출력 파일 계약

`guide_response.md`는 최소한 다음을 포함해야 한다.

| 항목 | 설명 |
|---|---|
| 현재 상태 요약 | 수집된 context를 단정 가능한 범위에서만 요약 |
| 판단 근거 | 어떤 trigger rule이 활성화됐는지 표시 |
| 실행 단계 | v2.0.12 기준 명령어만 사용 |
| 완료 신호 | 사용자가 무엇을 보면 성공으로 판단할지 제시 |
| fallback | 실패 시 다음 확인 항목 제시 |
| source attribution | 사용한 GOBI CLI 문서 경로 표시 |

## M4 최소 시나리오

| 시나리오 | problem signal | 기대 안내 |
|---|---|---|
| CLI 설치 확인 실패 | `gobi` 명령을 찾을 수 없음 | `npm install -g @gobi-ai/cli`, 새 터미널, `gobi --version` 확인 |
| 인증 상태 불명확 | `gobi auth status` 실패 또는 logged out | `gobi auth login`, device-code flow, `gobi auth status` 재확인 |
| Space/Post 작업 막힘 | Post 생성 명령을 모름 | `gobi space list`, `gobi space warp`, `gobi space create-post` 안내 |

## 완료 기준

- [ ] `user_context.json` 샘플 3개 작성
- [ ] `trigger_rules.json` 샘플 작성
- [ ] `manual_index.json`에 GOBI CLI v2.0.12 문서 최소 6개 등록
- [ ] 각 시나리오에서 `guide_response.md` 생성
- [ ] 생성된 안내가 구 명령어(`create-thread`, `BRAIN.md`, `gobi init`)를 사용하지 않음
- [ ] 실패 시 fallback과 source attribution 포함
