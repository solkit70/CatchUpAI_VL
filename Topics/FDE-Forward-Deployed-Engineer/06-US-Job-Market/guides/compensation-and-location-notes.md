# Compensation and Location Notes

**조사일**: 2026-08-16
**진행 방식**: 사용자 승인 후 VibeLearn AI M6 재진행

## 핵심 관찰

FDE 계열 공고의 compensation은 role title보다 seniority, company stage, customer segment, technical depth에 더 강하게 묶인다. 같은 "FDE"라도 OpenAI의 Seattle FDE, OpenAI FDSWE, Anthropic FDE, Scale Frontier Agents Engineer는 역할 중심축이 다르기 때문에 단순 salary range 비교만으로 우열을 판단하면 안 된다.

## 확인된 보상 범위

| Company | Role | Location | Public Range | 해석 |
|---|---|---|---|---|
| OpenAI | FDE, Seattle | Seattle | $162K-$280K + equity | 5+ years, production adoption ownership, travel up to 50% |
| OpenAI | Forward Deployed Software Engineer | San Francisco | $185K-$325K + equity | 7+ years, custom full-stack software builder, FDE와 함께 delivery |
| OpenAI | FDE, Gov | DC / Seattle / SF | $145.8K-$280K + equity | public sector, TS/SCI 또는 equivalent, cloud/IaC 요구 |
| Anthropic | FDE | NYC / SF / Seattle | $280K-$320K | 4+ years, founding FDE motion, Claude production workflows |
| Anthropic | Applied AI Engineer, Enterprise Tech | SF / NYC / Seattle | $200K-$320K | advisor + implementation + evals + workshops |
| Scale AI | Frontier Agents Engineer (FDE) | SF / NYC | $180K-$225K | 4+ years, production agent systems |
| Scale AI | Senior Frontier Agents Engineer (FDE) | SF / NYC | $252K-$315K | 5+ years, senior production agent systems |

Cursor FDE와 일부 adjacent roles는 2026-08-16 확인 시 public salary range를 안정적으로 확인하지 못했다. 따라서 보상표에는 원문에서 range를 확인한 OpenAI, Anthropic, Scale AI 공고만 포함했다.

## Location / Travel 판독

| 조건 | 의미 | 지원자 판단 |
|---|---|---|
| Hybrid 3 days/week | 회사 사무실 기반 collaboration이 중요하다 | relocation 가능성과 출퇴근 현실성을 먼저 확인한다 |
| Up to 50% travel | 고객 현장 delivery와 executive/customer workshop 비중이 높다 | 가족/건강/비자/생활 리듬상 감당 가능한지 따진다 |
| Potential 25% travel | 고정 travel보다 engagement별 onsite build 가능성을 의미한다 | 고객 onsite workshop 사례를 준비한다 |
| Remote included | remote-only 보장은 아니다 | 공고 하단의 team/location policy를 다시 확인한다 |
| TS/SCI clearance | public sector 또는 national security 고객 접근 조건이다 | clearance가 없으면 commercial FDE로 우회하는 편이 현실적일 수 있다 |

## Seniority 해석

"4+ years"나 "5+ years"는 단순 연차가 아니라 독립적으로 고객 문제를 받아 production path를 설계할 수 있는 최소 신호로 읽어야 한다. FDE 면접에서는 years보다 다음 증거가 더 중요하다.

| 신호 | 강한 증거 |
|---|---|
| 4+ years | 작은 제품/시스템을 독립적으로 ship하고 고객 또는 내부 stakeholder와 trade-off를 조율한 경험 |
| 5+ years | ambiguous enterprise problem을 scope, architecture, rollout plan으로 바꾼 경험 |
| 7+ years | scratch부터 production까지 여러 시스템을 설계하고 reusable abstraction으로 만든 경험 |
| Senior/Staff | 고객 account의 technical strategy, architecture review, production risk, team leverage까지 책임진 경험 |

## 지원 전략

### OpenAI형

OpenAI형 공고는 customer delivery와 core platform/product/research feedback loop를 동시에 본다. resume에는 "built X"만 쓰지 말고 "deployed X into customer workflow, measured Y adoption/impact, fed Z signal back into product" 구조로 써야 한다.

### Anthropic형

Anthropic형은 Claude ecosystem과 enterprise adoption을 강하게 본다. MCP, agent skills, eval framework, safe/reliable deployment를 portfolio에 넣으면 공고 언어와 잘 맞는다.

### Scale형

Scale형은 production agent systems와 enterprise integration이 핵심이다. distributed systems, cloud, data warehouse/internal API integration, observability, guardrail, regression testing 경험을 구체적으로 보여줘야 한다.

### Cursor형

Cursor형은 고객 개발팀의 software delivery bottleneck을 AI-native workflow로 바꾸는 능력이 중요하다. codebase migration, PR review automation, incident-to-fix pipeline, spec-to-implementation workflow 같은 developer productivity portfolio가 강한 신호다.

## 보상 비교 시 주의점

1. Base salary만 보지 말고 equity, bonus, location adjustment, travel burden을 함께 봐야 한다.
2. Public range는 넓고, 실제 offer는 level, location, interview performance, competing offer에 따라 달라진다.
3. Gov/public sector role은 compensation보다 clearance, mission context, security obligation이 fit을 크게 좌우한다.
4. Remote 표기가 있어도 customer onsite, office policy, travel expectation이 별도로 붙을 수 있다.
5. 높은 보상 범위는 대체로 ambiguity, customer pressure, production accountability도 함께 높다는 뜻이다.

## Source Notes

- OpenAI FDE Seattle: https://openai.com/careers/forward-deployed-engineer-%28fde%29-seattle-seattle/
- OpenAI FDSWE SF: https://openai.com/careers/forward-deployed-software-engineer-sf-san-francisco/
- OpenAI FDE Gov: https://openai.com/careers/forward-deployed-engineer-gov-washington-dc/
- Anthropic FDE: https://job-boards.greenhouse.io/anthropic/jobs/5302966008
- Anthropic Applied AI Engineer: https://job-boards.greenhouse.io/anthropic/jobs/5057647008
- Scale Frontier Agents Engineer: https://job-boards.greenhouse.io/scaleai/jobs/4694861005
- Scale Senior Frontier Agents Engineer: https://job-boards.greenhouse.io/scaleai/jobs/4694863005
