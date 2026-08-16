# 기업별 FDE Archetype

## 1. 왜 archetype으로 봐야 하는가

FDE는 아직 표준화된 직무명이 아니다. 어떤 회사에서는 production code를 직접 쓰는 field engineer에 가깝고, 어떤 회사에서는 technical advisor나 pre-sales architect에 가깝다. 따라서 "FDE가 되고 싶다"는 말은 충분하지 않다. 어떤 유형의 FDE를 목표로 하는지 구분해야 준비 전략이 정확해진다.

이 문서는 미국 AI/테크 취업시장을 중심으로 FDE 및 유사 직무를 여섯 가지 archetype으로 분류한다.

## 2. Archetype 1: Operational Platform FDE

**대표 회사**: Palantir

Operational Platform FDE는 고객의 mission-critical workflow를 데이터와 소프트웨어 플랫폼 위에 올리는 역할이다. Palantir FDSE는 고객의 현실에 embed되어 open-ended operational question을 데이터, custom application, LLM workflow, production solution으로 바꾼다.

이 유형의 핵심은 "outcome ownership"이다. 고객이 정확한 요구사항을 주지 않아도, FDE는 고객의 문제를 자기 문제처럼 받아들이고 product boundary를 넘어 해결책을 만든다.

**잘 맞는 사람**:
- 모호한 operational problem을 좋아하는 사람
- data, application, customer communication을 모두 다루고 싶은 사람
- 공공, 국방, 제조, 공급망, 헬스케어 같은 복잡한 도메인에 관심 있는 사람

**주의점**:
- travel/onsite 요구가 강할 수 있다.
- 고객 환경과 mission pressure가 크다.
- pure product engineering보다 field ownership이 훨씬 강하다.

## 3. Archetype 2: AI Lab FDE

**대표 회사**: OpenAI

AI Lab FDE는 frontier model을 고객의 production system으로 배포하는 역할이다. OpenAI FDE는 discovery, technical scoping, system design, build, production rollout을 맡고, 성공 기준은 production adoption, measurable workflow impact, eval-driven feedback이다.

이 유형의 핵심은 "research breakthrough to production system"이다. 단순히 API를 연결하는 것이 아니라, 고객의 domain team과 함께 모델이 실제 업무에 들어가도록 설계하고, field feedback을 product와 model roadmap으로 되돌린다.

**잘 맞는 사람**:
- LLM/generative AI product의 실제 배포에 관심 있는 사람
- product, research, security, GTM 사이에서 일할 수 있는 사람
- production-grade full-stack engineering과 고객 대면 업무를 모두 할 수 있는 사람

**주의점**:
- senior expectation이 높다. OpenAI FDE는 5년 이상 engineering/deployment/customer-facing 경험을 요구한다.
- travel이 최대 50%까지 요구될 수 있다.
- model behavior, eval, safety, security를 이해해야 한다.

## 4. Archetype 3: Applied AI Architect / Advisor

**대표 회사**: Anthropic

Anthropic의 Applied AI Architect는 FDE와 완전히 같은 직무는 아니지만, enterprise AI adoption의 인접 역할이다. Applied AI Architect는 대기업이 Claude를 기술 스택에 통합하고 배포할 수 있도록 technical discovery, architecture decision, eval design, technical content, customer advisory를 수행한다.

이 유형은 hands-on production coding보다 pre-sales technical architecture와 trusted advisor 성격이 강하다. 다만 Claude API, Claude for Work, eval framework, scalable architecture, product/engineering feedback을 다룬다는 점에서 AI FDE 생태계의 중요한 인접 직무다.

**잘 맞는 사람**:
- technical sales, solutions architect, enterprise customer advisory 경험이 있는 사람
- executive와 engineering team 모두에게 설명할 수 있는 사람
- LLM architecture, eval, AI safety/reliability를 고객 언어로 번역할 수 있는 사람

**주의점**:
- pure FDE처럼 직접 production code를 오래 소유하는 역할은 아닐 수 있다.
- pre-sales 성격이 강한 공고인지, post-sales deployment 성격이 강한 공고인지 반드시 구분해야 한다.
- 성과 지표가 production adoption보다 enterprise adoption journey나 deal support에 가까울 수 있다.

## 5. Archetype 4: Data·Agent Infrastructure FDE

**대표 회사**: Scale AI

Scale AI의 FDE는 GenAI data engine, evaluation, data infrastructure, enterprise AI deployment와 강하게 연결된다. GenAI FDE는 leading AI labs와 government agencies의 AI data 문제를 해결하고, full-stack feature와 infrastructure를 설계·배포한다. Senior Forward Deployed AI Engineer는 customer data pipelines, internal APIs, cloud environments, AI agents, evaluation frameworks, human-in-the-loop workflow까지 다룬다.

이 유형의 핵심은 "AI를 가능하게 하는 data·agent infrastructure"이다. 모델 자체보다 고객의 데이터와 agent workflow, evaluation, deployment boundary를 잘 다루는 능력이 중요하다.

**잘 맞는 사람**:
- data pipeline, ETL, cloud, distributed system 경험이 있는 사람
- LLM agent, RAG, evaluation framework를 production 관점에서 다루고 싶은 사람
- enterprise/government customer와 복잡한 data environment를 다루고 싶은 사람

**주의점**:
- AI application frontend만으로는 부족하다.
- cloud, data warehouse, internal API, security/compliance를 알아야 한다.
- senior role은 agent/system design 기대치가 높다.

## 6. Archetype 5: Developer Workflow FDE

**대표 회사**: Cursor

Cursor의 FDE는 고객 engineering team에 embed되어 production-grade Cursor workflow를 만든다. 고객 문제는 일반 business process가 아니라 software development workflow다. 예시는 large-scale refactor, migration, PR review loop, incident-to-fix pipeline, spec-to-implementation system 등이다.

이 유형의 핵심은 "개발 조직의 작업 방식을 AI-native하게 바꾸는 것"이다. FDE는 고객 개발팀의 병목을 찾아 success metric을 정의하고, 빠른 첫 버전을 만든 뒤, tracing, evals, metrics, debugging model behavior, latency/cost tradeoff까지 책임진다.

**잘 맞는 사람**:
- developer productivity, platform engineering, internal tools에 관심 있는 사람
- Python/TypeScript로 end-to-end workflow를 만들 수 있는 사람
- AI coding tool을 실제 팀 process에 정착시키는 데 관심 있는 사람

**주의점**:
- 고객이 엔지니어이므로 기술적 깊이와 credibility가 중요하다.
- 단순 prompt tip이나 tool training으로는 부족하다.
- production reliability, metrics, rollout, incident response 감각이 필요하다.

## 7. Archetype 6: Vertical Workflow FDE

**대표 회사**: Hebbia

Hebbia의 FDE는 금융/투자 workflow에 특화된 vertical AI platform을 고객의 workflow, data, domain에 맞게 last-mile customization하는 역할이다. 공고 설명에 따르면 FDE는 전략 고객에게 embed되어 플랫폼의 마지막 마일을 만들고, production code를 쓰고, 고객 engagement에서 배운 것을 engineering/product team으로 되돌린다.

이 유형의 핵심은 "domain workflow를 깊게 이해하고 AI platform을 indispensable하게 만드는 것"이다. 금융, 법률, 헬스케어, 제조처럼 도메인 지식이 중요한 vertical AI 회사에서 유사한 역할이 늘어날 가능성이 높다.

**잘 맞는 사람**:
- 특정 domain 지식과 software engineering을 결합하고 싶은 사람
- 고객 workflow와 data source를 깊게 파고드는 것을 좋아하는 사람
- product engineering과 GTM 사이에서 일하고 싶은 사람

**주의점**:
- domain 이해가 부족하면 고객 문제를 잘못 해석하기 쉽다.
- office/onsite 문화가 강할 수 있다.
- code quality, CI/CD, architecture alignment 등 core engineering 기준도 요구된다.

## 8. Archetype 비교 요약

| Archetype | 대표 회사 | 중심 질문 | 강한 역량 |
|---|---|---|---|
| Operational Platform FDE | Palantir | 고객 운영 문제를 데이터/플랫폼으로 어떻게 바꿀까? | data, application, field ownership |
| AI Lab FDE | OpenAI | frontier model을 production workflow에 어떻게 넣을까? | LLM, full-stack, eval, product feedback |
| Applied AI Architect / Advisor | Anthropic | Claude adoption을 enterprise architecture로 어떻게 설계할까? | architecture, eval, technical advisory |
| Data·Agent Infrastructure FDE | Scale AI | AI data/agent infrastructure를 고객 환경에 어떻게 붙일까? | data pipeline, cloud, agents, evals |
| Developer Workflow FDE | Cursor | 개발팀의 workflow를 AI-native하게 어떻게 바꿀까? | dev tools, automation, reliability |
| Vertical Workflow FDE | Hebbia | 특정 산업 workflow에 AI platform을 어떻게 심을까? | domain, integrations, production code |

## 9. Archetype 판별 질문

공고를 읽을 때 아래 질문에 답하면 어떤 archetype에 가까운지 빠르게 판단할 수 있다.

| 질문 | 답이 Yes이면 가까운 archetype |
|---|---|
| 고객 문제가 정부, 공공, 산업 운영, 공급망처럼 mission-critical operational workflow인가? | Operational Platform FDE |
| frontier model/API를 고객 production workflow에 배포하는 것이 핵심인가? | AI Lab FDE |
| pre-sales technical discovery, architecture workshop, eval design이 중심인가? | Applied AI Architect / Advisor |
| data pipeline, eval, agent infrastructure, cloud integration이 반복적으로 등장하는가? | Data·Agent Infrastructure FDE |
| 고객이 software engineering team이고 개발 workflow 개선이 핵심인가? | Developer Workflow FDE |
| 금융, 법률, 헬스케어 같은 특정 domain workflow에 깊게 들어가는가? | Vertical Workflow FDE |

## 10. 핵심 용어

| 용어 | 의미 |
|---|---|
| Archetype | 회사별 FDE 역할을 이해하기 위한 대표 유형 |
| AI Lab FDE | frontier model을 고객 production system으로 옮기는 FDE 유형 |
| Developer Workflow FDE | 개발팀의 업무 흐름을 AI-native하게 바꾸는 FDE 유형 |
| Data·Agent Infrastructure FDE | 데이터, eval, agent infrastructure를 고객 환경에 붙이는 FDE 유형 |
| Vertical Workflow FDE | 특정 산업/domain workflow에 AI platform을 깊게 적용하는 FDE 유형 |
| Applied AI Architect | FDE와 인접하지만 architecture/advisory 성격이 더 강한 역할 |

## 11. 학습자 실습

### 실습 1: 공고 문장으로 archetype 판별하기

아래 문장을 보고 가장 가까운 archetype을 고른다.

| 공고 문장 | 가장 가까운 archetype | 이유 |
|---|---|---|
| "Deploy frontier models into strategic customer production workflows." | | |
| "Build data connectors, eval pipelines, and AI agents within customer cloud environments." | | |
| "Embed with engineering teams to redesign PR review and migration workflows." | | |
| "Guide enterprises through Claude evaluation, architecture, and adoption." | | |
| "Customize platform workflows for investment research teams." | | |

### 실습 2: 내 목표 archetype 고르기

다음 세 문장을 완성한다.

```text
내가 가장 관심 있는 FDE archetype은 _______이다.
그 이유는 내가 _______ 문제를 풀고 싶고, _______ 역량을 강점으로 갖고 있기 때문이다.
하지만 현재 부족한 것은 _______이므로, 다음 3개월 동안 _______을 보완해야 한다.
```

## 12. 확인 질문

- [ ] OpenAI형 FDE와 Scale AI형 FDE의 기술 중심축 차이를 설명할 수 있는가?
- [ ] Cursor형 FDE와 Hebbia형 FDE의 고객 유형 차이를 설명할 수 있는가?
- [ ] Anthropic Applied AI Architect가 왜 FDE adjacent인지 설명할 수 있는가?
- [ ] 각 archetype별 포트폴리오 방향을 하나씩 제안할 수 있는가?

## 13. M3 결론

FDE는 하나의 직무가 아니라 "고객 현장형 AI/product engineering"이라는 큰 흐름 안의 여러 변형으로 봐야 한다. 지원자는 먼저 자신이 어느 archetype에 가까운지 판단해야 한다. 같은 FDE라도 Palantir, OpenAI, Scale AI, Cursor, Hebbia에서 요구하는 기술 깊이, 고객 유형, 성공 지표, 일하는 방식은 크게 다르다.
