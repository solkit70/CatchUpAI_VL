# WorkLog - M2: 자격 취득 절차 해부

**날짜**: 2026-08-30
**Topic**: WA-Caregiver-Pathways
**모듈**: M2 - 자격 취득 절차 해부
**작성자**: Codex with VibeLearn AI
**상태**: 완료

## 오늘의 학습 목표

- M1에서 넘긴 미확인 7건을 공식 1차 출처로 정리한다.
- HCA·IP·NAC/NAR 경로별 자격 취득 절차를 단계·기한·비용 기준으로 정리한다.
- 무경력자가 막힐 수 있는 지점을 따로 뽑는다.
- 배경조회가 언제, 누구를 통해 시작되는지 문서화한다.

## 진행 내용

### 1. M1 이월 항목 정리

M1의 핵심 이월은 200일 vs 365일, 가족 돌봄 면제의 VA-funded 범위, NAC vs NAR 차이, 신청비·시험비, 면제 목록 출처 불일치였다. 공식 WAC/DOH/WABON/DSHS/CDWA 출처를 다시 확인해 대부분 해소했다.

가장 큰 수정은 200일/365일 관계다. RCW 18.88B.021과 DOH FAQ에는 200일 문구가 남아 있지만, WAC 246-980-030/040은 2025-08-25부터 2027-12-31까지 365일, provisional certificate가 있으면 425일을 적용한다고 명시한다. 따라서 2026-08-30 현재 실무 안내는 365일을 중심으로 쓰되, 기본법 200일과 한시 규칙을 함께 설명해야 한다.

### 2. 면제 목록 층위 분리

M1에서 PDF와 FAQ 면제 목록이 달라 보였던 문제는 WAC를 보면서 정리됐다. HCA certification 자체의 면제는 WAC 246-980-025에 있고, 70-hour basic training 면제는 WAC 388-112A-0090에 있다. 즉 면제 목록이 단순히 충돌한 것이 아니라, 어떤 요건을 면제하는지 층위가 달랐다.

가족 돌봄 면제도 갱신됐다. WAC 246-980-025는 spouse/domestic partner 돌봄의 VA-funded 요건이 2026-07-01 이후 없어진 것으로 설명한다. M1에서 남긴 `VA-funded only` 의문은 이 조항으로 해소했다.

### 3. 절차도 작성

`02-Credentialing-Process/examples/credential-steps.md`에 HCA, IP, NAC/NAR 절차를 정리했다. HCA는 채용 또는 paid direct care 시작 → 근무 전 O/S 5시간 → +14일 DOH 신청 → +120일 75시간 교육 → Prometric 시험 → 현재 한시 규칙 +365일 인증의 흐름이다.

IP는 자격이 아니라 CDWA/DSHS 고용·계약 형태이므로, background check와 HCA 요건 판정이 hiring process 안에서 일어난다. NAC/NAR는 WABON 기준으로 분리했고, NAC가 HCA certification 면제에 직접 연결되는 자격임을 다시 확인했다.

### 4. 진입 장벽과 배경조회 문서화

`examples/entry-barriers.md`에는 무경력자 관점의 병목을 정리했다. 핵심 장벽은 전문지식 부족이 아니라, 고용 전 배경조회 선행 불가, 채용 후 120일 교육 시계, 시험·비용·교통·개인정보 처리다.

`guides/background-check.md`에는 DSHS/BCCU 배경조회 흐름을 정리했다. 개인이 혼자 먼저 끝내는 절차가 아니라 hiring entity, CDWA, facility를 통해 진행되는 구조다. confirmation code, 생년월일, SSN 같은 실제 신원 정보는 볼트에 기록하지 않는 규칙을 명시했다.

## 문제 해결 로그

| 문제 | 원인 | 해결/기록 |
|---|---|---|
| 200일과 365일 문구가 동시에 존재 | RCW 기본 규정과 WAC 한시 규칙이 함께 존재 | 2026-08-30 현재는 WAC 246-980-030/040의 365일/425일 한시 규칙을 실무 기준으로 기록 |
| 면제 목록이 출처마다 달라 보임 | HCA certification exemption과 70-hour basic training exemption이 다른 층위 | WAC 246-980-025와 WAC 388-112A-0090으로 분리 |
| 가족 돌봄 VA-funded 조건이 불명확 | 이전 문서의 표현이 2026-07-01 전후 변화를 반영하지 못함 | WAC 246-980-025 기준 2026-07-01 이후 spouse/domestic partner는 VA-funded 요건 없이 면제 가능으로 기록 |
| NAC vs NAR 차이 불명확 | DOH/WABON 이관 직후라 페이지가 나뉘어 있음 | WAC 246-841A-390/403과 WABON NAC 안내로 정리 |
| 배경조회 기산점 | IP에서 `Okay to Provide Care`와 date of hire 관계가 남음 | CDWA 문의 필요 항목으로 유지 |

## DoD 체크리스트

- [x] 3개 경로 전부 절차 단계도 완성 (기간·비용 포함)
- [x] 단계 간 선후 관계 명시
- [x] 무경력자 진입 장벽 목록 작성
- [x] 배경조회 절차·소요 기간 문서화
- [x] 확인 불가 항목마다 시도 경로와 다음 문의처 기록
- [x] README 작성
- [x] WorkLog + Daily Retrospective 작성

**완료율**: 7/7 (100%)

## Daily Retrospective

### What went well

M1의 이월 질문을 먼저 처리한 것이 좋았다. 특히 200일/365일 문제는 M2의 중심축이었고, 이를 정리하지 않았다면 이후 지원 일정과 안내 자료가 잘못될 수 있었다.

### What could be improved

공식 출처 간에도 최신 반영 속도가 다르다. DOH FAQ처럼 사용자에게 친절한 페이지가 항상 가장 최신 법령 상태를 반영한다고 가정하면 위험하다. 앞으로는 법령/WAC, 기관 FAQ, 실제 지원 페이지를 나눠 대조해야 한다.

### Insights

1. **면제는 하나가 아니다.** HCA certification 면제와 70-hour training 면제는 다른 층위다.
2. **현재 실무 규칙은 한시 조항을 봐야 한다.** 기본법 200일만 보면 2026~2027년 지원자에게 틀린 안내가 될 수 있다.
3. **파트타임 IP는 진짜 후보지만 아직 결론은 아니다.** 월 20시간 이하 HCA 면제는 강력한 단서지만, 급여·복지·의료보험 조건은 M3에서 봐야 한다.
4. **배경조회는 채용 경로와 묶여 있다.** 개인이 먼저 준비해 둘 수 있는 것은 서류와 일정 이해이지, DSHS background check 완료 자체가 아니다.

### Tomorrow's focus

- M3 착수 — 급여·복지 비교, 특히 의료보험 조건
- IP/CDWA의 part-time benefit 조건과 SEIU 775 benefit eligibility 확인
- 기관 소속 HCA, IP, NAC의 시작 시급과 실제 공고 시급 비교
- M3에서도 M5 전까지 본인 적합성 판단은 유보

## 참조 및 산출물

**생성된 파일**:

- `02-Credentialing-Process/README.md`
- `02-Credentialing-Process/examples/credential-steps.md`
- `02-Credentialing-Process/examples/entry-barriers.md`
- `02-Credentialing-Process/guides/background-check.md`

**공식 출처**:

- WA DOH Home Care Aide FAQ: https://doh.wa.gov/licenses-permits-and-certificates/professions-new-renew-or-update/home-care-aide/frequently-asked-questions
- WA DOH Home Care Aide Certification Information: https://doh.wa.gov/licenses-permits-and-certificates/professions-new-renew-or-update/home-care-aide/certification-information
- WA DOH Home Care Aide Exam Information: https://doh.wa.gov/pa/node/19595
- WAC 246-980-025: https://app.leg.wa.gov/wac/default.aspx?cite=246-980-025
- WAC 246-980-030: https://app.leg.wa.gov/wac/default.aspx?cite=246-980-030
- WAC 246-980-040: https://app.leg.wa.gov/wac/default.aspx?cite=246-980-040
- WAC 388-112A-0090: https://app.leg.wa.gov/wac/default.aspx?cite=388-112A-0090
- WAC 246-841A-390: https://app.leg.wa.gov/wac/default.aspx?cite=246-841A-390
- WAC 246-841A-403: https://app.leg.wa.gov/wac/default.aspx?cite=246-841A-403
- WABON NAC Information: https://nursing.wa.gov/education/nursing-assistant-training/na-program-student-info/nursing-assistant-certification-nac-information
- WABON Nurse License Fees: https://nursing.wa.gov/licensing/nurse-license-fees
- DSHS Background Checks: https://www.dshs.wa.gov/node/2527
- CDWA Resources: https://www.consumerdirectwa.com/resources/

**다음 세션 준비사항**:

- M3에서 급여·복지, 특히 의료보험 제공 여부와 조건을 확인한다.
- part-time IP 월 20시간 이하 면제와 benefit eligibility를 혼동하지 않는다.
- 실제 공고는 M3 또는 M4에서 수집하되, 개인정보와 지원 판단은 아직 기록하지 않는다.

**방법론**: VibeLearn AI
