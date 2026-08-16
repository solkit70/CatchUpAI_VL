# FDE와 유사 직무 Taxonomy

## 1. 비교의 핵심 축

FDE와 주변 직무를 구분할 때 가장 유용한 축은 두 가지다.

1. **Customer-facing 정도**: 고객과 직접 문제를 정의하고 adoption까지 책임지는가?
2. **Production coding 정도**: 실제 production code, system integration, deployment를 직접 소유하는가?

이 두 축을 기준으로 보면 FDE는 오른쪽 위에 위치한다. 즉 고객 접점도 강하고, 직접 만드는 책임도 강하다.

### 학습자가 먼저 해야 할 질문

직무 taxonomy를 외우려고 하면 금방 헷갈린다. 먼저 "이 역할은 누구의 문제를 끝까지 책임지는가?"와 "그 책임을 코드와 시스템으로 직접 해결하는가?"를 물어야 한다. 이 두 질문에 모두 강하게 "예"라고 답할 수 있을 때 FDE에 가까워진다.

## 2. 2축 직무 지도

| 직무 | Customer-facing | Production coding | 대표 책임 | FDE와의 거리 |
|---|---:|---:|---|---|
| Forward Deployed Engineer | 매우 높음 | 높음 | 고객 문제 scope, build, deploy, adoption, feedback | 기준점 |
| Forward Deployed Software Engineer | 매우 높음 | 매우 높음 | 고객 현장 full-stack/system build | FDE의 engineering-heavy 변형 |
| Applied AI Engineer | 중간-높음 | 높음 | AI app/agent/RAG/eval 구현 | 고객 현장성이 높으면 FDE와 가까움 |
| Solutions Engineer | 높음 | 낮음-중간 | demo, technical validation, pre-sales support | 구현 책임이 낮으면 FDE와 멀어짐 |
| Sales Engineer | 높음 | 낮음 | sales cycle의 기술 설명과 objection handling | sales 중심이면 FDE와 다름 |
| Solutions Architect | 높음 | 낮음-중간 | architecture 설계, integration guidance | hands-on build 여부가 관건 |
| Consultant | 높음 | 낮음-중간 | 문제 진단, 전략, 변화관리, PMO | 직접 code/deploy가 약하면 FDE와 다름 |
| ML Engineer | 낮음-중간 | 높음 | 모델 개발, training, inference, evaluation | 고객 workflow 책임이 약하면 FDE와 다름 |
| Product Engineer | 낮음-중간 | 높음 | 제품 기능 개발과 사용자 경험 개선 | 고객 현장 embed가 약하면 FDE와 다름 |
| Technical Account Manager | 높음 | 낮음 | 고객 성공, escalation, relationship management | code ownership이 약하면 FDE와 다름 |

### 2축 지도 해석법

2축 지도에서 오른쪽 위로 갈수록 고객 현장성과 production build 책임이 동시에 커진다. 오른쪽 아래는 고객과 많이 만나지만 직접 만드는 책임이 낮은 영역이고, 왼쪽 위는 강한 엔지니어링 역할이지만 고객 현장 책임이 약한 영역이다. FDE 준비자는 자신의 경력이 어느 사분면에 있는지 먼저 파악한 다음, 부족한 축을 보완해야 한다.

## 3. 직무별 상세 비교

### 3.1 FDE

FDE는 고객 문제를 직접 파악하고, technical scoping을 하고, 필요한 시스템을 만들고, production rollout과 adoption까지 책임지는 역할이다. AI 시대에는 LLM, RAG, agent, eval, workflow automation, enterprise data integration이 업무 범위에 들어온다.

핵심 질문:
- 고객의 실제 workflow에서 어떤 문제가 가장 high-leverage인가?
- 우리 제품/모델로 어디까지 해결할 수 있고, 어디부터 custom build가 필요한가?
- prototype이 아니라 production adoption까지 가려면 무엇이 필요한가?

### 3.2 Applied AI Engineer

Applied AI Engineer는 AI application을 실제로 만드는 역할이다. RAG, agent, LLM API, eval, data integration, workflow automation을 구현한다. 고객 현장에 깊게 들어가고 deployment/adoption까지 책임지면 FDE와 매우 가까워진다.

반대로 내부 제품팀에서 AI 기능만 개발한다면 Product/ML Engineer에 더 가깝다.

### 3.3 Solutions Engineer

Solutions Engineer는 보통 sales cycle에서 고객의 기술 질문에 답하고, demo, PoC, technical validation을 돕는다. 일부 회사에서는 light integration이나 prototype도 만든다. 하지만 production system을 장기간 소유하지 않는 경우가 많다.

FDE와의 차이는 "누가 production adoption을 끝까지 책임지는가"다. Solutions Engineer가 demo와 validation에서 멈추면 FDE가 아니다. 하지만 직접 고객 환경에 들어가 build/deploy까지 하면 FDE에 가까워진다.

### 3.4 Sales Engineer

Sales Engineer는 technical sales에 더 가깝다. 제품의 기술적 가치를 설명하고, 고객의 objection을 해결하며, account executive와 함께 deal을 성사시키는 역할이다. 기술 이해는 필요하지만 success metric은 production impact보다 sales outcome에 가까운 경우가 많다.

FDE와의 차이는 incentive와 ownership이다. Sales Engineer는 deal support가 중심이고, FDE는 deployment and adoption ownership이 중심이다.

### 3.5 Solutions Architect

Solutions Architect는 고객 시스템에 제품을 어떻게 통합할지 architecture를 설계한다. cloud, security, data flow, API integration, scalability를 설명하고 설계할 수 있어야 한다.

FDE와의 차이는 직접 구현 비중이다. Solutions Architect가 설계와 guidance에 머물면 FDE보다 advisory에 가깝다. 설계 후 직접 build하고 rollout까지 소유하면 FDE와 겹친다.

### 3.6 Consultant

Consultant는 문제를 구조화하고, 전략을 세우고, 조직 변화와 실행 계획을 돕는다. AI transformation이나 AX 프로젝트에서는 consultant가 use case 발굴, roadmap, governance, change management를 맡을 수 있다.

FDE와의 차이는 engineering accountability다. FDE는 실제 시스템을 만들어야 한다. consultant 출신이 FDE로 전환하려면 coding, system integration, LLM production pattern을 보완해야 한다.

### 3.7 ML Engineer

ML Engineer는 모델 개발, training, inference, data pipeline, evaluation을 다룬다. AI FDE와 기술적으로 겹치지만, ML Engineer는 고객 workflow와 adoption보다는 model/system performance에 더 집중하는 경우가 많다.

FDE와 가까운 ML Engineer는 고객 use case에 맞게 모델을 배포하고, eval과 monitoring을 만들고, business workflow 안에서 작동하게 만든 경험이 있는 사람이다.

### 3.8 Product Engineer

Product Engineer는 사용자가 쓰는 제품 기능을 빠르게 만들고 개선한다. FDE와 같이 pragmatic하고 full-stack인 경우가 많지만, 보통 내부 product roadmap을 중심으로 움직인다.

FDE와의 차이는 고객 현장성이다. FDE는 한 고객 또는 전략 고객군의 복잡한 환경에 깊게 들어가고, 그 현장 문제를 제품으로 환류한다.

## 4. FDE 판별 질문

공고를 볼 때 아래 질문 중 "예"가 많을수록 FDE에 가깝다.

| 질문 | 왜 중요한가 |
|---|---|
| 고객 현장 또는 customer engineering team에 embedded되는가? | field role인지 판단한다. |
| discovery와 scoping을 직접 하는가? | 단순 구현자가 아닌지 판단한다. |
| production code를 직접 쓰는가? | advisory와 engineering delivery를 구분한다. |
| deployment/rollout/adoption까지 책임지는가? | PoC role과 FDE를 구분한다. |
| success metric이 workflow impact나 production adoption인가? | sales support와 구분한다. |
| product/research roadmap으로 feedback을 주는가? | field-to-product loop가 있는지 본다. |
| ambiguity와 trade-off judgment를 강조하는가? | FDE의 open-ended 환경을 반영한다. |
| travel/onsite 요구가 있는가? | forward deployed 성격을 보여준다. |

## 5. Role Taxonomy 실습

### 실습 A: 직무 분류표 채우기

아래 표를 빈칸부터 채운다고 가정하고, 각 직무가 FDE에 가까운지 판단한다.

| 직무 | 고객 문제 정의 | 직접 구현 | 배포/운영 책임 | 성공 지표 | 최종 판정 |
|---|---|---|---|---|---|
| Applied AI Engineer |  |  |  |  |  |
| Solutions Engineer |  |  |  |  |  |
| Solutions Architect |  |  |  |  |  |
| ML Engineer |  |  |  |  |  |
| Consultant |  |  |  |  |  |

판정할 때는 직무명이 아니라 책임의 끝을 본다. 책임이 demo, architecture advice, model performance에서 멈추면 FDE와 일부만 겹친다. 책임이 production adoption과 measurable customer outcome까지 이어지면 FDE에 가깝다.

### 실습 B: 흔한 오해 바로잡기

| 오해 | 더 정확한 이해 |
|---|---|
| FDE는 고객사에 파견되는 개발자다. | 고객 현장에 가는 것보다 discovery, build, deploy, adoption을 함께 책임지는지가 핵심이다. |
| Solutions Engineer가 코딩하면 FDE다. | 코딩 여부만으로는 부족하고 production ownership과 product feedback loop가 있어야 한다. |
| Applied AI Engineer는 전부 FDE다. | 고객 현장 배포와 adoption 책임이 있으면 FDE에 가깝고, 내부 제품 기능 개발이면 Product/ML Engineer에 가깝다. |
| Consultant 출신은 FDE가 되기 어렵다. | 문제 구조화와 stakeholder management는 강점이지만, coding과 AI production pattern을 보완해야 한다. |
| ML Engineer가 FDE보다 더 기술적이다. | 기술의 종류가 다르다. FDE는 모델 자체보다 고객 workflow 안에서 작동하는 end-to-end system을 책임진다. |

### 실습 C: 자기 위치 표시

본인의 최근 프로젝트 1개를 기준으로 아래 질문에 답한다.

- 고객 또는 최종 사용자를 직접 만났는가?
- 요구사항이 모호한 상태에서 scope를 잡았는가?
- 직접 코드를 쓰거나 시스템을 연결했는가?
- prototype 이후 실제 업무 사용까지 이어졌는가?
- 결과가 수치나 반복 사용으로 검증됐는가?
- 얻은 학습을 제품, playbook, reusable component로 일반화했는가?

6개 중 4개 이상이 "예"라면 FDE형 경험으로 재구성할 수 있다. 2개 이하라면 아직 FDE보다 인접 직무 경험에 가까우므로 부족한 축을 의식적으로 보완해야 한다.

## 6. M4 결론

FDE는 "고객을 만나는 개발자"도 아니고 "코딩할 줄 아는 컨설턴트"도 아니다. 고객의 모호한 문제를 scope하고, 직접 build하며, production adoption과 measurable outcome까지 책임지는 역할이다. 이 기준을 적용하면 유사 직무와의 경계가 훨씬 선명해진다.
