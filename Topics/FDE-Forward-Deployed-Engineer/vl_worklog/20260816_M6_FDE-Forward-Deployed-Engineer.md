# 2026-08-16 M6 WorkLog - 미국 채용 공고 기반 역량 분석

## 오늘의 학습 목표

- VibeLearn AI daily learning 절차에 따라 사용자 승인 후 M6를 다시 진행한다.
- 미국 FDE 및 유사 직무 채용 공고를 데이터처럼 추출한다.
- 공통 역량 top 10을 도출한다.
- compensation, seniority, location, travel, clearance 조건을 지원 전략에 연결한다.
- 면접 루프 가설과 대비 질문을 만든다.

## 진행 내용

### 1. 절차 복구 및 승인

이전 M6 초안은 사용자 승인 없이 작성되어 VibeLearn AI 절차상 문제가 있었다. 사용자가 지적한 후 M6 현재 상태와 오늘의 학습 계획을 다시 제시했고, 사용자의 명시적 승인 후 재진행했다.

### 2. 최신 공고 재확인

2026-08-16 기준으로 OpenAI, Anthropic, Scale AI, Cursor의 공개 채용 페이지를 확인했다. OpenAI는 Seattle FDE, SF Forward Deployed Software Engineer, Gov FDE를 확인했고, Anthropic은 FDE와 Applied AI Engineer를 확인했다. Scale AI는 Frontier Agents Engineer FDE, Senior Frontier Agents Engineer FDE, GenAI FDE를 확인했으며, Cursor는 FDE와 careers listing의 인접 role들을 확인했다.

### 3. M6 산출물 폴더 생성

`06-US-Job-Market/` 폴더와 하위 `examples/`, `guides/` 폴더를 생성했다. 로드맵 산출물 구조에 맞춰 README, 공고 분석표, 면접 루프 가이드, 보상/지역 노트를 작성했다.

### 4. Job posting extraction sheet 재작성

`examples/us-fde-job-posting-analysis.md`에 10개 행의 분석표를 작성했다. 각 행은 company, role, location, years, stack, domain signal, travel/onsite, salary signal, role archetype을 포함한다. Hebbia 공고는 JS 렌더링으로 본문을 안정적으로 확인하지 못해 이번 분석표의 핵심 행에는 넣지 않고, 확인 가능한 공개 공고 중심으로 작성했다.

### 5. 공통 역량 top 10 도출

반복 역량은 production-grade engineering, customer-facing delivery, ambiguity scoping, full-stack fluency, LLM/agent implementation, evals, enterprise integration, security/governance, reusable pattern codification, communication으로 정리했다.

### 6. Interview loop 및 compensation notes 작성

`guides/fde-interview-loop-guide.md`에는 recruiter, HM, coding, system design, customer scenario, portfolio demo, leadership loop를 정리했다. `guides/compensation-and-location-notes.md`에는 공개 salary range와 location/travel/clearance 해석을 정리했다.

## 문제 해결 로그

- 문제: 이전 M6 작업은 사용자 승인 전 실행되어 VibeLearn AI daily learning 절차를 어겼다.
- 해결: M6 계획을 다시 제시하고 사용자 승인 후 산출물을 승인된 실행 결과로 보강했다.
- 문제: 일부 공고는 JS 렌더링 또는 redirect 때문에 본문을 안정적으로 확인하기 어려웠다.
- 해결: 2026-08-16 현재 직접 본문 확인 가능한 공개 공고를 우선 사용하고, 접근 제한이 있는 공고는 추정 근거로 사용하지 않았다.

## DoD 체크리스트

- [x] 10개 공고 분석표 작성
- [x] 공통 역량 top 10 도출
- [x] 면접 유형별 대비 가이드 작성
- [x] README 업데이트
- [x] WorkLog 작성
- [x] compensation/location/travel/clearance notes 작성
- [x] 사용자 승인 후 재진행 기록 반영

## Daily Retrospective

### 오늘 배운 것

FDE 공고에서 가장 강한 신호는 "AI를 안다"가 아니라 "고객 조직 안에서 production AI system을 책임지고 adoption까지 만든다"는 점이다. 회사별로 OpenAI는 research/product feedback loop, Anthropic은 Claude enterprise deployment와 safety, Scale은 production agent systems, Cursor는 developer workflow transformation에 무게가 있다.

### 잘한 점

M4의 role taxonomy와 M5의 production lifecycle을 공고 분석에 연결했다. 절차 오류를 복구하면서 M6 산출물에 승인 기반 재진행 기록도 남겼다.

### 개선할 점

앞으로 daily learning 단계에서는 사용자가 "계속 진행"이라고 하더라도 Step 3의 학습 계획 제시와 승인 대기를 생략하지 않아야 한다. M7에서는 학생/주니어 관점에서 senior-level 요구사항을 현실적인 milestone으로 낮춰 번역해야 한다.

### Tomorrow's Focus

- M7 학생/주니어 준비 로드맵을 작성한다.
- M6의 top 10 역량을 junior-friendly milestone으로 낮춰 번역한다.
- 6개월 포트폴리오 계획과 entry path decision tree를 만든다.

## 참조 및 산출물

- `06-US-Job-Market/README.md`
- `06-US-Job-Market/examples/us-fde-job-posting-analysis.md`
- `06-US-Job-Market/guides/fde-interview-loop-guide.md`
- `06-US-Job-Market/guides/compensation-and-location-notes.md`
- `vl_roadmap/20260816_RoadMap_FDE-Forward-Deployed-Engineer.md`
