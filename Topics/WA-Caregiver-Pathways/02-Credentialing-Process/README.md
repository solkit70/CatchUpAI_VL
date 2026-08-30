---
title: "M2 - 자격 취득 절차 해부"
created: 2026-08-30 06:55:00
tags:
  - wa-caregiver
  - m2
---

**모듈**: M2 / **상태**: 완료 (2026-08-30) / **소요**: 약 55분

## 요약

M2는 M1에서 발견한 "취업이 먼저" 구조를 자격 취득 절차로 풀어 쓴 모듈이다. HCA는 일반 자격증처럼 교육과 시험을 먼저 끝내고 취업하는 구조가 아니라, 채용 후 오리엔테이션·안전교육, DOH 신청, 75시간 교육, 시험, 자격 발급이 정해진 시계 안에서 진행된다.

가장 중요한 갱신은 **200일 vs 365일**이다. RCW 18.88B.021의 기본 규정은 200일이지만, 2026-08-30 현재 WAC 246-980-030/040은 2025-08-25부터 2027-12-31까지 한시적으로 365일, provisional certificate가 있으면 425일을 적용한다. 따라서 커뮤니티 안내 자료에는 "기본법은 200일, 현재 적용 중인 한시 규칙은 365일"로 써야 한다.

## 학습 순서

1. [examples/credential-steps.md](examples/credential-steps.md) — HCA·IP·NAC/NAR 절차를 단계, 기한, 비용, 담당 기관 기준으로 정리한다.
2. [examples/entry-barriers.md](examples/entry-barriers.md) — 무경력자가 실제로 막힐 수 있는 지점을 경로별로 정리한다.
3. [guides/background-check.md](guides/background-check.md) — DSHS/BCCU 배경조회와 IP·기관 소속 경로의 차이를 정리한다.

## M1에서 넘긴 미확인 항목 처리

| M1 이월 항목 | M2 처리 결과 |
|---|---|
| SB 5672의 365일 조항과 200일의 관계 | 해결. WAC 246-980-030/040의 한시 규칙으로 365일/425일 적용. RCW 18.88B.021의 200일 기본 규정과 함께 병기 필요 |
| IP 계약 시 기한 기산점 | 부분 해결. WAC 246-980-010은 date of hire를 첫 고용일 또는 유급 직접 돌봄 제공일로 정의. CDWA IP에서는 `Okay to Provide Care` 날짜와 연결되는지 추가 확인 필요 |
| NAC vs NAR 차이 | 해결. WAC 246-841A-390은 nursing assistants에 registered와 certified가 모두 포함된다고 정의하고, NAC는 certified credential, NAR는 registered credential로 구분 |
| 가족 돌봄 면제의 `VA-funded only` 범위 | 해결. WAC 246-980-025 기준 spouse/domestic partner는 2026-07-01부터 VA-funded 요건 없이 면제 가능 |
| 신청비·시험비 금액 | 해결. HCA 신청 $100, HCA knowledge $49, skills $101. NAC/NAR initial application $85, NAC knowledge $55, skills fee는 training program별 상이 |
| 면제 목록 출처 불일치 | 해결 방향 확정. HCA certification exemption은 WAC 246-980-025, 70-hour basic training exemption은 WAC 388-112A-0090으로 층위가 다름 |
| Certified Home Care Aide Checklist 원문 | 부분 해결. DOH Certification Information의 Application Quick Guide/packet 경로 확인. 세부 체크리스트 원문은 M4 또는 지원 직전 재확인 |

## 핵심 결론

### 1. HCA의 현재 실무 시계는 14일 / 120일 / 365일

채용 후 14일 안에 DOH 신청서를 제출하고, 120일 안에 75시간 교육을 끝내며, 현재 한시 규칙상 365일 안에 HCA 자격을 받아야 한다. provisional certificate가 있으면 425일까지 가능하다. 200일은 RCW 기본 문구로 남아 있으므로, 안내 자료에서는 현재 적용 규칙과 기본법을 분리해 설명해야 한다.

### 2. 면제는 두 종류다

HCA certification 자체를 면제하는 조항은 WAC 246-980-025다. 반면 70-hour basic training 면제는 WAC 388-112A-0090이다. M1에서 PDF와 FAQ의 면제 목록이 달라 보였던 이유는 출처가 틀렸다기보다 **무엇의 면제인지가 달랐기 때문**이다.

### 3. 파트타임 IP 가능성은 실제로 중요하다

월 20시간 이하로 한 사람에게 in-home care를 제공하는 long-term care worker는 HCA certification 면제 대상이다. 이 조항은 사용자의 "파트타임 가능성이 높다"는 조건과 직접 연결된다. 다만 certification 면제와 급여·복지 자격은 별개이므로 M3에서 의료보험 조건과 함께 다시 봐야 한다.

### 4. 배경조회는 개인이 단독으로 먼저 시작하는 절차가 아니다

DSHS 배경조회 페이지와 DOH FAQ 모두 채용 주체 또는 hiring entity를 먼저 접촉하라고 안내한다. IP의 경우 CDWA가 hiring process에서 background check code를 받는 구조다. 따라서 "미리 배경조회부터 받아 두기"는 기본 경로가 아니다.

## DoD

- [x] 3개 경로 전부 절차 단계도 완성 (기간·비용 포함)
- [x] 단계 간 선후 관계 명시
- [x] 무경력자 진입 장벽 목록 작성
- [x] 배경조회 절차·소요 기간 문서화
- [x] 확인 불가 항목마다 시도 경로와 다음 문의처 기록
- [x] README 작성
- [x] WorkLog + Daily Retrospective 작성

**완료율**: 7/7

## 이전 / 다음

- 이전: [../01-Role-Landscape/README.md](../01-Role-Landscape/README.md)
- 다음: **M3 - 급여·복지 비교 (의료보험 중심)** — `../03-Pay-and-Benefits/` (미생성)
