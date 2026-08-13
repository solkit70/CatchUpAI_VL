---
title: "What Is Vibe Guiding"
created: 2026-05-03 07:32:15
tags:
  - vibe-guiding
  - concept
  - vibelearn-ai
  - gobi
sources:
  - "[[Ingest/CatchUpAI_VL/Topics/Materials_For_Topics/Idea/Vibe_Guiding/VibeGuiding_BrainDump|VibeGuiding_BrainDump]]"
  - "[[Ingest/CatchUpAI_VL/Topics/GOBI-Guiding/2026-04-05 Vibe Guiding 구현 계획#Context|2026-04-05 Vibe Guiding 구현 계획]]"
  - "[[Ingest/CatchUpAI_VL/Topics/GOBI-Guiding/2026-04-13 Gobi Desktop Vibe Guiding 기능 수준 테스트#2. 테스트 결과 및 분석|2026-04-13 Gobi Desktop Vibe Guiding 기능 수준 테스트]]"
---

## 30초 설명

Vibe Guiding은 Vibe Learning으로 만든 최신 매뉴얼을 사용자의 현재 상황에 맞게 활성화하는 안내 시스템이다. 단순히 문서를 검색해서 답하는 것이 아니라, 사용자의 수준, 설정 상태, 막힌 지점, 제품 버전을 보고 지금 필요한 안내를 단계별로 제공한다. GOBI에서는 이 방식으로 Gobi Desktop, Space, CLI 같은 제품 사용 중 발생하는 혼란을 감지하고, 정확한 매뉴얼 근거와 완료 신호가 있는 가이드를 제공하는 것이 목표다.

## 3분 설명

Vibe Learning은 특정 Topic에 대해 AI와 함께 학습하고 실습하면서 교과서 품질의 산출물을 만드는 방법론이다. [[Ingest/CatchUpAI_VL/Topics/Materials_For_Topics/Idea/Vibe_Guiding/VibeGuiding_BrainDump|VibeGuiding_BrainDump]]에서는 이 산출물이 사람에게는 매뉴얼이 되고 AI에게는 잘 정리된 context가 된다는 점에서 Vibe Guiding의 출발점을 찾는다.

Vibe Guiding은 이 매뉴얼을 정적인 문서로 남겨두지 않고, 특정 사용자의 현재 상황에서 필요한 부분만 꺼내 안내로 바꾸는 레이어다. 그래서 핵심 질문은 "무엇을 알고 있는가"가 아니라 "지금 이 사용자에게 무엇을 알려줘야 작업이 끝나는가"가 된다. [[Ingest/CatchUpAI_VL/Topics/GOBI-Guiding/2026-04-05 Vibe Guiding 구현 계획#2-1. Guiding 엔진 설계|Vibe Guiding 구현 계획]]은 이 구조를 User Context와 Vibe Manual이 결합되어 Just-in-time 맞춤 안내를 만드는 흐름으로 설명한다.

GOBI 적용에서 Vibe Guiding은 제품 문서, specs, 소스코드, 사용자 환경 정보를 연결해야 한다. [[Ingest/CatchUpAI_VL/Topics/GOBI-Guiding/2026-04-13 Gobi Desktop Vibe Guiding 기능 수준 테스트#⚠️ 발견된 한계점 (Blockers)|Gobi Desktop 기능 수준 테스트]]는 기존 AI 안내가 대화는 가능했지만, Vault Path나 Applet 경로 같은 실제 상태를 반영하지 못해 작업 완수에 실패했다는 점을 보여준다. 따라서 Vibe Guiding의 품질은 답변 문장 자체보다 context 수집, trigger 판단, retrieval 근거, completion signal의 정확성에서 결정된다.

## Vibe Learning vs Vibe Guiding

| 구분 | Vibe Learning | Vibe Guiding |
|---|---|---|
| 주 목적 | 사용자가 Topic을 학습하고 이해하도록 돕는다 | 사용자가 현재 작업을 끝낼 수 있도록 안내한다 |
| 핵심 산출물 | Roadmap, 학습 문서, 실습 결과, WorkLog | 사용자 상황 기반 guide response, trigger log, scenario test |
| 문서의 역할 | 사람이 학습하는 교과서 품질 자료 | AI가 안내에 사용하는 최신 context |
| 시간 흐름 | 세션 단위 학습 계획과 진행 | 사용자가 막히는 순간의 Just-in-time 안내 |
| 사용자 상태 | 학습 수준과 진도 중심 | OS, 앱 버전, 설정값, 문제 신호, 숙련도 중심 |
| 성공 기준 | 사용자가 개념을 설명하고 실습 산출물을 만든다 | 사용자가 안내를 따라 실제 작업을 완료한다 |

## GOBI 적용 예시

사용자가 Gobi Desktop에서 Custom Homepage/Applet을 만들다가 "어디에 파일을 둬야 하는지 모르겠다"고 말하면, 일반 챗봇은 Applet 개념을 설명하거나 예시 코드를 줄 수 있다. Vibe Guiding은 먼저 사용자의 OS, Gobi Desktop 버전, vault path, applet 폴더 존재 여부, 기존 설정 상태를 확인한 뒤, 현재 버전에 맞는 경로와 다음 실행 단계를 안내한다. 마지막에는 "파일이 인식되었는지", "홈페이지가 실제로 바뀌었는지" 같은 완료 신호를 확인하게 하고, 실패하면 fallback 경로를 제시한다.

## 문서 검색 챗봇과 다른 점

Vibe Guiding은 문서 검색 챗봇이 아니다. 문서 검색 챗봇은 질문과 유사한 문서를 찾아 요약하는 데 초점을 둔다. Vibe Guiding은 사용자의 현재 상태를 먼저 보고, 가이드가 필요한 순간인지 판단한 뒤, 관련 매뉴얼을 선택하고, 사용자가 바로 실행할 수 있는 순서와 완료 신호로 재구성한다.

## M1 잠정 정의

Vibe Guiding은 Vibe Learning으로 생성되고 CVL로 최신성을 유지하는 Vibe Manual을, 사용자 상태와 problem signal에 맞춰 적시에 실행 가능한 안내로 바꾸는 시스템이다. 이 정의는 M2의 컴포넌트 분리, M3의 Vibe Manual Schema, M4의 Guiding Engine POC에서 계속 검증한다.
