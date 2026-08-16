# 2026-08-16 M5 WorkLog - AI FDE 기술 스택과 실무 흐름 재점검

## 오늘의 학습 목표

- `daily_learning_prompt.md` 기준으로 M5를 다시 진행한다.
- AI FDE의 delivery lifecycle을 demo가 아니라 production adoption 관점으로 보강한다.
- 기술 스택 맵을 목표 role archetype별 학습 우선순위 도구로 확장한다.
- eval, security, observability 체크리스트를 실습과 포트폴리오에 활용할 수 있게 만든다.

## 진행 내용

### 1. 기존 산출물 점검

M5의 기존 산출물은 `README.md`, `concepts/ai-fde-delivery-lifecycle.md`, `concepts/technical-stack-map.md`, `guides/evals-security-observability-checklist.md`로 구성되어 있었다. 이미 lifecycle, stack map, production readiness checklist가 있었지만, daily learning 기준으로 학습자가 직접 적용하는 실습과 M4/M6 연결을 보강할 필요가 있었다.

### 2. README 보강

`05-AI-FDE-Tech-Stack/README.md`에 daily learning 기준 재점검 기록을 추가했다. 또한 demo-to-production gap 찾기, 목표 role별 기술 깊이 표시, production readiness review 연습이라는 세 가지 학습 활동과 self-assessment를 추가했다.

### 3. Delivery Lifecycle 보강

`concepts/ai-fde-delivery-lifecycle.md`에 M4와의 연결, Demo-to-Production Gap, 사내 문서 AI Assistant lifecycle 실습, AI에게 지시하는 연습을 추가했다. 핵심은 FDE가 AI 기능 구현자에 머물지 않고 discovery부터 handoff와 product feedback까지 책임진다는 점이다.

### 4. Technical Stack Map 보강

`concepts/technical-stack-map.md`에 기술 깊이 자기진단, role별 기술 준비 예시, M6 채용공고 분석으로 이어지는 질문을 추가했다. 이를 통해 학습자가 모든 기술을 같은 깊이로 공부하는 대신 목표 FDE archetype에 맞춰 준비 우선순위를 정할 수 있게 했다.

### 5. Checklist 보강

`guides/evals-security-observability-checklist.md`에 checklist 사용 원칙, mini case review, production readiness 점수표, 포트폴리오 활용법을 추가했다. 모델 성능만 보는 것이 아니라 권한, 관측, 운영, adoption을 함께 점검하는 방향으로 강화했다.

## 문제 해결 로그

- 문제: M5는 기술 범위가 넓어 단순 stack list로 흐를 위험이 있었다.
- 해결: lifecycle decision, demo-to-production gap, readiness review를 중심으로 재구성해 FDE 역할의 실무 판단력을 드러내도록 보강했다.

## DoD 체크리스트

- [x] delivery lifecycle 작성
- [x] 기술 스택 맵 작성
- [x] eval/security/observability checklist 작성
- [x] README 업데이트
- [x] WorkLog 작성
- [x] daily_learning_prompt 기준 재점검 기록 반영
- [x] demo-to-production gap 실습 추가
- [x] production readiness 점수표 추가

## Daily Retrospective

### 오늘 배운 것

AI FDE의 기술 스택은 LLM API 사용법보다 훨씬 넓다. 고객 workflow, 데이터, 권한, eval, observability, rollout, handoff까지 연결되어야 production adoption을 만들 수 있다.

### 잘한 점

M4의 role taxonomy와 M5의 lifecycle을 연결했다. 이 덕분에 Applied AI Engineer와 FDE의 차이를 기술 수준이 아니라 lifecycle ownership 관점에서 설명할 수 있게 됐다.

### 개선할 점

M6에서 실제 미국 채용공고를 분석할 때 M5의 stack map과 readiness 질문을 검증해야 한다. 특히 공고마다 evals, security, observability가 얼마나 명시되는지 확인하면 M5의 실무성이 더 강해진다.

### Tomorrow's Focus

- M6에서는 실제 미국 FDE 및 유사 직무 공고를 데이터처럼 추출한다.
- M4의 role 판독 점수표와 M5의 기술 스택 질문을 함께 사용해 공고별 role 성격과 요구 역량을 분석한다.

## 참조 및 산출물

- `05-AI-FDE-Tech-Stack/README.md`
- `05-AI-FDE-Tech-Stack/concepts/ai-fde-delivery-lifecycle.md`
- `05-AI-FDE-Tech-Stack/concepts/technical-stack-map.md`
- `05-AI-FDE-Tech-Stack/guides/evals-security-observability-checklist.md`
- `vl_roadmap/20260816_RoadMap_FDE-Forward-Deployed-Engineer.md`
