# WorkLog - M2 Rerun: Palantir 모델과 FDE의 원형

**날짜**: 2026-08-16
**Topic**: FDE-Forward-Deployed-Engineer
**모듈**: M2 - Palantir 모델과 FDE의 원형
**학습 시간**: 07:10 - 07:14 (총 4분, 재점검 및 보강 세션)
**방법론**: VibeLearn AI
**진행 방식**: `daily_learning_prompt.md` 기준 학습 계획 제시 후 사용자 승인 받아 진행

## 오늘의 학습 목표

- [x] 기존 M2 산출물을 Roadmap DoD와 VibeLearn AI 학습 품질 기준으로 재검토한다.
- [x] Palantir FDSE, Deployment Strategist, AI FDE 비교를 학습자가 직접 수행할 수 있도록 활동을 보강한다.
- [x] M2 재진행 이력을 별도 WorkLog로 남긴다.
- [x] Roadmap 진행표에 daily prompt 기준 재점검 이력을 반영한다.

## 진행 내용

### 1. daily_learning_prompt.md 기반 M2 상태 분석

**시간**: 07:10 - 07:11

**목적**:
M2도 초기 작성 시 일일 학습 계획 승인 절차 없이 진행되었으므로, M1과 같은 방식으로 재점검했다.

**과정**:
1. `vl_prompts/daily_learning_prompt.md`를 다시 확인했다.
2. Roadmap의 M2 계획을 확인했다.
3. M1 Rerun WorkLog의 Tomorrow's focus를 확인했다.
4. 기존 M2 산출물 목록을 확인했다.
5. 사용자에게 M2 재진행 학습 계획을 제시하고 승인을 받았다.

**결과**:
기존 M2는 Palantir 원형 설명과 비교표는 충분했지만, 학습자용 실습, 핵심 용어, 자기평가, 검증 질문이 부족하다고 판단했다.

### 2. M2 산출물 보강

**시간**: 07:11 - 07:13

**목적**:
M2를 단순 설명 문서가 아니라 Palantir 원형을 직접 분석하고 AI FDE로 번역해 볼 수 있는 교재형 자료로 보강한다.

**업데이트한 파일**:
- `02-Palantir-Origin/README.md`
- `02-Palantir-Origin/concepts/palantir-fde-origin.md`
- `02-Palantir-Origin/examples/original-vs-ai-fde-comparison.md`

**보강 내용**:
- README에 학습 활동 3개 추가
- README에 Self-Assessment와 Definition of Done 추가
- Palantir 원형 문서에 핵심 용어 표 추가
- Palantir 원형 문서에 동사 추출, FDSE vs Deployment Strategist 사례 분리, AI FDE 번역 실습 추가
- Palantir 원형 문서에 확인 질문 추가
- 원형 vs AI FDE 비교 문서에 비교표 빈칸 채우기, 바뀐 것/바뀌지 않은 것 분류, 1분 설명 만들기 과제 추가
- 원형 vs AI FDE 비교 문서에 검증 질문 추가

### 3. Roadmap 이력 보정

**시간**: 07:13 - 07:14

**목적**:
M2는 완료 상태를 유지하되, `daily_learning_prompt.md` 기준 재점검과 학습 활동 보강이 완료되었음을 Roadmap에 기록한다.

## 문제 해결 로그

### 문제 1: M2도 산출물 제작 중심으로 진행됨

**증상**:
M2 산출물은 Palantir 원형과 AI FDE 비교 내용을 담고 있었지만, VibeLearn AI의 "학습자가 직접 따라 할 수 있는 실습" 요소가 부족했다.

**원인**:
초기 진행 당시 일일 학습 절차와 승인 단계를 생략하고 Roadmap DoD 산출물 작성에 집중했다.

**해결**:
사용자 승인 후 M2 문서에 학습 활동, 실습 과제, 확인 질문, 자기평가를 추가했다.

### 문제 2: FDSE와 Deployment Strategist의 관계가 수동 학습으로 연결되지 않음

**증상**:
문서에는 역할 분담표가 있었지만, 학습자가 직접 두 역할을 비교하고 사례에 적용하는 활동이 없었다.

**원인**:
초기 문서가 설명형 리포트에 가까웠다.

**해결**:
공급망 지연 예측 프로젝트를 가정한 FDSE vs Deployment Strategist 분리 실습을 추가했다.

## DoD 체크리스트

- [x] 기존 M2 산출물 검토 완료
- [x] 필요한 보강 사항 반영
- [x] README 학습 순서와 문서 링크 유지
- [x] M2 재진행 WorkLog 작성
- [x] Roadmap에 재점검 이력 반영

**완료율**: 5/5 (100%)

## Daily Retrospective

### What went well

- M2도 M1과 같은 승인 기반 흐름으로 재진행했다.
- Palantir 원형을 단순 읽기 자료가 아니라 학습자가 직접 분석할 수 있는 활동으로 바꾸었다.
- M3 기업별 비교로 넘어가기 전에 필요한 비교 기준을 더 명확히 만들었다.

### What could be improved

- M3에서는 기업별 공고 비교 매트릭스를 더 학습자 주도형으로 바꿔야 한다.
- M3 Rerun에서는 지원자-fit selector를 실제 가상 후보자 3명에게 적용하는 실습을 추가하면 좋다.

### Insights

- Palantir 원형을 이해하려면 FDSE와 Deployment Strategist를 따로 외우는 것보다, 하나의 customer outcome을 두 역할이 어떻게 나누어 책임지는지 사례로 보는 편이 효과적이다.
- AI FDE는 Palantir 원형의 "outcome ownership"을 유지하면서 eval, model behavior, security boundary 같은 새 실패 요인을 다루는 역할이다.

### Tomorrow's focus

- M3를 `daily_learning_prompt.md` 방식으로 다시 진행한다.
- 기존 M3 산출물에 학습자용 기업별 비교 실습, 가상 후보자 fit test, 자기평가를 보강한다.

## 참조 및 산출물

**참조 자료**:
- `vl_prompts/daily_learning_prompt.md`
- `vl_roadmap/20260816_RoadMap_FDE-Forward-Deployed-Engineer.md`
- `vl_worklog/20260816_M1_Rerun_FDE-Forward-Deployed-Engineer.md`

**업데이트된 파일**:
- `02-Palantir-Origin/README.md`: 학습 활동, Self-Assessment, DoD 추가.
- `02-Palantir-Origin/concepts/palantir-fde-origin.md`: 핵심 용어, 학습자 실습, 확인 질문 추가.
- `02-Palantir-Origin/examples/original-vs-ai-fde-comparison.md`: 실습 과제, 검증 질문 추가.

**다음 세션 준비사항**:
- M3 기존 산출물 검토.
- 기업별 FDE archetype 문서에 학습자용 비교 실습 추가.
- candidate-fit selector에 실제 적용 예시 추가.
