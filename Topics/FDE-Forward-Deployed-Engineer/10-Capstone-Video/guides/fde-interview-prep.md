# FDE 지원자 최종 가이드와 면접 준비

## 최종 가이드 패키지 목차

FDE 지원자는 아래 자료를 하나의 application package로 준비한다. 각 자료는 단독으로도 읽히되, 함께 봤을 때 "고객 문제를 production AI workflow로 바꿀 수 있는 사람"이라는 메시지를 강화해야 한다.

| 문서 | 목적 | 분량 |
|---|---|---|
| One-page FDE Narrative | 내가 왜 FDE형 인재인지 요약 | 1페이지 |
| Portfolio README | 대표 프로젝트 1개를 customer scenario 중심으로 설명 | 3-5페이지 |
| Architecture Diagram | system boundary, data flow, eval, rollout 설명 | 1장 |
| Demo Script | 5분 포트폴리오 데모 흐름 | 1페이지 |
| Resume Bullets | FDE형 성과 문장 | 5-8개 |
| Interview Bank | customer scenario, technical, behavioral 답변 | 20-30문항 |
| Target Company Matrix | 회사별 FDE archetype과 fit 판단 | 10개 회사 |

## 면접 루프별 준비

| 면접 유형 | 평가 질문 | 준비 산출물 |
|---|---|---|
| Recruiter Screen | 왜 FDE인가, 왜 이 회사인가, 고객-facing 역할을 감당할 수 있는가 | 60초 자기소개, target company fit |
| Hiring Manager | ambiguity, ownership, stakeholder management가 있는가 | project narrative 3개 |
| Technical Screen | API, data, backend, LLM workflow를 설명하고 구현할 수 있는가 | 작은 coding exercise, architecture walkthrough |
| System Design | 고객 환경에서 secure, scalable AI workflow를 설계할 수 있는가 | RAG/agent/eval/security design template |
| Customer Scenario | 모호한 고객 요구를 scope와 next step으로 바꿀 수 있는가 | discovery question bank |
| Portfolio Demo | 직접 만든 결과물을 설득력 있게 보여줄 수 있는가 | 5분 demo script, eval summary |
| Executive/Bar Raiser | business impact와 product feedback을 연결할 수 있는가 | adoption metric, field signal examples |

## 60초 자기소개 템플릿

```text
I am a [background] who works at the intersection of [customer/domain] and [technical delivery].
In my recent work, I focused on [customer problem] and built or led [technical/process solution] that produced [measurable outcome].
I am interested in FDE roles because I like turning ambiguous customer workflows into working systems, then feeding those lessons back into product and deployment patterns.
For this company, I am especially interested in [company-specific AI product/customer segment] because [fit reason].
```

## Customer Scenario 답변 프레임

고객 시나리오 면접에서는 바로 solution을 말하지 않는다. 좋은 답변은 discovery, constraint, prototype, eval, rollout 순서로 간다.

1. Customer goal: 고객이 실제로 달성하려는 business outcome은 무엇인가?
2. Workflow: 현재 사용자는 어떤 순서로 일하고 어디서 막히는가?
3. Data: 어떤 데이터가 있고, 품질/권한/보안 제약은 무엇인가?
4. Prototype: 1-2주 안에 검증할 최소 AI workflow는 무엇인가?
5. Eval: 성공과 실패를 어떻게 측정할 것인가?
6. Rollout: pilot, training, feedback, handoff를 어떻게 설계할 것인가?
7. Product signal: 이 고객 사례에서 제품팀으로 돌아갈 reusable insight는 무엇인가?

## 자주 나오는 질문과 답변 방향

| 질문 | 좋은 답변 방향 |
|---|---|
| FDE와 Solutions Engineer의 차이는 무엇인가? | FDE는 demo/pre-sales보다 build, deployment, product feedback 책임이 더 강하다고 설명 |
| 고객 요구가 모호할 때 어떻게 시작하는가? | business outcome, workflow, data, constraint, pilot success metric부터 묻는다고 답변 |
| LLM app을 production으로 가져갈 때 가장 큰 risk는? | eval, data boundary, latency/cost, observability, human review를 균형 있게 언급 |
| 실패한 customer project를 어떻게 다루는가? | scope mismatch, adoption blocker, technical assumption을 분리하고 다음 experiment로 바꾸는 방식 설명 |
| 포트폴리오 프로젝트가 toy가 아니라는 증거는? | customer scenario, eval, rollout, security boundary, metric이 있다고 보여줌 |

## 면접 전 최종 체크

- [ ] target company의 FDE archetype을 한 문장으로 말할 수 있다.
- [ ] 내 포트폴리오가 customer problem에서 시작한다.
- [ ] architecture diagram에 auth, data, eval, observability가 포함되어 있다.
- [ ] demo가 5분 안에 끝난다.
- [ ] customer scenario 질문에 discovery question부터 말한다.
- [ ] "모른다"를 인정한 뒤 검증 계획을 제시할 수 있다.
- [ ] 비IT/시니어/주니어 배경별 자신의 약점을 먼저 설명하고 보완 증거를 붙일 수 있다.

