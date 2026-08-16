# Junior FDE Skill Checklist

## 사용 방법

이 체크리스트는 학생/주니어가 FDE를 준비할 때 "무엇을 먼저 해야 하는가"를 정하기 위한 도구다. 목표는 모든 역량을 senior 수준으로 만드는 것이 아니라, 6개월 안에 FDE형 포트폴리오를 만들 수 있는 최소 실행 역량을 확보하는 것이다.

## 수준 정의

| 수준 | 의미 | 증거 |
|---|---|---|
| Beginner | 개념을 설명하고 작은 예제를 따라 할 수 있다 | 튜토리얼 재현, 짧은 노트, 단일 기능 demo |
| Intermediate | 작은 프로젝트를 직접 설계하고 막히면 디버깅할 수 있다 | end-to-end app, README, issue log |
| Job-ready | 제한된 범위에서 실제 사용자와 feedback loop를 만들 수 있다 | 배포 URL, eval 결과, user feedback, 개선 기록 |

## 핵심 역량 체크리스트

| 역량 | Beginner | Intermediate | Job-ready | 주니어 우선순위 |
|---|---|---|---|---|
| Coding | Python 또는 TypeScript 기본 문법과 API 호출을 이해한다 | FastAPI/Next.js 중 하나로 작은 app을 만든다 | auth, error handling, logging이 있는 workflow를 배포한다 | 필수 |
| AI App | LLM API, prompt, structured output을 이해한다 | RAG 또는 tool calling workflow를 구현한다 | eval과 failure case를 포함해 모델 품질을 설명한다 | 필수 |
| Cloud / Deployment | env var, secret, Docker 개념을 안다 | 간단한 app을 Vercel/Render/Fly/AWS 중 하나에 배포한다 | rollback, monitoring, cost/latency note를 남긴다 | 필수 |
| Evals | 좋은 답변/나쁜 답변 기준을 말할 수 있다 | 20-50개 test case와 rubric을 만든다 | regression 결과와 개선 전후 비교를 보여준다 | 필수 |
| Customer Discovery | 문제 인터뷰 질문을 작성할 수 있다 | 사용자 2-3명과 workflow를 관찰하고 기록한다 | success metric과 adoption blocker를 도출한다 | 필수 |
| Communication | 프로젝트를 2분 안에 설명한다 | technical README와 non-technical summary를 나눠 쓴다 | trade-off, risk, next step을 stakeholder 관점으로 말한다 | 필수 |
| Domain Workflow | 하나의 업무 도메인을 고른다 | 업무 흐름, 데이터, 예외 케이스를 문서화한다 | AI 적용 전후의 시간/품질/오류 변화를 측정한다 | 중요 |
| Security Literacy | PII, permission, secret leak 위험을 안다 | 사용자별 접근 권한과 데이터 보관 정책을 설계한다 | audit log, least privilege, provider data policy를 설명한다 | 중요 |
| Product Sense | 사용자 pain point를 설명한다 | MVP scope와 success metric을 정의한다 | usage/adoption feedback으로 iteration한다 | 중요 |
| Reusable Pattern | 배운 점을 메모한다 | template, checklist, playbook으로 정리한다 | 다른 use case에 재사용 가능한 component로 만든다 | 선택 |

## 주니어가 FDE 직행을 노릴 수 있는 경우

아래 조건 중 4개 이상을 만족하면 FDE 또는 FDE-adjacent 역할에 직접 도전할 수 있다.

- [ ] production에 가까운 AI workflow를 직접 배포한 경험이 있다.
- [ ] 실제 사용자 또는 고객과 discovery, feedback, iteration을 해본 적이 있다.
- [ ] Python 또는 TypeScript로 API, database, deployment를 연결할 수 있다.
- [ ] eval dataset과 failure taxonomy를 만들어 본 적이 있다.
- [ ] cloud 배포, logging, monitoring, secret 관리를 해본 적이 있다.
- [ ] 비기술 사용자에게 문제, trade-off, 결과를 설명할 수 있다.
- [ ] 특정 도메인 workflow를 깊게 이해하고 있다.

## 우회 경로가 더 현실적인 경우

아래 조건에 많이 해당하면 FDE 직행보다 우회 경로가 현실적이다.

| 현재 상태 | 추천 우회 경로 | 이유 |
|---|---|---|
| 코딩은 가능하지만 고객 경험이 없다 | Product Engineer, Implementation Engineer | build 경험을 유지하면서 사용자 접점을 늘린다 |
| 고객 커뮤니케이션은 강하지만 coding proof가 약하다 | Solutions Engineer, Technical Consultant | 고객 강점을 살리되 AI app portfolio로 coding gap을 줄인다 |
| AI 모델/데이터는 알지만 full-stack이 약하다 | Applied AI Engineer, Data/ML Engineer | AI 강점을 살리고 UI/API/deployment를 보완한다 |
| 도메인 전문성은 강하지만 기술이 약하다 | AI Consultant, Domain Solutions Specialist | domain workflow를 FDE형 problem framing으로 바꾼다 |
| 학생/신입이고 실무 경험이 없다 | SWE internship, AI app internship, startup builder role | production habit과 team collaboration 경험을 먼저 만든다 |

## 자기진단 표

| 역량 | 현재 수준 | 목표 수준 | 30일 행동 |
|---|---|---|---|
| Coding |  | Intermediate | 작은 API app 1개 구현 |
| AI App |  | Intermediate | RAG demo 1개 구현 |
| Cloud / Deployment |  | Beginner-Intermediate | app 배포와 env 관리 실습 |
| Evals |  | Intermediate | 30개 test case와 scoring rubric 작성 |
| Customer Discovery |  | Intermediate | 사용자 2명 인터뷰 |
| Communication |  | Intermediate | 2분 pitch와 README 작성 |
| Domain Workflow |  | Intermediate | 선택 도메인 workflow map 작성 |
| Security Literacy |  | Beginner | auth, PII, secret 관리 노트 작성 |

## AI에게 시킬 자기진단 프롬프트

```text
너는 미국 AI 회사의 FDE hiring manager다.
아래 내 경험을 보고 junior FDE 준비 상태를 평가해줘.

내 경험:
[프로젝트, 기술, 고객/사용자 경험, 배포 경험]

평가 기준:
- coding
- AI app
- deployment
- evals
- customer discovery
- communication
- domain workflow

출력:
1. 현재 수준: Beginner / Intermediate / Job-ready
2. 가장 큰 gap 3개
3. 30일 행동 계획
4. FDE 직행 가능성 vs 우회 경로 추천
```
