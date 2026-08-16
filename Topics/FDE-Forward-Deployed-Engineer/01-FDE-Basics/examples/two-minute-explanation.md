# FDE 2분 설명문

## 한국어 설명문

FDE는 Forward Deployed Engineer의 약자입니다. 직역하면 "현장에 전진 배치된 엔지니어"인데, 실제 의미는 고객사 가까이에 들어가서 고객의 문제를 자사 기술로 실제 작동하는 시스템으로 만들어 주는 엔지니어입니다.

일반 소프트웨어 엔지니어는 보통 회사 내부 제품을 만듭니다. 솔루션 엔지니어는 고객에게 제품을 설명하고 기술 검증을 돕는 경우가 많습니다. 컨설턴트는 문제를 분석하고 전략을 제안합니다. FDE는 이 세 역할의 일부를 모두 갖고 있지만, 핵심은 직접 구현하고 production까지 가져간다는 점입니다.

AI 시대에 FDE가 중요해진 이유는 AI 데모와 실제 기업 적용 사이의 간극이 크기 때문입니다. ChatGPT나 LLM API로 멋진 demo를 만드는 것은 쉬워졌지만, 기업의 실제 데이터, 보안, 권한, 업무 프로세스, 기존 시스템에 붙이는 것은 훨씬 어렵습니다. FDE는 고객의 업무를 이해하고, 어떤 AI use case가 진짜 가치가 있는지 찾고, RAG, agent, API, eval, workflow automation을 조합해서 실제 업무에 쓰이게 만듭니다.

예를 들어 OpenAI의 FDE는 frontier model을 고객의 production system에 배포하고, discovery부터 technical scoping, system design, build, rollout까지 책임집니다. Cursor의 FDE는 고객 개발팀에 들어가 대규모 refactor, migration, PR review loop 같은 개발 workflow를 AI-native하게 바꿉니다. Scale AI의 FDE는 AI data infrastructure와 evaluation 문제를 고객 환경에 맞게 해결합니다.

따라서 FDE는 단순한 AI 영업이나 기술 지원이 아닙니다. 고객 현장에서 문제를 정의하고, 코드를 쓰고, 시스템을 배포하고, 사용자가 실제로 쓰게 만들고, 그 경험을 다시 제품 개선으로 연결하는 신흥 직무입니다.

## English version

FDE stands for Forward Deployed Engineer. It refers to an engineer who works close to the customer, understands real operational problems, and turns the company's product, platform, or AI capability into a working production system in the customer's environment.

The role sits between software engineering, consulting, solutions engineering, and product work. A typical software engineer mostly builds the internal product. A solutions engineer often supports demos, validation, and technical sales. A consultant may define the problem and recommend a strategy. An FDE is different because they are expected to scope, build, deploy, and drive real adoption.

The role is becoming more important in AI because the gap between a demo and production is large. It is easy to build a prototype with an LLM. It is much harder to connect that prototype to enterprise data, permissions, security requirements, existing systems, evaluation metrics, and real user workflows. AI FDEs bridge that gap.

In practice, an AI FDE might help a customer identify a high-value workflow, design the system architecture, build a RAG or agent-based workflow, create evals, integrate APIs and internal tools, deploy the solution, monitor adoption, and bring field feedback back to the product and research teams.

So FDE is not just sales, support, or consulting. It is a hands-on, customer-facing engineering role focused on turning advanced technology into measurable production impact.

## 30초 요약

FDE는 고객 현장에 들어가 자사 기술을 고객의 실제 업무 시스템으로 만들어 주는 엔지니어다. AI 시대에는 LLM, agent, RAG, eval, workflow automation을 고객 데이터와 보안 환경에 맞게 붙여 production adoption을 만드는 역할로 확장되고 있다. 단순 데모나 컨설팅이 아니라, 문제 정의부터 구현, 배포, 사용 정착, 제품 feedback까지 책임지는 hybrid engineering role이다.

## 연습 과제

### 과제 1: 청중별 설명 바꾸기

같은 FDE 설명을 아래 세 청중에게 맞게 다시 써 본다.

| 청중 | 강조할 포인트 |
|---|---|
| 대학생/주니어 | 어떤 역량을 준비해야 하는지, 일반 SWE와 무엇이 다른지 |
| IT 시니어 | 기존 SI/컨설팅/엔지니어링 경험을 어떻게 FDE로 전환할 수 있는지 |
| 비IT 도메인 전문가 | 도메인 지식이 어떻게 AI workflow 설계와 연결될 수 있는지 |

### 과제 2: 30초 pitch 만들기

아래 빈칸을 채워 30초 pitch를 만든다.

```text
FDE는 _______ 문제를 가진 고객과 함께 일하면서,
_______ 기술을 고객의 실제 _______ 안에 넣고,
단순 demo가 아니라 _______까지 책임지는 역할입니다.
AI 시대에 이 역할이 중요한 이유는 _______ 때문입니다.
```

### 과제 3: 오해 바로잡기

다음 질문에 각각 2문장으로 답한다.

- FDE는 그냥 기술 영업 아닌가요?
- FDE는 SI 개발자와 뭐가 다른가요?
- 비전공자도 FDE가 될 수 있나요?
- AI FDE에게 코딩은 어느 정도 필요한가요?

## 자기 평가

- [ ] 30초, 2분, 5분 버전으로 FDE를 설명할 수 있다.
- [ ] 청중에 따라 설명의 강조점을 바꿀 수 있다.
- [ ] FDE를 둘러싼 흔한 오해 3가지를 바로잡을 수 있다.
- [ ] AI FDE가 미국 취업시장에서 왜 새로운 직무군으로 보이는지 설명할 수 있다.
