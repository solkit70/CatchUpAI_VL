# FDE 정의

## 1. 한 문장 정의

**Forward Deployed Engineer(FDE)는 고객 현장 가까이에 배치되어 고객의 실제 업무 문제를 파악하고, 자사 제품·플랫폼·AI 모델을 고객 환경에 맞게 설계, 구현, 배포, 정착시키는 엔지니어다.**

AI 분야에서 FDE는 특히 LLM이나 agent 같은 AI 기술을 고객의 데이터, 보안 조건, 업무 프로세스, 기존 시스템과 연결하여 실제 production adoption으로 만드는 역할을 한다. 여기서 핵심은 "AI를 소개하는 것"이 아니라 "AI가 고객 업무 안에서 반복 사용되고 성과를 내게 만드는 것"이다.

## 2. OpenAI식 정의에서 보이는 핵심

OpenAI의 FDE 채용 설명은 이 역할을 customer delivery와 core platform development의 교차점에 둔다. FDE는 discovery, technical scoping, system design, build, production rollout을 소유하고, 성공 기준은 production adoption, workflow impact, eval-driven feedback이다.

이 설명에서 중요한 점은 세 가지다. 첫째, FDE는 연구 결과나 모델 기능을 고객의 production 시스템으로 옮긴다. 둘째, 고객 engineering/domain team과 직접 협업한다. 셋째, 현장에서 얻은 feedback이 product와 model roadmap에 영향을 준다.

Source: [OpenAI FDE - Seattle](https://openai.com/careers/forward-deployed-engineer-%28fde%29-seattle-seattle/)

## 3. Scale AI식 정의에서 보이는 핵심

Scale AI의 GenAI FDE는 AI data infrastructure를 고객과 operator에게 맞게 만들고, leading AI labs와 government agencies의 복잡한 AI data 문제를 해결하는 역할로 설명된다. 여기서는 FDE가 full-stack feature, infrastructure, large-scale data processing, cloud, enterprise customer collaboration에 가까운 역할을 맡는다.

즉 Scale AI의 FDE는 "frontier model 자체를 고객에게 붙이는 사람"이라기보다, 고품질 데이터와 평가, alignment, AI application infrastructure를 고객 문제에 맞게 제공하는 engineer에 가깝다.

Source: [Scale AI FDE, GenAI](https://scale.com/careers/4593571005)

## 4. Cursor식 정의에서 보이는 핵심

Cursor의 FDE는 고객 engineering team에 embedded되어 production-grade Cursor workflow를 만든다. 여기서 고객은 일반 비즈니스 부서가 아니라 개발 조직이며, FDE가 해결하는 문제는 large-scale refactor, migration, PR review loop, incident-to-fix pipeline, spec-to-implementation workflow 같은 개발 생산성 문제다.

이 유형의 FDE는 developer tool adoption에 특화되어 있다. AI coding tool을 단순히 설치하게 하는 것이 아니라, 고객 개발팀의 실제 병목을 찾아 AI-native engineering workflow로 바꾸는 역할이다.

Source: [Cursor FDE](https://cursor.com/careers/forward-deployed-engineer)

## 5. FDE와 비슷하지만 다른 직무

| 직무 | FDE와의 차이 |
|---|---|
| Software Engineer | 보통 내부 제품 개발 중심이다. FDE는 고객 현장 문제와 production adoption까지 책임진다. |
| Solutions Engineer | demo, pre-sales, technical validation 비중이 큰 경우가 많다. FDE는 실제 구현과 배포 책임이 더 크다. |
| Consultant | 문제 정의와 전략 제안에 강하지만, FDE는 production-grade code와 system delivery가 핵심이다. |
| ML Engineer | 모델 개발·학습·평가에 집중하는 경우가 많다. AI FDE는 모델을 고객 업무 시스템에 넣고 운영되게 만드는 쪽에 가깝다. |
| Product Manager | 문제와 방향을 정의하지만 직접 코딩하지 않는 경우가 많다. FDE는 scope를 잡고 직접 build까지 수행한다. |

## 6. FDE에 대한 흔한 오해

### 오해 1: FDE는 기술 영업이다

FDE는 고객과 가까이 일하지만, 핵심 책임은 영업 설명이 아니라 production impact다. Sales Engineer나 Solutions Engineer가 sales cycle에서 제품의 기술적 가치를 설명하는 경우가 많다면, FDE는 고객 workflow 안에서 실제로 작동하는 시스템을 만들고 사용되게 한다.

### 오해 2: FDE는 SI 개발자다

FDE는 고객별 custom work를 하지만, 단순 외주 구현과는 다르다. FDE는 자사 제품이나 플랫폼의 경계를 고객 현실에 맞게 확장하고, 그 과정에서 얻은 반복 패턴을 product feature, playbook, eval, reusable component로 되돌린다.

### 오해 3: FDE는 AI demo를 빨리 만드는 사람이다

AI demo를 빠르게 만드는 능력은 필요하지만 충분하지 않다. FDE의 진짜 역량은 demo 이후의 데이터 연결, 권한, eval, security, rollout, adoption, monitoring을 다루는 데 있다.

## 7. 핵심 용어

| 용어 | 의미 |
|---|---|
| Forward deployed | 고객 현장 또는 고객 workflow 가까이에 배치되어 문제를 직접 해결하는 방식 |
| Production adoption | 실제 사용자가 반복적으로 사용하고 업무 방식이 바뀐 상태 |
| Field signal | 고객 현장에서 발견한 실패, 요구, 반복 패턴, 제품 개선 신호 |
| Last-mile integration | 제품 기본 기능과 고객의 실제 시스템·데이터·업무 사이를 연결하는 마지막 구현 |
| Evals | AI 시스템이 업무 목표를 달성하는지 측정하는 평가 체계 |
| Workflow impact | 시스템 도입 후 실제 업무 시간, 품질, 비용, 처리량, 의사결정이 바뀐 정도 |

## 8. AI 시대에 FDE가 다시 주목받는 이유

### 이유 1: AI는 데모와 production 사이의 간극이 크다

LLM demo는 빠르게 만들 수 있지만, 실제 기업 업무에 넣으려면 데이터 권한, 보안, 평가, 비용, latency, integration, governance 문제가 생긴다. FDE는 이 간극을 현장에서 줄이는 역할이다.

### 이유 2: 기업마다 workflow와 데이터가 다르다

같은 AI 모델이라도 금융, 제조, 공공, 헬스케어, 개발 조직에서 쓰이는 방식은 다르다. FDE는 고객별 workflow를 이해하고, 제품을 그대로 밀어 넣는 대신 고객 환경에 맞게 조정한다.

### 이유 3: AI 제품 회사도 현장 feedback이 필요하다

AI 제품은 실제 사용 맥락에서 실패 유형이 드러난다. FDE는 고객 현장에서 모델이 어디서 잘 작동하고 어디서 실패하는지 관찰하고, 이를 eval, playbook, reusable component, product roadmap으로 되돌린다.

## 9. 학습용 최종 정의

FDE는 "고객 현장에 들어간 엔지니어"라는 뜻을 넘어, **고객의 모호한 업무 문제를 자사 기술로 production-grade solution으로 바꾸고, 그 과정에서 얻은 현장 신호를 제품 개선으로 되돌리는 역할**이다. AI 시대의 FDE는 이 역할을 LLM, agent, RAG, eval, data integration, workflow automation 영역에서 수행하는 신흥 직무군으로 볼 수 있다.

## 10. 확인 질문

- [ ] FDE가 Sales Engineer와 다른 이유를 production ownership 관점에서 설명할 수 있는가?
- [ ] FDE가 SI 개발자와 다른 이유를 product feedback loop 관점에서 설명할 수 있는가?
- [ ] "AI demo"와 "AI production adoption"의 차이를 예시로 설명할 수 있는가?
- [ ] OpenAI, Scale AI, Cursor의 FDE가 각각 어떤 고객 문제에 가까운지 말할 수 있는가?
