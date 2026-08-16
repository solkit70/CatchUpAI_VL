# Palantir 원형 vs AI FDE 비교

## 1. 비교 요약

Palantir 원형과 AI FDE는 모두 고객 현장의 모호한 문제를 실제 시스템과 운영 성과로 바꾸는 역할이다. 차이는 중심 기술과 실패 양상에 있다. Palantir 원형은 data-driven operations와 platform deployment가 중심이고, AI FDE는 LLM, agent, eval, RAG, workflow automation이 중심이다.

## 2. 공통점

| 공통점 | 설명 |
|---|---|
| 고객 현장성 | 둘 다 고객과 가까운 위치에서 문제를 직접 관찰하고 해결한다. |
| 모호한 문제 처리 | 정해진 ticket보다 open-ended operational question에서 출발한다. |
| end-to-end ownership | discovery, scoping, build, deployment, adoption까지 넓게 책임진다. |
| 제품 경계 확장 | 기존 제품 기능만으로 부족하면 custom solution을 만든다. |
| field feedback | 현장에서 얻은 학습을 제품/플랫폼 개선으로 되돌린다. |

## 3. 차이점

| 비교 축 | Palantir 원형 FDE | AI FDE |
|---|---|---|
| 대표 기술 | data platform, ontology, pipeline, custom app, decision workflow | LLM, RAG, agent, evals, tool calling, workflow automation |
| 고객 문제 | 데이터 기반 의사결정과 운영 최적화 | AI를 실제 업무에 내재화하고 반복 사용되게 만드는 문제 |
| 실패 원인 | 데이터 품질, workflow mismatch, deployment complexity, user adoption | hallucination, eval failure, prompt fragility, latency/cost, security/compliance |
| 성공 지표 | 고객 운영 방식이 바뀌고 mission/business impact가 생김 | production adoption, measurable workflow impact, model/product feedback |
| 팀 구조 | FDSE + Deployment Strategist + product/design | FDE + product/research/security/GTM/customer engineering |
| 산출물 | data pipeline, custom app, operational dashboard, workflow | AI agent, RAG app, eval suite, integration, playbook, reusable component |
| 고객 접점 | operations, analysts, executives, public sector/enterprise teams | customer engineering, domain teams, business users, AI platform owners |

## 4. 바뀌지 않은 것

### 4.1 Outcome-first

Palantir 원형에서 가장 중요한 것은 고객 outcome이다. AI FDE도 마찬가지다. AI를 썼는지보다 고객 workflow가 실제로 개선되었는지가 더 중요하다.

### 4.2 현장 맥락 이해

FDE는 고객이 말한 요구사항만 구현하지 않는다. 고객의 workflow, 데이터, 조직 구조, 사용자의 동기, 제약 조건을 이해해야 한다.

### 4.3 직접 만드는 책임

FDE는 전략만 제안하지 않는다. 직접 만들고 배포하고 사용되게 한다. 이 점이 consultant나 pure product manager와의 핵심 차이다.

### 4.4 제품으로 되돌리는 학습

한 고객의 문제를 해결한 뒤 그것을 reusable pattern, product feature, internal playbook으로 일반화하는 흐름은 Palantir 원형과 AI FDE 모두에서 중요하다.

## 5. 바뀐 것

### 5.1 모델 행동이 새로운 변수로 들어왔다

AI FDE는 코드와 데이터뿐 아니라 model behavior를 다뤄야 한다. 같은 입력에도 불안정한 응답이 나올 수 있고, hallucination이나 instruction following 실패가 production risk가 된다.

### 5.2 eval이 핵심 산출물이 되었다

Palantir 원형에서 metric과 user adoption이 중요했다면, AI FDE에서는 eval suite가 시스템 품질의 핵심 산출물로 들어온다. AI workflow가 업무 목표를 달성하는지 측정하지 못하면 production rollout이 어렵다.

### 5.3 보안과 거버넌스가 더 복잡해졌다

AI는 내부 문서, 고객 데이터, 민감한 업무 맥락을 다루기 때문에 permission, audit, data retention, model provider boundary, compliance를 함께 설계해야 한다.

### 5.4 adoption의 단위가 workflow에서 role redesign으로 커졌다

AI FDE는 한 화면이나 dashboard를 쓰게 만드는 것을 넘어, 사람이 하던 판단·작성·검색·분류·실행 일부를 AI가 맡도록 workflow 자체를 재설계한다.

## 6. 사례형 비교

### Palantir 원형 시나리오

고객 질문: "공급망 지연을 예측하고 critical part delivery를 어떻게 보장할 수 있는가?"

FDE 접근:
1. 공급망 데이터와 운영 workflow를 파악한다.
2. 데이터셋을 정리하고 pipeline을 만든다.
3. 의사결정자가 볼 custom application이나 dashboard를 만든다.
4. 현장 사용자가 실제 운영 판단에 쓰도록 training과 iteration을 진행한다.
5. 재사용 가능한 product pattern을 내부로 환류한다.

### AI FDE 시나리오

고객 질문: "고객 지원팀이 하루 수천 건의 티켓을 더 빠르고 정확하게 처리하게 하려면 어떻게 해야 하는가?"

FDE 접근:
1. 티켓 workflow, 지식베이스, escalation rule, compliance constraint를 파악한다.
2. RAG 기반 답변 생성과 agentic triage workflow를 설계한다.
3. eval dataset과 success metric을 만든다.
4. CRM, ticketing system, internal docs와 통합한다.
5. rollout 후 hallucination, latency, cost, user override를 모니터링한다.
6. 반복 패턴을 reusable component와 product feedback으로 정리한다.

## 7. M3 분석을 위한 기준표

다음 모듈에서 기업별 FDE를 비교할 때 아래 축을 사용한다.

| 비교 기준 | 질문 |
|---|---|
| 고객 유형 | 누구의 문제를 푸는가? enterprise, government, developer team, finance user 등 |
| 핵심 기술 | data platform, LLM, RAG, agent, eval, workflow automation 중 무엇이 중심인가? |
| 업무 범위 | discovery부터 rollout까지 어디까지 책임지는가? |
| 코딩 비중 | production code를 직접 쓰는가, architecture/adoption 중심인가? |
| 제품 환류 | field signal이 product/research roadmap에 어떻게 반영되는가? |
| 성공 지표 | adoption, workflow impact, revenue, mission outcome, eval score 중 무엇을 보는가? |
| 요구 경력 | new grad 가능한가, 5년 이상 senior role인가? |
| 현장성 | onsite/travel/embedded 요구가 어느 정도인가? |

## 8. 실습 과제

### 과제 1: 비교표 빈칸 채우기

아래 표를 직접 채운다.

| 질문 | Palantir 원형 답변 | AI FDE 답변 |
|---|---|---|
| 고객이 처음 가져오는 문제는 어떤 형태인가? | | |
| FDE가 가장 먼저 확인해야 할 것은 무엇인가? | | |
| 주요 기술 실패 원인은 무엇인가? | | |
| adoption을 방해하는 요인은 무엇인가? | | |
| product team에 되돌릴 수 있는 학습은 무엇인가? | | |

### 과제 2: 바뀐 것과 바뀌지 않은 것 구분

다음 항목을 `바뀐 것` 또는 `바뀌지 않은 것`으로 분류하고 이유를 쓴다.

| 항목 | 분류 | 이유 |
|---|---|---|
| 고객 outcome 중심 | | |
| 제품 경계 밖 custom build | | |
| model hallucination | | |
| eval suite | | |
| field-to-product feedback | | |
| prompt injection/security boundary | | |

### 과제 3: 1분 설명 만들기

아래 문장을 완성한다.

```text
Palantir식 FDE와 AI FDE는 모두 _______를 책임진다는 점에서 같다.
하지만 Palantir 원형은 주로 _______를 다루고,
AI FDE는 여기에 _______ 문제가 추가된다.
그래서 AI FDE는 기존 FDE의 _______에 더해 _______ 역량이 필요하다.
```

## 9. 검증 질문

- [ ] Palantir 원형과 AI FDE의 공통점 3개를 말할 수 있는가?
- [ ] Palantir 원형과 AI FDE의 차이점 3개를 말할 수 있는가?
- [ ] AI FDE에서 eval이 왜 새 핵심 산출물이 되었는지 설명할 수 있는가?
- [ ] M3 기업별 비교 기준표의 각 항목이 왜 필요한지 설명할 수 있는가?

## 10. 결론

Palantir 원형은 FDE의 기본 문법을 만들었다. 고객의 가장 중요한 문제에 들어가고, 제품 경계를 넘어 만들고, 실제 운영 성과를 책임지고, 현장 학습을 제품으로 되돌리는 방식이다. AI FDE는 이 문법 위에 LLM, agent, eval, AI governance라는 새로운 기술 층을 얹은 역할로 이해하는 것이 가장 정확하다.
