# WorkLog - M5: AI FDE 기술 스택과 실무 흐름

**날짜**: 2026-08-16
**Topic**: FDE-Forward-Deployed-Engineer
**모듈**: M5 - AI FDE 기술 스택과 실무 흐름
**학습 시간**: 06:56 - 07:02 (총 6분, 초안 작성 세션)
**방법론**: VibeLearn AI

## 오늘의 학습 목표

- [x] AI FDE에게 필요한 기술 스택을 업무 흐름 기준으로 설명할 수 있다.
- [x] LLM prototype이 production deployment로 가는 단계를 설계할 수 있다.
- [x] evals, observability, security, cost/latency trade-off의 중요성을 설명할 수 있다.

## 진행 내용

### 1. AI FDE delivery lifecycle 설계

**목적**:
FDE가 고객 프로젝트를 어떻게 discovery에서 production adoption까지 가져가는지 표준 흐름을 만든다.

**진행 내용**:
1. Discovery, Scoping, Prototype, Evals, Integration, Rollout, Handoff & Product Feedback 7단계 lifecycle을 정의했다.
2. 각 단계별 입력, 산출물, 실패 위험, FDE가 내려야 할 핵심 결정을 정리했다.
3. OpenAI의 discovery/scoping/build/rollout 흐름, Scale AI의 data/agent infrastructure, Cursor의 eval/tracing/workflow hardening 요소를 반영했다.

### 2. 기술 스택 맵 작성

**목적**:
AI FDE가 모든 기술을 같은 깊이로 배울 필요가 없으므로, 업무 단계와 커리어 트랙별 필요한 깊이를 구분한다.

**진행 내용**:
- Literacy, Working, Production 세 수준을 정의했다.
- frontend, backend/API, data integration, LLM/RAG/agent, evals, cloud/deployment, security/compliance, observability/operations를 정리했다.
- 학생/주니어, IT 시니어 전환, 비IT 배경자별 요구 깊이를 비교했다.
- Palantir, OpenAI, Anthropic, Scale, Cursor, Hebbia archetype별 기술 강조점을 정리했다.

### 3. Production readiness checklist 작성

**목적**:
AI prototype을 production pilot로 넘기기 전에 확인해야 할 eval, security, observability 기준을 만든다.

**진행 내용**:
- Evals 체크리스트: task success, retrieval, groundedness, human review, regression.
- Security 체크리스트: identity/access, data boundary, audit/compliance, prompt/tool safety.
- Observability 체크리스트: logging, metrics, debugging, rollout monitoring.
- Cost/latency trade-off와 production readiness review table 작성.

## 문제 해결 로그

### 문제 1: 기술 스택 범위가 너무 넓어질 위험

**증상**:
AI FDE 기술 스택은 frontend, backend, data, cloud, LLM, eval, security까지 매우 넓어 한 문서에서 모든 것을 깊게 설명하기 어렵다.

**원인**:
FDE는 specialist라기보다 고객 문제를 풀기 위해 여러 기술을 조합하는 generalist-heavy role이다.

**해결**:
모든 기술을 깊게 설명하지 않고, Literacy/Working/Production 깊이 기준을 만들었다. 지원자의 목표 archetype과 경력 트랙에 따라 필요한 깊이를 다르게 제시했다.

## DoD 체크리스트

- [x] delivery lifecycle 작성
- [x] 기술 스택 맵 작성
- [x] eval/security/observability checklist 작성
- [x] README 업데이트
- [x] WorkLog 작성

**완료율**: 5/5 (100%)

## Daily Retrospective

### What went well

- AI FDE의 일을 단순 기술 목록이 아니라 delivery lifecycle로 정리했다.
- eval, security, observability를 production readiness의 핵심으로 배치했다.
- M6 채용공고 분석에서 요구 역량을 분류할 기준이 생겼다.

### What could be improved

- M6에서 실제 공고 10개를 분석하면서 기술 스택 맵의 빈도와 중요도를 검증해야 한다.
- 추후 portfolio module에서는 checklist를 실제 프로젝트 spec에 적용해 보는 예시가 필요하다.

### Insights

- AI FDE의 핵심 기술은 LLM API 사용법이 아니라 "고객 workflow를 AI system으로 바꾸고, 그 시스템이 안전하게 작동하는지 측정하는 능력"이다.
- evals, security, observability는 AI FDE의 보조 업무가 아니라 production deployment의 중심 업무다.

### Tomorrow's focus

- M6 - 미국 채용 공고 기반 역량 분석을 진행한다.
- M3/M5에서 만든 archetype과 기술 스택 기준을 실제 job posting 10개에 적용한다.
- 공통 역량 top 10과 interview loop 가설을 만든다.

## 참조 및 산출물

**참조 자료**:
- M1-M4에서 수집한 OpenAI, Scale AI, Cursor, Anthropic, Hebbia, Palantir 채용 설명.

**생성된 파일/폴더**:
- `05-AI-FDE-Tech-Stack/README.md`: M5 학습 순서와 요약.
- `05-AI-FDE-Tech-Stack/concepts/ai-fde-delivery-lifecycle.md`: AI FDE delivery lifecycle.
- `05-AI-FDE-Tech-Stack/concepts/technical-stack-map.md`: 기술 스택 맵과 트랙별 깊이.
- `05-AI-FDE-Tech-Stack/guides/evals-security-observability-checklist.md`: production readiness checklist.

**다음 세션 준비사항**:
- M6에서 실제 미국 job posting을 더 촘촘히 수집한다.
- 각 공고의 role title, company, location, years, stack, domain, travel, salary, success metric을 추출한다.
