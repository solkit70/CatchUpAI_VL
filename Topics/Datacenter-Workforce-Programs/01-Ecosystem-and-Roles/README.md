# M1 — 데이터센터 인력 생태계와 직무 지도

**상태**: 완료 · DoD 7/7
**예상 학습 시간**: 3h
**난이도**: ⭐

이후 모든 조사가 얹힐 **좌표계**를 만드는 모듈이다. 프로그램을 하나 볼 때마다
"이건 어느 칸인가"를 물을 수 있게 되면, 6개가 어디에 몰려 있고 어디가 비어 있는지 드러난다.

---

## 학습 순서

1. [concepts/role-map.md](concepts/role-map.md)
   — **먼저 읽을 것.** 건설기/운영기 × 숙련직/기술직 2×2 지도와 직무별 상세(연봉·진입 요건 포함)
2. [concepts/employment-structure.md](concepts/employment-structure.md)
   — 누가 실제로 고용하는가. 흔한 오해 4가지
3. [examples/program-to-role-matrix.md](examples/program-to-role-matrix.md)
   — 6개 프로그램을 지도 위에 배치한 결과와 해석

---

## 이 모듈에서 확인된 것

| # | 발견 | 영향 |
|---|---|---|
| 1 | **"빅테크 프로그램 수료 = 빅테크 직원"이 아니다** | 6개 중 4개가 건설기 숙련직이고, 그 고용 주체는 협력 건설업체다 |
| 2 | **가장 낮은 문은 기술직 쪽에 있다** — 데이터센터 기술자는 고졸 + 현장훈련, $60~90k | "기술직 = 학력 필요"라는 통념과 반대. M7 판별에 결정적일 수 있다 |
| 3 | **두 트랙은 분리돼 있지 않다** — Critical Facilities Engineer는 견습으로도 진입 가능 | M7을 "둘 중 하나 고르기"로 접근하면 이 다리를 놓친다 |
| 4 | **임금 구간이 겹친다** — 건설 숙련직 "six figures" vs 운영기 CFE $93~155k | 트랙 선택이 곧 수입 서열은 아니다 |
| 5 | **건설기 × 기술직 칸이 비어 있다** (6개 중 0개) | 짓는 동안엔 서버가 없다 — 구조적 공백으로 보인다 |
| 6 | **큰 데이터센터일수록 MW당 인력이 적다** — 소규모 8~12명/MW vs 하이퍼스케일 1~2명/MW | 지역 경제 효과 주장을 읽는 기준선 |
| 7 | **⑤ Amazon TWD가 두 칸에 걸친다** | 우산 브랜드 아래 별도 트랙일 가능성 → M2에서 분해 필요 |

---

## Definition of Done

- [x] 직무 지도 2×2 표 완성 (네 칸 모두 — 한 칸은 "구조적 공백"으로 근거와 함께 비움)
- [x] 직무별 고용 주체 표시 완료 (건설기: GC·하도급·인력공급업체 / 운영기: badged 직고용)
- [x] 6개 프로그램이 지도 위에 배치됨 (⑤는 두 칸 걸침으로 기록)
- [x] "프로그램 수료 = 빅테크 취업"이 아닌 이유를 문서로 설명
- [x] README 작성 (학습 순서 + 링크 + 1줄 설명)
- [x] WorkLog 작성 완료
- [x] Daily Retrospective 작성

---

## Self-Assessment

**개념 이해**

- [x] 건설기와 운영기에 필요한 직무가 왜 다른지 1-2문장으로 설명 가능
  → 짓는 동안엔 전기·배관·냉각 설비를 *설치*할 사람이 필요하고, 가동 후엔 그것을 *유지*하고
    서버를 다룰 사람이 필요하다. 서버는 건물이 완공된 뒤에 들어온다.

- [x] "Meta 프로그램을 수료하면 누구에게 고용되는가"에 답할 수 있다
  → Meta가 아니라 **협력 건설업체**다. Meta는 교육을 제공하고 고용은 GC·하도급업체가 한다.

**실무 활용**

- [x] 새로운 프로그램을 발견했을 때 직무 지도 위 어디인지 즉시 배치 가능
  → 대상 직무 목록을 보고 ①시간축(짓는 일인가 유지하는 일인가) ②직무축(면허·견습인가
    자격증·경력인가)을 물으면 칸이 정해진다. ⑤처럼 걸치는 경우는 하위 트랙 분해 신호다.

---

## 다음 모듈로 넘기는 것

M2에서 확인해야 할 항목이 각 문서 말미에 정리돼 있다. 요약하면:

- ⑤ Amazon TWD 하위 트랙 분해
- 6개 각각의 **수료 후 고용 주체** 공식 확인
- ④ Google.org의 실제 지원 창구 (구글인가 훈련기관인가)
- Uptime Institute MW당 인력 수치 원출처
- 프로그램을 더 확보한 뒤 "건설기 × 기술직" 공백 재확인
- 용접공·철골공 비중 (출처마다 트레이드 목록이 다르다)

---

## 참조 자료

- [Tradesmen International — The Skilled Trades Behind Data Center Construction](https://www.tradesmeninternational.com/news-events/the-skilled-trades-behind-data-center-construction-and-how-to-staff-them/)
  — 건설기 트레이드 5종과 각 역할 (원문 인용 출처)
- [Built In — Data Center Jobs: Pay, Roles and What to Expect](https://builtin.com/articles/data-center-jobs)
  — 운영기 직무 3종의 연봉·진입 요건
- [[Roundup/2026-08-19 - Daily Roundup#새로 생긴 학습 주제 두 가지]] — 6개 프로그램 기초 표
- [../vl_materials/00-baseline-programs.md](../vl_materials/00-baseline-programs.md) — 기초 자료 사본과 맥락

---

← 이전: (없음 — 첫 모듈)
→ 다음: M2 6개 프로그램 해부 + 모집 주기 조기 스캔 (`02-Program-Anatomy/`)
