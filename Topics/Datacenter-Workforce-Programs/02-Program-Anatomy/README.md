<!-- lang-switch -->
🇰🇷 **한국어** · [🇺🇸 English](README.en.md)
<!-- lang-switch -->

# M2 — 6개 프로그램 해부 + 모집 주기 조기 스캔

**상태**: 부분 완료 · DoD 5/7 — **⑤ Amazon TWD 미조사, ⑥ 자격 대상 확인 필요**
**예상 학습 시간**: 5h
**난이도**: ⭐⭐

기초 표의 6개를 같은 자로 분해하고, **로드맵을 앞지르는 마감이 있는지 먼저 확인**하는 모듈이다.

로드맵 규칙 1에 따라 **실습 2(모집 캘린더)를 실습 1(해부표)보다 먼저** 했다.
후반 모듈에 가서 마감을 확인하면 이미 닫혀 있을 수 있기 때문이다.

---

## 학습 순서

1. [examples/intake-calendar.md](examples/intake-calendar.md)
   — **먼저 읽을 것.** 모집 주기 스캔 결과와 일정 판단. ⚠️ 미검증 마감 주장 1건 포함
2. [examples/program-anatomy.md](examples/program-anatomy.md)
   — 6개 × 8항목 해부표. 프로그램별 상세와 확인 불가 항목
3. [guides/who-actually-hires-you.md](guides/who-actually-hires-you.md)
   — 운영 주체 ≠ 자금원 ≠ 고용주. M1 가설의 확인 결과

---

## 이 모듈에서 확인된 것

| # | 발견 | 영향 |
|---|---|---|
| 1 | **공식 마감일이 어디에도 없다** | 조사 부실이 아니라 구조 때문 — 대부분 지역 기관이 모집한다 |
| 2 | **모집 구조가 셋으로 갈린다** — 전국 자체 모집 / 대학 학사일정 / 노조 견습 일정 | "마감일" 개념이 성립하는 것은 ①⑥ 둘뿐 |
| 3 | **M1 가설 확인 — 6개 중 5개가 운영·자금·고용 주체가 갈린다** | 이름에 붙은 기업에 지원서를 내면 틀린다 |
| 4 | **④ Google.org는 지원 창구가 IBEW local이다** | 구글에 낼 곳이 없다. 돈만 댔다 |
| 5 | **③ MS NABTU의 2026 확대분은 AI 리터러시 교육이었다** | 기초 표의 "건설 숙련직 훈련"과 성격이 다르다. 실제 견습 창구는 TradesFutures |
| 6 | **① Meta AWA는 지역 제약이 사실상 없다** — 전 50주 + 항공·숙박·수당 제공 | WA 거주가 불리하지 않다. M7에서 중요 |
| 7 | **① Meta AWA는 훈련 전에 취업이 확정된다** — 협력사 조건부 채용 확약 | 6개 중 유일. 다만 고용주는 Meta 아님 |
| 8 | **⑥ Amazon만 이름=운영=고용주가 일치** | 빅테크 직고용을 원하면 이 형태 |
| 9 | **⑥ 자격 대상이 상충한다** — "군 출신·배우자" 표기 vs "대상 확대" 기사 | 확인 전에는 본인 해당 여부를 알 수 없다 |
| 10 | **② WA 옵션 확보** — Big Bend CC(Moses Lake), Quincy 데이터센터 연계, 2018년부터 | M5 정밀 조사 대상 |

---

## ⚠️ 미해결 2건 — 다음 세션 최우선

### 1. ⑥ Amazon 마감일 주장 (미검증)

2차 집계 사이트가 "fall intake closes by **August 30**"이라고 적었다.
**오늘이 8/23이므로 사실이면 7일 남았다.** 그런데 Amazon 공식 페이지 2곳 어디에도 이 날짜가 없다.

→ **채용 포털에서 실제 공고를 직접 확인**해야 한다. 확인 후 로드맵 규칙 1 발동 여부를 판단한다.
  지금 근거로는 로드맵을 흔들지 않는다.

### 2. ⑥ 군 출신 외 지원 가능 여부

`amazon.jobs` 랜딩은 "members of the military community—veterans and their spouses"를 대상으로
명시하고, aboutamazon 기사는 "recently expanded beyond military veterans and their spouses"라 적는다.

→ **이것이 확인되지 않으면 ⑥은 본인에게 해당 없는 프로그램일 수 있다.** M7의 선결 조건.

---

## Definition of Done

- [~] 6개 × 8항목 해부표 완성 (빈 칸 없음) — **5/6 완료. ⑤ Amazon TWD 미착수**
- [x] 모집 캘린더에 6개 전부의 다음 모집 정보 기록 (값 또는 "확인 불가 + 문의처")
- [x] 로드맵 기간 내 마감 건 판정 완료 및 일정 조정 여부 결정 — **확인된 마감 0건 → 정상 순서 유지**
- [x] "운영 주체 ≠ 자금원 ≠ 고용 주체" 사례 문서화 — 5건 확인
- [x] 확인 불가 항목마다 시도한 경로와 다음 문의처 기록
- [x] README 작성
- [x] WorkLog 작성 완료

**완료율**: 5/7 완료 + 1건 부분 + 1건 미착수

---

## Self-Assessment

**개념 이해**

- [x] 6개 중 "빅테크가 직접 운영하지 않는" 프로그램을 지목하고 이유를 설명 가능
  → ②③④가 그렇다. ②는 커뮤니티 칼리지, ③은 NABTU/TradesFutures, ④는 etA(NECA+IBEW)가 운영한다.
    빅테크는 자금·커리큘럼·장비를 대고 운영과 모집은 지역 기관이 한다.

- [x] intake window가 이 Topic 일정에 왜 결정적인지 설명 가능
  → 학습은 내 통제 안에 있지만 모집은 아니다. 준비를 마쳐도 창이 닫혀 있으면 지원할 수 없고,
    창은 보통 연 1~2회다. 그래서 로드맵 종료 조건에서 지원 완료를 뺐다.

**실무 활용**

- [x] 새 프로그램을 만나면 8항목 표로 즉시 분해 가능
- [x] 마감이 임박한 건을 발견했을 때 무엇을 먼저 할지 안다
  → 1차 출처로 확인부터 한다. 2차 집계 사이트의 날짜로 계획을 바꾸지 않는다.

---

## 다음 모듈로 넘기는 것

**M2 잔여 (다음 세션 우선)**
- ⑤ Amazon TWD 하위 트랙 분해 (미착수)
- ⑥ 마감일·자격 대상 공식 확인

**M3(자격 체계)로**
- ③④의 견습 기간·비용 — IBEW/TradesFutures 견습 구조를 알아야 채울 수 있다
- M1에서 세운 "숙련직/기술직" 축이 실제 제도 구분과 맞는지 검증

**M5(WA 정밀 조사)로**
- Big Bend CC — Systems Administration Datacenter Specialization 등록 마감
- WA 지역 IBEW local 견습 모집 시기
- WA TradesFutures 운영 여부

---

## 참조 자료

- [Meta — America's Workforce Academy](https://www.meta.com/actions/americas-workforce-academy/)
- [Microsoft Datacenter Academy — Careers](https://careers.microsoft.com/v2/global/en/datacenteracademy.html)
- [Microsoft Local — Big Bend Community College](https://local.microsoft.com/blog/big-bend-community-college-cultivates-a-hometown-tech-workforce/)
- [BBCC — Data Center program](https://www.bigbend.edu/post/bbcc-data-center-program-prepares-graduates-for-high-demand-it-careers.html)
- [NABTU·Microsoft 확대 발표 (2026-04-21)](https://news.microsoft.com/source/2026/04/21/nabtu-and-microsoft-expand-nationwide-initiative-to-strengthen-ai-training-and-career-pathways-across-the-skilled-trades/)
- [NECA — Google.org의 etA 지원 (2026-06-12)](https://www.necanet.org/news-media/detail/press-releases/2026/06/12/neca-applauds-google.org-for-support-of-the-electrical-training-alliance-and-skilled-trades-growth)
- [Amazon — Technical Apprenticeships](https://www.amazon.jobs/en/landing_pages/mil-apprentice)
- [AWS hires 1,000th apprentice](https://www.aboutamazon.com/news/aws/aws-hires-1-000th-apprentice-for-technical-training-program)

---

← 이전: [M1 데이터센터 인력 생태계와 직무 지도](../01-Ecosystem-and-Roles/README.md)
→ 다음: M3 자격 체계와 견습 제도 (`03-Credentials-and-Apprenticeship/`)
