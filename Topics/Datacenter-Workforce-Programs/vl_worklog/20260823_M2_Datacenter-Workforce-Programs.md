---
title: "WorkLog - M2: 6개 프로그램 해부 + 모집 주기 조기 스캔"
created: 2026-08-23 07:34:00
tags:
  - worklog
  - datacenter-workforce
---

## 세션 정보

**날짜**: 2026-08-23
**Topic**: Datacenter-Workforce-Programs
**모듈**: M2 - 6개 프로그램 해부 + 모집 주기 조기 스캔
**이전 세션**: [20260823_M1_Datacenter-Workforce-Programs.md](20260823_M1_Datacenter-Workforce-Programs.md)
**학습 시간**: 07:34 - 07:42 (8분)

## 🎯 오늘의 학습 목표

- [x] 6개 각각의 운영 주체·자금원·수료 후 고용 주체를 구분해 설명할 수 있다
- [x] "빅테크 직접 운영"과 "자금만 대고 지역기관이 운영"을 구별할 수 있다
- [~] 6개 전부의 모집 주기와 다음 마감일을 표로 확보한다 — **확보 실패. 실패 이유를 규명**
- [x] 로드맵 기간 안에 닫히는 프로그램이 있는지 판정하고 일정 조정 여부를 결정한다

## 📚 진행 내용

### 1. 실습 2를 실습 1보다 먼저 했다

**순서**: 1번째. M1 회고에서 예고한 대로.

로드맵 규칙 1이 요구하는 것이 "마감이 로드맵을 앞지르는지 먼저 보라"이므로
해부표(실습 1)보다 모집 캘린더(실습 2)를 앞세웠다.

**결과는 예상과 달랐다 — 마감일을 찾지 못했다.** 6개 공식 페이지 어디에도 없다.

처음엔 조사 부실인 줄 알았는데 아니었다. **구조 때문**이었다.

```
유형 A  전국 단위 자체 모집        ① Meta AWA · ⑥ Amazon Apprenticeship
유형 B  대학 학사일정에 종속        ② MS Datacenter Academy
유형 C  노조 견습 일정에 종속       ③ MS NABTU · ④ Google.org
```

**"마감일"이라는 개념이 성립하는 것은 ①⑥ 둘뿐**이고, 나머지는 지역 기관마다 다르다.
Microsoft에 물어도 답이 없고 대학에 물어야 한다.

산출물: [intake-calendar.md](../02-Program-Anatomy/examples/intake-calendar.md)

### 2. 실습 1 — 8항목 해부표

**순서**: 2번째.

운영 주체 / 자금원 / 대상 직무 / 기간 / 비용 / 수료 후 고용 주체 / 지역 / 지원 창구.
**5개는 채웠고 ⑤ Amazon TWD는 착수하지 못했다.**

산출물: [program-anatomy.md](../02-Program-Anatomy/examples/program-anatomy.md)

### 3. M1 가설 검증 — 맞았다

M1에서 "운영 주체 ≠ 자금원 ≠ 고용주"를 가설로 적었는데 **6개 중 5개가 갈렸다.**
가장 뚜렷한 것은 ④ Google.org — **구글에는 지원서를 낼 곳이 아예 없다.**
돈만 대고 운영은 etA(NECA+IBEW), 지원은 지역 IBEW local이다.

산출물: [who-actually-hires-you.md](../02-Program-Anatomy/guides/who-actually-hires-you.md)

## 🐛 문제 해결 로그

### 문제 1: 마감 7일 남았다는 주장을 만났다 ← 이 세션에서 가장 중요

2차 집계 사이트가 Amazon Technical Apprenticeship에 대해
*"the fall intake closes by August 30"* 이라고 적고 있었다. **오늘이 8/23이니 7일 뒤다.**

로드맵 규칙 1이 정확히 이 상황을 위한 것이고, 발동하면 M3~M7을 건너뛰고
⑥ 지원 준비에 즉시 들어가야 한다. **로드맵 전체를 흔드는 판단이다.**

그래서 M1에서 정한 원칙을 적용했다 — *인상적인 숫자일수록 원출처 확인이 필요하다.*
Amazon 공식 페이지 두 곳을 확인했다.

```
amazon.jobs 랜딩       마감일 없음
aboutamazon 기사        마감일 없음
```

**1차 출처로 확인되지 않았다.** 그래서 규칙 1을 발동하지 않았다.
대신 "미검증 주장 + 최우선 확인 항목"으로 기록했다.

만약 확인 없이 발동했다면 로드맵 순서를 뒤집고 며칠을 썼을 것이다.
반대로 무시했다면 진짜 마감을 놓쳤을 수도 있다. **둘 다 피하는 방법은 확인뿐이다.**

### 문제 2: 자격 대상이 상충한다

⑥의 `amazon.jobs` 랜딩은 **"members of the military community—veterans and their spouses"**
를 대상으로 명시한다. 그런데 aboutamazon 기사는 프로그램이
**"recently expanded beyond military veterans and their spouses"** 라고 적는다.

내가 받은 페이지가 군 전용 랜딩(`mil-apprentice`)이라 **프로그램 전체가 군 대상인지
그 페이지만 그런지 구별되지 않는다.**

이건 사소한 불일치가 아니다. **확인 결과에 따라 ⑥이 본인에게 해당 없는 프로그램이 된다.**
M7 적합성 판별의 선결 조건으로 올렸다.

### 문제 3: 기초 표와 실물이 달랐다 (③ MS NABTU)

8/19 기초 표는 ③을 "전기·배관·HVAC 건설 숙련직 / 노조 견습·지역 훈련 강화"로 적었다.
그런데 2026-04-21 발표된 확대분의 실체는 **"no-cost AI literacy courses"** —
숙련직을 훈련하는 게 아니라 **숙련직에게 AI를 가르치는** 것이었다.

기초 표가 틀렸다기보다 **"Microsoft가 NABTU와 뭔가 한다"를 데이터센터 취업 프로그램으로
읽은 것**이 어긋남의 원인으로 보인다. 데이터센터 취업 경로로서의 실체는
Microsoft 쪽이 아니라 **TradesFutures 견습 준비 프로그램**이다.

→ 기초 자료를 그대로 믿지 않고 하나씩 원문으로 확인한 것이 값을 했다.

### 문제 4: ⑤를 착수하지 못했다

M1에서 "⑤ Amazon TWD는 두 칸에 걸치니 M2에서 하위 트랙으로 분해하라"고 넘겼는데
①②③④⑥을 하다가 닿지 못했다.

**빈 칸으로 두지 않고 "미조사 + 시도한 경로: 없음(착수 못 함)"으로 명시**했다.
"확인 불가"와 "안 했음"은 다르고, 뭉치면 다음 세션이 이미 시도해 본 줄 안다.

## 📊 DoD 체크리스트

- [~] 6개 × 8항목 해부표 완성 — **5/6. ⑤ 미착수**
- [x] 모집 캘린더에 6개 전부 기록 (값 또는 "확인 불가 + 문의처")
- [x] 로드맵 기간 내 마감 건 판정 — **확인된 마감 0건 → 정상 순서 유지**
- [x] "운영 주체 ≠ 자금원 ≠ 고용 주체" 사례 문서화 — 5건
- [x] 확인 불가 항목마다 시도한 경로·다음 문의처 기록
- [x] README 작성
- [x] WorkLog 작성 완료

**완료율**: 5/7 + 1건 부분 + 1건 미착수

## 💡 Daily Retrospective

### What went well (잘된 점)

- **실습 순서를 바꾼 판단이 맞았다.** 해부표를 먼저 했으면 마감 주장을 세션 끝에 만났을 것이다.
  규칙 1을 로드맵에 넣어 둔 것이 실제로 작동했다
- **미검증 주장에 로드맵을 걸지 않았다.** 7일이라는 숫자는 행동을 촉구하는 힘이 세다.
  그런데 1차 출처에 없었다. 확인 전에는 움직이지 않기로 한 것이 옳았다고 본다
- **기초 자료를 원문으로 재확인한 것.** ③이 기초 표와 성격이 달랐다.
  그대로 믿고 갔으면 M7까지 잘못된 전제를 안고 갔을 것이다
- "확인 불가"와 "미착수"를 구분해 적었다

### What could be improved (개선할 점)

- **⑤를 빠뜨렸다.** M1이 명시적으로 넘긴 과제였는데 우선순위에서 밀렸다.
  다음 세션 시작 시 **이전 세션이 넘긴 항목부터 확인**하는 절차가 필요하다
  (daily_learning_prompt에 "확인 불가 항목이 쌓여 있는가"를 넣어 뒀는데, 정작 내가 안 봤다)
- **8분에 끝났다. M1은 13분이었고 로드맵 추정은 각각 3h·5h다.**
  M1 회고에서 "M2에서 같은 비율이 나오면 시간 추정을 다시 잡아야 한다"고 적었는데
  **실제로 그렇게 나왔다** (추정의 2.7%). 아래 인사이트 참조
- 공식 페이지 403이 두 번 났다(Glendale CC, Amazon hiring). 우회 경로를 찾지 않고 넘어갔다

### Insights (인사이트)

**로드맵 시간 추정이 실제와 맞지 않는다 — 두 세션 연속.**

| | 로드맵 추정 | 실제 | 비율 |
|---|---|---|---|
| M1 | 3h | 13분 | 7% |
| M2 | 5h | 8분 | 2.7% |

두 가지 해석이 가능하다.

1. **로드맵 추정이 사람 기준이다.** 사람이 직접 조사하면 검색·읽기·표 작성에 그만큼 걸린다.
   AI가 대신하면 시간 축이 통째로 다르다.
2. **내가 얕게 하고 있다.** M2에서 ⑤를 통째로 빠뜨렸고 403 우회도 안 했다.

**둘 다 맞을 것이다.** 그런데 어느 쪽이든 대응이 다르다 —
1번이면 시간 대신 **산출물 기준**으로 DoD를 재정의해야 하고,
2번이면 **깊이 기준**을 올려야 한다.

→ M3에서 판별한다. 이번엔 의도적으로 끝까지 파고(확인 불가를 남기지 않고) 시간을 재 본다.
  그래도 짧으면 1번이다.

**"마감 임박" 정보는 그 자체로 압력을 만든다.** 7일이라는 숫자를 본 순간
로드맵을 바꾸고 싶어졌다. 정보의 긴급성과 정보의 신뢰성은 별개인데,
긴급할수록 검증을 건너뛰게 된다. **긴급한 정보일수록 출처를 먼저 봐야 하는 이유가 이것이다.**

**"마감일이 없다"가 답이었다.** 실습 2의 목표는 마감일 확보였고 실패했다.
그런데 실패 이유를 규명하니 그것이 더 쓸모 있는 결과였다 —
**대부분의 프로그램은 전국 단위 마감이 존재하지 않고 지역 기관에 물어야 한다.**
이건 M5(WA 정밀 조사)의 문의 목록으로 바로 이어진다.

목표를 달성하지 못한 것과 아무것도 얻지 못한 것은 다르다.

### Tomorrow's focus (다음에 할 것)

**세션 시작 시 먼저 할 것 (M2 잔여)**
- [ ] ⑥ Amazon 채용 포털에서 실제 공고 확인 — 마감일과 **군 출신 외 지원 가능 여부**
- [ ] ⑤ Amazon TWD 하위 트랙 분해

**M3 본 작업**
- [ ] registered apprenticeship / pre-apprenticeship / certificate 구분
- [ ] M1에서 내가 정한 "숙련직/기술직" 축이 실제 제도 구분과 맞는지 검증
- [ ] ③④의 견습 기간·비용 (IBEW/TradesFutures 구조를 알아야 채워진다)
- [ ] **의도적으로 끝까지 파고 시간을 잰다** — 시간 추정 문제 판별용

## 📎 참조 및 산출물

**생성된 파일**

- `02-Program-Anatomy/README.md` — 학습 순서와 발견 10건, 미해결 2건
- `02-Program-Anatomy/examples/intake-calendar.md` — 모집 구조 3유형, 일정 판단, 미검증 주장
- `02-Program-Anatomy/examples/program-anatomy.md` — 6개 × 8항목 (5/6 완료)
- `02-Program-Anatomy/guides/who-actually-hires-you.md` — 운영·자금·고용 주체 분리 사례 5건

**확보한 1차 출처**

- [Meta — America's Workforce Academy](https://www.meta.com/actions/americas-workforce-academy/)
- [Microsoft Datacenter Academy — Careers](https://careers.microsoft.com/v2/global/en/datacenteracademy.html)
- [NABTU·Microsoft 확대 발표 (2026-04-21)](https://news.microsoft.com/source/2026/04/21/nabtu-and-microsoft-expand-nationwide-initiative-to-strengthen-ai-training-and-career-pathways-across-the-skilled-trades/)
- [NECA — Google.org의 etA 지원 (2026-06-12)](https://www.necanet.org/news-media/detail/press-releases/2026/06/12/neca-applauds-google.org-for-support-of-the-electrical-training-alliance-and-skilled-trades-growth)
- [Amazon — Technical Apprenticeships](https://www.amazon.jobs/en/landing_pages/mil-apprentice)
- [AWS hires 1,000th apprentice](https://www.aboutamazon.com/news/aws/aws-hires-1-000th-apprentice-for-technical-training-program)
- [BBCC — Data Center program](https://www.bigbend.edu/post/bbcc-data-center-program-prepares-graduates-for-high-demand-it-careers.html)

**다음 세션 준비사항**

- Amazon 채용 포털은 403이 날 수 있다 — 브라우저로 직접 열어 확인하는 편이 빠를 수 있다
- M3는 제도 조사라 정부·노조 공식 사이트(DOL, IBEW, WA L&I)가 1차 출처다

---

**작성자**: solkit70
**방법론**: VibeLearn AI
