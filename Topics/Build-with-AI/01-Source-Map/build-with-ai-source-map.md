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

## Part Map

| Part | Role in Source | Video Use |
|---|---|---|
| Part 0 | 비개발자도 실제 작동하는 산출물을 만들 수 있다는 입구를 연다. 코딩 경험보다 문제·데이터·사용자를 신중하게 생각하는 태도가 전제다. | 영상의 약속: 코딩 강의가 아니라 빌더 사고법을 다룬다고 선언한다. |
| Part 1 | AI를 협업자로 쓰려면 브리핑이 필요하다는 사고 전환을 제시한다. | "AI가 답답한 이유는 도구보다 briefing/context 부족"이라는 hook으로 사용한다. |
| Part 2 | AI가 잘하는 일과 취약한 일을 구분한다. 언어 변환·요약·패턴 종합은 강하지만 사실 검증·중요 판단은 주의해야 한다. | AI와 사람이 각각 책임질 경계를 설명한다. `맡길 일 / 검증할 일 / 사람이 결정할 일` 구분에 사용한다. |
| Part 3 | AI 솔루션을 모델, 오케스트레이션, 인터페이스의 세 레이어로 설명한다. | 도구명 나열 대신 워크플로 조립 관점으로 전환한다. Bila AI Agent 설명의 bridge로 사용한다. |
| Part 4 | 실제 병목이 모델보다 데이터 품질과 맥락에 있음을 강조한다. | 서비스화 실패 원인 1: 데이터와 업무 맥락 부족. Builders Lounge 기록/context 전략과 직접 연결한다. |
| Part 5 | 진짜 기술은 코딩이 아니라 문제를 정확히 정의하는 능력이라고 본다. | 첫 영상의 중심 thesis. `상황 / 사용자 / 제약 / 성공 조건` 프레임워크로 소개한다. |
| Part 6 | 프롬프팅을 프로그래밍에 가까운 설계 행위로 본다. 역할, 작업, 맥락, 형식, 제약, 예시가 중요하다. | 지시문이 아니라 요구사항/검증 조건을 만드는 장면에 연결한다. Context의 중요성을 Catch Up AI 관점으로 보강한다. |
| Part 7 | AI Agent를 트리거, 도구, 결정, 목표를 가진 행동 시스템으로 설명한다. | [[Ingest/CatchUpAI_VL/Topics/Material_For_Topics/Bila_AI_Agent/bila_agent_project_plan#Bila AI Agent 프로젝트 플랜|Bila AI Agent]] 연결 지점. 챗봇이 아니라 Product Discovery 운영 시스템으로 설명한다. |
| Part 8 | 바이브 코딩은 자연어로 구현을 지시하고 테스트·반복하는 프로세스라고 설명한다. | "말로 만들 수 있다"와 "막 만들면 된다"를 구분한다. 정의→구조→작은 구현→테스트→반복 흐름에 사용한다. |
| Part 9 | 코드 어시스턴트가 코드 가시성, 유지보수성, 디버깅, 리뷰를 제공한다고 본다. | Codex/Claude Code/Cursor 등 제작 도구를 현실적인 작업 환경으로 소개한다. 비개발자도 구조를 이해해야 한다는 메시지에 사용한다. |
| Part 10 | 데모와 프로덕션의 차이를 예측 불가능한 입력, 실제 사용자 데이터, 비용, 지연, 신뢰, 실패 대응으로 설명한다. | 첫 영상의 핵심 챕터. `Demo → Pilot → Production` 도식으로 사용한다. |
| Part 11 | 할루시네이션과 책임 있는 AI를 grounding, 범위 제한, 검증, 로깅 문제로 다룬다. | 서비스화 실패 원인 3: 검증 경계와 책임 부재. Bila AI Agent 안전장치 설계에 연결한다. |
| Part 12 | 다음 물결을 에이전트 네트워크, 물리 AI, 자기 개선 시스템으로 전망한다. 해자는 도메인 지식과 적응성이라고 본다. | 후속 영상 또는 시리즈 확장용 소재. 마무리에서 "도구는 바뀌지만 기본기는 남는다"는 메시지로 사용한다. |

## Video Thesis Candidates

| Candidate | Thesis | 판단 |
|---|---|---|
| A | AI 시대의 병목은 코딩이 아니라 문제 정의다. | 강하지만 데이터·검증·운영까지 포괄하기엔 좁다. |
| B | 데모는 AI가 만들 수 있지만, 서비스는 문제·데이터·검증·운영 기준이 있어야 한다. | 첫 영상에 가장 적합하다. |
| C | 비개발자 빌더의 경쟁력은 코딩이 아니라 자기 도메인의 문제와 데이터를 AI에게 설명하는 능력이다. | Builders Lounge 관점의 후속 영상 또는 결론 메시지로 좋다. |

**추천 thesis**: 데모는 AI가 만들 수 있지만, 서비스는 문제·데이터·검증·운영 기준이 있어야 한다.

## Builders Lounge Connection

Build with AI는 비개발자 빌더가 데모를 만드는 방법에서 출발하지만, Builders Lounge 관점에서는 "각 빌더의 Product 상태를 어떻게 발견하고 서로 연결할 것인가"라는 운영 질문으로 확장된다. [[Ingest/CatchUpAI_VL/Topics/Material_For_Topics/Bila_AI_Agent/bila_agent_project_plan#Phase 2 — 멤버 매칭 (Product 모니터링 & 자동 연결)|Bila AI Agent]]는 멤버의 Product 상태 모니터링, 보완 관계 감지, 자동 연결 알림을 목표로 하므로 Build with AI의 문제 구조화 논지를 커뮤니티 운영 시스템으로 연결할 수 있다.

특히 Part 4와 Part 7이 중요하다. Part 4는 AI Agent의 성능이 모델보다 데이터와 맥락에 달려 있음을 보여주고, Part 7은 Agent가 단일 챗봇이 아니라 트리거·도구·결정·목적지를 가진 시스템임을 설명한다. Builders Lounge의 회의록, 멤버 소개, Product 상태, 피드백 기록은 단순 저장 자료가 아니라 Agent가 사용할 context다.

## First Video Candidate

첫 영상은 Build with AI 전체 소개보다 "AI로 데모는 만들었는데 왜 서비스는 안 될까?"에 집중하는 편이 좋다. 이 angle은 Part 5, Part 7, Part 10, Part 11을 중심축으로 삼고, Part 0-4를 배경 설명으로 사용하며, Bila AI Agent는 마지막에 "이 문제를 커뮤니티/에이전트 시스템으로 풀려면 무엇이 필요한가"라는 다음 질문으로 배치한다.

## Proposed First Video Structure

| Segment | Purpose | Source |
|---|---|---|
| Hook | "AI로 데모는 만들었는데 왜 서비스는 안 될까?"라는 시청자 경험을 호출한다. | Part 0, Part 10 |
| Core Claim | 병목은 코딩이 아니라 문제를 서비스 가능한 구조로 바꾸는 능력이라고 말한다. | Part 5 |
| Wall 1: Problem Definition | 상황, 사용자, 제약, 성공 조건이 없으면 AI가 잘못된 문제를 빠르게 만든다. | Part 5, Part 6 |
| Wall 2: Data and Context | 모델보다 데이터 품질과 조직 맥락이 중요하다. | Part 4 |
| Wall 3: Validation and Responsibility | 프로덕션은 검증, 비용, 지연, 신뢰, 실패 대응을 요구한다. | Part 10, Part 11 |
| Builders Lounge Bridge | 혼자 만든 데모를 커뮤니티 검증과 Agent context로 연결한다. | Part 3, Part 7 |
| Close | 도구는 바뀌지만 문제 정의·데이터·검증·운영 기준은 남는다고 정리한다. | Part 12 |
