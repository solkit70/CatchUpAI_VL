# 비IT 배경자 FDE 진입 경로

## 핵심 판단

비IT 배경자의 FDE 직행은 가능하지만 예외적이다. 가능성이 생기는 경우는 강한 도메인 전문성, 고객-facing 경험, AI workflow 이해, 최소 기술 구현 능력이 동시에 있을 때다. 반대로 도메인 지식만 있고 API, 데이터, 소프트웨어 delivery, technical trade-off를 설명하지 못하면 FDE보다 domain specialist 또는 AI consultant 쪽이 더 현실적이다.

FDE는 "고객을 잘 아는 사람"만으로는 부족하다. 고객 업무를 software, data, model, integration, rollout으로 바꾸는 사람이기 때문에 technical minimum이 필요하다. 비IT 배경자는 먼저 FDE 주변 역할로 들어가고, 실제 implementation evidence를 쌓아 FDE에 가까워지는 전략이 더 성공 확률이 높다.

## FDE 직행 가능성과 한계

| 항목 | 직행 가능성을 높이는 조건 | 직행을 어렵게 만드는 조건 |
|---|---|---|
| 도메인 전문성 | 금융, 헬스케어, 제조, 공공 등 복잡한 workflow를 깊게 안다 | 도메인 경험이 일반 운영 수준에 머문다 |
| 고객 커뮤니케이션 | 현업, 임원, IT팀 사이 요구사항을 조율한 경험이 있다 | 요구사항 전달은 했지만 실행 책임은 없었다 |
| 기술 이해 | API, 데이터 모델, 권한, integration, LLM workflow를 설명할 수 있다 | no-code 사용 경험만 있고 시스템 구조를 모른다 |
| 산출물 증거 | 업무 자동화, AI assistant, dashboard, workflow prototype을 만들었다 | 학습 이력은 있지만 작동하는 결과물이 없다 |
| 채용 포지션 | vertical AI, regulated industry, domain-heavy FDE | core infra, model platform, developer tool FDE |

## 현실적인 우회 경로

| 경로 | 적합한 배경 | 핵심 업무 | FDE로 이어지는 연결점 |
|---|---|---|---|
| Domain Solution Specialist | 산업 실무자, SME, 컨설턴트 | 고객 업무를 solution requirement로 번역 | domain workflow와 AI use case framing |
| AI Consultant | 전략/운영/업무 혁신 배경 | AI 적용 과제 발굴, PoC 설계, adoption 지원 | discovery, scope, stakeholder alignment |
| Implementation Analyst | 업무 시스템 운영, ERP/CRM, 데이터 운영 | 고객 데이터와 workflow를 구현팀에 연결 | integration, rollout, handoff 경험 |
| GTM Engineer | 영업기획, RevOps, growth, pre-sales | demo, prototype, 고객별 technical narrative 작성 | customer-facing technical proof |
| Solutions Engineer Associate | 비전공 technical learner | demo, API 연동, technical validation 지원 | FDE와 가장 가까운 technical bridge |
| Vertical AI Product Specialist | 특정 산업 PM/기획자 | 산업별 AI feature requirement와 adoption 설계 | field signal을 product feedback으로 전환 |

## 비IT 배경자의 technical minimum

비IT 배경자는 모든 것을 깊게 배울 필요는 없지만, 고객 현장에서 기술팀과 같은 언어로 토론할 최소 기준은 갖춰야 한다.

| 영역 | 최소 기준 | 확인 질문 |
|---|---|---|
| API | REST API 요청/응답, auth token, webhook 개념 이해 | 고객 시스템과 AI 앱을 어떻게 연결할 것인가? |
| Data | CSV, SQL 기본, schema, PII, data quality 이해 | 어떤 데이터가 모델 답변 품질을 제한하는가? |
| LLM workflow | prompt, RAG, tool calling, eval의 역할 이해 | 단순 챗봇과 업무 agent의 차이는 무엇인가? |
| Prototype | Python 또는 JavaScript로 작은 업무 자동화 구현 | 1주 안에 작동하는 demo를 만들 수 있는가? |
| Security | 권한, audit log, data boundary, compliance 기초 | 이 use case에서 고객이 승인하지 않을 위험은 무엇인가? |
| Adoption | 현업 교육, KPI, 운영 handoff 설계 | 사용자가 계속 쓰게 하려면 무엇을 측정해야 하는가? |

## 지원 전략

비IT 배경자는 이력서에서 "AI에 관심이 있다"보다 "내 도메인에서 반복되는 업무 문제를 AI workflow로 바꿔 본 증거"를 보여줘야 한다. 예를 들어 보험 심사 담당자는 claim triage assistant를, 제조 운영자는 maintenance report summarizer를, HR 담당자는 policy Q&A bot과 escalation workflow를 포트폴리오로 만들 수 있다.

면접에서는 FDE라는 title을 고집하기보다 adjacent role을 함께 지원하는 것이 좋다. domain solution specialist, implementation consultant, AI transformation analyst, solutions engineer associate는 FDE 역량을 쌓는 stepping stone이 될 수 있다. 6-12개월 뒤에는 실제 고객 문제, technical artifact, adoption metric을 묶어 FDE narrative로 전환한다.

