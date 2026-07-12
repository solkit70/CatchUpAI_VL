---
title: "First Video Angle - Build with AI"
created: 2026-07-05 07:55:23
tags:
  - build-with-ai
  - video-angle
  - catch-up-ai
---

## Status

이 문서는 승인 전 선행 초안이다. M2를 정식 완료로 처리하려면 먼저 M2 오늘 학습 계획을 사용자에게 제시하고 승인을 받은 뒤, 아래 angle 후보와 story flow를 검토/수정해야 한다. 아래 DoD 체크는 초안 기준 완료를 뜻하며 Roadmap 정식 완료율에는 반영하지 않는다.

## Recommended Angle

첫 영상의 추천 angle은 "AI로 데모는 만들었는데 왜 서비스는 안 될까?"이다. 이 질문은 Build with AI 자료의 핵심인 비개발자 빌더, 문제 구조화, 데이터 병목, 에이전트, 바이브 코딩, 프로덕션 전환을 하나의 시청자 문제로 묶을 수 있다.

최종 추천 thesis는 다음이다.

> 데모는 AI가 만들 수 있지만, 서비스는 문제·데이터·검증·운영 기준이 있어야 한다.

## Target Viewer

대상 시청자는 AI 도구로 뭔가를 만들어 본 적은 있지만 실제 사용자에게 쓰게 만들지는 못한 비개발자 빌더다. 예를 들면 창업자, 운영 담당자, 컨설턴트, 도메인 전문가, 또는 Cursor/Codex/Claude Code로 데모를 만들어 봤지만 제품화 기준에서 멈춘 사람이다.

이 시청자는 "AI 도구를 써본 적 없는 초보자"가 아니다. 이미 ChatGPT, Claude, Cursor, Lovable, Bolt, Codex 같은 도구로 뭔가를 만들어봤고, 화면에 보이는 데모나 작은 자동화까지는 경험했다. 하지만 실제 사용자, 반복 사용, 데이터 품질, 비용, 검증, 운영 책임 앞에서 멈춰 있는 사람이다.

## Main Message

이 영상의 메시지는 "서비스화의 병목은 코딩 실력이 아니라 문제, 데이터, 사용자, 검증, 운영 기준을 구조화하는 능력"이다. [[Initiatives/Builders Lounge/builders/Song-Jae-hee-Build-with-AI/2026-06-29 Build with AI source note#Live #17 Experiment Angle|Build with AI source note]]의 관찰처럼 데모와 서비스 사이에는 단순 기능 구현 이상의 벽이 있으며, 이 벽을 넘으려면 AI를 잘 쓰는 법보다 먼저 무엇을 서비스로 만들 것인지 정의해야 한다.

## Angle Candidates

| 후보 | 설명 | 장점 | 보류/선택 이유 |
|---|---|---|---|
| A. Build with AI 전체 소개 | 12부작 전체를 소개하고 각 파트가 무엇을 다루는지 개괄한다. | 자료 소개에는 충실하고 송재희님 가이드 전체를 알리기 좋다. | 첫 영상으로는 너무 넓다. 시청자의 즉각적인 문제를 잡기 어렵다. |
| B. AI로 데모는 만들었는데 왜 서비스는 안 될까? | 데모와 실제 서비스 사이의 벽을 문제 정의, 데이터, 검증, 운영 기준으로 설명한다. | 시청자가 이미 겪었을 법한 막힘을 바로 호출하고, Build with AI 핵심 파트를 하나의 논지로 묶을 수 있다. | **최종 추천**. |
| C. 비개발자 빌더의 새 경쟁력 | 코딩보다 도메인 지식, 문제 정의, context가 중요하다는 관점으로 간다. | Catch Up AI와 Builders Lounge 철학을 강하게 드러낼 수 있다. | 후속 영상 또는 결론 메시지로 적합하다. 첫 영상 본론으로는 추상적일 수 있다. |

## Story Flow

| Segment | Purpose | Notes |
|---|---|---|
| Hook | "AI로 만든 데모가 왜 실제 서비스가 되지 못할까?" | 시청자의 경험을 바로 호출한다. |
| Source Setup | Build with AI 12부작 소개 | 전체 소개는 짧게, 이 영상은 Part 4, 5, 7, 10, 11을 중심으로 간다고 설명한다. |
| Barrier 1 | 문제 정의가 불명확하다 | 사용자가 누구이고 어떤 반복 문제를 해결하는지 정리해야 한다. Source: Part 5, Part 6. |
| Barrier 2 | 데이터와 워크플로가 준비되지 않았다 | AI 성능보다 입력 데이터와 업무 맥락이 병목이 된다. Source: Part 4. |
| Barrier 3 | 검증과 운영 기준이 없다 | 예측 불가능한 입력, 비용, 지연, 신뢰, 할루시네이션을 다뤄야 한다. Source: Part 10, Part 11. |
| Builders Lounge Bridge | 혼자 만드는 데모에서 커뮤니티 기반 검증으로 | Product Discovery와 Bila AI Agent 연결. Source: Part 3, Part 7. |
| Close | 다음 단계 예고 | Build with AI를 바탕으로 실제 영상/프로덕트 실험을 시작한다. |

## Scope Boundary

이번 영상에서 다룰 것:

- 데모와 서비스의 차이
- 문제 정의의 중요성
- 데이터/context 병목
- 검증과 운영 기준
- Builders Lounge/Bila AI Agent로 이어지는 커뮤니티 검증 아이디어

이번 영상에서 깊게 다루지 않을 것:

- Build with AI 12부작 전체 상세 요약
- 모든 AI 도구 비교
- 실제 n8n Agent 구현 튜토리얼
- Claude Code, Cursor, Codex 세부 사용법
- Physical AI와 다음 물결 전망

## Builders Lounge and Bila Bridge

[[Ingest/CatchUpAI_VL/Topics/Material_For_Topics/Bila_AI_Agent/bila_agent_project_plan#Phase 2 — 멤버 매칭 (Product 모니터링 & 자동 연결)|Bila AI Agent 구축 플랜]]은 멤버가 막힌 지점을 감지하고 유사한 경험을 가진 사람을 연결하는 시나리오를 제시한다. 이 구조는 Build with AI의 "혼자 데모를 만드는 단계"를 넘어 "다른 사람의 피드백과 검증으로 서비스 기준을 갖추는 단계"로 확장하는 데 쓸 수 있다.

이 bridge는 본론을 침범하지 않게 마지막 1~2분에 배치한다. 핵심은 "서비스화의 벽을 혼자 넘으려 하지 말고, 커뮤니티와 Agent를 통해 검증 루프를 만들자"이다. Builders Lounge는 데모와 프로덕션 사이의 작은 파일럿 환경이 될 수 있고, Bila AI Agent는 멤버의 Product 상태와 막힌 지점을 context로 관리하는 시스템이 될 수 있다.

## Review Decision

사용자 리뷰가 필요한 결정은 이 영상이 Build with AI 전체 소개 영상인지, 아니면 "데모에서 서비스로 넘어가는 벽"이라는 문제 중심 영상인지이다. 현재 추천은 후자이며, Build with AI 전체 소개는 영상 안의 신뢰 배경으로 짧게 처리하는 것이다.

### 승인 질문

1. 첫 영상 제목을 **"AI로 데모는 만들었는데, 왜 서비스는 안 될까?"**로 확정할 것인가?
2. Build with AI 12부작 전체 소개는 60초 이내의 source setup으로 제한할 것인가?
3. Builders Lounge/Bila AI Agent 연결은 본론이 아니라 마지막 bridge로 배치할 것인가?

## M2 DoD Check

아래 체크는 초안 기준이다. 정식 M2 DoD는 사용자 승인 후 다시 검토한다.

- [x] 타깃 시청자가 구체적으로 정의되었다.
- [x] 추천 angle이 1개로 좁혀졌다.
- [x] 대체 angle이 보류 사유와 함께 기록되었다.
- [x] 영상 segment별 목적이 표로 정리되었다.
- [x] Bila AI Agent 연결이 본론을 침범하지 않게 배치되었다.
- [x] 사용자 리뷰 결정 사항이 명시되었다.
