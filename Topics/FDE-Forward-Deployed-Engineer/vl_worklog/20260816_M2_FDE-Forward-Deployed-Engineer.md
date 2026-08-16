# WorkLog - M2: Palantir 모델과 FDE의 원형

**날짜**: 2026-08-16
**Topic**: FDE-Forward-Deployed-Engineer
**모듈**: M2 - Palantir 모델과 FDE의 원형
**학습 시간**: 06:33 - 06:42 (총 9분, 초안 작성 세션)
**방법론**: VibeLearn AI

## 오늘의 학습 목표

- [x] Palantir식 FDE의 핵심 구조를 설명할 수 있다.
- [x] Deployment Strategist와 FDE의 관계를 정리할 수 있다.
- [x] Palantir 원형이 AI 기업 FDE와 어떻게 달라졌는지 비교할 수 있다.

## 진행 내용

### 1. Palantir source 확인

**목적**:
FDE 원형을 현재 Palantir 채용 설명에 근거해 정리하기 위해 Palantir 공식 careers 및 Lever job posting을 확인했다.

**확인한 자료**:
1. Palantir Careers open positions
2. Palantir FDSE New Grad - Commercial
3. Palantir FDSE New Grad - US Government
4. Palantir Deployment Strategist - Korea Forward Deployed

**핵심 확인 내용**:
- Palantir는 FDSE를 `Delta`, Deployment Strategist를 `Echo`로 구분한다.
- FDSE는 고객 outcome에 대한 radical commitment, customer reality에 embedded되는 태도, end-to-end ownership을 강조한다.
- FDSE는 custom applications, LLM workflows, production solutions를 특정 고객 현실에 맞게 만든다.
- Deployment Strategist는 고객 workflow, 데이터 의미, 사용자 동기, impact 위치를 종합하고, FDE와 함께 stable/extensible pipeline 및 bespoke workflow를 만든다.

### 2. M2 산출물 작성

**목적**:
M3 기업별 FDE 모델 비교에 사용할 기준을 만들기 위해 Palantir 원형을 구조화했다.

**생성된 파일**:
- `02-Palantir-Origin/README.md`
- `02-Palantir-Origin/concepts/palantir-fde-origin.md`
- `02-Palantir-Origin/examples/original-vs-ai-fde-comparison.md`

**핵심 인사이트**:
Palantir식 FDE는 단순 파견 개발자가 아니라 customer outcome을 자기 책임처럼 받아들이는 field product engineer에 가깝다. AI FDE는 이 원형을 그대로 이어받되, 다루는 실패 원인과 산출물이 LLM behavior, eval, RAG, agent, AI governance로 확장된다.

## 문제 해결 로그

### 문제 1: Palantir 공식 careers 일부 페이지가 짧게만 수집됨

**증상**:
Palantir students/early talent 페이지는 web open 결과가 sitemap/iframe 수준으로만 나왔다.

**원인**:
페이지 일부가 동적 렌더링에 의존하는 것으로 보인다.

**해결**:
검색 결과 snippet과 직접 열람 가능한 Lever job posting을 우선 근거로 사용했다. 핵심 내용은 FDSE Commercial, FDSE US Government, Deployment Strategist Korea Forward Deployed 페이지에서 확인했다.

## DoD 체크리스트

- [x] Palantir 원형 분석 문서 작성
- [x] 원형 vs AI FDE 비교표 작성
- [x] 다음 모듈에서 쓸 비교 기준 확정
- [x] README 업데이트
- [x] WorkLog 작성

**완료율**: 5/5 (100%)

## Daily Retrospective

### What went well

- Palantir식 FDSE와 Deployment Strategist의 역할 분담을 명확히 나누었다.
- M3에서 기업별 FDE를 비교할 수 있도록 고객 유형, 핵심 기술, 업무 범위, 코딩 비중, 제품 환류, 성공 지표, 요구 경력, 현장성 기준을 만들었다.

### What could be improved

- Palantir의 product ontology, Foundry/AIP, Apollo 같은 제품 구조를 더 깊게 이해하면 M2의 해상도가 올라간다.
- M3에서는 Palantir를 기준점으로 두고 OpenAI, Anthropic, Scale AI, Cursor, Hebbia의 차이를 더 세밀하게 분석해야 한다.

### Insights

- Palantir 원형에서 FDE와 Deployment Strategist는 각각 "만드는 힘"과 "문제/사용/impact를 구조화하는 힘"을 대표한다.
- AI FDE를 이해할 때도 technical builder와 deployment strategist적 감각을 함께 봐야 한다.

### Tomorrow's focus

- M3 - 미국 AI 기업별 FDE 모델 비교를 진행한다.
- OpenAI, Anthropic, Scale AI, Cursor, Hebbia, Palantir를 같은 기준표로 비교한다.
- 각 회사별 FDE archetype을 명명한다.

## 참조 및 산출물

**참조 자료**:
- [Palantir FDSE New Grad - Commercial](https://jobs.lever.co/palantir/2e6b0ac8-83e9-4be5-a3aa-cf319f751728): Palantir식 FDE의 customer outcome, embedded, product boundary 확장 설명.
- [Palantir FDSE New Grad - US Government](https://jobs.lever.co/palantir/cbe90327-3e6e-451c-a54c-1d3cbcef5aeb): open-ended mission problem과 end-to-end execution 설명.
- [Palantir Deployment Strategist - Korea Forward Deployed](https://jobs.lever.co/palantir/1a53939d-8ffa-4570-b31a-6d0bc53fdb59): Deployment Strategist와 FDE의 협업 구조 설명.

**생성된 파일/폴더**:
- `02-Palantir-Origin/README.md`: M2 학습 순서와 요약.
- `02-Palantir-Origin/concepts/palantir-fde-origin.md`: Palantir식 FDE 원형 분석.
- `02-Palantir-Origin/examples/original-vs-ai-fde-comparison.md`: Palantir 원형과 AI FDE 비교표.

**다음 세션 준비사항**:
- M3 기업별 비교를 위해 OpenAI, Anthropic, Scale AI, Cursor, Hebbia 자료를 같은 기준으로 재확인한다.
- 각 회사별 role archetype을 `AI Lab FDE`, `Developer Workflow FDE`, `Data Infrastructure FDE`, `Vertical AI FDE`, `Operational Platform FDE`로 가설 설정한다.
