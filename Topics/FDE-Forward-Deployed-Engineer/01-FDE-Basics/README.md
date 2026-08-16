# M1 - FDE 기본 정의와 역사

**상태**: 완료
**예상 학습 시간**: 3시간
**Topic**: FDE-Forward-Deployed-Engineer

## 학습 순서

1. [concepts/fde-definition.md](concepts/fde-definition.md) - FDE의 기본 정의와 AI 시대 의미를 학습한다.
2. [concepts/fde-history-timeline.md](concepts/fde-history-timeline.md) - Palantir식 원형에서 AI FDE로 확장된 흐름을 시간순으로 정리한다.
3. [examples/two-minute-explanation.md](examples/two-minute-explanation.md) - 비전공자와 취업 준비생에게 설명할 수 있는 2분 설명문을 연습한다.

## 모듈 목표

- FDE를 2문장으로 정의할 수 있다.
- FDE가 software engineer, consultant, solutions engineer와 다른 지점을 설명할 수 있다.
- AI 시대에 FDE가 다시 주목받는 이유를 3가지로 정리할 수 있다.

## 핵심 요약

FDE는 고객 가까이에 배치되어 실제 업무 문제를 파악하고, 자사 제품이나 AI 플랫폼을 고객 환경에 맞게 설계·구현·배포하는 엔지니어다. 전통적인 엔지니어가 제품 내부 개발에 집중한다면, FDE는 고객 현장의 모호한 문제를 production 시스템과 measurable adoption으로 연결한다.

AI 시대의 FDE는 특히 LLM, agent, RAG, eval, workflow automation, enterprise data integration을 고객의 실제 업무 안에 넣는 역할로 확장되고 있다. 그래서 단순 데모나 pre-sales가 아니라, 고객과 함께 문제를 정의하고 코드와 시스템으로 결과를 만드는 hybrid engineering role로 이해해야 한다.

## 학습 활동

### 활동 1: FDE 정의 재작성

1. [concepts/fde-definition.md](concepts/fde-definition.md)를 읽는다.
2. "FDE는 무엇인가?"에 대한 답을 한국어 2문장, 영어 2문장으로 다시 쓴다.
3. 작성한 문장에 다음 요소가 들어갔는지 확인한다.
   - 고객 현장성
   - 직접 구현
   - production adoption
   - 제품/모델 feedback loop

### 활동 2: FDE가 아닌 것 구분하기

다음 문장이 FDE 설명으로 충분한지 판단한다.

| 문장 | 판단 기준 |
|---|---|
| "AI 솔루션을 고객에게 설명하는 사람" | 설명만 있고 production ownership이 없으면 부족하다. |
| "고객 요구사항을 받아 개발하는 외주 개발자" | 고객 outcome과 product feedback loop가 없으면 부족하다. |
| "LLM API로 빠르게 demo를 만드는 사람" | demo에서 production으로 가는 과정이 빠져 있으면 부족하다. |
| "고객 workflow를 이해하고 AI 시스템을 배포해 실제 사용되게 만드는 사람" | FDE 정의에 가깝다. |

### 활동 3: 2분 설명 연습

1. [examples/two-minute-explanation.md](examples/two-minute-explanation.md)의 30초 요약을 먼저 읽는다.
2. 비전공자에게 설명한다고 가정하고 2분 설명을 소리 내어 읽는다.
3. 설명 후 아래 질문에 답할 수 있어야 한다.
   - FDE와 컨설턴트는 무엇이 다른가?
   - FDE와 Solutions Engineer는 무엇이 다른가?
   - 왜 AI 시대에 FDE가 더 중요해졌는가?

## Self-Assessment

- [ ] FDE를 2문장으로 정의할 수 있다.
- [ ] FDE를 AI 솔루션 영업, 컨설턴트, 일반 software engineer와 구분할 수 있다.
- [ ] AI demo와 production adoption의 차이를 설명할 수 있다.
- [ ] Palantir 원형에서 AI FDE로 확장된 이유를 말할 수 있다.
- [ ] OpenAI, Scale AI, Cursor 사례를 각각 다른 유형의 FDE로 설명할 수 있다.

## Definition of Done

- [x] FDE 정의 문서 작성
- [x] 역사 타임라인 작성
- [x] 2분 설명문 작성
- [x] README에 학습 순서와 문서 링크 정리
- [x] 학습 활동과 Self-Assessment 보강
- [x] WorkLog 작성

## 이전/다음 모듈

- 이전 모듈: 없음
- 다음 모듈: `../02-Palantir-Origin/`
