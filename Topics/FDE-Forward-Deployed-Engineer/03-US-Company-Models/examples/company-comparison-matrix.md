# 미국 AI 기업별 FDE 비교 매트릭스

## 1. 비교 기준

이 비교표는 M2에서 만든 기준을 사용한다.

| 기준 | 질문 |
|---|---|
| 고객 유형 | 누구의 문제를 푸는가? |
| 핵심 기술 | 어떤 기술이 중심인가? |
| 업무 범위 | discovery부터 rollout까지 어디까지 책임지는가? |
| 코딩 비중 | production code를 직접 쓰는가? |
| 제품 환류 | field signal이 product/research roadmap에 반영되는가? |
| 성공 지표 | 무엇으로 성공을 측정하는가? |
| 요구 경력 | entry/new grad 가능한가, senior 중심인가? |
| 현장성 | onsite/travel/embedded 요구가 얼마나 강한가? |

## 2. 회사별 요약 매트릭스

| 회사 | 직무명/계열 | Archetype | 고객 유형 | 핵심 기술 | 업무 범위 | 코딩 비중 | 성공 지표 |
|---|---|---|---|---|---|---|---|
| Palantir | FDSE, Deployment Strategist | Operational Platform FDE | 정부, 국방, 산업, 공급망, 헬스케어 등 mission-critical 조직 | data platform, custom app, pipeline, LLM workflow | open-ended problem 이해부터 production solution까지 | 높음 | operational impact, customer outcome |
| OpenAI | Forward Deployed Engineer, Forward Deployed Software Engineer | AI Lab FDE | 전략 고객, 정부, enterprise domain/engineering teams | frontier models, API, full-stack, evals, security | discovery, scoping, design, build, rollout, roadmap feedback | 높음 | production adoption, workflow impact, eval-driven feedback |
| Anthropic | Applied AI Architect, Applied AI Engineer, FDE 계열 | Applied AI Architect / Advisor | large enterprise, enterprise tech, public sector, startups | Claude API, Claude for Work, evals, architecture, safety/reliability | discovery, evaluation, architecture, deployment guidance | 중간, role별 차이 큼 | Claude adoption, architecture quality, eval success, customer success |
| Scale AI | FDE GenAI, Forward Deployed AI Engineer, Enterprise | Data·Agent Infrastructure FDE | AI labs, enterprise, government agencies | data engine, RLHF, eval, ETL, cloud, agents, RAG | customer data/infrastructure 이해부터 agent/model deployment까지 | 높음 | reliable AI application, data/eval quality, production deployment |
| Cursor | Forward Deployed Engineer | Developer Workflow FDE | customer engineering teams, Staff+/Platform/Eng leaders | Cursor workflows, Python/TypeScript, evals, tracing, model debugging | bottleneck discovery부터 workflow launch, hardening, support까지 | 높음 | day-30 workflow change, production-grade AI coding workflow |
| Hebbia | Forward Deployed Engineer | Vertical Workflow FDE | finance, investment, banking, asset management customers | platform integrations, workflow automation, data connectors, production code | strategic account embed, last-mile build, product feedback | 높음 | customer workflow value, platform indispensability, reusable patterns |

## 3. 회사별 상세 분석

### 3.1 Palantir

Palantir는 FDE의 원형에 가깝다. FDSE는 고객의 open-ended operational question을 data, custom app, production solution으로 바꾼다. Deployment Strategist는 고객 workflow, 데이터 의미, 사용자 동기, impact 지점을 구조화하고 FDE와 함께 pipeline, workflow, adoption을 만든다.

**지원자에게 주는 의미**:
Palantir형을 목표로 하면 단순 coding test 준비만으로는 부족하다. 모호한 문제를 구조화하고, 고객 현장에 들어가며, data와 application을 엮어 operational outcome을 만드는 경험을 보여줘야 한다.

**참조**:
- [Palantir FDSE New Grad - Commercial](https://jobs.lever.co/palantir/2e6b0ac8-83e9-4be5-a3aa-cf319f751728)
- [Palantir FDSE New Grad - US Government](https://jobs.lever.co/palantir/cbe90327-3e6e-451c-a54c-1d3cbcef5aeb)
- [Palantir Deployment Strategist - Korea Forward Deployed](https://jobs.lever.co/palantir/1a53939d-8ffa-4570-b31a-6d0bc53fdb59)

### 3.2 OpenAI

OpenAI의 FDE는 frontier model을 전략 고객의 production system으로 가져가는 역할이다. 공고는 discovery, technical scoping, system design, build, production rollout을 명시하고, 성공을 production adoption, measurable workflow impact, eval-driven feedback으로 측정한다고 설명한다.

**지원자에게 주는 의미**:
OpenAI형을 목표로 하면 LLM/generative model을 production system으로 배포한 경험이 중요하다. Python/JavaScript full-stack, customer-facing deployment, eval, model behavior 이해, security/GRC 협업 감각이 필요하다.

**참조**:
- [OpenAI FDE - Seattle](https://openai.com/careers/forward-deployed-engineer-%28fde%29-seattle-seattle/)
- [OpenAI Forward Deployed Software Engineer](https://openai.com/careers/forward-deployed-software-engineer-sf-san-francisco/)

### 3.3 Anthropic

Anthropic은 Applied AI 조직 아래 Applied AI Architect, Applied AI Engineer, Solutions Architect, FDE 계열 role을 운영한다. Applied AI Architect 공고는 Claude adoption을 돕는 pre-sales architect 성격이 강하고, customer discovery, evaluation, architecture design, Claude API/Claude for Work integration guidance를 강조한다.

**지원자에게 주는 의미**:
Anthropic형은 "FDE"라는 이름보다 Applied AI/Solutions Architecture 언어로 접근해야 한다. 직접 production code를 오래 소유하는 역할인지, pre-sales technical advisory 역할인지 공고별로 구분해야 한다. 강한 technical communication, enterprise architecture, eval 설계 역량이 중요하다.

**참조**:
- [Anthropic Applied AI Architect, Enterprise Tech](https://job-boards.greenhouse.io/anthropic/jobs/5065835008)
- [Anthropic careers](https://www.anthropic.com/careers/jobs)

### 3.4 Scale AI

Scale AI의 FDE는 data/eval/agent infrastructure에 강하다. GenAI FDE는 leading AI labs와 government agencies의 AI data 문제를 해결하고, full-stack systems와 customer/operator-specific infrastructure를 만든다. Senior Forward Deployed AI Engineer는 customer data pipeline, cloud, data warehouse, internal API, AI agent, multi-agent system, eval framework까지 다룬다.

**지원자에게 주는 의미**:
Scale형을 목표로 하면 data engineering, cloud, ETL, enterprise integration, LLM agent, eval framework가 강해야 한다. 단순 AI app demo보다 고객 데이터 환경과 production infrastructure에 대한 이해가 중요하다.

**참조**:
- [Scale AI FDE, GenAI](https://scale.com/careers/4593571005)
- [Scale AI Senior Forward Deployed AI Engineer](https://job-boards.greenhouse.io/scaleai/jobs/4597399005)

### 3.5 Cursor

Cursor의 FDE는 고객 개발팀에 embed되어 production-grade Cursor workflow를 만드는 역할이다. 공고는 large-scale refactor, migration, PR review loop, incident-to-fix pipeline, spec-to-implementation system 같은 개발 workflow를 예시로 들고, tracing, evals, metrics, model behavior debugging, latency/cost tradeoff를 production quality 요소로 본다.

**지원자에게 주는 의미**:
Cursor형은 developer productivity와 platform engineering 감각이 중요하다. 고객도 엔지니어이므로 code credibility가 필요하고, AI coding workflow를 실제 조직에 rollout하는 경험이 강점이다.

**참조**:
- [Cursor FDE](https://cursor.com/careers/forward-deployed-engineer)
- [Cursor RVP Forward Deployed Engineering](https://cursor.com/de/careers/rvp-forward-deployed-engineering-emea)

### 3.6 Hebbia

Hebbia의 FDE는 전략 고객에게 embed되어 platform의 last mile을 고객 workflow, data, domain에 맞게 만든다. 특히 finance/investment domain에서 AI가 capital deployment, risk management, value creation workflow에 들어가도록 custom integrations, workflow automation, domain-specific solution을 만든다.

**지원자에게 주는 의미**:
Hebbia형은 domain expertise와 production engineering의 결합이 중요하다. 금융/투자/법률처럼 지식 집약적 workflow를 이해하고, 고객 데이터와 문서 시스템에 platform을 깊게 붙이는 경험이 유리하다.

**참조**:
- [Hebbia FDE](https://jobs.ashbyhq.com/hebbia-ai/b35852eb-97ac-491a-b375-91fd13d0b7b3/)

## 4. 공통 요구 역량 Top 10

| 순위 | 역량 | 설명 |
|---:|---|---|
| 1 | 모호한 문제 구조화 | 고객이 명확한 요구사항을 주지 않아도 문제를 scope로 바꾸는 능력 |
| 2 | production-grade engineering | prototype을 실제 운영 가능한 시스템으로 만드는 능력 |
| 3 | customer-facing communication | engineering team, domain user, executive와 모두 대화하는 능력 |
| 4 | full-stack 또는 broad technical range | frontend, backend, data, infra 중 필요한 부분을 넘나드는 능력 |
| 5 | AI/LLM application understanding | LLM, RAG, agent, eval, model behavior를 이해하는 능력 |
| 6 | data integration | 고객 데이터, API, data warehouse, internal system을 연결하는 능력 |
| 7 | eval/metrics thinking | 성공 기준과 품질 평가 체계를 만드는 능력 |
| 8 | security/compliance awareness | enterprise/government 환경의 제약을 고려하는 능력 |
| 9 | field-to-product feedback | 고객 현장 학습을 reusable pattern이나 product feedback으로 바꾸는 능력 |
| 10 | autonomy and judgment | 빠르고 모호한 환경에서 trade-off를 결정하는 능력 |

## 5. 지원자 관점의 빠른 매칭

| 지원자 배경 | 잘 맞는 archetype | 이유 |
|---|---|---|
| SWE + enterprise integration 경험 | OpenAI, Scale, Hebbia | production code와 고객 시스템 통합 경험이 직접 연결된다. |
| Data engineer / ML platform engineer | Scale, Palantir | data pipeline, infra, eval, platform 역량이 강점이다. |
| Developer productivity / platform engineer | Cursor | 고객 개발팀의 workflow 병목을 잘 이해할 수 있다. |
| Solutions architect / sales engineer | Anthropic, OpenAI adjacent | technical advisory, eval, architecture communication이 강점이다. |
| Consultant / SI project lead | Palantir, Anthropic, Scale | 문제 구조화와 stakeholder management가 강점이지만 coding/AI production gap을 보완해야 한다. |
| Finance/legal domain + engineering | Hebbia, vertical AI startups | domain workflow 이해가 큰 차별점이다. |

## 6. 빈칸 비교 실습

아래 표를 직접 채운다. 원문 매트릭스를 보지 않고 먼저 작성한 뒤, 다시 비교한다.

| 회사 | 고객 유형 | 핵심 기술 | 업무 범위 | 코딩 비중 | 성공 지표 | Archetype |
|---|---|---|---|---|---|---|
| Palantir | | | | | | |
| OpenAI | | | | | | |
| Anthropic | | | | | | |
| Scale AI | | | | | | |
| Cursor | | | | | | |
| Hebbia | | | | | | |

## 7. 분석 실습

### 실습 1: 가장 engineering-heavy한 회사 고르기

아래 질문에 답한다.

- production code ownership이 가장 강해 보이는 회사는 어디인가?
- 그 근거는 무엇인가?
- 이 회사에 지원하려면 어떤 portfolio가 필요한가?

### 실습 2: 가장 advisory-heavy한 회사 고르기

아래 질문에 답한다.

- architecture/advisory 성격이 가장 강해 보이는 회사는 어디인가?
- 이 role이 FDE와 겹치는 부분은 무엇인가?
- 이 role이 FDE와 다른 부분은 무엇인가?

### 실습 3: 내 배경과 연결하기

아래 문장을 완성한다.

```text
내 현재 배경은 _______에 가깝다.
따라서 가장 잘 맞는 FDE 유형은 _______이다.
하지만 해당 유형에서 요구하는 _______ 역량이 부족하므로,
포트폴리오에서는 _______ 프로젝트를 만들어 보완해야 한다.
```

## 8. 자기 평가

- [ ] 회사별 FDE 차이를 고객 유형 기준으로 설명할 수 있다.
- [ ] 회사별 FDE 차이를 기술 스택 기준으로 설명할 수 있다.
- [ ] 회사별 FDE 차이를 성공 지표 기준으로 설명할 수 있다.
- [ ] 내 배경에 맞는 FDE archetype을 하나 선택하고 근거를 말할 수 있다.

## 9. 결론

미국 AI 기업의 FDE는 하나의 표준 직무가 아니라 기업의 제품, 고객, GTM 전략에 따라 다른 형태로 나타난다. 지원자는 먼저 자신이 "모델 배포형", "데이터/agent infrastructure형", "개발 workflow형", "vertical workflow형", "technical advisory형" 중 어디에 가까운지 판단해야 한다. 그 다음에 기술 스택과 포트폴리오를 맞춰야 한다.
