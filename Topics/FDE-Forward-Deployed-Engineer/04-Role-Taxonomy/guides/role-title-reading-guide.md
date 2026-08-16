# 직무명 읽기 가이드

## 1. 직무명보다 책임 범위를 먼저 본다

AI 기업 채용 공고에서는 같은 일을 다른 이름으로 부르거나, 같은 이름이 회사마다 다른 일을 뜻하는 경우가 많다. 따라서 title만 보고 판단하면 안 된다.

예를 들어 "Forward Deployed Engineer"라도 어떤 회사는 production coding이 핵심이고, 어떤 회사는 customer success에 더 가깝다. "Applied AI Architect"는 FDE가 아니라고 단정하기 쉽지만, 고객 discovery, eval, architecture, deployment guidance를 맡으면 FDE adjacent role이다.

## 2. 공고에서 먼저 찾아야 할 문장

### 2.1 직접 build하는가?

찾을 표현:
- build full-stack systems
- write production code
- design and implement
- deploy features across the stack
- own technical delivery

해석:
이 표현이 강하면 FDE 또는 FDSE에 가깝다. 반대로 "advise", "guide", "support", "demo" 중심이면 Solutions Architect나 Solutions Engineer에 가까울 수 있다.

### 2.2 고객과 어디까지 같이 가는가?

찾을 표현:
- embed with customers
- work directly with customer engineering teams
- customer discovery
- onsite
- strategic customers
- guide adoption

해석:
고객 접점이 강할수록 FDE에 가까워진다. 단, pre-sales discovery만 있고 production ownership이 없으면 FDE와는 다르다.

### 2.3 성공 지표가 무엇인가?

찾을 표현:
- production adoption
- measurable workflow impact
- mission impact
- real-world impact
- day-30 change
- customer outcome

해석:
성공 지표가 adoption과 workflow impact면 FDE에 가깝다. 성공 지표가 pipeline, ARR, deal conversion이면 Sales/Solutions 쪽일 가능성이 높다.

### 2.4 제품팀과 연결되는가?

찾을 표현:
- feedback to Product and Research
- generalize reusable patterns
- shape product roadmap
- codify playbooks
- contribute insights back to engineering

해석:
field signal을 product로 되돌리는 구조가 있으면 FDE의 핵심 특징이 살아 있다.

## 3. 직무명별 판독법

### Forward Deployed Engineer

먼저 production code ownership을 확인한다. FDE라는 이름이 있어도 실제로는 training/adoption/support 중심일 수 있다. "build", "deploy", "own delivery", "production"이 같이 나오면 진짜 FDE일 가능성이 높다.

### Forward Deployed Software Engineer

FDE보다 coding 비중이 더 강한 경우가 많다. 고객 문제를 직접 다루면서 software engineer 수준의 구현 책임을 기대한다. Palantir의 FDSE가 대표적이다.

### Applied AI Engineer

회사마다 의미가 크게 다르다. 내부 AI product engineer일 수도 있고, 고객-facing AI deployment engineer일 수도 있다. customer, deployment, eval, production, integration이 함께 나오면 FDE에 가깝다.

### Applied AI Architect

보통 architecture와 advisory 성격이 강하다. pre-sales인지 post-sales인지 확인해야 한다. 직접 build보다는 customer adoption journey, technical discovery, eval design, architecture guidance 중심일 수 있다.

### Solutions Engineer

demo, technical validation, PoC, sales support가 핵심인지 확인한다. production rollout을 오래 소유하지 않으면 FDE는 아니다. 다만 hands-on implementation이 강한 회사에서는 FDE와 겹칠 수 있다.

### Solutions Architect

cloud와 enterprise integration 설계에 강하다. 직접 build/deploy까지 맡는지, 아니면 architecture recommendation에 머무는지 확인한다.

### Technical Deployment Lead

delivery orchestration이 중심일 수 있다. 직접 code를 쓰는지, project/program management에 가까운지 확인해야 한다.

### AI Adoption Engineer / AI Deployment Manager

adoption과 rollout이 중심일 가능성이 높다. 기술 구현보다 enablement/change management가 강할 수 있으니 build responsibility를 확인한다.

## 4. 오판을 줄이는 체크리스트

지원 전에 아래 항목을 공고에서 표시한다.

- [ ] 직접 production code를 쓰는가?
- [ ] 고객 현장/고객 engineering team에 embed되는가?
- [ ] discovery와 scoping을 직접 하는가?
- [ ] prototype 이후 rollout과 post-production support까지 가는가?
- [ ] success metric이 customer outcome인가?
- [ ] field feedback이 product/research로 환류되는가?
- [ ] travel/onsite 요구가 있는가?
- [ ] 요구 경력이 coding-heavy인가 advisory-heavy인가?
- [ ] pre-sales인지 post-sales인지 분명한가?
- [ ] compensation 구조가 sales OTE인지 engineering salary/equity인지 확인했는가?

## 5. 판독 점수표

공고를 읽을 때 아래 항목에 0-2점을 준다. 0점은 언급 없음, 1점은 보조 책임, 2점은 핵심 책임이다.

| 항목 | 0점 | 1점 | 2점 |
|---|---|---|---|
| Customer discovery | 없음 | 일부 미팅 참여 | 직접 문제 정의와 scoping 소유 |
| Production build | 없음 | prototype 또는 script 작성 | production-grade system 구현 |
| Deployment ownership | 없음 | launch 보조 | rollout, 운영, adoption까지 책임 |
| Success metric | sales/demo 중심 | technical validation 중심 | workflow impact, adoption, customer outcome 중심 |
| Product feedback | 없음 | 고객 요청 전달 | 반복 패턴을 product/research roadmap으로 환류 |
| Ambiguity handling | 요구사항 명확 | 부분적 trade-off 판단 | 모호한 문제를 구조화하고 해결 방향 결정 |

총점 해석:

| 점수 | 판정 |
|---:|---|
| 0-4 | FDE보다는 일반 SE, SA, TAM, consultant일 가능성이 높다. |
| 5-8 | FDE-adjacent role이다. title과 책임 범위를 더 확인해야 한다. |
| 9-12 | FDE 또는 FDSE에 가까운 role일 가능성이 높다. |

## 6. 공고 해석 예시

### 예시 A: "own discovery, scoping, system design, build, production rollout"

이 문장은 매우 FDE답다. 고객 문제 정의부터 production rollout까지 책임지는 구조이기 때문이다. OpenAI FDE형에 가깝다.

### 예시 B: "trusted technical advisor, pre-sales architect, guide customers through evaluation"

이 문장은 FDE보다는 Applied AI Architect나 Solutions Architect에 가깝다. 고객-facing이지만 직접 production build ownership은 낮을 수 있다.

### 예시 C: "embed with customer engineering teams, ship production-grade workflows"

이 문장은 Developer Workflow FDE에 가깝다. Cursor형 FDE처럼 고객 개발팀의 workflow를 실제로 바꾸는 역할이다.

### 예시 D: "build data connectors, ETL pipelines, deploy AI agents within compliance boundaries"

이 문장은 Data·Agent Infrastructure FDE에 가깝다. Scale AI형 role에서 자주 보이는 패턴이다.

## 7. Mini Practice

아래 가상 공고 문장을 읽고 FDE에 가까운지 판정한다.

### Practice 1

"Partner with account executives to deliver technical demos, answer security questions, and support enterprise evaluations."

판정: Solutions Engineer 또는 Sales Engineer에 가깝다. 고객-facing은 높지만 production build와 adoption ownership이 보이지 않는다.

### Practice 2

"Work directly with customer engineering teams to scope, build, and deploy AI workflows using our platform, then feed recurring deployment patterns back into product."

판정: FDE에 가깝다. customer embedding, build/deploy, product feedback loop가 모두 보인다.

### Practice 3

"Design reference architectures for regulated enterprises adopting generative AI, guide integration strategy, and advise executives on rollout risks."

판정: Solutions Architect 또는 Applied AI Architect에 가깝다. advisory와 architecture는 강하지만 직접 production coding 책임은 약하다.

### Practice 4

"Train and evaluate retrieval models, optimize inference latency, and improve benchmark performance for internal product teams."

판정: ML Engineer 또는 Applied AI Engineer에 가깝다. 기술 구현은 강하지만 고객 현장 workflow와 adoption 책임이 보이지 않는다.

## 8. 결론

FDE 직무를 읽을 때는 title보다 "무엇을 끝까지 책임지는가"를 봐야 한다. 책임의 끝이 demo라면 FDE가 아니고, 책임의 끝이 production adoption과 measurable workflow impact라면 FDE에 가깝다. 특히 미국 AI 기업 채용시장에서는 같은 title이라도 회사별 GTM 구조와 제품 성숙도에 따라 실제 업무가 크게 달라질 수 있으므로, 공고 문장 속 동사와 성공 지표를 먼저 읽어야 한다.
