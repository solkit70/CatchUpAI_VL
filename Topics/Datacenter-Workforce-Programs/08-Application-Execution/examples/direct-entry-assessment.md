# 직접 입사 가능성 판정 — shortlist를 우회할 수 있는가

**작성일**: 2026-08-31 · **M8 실습 1 부속**
**질문**: 기존 IT 경력으로 교육 프로그램 없이 **일반 Data Center Technician 에 바로 지원**할 수 있는가

> ⚠️ **이 문서는 Topic 범위 밖이다** (2026-08-31 사용자 지적).
>
> 이 Topic 의 목적은 **"빅테크가 교육을 지원하고 일자리까지 연결하는 프로그램"** 을 조사하고
> 가능하면 지원하는 것이다. **일반 구직 활동이 아니다.**
> 이 문서는 그 경계를 넘어 채용 공고를 조사한 기록이므로 **부속 자료로만 남긴다.**
>
> **다만 두 가지는 본선에 유효하다** — 아래 「본선에 남는 것」 참조.

---

## 왜 이 질문이 나왔나

M7 shortlist 는 **"진입 요건 없음 · 경력 요건 없음"** 을 장점으로 놓고 짜였다.
그런데 2026-08-31 에 사용자 LinkedIn 을 확인하니 전제가 달랐다.

| 확인된 이력 | |
|---|---|
| **AWS Certified Cloud Practitioner** | 2020-03 |
| Oracle OCP DBA 9i | 2003 |
| SAP ABAP Development Consultant | 2009 |
| TOSCA Automation Specialist L1·L2 | 2020 |
| Core Java · Test Automation · Power BI (Coursera) | 2021~2022 |
| 근무 지역 | Bellevue · Chicago · San Diego · Seoul · Rotterdam · Zilina · Pune |
| 학력 | 강원대학교 (South Korea) |

**20년 이상의 IT 경력자가 "경력 요건 없는 입문 프로그램"을 찾고 있었다.**
문을 잘못 고른 것일 수 있어 확인했다.

---

## 판정 1 — 자격 요건: **통과 가능성이 높다**

M5 가 확보한 일반 Data Center Technician 공고 원문이다.

> *"2+ years of computer/server hardware troubleshooting experience, **or experience related IT**;
> 2+ years of computer layer 1/2 networking (including troubleshooting and repair) experience"*

M5 는 이 문장을 **"WBLP(무경력)와 일반 DCT(2년) 사이의 큰 문턱"** 으로 읽었다.
그런데 **`or experience related IT`** 가 있다. 서버 하드웨어 트러블슈팅이 아니어도
**관련 IT 경력이면 대체된다**는 뜻이다.

| 요건 | 사용자 이력 | 판정 |
|---|---|---|
| 서버/하드웨어 트러블슈팅 2년 **또는 관련 IT 경력** | DBA · ABAP 개발 · 테스트 자동화 20년+ | ✅ **충족 가능성 높음** |
| Layer 1/2 네트워킹 2년 | ❓ 이력에서 확인 안 됨 | ⚠️ **약점** |
| 클라우드 기초 이해 | **AWS CCP 보유** | ✅ 유리 |

**약점은 네트워킹 한 줄이다.** 케이블링·스위치·물리 계층 경험이 이력에 안 보인다.
다만 이건 **교육 프로그램 1년으로 메우기엔 과한 격차**이고, 자격증(CompTIA Network+ 등)이나
Cisco Packet Tracer 실습으로 훨씬 짧게 보완할 수 있는 종류다.

> **M7 이 "기다림을 준비로 바꾸는 유일한 항목"이라고 부른 Cisco Packet Tracer 가
> 여기서 의미가 달라진다.** 대기 중 소일거리가 아니라 **직접 입사의 유일한 약점을
> 메우는 작업**이다.

---

## 판정 2 — 그런데 **자리가 없다.** 이것이 진짜 제약이다

자격이 되는지보다 **지원할 공고가 근처에 있는지**가 먼저였다.

### AWS — 워싱턴주 데이터센터 기술직 **0건**

`amazon.jobs` 검색 JSON 을 직접 조회했다 (M5 와 같은 방법).

| 검색어 | 미국 전체 | **워싱턴주** |
|---|---:|---:|
| data center technician | 1,337 | **0** |
| engineering operations technician | 다수 | **0** |
| data center operations | 다수 | **0** |

워싱턴주 결과 4건은 전부 **시애틀 소재 엔지니어링·설계직**이었다 —
Mechanical BIM Designer, Cloud Hardware Development Engineer, NW Deployment Planner.
**기술직이 아니다.**

실제 DCT 공고가 있는 곳:

```
Umatilla, Oregon        New Carlisle, Indiana      Aurora, Colorado
Hilliard, Ohio          Leesburg, Virginia         Fredericksburg, Virginia
Jeffersonville, Ohio
```

**가장 가까운 것이 오리건 Umatilla — 편도 약 200마일이다.**

### Sabey — 워싱턴주 운영직은 **East Wenatchee**

Sabey 는 미국 최대 민간 데이터센터 사업자이고 **Tukwila(Intergate.Seattle)에 시설이 있다.**
그런데 자체 채용 페이지의 워싱턴주 공고는 이렇다.

| 직무 | 위치 |
|---|---|
| Data Center Operations Electrical Engineer II | **East Wenatchee** |
| IT Support Lead · IT Help Desk Supervisor | Seattle (본사) |
| Director of Procurement · Corporate Counsel 등 | Seattle (본사) |

**Tukwila 운영직 공고는 현재 없다.**

> ⚠️ 집계 사이트(Indeed·ZipRecruiter·Glassdoor)는 시애틀 지역 *"data center technician"*
> 을 626~2,440건으로 표시하지만, **AWS·Microsoft 본사의 데이터센터 *관련* 사무직이
> 대량 포함된 수치**다. 사업자 자체 페이지로 확인하면 Puget Sound 운영 기술직은 희소하다.
> **집계 숫자를 근거로 쓰지 않는다.**

### 구조 — 워싱턴주 데이터센터는 중부에 있다

| 지역 | 시설 |
|---|---|
| **Quincy** | Microsoft(Columbia DC) · Vantage(89MW) · H5 등 16곳 |
| **East Wenatchee / Malaga** | Sabey(70MW×다수) · Microsoft 신설 중 |
| **Moses Lake** | ServerFarm(32MW) · Bitfarms(21MW) |
| Puget Sound | Sabey Intergate.Seattle(Tukwila) · Westin Building — **상대적으로 소수** |

중부에 몰린 이유는 **저렴한 수력 전기**다. 이건 바뀌지 않는 구조다.

---

## 결론 — shortlist 는 우회 대상이 아니었다. 다만 **이유가 달랐다**

들어가기 전 가설은 *"경력이 있으니 입문 프로그램이 불필요할 것"* 이었다.
**절반만 맞았다.**

| | 가설 | 실측 |
|---|---|---|
| 자격 요건 | 넘을 것이다 | ✅ **넘을 가능성 높음** (네트워킹 한 줄 제외) |
| 지원할 자리 | 있을 것이다 | ❌ **Puget Sound 에 거의 없다** |

**병목은 자격이 아니라 지리다.**

그리고 이 발견은 M7 의 판단을 **뒤집는 게 아니라 다시 설명한다.**

> **BBCC(Moses Lake)의 편도 180마일은 학교가 멀어서가 아니다.
> 일자리가 거기 있기 때문이다.**

M5 는 *"거리 제약의 방향이 예상과 반대였다 — 교육기관이 멀고 고용지는 가깝다"* 라고
적었는데, **그 판단의 근거였던 Kent WA 고용지에 실제 공고가 0건**이다.
교육기관과 고용지가 **둘 다 중부에 있다.**

---

## 이 판정이 바꾸는 것

### ① 1순위 AWS WBLP 의 성격이 달라진다

*"경력 문턱을 건너는 유일한 통로"* 로 봤는데, 자격이 이미 된다면 **WBLP 의 값어치는
문턱 통과가 아니라 「Kent WA 라는 위치」** 다. 그런데 그 위치의 공고가 0건이다.

→ **알림 등록은 유지하되, 1순위 지위는 재검토 대상.**

### ② 통근 판정을 다시 해야 한다

[M5 통근 분류](../../05-WA-Deep-Dive/examples/commute-feasibility.md)가 *"고용지는 가깝다(Kent·Renton 20~25마일)"*
를 전제로 짜였다. **그 전제가 실측으로 무너졌다.**

### ③ 새 선택지가 생긴다 — 원격 근무 IT 직무

데이터센터 기술직은 물리적으로 현장에 있어야 하지만, **사용자 이력의 대부분(DBA·개발·
테스트 자동화)은 원격 가능한 직군**이다. 이 Topic 의 범위 밖이지만
**같은 목적(생활비)을 훨씬 짧은 경로로 달성할 수 있는지**는 별도로 볼 만하다.

→ [WA-Caregiver-Pathways](../../../WA-Caregiver-Pathways/README.md) 와 함께
「생계 경로」 갈래로 묶여 있는 주제다.

---

## 다음에 확인할 것

- [ ] **네트워킹 격차의 실제 크기** — 공고가 요구하는 Layer 1/2 수준이 무엇인지. CompTIA Network+ 로 충분한가
- [ ] **오리건 Umatilla 통근·이주 판정** — 편도 200마일. M7 탈락선(주 3일 이상 체류)에 걸리는가
- [ ] **Puget Sound 사업자 직접 확인** — Sabey Tukwila 외에 Westin Building 등 운영 주체의 채용 주기
- [ ] **집계 사이트가 아닌 사업자 페이지로** 월 1회 공고 점검 루틴

## 출처

- `amazon.jobs` 검색 JSON 직접 조회 (2026-08-31)
- [Sabey Data Centers 채용](https://sabeydatacenters.com/careers) (2026-08-31)
- [Washington Data Center Map](https://dcmap.us/states/washington/) · [Quincy 데이터센터 목록](https://www.datacenters.com/locations/united-states/washington/quincy)
- [M5 WA 기관 조사](../../05-WA-Deep-Dive/examples/wa-institutions.md) — 일반 DCT 공고 원문
- 사용자 LinkedIn (2026-08-31 사용자 제공)

---

## 본선에 남는 것 — Topic 범위 안의 사실 두 가지

이 조사가 범위를 벗어났지만, **프로그램 판단에 직접 쓰이는 사실**이 둘 나왔다.

### 1. 워싱턴주 데이터센터는 중부에 있다

| 지역 | 시설 |
|---|---|
| **Quincy · East Wenatchee · Moses Lake** | Microsoft · Vantage · Sabey · ServerFarm 등 다수 |
| Puget Sound | 소수 |

**② Microsoft Datacenter Academy 가 BBCC(Moses Lake)에 있는 이유가 이것이다.**
프로그램이 일자리 옆에 있다. 편도 180마일은 **학교가 멀어서가 아니라 산업이 거기 있어서**다.

→ [M5 통근 판정](../../05-WA-Deep-Dive/examples/commute-feasibility.md)의 *"고용지는 가깝다(Kent·Renton)"*
전제는 재검토가 필요하다.

### 2. ⑤ WBLP 의 값어치가 달라진다

WBLP 를 *"경력 문턱을 건너는 통로"* 로 봤는데, 일반 DCT 요건이
*"2+ years ... **or experience related IT**"* 이므로 **문턱 자체가 낮을 수 있다.**

그렇다면 WBLP 의 값어치는 문턱 통과가 아니라 **「Kent WA 라는 위치 + 유급 + 직고용 보장」** 이다.
프로그램으로서의 매력은 그대로지만 **1순위 근거는 바뀐다.**
