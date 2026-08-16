# Junior FDE Portfolio Project Briefs

## 프로젝트 선택 기준

주니어 포트폴리오는 화려한 모델보다 FDE형 사고를 보여줘야 한다. 좋은 프로젝트는 고객 문제, 데이터 연결, AI workflow, eval, 배포, feedback loop가 모두 작게라도 포함된다.

## Project 1: Internal Knowledge RAG Assistant

### 문제 정의

작은 팀이나 동아리, 연구실, 스타트업은 문서가 흩어져 있어 반복 질문과 onboarding 비용이 높다. 이 프로젝트는 문서 기반 질문 답변 assistant를 만들어 새 구성원이 필요한 정보를 더 빨리 찾도록 돕는다.

### 사용자

- 동아리 운영진
- 연구실 신입 구성원
- 작은 스타트업의 customer support 또는 onboarding 담당자

### 핵심 기능

- Markdown/PDF/Google Docs export 문서 ingestion
- chunking과 vector search
- source citation 포함 답변
- 모르는 질문에 대한 fallback
- feedback button 또는 simple rating

### 기술 스택

| 영역 | 추천 |
|---|---|
| Backend | Python FastAPI |
| LLM/RAG | OpenAI/Anthropic API, vector DB 또는 local embedding store |
| Frontend | simple Next.js 또는 Streamlit |
| Eval | 30개 질문/정답/근거 문서 set |
| Deployment | Render/Fly/Vercel 중 하나 |

### Eval 기준

| 기준 | 측정 방법 |
|---|---|
| 답변 정확도 | 30개 질문 중 correct/partial/wrong |
| citation 품질 | source가 실제 답변 근거인지 확인 |
| hallucination | 문서에 없는 내용을 말한 횟수 |
| latency | 평균 응답 시간 |
| usability | 사용자 2명 feedback |

### FDE Resume Bullet

```text
Built and deployed an internal knowledge RAG assistant for a small team, integrating document ingestion, source-grounded answers, and a 30-question eval set to reduce repeated onboarding questions.
```

## Project 2: Workflow Automation Assistant

### 문제 정의

많은 팀은 회의록, ticket, email에서 action item을 놓친다. 이 프로젝트는 문서나 ticket을 읽고 action item, owner, due date, risk를 구조화해 follow-up workflow로 바꾼다.

### 사용자

- 프로젝트 매니저
- 학생 팀 프로젝트 리더
- 소규모 운영팀

### 핵심 기능

- meeting note 또는 ticket text 입력
- action item extraction
- owner/due date/risk structured output
- human review step
- CSV/Notion/Trello/Jira mock export

### 기술 스택

| 영역 | 추천 |
|---|---|
| Backend | TypeScript/Node 또는 Python |
| LLM | structured output, function calling |
| Data | local SQLite 또는 JSON store |
| UI | table editor |
| Eval | 20개 meeting note sample과 expected action items |

### Eval 기준

| 기준 | 측정 방법 |
|---|---|
| extraction precision | 잘못 뽑은 action item 비율 |
| extraction recall | 놓친 action item 비율 |
| structured output validity | schema validation pass rate |
| human review usefulness | 사용자가 수정한 항목 비율 |

### FDE Resume Bullet

```text
Designed a workflow automation assistant that extracts action items from meeting notes into structured follow-up tasks, with schema validation, human review, and precision/recall evals.
```

## Project 3: AI Eval Dashboard

### 문제 정의

AI application은 demo에서는 좋아 보여도 prompt, model, data가 바뀌면 조용히 품질이 떨어질 수 있다. 이 프로젝트는 작은 AI app의 output을 지속적으로 평가하고 failure pattern을 보여주는 dashboard를 만든다.

### 사용자

- AI app 개발자
- startup founder
- 학생 프로젝트 팀

### 핵심 기능

- test case 관리
- model/prompt version 비교
- rubric score 입력
- failure taxonomy 분류
- latency/cost 기록
- before/after summary

### 기술 스택

| 영역 | 추천 |
|---|---|
| Backend | Python/FastAPI 또는 Next.js API routes |
| Database | SQLite/Postgres |
| Frontend | table + chart UI |
| Eval | rule-based score + LLM-as-a-Judge optional |
| Deployment | Vercel/Render |

### Eval 기준

| 기준 | 측정 방법 |
|---|---|
| regression detection | 새 prompt가 기존 test를 깨뜨리는지 확인 |
| failure taxonomy coverage | 실패를 4-6개 유형으로 분류 |
| cost/latency visibility | request별 token/cost/latency 기록 |
| decision usefulness | launch/block decision을 낼 수 있는지 확인 |

### FDE Resume Bullet

```text
Built an AI eval dashboard that tracks prompt/model regressions across test cases, failure categories, latency, and cost, enabling launch decisions for an AI workflow prototype.
```

## 포트폴리오 README 구조

각 프로젝트 README는 아래 구조를 따른다.

1. Problem: 누구의 어떤 workflow 문제인가?
2. Users: 실제 또는 가상 사용자와 사용 맥락
3. System: architecture diagram 또는 data flow
4. Demo: 실행 방법, 배포 URL, screenshot
5. Evals: test set, metric, result, failure cases
6. Security: data handling, secrets, permission assumptions
7. Iteration: feedback과 개선 기록
8. FDE Relevance: 이 프로젝트가 어떤 FDE 역량을 증명하는가?

## 프로젝트 선택 조언

처음부터 세 프로젝트를 모두 완성하려고 하지 않는다. 먼저 RAG Assistant 하나를 끝까지 배포하고 eval까지 만든다. 그 다음 workflow automation으로 customer problem framing을 강화하고, 마지막으로 eval dashboard로 production readiness 신호를 보강한다.
