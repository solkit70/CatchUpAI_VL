---
title: "Build with AI Source Map"
created: 2026-07-05 07:55:23
tags:
  - build-with-ai
  - source-map
  - builders-lounge
---

## Core Thesis

Build with AI의 핵심 thesis는 **"AI 시대의 병목은 코딩이 아니라 문제를 서비스 가능한 구조로 바꾸는 능력"**이다. AI 도구는 데모를 빠르게 만들 수 있지만, 실제 서비스가 되려면 문제 정의, 데이터 준비, 사용자 검증, 인간 검토 경계, 비용·지연·신뢰성 같은 운영 기준이 필요하다. [[Initiatives/Builders Lounge/builders/Song-Jae-hee-Build-with-AI/2026-06-29 Build with AI source note#Live #17 Experiment Angle|Build with AI source note]]의 "데모에서 서비스로 넘어가는 벽"은 이 Topic의 첫 영상 중심 질문으로 적합하다.

이 thesis는 `reading-notes.md`의 완독 이해 노트에서 다시 확인된다. Part 5는 문제 정의를, Part 4는 데이터 준비를, Part 10은 프로덕션 전환을, Part 11은 책임과 검증을 다룬다. 즉 첫 영상은 Build with AI 전체 요약이 아니라, **"왜 AI로 만든 데모는 많지만 실제 서비스는 적은가"**라는 하나의 시청자 문제에 집중하는 편이 좋다.

## User Review Reflected

2026-07-19에 사용자가 `reading-notes.md`를 직접 읽고 리뷰를 반영했다. 이 리뷰에서 첫 영상의 대상과 톤이 더 명확해졌다. 대상은 **도메인 지식은 풍부하지만 컴퓨터·IT에는 익숙하지 않은 시니어 비개발자**이며, 대표 사례는 BeYouLifeUpWithUs 프로젝트에서 이선생님과 함께 Voice Legacy 앱을 테스트하고 배포 과정에서 막힌 경험이다. 따라서 M2 이후 영상 기획은 Builders Lounge/Bila AI Agent를 중심 사례로 밀기보다, 비개발자가 AI로 만들기는 성공했지만 배포·검증·공유 단계에서 막히는 실제 장면을 중심에 둔다.

영상 톤은 세 가지를 동시에 잡는다. 첫째, "당신의 도메인 지식이 해자다"라고 격려한다. 둘째, "AI가 처음부터 끝까지 다 해주지는 않는다"는 현실을 분명히 말한다. 셋째, 그래도 지금 AI와 함께 배우고 만들어 보는 경험 자체가 미래 준비이므로 도전하라고 권한다. 이 기준은 M2 `Audience and Product Discovery Angle`의 우선 입력값으로 사용한다.

## Part Map

| Part | Role in Source | Video Use |
|---|---|---|
| Part 0 | 비개발자도 실제 작동하는 산출물을 만들 수 있다는 입구를 연다. 코딩 경험보다 문제·데이터·사용자를 신중하게 생각하는 태도가 전제다. | 영상의 약속: 코딩 강의가 아니라, 문제를 아는 사람이 AI로 실제 결과물을 만드는 사고법을 다룬다고 선언한다. |
| Part 1 | AI를 협업자로 쓰려면 브리핑과 맥락이 필요하다는 사고 전환을 제시한다. | "AI가 답답한 이유는 도구보다 briefing/context 부족"이라는 hook으로 사용한다. 로컬 기록과 md 기반 context 축적의 가치를 함께 설명한다. |
| Part 2 | AI가 잘하는 일과 취약한 일을 구분한다. 언어 변환·요약·패턴 종합은 강하지만 사실 검증·중요 판단은 주의해야 한다. | `맡길 일 / 검증할 일 / 사람이 결정할 일` 구분에 사용한다. 이선생님 사례에서는 코딩은 빨라졌지만 배포와 다음 질문 설계에서 막힌 지점을 보여준다. |
| Part 3 | AI 솔루션을 모델, 오케스트레이션, 인터페이스의 세 레이어로 설명한다. | 도구명 나열 대신 워크플로 조립 관점으로 전환한다. 비개발자에게는 "두뇌 / 조율 / 앞문" 정도의 쉬운 말로 바꿔 설명한다. |
| Part 4 | 실제 병목이 모델보다 데이터 품질과 맥락에 있음을 강조한다. | 서비스화 실패 원인 1: 데이터와 업무 맥락 부족. 사용자의 도메인 지식과 기록이 AI 결과물의 차이를 만든다는 메시지로 연결한다. |
| Part 5 | 진짜 기술은 코딩이 아니라 문제를 정확히 정의하는 능력이라고 본다. | 첫 영상의 중심 thesis. `상황 / 사용자 / 제약 / 성공 조건` 프레임워크로 소개하되, 비개발자가 자기 언어로 문제를 설명하는 장면을 우선한다. |
| Part 6 | 프롬프팅을 프로그래밍에 가까운 설계 행위로 본다. 역할, 작업, 맥락, 형식, 제약, 예시가 중요하다. | 지시문이 아니라 요구사항/검증 조건을 만드는 장면에 연결한다. "프롬프트 기술"보다 "생각을 정리해 AI에게 넘기는 법"으로 풀어낸다. |
| Part 7 | AI Agent를 트리거, 도구, 결정, 목표를 가진 행동 시스템으로 설명한다. | [[Ingest/CatchUpAI_VL/Topics/Material_For_Topics/Bila_AI_Agent/bila_agent_project_plan#Bila AI Agent 프로젝트 플랜|Bila AI Agent]]는 후속 bridge로 남긴다. 첫 영상에서는 챗봇과 실제 행동 시스템의 차이를 쉬운 예로 설명한다. |
| Part 8 | 바이브 코딩은 자연어로 구현을 지시하고 테스트·반복하는 프로세스라고 설명한다. | "말로 만들 수 있다"와 "막 만들면 된다"를 구분한다. 비개발자에게는 먼저 계획을 요청하고 작은 단위로 만들며 테스트하는 습관을 강조한다. |
| Part 9 | 코드 어시스턴트가 코드 가시성, 유지보수성, 디버깅, 리뷰를 제공한다고 본다. | 비개발자도 구조를 이해해야 통제권이 생긴다는 메시지에 사용한다. AI는 만능 해결책이 아니라, 배우며 리드하거나 전문가 도움을 받을 때 강해진다는 현실을 넣는다. |
| Part 10 | 데모와 프로덕션의 차이를 예측 불가능한 입력, 실제 사용자 데이터, 비용, 지연, 신뢰, 실패 대응으로 설명한다. | 첫 영상의 핵심 챕터. `나 혼자 쓸 앱`과 `다른 사람도 쓸 앱`의 차이를 이선생님 Voice Legacy 앱 배포 사례로 쉽게 보여준다. |
| Part 11 | 할루시네이션과 책임 있는 AI를 grounding, 범위 제한, 검증, 로깅 문제로 다룬다. | 비개발자 대상 핵심 장면. "AI는 사실을 검색하는 사서가 아니라 그럴듯한 다음 말을 만드는 시스템"이라는 쉬운 설명 후, 낮은 리스크/높은 리스크 구분으로 넘어간다. |
| Part 12 | 다음 물결을 에이전트 네트워크, 물리 AI, 자기 개선 시스템으로 전망한다. 해자는 도메인 지식과 적응성이라고 본다. | 마무리 메시지: 당신의 도메인 지식이 해자다. AI가 다 해주지는 않지만, 지금 배우며 만들어 보는 경험 자체가 미래 준비다. |

## Video Thesis Candidates

| Candidate | Thesis | 판단 |
|---|---|---|
| A | AI 시대의 병목은 코딩이 아니라 문제 정의다. | 강하지만 데이터·검증·운영까지 포괄하기엔 좁다. |
| B | 데모는 AI가 만들 수 있지만, 서비스는 문제·데이터·검증·운영 기준이 있어야 한다. | 첫 영상에 가장 적합하다. |
| C | 비개발자 빌더의 경쟁력은 코딩이 아니라 자기 도메인의 문제와 데이터를 AI에게 설명하는 능력이다. | Builders Lounge 관점의 후속 영상 또는 결론 메시지로 좋다. |

**추천 thesis**: 데모는 AI가 만들 수 있지만, 서비스는 문제·데이터·검증·운영 기준이 있어야 한다.

## Audience and Tone

| 항목 | 결정 |
|---|---|
| Primary Audience | 도메인 지식은 풍부하지만 컴퓨터·IT에 익숙하지 않은 시니어 비개발자 |
| Representative Case | BeYouLifeUpWithUs 프로젝트에서 이선생님이 Voice Legacy 앱을 만들고, 가족도 쓸 수 있게 배포하는 단계에서 막힌 경험 |
| Core Promise | "AI로 데모를 만드는 데서 멈추지 않고, 다른 사람도 쓸 수 있는 결과물로 가려면 무엇을 생각해야 하는지 쉽게 설명한다." |
| Tone | 격려 + 현실 + 도전 권유 |
| Avoid | 도구명 나열, 개발자 중심 설명, Builders Lounge 내부 운영 이야기 과다 사용 |

## BeYouLifeUpWithUs Connection

이번 영상의 중심 사례는 BeYouLifeUpWithUs 프로젝트에서 얻은 실제 협업 인사이트로 잡는다. 이선생님은 컴퓨터·IT에 익숙한 편은 아니지만, 자신의 도메인 문제와 사용 목적은 분명히 알고 있었다. Vibe Coding을 통해 "녹음 → 전사 → 문서 저장 → 프린트"까지 되는 앱을 빠르게 만들었지만, 가족도 쓸 수 있게 Public에 배포하고 URL을 전달하는 단계에서 막혔다. 이 장면은 Part 10의 `데모와 프로덕션의 차이`, Part 2의 `AI가 대신 못 하는 일`, Part 9의 `AI를 리드할 정도의 지식 또는 전문가 도움 필요`를 한 번에 설명하는 사례다. → [[Ingest/Transcripts/BeYouLifeUpWithUs/2026-07-16 Session 18 - Voice Legacy 영어 앱 테스트 + Netlify 배포|BeYouLifeUpWithUs S18: Voice Legacy 앱 배포]]

## Builders Lounge Connection

Build with AI는 비개발자 빌더가 데모를 만드는 방법에서 출발하지만, Builders Lounge 관점에서는 "각 빌더의 Product 상태를 어떻게 발견하고 서로 연결할 것인가"라는 운영 질문으로 확장된다. [[Ingest/CatchUpAI_VL/Topics/Material_For_Topics/Bila_AI_Agent/bila_agent_project_plan#Phase 2 — 멤버 매칭 (Product 모니터링 & 자동 연결)|Bila AI Agent]]는 멤버의 Product 상태 모니터링, 보완 관계 감지, 자동 연결 알림을 목표로 하므로 Build with AI의 문제 구조화 논지를 커뮤니티 운영 시스템으로 연결할 수 있다.

다만 첫 영상에서는 Builders Lounge/Bila AI Agent를 중심 사례로 두지 않는다. 이번 영상의 대상은 더 넓고 쉬운 설명이 필요한 비개발자이므로, Builders Lounge는 "후속 질문" 또는 "커뮤니티 검증장" 정도로만 배치한다. 특히 Part 4와 Part 7은 후속 영상에서 더 중요하다. Part 4는 AI Agent의 성능이 모델보다 데이터와 맥락에 달려 있음을 보여주고, Part 7은 Agent가 단일 챗봇이 아니라 트리거·도구·결정·목적지를 가진 시스템임을 설명한다.

## First Video Candidate

첫 영상은 Build with AI 전체 소개보다 "AI로 데모는 만들었는데 왜 서비스는 안 될까?"에 집중하는 편이 좋다. 이 angle은 Part 5, Part 10, Part 11을 중심축으로 삼고, Part 0-4를 배경 설명으로 사용한다. Part 7과 Bila AI Agent는 마지막에 "이 문제를 커뮤니티/에이전트 시스템으로 풀려면 무엇이 필요한가"라는 후속 질문으로 배치한다.

## Proposed First Video Structure

| Segment | Purpose | Source |
|---|---|---|
| Hook | "AI로 앱은 만들었는데, 가족에게 링크 하나 보내는 단계에서 막힌다"는 실제 경험을 호출한다. | Part 0, Part 2, Part 10 |
| Audience Promise | 코딩 강의가 아니라, 문제를 아는 비개발자가 AI로 결과물을 만들 때 필요한 생각의 순서를 알려준다고 말한다. | Part 0, Part 12 |
| Core Claim | 병목은 코딩이 아니라 문제를 서비스 가능한 구조로 바꾸는 능력이라고 말한다. | Part 5 |
| Wall 1: Problem Definition | 상황, 사용자, 제약, 성공 조건이 없으면 AI가 잘못된 문제를 빠르게 만든다. | Part 5, Part 6 |
| Wall 2: Context and Records | 모델보다 데이터 품질과 자기 맥락이 중요하다. 생각을 기록해야 AI에게 줄 수 있는 입력이 생긴다. | Part 1, Part 4 |
| Wall 3: From My App to Other People's App | 나 혼자 쓰는 데모와 다른 사람도 쓰는 서비스의 차이를 설명한다. | Part 10 |
| Wall 4: Trust and Human Review | AI의 환각과 책임 문제를 쉬운 말로 설명하고, 어디서 사람이 확인해야 하는지 나눈다. | Part 2, Part 11 |
| Bridge | Builders Lounge/Bila AI Agent는 이런 데모를 커뮤니티 검증과 context 기반 Agent로 연결하는 후속 질문으로 둔다. | Part 3, Part 7 |
| Close | 도메인 지식은 해자이고, AI가 다 해주지는 않지만, 지금 배우며 만드는 경험 자체가 미래 준비라고 정리한다. | Part 12 |

## M1 Completion Note

2026-07-19 사용자 확인에 따라 `reading-notes.md`의 사용자 리뷰 반영을 M1 실습1 완료 조건으로 인정한다. 이 Source Map은 해당 리뷰를 반영해 M1 실습2 산출물로 확정한다. 다음 단계는 M2에서 이 Source Map을 기준으로 첫 영상의 Audience와 Product Discovery Angle을 정식으로 좁히는 것이다.
