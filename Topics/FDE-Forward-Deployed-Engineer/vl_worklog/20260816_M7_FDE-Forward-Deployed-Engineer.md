# 2026-08-16 M7 WorkLog - 학생/주니어 준비 로드맵

## 오늘의 학습 목표

- VibeLearn AI daily learning 절차에 따라 사용자 승인 후 M7을 진행한다.
- M6의 top 10 역량을 학생/주니어가 실행 가능한 milestone으로 낮춰 번역한다.
- 주니어 역량 체크리스트와 6개월 포트폴리오 계획을 작성한다.
- FDE형 포트폴리오 프로젝트 3종을 설계한다.

## 진행 내용

### 1. 이전 WorkLog 및 Roadmap 확인

M6 WorkLog의 Tomorrow's Focus를 확인했다. 다음 작업은 M7에서 senior-level FDE 요구사항을 junior-friendly milestone으로 번역하고, 6개월 포트폴리오 계획과 entry path decision tree를 만드는 것이었다.

### 2. M6 역량을 주니어 기준으로 번역

M6의 공통 역량 top 10 중 production-grade engineering, customer-facing delivery, ambiguity scoping, full-stack fluency, LLM/agent implementation, evals, enterprise integration, security/governance, reusable pattern codification, communication을 주니어 체크리스트로 바꿨다. 핵심은 senior 공고를 그대로 따라 하는 것이 아니라 작은 프로젝트에서 같은 신호를 축소 증명하는 것이다.

### 3. M7 산출물 폴더 생성

`07-Junior-Track/` 폴더와 하위 `guides/`, `examples/` 폴더를 생성했다. 로드맵 산출물 구조에 맞춰 README, 주니어 역량 체크리스트, 6개월 계획, 포트폴리오 프로젝트 brief를 작성했다.

### 4. Junior Skill Checklist 작성

`guides/junior-skill-checklist.md`에는 coding, AI app, cloud/deployment, evals, customer discovery, communication, domain workflow, security literacy, product sense, reusable pattern을 beginner/intermediate/job-ready 기준으로 나눴다. 또한 FDE 직행 가능 조건과 우회 경로가 더 현실적인 조건을 분리했다.

### 5. Six-Month Plan 작성

`guides/six-month-plan.md`에는 6개월 동안 AI workflow project 3개, eval report, 사용자 feedback, portfolio hub, resume bullet을 만드는 계획을 작성했다. 마지막에는 entry path decision tree를 Mermaid로 정리했다.

### 6. Portfolio Project Briefs 작성

`examples/portfolio-project-briefs.md`에는 Internal Knowledge RAG Assistant, Workflow Automation Assistant, AI Eval Dashboard의 세 프로젝트를 설계했다. 각 프로젝트는 문제 정의, 사용자, 핵심 기능, 기술 스택, eval 기준, FDE resume bullet을 포함한다.

## 문제 해결 로그

- 문제: 주니어에게 senior FDE 공고를 그대로 제시하면 비현실적인 준비 계획이 된다.
- 해결: 공고 요구사항을 "작은 증거"로 낮췄다. 예를 들어 production-grade engineering은 대규모 운영 경험이 아니라 배포 URL, logging, eval, failure case 기록으로 축소했다.

## DoD 체크리스트

- [x] 주니어 역량 체크리스트 작성
- [x] 6개월 포트폴리오 계획 작성
- [x] 포트폴리오 프로젝트 3종 설계
- [x] README 업데이트
- [x] WorkLog 작성

## Daily Retrospective

### 오늘 배운 것

학생/주니어 FDE 준비의 핵심은 senior 공고를 그대로 따라 하는 것이 아니라 FDE형 신호를 작은 프로젝트로 증명하는 것이다. customer problem, deployed workflow, eval, feedback loop, clear communication을 갖추면 FDE 직행이 아니더라도 FDE-adjacent 경로로 접근할 수 있다.

### 잘한 점

M6의 채용 공고 분석을 M7의 실행 가능한 준비 계획으로 연결했다. 특히 직행 조건과 우회 경로를 분리해 과장된 커리어 조언을 피했다.

### 개선할 점

M8에서는 IT 시니어 전환자를 다룰 때 주니어와 반대로 "이미 가진 경험을 FDE 언어로 재해석"하는 데 집중해야 한다. senior는 기술 입문보다 기존 delivery, 운영, 고객, stakeholder 경험을 AI production pattern과 연결하는 것이 중요하다.

### Tomorrow's Focus

- M8 IT 시니어 커리어 전환 로드맵을 작성한다.
- SWE, SI, PM, Consultant, Solutions Architect 출신별 강점과 gap을 구분한다.
- senior FDE resume narrative와 90일 전환 계획을 만든다.

## 참조 및 산출물

- `07-Junior-Track/README.md`
- `07-Junior-Track/guides/junior-skill-checklist.md`
- `07-Junior-Track/guides/six-month-plan.md`
- `07-Junior-Track/examples/portfolio-project-briefs.md`
- `06-US-Job-Market/examples/us-fde-job-posting-analysis.md`
- `05-AI-FDE-Tech-Stack/concepts/technical-stack-map.md`
- `04-Role-Taxonomy/concepts/role-taxonomy.md`
