# WorkLog - M3: 미국 AI 기업별 FDE 모델 비교

**날짜**: 2026-08-16
**Topic**: FDE-Forward-Deployed-Engineer
**모듈**: M3 - 미국 AI 기업별 FDE 모델 비교
**학습 시간**: 06:43 - 06:51 (총 8분, 초안 작성 세션)
**방법론**: VibeLearn AI

## 오늘의 학습 목표

- [x] OpenAI, Anthropic, Scale AI, Cursor, Hebbia의 FDE/유사 직무를 비교할 수 있다.
- [x] 기업별 FDE가 product, GTM, customer success, engineering 중 어디에 가까운지 분류할 수 있다.
- [x] 회사별 특색을 지원자 관점의 준비 전략으로 번역할 수 있다.

## 진행 내용

### 1. 기업별 자료 확인

**목적**:
FDE가 미국 AI/테크 기업마다 어떻게 다른지 현재 채용 설명을 기준으로 비교하기 위해 자료를 확인했다.

**확인한 자료**:
1. OpenAI Forward Deployed Engineer
2. Scale AI Forward Deployed Engineer, GenAI
3. Scale AI Senior Forward Deployed AI Engineer, Enterprise
4. Cursor Forward Deployed Engineer
5. Cursor RVP Forward Deployed Engineering
6. Anthropic Applied AI Architect, Enterprise Tech
7. Anthropic careers Applied AI role list
8. Hebbia Forward Deployed Engineer
9. Palantir FDSE/Deployment Strategist 자료(M2)

**핵심 확인 내용**:
- OpenAI: frontier model을 production system으로 가져가는 AI Lab FDE.
- Anthropic: FDE보다는 Applied AI Architect/Advisor 계열이 강하고 pre-sales technical architecture 성격이 있다.
- Scale AI: data, eval, agent infrastructure를 고객 환경에 붙이는 Data·Agent Infrastructure FDE.
- Cursor: 고객 개발팀의 AI-native engineering workflow를 만드는 Developer Workflow FDE.
- Hebbia: finance/investment workflow에 platform last mile을 만드는 Vertical Workflow FDE.
- Palantir: operational platform FDE의 원형.

### 2. M3 산출물 작성

**생성된 파일**:
- `03-US-Company-Models/README.md`
- `03-US-Company-Models/concepts/fde-company-archetypes.md`
- `03-US-Company-Models/examples/company-comparison-matrix.md`
- `03-US-Company-Models/guides/candidate-fit-selector.md`

**핵심 인사이트**:
FDE는 하나의 표준 직무라기보다 고객 현장형 AI/product engineering의 여러 변형이다. 지원자는 직무명보다 회사의 제품, 고객, GTM 구조, 코딩 비중, 성공 지표, field feedback loop를 보고 판단해야 한다.

## 문제 해결 로그

### 문제 1: 일부 직무 페이지 접근 제한 또는 동적 렌더링

**증상**:
Cursor와 Hebbia 일부 페이지는 직접 open 결과가 제한적이거나 검색 결과에 더 많은 내용이 노출되었다.

**원인**:
채용 페이지가 동적 렌더링 또는 crawler 노출 방식 차이에 의존한다.

**해결**:
접근 가능한 공식 채용 페이지, 검색 결과에 노출된 채용 설명, Greenhouse/Ashby/Lever mirror를 함께 사용했다. M3 문서에는 특히 OpenAI, Scale AI, Palantir처럼 직접 열람 가능한 원문을 강한 근거로 두고, Cursor/Hebbia는 검색 결과 요약을 보조 근거로 사용했다.

## DoD 체크리스트

- [x] 5개 이상 기업 비교표 작성
- [x] FDE archetype 4개 이상 정의
- [x] 지원자-fit 판단 도구 작성
- [x] README 업데이트
- [x] WorkLog 작성

**완료율**: 5/5 (100%)

## Daily Retrospective

### What went well

- FDE를 Palantir, OpenAI, Anthropic, Scale AI, Cursor, Hebbia의 6개 archetype으로 분류했다.
- 지원자가 자신의 배경과 선호를 기준으로 목표 FDE 유형을 고를 수 있는 질문지를 만들었다.
- M4에서 유사 직무 비교로 확장할 기준이 생겼다.

### What could be improved

- M6 미국 채용시장 분석 단계에서는 10개 이상의 공고를 spreadsheet 형태로 더 촘촘히 추출해야 한다.
- Anthropic은 FDE라는 명칭보다 Applied AI/Solutions Architecture 명칭이 섞여 있으므로 M4에서 유사 직무와의 경계를 더 명확히 해야 한다.

### Insights

- FDE 채용에서 가장 중요한 질문은 "이 회사에서 FDE가 무엇을 소유하는가?"이다. 어떤 회사는 production code를 소유하고, 어떤 회사는 architecture와 adoption journey를 소유한다.
- Cursor 사례는 FDE가 일반 기업 workflow뿐 아니라 개발팀 workflow 자체를 AI-native하게 바꾸는 역할로 확장되고 있음을 보여준다.
- Scale AI 사례는 AI FDE가 model app builder가 아니라 data/eval/agent infrastructure builder일 수도 있음을 보여준다.

### Tomorrow's focus

- M4 - FDE와 유사 직무 비교를 진행한다.
- FDE, Applied AI Engineer, Solutions Engineer, Sales Engineer, Solutions Architect, Consultant, ML Engineer, Product Engineer를 customer-facing 정도와 coding 정도 기준으로 배치한다.
- 기존 경력을 FDE형 resume bullet로 바꾸는 예시를 만든다.

## 참조 및 산출물

**참조 자료**:
- [OpenAI FDE - Seattle](https://openai.com/careers/forward-deployed-engineer-%28fde%29-seattle-seattle/): AI Lab FDE 기준.
- [Scale AI FDE, GenAI](https://scale.com/careers/4593571005): Data·Agent Infrastructure FDE 기준.
- [Scale AI Senior Forward Deployed AI Engineer](https://job-boards.greenhouse.io/scaleai/jobs/4597399005): enterprise AI agent/integration/eval 사례.
- [Cursor FDE](https://cursor.com/careers/forward-deployed-engineer): Developer Workflow FDE 기준.
- [Cursor RVP FDE](https://cursor.com/de/careers/rvp-forward-deployed-engineering-emea): FDE 조직화와 day-30 impact 관점.
- [Anthropic Applied AI Architect](https://job-boards.greenhouse.io/anthropic/jobs/5065835008): Applied AI Architect/Advisor 기준.
- [Hebbia FDE](https://jobs.ashbyhq.com/hebbia-ai/b35852eb-97ac-491a-b375-91fd13d0b7b3/): Vertical Workflow FDE 기준.

**생성된 파일/폴더**:
- `03-US-Company-Models/README.md`: M3 학습 순서와 요약.
- `03-US-Company-Models/concepts/fde-company-archetypes.md`: 6개 FDE archetype.
- `03-US-Company-Models/examples/company-comparison-matrix.md`: 회사별 비교 매트릭스.
- `03-US-Company-Models/guides/candidate-fit-selector.md`: 지원자-fit 선택 가이드.

**다음 세션 준비사항**:
- M4에서 FDE와 유사 직무를 비교할 2축 맵을 만든다.
- M3의 archetype을 FDE 주변 직무군과 연결한다.
