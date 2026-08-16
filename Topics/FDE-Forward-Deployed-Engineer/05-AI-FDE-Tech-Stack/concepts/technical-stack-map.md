# AI FDE Technical Stack Map

## 1. 기술 스택을 보는 기준

AI FDE는 모든 기술을 specialist 수준으로 알아야 하는 것은 아니다. 하지만 고객 현장의 문제를 production system으로 만들기 위해 각 영역의 핵심 개념, trade-off, 위험 신호를 이해해야 한다.

이 문서는 기술 스택을 세 수준으로 나눈다.

| 수준 | 의미 |
|---|---|
| Literacy | 개념을 이해하고 AI/전문가에게 정확히 지시할 수 있다. |
| Working | 직접 구현하고 디버깅할 수 있다. |
| Production | 운영, 보안, 성능, 비용, 장애 대응까지 고려해 설계할 수 있다. |

### 학습 포인트

FDE 준비자는 모든 항목을 Production 수준으로 만들려고 하면 실패한다. 먼저 목표 회사와 role archetype을 정하고, 해당 archetype에서 production risk를 직접 다루는 영역만 깊게 파야 한다. 예를 들어 Cursor형은 developer workflow, tracing, evals가 중요하고, Scale형은 data pipeline, agent infrastructure, compliance boundary가 더 중요하다.

## 2. 업무 단계별 필요한 기술

| Lifecycle 단계 | 필요한 기술 |
|---|---|
| Discovery | workflow mapping, stakeholder interview, data/source inventory, risk analysis |
| Scoping | system design, API/data feasibility, MVP design, success metric/eval design |
| Prototype | frontend, backend, LLM API, RAG, agent orchestration, simple auth, logging |
| Evals | eval dataset, scoring rubric, human review workflow, regression testing |
| Integration | API integration, ETL, data warehouse, SSO, permission model, cloud deployment |
| Rollout | observability, feature flag, monitoring, support workflow, user training |
| Handoff | documentation, runbook, ownership matrix, reusable playbook, product feedback |

## 3. 기술 영역별 지도

### 3.1 Frontend / User Interface

**필요 이유**:
고객이 실제로 workflow를 수행할 수 있는 화면이나 tool이 필요하다. FDE는 polished product designer일 필요는 없지만, usable prototype과 internal tool은 만들 수 있어야 한다.

**핵심 역량**:
- React/Next.js 또는 유사 frontend framework
- form, table, search, chat interface
- loading/error state
- feedback capture
- basic accessibility

**FDE 기준**:
Working 수준이면 충분한 경우가 많다. Developer Workflow FDE나 full-stack-heavy FDE는 Production에 가까워야 한다.

### 3.2 Backend / API

**필요 이유**:
AI workflow는 고객 데이터, internal tool, model provider, logging system을 연결해야 한다.

**핵심 역량**:
- Python/FastAPI 또는 Node/Express
- REST/GraphQL API
- authentication and authorization
- background jobs
- queue/retry/error handling
- database basics

**FDE 기준**:
대부분 Working 이상이 필요하다. OpenAI, Scale, Cursor, Hebbia형 FDE는 Production 감각이 강점이다.

### 3.3 Data Integration

**필요 이유**:
AI는 고객의 실제 문서, 업무 데이터, 시스템 상태와 연결되어야 가치가 생긴다.

**핵심 역량**:
- SQL
- ETL/ELT
- data warehouse
- document ingestion
- data quality checks
- schema mapping
- data freshness/source-of-truth

**FDE 기준**:
Scale/Palantir형은 Production 수준이 필요할 수 있다. OpenAI/Cursor형도 적어도 Working 수준은 필요하다.

### 3.4 LLM / RAG / Agent

**필요 이유**:
AI FDE의 중심 기술이다. 다만 FDE에게 중요한 것은 모델 연구보다 업무 적용 패턴이다.

**핵심 역량**:
- prompt/instruction design
- function/tool calling
- RAG pipeline
- retrieval quality
- agent orchestration
- structured outputs
- model selection
- latency/cost trade-off

**FDE 기준**:
Working 이상이 필요하다. AI Lab FDE나 Developer Workflow FDE는 Production 수준의 debugging과 evaluation 감각이 필요하다.

### 3.5 Evals

**필요 이유**:
production AI system은 품질을 측정하지 않으면 운영할 수 없다.

**핵심 역량**:
- task-specific eval design
- golden dataset
- rubric-based scoring
- human review
- regression test
- failure taxonomy
- acceptance threshold

**FDE 기준**:
모든 AI FDE가 Working 이상이어야 한다. OpenAI/Cursor/Scale형에서는 핵심 역량이다.

### 3.6 Cloud / Deployment

**필요 이유**:
prototype이 고객 환경에서 안정적으로 돌아가야 한다.

**핵심 역량**:
- Docker
- cloud basics: AWS/GCP/Azure
- environment variables/secrets
- CI/CD basics
- logging/monitoring
- scalability basics
- rollback strategy

**FDE 기준**:
Working 이상이 필요하다. infrastructure-heavy role은 Production 수준이 필요하다.

### 3.7 Security / Compliance

**필요 이유**:
기업 고객은 데이터, 권한, audit, retention, compliance 요구가 강하다. AI system은 민감한 문서와 의사결정에 접근하기 때문에 위험이 크다.

**핵심 역량**:
- authN/authZ
- SSO/SAML/OIDC 개념
- least privilege
- audit logging
- data retention
- PII/PHI/security boundary
- model provider data policy
- SOC2/GDPR/HIPAA/FedRAMP literacy

**FDE 기준**:
최소 Literacy는 필수다. government/healthcare/finance role은 Working 이상의 감각이 필요하다.

### 3.8 Observability / Operations

**필요 이유**:
AI system은 실패가 조용히 발생할 수 있다. 모델 응답 품질, latency, cost, tool call failure, retrieval failure를 관찰해야 한다.

**핵심 역량**:
- structured logging
- tracing
- metrics dashboard
- alerting
- cost monitoring
- user feedback loop
- incident/debug workflow

**FDE 기준**:
Cursor와 Scale형에서 특히 중요하다. 모든 AI FDE가 Literacy 이상은 갖춰야 한다.

## 4. 커리어 트랙별 요구 깊이

| 기술 영역 | 학생/주니어 | IT 시니어 전환 | 비IT 배경자 |
|---|---|---|---|
| Frontend | Working | Literacy-Working | Literacy |
| Backend/API | Working | Working | Literacy-초급 Working |
| Data Integration | Literacy-Working | Working-Production | Literacy |
| LLM/RAG/Agent | Working | Working | Literacy-Working |
| Evals | Working | Working | Literacy |
| Cloud/Deployment | Literacy-Working | Working | Literacy |
| Security/Compliance | Literacy | Working | Literacy |
| Customer Discovery | Working | Working-Production | Working-Production |
| Domain Workflow | Literacy | Working | Production if domain expert |

## 5. Archetype별 기술 강조점

| Archetype | 반드시 강해야 하는 영역 |
|---|---|
| Palantir형 | data integration, custom app, operational workflow, customer discovery |
| OpenAI형 | LLM app, full-stack, eval, security, production rollout |
| Anthropic형 | architecture, eval design, technical communication, safety/reliability |
| Scale형 | data pipeline, cloud, agent infrastructure, eval, enterprise integration |
| Cursor형 | developer tools, TypeScript/Python, tracing, evals, workflow automation |
| Hebbia형 | domain workflow, integrations, production code, data/document systems |

## 6. 학습 우선순위

### 우선순위 1: 모든 AI FDE 공통

- Python 또는 TypeScript 중 하나
- API integration
- LLM API 사용
- RAG 기본
- eval 기본
- 고객 workflow discovery
- production readiness checklist

### 우선순위 2: 지원 회사별 선택

- OpenAI: full-stack + eval + security
- Scale AI: data pipeline + agents + cloud
- Cursor: developer workflow + tracing + automation
- Anthropic: architecture + eval + enterprise communication
- Hebbia: domain workflow + document/data integration
- Palantir: data platform + operational app + field ownership

### 우선순위 3: 차별화 역량

- customer-facing technical communication
- domain expertise
- production incident/debugging 경험
- reusable playbook 작성
- measurable adoption metric 설계

## 7. 기술 깊이 자기진단

아래 표에 현재 수준과 목표 수준을 표시한다. 목표 수준은 지원하려는 FDE archetype에 따라 달라져야 한다.

| 기술 영역 | 현재 수준 | 목표 수준 | 다음 학습 행동 |
|---|---|---|---|
| Frontend/UI |  |  |  |
| Backend/API |  |  |  |
| Data Integration |  |  |  |
| LLM/RAG/Agent |  |  |  |
| Evals |  |  |  |
| Cloud/Deployment |  |  |  |
| Security/Compliance |  |  |  |
| Observability/Operations |  |  |  |
| Customer Discovery |  |  |  |
| Domain Workflow |  |  |  |

### 해석 기준

- 현재 수준과 목표 수준 차이가 2단계 이상이면 바로 job-ready gap이다.
- 목표 FDE archetype에서 핵심 영역이 Literacy에 머물러 있으면 포트폴리오나 실무 경험으로 보완해야 한다.
- 비핵심 영역은 AI에게 지시하고 결과를 검토할 수 있는 Literacy부터 확보한다.

## 8. Role별 기술 준비 예시

| 목표 role | 반드시 Working 이상이어야 할 영역 | Literacy로 시작해도 되는 영역 | 포트폴리오 증거 |
|---|---|---|---|
| AI Lab FDE | Backend/API, LLM/RAG, Evals, Security | Frontend, Cloud 세부 운영 | 고객 시나리오 기반 AI workflow와 eval 결과 |
| Developer Tool FDE | TypeScript/Python, developer workflow, tracing, evals | enterprise compliance | 개발팀 생산성 workflow 개선 demo |
| Data/Agent Infra FDE | Data integration, ETL, agents, cloud, observability | UI polish | 데이터 connector와 agent workflow 배포 사례 |
| Vertical AI FDE | Domain workflow, integrations, full-stack, customer discovery | 모델 연구 | 도메인 업무를 AI system으로 바꾼 case narrative |
| FDE-adjacent Architect | Architecture, eval design, security literacy, communication | hands-on frontend | production readiness review와 architecture memo |

## 9. M6로 이어지는 채용공고 읽기 질문

M6에서 미국 채용공고를 분석할 때 아래 질문을 사용한다.

- 공고가 특정 언어와 framework를 요구하는가, 아니면 system design과 customer deployment를 강조하는가?
- evals, observability, security가 명시되어 있는가?
- data connector, ETL, internal API, SSO 같은 enterprise integration 단어가 있는가?
- "production-grade", "customer infrastructure", "deployment", "rollout" 같은 표현이 있는가?
- 요구 역량이 coding-heavy인지, architecture/advisory-heavy인지, sales-support-heavy인지 구분되는가?

이 질문은 M4의 role taxonomy와 연결된다. 같은 "Applied AI Engineer" title이라도 위 질문에 대한 답이 강하면 FDE에 가까워지고, 내부 기능 개발 중심이면 product engineering에 가까워진다.

## 10. 결론

AI FDE의 기술 스택은 "LLM을 잘 쓰는 법"보다 넓다. 실제로는 고객 workflow를 이해하고, 데이터를 연결하고, AI workflow를 만들고, 평가하고, 보안과 운영 조건 안에서 배포하는 end-to-end stack이다. 좋은 준비 전략은 모든 것을 깊게 파는 것이 아니라, 목표 archetype에 맞춰 깊이를 조절하는 것이다.
