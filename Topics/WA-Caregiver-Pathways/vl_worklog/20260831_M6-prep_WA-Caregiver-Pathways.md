# WorkLog - M6-prep: 교육 등록과 이수 준비

**날짜**: 2026-08-31  
**Topic**: WA-Caregiver-Pathways  
**모듈**: M6 - 교육 등록과 이수 준비  
**상태**: 완료 (prep), M6 전체는 진행 중  
**작성 시각**: 2026-08-31 16:48:12

## 오늘의 학습 목표

M8 actual-contact 결과를 기다리는 동안, employer training이 막혔을 때 바로 움직일 수 있는 M6 교육 등록 fallback을 준비한다. 실제 등록, 결제, 신원 서류 제출은 사용자가 직접 수행해야 하므로 이번 세션은 등록 전 비교표와 체크리스트 작성으로 제한했다.

## 진행 내용

### 1. M6 범위 재정의

Roadmap의 M6 DoD에는 실제 교육 등록 완료와 시작일·종료 예정일 기록이 포함된다. 그러나 현재는 employer training 여부가 아직 확인되지 않았고, 등록에는 개인정보와 결제가 필요하다. 따라서 이번 세션은 M6-prep으로 분리해 등록 전 판단 자료만 만들었다.

### 2. 교육기관 공개 정보 재확인

2026-08-31 현재 Kent Nursing Academy, Two Rivers Care Training, Vibrant Health Homecare, Wellspring Home Health Training Academy 공개 정보를 확인했다. Kent는 $675와 3주 in-person이 명확하지만 next session은 전화 확인이 필요하다. Two Rivers는 HCA 75시간 $700과 flexible daily scheduling을 표시한다. Vibrant는 $650, hybrid, Thu/Fri 9am-5pm skills practice를 표시한다. Wellspring은 rolling enrollment, Lakewood skills lab, LMS, admission requirements, payment path를 가장 자세히 공개한다.

### 3. 산출물 작성

`06-Training-Enrollment/` 폴더를 만들고 README, enrollment steps, provider selection, training log를 작성했다. 실제 등록을 하지 않았으므로 M6 전체 완료가 아니라 prep 완료로 표시했다.

## 문제 해결 로그

| 문제 | 판단 | 처리 |
|------|------|------|
| 실제 등록에는 개인정보와 결제가 필요함 | AI가 대신 수행하지 않음 | 체크리스트와 문의 질문만 작성 |
| employer training이 가능할 수 있음 | self-pay 교육 등록을 서두르면 중복 비용 위험 | employer training 확인 후 fallback으로 M6 실행 |
| 교육기관 일정이 공개 페이지에 부분적으로만 있음 | 시작일과 seat availability는 문의 필요 | provider별 확인 질문 작성 |

## DoD 체크리스트

### M6-prep DoD

- [x] M4 교육기관 후보를 M6 등록 관점으로 재정렬
- [x] employer training 우선 / self-pay fallback 원칙 명시
- [x] 등록 전 질문 목록 작성
- [x] 개인정보 마스킹 기준 작성
- [x] training log 템플릿 작성
- [x] README 작성
- [x] WorkLog 작성

**완료율**: 7/7 (100%)

### M6 전체 DoD 현황

- [ ] 교육 등록 완료 (접수 확인 기록)
- [x] 필요 서류 목록과 실제 제출본 기록 구조 작성
- [ ] 시작일·종료 예정일·출석 요건 기록
- [x] 이수 로그 작성 시작 준비
- [x] README 작성
- [x] WorkLog 작성

**M6 전체 완료율**: 4/6 진행 중

## Daily Retrospective

### What went well

M8 actual-contact가 사용자 실행을 기다리는 동안 멈추지 않고, 다음 fallback을 준비했다. 이 덕분에 employer training이 안 된다는 답변이 와도 바로 Two Rivers 또는 Wellspring 문의로 넘어갈 수 있다.

### What could be improved

교육기관의 실제 시작일과 총비용은 아직 문의 전이라 확정할 수 없다. 특히 Wellspring의 총비용과 Two Rivers의 실제 skills lab 날짜는 공개 정보만으로는 부족하다.

### Insights

M6의 핵심은 "어느 학교가 좋아 보이는가"가 아니라 "employer training을 놓치지 않으면서도 120일 교육 리스크를 줄일 fallback을 확보하는가"다. 그래서 self-pay 교육 등록은 1순위 행동이 아니라 employer 문의 실패 시 작동하는 보험으로 두는 편이 맞다.

### Tomorrow's focus

- M8 actual-contact에서 Family Resource 또는 Visiting Angels가 employer training을 제공하는지 확인한다.
- employer training이 불가능하면 Two Rivers와 Wellspring에 next start, total cost, skills lab schedule을 문의한다.
- 실제 등록이 이루어지면 `06-Training-Enrollment/examples/training-log.md`에 시작일과 출석 요건을 기록한다.

## 참조 및 산출물

- `06-Training-Enrollment/README.md`
- `06-Training-Enrollment/guides/enrollment-steps.md`
- `06-Training-Enrollment/examples/provider-selection.md`
- `06-Training-Enrollment/examples/training-log.md`
- Kent Nursing Academy: https://kentnursingacademy.com/
- Two Rivers Care Training: https://tworiverscaretraining.com/courses.php
- Vibrant Health Homecare HCA: https://vibranthealthhomecare.com/home-care-aide/
- Wellspring Admissions: https://wellspringtrainingacademy.com/admissions
- Wellspring Lakewood Skills Lab: https://wellspringtrainingacademy.com/locations/lakewood
