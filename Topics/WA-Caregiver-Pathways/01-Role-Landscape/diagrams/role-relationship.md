---
title: "세 경로 관계도"
created: 2026-08-29 03:40:00
tags:
  - wa-caregiver
  - m1
  - diagram
---

## 층위 구조 — 나란한 3개가 아니다

```mermaid
flowchart TB
    LTC["Long-Term Care Worker<br/>상위 직군"]
    subgraph EMP["고용 형태"]
        direction LR
        AG["기관 소속<br/>home care agency<br/>assisted living<br/>adult family home"]
        IP["IP<br/>Individual Provider<br/>DSHS와 직접 계약"]
    end
    HCA["HCA 자격<br/>Home Care Aide<br/>채용일 +365일 내 취득<br/>(2025-08-25~2027-12-31 한시)"]
    NAC["NAC<br/>Nursing Assistant-Certified<br/>HCA 인증 면제 대상"]
    EX["면제 대상<br/>월 20시간 이하 IP<br/>respite 연 300시간 미만<br/>가족 돌봄 등"]

    LTC --> AG
    LTC --> IP
    AG --> HCA
    IP --> HCA
    IP -.면제 조건 해당 시.-> EX
    HCA -->|"NAC Bridge 38시간"| NAC
    NAC -.면제.-> HCA
```

**읽는 법**

- **IP는 HCA의 대안이 아니다.** IP는 고용 형태이고, IP로 일하면 HCA 자격 대상이 된다
- **NAC는 위층이다.** NAC를 가지면 HCA 인증이 면제된다
- **HCA → NAC로 올라가는 지정 경로가 있다** — Bridge 38시간

## 진입 순서 — 취업이 먼저다

```mermaid
flowchart TB
    A["무자격 · 무경력"] --> B["채용<br/>date of hire"]
    B --> C["근무 시작 전<br/>오리엔테이션 2h + 안전교육 3h"]
    C --> D["근무 시작"]
    D --> E["채용 +14일<br/>DOH 신청서 제출"]
    D --> F["채용 +120일<br/>75시간 교육 이수"]
    F --> G["Prometric 시험<br/>지식 + 술기"]
    G --> H["채용 +365일<br/>HCA 자격 취득<br/>(provisional +425일)"]
    H --> I["매년 생일 갱신<br/>연 12시간 보수교육"]
    H -.희망 시.-> J["NAC Bridge 38시간<br/>→ NAC"]
```

**일반 자격증 직종과 반대다.**

| | 일반적인 순서 | **WA HCA** |
|---|---|---|
| 1 | 교육 | **채용** |
| 2 | 시험 | 오리엔테이션·안전교육 |
| 3 | 자격 취득 | 근무 시작 |
| 4 | 취업 | 교육 → 시험 → 자격 |

> **"If you are not currently working, you are not able to obtain the DSHS background check."**
>
> 고용 전에는 배경조회를 받을 수 없으므로 **자격을 미리 딸 수 없다.**

## 관계 판정 요약

| 질문 | 답 |
|---|---|
| 세 경로가 같은 층위인가 | ❌ **아니다** |
| 병렬인가 계단식인가 | **혼합.** IP는 고용 형태(병렬 아님), HCA→NAC는 계단식 |
| 하나를 고르는 구조인가 | ❌ IP + HCA는 함께 간다 |
| 진입 순서는 | **취업 → 교육 → 자격** |

## 참조

- 세 경로 정의: [../concepts/three-roles.md](../concepts/three-roles.md)
- 일정 스캔: [../examples/intake-calendar.md](../examples/intake-calendar.md)
