# M6 - 미국 채용 공고 기반 역량 분석

**상태**: 완료
**예상 학습 시간**: 5시간
**Topic**: FDE-Forward-Deployed-Engineer
**진행일**: 2026-08-16
**진행 방식**: 2026-08-16 사용자 승인 후 VibeLearn AI daily learning 절차에 따라 재진행

## 학습 순서

1. [examples/us-fde-job-posting-analysis.md](examples/us-fde-job-posting-analysis.md) - 미국 FDE 및 유사 직무 공고를 데이터처럼 추출하고 공통 역량을 도출한다.
2. [guides/fde-interview-loop-guide.md](guides/fde-interview-loop-guide.md) - 공고에서 역추론한 FDE 면접 루프와 평가 역량을 학습한다.
3. [guides/compensation-and-location-notes.md](guides/compensation-and-location-notes.md) - 보상, 지역, hybrid, travel, clearance 조건을 지원 전략으로 연결한다.

## 모듈 목표

- 미국 FDE 채용 공고에서 반복되는 핵심 역량을 추출할 수 있다.
- 요구 경력, 기술, 도메인, onsite/travel 조건을 분석할 수 있다.
- compensation과 seniority 차이를 지원 전략에 반영할 수 있다.
- 공고의 role title보다 실제 업무 동사와 산출물 요구를 기준으로 fit을 판단할 수 있다.

## 핵심 요약

2026-08-16 기준 공개 공고를 보면 FDE 시장은 "고객 대면 엔지니어"라는 넓은 말보다 훨씬 구체적이다. 반복 신호는 production AI deployment, full-stack/product engineering, enterprise integration, evals/observability/security, ambiguous scoping, customer communication, reusable pattern codification이다.

회사별 차이도 뚜렷하다. OpenAI는 frontier model을 고객 production workflow에 넣고 product/research feedback loop를 만드는 ownership을 강조한다. Anthropic은 Claude 기반 enterprise adoption, MCP, agent skills, 안전성과 reliability를 강하게 드러낸다. Scale AI는 production agent architecture, enterprise integration, eval harness, guardrail, observability 같은 systems engineering 깊이가 두드러진다. Cursor는 개발팀 workflow 자체를 바꾸는 AI-native developer productivity FDE에 가깝다.

## 원문 신호

> "production systems"

OpenAI FDE 공고의 핵심 신호다. 연구 성과를 고객의 실제 시스템으로 옮기는 역할로 정의된다.

> "MCP servers, sub-agents, and agent skills"

Anthropic FDE 공고의 특징적 신호다. Claude ecosystem 기반의 production workflow 산출물을 요구한다.

> "complex production environments"

Scale AI Frontier Agents Engineer 공고의 핵심 신호다. 좋은 모델보다 enterprise production integration이 어렵다는 관점이 드러난다.

## 오늘의 학습 활동

### Activity 1: Job posting extraction sheet

공고를 "읽을거리"가 아니라 데이터 행(row)으로 분해했다. title, location, years, stack, domain, travel, compensation, role archetype, evidence를 같은 기준으로 추출해 비교 가능하게 만들었다.

### Activity 2: 공통 역량 Top 10 도출

반복되는 요구사항을 technical, delivery, customer, operating context로 묶었다. 특히 LLM 경험만으로는 부족하고, production code와 고객 조직 안에서의 deployment ownership이 핵심이라는 결론을 도출했다.

### Activity 3: Interview loop 가설 작성

Recruiter screen, technical screen, system design, customer scenario, portfolio demo, bar raiser/leadership conversation의 평가 포인트를 공고 신호에서 역추론했다. 각 루프마다 준비 질문과 증거 자료를 연결했다.

## Self-Assessment

- [x] FDE 공고의 "5+ years"가 실제로 요구하는 역량을 설명할 수 있다.
- [x] 공공/국방 FDE와 commercial FDE의 요구조건 차이를 설명할 수 있다.
- [x] 자신의 이력서가 어떤 공고에 fit인지 판단하는 기준을 만들 수 있다.
- [x] FDE와 Applied AI Engineer, Field Engineer, Solutions Architect의 경계를 공고 문장 기준으로 판독할 수 있다.

## 이전/다음 모듈

- 이전 모듈: `../05-AI-FDE-Tech-Stack/`
- 다음 모듈: `../07-Junior-Track/`
