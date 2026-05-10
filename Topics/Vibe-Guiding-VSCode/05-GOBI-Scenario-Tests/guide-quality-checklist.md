---
title: "Guide Quality Checklist"
created: 2026-05-10 07:22:45
tags:
  - vibe-guiding
  - quality-checklist
  - scenario-test
sources:
  - "[[Ingest/CatchUpAI_VL/Topics/GOBI-Guiding/2026-04-13 Gobi Desktop Vibe Guiding 기능 수준 테스트#3. 향후 보완 및 개선 방향|GOBI Desktop Vibe Guiding 기능 수준 테스트]]"
  - "[[Ingest/CatchUpAI_VL/Topics/Vibe-Guiding-VSCode/04-Guiding-Engine-POC/README|M4 Guiding Engine POC]]"
---

## 평가 목적

Guide Quality Checklist는 `guide_response.md`가 사용자의 막힘을 실제로 줄이는지 평가하기 위한 기준이다. M5에서는 정답 문장 자체보다 입력 context, trigger rule, retrieval manual, guide response 사이의 연결이 논리적인지 확인한다.

> **할루시네이션 방지**: 이번 테스트에서 앱에 존재하지 않는 메뉴를 안내한 사례가 발생함.

이 인용문은 Desktop/Applet 안내에서 가장 중요한 품질 기준을 보여준다. Vibe Guiding은 친절한 답변을 만드는 것이 아니라, 사용자의 실제 상태를 확인한 뒤 검증된 범위 안에서 다음 행동을 제안해야 한다.

## 공통 체크리스트

| 기준 | 통과 조건 | 실패 시 의심 컴포넌트 |
|---|---|---|
| 상태 요약 | 문제 신호, 버전, 인증 상태, 활성 작업 맥락을 누락하지 않는다. | context |
| Trigger 적합성 | selected rule이 problem signal의 실제 원인과 맞다. | trigger |
| Manual 적합성 | selected manual이 guide type과 사용자 목표에 맞다. | retrieval |
| 실행 가능성 | 사용자가 바로 실행하거나 확인할 수 있는 다음 행동이 있다. | compose |
| 완료 신호 | 성공 여부를 판단할 수 있는 관찰 가능한 신호가 있다. | manual |
| Fallback | 실패했을 때 되돌아갈 확인 절차가 있다. | manual 또는 compose |
| 최신성 | v2.0.12 기준의 Post, Vault, PUBLISH.md 용어를 사용한다. | manual 또는 retrieval |
| 비단정성 | 확인되지 않은 메뉴, 버튼, 경로를 지어내지 않는다. | compose |

## 시나리오별 추가 기준

| 시나리오 | 추가 품질 기준 |
|---|---|
| CLI 미설치 | `npm install -g @gobi-ai/cli`, 새 터미널, `gobi --version` 확인을 포함한다. |
| CLI 인증 필요 | `gobi auth login`과 `gobi auth status`를 분리하고, device-code flow를 설명한다. |
| Space/Post 막힘 | 구 `thread` 용어를 새 `post` 용어로 변환한다. |
| Desktop/Applet 막힘 | Desktop 버전, Vault Path, Applet 경로, 실제 Settings 메뉴 확인을 먼저 요구한다. |
| Version mismatch | `node --version`, `npm --version`, `gobi --version` 확인을 제품 단계보다 먼저 둔다. |

## 실패 원인 분류 규칙

실패 원인은 한 번에 하나의 1차 원인으로 분류한다. 입력에 필요한 상태가 없으면 context, 상태는 맞는데 rule이 틀리면 trigger, rule은 맞는데 manual이 틀리면 retrieval, manual은 맞는데 안내문이 위험하거나 실행 불가능하면 compose로 본다.
