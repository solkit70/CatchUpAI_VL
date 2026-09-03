---
title: "M3 - 자격 체계와 견습(apprenticeship) 제도"
created: 2026-08-28 21:45:00
tags:
  - datacenter-workforce
  - m3
---

<!-- lang-switch -->
🇰🇷 **한국어** · [🇺🇸 English](README.en.md)
<!-- lang-switch -->

## 요약

M2가 "6개 프로그램이 각각 무엇인가"를 밝혔다면, M3는 **"그 프로그램들이 자격 체계에서 어디에 놓이는가"** 를 정리한다.

같은 "교육 프로그램"이라는 말 아래 성격이 전혀 다른 넷이 섞여 있었다 — **등록 견습 · 예비 견습 · 인증과정 · 학위.** 어느 형태인지에 따라 **훈련 중 수입이 있는지, 끝나고 무엇이 남는지, 지원을 어디에 하는지**가 전부 달라진다.

## 핵심 발견

### 1. 등록 견습만 훈련 중 수입이 있다

DOL이 직접 쓴 표현이 **"Apprenticeships are jobs!"** 다. 학생이 아니라 직원이고, 첫날부터 임금이 나오며 숙련도에 따라 오른다.

나머지 셋(예비 견습·인증과정·학위)은 **배우는 동안 수입이 없다.**

> **비용이 0이어도 1년간 수입이 없으면 실질 비용은 1년치 생활비다.** 직종 전환에서는 이 한 가지가 나머지 조건을 압도할 수 있다.

### 2. 6개 프로그램을 자격 형태로 다시 분류하면

| 프로그램 | 자격 형태 | 훈련 중 수입 |
|---|---|---|
| ① Meta AWA | Certificate | **있음** (무료 + 일당) |
| ② MS Datacenter Academy | Certificate / Degree | 없음 |
| ③ MS NABTU | Pre-apprenticeship + 부가 교육 | 없음 |
| ④ Google.org / etA | **Registered Apprenticeship** | **있음** |
| ⑤-a AWS WBLP | **등록 여부 미확인** — 고용 관계 있음, 유급 | **있음** |
| ⑥ Amazon Apprenticeship | **Registered Apprenticeship** (DOL 인증) | **있음** |

### 3. ⑤-a의 분류가 애매하다 — M5 확인 항목

WBLP는 12개월 유급 후 AWS 정규직 배치다. **고용 관계와 유급이라는 점에서 등록 견습과 같지만 DOL 등록 여부가 공식 페이지에 없다.**

| 등록됐다면 | 등록 안 됐다면 |
|---|---|
| 전국 통용 자격 | AWS 내부 이력 |
| 이직 시 인정 | 경력으로만 |

M2에서 WBLP를 최적 후보로 판정했는데, **이 항목이 그 판정의 강도를 바꾼다.**

### 4. 두 트랙은 진입 관문 자체가 다르다

| | 트랙 A 숙련직 | 트랙 B 기술직 |
|---|---|---|
| 진입 | **노조 local JATC 선발** — 경쟁·대기 존재 | **채용 공고 지원** |
| 기간 | 8,000시간 (약 4~5년) | 12개월 (WBLP) |
| 최종 고용주 | 조합 건설사 (프로젝트 단위) | 데이터센터 운영사 (상시) |

M1의 **"건설기 × 기술직 칸은 구조적 공백"** 이 경로 차원에서 다시 확인됐다. **짓는 사람과 돌리는 사람은 애초에 다른 문으로 들어온다.**

### 5. 표준서에 답이 다 있다

비교표에서 비어 있던 항목들 — **견습 시작 임금 비율, 신체 요구 조건, 선발 배점** — 은 조사가 부족해서가 아니라 **WSATC 프로그램 표준서 PDF에 프로그램별로 따로 규정**돼 있기 때문이다. 전국 단일 값이 없다.

→ M5에서 Puget Sound Electrical JATC 표준서(WSATC-0134)를 열면 채워진다.

## 산출물

- [concepts/credential-types.md](concepts/credential-types.md) — 4종 자격 형태 구분, 6개 프로그램 분류
- [examples/career-pathways.md](examples/career-pathways.md) — 2트랙 경로도 (기간·비용·수입)
- [examples/track-comparison.md](examples/track-comparison.md) — 7항목 × 2트랙 비교표
- [guides/union-local-entry.md](guides/union-local-entry.md) — 노조 local 진입 절차

## M5로 넘기는 미확인 항목

| # | 항목 | 확인처 |
|---|---|---|
| 1 | **WBLP의 DOL 등록 여부** | apprenticeship.gov / L&I 등록 목록 |
| 2 | **WBLP 훈련 기간 임금** | Kent WA 실제 공고 (WA는 임금 공개 의무 주) |
| 3 | **견습 시작 임금 비율** | WSATC-0134 표준서 · L&I 견습 임금 조회 |
| 4 | **신체 요구 조건 — 양 트랙 모두** | 표준서 및 실제 공고의 physical requirements |
| 5 | JATC 선발 경쟁률·대기 기간·모집 시기 | Puget Sound Electrical JATC 문의 |

**4번이 양쪽 다 비어 있다.** 두 트랙 모두 현장 작업이고 공식 페이지에 잘 나오지 않는다. M7 판단에 직접 영향을 주므로 M5에서 반드시 확보한다.

## 이전 / 다음

- 이전: [M2 - 프로그램 해부](../02-Program-Anatomy/README.md)
- 다음: **M4 - 전미 지역 지도**
  단, **M5(워싱턴주 정밀 조사)의 우선순위가 올라갔다.** M4는 시청자 정보 제공용이고, 본인 지원과 직결되는 것은 M5다. 순서 조정은 사용자 판단.
