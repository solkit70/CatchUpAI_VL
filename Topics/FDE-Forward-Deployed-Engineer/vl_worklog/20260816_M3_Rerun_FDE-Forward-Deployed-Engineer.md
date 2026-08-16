# WorkLog - M3 Rerun: 미국 AI 기업별 FDE 모델 비교

**날짜**: 2026-08-16
**Topic**: FDE-Forward-Deployed-Engineer
**모듈**: M3 - 미국 AI 기업별 FDE 모델 비교
**학습 시간**: 07:16 - 07:25 (총 9분, 재점검 및 보강 세션)
**방법론**: VibeLearn AI
**진행 방식**: `daily_learning_prompt.md` 기준 학습 계획 제시 후 사용자 승인 받아 진행

## 오늘의 학습 목표

- [x] 기존 M3 산출물을 Roadmap DoD와 VibeLearn AI 학습 품질 기준으로 재검토한다.
- [x] 기업별 FDE archetype을 학습자가 직접 분류할 수 있는 활동을 보강한다.
- [x] 비교 매트릭스와 candidate-fit selector에 실습 요소를 추가한다.
- [x] M3 재진행 이력을 별도 WorkLog로 남긴다.
- [x] Roadmap 진행표에 daily prompt 기준 재점검 이력을 반영한다.

## 진행 내용

### 1. daily_learning_prompt.md 기반 M3 상태 분석

**시간**: 07:16 - 07:18

**목적**:
M3도 초기 작성 시 일일 학습 계획 승인 절차 없이 진행되었으므로, M1/M2와 같은 방식으로 재점검했다.

**과정**:
1. `vl_prompts/daily_learning_prompt.md`를 다시 확인했다.
2. Roadmap의 M3 계획을 확인했다.
3. M2 Rerun WorkLog의 Tomorrow's focus를 확인했다.
4. 기존 M3 산출물 목록을 확인했다.
5. 사용자에게 M3 재진행 학습 계획을 제시하고 승인을 받았다.

**결과**:
기존 M3는 기업별 archetype과 비교표는 충분했지만, 학습자가 직접 분류·적용해 보는 실습이 부족하다고 판단했다.

### 2. M3 산출물 보강

**시간**: 07:18 - 07:23

**목적**:
M3를 단순 비교 리포트가 아니라, 학습자가 직접 기업별 FDE 유형을 판별하고 자신의 fit을 평가할 수 있는 교재형 자료로 보강한다.

**업데이트한 파일**:
- `03-US-Company-Models/README.md`
- `03-US-Company-Models/concepts/fde-company-archetypes.md`
- `03-US-Company-Models/examples/company-comparison-matrix.md`
- `03-US-Company-Models/guides/candidate-fit-selector.md`

**보강 내용**:
- README에 회사별 archetype 맞히기, 비교 매트릭스 직접 채우기, candidate-fit selector 적용 활동 추가
- README에 Self-Assessment와 Definition of Done 추가
- archetype 문서에 판별 질문, 핵심 용어, 공고 문장 기반 archetype 판별 실습 추가
- 비교 매트릭스 문서에 빈칸 비교표, engineering-heavy/advisory-heavy 분석 실습, 자기 평가 추가
- candidate-fit selector에 가상 후보자 A/B/C 적용 예시 추가
- candidate-fit selector에 자기 적용 워크시트와 검증 질문 추가

### 3. Roadmap 이력 보정

**시간**: 07:23 - 07:25

**목적**:
M3는 완료 상태를 유지하되, `daily_learning_prompt.md` 기준 재점검과 학습 활동 보강이 완료되었음을 Roadmap에 기록한다.

## 문제 해결 로그

### 문제 1: M3가 비교 리포트 중심으로 치우침

**증상**:
M3는 회사별 FDE 유형과 비교표를 잘 정리했지만, 학습자가 직접 blank matrix를 채우거나 archetype을 판별하는 활동이 부족했다.

**원인**:
초기 작성이 산출물 제작 중심으로 진행되었고, VibeLearn AI의 실습 중심 원칙이 충분히 반영되지 않았다.

**해결**:
README, archetype 문서, 비교 매트릭스 문서에 학습자 직접 수행 활동을 추가했다.

### 문제 2: candidate-fit selector가 실제 적용 예시 없이 추상적임

**증상**:
질문지는 있었지만, 서로 다른 배경을 가진 사람이 어떻게 다른 archetype으로 매칭되는지 예시가 없었다.

**원인**:
초기 문서가 도구 설명에 머물렀다.

**해결**:
Backend SWE, Data Engineer, 전략 컨설턴트/비전공자 3명의 가상 후보자 예시를 추가했다.

## DoD 체크리스트

- [x] 기존 M3 산출물 검토 완료
- [x] 기업별 FDE archetype 학습 활동 보강
- [x] 비교 매트릭스 실습 보강
- [x] candidate-fit selector에 가상 후보자 적용 예시 추가
- [x] M3 재진행 WorkLog 작성
- [x] Roadmap에 재점검 이력 반영

**완료율**: 6/6 (100%)

## Daily Retrospective

### What went well

- M3도 승인 기반 흐름으로 재진행했다.
- 기업별 FDE 비교를 읽는 자료에서 직접 분류해 보는 학습 자료로 바꾸었다.
- 후보자-fit selector가 실제 커리어 판단 도구에 가까워졌다.

### What could be improved

- M4에서는 FDE와 유사 직무 비교를 학습자 개인 이력서/경력 전환 실습과 더 직접 연결해야 한다.
- M6에서 실제 job posting 분석을 할 때 M3의 archetype 기준을 검증해야 한다.

### Insights

- FDE 유형 분류는 회사명보다 고객 유형, 기술 중심축, 성공 지표, 코딩 비중을 봐야 정확하다.
- 지원자에게 필요한 것은 "FDE가 되고 싶다"가 아니라 "나는 어떤 FDE archetype에 맞는가"를 판단하는 능력이다.

### Tomorrow's focus

- M4를 `daily_learning_prompt.md` 방식으로 다시 진행한다.
- 기존 M4 산출물에 학습자용 role taxonomy 실습, 공고 판독 실습, resume bullet 직접 변환 워크시트를 보강한다.

## 참조 및 산출물

**참조 자료**:
- `vl_prompts/daily_learning_prompt.md`
- `vl_roadmap/20260816_RoadMap_FDE-Forward-Deployed-Engineer.md`
- `vl_worklog/20260816_M2_Rerun_FDE-Forward-Deployed-Engineer.md`

**업데이트된 파일**:
- `03-US-Company-Models/README.md`: 학습 활동, Self-Assessment, DoD 추가.
- `03-US-Company-Models/concepts/fde-company-archetypes.md`: 판별 질문, 핵심 용어, 학습자 실습, 확인 질문 추가.
- `03-US-Company-Models/examples/company-comparison-matrix.md`: 빈칸 비교표, 분석 실습, 자기평가 추가.
- `03-US-Company-Models/guides/candidate-fit-selector.md`: 가상 후보자 3명 적용 예시, 자기 적용 워크시트, 검증 질문 추가.

**다음 세션 준비사항**:
- M4 기존 산출물 검토.
- role taxonomy를 실제 job title 판독 실습으로 보강.
- resume bullet transformation을 사용자/학습자 직접 작성 워크시트로 확장.
