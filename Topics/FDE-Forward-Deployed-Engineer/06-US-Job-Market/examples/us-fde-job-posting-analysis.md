# US FDE Job Posting Analysis

**조사일**: 2026-08-16
**진행 방식**: 사용자 승인 후 VibeLearn AI M6 재진행
**범위**: 미국 중심 FDE 및 유사 Applied AI/customer-facing engineering 공고
**주의**: 채용 공고는 수시로 바뀐다. 이 문서는 2026-08-16에 확인 가능한 공개 페이지 기준의 학습용 스냅샷이다.

## 분석 기준

각 공고는 다음 질문으로 추출했다. Title은 표면 신호이고, 더 중요한 것은 업무 동사다. `own`, `embed`, `deploy`, `integrate`, `evaluate`, `codify`, `advise`, `support production` 같은 동사가 반복되면 FDE 성격이 강하다.

| 분석 항목 | 판독 질문 |
|---|---|
| Role ownership | discovery부터 production rollout까지 소유하는가? |
| Technical depth | full-stack, cloud, infra, eval, agent, RAG 중 어디까지 요구하는가? |
| Customer context | 고객과 직접 일하고 조직 내 ambiguity를 다루는가? |
| Product feedback | field signal을 product/research roadmap으로 되돌리는가? |
| Operating constraints | hybrid, travel, clearance, domain background가 필요한가? |

## 공고 분석표

| # | Company | Role | Location | Years | Core Stack / Skills | Domain Signal | Travel / Onsite | Salary Signal | Role Archetype |
|---:|---|---|---|---:|---|---|---|---|---|
| 1 | OpenAI | Forward Deployed Engineer (FDE) | Seattle | 5+ | Python, JavaScript, full-stack production code, LLM deployment, eval feedback | Strategic customers, research/product/GRC/security/GTM collaboration | Hybrid 3 days/week, up to 50% travel | $162K-$280K + equity | Production adoption owner |
| 2 | OpenAI | Forward Deployed Software Engineer | San Francisco | 7+ | Full-stack custom software, Postgres/MySQL, OpenAI APIs, scalable abstractions | Customer problems, account team collaboration | Hybrid 3 days/week, up to 50% travel | $185K-$325K + equity | Builder paired with FDE motion |
| 3 | OpenAI | Forward Deployed Engineer, Gov | Washington DC / Seattle / SF | 5+ | Python, JavaScript, Azure/AWS, Kubernetes, Terraform, LLM systems | Government, defense, intelligence, public sector | Hybrid 3 days/week, up to 50% travel | $145.8K-$280K + equity | Cleared public-sector deployment owner |
| 4 | Anthropic | Forward Deployed Engineer | NYC / SF / Seattle | 4+ | Python, TypeScript/Java, LLM production, agents, eval frameworks, MCP, agent skills | Strategic enterprise customers, Applied AI | 25% office baseline, potential 25% travel | $280K-$320K | Claude enterprise adoption FDE |
| 5 | Anthropic | Applied AI Engineer, Enterprise Tech | SF / NYC / Seattle | 4+ | Python/TypeScript, prompt engineering, agents, evals, transcript analysis, MCP | Digital native businesses adopting Claude API | 3 days/week office, occasional travel | $200K-$320K | Technical product advisor |
| 6 | Scale AI | Frontier Agents Engineer (FDE) | SF / NYC | 4+ | Python, distributed systems, cloud, LLM APIs, agent frameworks, MCP, RAG, vector DBs | Enterprise AI agents across finance, healthcare, manufacturing, media, telecom, government | Location-based office role | $180K-$225K | Production agent systems engineer |
| 7 | Scale AI | Senior Frontier Agents Engineer (FDE) | SF / NYC | 5+ | Same as Scale FDE plus senior production ownership | Enterprise production agent systems | Location-based office role | $252K-$315K | Senior production agent systems engineer |
| 8 | Scale AI | Forward Deployed Engineer, GenAI | SF / NYC | 2+ preferred | Full-stack features, data infrastructure, rapid experiments, customer/operator-specific infrastructure | Data engine for model builders and government agencies | Hybrid team in SF or NYC | Not visible on scraped page | GenAI data infrastructure FDE |
| 9 | Cursor | Forward Deployed Engineer | SF / NY / Remote | Not explicit in captured listing | Python, TypeScript/JavaScript, Cursor workflows, tracing, evals, model debugging, latency/cost tradeoffs | Customer engineering teams, developer productivity | SF / NY / Remote | Not visible in captured listing | Developer workflow transformation FDE |
| 10 | Cursor | Field Engineer / AI Adoption / Deployment adjacent roles | SF / NY / global variants | Varies | Field engineering, adoption, deployment, customer success, developer workflows | Enterprise Cursor adoption | Varies by region | Not analyzed role-by-role | Adjacent GTM technical roles |

## 공통 역량 Top 10

1. **Production-grade engineering**: 공고 대부분이 prototype이 아니라 stable production, scalable solution, production application을 말한다.
2. **Customer-facing technical delivery**: 고객 engineering/product/domain 팀과 직접 일한 경험이 반복된다.
3. **Ambiguity scoping**: 불완전한 요구사항에서 scope, sequence, trade-off를 잡는 능력이 핵심이다.
4. **Full-stack fluency**: Python과 JavaScript/TypeScript, frontend/backend, database, APIs를 넘나드는 generalist 성향이 강하다.
5. **LLM and agent implementation**: LLM API, agent framework, MCP, RAG, vector DB, prompt engineering, model behavior debugging이 자주 등장한다.
6. **Evals and quality systems**: evaluation framework, golden dataset, regression suite, LLM-as-a-Judge, tracing, observability가 강한 신호다.
7. **Enterprise integration**: cloud, data warehouse, internal APIs, identity/permission, customer infrastructure에 연결하는 능력이 필요하다.
8. **Security and governance**: government, public sector, GRC, compliance, guardrails, grounding, safety 요구가 여러 공고에 나온다.
9. **Reusable pattern codification**: 한 고객 프로젝트를 internal tools, playbooks, reusable building blocks, product feedback으로 전환해야 한다.
10. **Executive and engineer communication**: customer engineer와 deep technical discussion을 하면서 leadership/stakeholder에게 trade-off와 impact를 설명해야 한다.

## 회사별 해석

### OpenAI

OpenAI FDE는 frontier model을 고객의 production system으로 옮기는 end-to-end owner에 가깝다. Seattle FDE 공고는 discovery, scoping, system design, build, rollout, production adoption, eval-driven feedback, product/model roadmap 영향까지 한 사람이 연결한다는 점이 핵심이다. Gov FDE는 여기에 TS/SCI clearance, government stakeholder, Azure/AWS/Kubernetes/Terraform 같은 public-sector deployment 조건이 추가된다.

### Anthropic

Anthropic은 FDE를 Applied AI 팀 안의 enterprise deployment motion으로 설명한다. FDE 공고에는 MCP servers, sub-agents, agent skills, production workflows 같은 Claude ecosystem 특화 산출물이 나온다. Applied AI Engineer는 FDE와 유사하지만 customer portfolio advisor, workshop, code review, public/internal asset creation 성격이 더 강하다.

### Scale AI

Scale의 Frontier Agents Engineer는 FDE와 Applied AI를 합친 production agent systems role이다. enterprise environment 안에서 cloud, data warehouse, internal API, business application, proprietary software와 agent를 연결하고, eval harness, tracing, guardrails, monitoring까지 운영해야 한다. title은 FDE지만 요구 역량은 distributed systems + AI infra + customer engineering에 가깝다.

### Cursor

Cursor FDE는 개발팀의 실제 software delivery workflow를 바꾸는 역할이다. large-scale refactor, migration, PR review loop, incident-to-fix pipeline, spec-to-implementation system 같은 개발 조직 내부 use case가 중심이다. 따라서 일반 enterprise AI FDE보다 developer productivity, codebase context, model behavior debugging, rollout monitoring이 중요하다.

## 접근 제한 및 신뢰도 메모

- OpenAI, Anthropic, Scale AI 공고는 2026-08-16에 본문과 주요 요구사항을 직접 확인했다.
- Scale GenAI FDE는 Scale careers 페이지에서 본문 일부를 확인했으나 salary range는 페이지에 노출되지 않았다.
- Cursor FDE는 직접 open 시 안정적으로 본문을 가져오지 못해 검색 캐시와 Cursor careers listing을 함께 사용했다. 따라서 salary와 years는 확인된 값으로 쓰지 않았다.

## Fit 판단 규칙

| 후보자 배경 | 강한 Fit 공고 | 보완해야 할 약점 |
|---|---|---|
| Full-stack/product engineer + customer exposure | OpenAI FDE, OpenAI FDSWE, Cursor FDE | evals, enterprise deployment, stakeholder storytelling |
| Backend/distributed systems engineer | Scale Frontier Agents Engineer | customer discovery, product impact narrative |
| Solutions architect / sales engineer with coding depth | Anthropic Applied AI Engineer, FDE | production code proof, portfolio demo |
| Public sector / defense engineer | OpenAI Gov FDE | clearance, cloud/IaC, LLM deployment examples |
| Data/ML engineer | Scale GenAI/FDE, Anthropic Applied AI | full-stack UX and customer workflow mapping |

## Source Notes

- OpenAI Forward Deployed Engineer (Seattle): https://openai.com/careers/forward-deployed-engineer-%28fde%29-seattle-seattle/
- OpenAI Forward Deployed Software Engineer (SF): https://openai.com/careers/forward-deployed-software-engineer-sf-san-francisco/
- OpenAI Forward Deployed Engineer, Gov: https://openai.com/careers/forward-deployed-engineer-gov-washington-dc/
- Anthropic Forward Deployed Engineer: https://job-boards.greenhouse.io/anthropic/jobs/5302966008
- Anthropic Applied AI Engineer, Enterprise Tech: https://job-boards.greenhouse.io/anthropic/jobs/5057647008
- Scale AI Frontier Agents Engineer (FDE): https://job-boards.greenhouse.io/scaleai/jobs/4694861005
- Scale AI Senior Frontier Agents Engineer (FDE): https://job-boards.greenhouse.io/scaleai/jobs/4694863005
- Scale AI Forward Deployed Engineer, GenAI: https://scale.com/careers/4593571005
- Cursor Forward Deployed Engineer: https://cursor.com/careers/forward-deployed-engineer
- Cursor Careers listing: https://cursor.com/en-US/careers
