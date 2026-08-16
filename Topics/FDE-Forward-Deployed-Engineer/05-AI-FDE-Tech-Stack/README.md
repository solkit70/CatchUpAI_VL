# M5 - AI FDE 기술 스택과 실무 흐름

**상태**: 완료
**예상 학습 시간**: 5시간
**Topic**: FDE-Forward-Deployed-Engineer
**재점검**: 2026-08-16 daily_learning_prompt 기준 보강 완료

## 학습 순서

1. [concepts/ai-fde-delivery-lifecycle.md](concepts/ai-fde-delivery-lifecycle.md) - AI FDE 프로젝트의 discovery부터 handoff까지 전체 흐름을 학습한다.
2. [concepts/technical-stack-map.md](concepts/technical-stack-map.md) - AI FDE에게 필요한 기술 스택을 업무 단계와 커리어 트랙별로 정리한다.
3. [guides/evals-security-observability-checklist.md](guides/evals-security-observability-checklist.md) - production AI deployment에서 반드시 확인해야 할 eval, security, observability 체크리스트를 사용한다.

## 모듈 목표

- AI FDE에게 필요한 기술 스택을 업무 흐름 기준으로 설명할 수 있다.
- LLM prototype이 production deployment로 가는 단계를 설계할 수 있다.
- evals, observability, security, cost/latency trade-off의 중요성을 설명할 수 있다.
- Applied AI Engineer와 FDE의 차이를 production lifecycle ownership 관점에서 설명할 수 있다.

## 핵심 요약

AI FDE의 일은 “AI demo를 만드는 것”이 아니라 고객의 실제 workflow를 AI-enabled production system으로 바꾸는 것이다. 이 과정은 discovery, scoping, prototype, eval, integration, rollout, handoff로 진행되며, 각 단계마다 산출물과 실패 위험이 다르다.

기술 스택도 단순히 LLM API 사용법에 머물지 않는다. AI FDE는 frontend, backend, data integration, cloud deployment, identity/permission, LLM orchestration, evals, observability, security/compliance를 고객 환경에 맞게 조합해야 한다.

## 오늘의 학습 활동

### Activity 1: Demo에서 Production으로 넘어가는 gap 찾기

`concepts/ai-fde-delivery-lifecycle.md`를 읽고 각 단계마다 "demo에서는 없어도 되지만 production에서는 반드시 필요한 것"을 표시한다. 예를 들어 Prototype 단계에서는 clickable demo가 중요하지만, Integration 단계에서는 permission model, data flow, error handling이 핵심이 된다.

### Activity 2: 내 목표 role에 맞는 기술 깊이 표시

`concepts/technical-stack-map.md`의 Literacy, Working, Production 기준을 사용해 본인의 현재 수준과 목표 수준을 표시한다. OpenAI형, Scale형, Cursor형, Hebbia형 중 목표 archetype을 하나 고르고 어떤 기술을 Working 이상으로 올려야 하는지 정리한다.

### Activity 3: Production Readiness Review 연습

`guides/evals-security-observability-checklist.md`의 Production Readiness Review를 사용해 가상의 "사내 문서 기반 AI assistant" 프로젝트를 평가한다. launch 가능 여부를 판단할 때 모델 성능만 보지 말고 eval, security, observability, adoption metric을 함께 확인한다.

## Self-Assessment

- [ ] LLM demo와 production AI workflow의 차이를 5개 이상 말할 수 있다.
- [ ] eval이 FDE의 product feedback loop와 어떻게 연결되는지 설명할 수 있다.
- [ ] 고객 보안/권한 환경을 고려해 AI workflow 설계 지시를 작성할 수 있다.
- [ ] 자신의 목표 FDE archetype에 맞춰 기술 학습 우선순위를 정할 수 있다.

## 이전/다음 모듈

- 이전 모듈: `../04-Role-Taxonomy/`
- 다음 모듈: `../06-US-Job-Market/`
