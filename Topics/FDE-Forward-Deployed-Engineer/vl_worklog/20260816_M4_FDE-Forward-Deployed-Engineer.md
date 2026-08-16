# WorkLog - M4: FDE와 유사 직무 비교

**날짜**: 2026-08-16
**Topic**: FDE-Forward-Deployed-Engineer
**모듈**: M4 - FDE와 유사 직무 비교
**학습 시간**: 06:52 - 06:55 (총 3분, 초안 작성 세션)
**방법론**: VibeLearn AI

## 오늘의 학습 목표

- [x] FDE와 유사 직무 8개를 비교할 수 있다.
- [x] 직무명만 보고 실제 업무를 오판하지 않는 기준을 만들 수 있다.
- [x] 지원자가 자신의 기존 경험을 FDE 언어로 재포장할 수 있다.

## 진행 내용

### 1. Role taxonomy 작성

**목적**:
M3에서 정리한 FDE archetype을 주변 직무군과 연결하여, FDE가 어디에 위치하는지 명확히 한다.

**진행 내용**:
1. customer-facing 정도와 production coding 정도를 2축으로 설정했다.
2. FDE, FDSE, Applied AI Engineer, Solutions Engineer, Sales Engineer, Solutions Architect, Consultant, ML Engineer, Product Engineer, Technical Account Manager를 비교했다.
3. 각 직무가 FDE와 가까워지는 조건과 멀어지는 조건을 정리했다.

**핵심 결과**:
FDE는 customer-facing도 높고 production coding도 높은 역할이다. 주변 직무가 FDE와 가까워지려면 customer embedding, production build, deployment ownership, adoption metric, product feedback loop가 필요하다.

### 2. 직무명 읽기 가이드 작성

**목적**:
채용 공고 title만 보고 FDE 여부를 오판하지 않도록 판별 기준을 제공한다.

**진행 내용**:
- "build full-stack systems", "write production code", "embed with customers", "production adoption", "field feedback" 같은 표현을 FDE 판별 신호로 정리했다.
- Applied AI Architect, Solutions Engineer, Solutions Architect, AI Deployment Manager 같은 직무명을 읽을 때 확인해야 할 항목을 만들었다.

### 3. Resume bullet 변환 예시 작성

**목적**:
지원자가 기존 경력을 FDE식 언어로 재구성할 수 있게 한다.

**진행 내용**:
- SWE, backend, data engineer, ML engineer, solutions engineer, consultant, SI/implementation, PM, 비IT 도메인 전문가 출신 예시를 작성했다.
- 단순 업무 나열을 customer problem, technical action, deployment context, measurable outcome, reusable learning 구조로 바꾸는 방식을 제시했다.

## 문제 해결 로그

### 문제 1: 유사 직무 경계가 회사마다 다름

**증상**:
Applied AI Engineer, Solutions Architect, Solutions Engineer 같은 직무는 회사마다 실제 업무 범위가 크게 다르다.

**원인**:
AI 기업들이 아직 role taxonomy를 표준화하지 않았고, GTM/engineering/product 조직 구조에 따라 같은 title이 다르게 쓰인다.

**해결**:
title이 아니라 책임 범위와 ownership 기준으로 판별하도록 가이드를 작성했다. 핵심 기준은 direct build, customer embed, production rollout, adoption metric, product feedback loop다.

## DoD 체크리스트

- [x] 직무 taxonomy 작성
- [x] 2축 role map 작성
- [x] resume bullet 변환 예시 10개 작성
- [x] README 업데이트
- [x] WorkLog 작성

**완료율**: 5/5 (100%)

## Daily Retrospective

### What went well

- FDE와 주변 직무의 차이를 title이 아니라 ownership 관점으로 정리했다.
- 이후 학생/주니어, 시니어 전환, 비IT 전환 모듈에서 재사용할 resume bullet 변환 프레임을 만들었다.

### What could be improved

- M6에서 실제 공고 10개 이상을 분석할 때 이 taxonomy를 검증해야 한다.
- M7-M9에서 각 배경별 bullet 예시를 더 구체적인 포트폴리오 프로젝트와 연결하면 좋다.

### Insights

- FDE를 가장 잘 구분하는 질문은 "이 사람이 무엇을 끝까지 책임지는가?"이다.
- 책임의 끝이 demo나 deal support라면 FDE가 아니고, 책임의 끝이 production adoption과 measurable workflow impact라면 FDE에 가깝다.

### Tomorrow's focus

- M5 - AI FDE 기술 스택과 실무 흐름을 진행한다.
- discovery, scoping, prototype, eval, integration, rollout, handoff lifecycle을 만든다.
- junior/senior/non-IT 트랙별 기술 스택 깊이를 구분한다.

## 참조 및 산출물

**참조 자료**:
- M1-M3에서 수집한 OpenAI, Palantir, Anthropic, Scale AI, Cursor, Hebbia 채용 설명.

**생성된 파일/폴더**:
- `04-Role-Taxonomy/README.md`: M4 학습 순서와 요약.
- `04-Role-Taxonomy/concepts/role-taxonomy.md`: FDE와 유사 직무 비교.
- `04-Role-Taxonomy/guides/role-title-reading-guide.md`: 채용 공고 판독 가이드.
- `04-Role-Taxonomy/examples/resume-bullet-transformations.md`: FDE형 resume bullet 변환 예시.

**다음 세션 준비사항**:
- M5에서 AI FDE delivery lifecycle을 설계한다.
- 기술 스택을 frontend/backend/data/cloud/LLM/evals/security로 나눈다.
