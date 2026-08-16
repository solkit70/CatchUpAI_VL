# FDE 역사 타임라인

## 개요

FDE는 갑자기 생긴 완전히 새로운 직무라기보다, enterprise software, consulting, field engineering, product engineering이 결합되며 형성된 역할이다. 다만 2020년대 중반 이후 생성형 AI가 기업 업무에 들어가면서 FDE라는 이름이 다시 강하게 부상했다.

## 타임라인

| 시기 | 변화 | FDE 관점의 의미 |
|---|---|---|
| 2000년대 후반-2010년대 | Palantir식 forward deployed model 확산 | 고객의 복잡한 데이터/운영 문제를 플랫폼 위에서 해결하는 embedded engineering 방식이 알려짐 |
| 2010년대 | Enterprise SaaS, cloud, data platform 성장 | 고객 환경에 제품을 붙이는 solutions engineering, customer engineering, professional services 역할이 커짐 |
| 2020-2022년 | AI/ML application과 MLOps 확산 | 모델을 실제 업무에 배포하고 운영하는 문제가 중요해짐 |
| 2023-2024년 | 생성형 AI와 LLM 도입 붐 | PoC는 쉬워졌지만 production adoption은 어려워져 현장형 AI engineer 수요가 커짐 |
| 2025-2026년 | OpenAI, Scale AI, Cursor, Anthropic, Hebbia 등에서 FDE/Applied AI/Field Engineering 채용 확대 | FDE가 AI 제품을 고객 workflow에 심는 신흥 직무군으로 재해석됨 |

## Palantir식 원형

Palantir의 FDE 원형은 고객의 mission-critical 문제에 엔지니어가 직접 붙어 플랫폼을 배포하고, 고객 데이터와 workflow를 운영 가능한 형태로 만드는 데 초점이 있었다. 이 모델은 전통 SI와 비슷해 보이지만, 중요한 차이는 고객별 구현을 통해 reusable product pattern을 발견하고 플랫폼을 더 강하게 만든다는 점이다.

이 원형에서 FDE는 고객 문제를 듣는 사람, 코드를 쓰는 사람, 배포를 책임지는 사람, 사용자가 실제로 쓰게 만드는 사람이 한 몸에 가깝다. 그래서 Palantir식 FDE는 "현장형 product engineer"라는 성격이 강했다.

## AI FDE로의 확장

AI FDE는 Palantir식 원형에서 몇 가지가 바뀐다. 첫째, 다루는 핵심 기술이 data platform만이 아니라 LLM, agent, eval, RAG, workflow automation으로 확장된다. 둘째, 고객사가 원하는 것은 단순 시스템 구축이 아니라 AI가 실제 업무 일부를 맡도록 만드는 것이다. 셋째, 실패 원인이 코드 버그만이 아니라 model behavior, hallucination, eval mismatch, data permission, prompt/instruction design 같은 영역으로 넓어진다.

OpenAI의 FDE 설명은 이 변화를 잘 보여준다. FDE는 frontier model deployment를 맡고, 성공 기준은 production adoption과 measurable workflow impact이며, 현장 feedback이 model/product roadmap에 연결된다. Scale AI의 FDE는 AI data infrastructure와 evaluation, enterprise/government customer collaboration에 가깝다. Cursor의 FDE는 고객 개발팀의 bottleneck을 찾아 production-grade AI coding workflow를 만드는 쪽으로 특화된다.

## 왜 2026년에 더 중요해졌나

AI 도입은 license 구매나 chatbot 배포만으로 끝나지 않는다. 기업은 "우리 데이터로", "우리 보안 체계 안에서", "우리 workflow에 맞게", "성과가 측정되는 방식으로" AI를 쓰고 싶어 한다. 이 조건이 붙는 순간 단순 sales나 support로는 부족하고, 고객과 함께 실제 시스템을 만들 수 있는 사람이 필요해진다.

FDE는 이 지점에서 등장한다. 제품 회사 입장에서는 고객 adoption과 product learning을 동시에 얻는 방법이고, 고객사 입장에서는 AI vendor의 기술을 실제 업무 성과로 바꾸는 실행 파트너다.

## M1 결론

FDE의 역사는 Palantir에서 시작된 특정 회사의 직무명으로만 보면 좁다. 더 넓게 보면 기업용 소프트웨어가 고객 현장에 깊게 들어갈수록 생기는 필연적 역할이고, 생성형 AI 시대에는 그 필요가 더 커졌다. AI가 범용 기술일수록 고객별 적용은 더 구체적이어야 하며, 바로 그 구체화를 맡는 사람이 AI FDE다.

## 학습자 실습

### 실습 1: 타임라인을 5문장으로 요약하기

아래 형식으로 FDE의 변화를 5문장으로 요약한다.

1. Palantir식 FDE는 무엇에서 출발했는가?
2. Enterprise SaaS와 cloud 시대에는 어떤 인접 직무들이 커졌는가?
3. ML/MLOps 시대에는 어떤 문제가 중요해졌는가?
4. 생성형 AI 이후에는 왜 FDE 수요가 커졌는가?
5. 2026년 현재 AI FDE는 어떤 직무군으로 재해석되고 있는가?

### 실습 2: "왜 지금 FDE인가" 답변 만들기

다음 조건을 모두 포함해 5문장 답변을 작성한다.

- AI demo와 production 사이의 간극
- 고객별 데이터와 workflow 차이
- eval/security/integration의 중요성
- 제품 회사가 field feedback을 필요로 하는 이유
- 미국 AI 기업들이 FDE 또는 유사 직무를 채용하는 흐름

## 검증 질문

- [ ] FDE가 Palantir만의 고유 직무명으로 끝나지 않고 AI 업계로 확장된 이유를 설명할 수 있는가?
- [ ] "field engineering", "solutions engineering", "product engineering"이 FDE 안에서 어떻게 결합되는지 설명할 수 있는가?
- [ ] 생성형 AI가 FDE 수요를 키운 이유를 production adoption 관점으로 설명할 수 있는가?

## 참조

- [OpenAI FDE - Seattle](https://openai.com/careers/forward-deployed-engineer-%28fde%29-seattle-seattle/)
- [Scale AI FDE, GenAI](https://scale.com/careers/4593571005)
- [Cursor FDE](https://cursor.com/careers/forward-deployed-engineer)
