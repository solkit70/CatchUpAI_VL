# WorkLog - M1: FDE 기본 정의와 역사

**날짜**: 2026-08-16
**Topic**: FDE-Forward-Deployed-Engineer
**모듈**: M1 - FDE 기본 정의와 역사
**학습 시간**: 06:20 - 06:32 (총 12분, 초안 작성 세션)
**방법론**: VibeLearn AI

## 오늘의 학습 목표

- [x] FDE를 2문장으로 정의할 수 있다.
- [x] FDE가 software engineer, consultant, solutions engineer와 다른 지점을 설명할 수 있다.
- [x] AI 시대에 FDE가 다시 주목받는 이유를 3가지로 정리할 수 있다.

## 진행 내용

### 1. M1 source 확인

**목적**:
FDE 정의를 추측이 아니라 현재 기업 채용 설명에 근거해 정리하기 위해 공식/채용 자료를 확인했다.

**과정**:
1. OpenAI FDE 채용 페이지를 확인했다.
2. Scale AI GenAI FDE 채용 페이지를 확인했다.
3. Cursor FDE와 Hebbia FDE는 검색 결과 및 채용 설명 요약을 참고했다.
4. 각 회사의 FDE 설명에서 반복되는 요소를 추출했다.

**결과**:
- OpenAI형 FDE: frontier model production deployment, discovery/scoping/system design/build/rollout, product/model roadmap feedback.
- Scale AI형 FDE: GenAI data infrastructure, customer/operator-specific infrastructure, full-stack delivery, enterprise/government AI data problems.
- Cursor형 FDE: customer engineering team embedded, production-grade AI coding workflows, evals/tracing/model behavior debugging.
- Hebbia형 FDE: vertical workflow, finance/customer-specific last-mile integration.

### 2. M1 산출물 작성

**목적**:
다음 학습자가 M1 폴더만 열어도 FDE 기본 개념을 학습할 수 있도록 교재형 산출물을 만든다.

**생성된 파일**:
- `01-FDE-Basics/README.md`
- `01-FDE-Basics/concepts/fde-definition.md`
- `01-FDE-Basics/concepts/fde-history-timeline.md`
- `01-FDE-Basics/examples/two-minute-explanation.md`

**핵심 인사이트**:
FDE는 새로운 이름의 단순 영업/컨설팅 직무가 아니라, 고객 현장의 문제를 production system으로 바꾸는 engineering delivery role이다. AI 시대에는 이 역할이 LLM, agent, RAG, eval, workflow automation, enterprise data integration을 고객 환경에 맞게 적용하는 방향으로 확장되고 있다.

## 문제 해결 로그

### 문제 1: 일부 채용 페이지의 JavaScript 렌더링

**증상**:
Hebbia 채용 페이지는 브라우저 JavaScript 활성화가 필요하다는 응답만 반환했다.

**원인**:
채용 페이지가 client-side rendering에 의존한다.

**해결**:
검색 결과에 노출된 채용 설명 요약과 이미 Roadmap 생성 시 확인한 검색 결과를 M1의 보조 근거로 사용했다. 핵심 정의는 접근 가능한 OpenAI와 Scale AI 원문을 우선 근거로 삼았다.

## DoD 체크리스트

- [x] FDE 정의 문서 작성
- [x] 역사 타임라인 작성
- [x] 2분 설명문 작성
- [x] README에 학습 순서와 문서 링크 정리
- [x] WorkLog 작성

**완료율**: 5/5 (100%)

## Daily Retrospective

### What went well

- OpenAI와 Scale AI의 현재 채용 설명을 기준으로 FDE의 핵심 정의를 정리했다.
- M1 산출물을 정의, 역사, 설명문으로 나누어 다음 모듈의 기반 자료로 재사용할 수 있게 만들었다.

### What could be improved

- M2에서는 Palantir 원형을 더 정확히 다루기 위해 Palantir 공식 자료와 관련 공고를 추가로 확인해야 한다.
- Cursor와 Hebbia는 접근 가능한 원문 또는 별도 채용 mirror를 더 찾아서 M3에서 기업별 비교의 근거를 강화해야 한다.

### Insights

- AI FDE의 핵심 성공 기준은 "모델을 붙였다"가 아니라 "고객 workflow에서 반복 사용되고, 측정 가능한 impact가 생겼고, 그 feedback이 제품 개선으로 돌아갔다"에 있다.
- 회사별 FDE는 이름은 같아도 실제 업무 중심축이 다르다. OpenAI는 frontier model deployment, Scale AI는 data/eval infrastructure, Cursor는 developer workflow, Hebbia는 finance vertical workflow에 가깝다.

### Tomorrow's focus

- M2 - Palantir 모델과 FDE의 원형을 진행한다.
- Palantir식 FDE와 Deployment Strategist의 관계를 정리한다.
- Palantir 원형과 AI FDE의 "바뀐 것/안 바뀐 것" 비교표를 만든다.

## 참조 및 산출물

**참조 자료**:
- [OpenAI FDE - Seattle](https://openai.com/careers/forward-deployed-engineer-%28fde%29-seattle-seattle/): frontier model production deployment와 FDE의 role scope.
- [Scale AI FDE, GenAI](https://scale.com/careers/4593571005): GenAI data infrastructure 중심 FDE 사례.
- [Cursor FDE](https://cursor.com/careers/forward-deployed-engineer): developer workflow 중심 FDE 사례.
- [Hebbia FDE](https://jobs.ashbyhq.com/hebbia-ai/b35852eb-97ac-491a-b375-91fd13d0b7b3): vertical AI workflow형 FDE 사례.

**생성된 파일/폴더**:
- `01-FDE-Basics/README.md`: M1 학습 순서와 요약.
- `01-FDE-Basics/concepts/fde-definition.md`: FDE 정의와 AI 시대 의미.
- `01-FDE-Basics/concepts/fde-history-timeline.md`: FDE 역사 타임라인.
- `01-FDE-Basics/examples/two-minute-explanation.md`: 한국어/영어 2분 설명문.

**다음 세션 준비사항**:
- Palantir FDE 및 Deployment Strategist 자료 확인.
- Accenture/Palantir 관련 채용 공고의 responsibilities를 업무 단위로 분해.
- M2 비교표의 축을 product, customer, technology, success metric으로 설정.
