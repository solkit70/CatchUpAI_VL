---
title: "Architecture Diagrams - Vibe Guiding"
created: 2026-05-10 06:32:59
tags:
  - vibe-guiding
  - architecture
  - mermaid
  - gobi-cli
sources:
  - "[[Ingest/CatchUpAI_VL/Topics/Vibe-Guiding-VSCode/02-Architecture-Design/component-responsibilities#컴포넌트 책임표|Component Responsibilities]]"
  - "[[Ingest/CatchUpAI_VL/Topics/GOBI-CLI/vl_worklog/20260510_CVL_GOBI-CLI#GOBI CLI v2.0 주요 변경사항|GOBI CLI CVL WorkLog]]"
---

## 전체 아키텍처

Vibe Guiding은 `Build the Brain`과 `Activate the Brain`을 분리한다. Build 단계는 최신 매뉴얼을 만드는 과정이고, Activate 단계는 사용자의 현재 문제를 보고 그 매뉴얼을 실행 가능한 안내로 바꾸는 과정이다.

```mermaid
flowchart LR
    subgraph Build["Build the Brain: Vibe Manual/CVL"]
        A[GOBI CLI Topic Docs] --> B[CVL Update]
        B --> C[Manual Builder]
        C --> D[manual_index.json]
        B --> E[known_failures.md]
    end

    subgraph Activate["Activate the Brain: Guiding Engine"]
        F[User Context] --> G[Trigger Evaluator]
        H[Problem Signal] --> G
        G --> I[Retriever]
        D --> I
        E --> I
        I --> J[Guide Composer]
        J --> K[guide_response.md]
    end
```

## Vibe Manual/CVL 흐름

이 흐름은 GOBI CLI v2.0.12처럼 대상 기술이 바뀔 때 기존 학습 산출물을 어떻게 최신 매뉴얼로 유지할지 보여준다.

```mermaid
flowchart TD
    A[Detect Change] --> B{Major Command Change?}
    B -- Yes --> C[Read CVL WorkLog]
    B -- No --> D[Patch Affected Guide]
    C --> E[Update Topic Guides]
    E --> F[Update Module README]
    F --> G[Extract Manual Entries]
    D --> G
    G --> H[manual_index.json]
    H --> I[Retrieval-ready Vibe Manual]
```

핵심 산출물은 사람에게 읽히는 문서와 AI가 검색할 수 있는 index가 함께 존재하는 상태다. v2.0.12 변경에서는 `gobi init`, `BRAIN.md`, `Thread` 같은 구 표현이 남아 있으면 Retrieval이 잘못된 안내를 만들 수 있으므로 CVL 결과가 index에 반영되어야 한다.

## Guiding Engine 실행 흐름

이 흐름은 사용자가 GOBI CLI 작업에서 막혔을 때 어떤 순서로 안내가 만들어지는지 보여준다.

```mermaid
sequenceDiagram
    participant U as User
    participant C as Context Collector
    participant T as Trigger Evaluator
    participant R as Retriever
    participant G as Guide Composer
    participant M as Manual Index

    U->>C: problem_signal 입력
    C->>C: gobi --version / auth status / space list
    C->>T: user_context.json
    T->>T: trigger_rules.json 평가
    T->>R: 필요한 안내 유형
    R->>M: 관련 manual entry 검색
    M-->>R: source docs + completion signals
    R->>G: retrieval result
    G-->>U: guide_response.md
```

## 파일 흐름

```mermaid
flowchart TD
    A[user_context.json] --> D[evaluate_trigger.py]
    B[problem_signal.md] --> D
    C[trigger_rules.json] --> D
    D --> E[trigger_decision.json]
    F[manual_index.json] --> G[retrieve_manual.py]
    E --> G
    G --> H[retrieval_result.json]
    H --> I[compose_guide.py]
    A --> I
    I --> J[guide_response.md]
```

## M2 설계 기준

다이어그램의 모든 흐름은 `manual_index`, `user_context`, `trigger_rules`, `guide_response`를 포함해야 한다. 이 네 파일은 M4 POC의 최소 계약이며, 이 계약이 지켜지면 이후 Desktop/Applet 시나리오도 같은 방식으로 확장할 수 있다.
