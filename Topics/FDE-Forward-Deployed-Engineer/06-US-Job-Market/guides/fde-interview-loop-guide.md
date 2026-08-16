# FDE Interview Loop Guide

**작성일**: 2026-08-16
**근거**: 사용자 승인 후 재진행한 OpenAI, Anthropic, Scale AI, Cursor 공고 분석

## 기본 가설

FDE 면접은 일반 SWE 면접과 solutions 면접이 합쳐진 형태다. 코딩만 잘하는지보다 고객 문제를 구조화하고, 빠르게 prototype을 만들고, production으로 harden하고, 고객과 내부 product/research 팀 모두를 움직일 수 있는지가 평가된다.

## 예상 면접 루프

| Loop | 평가 대상 | 좋은 증거 |
|---|---|---|
| Recruiter screen | 동기, location, travel, salary, visa, customer-facing 선호 | 왜 FDE인지, 어떤 고객 문제를 풀고 싶은지, travel/hybrid 수용 여부 |
| Hiring manager screen | role fit, ambiguity, delivery ownership | "모호한 문제를 scope로 바꾼 경험" 2-3개 |
| Technical coding | production-grade coding, debugging, APIs, data handling | Python/TypeScript로 작은 integration 또는 workflow를 안정적으로 구현 |
| System design | enterprise AI architecture, scale, reliability, security | RAG/agent system을 권한, eval, observability, rollout까지 설계 |
| Customer scenario | discovery, trade-off, stakeholder communication | 고객 요구를 재정의하고 성공 지표와 delivery plan을 제시 |
| Portfolio demo | 실제 산출물, product sense, iteration | 작동하는 AI workflow, eval 결과, failure analysis, README |
| Bar raiser / leadership | judgment, integrity, calm under pressure | scope-speed-quality trade-off 사례, 실패를 조기에 드러낸 경험 |

## 면접별 준비 질문

### Recruiter / HM

1. 왜 SWE, Solutions Engineer, Consultant가 아니라 FDE인가?
2. 고객과 직접 일하는 환경에서 가장 잘했던 프로젝트는 무엇인가?
3. 25-50% travel 또는 hybrid 조건을 현실적으로 감당할 수 있는가?
4. 최근 LLM/agent 프로젝트 중 production에 가까운 것은 무엇인가?
5. 빠르게 prototype을 만든 뒤 production hardening까지 간 경험이 있는가?

### Technical

1. 내부 문서 API를 호출해 RAG answer를 반환하는 작은 service를 어떻게 만들겠는가?
2. Python으로 flaky external API를 안정적으로 호출하려면 retry, timeout, logging을 어떻게 설계하겠는가?
3. TypeScript frontend와 Python backend 사이의 schema mismatch를 어떻게 줄이겠는가?
4. model output이 간헐적으로 format을 어길 때 어떻게 detect하고 recover하겠는가?
5. customer data connector를 만들 때 permission boundary를 어떻게 확인하겠는가?

### System Design

1. Fortune 500 고객의 internal knowledge assistant를 6주 안에 pilot에서 production으로 옮기는 architecture를 설계하라.
2. agent가 CRM, ticketing, document store를 호출해야 할 때 tool permission과 audit log를 어떻게 구성하겠는가?
3. eval harness를 offline benchmark, online metric, human review로 나누어 설계하라.
4. latency와 cost가 목표치를 넘을 때 어떤 단계로 튜닝하겠는가?
5. model upgrade가 customer workflow를 깨뜨리지 않게 regression suite를 어떻게 운영하겠는가?

### Customer Scenario

1. 고객이 "우리 팀에 AI를 도입하고 싶다"고만 말할 때 첫 30분 discovery를 어떻게 진행하겠는가?
2. 고객 임원은 빠른 demo를 원하고 security 팀은 반대한다. 어떻게 scope를 조정하겠는가?
3. 고객 engineer가 솔루션을 신뢰하지 않는다. 어떤 evidence를 보여주겠는가?
4. pilot은 성공했지만 사용률이 낮다. adoption metric을 어떻게 다시 설계하겠는가?
5. 고객 요구가 core product roadmap과 충돌할 때 어떤 신호를 내부 팀에 전달하겠는가?

### Portfolio Demo

1. 문제 정의: 어떤 고객 workflow를 바꾸는가?
2. Before/after: 기존 업무와 AI 적용 후 workflow를 비교했는가?
3. Architecture: data source, model, tools, auth, deployment boundary가 명확한가?
4. Evals: 성공/실패 기준과 regression 사례가 있는가?
5. Operations: logging, tracing, fallback, cost/latency 측정이 있는가?
6. Narrative: 이 프로젝트가 왜 FDE 역량 증거인지 설명할 수 있는가?

## 준비 산출물

| 산출물 | 목적 |
|---|---|
| 2분 FDE pitch | recruiter/HM에게 role fit을 빠르게 설명 |
| Customer story bank | STAR 형식으로 ambiguity, delivery, conflict, adoption 사례 준비 |
| AI workflow demo | LLM/agent/RAG를 production boundary까지 고려해 보여줌 |
| Eval report | 모델 품질을 감으로 말하지 않고 측정할 수 있음을 증명 |
| Architecture one-pager | system design과 portfolio demo를 연결 |
| Role fit matrix | 회사별 공고에 맞춰 resume bullet을 바꾸기 위한 기준 |

## 평가자 관점의 위험 신호

- "LLM 써봤다" 수준에서 멈추고 production failure mode를 설명하지 못한다.
- 고객이 원하는 것을 그대로 받아 적고 scope trade-off를 하지 못한다.
- 코딩은 가능하지만 stakeholder communication evidence가 없다.
- consultant 경험은 있지만 직접 build/ship한 증거가 약하다.
- eval, security, observability를 launch 이후의 부가 작업으로 취급한다.

## AI에게 시킬 연습 프롬프트

```text
너는 미국 AI 기업의 Forward Deployed Engineer 면접관이다.
아래 프로젝트 설명을 보고 FDE 면접 기준으로 1) 강점 2) 약점 3) 추가 질문 5개 4) portfolio demo 개선안을 작성해줘.

프로젝트:
[내 AI workflow 프로젝트 설명]

평가 기준:
- customer problem framing
- production engineering
- evals and observability
- security and deployment boundary
- communication and trade-off judgment
```
