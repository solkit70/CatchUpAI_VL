# WorkLog - M2b: 잔여 2건 마무리 (⑤ 해부 · ⑥ 검증)

**날짜**: 2026-08-28
**Topic**: Datacenter-Workforce-Programs
**모듈**: M2 - 6개 프로그램 해부 + 모집 주기 조기 스캔 (잔여 작업)
**작성자**: Claude Code with VibeLearn AI
**이전 세션**: 2026-08-23 (M2 71%, 5/7)

## 오늘의 학습 목표

- 8/30 마감 주장을 1차 출처로 판정한다 (로드맵 규칙 1 적용 여부 결정)
- ⑤ Amazon TWD 8항목을 해부해 해부표를 6/6으로 완성한다
- ⑥ 군 출신 외 지원 자격 상충을 해소한다

## 진행 내용

### 1. 8/30 마감 주장 — 근거 없음으로 판정

`amazon.jobs` 공식 프로그램 페이지를 직접 열어 확인했다. **마감일·코호트 시작일 표기 자체가 없다.** `aboutamazon` 기사에도 마감 언급이 없고, 2021년 지원자가 *"final day for applications"* 에 지원했다는 일화만 있어 오히려 상시 모집 정황에 가깝다.

**로드맵 정상 순서를 유지한다.** 8/23의 판단이 옳았다.

### 2. ⑤ — 프로그램명 자체가 틀렸다

`Technical Workforce Development`는 **Amazon이 쓰는 공식 명칭이 아니었다.** 실제 우산 브랜드는 **`AWS Grow Our Own Talent`** 이고, 그 아래 4개 경로가 있다.

| # | 경로 | 성격 |
|---|---|---|
| **⑤-a** | **Work-Based Learning Program (WBLP)** | 12개월 유급 → AWS 데이터센터 정규직 |
| ⑤-b | College internships | 재학생 |
| ⑤-c | Amazon Dedicated Cloud | 보안 인가자 |
| ⑤-d | Current employee opportunities | 사내 전환 |

M1이 이 항목을 "건설기·운영기 두 칸에 걸친다"고 본 것은 맞았다. **하나가 아니라 여러 개였기 때문이다.**

본인에게 해당하는 것은 **⑤-a 하나뿐**이고, 8항목을 전부 채웠다. 자금원만 미명시다.

### 3. ⑤-a WBLP — 이 Topic에서 가장 중요한 발견

| 항목 | 값 |
|---|---|
| 대상 직무 | data center **operations / install / decommissioning technician · logistics specialist** (4종) |
| 기간·비용 | **12개월 유급 훈련, 무료** |
| 고용 주체 | **AWS 직고용** — *"promoted into their chosen roles at an AWS data center"* |
| 지역 | Haymarket VA · **Kent WA** · Aurora CO |
| 자격 | 학위·경력 요건 명시 없음. 고졸 직후·무경험 수료 사례 존재 |

**6개 중 워싱턴주 소재가 확인된 유일한 경로다.** ②MS Datacenter Academy의 Big Bend CC(Moses Lake)가 WA에 있지만 그것은 대학 과정이고 고용 보장이 없다. WBLP는 수료가 곧 AWS 정규직 배치다.

### 4. ⑥ — 상충이 해소되지 않았고, 오히려 두 번째 문제가 나왔다

**자격**: 공식 페이지는 여전히 군 커뮤니티만 명시한다. 확대를 주장하는 것은 2차 자료뿐이고 그조차 범위를 밝히지 않는다.

**직무 — 새로 발견한 문제**: 현재 7개 트랙이 **전부 클라우드 직군**이다. 이전 조사에서 대상 직무에 넣었던 **Data Center Technician이 목록에 없다.** 기사에 2021년 견습생 사례가 나오지만 현재도 열려 있다는 근거가 공식 페이지에 없다.

→ **⑥은 본인 기준 사실상 해당 없음.** M7 shortlist 제외 후보로 두되, M5에서 실제 공고로 한 번 더 확인한다.

## 문제 해결 로그

| 문제 | 원인 | 해결 |
|---|---|---|
| ⑤ 검색이 안 잡힘 | `Technical Workforce Development`가 공식 명칭이 아님 | 데이터센터 직무 키워드로 우회 검색 → `Grow Our Own Talent` 우산 발견 |
| 8/23에 공식 페이지 403 두 번 | 우회 시도 없이 넘어감 | 이번엔 `amazon.jobs` 경로로 직접 접근해 성공 |
| ⑥ 자격 상충 | 1차·2차 출처가 다름 | **해소 불가로 판정.** 1차 우선 원칙에 따라 "군 대상"으로 기록 |

## DoD 체크리스트

- [x] 6개 × 8항목 해부표 완성 — **6/6**
- [x] 모집 캘린더에 6개 전부 기록
- [x] 로드맵 기간 내 마감 건 판정 — **8/30 주장 근거 없음 → 정상 순서 유지**
- [x] "운영 주체 ≠ 자금원 ≠ 고용 주체" 사례 문서화
- [x] 확인 불가 항목마다 시도한 경로·다음 문의처 기록
- [x] README 작성
- [x] WorkLog 작성

**완료율**: **7/7 (100%)**

## Module Retrospective - M2

### 학습 목표 달성도

- [x] 6개 프로그램의 운영 주체·자금원·고용 경로를 구분해 설명할 수 있다
- [x] 모집 주기 구조를 파악하고 로드맵 순서 변경 여부를 판정할 수 있다

### 핵심 인사이트

**1. 프로그램명을 의심하지 않은 것이 8/23 실패의 원인이었다.** 기초 표의 `Technical Workforce Development`를 그대로 검색어로 썼는데 그런 이름의 프로그램이 없었다. 403이 문제가 아니라 **검색어가 문제였다.** ③에서 "기초 표와 성격이 다르다"를 이미 겪었는데, 같은 교훈을 ⑤에는 적용하지 않았다.

**2. 미검증 주장을 버티는 것이 실제로 이득이 됐다.** 8/30 마감은 근거가 없었다. 그 압박에 순서를 바꿨다면 오늘 시점에 조사 단계를 통째로 건너뛴 상태였을 것이다. **인상적인 숫자일수록 원출처 확인**이라는 M1 원칙이 두 번 연속 유효했다.

**3. 답을 찾으러 갔다가 더 중요한 것을 발견했다.** ⑥의 마감을 확인하러 들어갔는데 ⑥이 애초에 해당 없다는 것이 드러났고, ⑤를 파다가 이 Topic 전체에서 가장 적합한 경로(WBLP, Kent WA)를 찾았다. **6개를 같은 자로 재기로 한 M2의 설계가 여기서 값을 했다.**

**4. 6개 중 실제 후보는 셋으로 줄었다.**

| 판정 | 프로그램 |
|---|---|
| **유력** | ⑤-a AWS WBLP (WA · AWS 직고용 · 무경력) |
| 후보 | ① Meta AWA (지역 제약 없음) · ② MS Datacenter Academy (Big Bend CC, WA) |
| 제외 후보 | ③ NABTU(실체는 AI 리터러시) · ④ Google(건설 숙련직·IBEW) · ⑥ Amazon Appr.(군 대상·클라우드 직군) |

### 다음 모듈 준비 사항

M3(자격 체계·견습 제도)로 넘어간다. 다만 **M5(워싱턴주)의 우선순위가 올라갔다** — WBLP Kent 공고 존재 여부가 이 Topic의 실질 성패를 가른다.

## Daily Retrospective

### What went well

이전 세션이 넘긴 항목부터 시작했다. 8/23 회고가 *"다음 세션 시작 시 이전 세션이 넘긴 항목부터 확인하는 절차가 필요하다"* 고 적었는데 이번엔 그렇게 했다.

### What could be improved

**⑤-a WBLP의 자금원을 확인하지 못했다.** 공식 페이지에 명시가 없다. 다만 AWS 직접 운영·직고용 구조라 자체 예산으로 보는 것이 자연스럽고, 이 항목이 판단을 바꾸지 않으므로 추가 추적하지 않았다.

### Insights

**"확인 불가"와 "잘못 찾았다"는 다르다.** 8/23의 ⑤는 확인 불가가 아니라 **찾는 이름이 틀린 것**이었다. 확인 불가로 분류해 두면 다시 시도하지 않게 된다. 다음부터 확인 불가로 넘길 때는 **검색어 자체를 의심했는지**를 함께 적는다.

### Tomorrow's focus

- M3 착수 — 자격 체계와 견습 제도
- M5 우선순위 상향 검토 — WBLP Kent WA 실제 공고 확인

## 참조 및 산출물

- [02-Program-Anatomy/examples/program-anatomy.md](../02-Program-Anatomy/examples/program-anatomy.md) — ⑤ 신규, ⑥ 정정
- [02-Program-Anatomy/examples/intake-calendar.md](../02-Program-Anatomy/examples/intake-calendar.md) — 8/30 판정
- 공식: `amazon.jobs` Technical Apprenticeships · AWS Work-Based Learning Program · AWS Grow Our Own Talent
- 2차: `aboutamazon` AWS 견습 1,000번째 기사
