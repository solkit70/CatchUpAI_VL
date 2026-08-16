# Senior Transition Map

## 핵심 질문

IT 시니어가 FDE로 전환할 때 가장 먼저 물어야 할 질문은 "나는 어떤 기술을 새로 배워야 하는가?"가 아니다. 먼저 "내 기존 경력 중 고객의 모호한 문제를 scope하고, 시스템으로 만들고, 운영/adoption까지 책임진 경험은 무엇인가?"를 찾아야 한다.

## 출신별 전환표

| 출신 | 이미 가진 강점 | FDE 관점의 gap | 보완 학습 | Target role |
|---|---|---|---|---|
| Software Engineer | production code, system design, debugging, engineering ownership | customer discovery, stakeholder communication, business impact framing | discovery interview, success metric, eval design, customer-facing writing | Forward Deployed Software Engineer, Applied AI Engineer, Cursor형 FDE |
| SI / System Integrator | 고객 환경 이해, 요구사항 조율, integration, rollout, 운영 이슈 대응 | product feedback loop, modern AI stack, reusable pattern narrative | LLM/RAG/agent, evals, cloud-native deployment, portfolio packaging | Enterprise FDE, Implementation-heavy FDE, Scale형 FDE |
| Technical PM / Program Manager | ambiguity management, stakeholder alignment, delivery sequencing, risk tracking | hands-on coding proof, AI system architecture depth | Python/TypeScript app, RAG prototype, eval dashboard, architecture memo | Technical Deployment Lead, Applied AI PM, FDE-adjacent |
| Consultant | problem framing, executive communication, change management, domain analysis | production code ownership, technical implementation credibility | AI workflow prototype, data integration basics, eval/security literacy | AI Consultant to FDE-adjacent, Solutions Architect, Applied AI Architect |
| Solutions Architect | architecture, customer communication, integration design, security discussion | direct build/deploy evidence, measurable adoption ownership | hands-on full-stack AI app, observability, regression evals | Anthropic Applied AI Engineer, Solutions/FDE hybrid, Enterprise FDE |
| Solutions Engineer | demo, technical validation, customer objection handling, pre-sales communication | post-sale production ownership, deeper engineering systems, long-term operations | production hardening, runbook, monitoring, customer feedback loop | Field Engineer, AI Deployment Engineer, FDE-adjacent |
| Data / ML Engineer | data pipeline, model/eval literacy, metrics, experimentation | customer workflow, full-stack product, deployment boundary | workflow discovery, frontend/API, security/compliance, portfolio story | Scale형 FDE, Applied AI Engineer, Data/Agent Infra FDE |

## 강점 재해석 패턴

| 기존 표현 | FDE식 재해석 |
|---|---|
| 요구사항 분석을 했다 | ambiguous customer workflow를 scoped delivery plan으로 전환했다 |
| 시스템을 구축했다 | customer problem을 production system으로 구현하고 rollout했다 |
| 장애 대응을 했다 | production risk를 감지하고 adoption impact를 보호했다 |
| 고객 커뮤니케이션을 했다 | technical trade-off를 stakeholder language로 번역했다 |
| PoC를 했다 | prototype success criteria와 production gap을 검증했다 |
| 운영 문서를 작성했다 | reusable deployment playbook과 handoff runbook을 codify했다 |

## Senior의 AI Gap

시니어가 흔히 과소평가하는 gap은 coding 기초가 아니라 AI production pattern이다. 다음 영역은 90일 안에 최소 Working 수준으로 올려야 한다.

| AI Gap | 왜 중요한가 | 최소 증거 |
|---|---|---|
| LLM/RAG/Agent | AI FDE의 핵심 구현 패턴 | 고객 workflow 기반 RAG 또는 agent demo |
| Evals | 모델 품질과 regression을 설명하는 언어 | 30-50개 eval set, scoring rubric, failure taxonomy |
| Observability | production AI failure를 감지하는 방법 | latency, cost, tool failure, retrieval failure 로그 |
| Security Boundary | enterprise 고객 신뢰의 기본 | PII, secret, permission, audit assumption 문서 |
| Product Feedback | field signal을 제품 개선으로 바꾸는 능력 | reusable pattern note 또는 product feedback memo |

## 출신별 전환 전략

### SWE 출신

SWE 출신은 coding과 system design은 강하지만 고객 현장성과 business ambiguity가 약하게 보일 수 있다. 대표 프로젝트를 "기능 개발"이 아니라 "사용자 workflow 개선"으로 다시 설명해야 한다. 특히 customer interview, adoption metric, support issue, rollout decision을 resume에 넣으면 FDE 신호가 강해진다.

### SI 출신

SI 출신은 FDE와 닮은 경험이 많다. 고객 환경, legacy system, integration, rollout, 장애 대응을 이미 겪었기 때문이다. 다만 미국 AI 기업 공고에서는 SI라는 단어 자체보다 production AI, reusable pattern, product feedback, high-agency delivery 언어로 번역해야 한다.

### PM / Program Manager 출신

PM 출신은 ambiguity, stakeholder, sequencing이 강하다. 그러나 FDE 지원에서는 직접 build 가능한 증거가 필요하다. 작은 AI workflow를 직접 구현하고 architecture note와 eval report를 붙여야 "talker"가 아니라 "builder"로 읽힌다.

### Consultant 출신

Consultant 출신은 problem framing과 executive communication이 강하다. 약점은 production accountability다. strategy deck보다 작동하는 AI workflow, deployment note, failure analysis를 만들어야 한다. 도메인 전문성이 있으면 Vertical AI FDE-adjacent 경로가 현실적이다.

### Solutions Architect 출신

Solutions Architect는 FDE와 매우 가깝지만 직접 구현 비중이 관건이다. architecture와 advisory만 강조하면 FDE보다 SA로 읽힌다. "designed and built", "coded with customer engineers", "rolled out", "measured adoption" 같은 증거가 필요하다.

## 자기진단 질문

- 최근 3년 안에 고객의 모호한 요구를 scope로 바꾼 사례가 있는가?
- 내가 직접 코드, integration, deployment 중 하나를 소유했는가?
- 결과가 production adoption 또는 workflow impact로 이어졌는가?
- 장애, 보안, 운영, rollout risk를 다룬 경험이 있는가?
- 그 경험을 reusable playbook, internal tool, product feedback으로 일반화했는가?
- LLM/RAG/agent/eval 경험을 붙이면 AI FDE narrative가 되는 프로젝트가 있는가?

6개 중 4개 이상이 "예"라면 senior FDE narrative로 재구성할 수 있다. 2개 이하라면 FDE 직행보다 FDE-adjacent role 또는 AI delivery role부터 노리는 편이 낫다.
