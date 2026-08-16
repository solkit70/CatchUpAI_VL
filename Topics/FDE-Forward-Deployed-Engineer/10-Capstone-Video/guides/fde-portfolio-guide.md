# FDE 포트폴리오 가이드

## 핵심 원칙

FDE 포트폴리오는 "코드를 잘 짰다"를 보여주는 자료가 아니다. 고객 문제를 발견하고, 제약 안에서 solution scope를 잡고, 작동하는 prototype을 만들고, eval과 rollout 계획으로 production adoption 가능성을 설명하는 증거물이다. 따라서 GitHub repo 하나만으로는 부족하고, case narrative, architecture, demo script, risk checklist, adoption metric이 함께 있어야 한다.

일반 SWE 포트폴리오가 algorithm, code quality, feature completeness, UI polish를 강조한다면 FDE 포트폴리오는 customer problem, integration boundary, measurable outcome, stakeholder communication을 강조한다. 좋은 FDE 포트폴리오는 채용자가 "이 사람을 고객 현장에 보내도 문제를 구조화하고 기술팀과 고객팀 사이를 연결하겠다"고 판단하게 만든다.

## 포트폴리오 구성 요소

| 구성 요소 | 질문 | 산출물 |
|---|---|---|
| Customer Scenario | 어떤 고객이 어떤 업무 문제를 겪는가? | 1페이지 case brief |
| Workflow Map | 현재 업무 흐름과 병목은 무엇인가? | Mermaid flow 또는 단계표 |
| Architecture | 어떤 시스템, 데이터, 모델, API가 연결되는가? | architecture diagram |
| Prototype | 사용자가 실제로 무엇을 할 수 있는가? | demo app, notebook, API mock |
| Eval | 답변/추천/자동화 품질을 어떻게 측정하는가? | eval dataset, scoring rubric |
| Security Boundary | 어떤 데이터와 권한을 보호해야 하는가? | risk checklist |
| Rollout Plan | pilot에서 production adoption까지 어떻게 확장하는가? | 30/60/90 rollout plan |
| Success Metric | 성공을 어떤 수치로 판단하는가? | adoption, time saved, error reduced |

## README 구조

```markdown
# Project Name

## Customer Problem
누가 어떤 업무 문제를 겪고 있으며, 왜 지금 해결해야 하는가?

## Current Workflow
기존 업무 흐름, 병목, stakeholder, 데이터 출처를 설명한다.

## Proposed AI Workflow
AI가 어떤 판단, 검색, 요약, 분류, 추천, 자동화를 수행하는지 설명한다.

## Architecture
frontend, backend, data source, LLM, eval, observability, auth boundary를 연결한다.

## Demo Script
3-5분 안에 보여줄 사용자 시나리오를 단계별로 작성한다.

## Evaluation
정답 기준, 실패 유형, human review 기준, 개선 루프를 적는다.

## Rollout and Adoption
pilot 사용자, success metric, training, feedback loop, handoff를 설계한다.

## Risks and Trade-offs
보안, 비용, latency, hallucination, data quality, change management를 다룬다.
```

## 지원자 트랙별 포트폴리오 전략

| 지원자 유형 | 강조할 증거 | 피해야 할 약점 |
|---|---|---|
| 학생/주니어 | 작동하는 demo, README clarity, eval 사고방식 | 기술 toy project처럼 보이는 것 |
| SWE 출신 | production architecture, integration, observability | 고객 문제와 adoption 설명 부족 |
| SI/Consultant 출신 | stakeholder, rollout, enterprise constraint | hands-on artifact 부족 |
| PM 출신 | problem framing, metric, prioritization | 직접 구현 가능성 부족 |
| 비IT 도메인 출신 | domain workflow, user pain, compliance 감각 | technical minimum 부재 |

## 포트폴리오 평가 체크리스트

- [ ] 고객과 사용자가 구체적으로 정의되어 있다.
- [ ] 기존 workflow와 AI 이후 workflow가 비교된다.
- [ ] architecture가 실제 구현 가능한 수준으로 설명된다.
- [ ] eval과 실패 유형이 포함되어 있다.
- [ ] security/data boundary가 빠지지 않았다.
- [ ] rollout plan과 adoption metric이 있다.
- [ ] demo script가 3-5분 안에 전달 가능하다.
- [ ] resume bullet로 바꿀 수 있는 impact statement가 있다.

## Resume bullet 변환 공식

FDE 포트폴리오를 이력서에 쓸 때는 다음 구조를 사용한다.

```text
Designed and prototyped [AI workflow] for [customer/user scenario], integrating [data/system/model] with [evaluation/rollout mechanism], targeting [measurable business outcome].
```

예시:

```text
Designed and prototyped a compliance review copilot for financial operations teams, integrating policy retrieval, risk classification, and human-in-the-loop evaluation to reduce manual review time while preserving auditability.
```

