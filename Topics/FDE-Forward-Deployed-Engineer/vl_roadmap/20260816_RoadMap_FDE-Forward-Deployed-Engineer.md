# FDE-Forward-Deployed-Engineer 학습 로드맵

**생성일**: 2026-08-16
**방법론**: VibeLearn AI
**버전**: 1.0
**주 분석 대상**: 미국 AI/테크 취업시장
**Sub-study**: 한국 AX, 일본 DX to AX, 유럽 enterprise AI transformation

## 학습 기간 적정성 분석

**사용자 입력 기간**: 6주, 주당 4-6시간
**Topic 복잡도**: 복잡
**권장 기간**: 6-8주

**분석 결과**: 적정함. FDE는 단순 직무 정의가 아니라 기업별 변형, 미국 채용 공고 분석, AI 기술 스택, 커리어 전환 전략, 포트폴리오, 영상화까지 포함하는 복합 Topic이다. 6주 안에 핵심 산출물까지 만들 수 있지만, 각 기업별 deep dive를 더 촘촘히 하려면 8주까지 확장 가능하다.

**진행 결정**: 사용자가 승인했으므로 6주 기준으로 진행한다. 필요하면 M6-M9에서 자료량에 따라 1-2주 확장한다.

## 학습 개요

### Topic 소개

Forward Deployed Engineer(FDE)는 고객 현장에 깊게 들어가 제품, 데이터, 업무 프로세스, AI 모델을 실제 production 시스템으로 연결하는 hybrid engineering role이다. Palantir에서 강하게 알려진 모델이지만, 2026년 현재 OpenAI, Anthropic, Scale AI, Cursor, Hebbia 같은 AI 기업들이 각자의 방식으로 FDE 또는 유사 직무를 채용하고 있다. 이 Roadmap은 미국 취업시장을 중심으로 FDE가 어떤 신흥 직업군으로 자리 잡고 있는지, 누가 어떻게 준비해야 하는지 학습한다.

### 학습 목표

- [ ] FDE의 정의, 역사, 대표 기업 사례를 설명할 수 있다.
- [ ] 미국 FDE 및 유사 직무 채용 공고를 분석하여 공통 역량과 기업별 특색을 도출할 수 있다.
- [ ] FDE, Applied AI Engineer, Solutions Engineer, Sales Engineer, Solutions Architect, Consultant, ML Engineer의 차이를 비교할 수 있다.
- [ ] AI FDE에게 필요한 기술 스택을 실무 시나리오 기준으로 정리할 수 있다.
- [ ] 학생/주니어, IT 시니어, 비IT 배경자용 FDE 준비 로드맵과 포트폴리오 가이드를 만들 수 있다.
- [ ] Topic 학습 결과를 Remotion AI 영상 시리즈 대본/스토리보드 구조로 변환할 수 있다.

### 전체 로드맵 구조

| 모듈 | 모듈명 | 난이도 | 예상 시간 | 산출물 폴더 |
|---|---|---:|---:|---|
| M1 | FDE 기본 정의와 역사 | 1 | 3h | `01-FDE-Basics/` |
| M2 | Palantir 모델과 FDE의 원형 | 2 | 3h | `02-Palantir-Origin/` |
| M3 | 미국 AI 기업별 FDE 모델 비교 | 2 | 5h | `03-US-Company-Models/` |
| M4 | FDE와 유사 직무 비교 | 2 | 4h | `04-Role-Taxonomy/` |
| M5 | AI FDE 기술 스택과 실무 흐름 | 3 | 5h | `05-AI-FDE-Tech-Stack/` |
| M6 | 미국 채용 공고 기반 역량 분석 | 3 | 5h | `06-US-Job-Market/` |
| M7 | 학생/주니어 준비 로드맵 | 2 | 4h | `07-Junior-Track/` |
| M8 | IT 시니어 커리어 전환 로드맵 | 2 | 4h | `08-Senior-Transition/` |
| M9 | 비IT 배경자와 글로벌 Sub-study | 2 | 4h | `09-Non-IT-Global-Context/` |
| M10 | 포트폴리오와 Remotion 영상화 Capstone | 3 | 6h | `10-Capstone-Video/` |

**총 예상 시간**: 43시간, 버퍼 포함

## 모듈별 상세 계획

### M1 - FDE 기본 정의와 역사

**난이도**: 1
**예상 시간**: 3h
**산출물 폴더**: `01-FDE-Basics/`

#### 학습 목표

- [ ] FDE를 2문장으로 정의할 수 있다.
- [ ] FDE가 software engineer, consultant, solutions engineer와 다른 지점을 설명할 수 있다.
- [ ] AI 시대에 FDE가 다시 주목받는 이유를 3가지로 정리할 수 있다.

#### 주요 개념

1. **Forward deployed**: 제품팀 바깥의 고객 현장에 배치되어 문제를 직접 해결하는 방식.
2. **Production adoption**: 데모가 아니라 실제 업무에서 반복 사용되는 상태.
3. **Field signal**: 고객 현장에서 얻은 제품/모델 개선 신호.
4. **Hybrid role**: engineering, consulting, product, GTM이 섞인 역할.

#### 실습 과제

**실습 1: FDE 한 문장 정의 만들기**
- 목적: 모호한 직무를 명확한 설명으로 압축한다.
- 단계: 1. OpenAI/Scale/Cursor/Hebbia 공고의 공통 문장을 추출한다. 2. 반복 키워드를 묶는다. 3. 한국어/영어 정의를 각각 작성한다.
- 예상 시간: 50분
- 난이도: 1
- 검증: 비전공자에게 설명했을 때 FDE와 일반 컨설턴트 차이가 전달된다.

**실습 2: FDE 등장 배경 타임라인**
- 목적: Palantir식 원형에서 AI FDE로 이어지는 흐름을 잡는다.
- 단계: 1. Palantir, enterprise software, generative AI adoption 흐름을 연도별로 정리한다. 2. 각 시점의 고객 문제를 기록한다. 3. 5단계 타임라인을 만든다.
- 예상 시간: 70분
- 난이도: 2
- 검증: 타임라인이 "왜 지금 FDE인가"를 설명한다.

#### 산출물

```
01-FDE-Basics/
├── README.md
├── concepts/
│   ├── fde-definition.md
│   └── fde-history-timeline.md
└── examples/
    └── two-minute-explanation.md
```

#### Definition of Done

- [ ] FDE 정의 문서 작성
- [ ] 역사 타임라인 작성
- [ ] 2분 설명문 작성
- [ ] README에 학습 순서와 문서 링크 정리
- [ ] WorkLog 작성

#### Self-Assessment

- [ ] FDE를 AI 솔루션 영업과 구분해 설명할 수 있는가?
- [ ] FDE의 결과물이 왜 production adoption인지 설명할 수 있는가?
- [ ] AI에게 "FDE와 SE 차이 비교표를 만들어라"라고 지시하고 결과 품질을 판단할 수 있는가?

#### 예상 시간 배분

- 개념 학습: 40분
- 실습 1: 50분
- 실습 2: 70분
- 문서화: 20분
- 합계: 3h

#### 참조 자료

- OpenAI FDE: https://openai.com/careers/forward-deployed-engineer-%28fde%29-seattle-seattle/ - FDE를 production deployment와 product feedback의 교차점으로 설명한다.
- Cursor FDE: https://cursor.com/careers/forward-deployed-engineer - "demo role이 아니다"라는 AI developer tool형 FDE 설명이 명확하다.

### M2 - Palantir 모델과 FDE의 원형

**난이도**: 2
**예상 시간**: 3h
**산출물 폴더**: `02-Palantir-Origin/`

#### 학습 목표

- [ ] Palantir식 FDE의 핵심 구조를 설명할 수 있다.
- [ ] Deployment Strategist와 FDE의 관계를 정리할 수 있다.
- [ ] Palantir 원형이 AI 기업 FDE와 어떻게 달라졌는지 비교할 수 있다.

#### 주요 개념

1. **Ontology/product platform**: 고객 업무를 소프트웨어 플랫폼 위에 모델링하는 접근.
2. **Embedded delivery**: 고객 현장에 붙어 프로토타입부터 운영까지 책임지는 방식.
3. **Operational workflow**: 데이터 분석을 실제 의사결정과 실행으로 연결하는 흐름.
4. **Reusable pattern**: 특정 고객 문제 해결 후 제품 기능이나 playbook으로 일반화하는 결과.

#### 실습 과제

**실습 1: Palantir형 FDE 역할 분해**
- 목적: FDE 원형의 업무 단위를 이해한다.
- 단계: 1. Palantir/Accenture 공고에서 동사를 추출한다. 2. 요구 역량을 engineering, domain, deployment, communication으로 분류한다. 3. 현재 AI FDE와 비교할 기준을 만든다.
- 예상 시간: 70분
- 난이도: 2
- 검증: Palantir형 FDE의 5대 업무가 표로 정리된다.

**실습 2: 원형 vs AI FDE 비교**
- 목적: AI 시대 변화를 구조화한다.
- 단계: 1. Palantir형과 OpenAI/Cursor형을 비교한다. 2. 제품, 고객, 기술, 성공 지표 차이를 표로 만든다. 3. "바뀐 것/안 바뀐 것"을 분리한다.
- 예상 시간: 70분
- 난이도: 2
- 검증: 비교표가 M3 기업별 분석의 기준표로 재사용 가능하다.

#### 산출물

```
02-Palantir-Origin/
├── README.md
├── concepts/
│   └── palantir-fde-origin.md
└── examples/
    └── original-vs-ai-fde-comparison.md
```

#### Definition of Done

- [ ] Palantir 원형 분석 문서 작성
- [ ] 원형 vs AI FDE 비교표 작성
- [ ] 다음 모듈에서 쓸 비교 기준 확정
- [ ] README 업데이트
- [ ] WorkLog 작성

#### Self-Assessment

- [ ] Palantir형 FDE가 왜 consulting도 pure engineering도 아닌지 설명할 수 있는가?
- [ ] AI FDE와 Palantir 원형의 공통점 3개와 차이점 3개를 말할 수 있는가?
- [ ] 기업별 FDE 분석 기준을 스스로 만들 수 있는가?

#### 예상 시간 배분

- 개념 학습: 40분
- 실습 1: 70분
- 실습 2: 70분
- 문서화: 20분
- 합계: 3h

#### 참조 자료

- Accenture Palantir FDE: https://www.accenture.com/us-en/careers/jobdetails?id=R00324743_en - Palantir software를 고객 운영 문제에 배포하는 역할 설명.
- Palantir Forward Deployed Infrastructure Engineer: https://jobs.lever.co/palantir/33243fb5-6907-40c7-930c-968b25d825d0 - forward deployed 팀과 운영/인프라 책임의 관계를 보여준다.

### M3 - 미국 AI 기업별 FDE 모델 비교

**난이도**: 2
**예상 시간**: 5h
**산출물 폴더**: `03-US-Company-Models/`

#### 학습 목표

- [ ] OpenAI, Anthropic, Scale AI, Cursor, Hebbia의 FDE/유사 직무를 비교할 수 있다.
- [ ] 기업별 FDE가 product, GTM, customer success, engineering 중 어디에 가까운지 분류할 수 있다.
- [ ] 회사별 특색을 지원자 관점의 준비 전략으로 번역할 수 있다.

#### 주요 개념

1. **AI lab FDE**: frontier model을 고객 production 시스템에 연결하는 역할.
2. **Developer tool FDE**: 고객 개발팀의 workflow를 AI-native하게 바꾸는 역할.
3. **Data/GenAI infrastructure FDE**: 데이터, eval, agent, 플랫폼 연동을 담당하는 역할.
4. **Vertical AI FDE**: 금융, 법률, 공공 등 특정 도메인 workflow에 깊게 들어가는 역할.

#### 실습 과제

**실습 1: 기업별 공고 비교 매트릭스**
- 목적: FDE가 회사마다 어떻게 다른지 구조화한다.
- 단계: 1. 공고별 팀 위치, 고객, 기술, 요구 경력, travel, compensation을 추출한다. 2. 5개 기업 비교표를 만든다. 3. 각 기업의 FDE archetype을 명명한다.
- 예상 시간: 120분
- 난이도: 2
- 검증: 각 회사별 FDE 특색이 한눈에 보인다.

**실습 2: 지원자-fit 판단 도구 만들기**
- 목적: 학습자가 자신에게 맞는 FDE 유형을 고를 수 있게 한다.
- 단계: 1. 성향 질문 10개를 만든다. 2. 답변을 AI lab형, developer tool형, data infra형, vertical AI형으로 매핑한다. 3. 추천 결과 템플릿을 만든다.
- 예상 시간: 100분
- 난이도: 2
- 검증: 3명의 가상 후보자에게 적용해 다른 추천이 나온다.

#### 산출물

```
03-US-Company-Models/
├── README.md
├── concepts/
│   └── fde-company-archetypes.md
├── examples/
│   └── company-comparison-matrix.md
└── guides/
    └── candidate-fit-selector.md
```

#### Definition of Done

- [ ] 5개 이상 기업 비교표 작성
- [ ] FDE archetype 4개 이상 정의
- [ ] 지원자-fit 판단 도구 작성
- [ ] README 업데이트
- [ ] WorkLog 작성

#### Self-Assessment

- [ ] OpenAI형 FDE와 Cursor형 FDE의 성공 지표 차이를 설명할 수 있는가?
- [ ] Scale AI와 Hebbia의 FDE가 왜 data/domain workflow에 가까운지 설명할 수 있는가?
- [ ] Anthropic의 Applied AI/FDE 계열을 FDE 생태계 안에서 위치시킬 수 있는가?

#### 예상 시간 배분

- 개념 학습: 60분
- 실습 1: 120분
- 실습 2: 100분
- 문서화: 20분
- 합계: 5h

#### 참조 자료

- OpenAI FDE: https://openai.com/careers/forward-deployed-engineer-%28fde%29-seattle-seattle/
- Anthropic careers: https://www.anthropic.com/careers/jobs
- Scale AI FDE GenAI: https://scale.com/careers/4593571005
- Cursor FDE: https://cursor.com/careers/forward-deployed-engineer
- Hebbia FDE: https://jobs.ashbyhq.com/hebbia-ai/b35852eb-97ac-491a-b375-91fd13d0b7b3

### M4 - FDE와 유사 직무 비교

**난이도**: 2
**예상 시간**: 4h
**산출물 폴더**: `04-Role-Taxonomy/`

#### 학습 목표

- [ ] FDE와 유사 직무 8개를 비교할 수 있다.
- [ ] 직무명만 보고 실제 업무를 오판하지 않는 기준을 만들 수 있다.
- [ ] 지원자가 자신의 기존 경험을 FDE 언어로 재포장할 수 있다.

#### 주요 개념

1. **Solutions Engineer**: pre-sales와 technical validation 중심인 경우가 많다.
2. **Applied AI Engineer**: AI application build에 가깝지만 고객 현장성은 회사마다 다르다.
3. **Solutions Architect**: architecture와 adoption을 다루지만 hands-on production coding 비중은 다양하다.
4. **Technical Deployment Lead**: 구현보다 delivery orchestration 비중이 높을 수 있다.

#### 실습 과제

**실습 1: 직무 taxonomy 작성**
- 목적: 유사 직무 간 경계를 명확히 한다.
- 단계: 1. 8개 직무를 customer-facing 정도와 coding 정도 2축에 배치한다. 2. 각 직무의 대표 산출물을 적는다. 3. FDE의 위치를 표시한다.
- 예상 시간: 90분
- 난이도: 2
- 검증: 직무맵만 보고 차이를 설명할 수 있다.

**실습 2: 이력서 bullet 변환**
- 목적: 기존 경험을 FDE형 언어로 바꾼다.
- 단계: 1. SI/PM/개발/컨설팅 경험 예시를 만든다. 2. discovery, scope, build, deploy, adoption, feedback 언어로 변환한다. 3. 좋은 bullet과 나쁜 bullet을 비교한다.
- 예상 시간: 90분
- 난이도: 2
- 검증: 최소 10개 resume bullet이 생성된다.

#### 산출물

```
04-Role-Taxonomy/
├── README.md
├── concepts/
│   └── role-taxonomy.md
├── examples/
│   └── resume-bullet-transformations.md
└── guides/
    └── role-title-reading-guide.md
```

#### Definition of Done

- [ ] 직무 taxonomy 작성
- [ ] 2축 role map 작성
- [ ] resume bullet 변환 예시 10개 작성
- [ ] README 업데이트
- [ ] WorkLog 작성

#### Self-Assessment

- [ ] FDE와 Solutions Engineer의 차이를 사례로 설명할 수 있는가?
- [ ] "Applied AI Engineer" 공고가 FDE형인지 아닌지 판단할 수 있는가?
- [ ] 자신의 경험 하나를 FDE형 bullet로 바꿀 수 있는가?

#### 예상 시간 배분

- 개념 학습: 50분
- 실습 1: 90분
- 실습 2: 90분
- 문서화: 10분
- 합계: 4h

#### 참조 자료

- Cursor careers: https://cursor.com/careers - FDE, Field Engineer, AI Adoption Engineer, AI Deployment Manager 등 유사 직무가 함께 존재한다.
- Anthropic careers: https://www.anthropic.com/careers/jobs - Applied AI Architect, Applied AI Engineer, FDE 계열 명칭 비교에 유용하다.

### M5 - AI FDE 기술 스택과 실무 흐름

**난이도**: 3
**예상 시간**: 5h
**산출물 폴더**: `05-AI-FDE-Tech-Stack/`

#### 학습 목표

- [ ] AI FDE에게 필요한 기술 스택을 업무 흐름 기준으로 설명할 수 있다.
- [ ] LLM prototype이 production deployment로 가는 단계를 설계할 수 있다.
- [ ] evals, observability, security, cost/latency trade-off의 중요성을 설명할 수 있다.

#### 주요 개념

1. **RAG/data integration**: 고객 내부 지식과 AI 모델을 연결하는 핵심 패턴.
2. **Agentic workflow**: 모델이 도구와 시스템을 호출해 업무를 수행하는 구조.
3. **Evals**: 모델/agent가 업무 목표를 달성하는지 측정하는 체계.
4. **Deployment boundary**: 고객 보안, 권한, compliance 안에서 시스템을 배포하는 경계.

#### 실습 과제

**실습 1: AI FDE delivery lifecycle 설계**
- 목적: discovery부터 rollout까지 표준 흐름을 만든다.
- 단계: 1. discovery, scoping, prototype, eval, integration, rollout, handoff 단계를 정의한다. 2. 각 단계의 입력/출력물을 적는다. 3. risk checklist를 붙인다.
- 예상 시간: 110분
- 난이도: 3
- 검증: 고객 시나리오 하나에 lifecycle을 적용할 수 있다.

**실습 2: FDE용 기술 스택 맵**
- 목적: 어떤 기술을 어느 깊이까지 알아야 하는지 구분한다.
- 단계: 1. frontend/backend/data/cloud/LLM/evals/security를 나눈다. 2. junior/senior/non-IT 트랙별 필수 깊이를 표시한다. 3. 학습 우선순위를 만든다.
- 예상 시간: 110분
- 난이도: 3
- 검증: 세 트랙별 기술 준비표가 완성된다.

#### 산출물

```
05-AI-FDE-Tech-Stack/
├── README.md
├── concepts/
│   ├── ai-fde-delivery-lifecycle.md
│   └── technical-stack-map.md
└── guides/
    └── evals-security-observability-checklist.md
```

#### Definition of Done

- [ ] delivery lifecycle 작성
- [ ] 기술 스택 맵 작성
- [ ] eval/security/observability checklist 작성
- [ ] README 업데이트
- [ ] WorkLog 작성

#### Self-Assessment

- [ ] AI prototype과 production AI system의 차이를 설명할 수 있는가?
- [ ] eval이 FDE 업무에서 왜 product feedback과 연결되는지 설명할 수 있는가?
- [ ] 고객 보안 환경을 고려한 AI workflow 설계를 AI에게 지시할 수 있는가?

#### 예상 시간 배분

- 개념 학습: 70분
- 실습 1: 110분
- 실습 2: 110분
- 문서화: 10분
- 합계: 5h

#### 참조 자료

- OpenAI Forward Deployed Software Engineer: https://openai.com/careers/forward-deployed-software-engineer-sf-san-francisco/ - OpenAI API 기반 custom software와 고객 인프라 내 공동 구현을 설명한다.
- Scale AI Enterprise FDE: https://job-boards.greenhouse.io/scaleai/jobs/4597399005 - agent, data connectors, ETL, compliance boundary가 명시되어 있다.
- Cursor FDE: https://cursor.com/careers/forward-deployed-engineer - tracing, evals, model behavior debugging, latency/cost trade-off가 명확하다.

### M6 - 미국 채용 공고 기반 역량 분석

**난이도**: 3
**예상 시간**: 5h
**산출물 폴더**: `06-US-Job-Market/`

#### 학습 목표

- [ ] 미국 FDE 채용 공고에서 반복되는 핵심 역량을 추출할 수 있다.
- [ ] 요구 경력, 기술, 도메인, onsite/travel 조건을 분석할 수 있다.
- [ ] compensation과 seniority 차이를 지원 전략에 반영할 수 있다.

#### 주요 개념

1. **Customer-facing engineering experience**: 고객과 직접 일한 기술 경험.
2. **Ambiguity tolerance**: 불완전한 요구사항에서 scope를 잡는 능력.
3. **Travel/onsite requirement**: FDE가 remote-only 직무가 아닐 수 있음을 보여주는 조건.
4. **Security clearance**: 미국 공공/국방 FDE에서 중요한 진입 조건.

#### 실습 과제

**실습 1: Job posting extraction sheet**
- 목적: 공고를 데이터처럼 분석한다.
- 단계: 1. 10개 공고를 수집한다. 2. role title, company, location, years, stack, domain, travel, salary를 추출한다. 3. 공통 top 10 요구사항을 만든다.
- 예상 시간: 130분
- 난이도: 3
- 검증: 공고 분석표가 재사용 가능하다.

**실습 2: Interview loop 가설 만들기**
- 목적: 채용 준비를 면접 유형별로 구조화한다.
- 단계: 1. recruiter screen, technical screen, system design, customer scenario, portfolio demo를 정의한다. 2. 각 면접의 평가 역량을 매핑한다. 3. 대비 질문 20개를 만든다.
- 예상 시간: 120분
- 난이도: 3
- 검증: 면접 준비 가이드 초안이 완성된다.

#### 산출물

```
06-US-Job-Market/
├── README.md
├── examples/
│   └── us-fde-job-posting-analysis.md
└── guides/
    ├── fde-interview-loop-guide.md
    └── compensation-and-location-notes.md
```

#### Definition of Done

- [ ] 10개 공고 분석표 작성
- [ ] 공통 역량 top 10 도출
- [ ] 면접 유형별 대비 가이드 작성
- [ ] README 업데이트
- [ ] WorkLog 작성

#### Self-Assessment

- [ ] FDE 공고의 "5+ years"가 실제로 요구하는 역량을 설명할 수 있는가?
- [ ] 공공/국방 FDE와 commercial FDE의 요구조건 차이를 설명할 수 있는가?
- [ ] 자신의 이력서가 어떤 공고에 fit인지 판단할 수 있는가?

#### 예상 시간 배분

- 개념 학습: 40분
- 실습 1: 130분
- 실습 2: 120분
- 문서화: 10분
- 합계: 5h

#### 참조 자료

- OpenAI Gov FDE: https://openai.com/careers/forward-deployed-engineer-gov-washington-dc/
- Scale AI Public Sector FDSE: https://job-boards.greenhouse.io/scaleai/jobs/4481921005
- Hebbia FDE: https://jobs.ashbyhq.com/hebbia-ai/b35852eb-97ac-491a-b375-91fd13d0b7b3

### M7 - 학생/주니어 준비 로드맵

**난이도**: 2
**예상 시간**: 4h
**산출물 폴더**: `07-Junior-Track/`

#### 학습 목표

- [ ] 학생/주니어가 FDE로 가기 위한 최소 준비 역량을 정의할 수 있다.
- [ ] 6개월 포트폴리오 계획을 만들 수 있다.
- [ ] 미국 취업시장 기준으로 주니어가 직접 FDE에 갈 수 있는 경우와 우회 경로를 구분할 수 있다.

#### 주요 개념

1. **T-shaped junior**: 넓은 기본기와 하나의 실전 강점.
2. **Portfolio proof**: 말보다 실제 작동하는 프로젝트로 증명하는 방식.
3. **Entry path**: FDE 직행, solutions engineer, software engineer, implementation engineer 등 진입 경로.
4. **Customer problem framing**: 기술보다 고객 문제를 먼저 정의하는 능력.

#### 실습 과제

**실습 1: 주니어 역량 체크리스트**
- 목적: 준비해야 할 역량을 과장 없이 정리한다.
- 단계: 1. coding, AI app, cloud, communication, domain 항목을 만든다. 2. beginner/intermediate/job-ready 기준을 정의한다. 3. 부족한 역량별 학습 과제를 붙인다.
- 예상 시간: 90분
- 난이도: 2
- 검증: 자기 평가가 가능한 체크리스트가 완성된다.

**실습 2: 주니어 포트폴리오 3종 설계**
- 목적: 채용자가 볼 수 있는 증거물을 만든다.
- 단계: 1. RAG 업무봇, workflow automation, eval dashboard 프로젝트를 설계한다. 2. 각 프로젝트의 customer scenario와 success metric을 정의한다. 3. GitHub README 구조를 만든다.
- 예상 시간: 110분
- 난이도: 2
- 검증: 3개 프로젝트 brief가 완성된다.

#### 산출물

```
07-Junior-Track/
├── README.md
├── guides/
│   ├── junior-skill-checklist.md
│   └── six-month-plan.md
└── examples/
    └── portfolio-project-briefs.md
```

#### Definition of Done

- [ ] 주니어 역량 체크리스트 작성
- [ ] 6개월 학습 계획 작성
- [ ] 포트폴리오 프로젝트 3개 brief 작성
- [ ] README 업데이트
- [ ] WorkLog 작성

#### Self-Assessment

- [ ] 주니어가 바로 FDE에 지원하기 어려운 이유를 설명할 수 있는가?
- [ ] 우회 경로 3개를 제시할 수 있는가?
- [ ] 포트폴리오 프로젝트에 customer outcome을 넣을 수 있는가?

#### 예상 시간 배분

- 개념 학습: 40분
- 실습 1: 90분
- 실습 2: 110분
- 문서화: 0-20분
- 합계: 4h

#### 참조 자료

- Cursor FDE: https://cursor.com/careers/forward-deployed-engineer - AI-native workflow production 경험의 중요성을 보여준다.
- Scale AI FDE GenAI: https://scale.com/careers/4593571005 - 2년 이상 관련 경험 선호 사례.

### M8 - IT 시니어 커리어 전환 로드맵

**난이도**: 2
**예상 시간**: 4h
**산출물 폴더**: `08-Senior-Transition/`

#### 학습 목표

- [ ] 기존 IT 시니어 경험을 FDE 역량으로 재해석할 수 있다.
- [ ] SI, consultant, PM, software engineer, solutions architect 출신별 전환 전략을 만들 수 있다.
- [ ] senior FDE 지원용 resume narrative를 작성할 수 있다.

#### 주요 개념

1. **Transferable experience**: 고객 문제 해결, 배포, 운영, stakeholder management 경험.
2. **AI gap**: 기존 IT 경험자는 AI/LLM production 패턴을 보완해야 한다.
3. **Outcome ownership**: 단순 구현보다 고객 성과까지 책임지는 서사.
4. **Field-to-product feedback**: 현장 문제를 reusable platform capability로 바꾸는 역량.

#### 실습 과제

**실습 1: 시니어 출신별 전환 맵**
- 목적: 경력 배경별 장단점을 구분한다.
- 단계: 1. SWE/SI/PM/Consultant/Solutions Architect 출신을 나눈다. 2. 강점, 약점, 보완 학습, target role을 적는다. 3. 90일 준비 계획을 만든다.
- 예상 시간: 100분
- 난이도: 2
- 검증: 5개 출신별 전환표가 완성된다.

**실습 2: senior FDE resume narrative**
- 목적: 경력 전환 메시지를 만든다.
- 단계: 1. 대표 프로젝트 3개를 고른다. 2. customer problem, technical action, production impact, reusable learning 구조로 재작성한다. 3. LinkedIn summary 초안을 만든다.
- 예상 시간: 100분
- 난이도: 2
- 검증: senior 지원자용 resume narrative 초안이 완성된다.

#### 산출물

```
08-Senior-Transition/
├── README.md
├── guides/
│   ├── senior-transition-map.md
│   └── ninety-day-transition-plan.md
└── examples/
    └── senior-resume-narrative.md
```

#### Definition of Done

- [ ] 시니어 출신별 전환표 작성
- [ ] 90일 준비 계획 작성
- [ ] resume narrative 작성
- [ ] README 업데이트
- [ ] WorkLog 작성

#### Self-Assessment

- [ ] 자신의 기존 경험을 FDE의 discovery-build-deploy-adoption 언어로 바꿀 수 있는가?
- [ ] AI/LLM production gap을 구체적으로 식별할 수 있는가?
- [ ] senior FDE와 junior FDE의 기대치 차이를 설명할 수 있는가?

#### 예상 시간 배분

- 개념 학습: 40분
- 실습 1: 100분
- 실습 2: 100분
- 문서화: 0-20분
- 합계: 4h

#### 참조 자료

- OpenAI FDE: https://openai.com/careers/forward-deployed-engineer-%28fde%29-seattle-seattle/ - 5년 이상 engineering/deployment/customer-facing 경험 요구.
- Hebbia FDE: https://jobs.ashbyhq.com/hebbia-ai/b35852eb-97ac-491a-b375-91fd13d0b7b3 - 5년 이상 full-stack, 고객 embedded, domain workflow 경험 요구.

### M9 - 비IT 배경자와 글로벌 Sub-study

**난이도**: 2
**예상 시간**: 4h
**산출물 폴더**: `09-Non-IT-Global-Context/`

#### 학습 목표

- [ ] 비IT 배경자가 FDE 자체에 바로 진입하기 어려운 지점과 가능한 우회 경로를 설명할 수 있다.
- [ ] 도메인 전문성이 FDE 생태계에서 어떤 역할로 전환될 수 있는지 정리할 수 있다.
- [ ] 한국 AX, 일본 DX to AX, 유럽 enterprise transformation 문맥을 미국 FDE와 비교할 수 있다.

#### 주요 개념

1. **Domain specialist path**: 금융, 헬스케어, 제조, 공공 도메인 지식을 AI deployment에 연결하는 경로.
2. **Technical minimum**: 비IT 배경자가 갖춰야 할 최소 API, data, workflow, AI literacy.
3. **AX context**: 한국에서 AI transformation이 SI/컨설팅/대기업 전환 프로젝트 언어로 쓰이는 흐름.
4. **Regional variation**: 미국은 role/title과 startup GTM 중심, 한국/일본은 transformation 담론 중심인 경향.

#### 실습 과제

**실습 1: 비IT 진입 경로 설계**
- 목적: 비IT 배경자에게 현실적 경로를 제시한다.
- 단계: 1. FDE 직행 가능성과 한계를 적는다. 2. domain solution specialist, AI consultant, implementation analyst, GTM engineer 등 우회 경로를 정리한다. 3. 12개월 준비 계획을 만든다.
- 예상 시간: 100분
- 난이도: 2
- 검증: 비IT 배경자용 단계별 준비표가 완성된다.

**실습 2: 미국 vs 한국/일본/유럽 비교**
- 목적: FDE와 AX를 혼동하지 않고 연결한다.
- 단계: 1. 미국 FDE 용례와 한국 AX 용례를 비교한다. 2. 일본 DX to AX 사례를 sub-study로 정리한다. 3. 유럽 regulated enterprise AI 문맥을 간단히 메모한다.
- 예상 시간: 100분
- 난이도: 2
- 검증: 국가별 용어/조직/프로젝트 차이가 표로 정리된다.

#### 산출물

```
09-Non-IT-Global-Context/
├── README.md
├── guides/
│   ├── non-it-entry-path.md
│   └── twelve-month-plan.md
└── concepts/
    └── us-fde-vs-global-ax-context.md
```

#### Definition of Done

- [ ] 비IT 배경자 진입 경로 작성
- [ ] 12개월 준비 계획 작성
- [ ] 미국/한국/일본/유럽 비교표 작성
- [ ] README 업데이트
- [ ] WorkLog 작성

#### Self-Assessment

- [ ] 비IT 배경자가 FDE가 되려면 어떤 기술 minimum이 필요한지 말할 수 있는가?
- [ ] 한국 AX와 미국 FDE의 관계를 "프로젝트/역할" 관점으로 설명할 수 있는가?
- [ ] 지역별 용어 차이가 커리어 전략에 주는 영향을 설명할 수 있는가?

#### 예상 시간 배분

- 개념 학습: 40분
- 실습 1: 100분
- 실습 2: 100분
- 문서화: 0-20분
- 합계: 4h

#### 참조 자료

- SK AX: https://www.skax.co.kr/insight/trend/3330 - 한국 AX 기업 전환 담론의 대표 사례.
- Gartner Japan DX to AX: https://www.gartner.com/en/conferences/apac/data-analytics-japan/sessions/detail/4585775-Executive-Story-From-DX-to-AX-Designing-Continuous-Transformation-with-Discontinuous-Leaps-at-Cosmo-Energy - 일본의 DX to AX 용례.

### M10 - 포트폴리오와 Remotion 영상화 Capstone

**난이도**: 3
**예상 시간**: 6h
**산출물 폴더**: `10-Capstone-Video/`

#### 학습 목표

- [ ] FDE 지망자를 위한 최종 가이드 패키지를 구성할 수 있다.
- [ ] FDE 포트폴리오 프로젝트를 customer scenario, architecture, demo, success metric 중심으로 설계할 수 있다.
- [ ] Remotion AI 영상 시리즈 제작을 위한 대본/스토리보드/장면 구성안을 만들 수 있다.

#### 주요 개념

1. **FDE portfolio**: 코드만이 아니라 고객 문제, 배포, adoption, metric을 함께 보여주는 증거물.
2. **Case narrative**: 문제, 제약, 선택지, 구현, 결과를 이야기 구조로 설명하는 방식.
3. **Video curriculum**: 학습 결과를 시청자가 따라갈 수 있는 영상 시리즈로 재구성하는 방법.
4. **Remotion handoff**: Markdown 기반 학습 산출물을 영상 대본과 장면 지시로 넘기는 과정.

#### 실습 과제

**실습 1: FDE 포트폴리오 프로젝트 스펙**
- 목적: 지원자가 실제로 만들 수 있는 포트폴리오를 설계한다.
- 단계: 1. enterprise customer scenario 3개를 만든다. 2. 각 시나리오에 architecture, stack, eval, rollout, metric을 붙인다. 3. README와 demo script 구조를 만든다.
- 예상 시간: 140분
- 난이도: 3
- 검증: 바로 구현 가능한 project spec 3개가 완성된다.

**실습 2: Remotion 영상 시리즈 구성**
- 목적: Topic 결과를 영상 제작으로 연결한다.
- 단계: 1. 6편 시리즈 제목과 핵심 메시지를 정한다. 2. 각 편의 scene outline, visual asset, narration bullet을 만든다. 3. Remotion 제작용 handoff 문서를 만든다.
- 예상 시간: 160분
- 난이도: 3
- 검증: 영상 제작자가 바로 다음 단계로 들어갈 수 있는 스토리보드가 완성된다.

#### 산출물

```
10-Capstone-Video/
├── README.md
├── guides/
│   ├── fde-portfolio-guide.md
│   └── fde-interview-prep.md
├── examples/
│   └── portfolio-project-specs.md
└── video/
    ├── remotion-series-outline.md
    ├── episode-scripts.md
    └── visual-storyboard.md
```

#### Definition of Done

- [ ] 포트폴리오 프로젝트 3개 spec 작성
- [ ] FDE 지원자 최종 가이드 패키지 목차 작성
- [ ] Remotion 영상 6편 outline 작성
- [ ] episode script 초안 작성
- [ ] visual storyboard 작성
- [ ] README 업데이트
- [ ] Topic Retrospective 작성

#### Self-Assessment

- [ ] FDE 포트폴리오가 일반 SWE 포트폴리오와 다른 점을 설명할 수 있는가?
- [ ] 영상 1편의 핵심 메시지를 30초 hook으로 만들 수 있는가?
- [ ] Remotion AI에게 장면, 내레이션, 시각 자료를 명확히 지시할 수 있는가?

#### 예상 시간 배분

- 개념 학습: 50분
- 실습 1: 140분
- 실습 2: 160분
- 문서화: 10분
- 합계: 6h

#### 참조 자료

- Cursor FDE: https://cursor.com/careers/forward-deployed-engineer - production-grade AI workflow 포트폴리오 방향에 적합하다.
- OpenAI FDSWE: https://openai.com/careers/forward-deployed-software-engineer-sf-san-francisco/ - customer problem을 custom software로 해결하는 포트폴리오 기준에 유용하다.

## WorkLog 작성 가이드

각 학습 세션마다 WorkLog를 작성하여 진행 상황을 추적한다.

**파일명 규칙**: `vl_worklog/YYYYMMDD_MX_FDE-Forward-Deployed-Engineer.md`

**WorkLog 필수 섹션**:

1. 오늘의 학습 목표
2. 진행 내용
3. 문제 해결 로그
4. DoD 체크리스트
5. Daily Retrospective
6. 참조 및 산출물

## Retrospective 가이드

### Daily Retrospective

매일 WorkLog 안에 작성한다. 오늘 잘된 점, 개선할 점, 핵심 인사이트, 다음 세션의 focus를 기록한다.

### Module Retrospective

모듈 완료 시 `vl_worklog/YYYYMMDD_MX_Retrospective.md`에 작성한다. 계획 대비 실제 소요, 산출물 품질, Roadmap 수정 필요 여부, 다음 모듈 준비사항을 기록한다.

### Topic Retrospective

전체 Topic 완료 시 `vl_worklog/YYYYMMDD_FDE-Forward-Deployed-Engineer_Final_Retrospective.md`에 작성한다. 학습 여정, 산출물 품질, 영상화 가능성, 다음 Topic으로 이어질 질문을 정리한다.

## 전체 폴더 구조

```
FDE-Forward-Deployed-Engineer/
├── topic_info.md
├── vl_prompts/
│   ├── roadmap_prompt.md
│   └── daily_learning_prompt.md
├── vl_roadmap/
│   └── 20260816_RoadMap_FDE-Forward-Deployed-Engineer.md
├── vl_worklog/
├── vl_materials/
├── 01-FDE-Basics/
├── 02-Palantir-Origin/
├── 03-US-Company-Models/
├── 04-Role-Taxonomy/
├── 05-AI-FDE-Tech-Stack/
├── 06-US-Job-Market/
├── 07-Junior-Track/
├── 08-Senior-Transition/
├── 09-Non-IT-Global-Context/
└── 10-Capstone-Video/
```

## 학습 진행 상황 추적

| 모듈 | 시작일 | 종료일 | 상태 | DoD 달성률 | 비고 |
|---|---|---|---|---:|---|
| M1 | 2026-08-16 | 2026-08-16 | 완료 | 100% | daily_learning_prompt 기준 재점검 및 학습 활동 보강 완료 |
| M2 | 2026-08-16 | 2026-08-16 | 완료 | 100% | daily_learning_prompt 기준 재점검 및 Palantir 원형 실습 보강 완료 |
| M3 | 2026-08-16 | 2026-08-16 | 완료 | 100% | daily_learning_prompt 기준 재점검 및 기업별 archetype 실습 보강 완료 |
| M4 | 2026-08-16 | 2026-08-16 | 완료 | 100% | daily_learning_prompt 기준 재점검 및 유사 직무 판별 실습 보강 완료 |
| M5 | 2026-08-16 | 2026-08-16 | 완료 | 100% | daily_learning_prompt 기준 재점검 및 production lifecycle 실습 보강 완료 |
| M6 | | | 대기 | 0% | |
| M7 | | | 대기 | 0% | |
| M8 | | | 대기 | 0% | |
| M9 | | | 대기 | 0% | |
| M10 | | | 대기 | 0% | |

## 성공 기준

- [ ] 모든 모듈 완료
- [ ] 최소 10개 산출물 폴더 생성
- [ ] 기업별 FDE 모델 비교 리포트 완성
- [ ] 미국 FDE 채용시장 분석표 완성
- [ ] FDE 역량 매트릭스 완성
- [ ] 학생/주니어, IT 시니어, 비IT 배경자 준비 가이드 완성
- [ ] FDE 포트폴리오 프로젝트 가이드 완성
- [ ] Remotion AI 영상 제작용 시리즈 outline, 대본, 스토리보드 완성
- [ ] Topic Retrospective 작성

## 다음 학습 세션 제안

첫 세션은 M1부터 시작한다. 목표는 "FDE를 정확히 정의하고, 왜 AI 시대에 다시 부상했는지 설명하는 2분 설명문"을 만드는 것이다. 첫 세션 예상 시간은 2-3시간이며, 산출물은 `01-FDE-Basics/concepts/fde-definition.md`, `01-FDE-Basics/concepts/fde-history-timeline.md`, `01-FDE-Basics/examples/two-minute-explanation.md`이다.

**생성자**: Codex with VibeLearn AI
**Roadmap 버전**: 1.0
**방법론 버전**: VibeLearn AI 2.0








