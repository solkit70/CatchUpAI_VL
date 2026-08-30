# WorkLog - M3: 급여·복지 비교 (의료보험 중심)

**날짜**: 2026-08-30
**Topic**: WA-Caregiver-Pathways
**모듈**: M3 - 급여·복지 비교 (의료보험 중심)
**작성자**: Codex with VibeLearn AI
**상태**: 완료

## 오늘의 학습 목표

- M2를 최종 점검하고 M3로 전환한다.
- 기관 소속 HCA, IP/CDWA, NAC 고용의 급여를 공식 임금표·통계와 실제 공고로 대조한다.
- 세 경로 × 전업·파트타임의 6개 복지 경우를 완성한다.
- 의료보험의 시간·근속·신청·유지 조건을 분리해 설명한다.
- M5 전까지 본인 적합성 판단을 유보한다.

## 진행 내용

### 1. M2 최종 종료 점검

M2 WorkLog와 산출물 4개를 다시 대조해 DoD 7/7을 확인했다. 남아 있는 200일 문구는 오류가 아니라 RCW 기본법과 현재 WAC 한시 규칙 365일/425일을 구분하기 위한 설명이었다. Daily Prompt의 Tomorrow's focus만 M2 회고 내용과 동기화 대상으로 확인했다.

### 2. 급여 출처를 층위별로 분리

HCA와 IP는 BLS/WA ESD의 Home Health and Personal Care Aides(SOC 31-1120)에 함께 집계되므로 통계만으로 두 경로를 분리하지 않았다. 대신 공식 직업통계의 분류·시장 기준, 단체협약 임금표, 공식 채용 페이지, 실제 지역 공고를 구분해 사용했다.

2026-08-30 현재 IP/CDWA 임금표는 신입 CCH 0~2,000에서 $23.54이고, 최고 $27.28은 40,001+ CCH 구간이다. 기관 HCA 대표 사례인 Full Life Care는 기본 $23.58, HCA differential 포함 $23.83이다. NAC 대표 공고는 WDVA full-time $51,600~$59,760/년, part-time 60% $24.23~$28.06/시간, on-call $24.71~$28.62/시간이었다.

### 3. 의료보험 시간 문턱 비교

IP/SEIU 775는 월 80 paid hours를 2개월 연속 일하고 이후 매월 80시간을 유지해야 한다. 개인 medical+dental co-premium은 월 $25이며, 2026-08-01부터 vision benefit 확대도 공식 페이지에 반영돼 있다. 월 80시간은 주당 평균 약 18.5시간이므로 파트타임도 시간 기준을 넘을 수 있지만 client hours가 월별로 변하면 coverage가 흔들릴 수 있다.

기관 HCA는 고용주별 차이가 있다. Full Life Care CBA 사례는 월 80시간 이상 정기 배정과 benefit eligibility waiting period 완료를 요구하고 Home Care Worker medical premium을 employer가 부담한다. 다만 waiting period의 정확한 기간과 vision은 CBA에서 확인되지 않아 HR 문의 항목으로 남겼다.

주정부 NAC의 PEBB는 채용 시 월평균 80시간, 매월 8시간 이상, 6개월 초과 근무가 예상되면 자격을 받을 수 있다. 60% permanent는 시간상 기준을 넘을 가능성이 높지만 최종 판정은 employer가 한다. on-call은 intermittent/sporadic이므로 공고만으로 보험·연금 자격을 확정하지 않았다.

### 4. 복지 6개 경우 완성

`examples/benefits-matrix.md`에 기관 HCA, IP/CDWA, NAC 각각의 전업·파트타임을 6개 행으로 작성했다. 의료보험, 치과·안과, PTO, 은퇴연금, 교육 지원, 교통비를 고정 열로 두고, 값이 없는 항목은 확인 불가와 다음 문의처를 남겼다.

## 문제 해결 로그

| 문제 | 원인 | 해결/기록 |
|---|---|---|
| HCA와 IP의 통계 임금을 분리하기 어려움 | 둘 다 SOC 31-1120에 포함되는 경우가 많음 | 통계는 시장 기준으로 공유하고, CBA·고용주 공식 임금표로 경로를 분리 |
| 시급 범위 최고액이 신입 급여처럼 보임 | CCH·경력 전 구간을 하나의 range로 광고 | 신입 CCH 0~2,000과 40,001+ 최고 구간을 따로 기록 |
| 최신 BLS/ESD 원자료의 동적·다운로드 접근 제한 | 웹 인터페이스와 자동 다운로드 제한 | 공식 통계의 분류·방법론을 사용하고, 현재 금액은 공식 CBA와 실제 공고로 교차 확인. 미검증 숫자는 쓰지 않음 |
| agency HCA 보험 waiting period 숫자가 없음 | 대표 CBA가 존재만 명시하고 기간 미기재 | 확인 불가로 표시하고 employer HR 문의 질문 작성 |
| NAC on-call 복지가 공고 목록만으로 불명확 | 근무가 intermittent/sporadic이고 appointment별 판정 | WDVA recruiter/benefits office 문의 항목으로 유지 |
| 이전 SEIU 2025-2026 PDF의 적용기간 종료 | 2026-07-31 종료 자료가 검색 상위에 노출 | 2026-08-01 신규 benefits가 반영된 현재 Get Health Coverage 페이지로 교체 |

## DoD 체크리스트

- [x] 경로별 급여를 출처 2종으로 확보
- [x] 복지 비교표 6칸 완성
- [x] 의료보험 자격 조건(시간·근속) 명시
- [x] 전업/파트타임 차이가 표에서 드러남
- [x] 본인 판단이 섞이지 않았음을 확인
- [x] README 작성
- [x] WorkLog + Daily Retrospective 작성

**완료율**: 7/7 (100%)

## Self-Assessment

- [x] 월 80시간이 주당 약 18.5시간이며, 파트타임도 보험 대상이 될 수 있음을 설명할 수 있다.
- [x] 공고의 benefit 목록과 실제 eligibility condition을 구분할 수 있다.
- [x] 공고에 조건이 없을 때 employer HR, SEIU 775 Benefits Group, PEBB benefits office 중 어디에 물을지 안다.

## Daily Retrospective

### What went well

의료보험을 단순한 제공 여부가 아니라 최초 자격, 신청, 시작, 유지, 상실 위험으로 나눴다. 특히 2026-08-01부터 바뀐 SEIU 775 현재 페이지를 찾아 종료된 2025-2026 PDF에 의존하지 않은 점이 중요했다.

### What could be improved

민간 agency와 시설은 공고에 benefit 이름만 쓰고 시간·근속 조건을 생략하는 경우가 많았다. M4에서 실제 지원 후보를 좁힐 때는 각 고용주의 benefits summary 또는 HR 답변까지 확보해야 6개 경우를 일반화할 수 있다.

### Insights

1. **파트타임과 무보험은 같은 말이 아니다.** 월 80시간 기준을 넘는 고정 파트타임은 여러 체계에서 보험 가능성이 있다.
2. **같은 80시간도 진입 시점이 다르다.** IP는 2개월 연속 실제 근무, agency는 정기 배정+대기기간, PEBB는 예상 근무시간과 6개월 초과 기간으로 판정한다.
3. **시급보다 배정 안정성이 월소득과 보험을 좌우할 수 있다.** 특히 IP와 on-call은 높은 시간급만으로 비교할 수 없다.
4. **NAC는 하나의 복지 체계가 아니다.** 주정부, 병원, nursing facility, home care agency에 따라 보험과 연금이 달라진다.

### Tomorrow's focus

- M4 착수 전 조사 반경의 기준점을 Tehaleh/Bonney Lake로 재확인한다.
- 반경 약 50마일에서 교육기관 3곳 이상과 고용주 3곳 이상을 근거리·중거리·원거리로 나눈다.
- 실제 공고마다 시급, FTE, 의료보험 시간·대기 조건, 배정 지역, 교통비를 수집한다.
- M4에서도 M5 전까지 본인 적합성 판단은 유보한다.

## 세션 인계 — Codex → Claude Code (2026-08-30)

**Codex 세션이 usage limit 으로 중단됐다.** 산출물 4개와 WorkLog 본문까지 작성한 뒤, **Roadmap·Daily Prompt 동기화와 링크·DoD 검증** 단계에서 끊겼다. Claude Code 가 그 지점부터 이어받았다.

### 인계 시점의 상태

| | 상태 |
|---|---|
| `03-Pay-and-Benefits/` 4개 파일 | ✅ 작성 완료 |
| WorkLog 본문 | ✅ 작성 완료 |
| Roadmap 진행표 | ❌ M3 행이 `⏳ 0%` 로 남음 |
| `daily_learning_prompt.md` | ❌ M2 시점 상태 그대로 |
| 링크 검증 | ❌ 미실행 |
| Task Board | ❌ M2 로 남음 |

### 이어받아 수행한 것

**1. 링크 검증 (실행)**

상대 링크 31개를 전수 확인했다.

```
정상 21 · 깨짐 10
```

**깨진 10건은 전부 `vl_prompts/` 의 템플릿 예시**(`concepts/overview.md`, `examples/hello.py`, `URL` 등)로, 실제 링크가 아니라 로드맵 프롬프트 템플릿에 남아 있는 자리표시자다. **M3 산출물의 링크는 21/21 정상이다.**

**2. 핵심 수치 1차 출처 재검증 (실행)**

M3 결론이 걸린 IP 의료보험 조건을 원문에서 다시 확인했다. **전부 일치했다.**

| 항목 | 문서 기재 | 1차 출처 확인 |
|---|---|---|
| 시간 문턱 | 월 80h · 2개월 연속 · 이후 유지 | ✅ *"work 80 hours each month for **two months in a row** and maintain 80 hours per month going forward"* |
| 개인부담 | 월 $25 | ✅ `$25/mo.` |
| 자녀 기준 | 월 120h | ✅ *"work 120 paid hours or more a month … Coverage for Kids"* |
| Grace Month | 연 2개 · 연속 사용 불가 | ✅ *"2 Grace Months per coverage year (August–July)"* · *"cannot use Grace Months 2 months in a row"* |
| 시작 시점 | 신청 처리 후 다음 달 1일 | ✅ *"the 1st of the month after your application is received and processed, which takes about 2 weeks"* |
| 적용일 | 2026-08-01 | ✅ |

> **`myseiubenefits.org/help-lp/` 에는 시간 문턱만 있고 $25·Grace Month·120시간은 없다.** 그 세부는 `seiu775benefitsgroup.org/health/get-coverage/` 에 있다. 두 페이지를 나눠 인용한 것이 맞았다.

**3. 동기화 (실행)**

- Roadmap 진행표 M3 행 → `✅ 100% (7/7)` + 발견 요약
- `daily_learning_prompt.md` → M2 상태를 M3 완료로 교체, 다음 모듈을 M4 로, Tomorrow's focus 4항목 이전
- Task Board → `M2` 행을 `M4` 로 갱신

### 인계에서 배운 것

**산출물이 끝났다고 모듈이 끝난 것이 아니다.** 이 Topic 의 모듈 완료는 문서 4개가 아니라 **Roadmap·Daily Prompt·Task Board 세 곳의 상태까지** 맞아야 성립한다. Codex 가 남긴 상태에서 다음 세션이 `daily_learning_prompt.md` 만 읽고 시작했다면 **M3 를 다시 시작했을 것이다.**

**중단된 세션을 이어받을 때는 "무엇을 했는가"보다 "어디서 멈췄는가"가 중요하다.** 산출물은 파일로 남아 눈에 보이지만, **동기화가 안 된 상태는 아무 흔적도 남기지 않는다.** 그래서 인계 지점을 이 표로 명시해 뒀다.

## 참조 및 산출물

**생성된 파일**:

- `03-Pay-and-Benefits/README.md`
- `03-Pay-and-Benefits/examples/pay-comparison.md`
- `03-Pay-and-Benefits/examples/benefits-matrix.md`
- `03-Pay-and-Benefits/guides/health-insurance-eligibility.md`

**주요 출처**:

- SEIU 775 Benefits Group Get Health Coverage: https://seiu775benefitsgroup.org/health/get-coverage/
- CDWA Become a Provider: https://www.consumerdirectwa.com/become-a-provider/
- CDWA 2025-2027 wage scale: https://seiu775.org/cdwata2025/
- Full Life Care 2025-2027 CBA: https://seiu775.org/wp-content/uploads/2026/04/Full-Life-Care-2025-2027-CBA.pdf
- WA HCA PEBB eligibility: https://www.hca.wa.gov/employee-retiree-benefits/public-employees/am-i-eligible
- 2026 PEBB Employee Enrollment Guide: https://www.hca.wa.gov/assets/pebb/50-0100-pebb-employee-enrollment-guide-2026.pdf
- WA ESD OEWS: https://esd.wa.gov/jobs-and-training/labor-market-information/employment-and-wages/occupational-employment-and-wage-statistics-oews
- BLS May 2025 OEWS: https://www.bls.gov/oes/tables.htm
- WDVA NAC postings: `pay-comparison.md`에 링크 기록

**다음 세션 준비사항**:

- M4에서 현재 열려 있는 공고와 교육기관 일정을 확인한다.
- 기관 문의가 필요하면 사용자가 직접 연락하고, 볼트에는 질문·일시·답변만 기록한다.
- 실제 보험 신청정보나 신원정보는 기록하지 않는다.

**방법론**: VibeLearn AI
