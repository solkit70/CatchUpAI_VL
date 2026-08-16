# Ninety-Day Senior FDE Transition Plan

## 목표

90일 계획의 목표는 seniority를 새로 만드는 것이 아니라 기존 seniority를 AI FDE 시장에서 읽히는 증거로 바꾸는 것이다. 90일 후에는 대표 프로젝트 3개, AI workflow demo 1개, eval report 1개, resume narrative, LinkedIn summary, interview story bank가 준비되어야 한다.

## 30/60/90일 개요

| 기간 | 목표 | 핵심 산출물 |
|---|---|---|
| Day 1-30 | 기존 경력 inventory와 AI gap 파악 | transition map, project shortlist, AI stack crash plan |
| Day 31-60 | AI workflow demo와 eval evidence 작성 | RAG/agent demo, eval set, architecture note |
| Day 61-90 | 지원 자료 패키징과 면접 준비 | resume bullets, LinkedIn summary, portfolio one-pager, interview story bank |

## Day 1-30: 경력 재해석

### 작업 1: 대표 프로젝트 5개 inventory

각 프로젝트를 아래 기준으로 정리한다.

| 항목 | 질문 |
|---|---|
| Customer problem | 누구의 어떤 업무 문제가 있었는가? |
| Ambiguity | 처음에 무엇이 불명확했는가? |
| Technical action | 내가 직접 설계/구현/통합/운영한 것은 무엇인가? |
| Production impact | 실제 사용, 비용, 시간, 품질, 안정성에 어떤 변화가 있었는가? |
| Stakeholder | 누구를 설득하거나 조율했는가? |
| Reusable learning | 이후 다른 팀/고객/제품에 재사용한 패턴은 무엇인가? |

### 작업 2: FDE fit 점수화

| 프로젝트 | Customer-facing | Production coding | AI relevance | Impact metric | Reusable pattern | 총점 |
|---|---:|---:|---:|---:|---:|---:|
| Project A |  |  |  |  |  |  |
| Project B |  |  |  |  |  |  |
| Project C |  |  |  |  |  |  |

각 항목은 0-2점으로 평가한다. 8점 이상인 프로젝트 3개를 resume narrative 후보로 고른다.

### 작업 3: AI gap crash plan

| Gap | 30일 학습 행동 | 완료 기준 |
|---|---|---|
| LLM API | structured output app 1개 구현 | GitHub README와 실행 방법 |
| RAG | 기존 문서 20개로 RAG prototype | source citation과 failure examples |
| Evals | 30개 test case와 rubric | pass/fail table |
| Deployment | demo 배포 또는 Docker 실행 | 다른 사람이 실행 가능 |
| Security | secret, PII, permission assumptions 문서화 | security note |

## Day 31-60: AI Workflow Evidence

### 추천 프로젝트: Existing Workflow AI Retrofit

기존 경력에서 익숙한 업무 하나를 고른다. 예를 들어 SI 출신은 장애 ticket triage, PM 출신은 status report automation, consultant 출신은 discovery note synthesis, SWE 출신은 incident-to-fix workflow를 고를 수 있다.

### 필수 구성

| 구성 | 요구사항 |
|---|---|
| Problem brief | 고객 또는 내부 사용자의 반복 업무 문제 |
| Data source | ticket, doc, meeting note, log, spreadsheet 중 하나 |
| AI workflow | RAG, classification, extraction, agent tool call 중 하나 |
| Eval | 30개 이상 test case와 failure taxonomy |
| Deployment | local 실행 또는 hosted demo |
| Runbook | 운영, failure, rollback, security assumption |

### 산출물 구조

```text
ai-workflow-retrofit/
├── README.md
├── architecture.md
├── eval-report.md
├── security-note.md
├── runbook.md
└── demo/
```

## Day 61-90: 지원 자료 패키징

### Resume 작업

대표 bullet은 반드시 아래 구조를 따른다.

```text
Scoped [ambiguous customer/workflow problem], built/integrated [technical system], deployed/operated it across [users/systems], improving [metric], and codified [reusable pattern/playbook].
```

AI 보강 bullet은 아래 구조를 따른다.

```text
Built [LLM/RAG/agent workflow] on top of [domain data/system], with [eval method], [observability/security measure], and [deployment/runbook], demonstrating AI FDE readiness.
```

### LinkedIn Summary 구조

```text
Senior [background] with experience turning ambiguous enterprise workflows into production systems. I combine [core technical strength] with customer-facing delivery, stakeholder alignment, and operational ownership. Recently focused on AI deployment patterns including LLM/RAG workflows, evals, observability, and secure enterprise integration.
```

### Interview Story Bank

| Story | 평가 역량 | 준비 질문 |
|---|---|---|
| Ambiguous customer problem | scoping, judgment | 처음에 무엇이 불명확했고 어떻게 scope했는가? |
| Production incident | calm, ownership | 무엇이 깨졌고 어떻게 impact를 줄였는가? |
| Stakeholder conflict | communication | 기술/일정/보안 trade-off를 어떻게 설명했는가? |
| Reusable pattern | product feedback | 한 프로젝트에서 배운 것을 어떻게 일반화했는가? |
| AI workflow demo | AI FDE readiness | eval, security, observability를 어떻게 설계했는가? |

## 90일 후 지원 전략

| 준비 결과 | 추천 지원 |
|---|---|
| 기존 production/customer 경험 + AI demo/eval 완료 | FDE, FDSWE, Applied AI Engineer |
| strong architecture + AI literacy + hands-on demo 약함 | Solutions Architect, Applied AI Architect |
| strong customer/stakeholder + coding 약함 | AI Consultant, Technical Deployment Lead |
| strong backend/infra + customer 약함 | Scale형 Agent/Infra role, backend-heavy Applied AI |

## 매주 체크포인트

- 이번 주에 FDE narrative가 강해진 evidence가 생겼는가?
- 기존 경력 설명에서 "내가 한 일"보다 "고객 workflow impact"가 더 선명해졌는가?
- AI demo가 단순 기능이 아니라 eval/security/operation까지 설명 가능한가?
- 다음 면접에서 바로 말할 수 있는 story가 하나 늘었는가?
