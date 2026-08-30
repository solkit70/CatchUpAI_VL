---
title: "자격 형태 4종 구분 — registered / pre / certificate / degree"
created: 2026-08-28 21:10:00
tags:
  - datacenter-workforce
  - m3
  - credentials
---

## 왜 이 구분이 필요한가

M2에서 6개 프로그램을 해부하니 **같은 "교육 프로그램"이라는 말 아래 성격이 전혀 다른 것들이 섞여 있었다.** ⑥ Amazon Apprenticeship은 DOL 등록 견습이고, ② MS Datacenter Academy는 대학 인증과정이며, ③ NABTU 확대분은 무료 단기 교육이다. **어느 형태인지에 따라 훈련 중 수입이 있는지, 끝나고 무엇이 남는지, 중간에 그만두면 어떻게 되는지가 전부 다르다.**

## 4종 비교

| | **① Registered Apprenticeship** | **② Pre-apprenticeship** | **③ Certificate** | **④ Degree** |
|---|---|---|---|---|
| 인증 주체 | **미 노동부(DOL) 또는 주 견습청** | 없음 (프로그램별) | 교육기관·업계 단체 | 교육기관 (지역 인증) |
| 고용 관계 | **있음 — 채용된 상태** | 없음 | 없음 | 없음 |
| 훈련 중 수입 | **있음 (유급, 임금 상승형)** | 대개 무급 | 없음 | 없음 |
| 비용 | 무료 또는 저비용 | 대개 무료 | 등록금 | 등록금 |
| 기간 | 1~5년 (직종별) | 수 주~수 개월 | 6개월~1년 | 2년(준학사)~ |
| 결과물 | **전국 통용 자격** + 저니맨 지위 | 견습 지원 자격·우선권 | 수료증·자격증 | 학위 |
| 중도 이탈 시 | 근무 이력·부분 시간 인정 | 남는 것 적음 | 이수분만 | 학점 |

## ① Registered Apprenticeship (등록 견습)

미 노동부 정의는 이렇다.

> "an industry-driven, high-quality career pathway where employers can develop and prepare their future workforce, and individuals can obtain **paid work experience** with a mentor, receive **progressive wage increases**, classroom instruction, and a **portable, nationally-recognized credential**."

핵심 요소 5가지가 명시돼 있다 — **Industry Led · Paid Job · Structured On-the-Job Learning/Mentorship · Supplemental Education · Credentials**.

**"Apprenticeships are jobs!"** — DOL이 직접 쓴 표현이다. 학생이 아니라 **직원**이다.

### 이 형태의 결정적 차이 — 무직 기간이 없다

다른 세 형태는 전부 **배우는 동안 수입이 없다.** 등록 견습만 훈련 기간에도 임금이 나오고, 숙련도가 올라가면 임금도 단계적으로 오른다.

생계를 유지하면서 직종을 바꾸려는 사람에게는 이 한 가지가 나머지 모든 조건을 압도할 수 있다. **비용이 0이어도 1년간 수입이 없으면 실질 비용은 1년치 생활비다.**

### 등록 vs 비등록

DOL 또는 주 견습청이 **"industry-vetted and approved and validated"** 한 것만 등록 견습이다. 비등록 훈련은 이 검증을 거치지 않았고, 따라서

- 자격이 **전국 통용되지 않을 수 있다** (이직·이주 시 인정 문제)
- 임금 상승 구조가 보장되지 않는다
- 프로그램이 중단돼도 구제 절차가 없다

**참전용사는 GI Bill 수당을 임금과 별도로 받을 수 있다** (DOL 명시).

## ② Pre-apprenticeship (예비 견습)

견습에 지원하기 **전에** 거치는 준비 과정이다. 대개 무급이지만 짧고 무료다.

목적은 두 가지다 — **견습 선발 시험·면접 통과 준비**, 그리고 **견습 프로그램의 우선 선발권 확보**. ③ NABTU의 TradesFutures가 이 유형이다.

**그 자체로는 취업 자격이 아니다.** 견습으로 이어지지 않으면 남는 것이 적다.

## ③ Certificate (인증과정)

교육기관이나 업계 단체가 발급한다. ② MS Datacenter Academy가 이 형태다 — Big Bend CC의 **Systems Administration – Datacenter Specialization** 1년 인증과정.

등록금이 들고(장학금으로 커버될 수 있다) 고용 관계가 없다. **수료가 취업을 보장하지 않는다** — M2에서 ②의 "수료 후 고용 주체"가 "명시 없음"이었던 이유다.

## ④ Degree (학위)

준학사(2년) 이상. ② Datacenter Academy에는 2년 준학사 경로도 있다.

## 🔑 stackable credential

자격을 쌓아 올리는 구조를 말한다. 예비 견습 → 등록 견습 → 저니맨처럼, **앞 단계가 뒤 단계의 입력이 되고 중간에 멈춰도 딴 것은 남는다.**

반대로 쌓이지 않는 구조도 있다. 단기 교육 수료증은 다음 단계의 요건이 아닌 경우가 많다.

## 6개 프로그램의 자격 형태 분류

M2 해부표를 이 기준으로 다시 읽으면 이렇게 된다.

| 프로그램 | 자격 형태 | 훈련 중 수입 |
|---|---|---|
| ① Meta AWA | ③ Certificate (NCCER + America's Workforce Certificate) | **있음** (무료 + 일당) |
| ② MS Datacenter Academy | ③ Certificate 또는 ④ Degree | 없음 |
| ③ MS NABTU | ② Pre-apprenticeship (TradesFutures) + 부가 교육 | 없음 |
| ④ Google.org / etA | ① **Registered Apprenticeship** (IBEW 견습) | **있음** |
| **⑤-a AWS WBLP** | 등록 여부 미확인 — **고용 관계 있음, 유급** | **있음** |
| ⑥ Amazon Apprenticeship | ① **Registered Apprenticeship** (DOL 인증 명시) | **있음** |

### ⑤-a의 분류가 애매하다

WBLP는 **12개월 유급 훈련 후 AWS 데이터센터 정규직 배치**다. 고용 관계와 유급이라는 점에서 등록 견습과 같지만, **DOL 등록 여부가 공식 페이지에 명시돼 있지 않다.**

| 구분 | 등록됐다면 | 등록 안 됐다면 |
|---|---|---|
| 자격 | 전국 통용 | AWS 내부 이력 |
| 이직 시 | 다른 사업장에서 인정 | 경력으로만 |

→ **M5에서 확인할 항목.** apprenticeship.gov 프로그램 검색 또는 WA L&I 등록 목록에서 AWS 이름을 조회하면 판별된다.

## 참조

- 미 노동부 견습 포털: https://www.apprenticeship.gov/employers/registered-apprenticeship-program
- WA 주 L&I 견습: https://www.apprenticeship.lni.wa.gov/
- WA 주 견습 프로그램 공개 검색: https://secure.lni.wa.gov/arts-public/
