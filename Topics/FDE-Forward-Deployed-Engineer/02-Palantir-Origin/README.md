# M2 - Palantir 모델과 FDE의 원형

**상태**: 완료
**예상 학습 시간**: 3시간
**Topic**: FDE-Forward-Deployed-Engineer

## 학습 순서

1. [concepts/palantir-fde-origin.md](concepts/palantir-fde-origin.md) - Palantir식 FDE 원형과 Deployment Strategist와의 관계를 학습한다.
2. [examples/original-vs-ai-fde-comparison.md](examples/original-vs-ai-fde-comparison.md) - Palantir 원형과 AI FDE의 공통점·차이점을 비교한다.

## 모듈 목표

- Palantir식 FDE의 핵심 구조를 설명할 수 있다.
- Deployment Strategist와 FDE의 관계를 정리할 수 있다.
- Palantir 원형이 AI 기업 FDE와 어떻게 달라졌는지 비교할 수 있다.

## 핵심 요약

Palantir의 FDE 원형은 고객 outcome에 대한 강한 책임에서 출발한다. Palantir는 Forward Deployed Software Engineer(FDSE)를 고객의 현실에 깊이 들어가 문제를 자기 문제처럼 받아들이고, 제품의 기존 경계를 넘어 custom application, data pipeline, LLM workflow, production solution을 만드는 역할로 설명한다.

Palantir식 모델에서 FDSE와 Deployment Strategist는 한 팀으로 움직인다. FDSE가 기술 구현과 production delivery의 중심이라면, Deployment Strategist는 고객 workflow, 사용자 동기, 데이터 의미, impact 지점을 종합해 무엇을 만들고 어떻게 확산할지 정리하는 역할에 가깝다.

## 학습 활동

### 활동 1: Palantir 원형의 5대 업무 단위 재구성

1. [concepts/palantir-fde-origin.md](concepts/palantir-fde-origin.md)의 `Palantir 원형의 5대 업무 단위`를 읽는다.
2. 각 업무 단위를 한 문장으로 다시 쓴다.
3. 각 업무 단위에 대응하는 AI FDE 활동을 하나씩 적는다.

| Palantir 원형 | AI FDE 대응 활동 |
|---|---|
| Problem immersion | 고객 AI use case discovery |
| Data and workflow translation | RAG/agent workflow 설계 |
| Custom build beyond product boundary | 고객 시스템 통합과 custom tool build |
| Production ownership | eval, rollout, monitoring |
| Field-to-product learning | reusable playbook/product feedback |

### 활동 2: FDSE와 Deployment Strategist 역할 분리

다음 질문에 답한다.

- FDSE가 주로 책임지는 산출물은 무엇인가?
- Deployment Strategist가 주로 책임지는 산출물은 무엇인가?
- 두 역할이 겹치는 지점은 어디인가?
- AI FDE는 이 두 역할 중 어느 쪽에 더 가까운가, 또는 둘을 모두 포함하는가?

### 활동 3: 원형 vs AI FDE 비교 설명

1. [examples/original-vs-ai-fde-comparison.md](examples/original-vs-ai-fde-comparison.md)의 비교표를 읽는다.
2. "바뀌지 않은 것" 2개와 "바뀐 것" 2개를 고른다.
3. 각 항목을 실제 고객 프로젝트 예시로 설명한다.

## Self-Assessment

- [ ] Palantir식 FDE가 왜 FDE 논의의 원형인지 설명할 수 있다.
- [ ] FDSE와 Deployment Strategist의 차이를 말할 수 있다.
- [ ] Palantir 원형의 5대 업무 단위를 암기 없이 재구성할 수 있다.
- [ ] AI FDE가 Palantir 원형에서 이어받은 점과 새롭게 추가된 점을 구분할 수 있다.
- [ ] 다음 모듈의 기업별 FDE 비교 기준을 설명할 수 있다.

## Definition of Done

- [x] Palantir 원형 분석 문서 작성
- [x] 원형 vs AI FDE 비교표 작성
- [x] 다음 모듈에서 쓸 비교 기준 확정
- [x] README 업데이트
- [x] 학습 활동과 Self-Assessment 보강
- [x] WorkLog 작성

## 이전/다음 모듈

- 이전 모듈: `../01-FDE-Basics/`
- 다음 모듈: `../03-US-Company-Models/`
