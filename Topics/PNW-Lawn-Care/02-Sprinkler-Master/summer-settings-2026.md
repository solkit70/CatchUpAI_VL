---
title: "여름 스프링클러 세팅 가이드 2026"
created: 2026-07-01
system: "Rain Bird ESP-ME3"
location: "Tehaleh, WA (Zone 8b)"
---

# 여름 스프링클러 세팅 가이드 2026

> **용도**: 컨트롤러 앞에서 보면서 바로 세팅 변경용

---

## 현재 Program 구성

| Program | 대상 | 스테이션 | Start Time | Water Days | Run Time |
|---------|------|---------|------------|------------|----------|
| A | 앞마당 잔디 | St. 2, 4 | 5:00 AM | 매일 | 10분 |
| B | 뒷마당 잔디 | St. 6, 7, 8 | 5:30 AM | 매일 | 10분 |
| C | Bark/화단 드립 | St. 1, 3, 5 | 6:15 AM | 월/수/금 | 20분 |

> Start Time은 여름에도 새벽 유지 — 낮 관수는 증발 손실 30~50% ❌

---

## 월별 세팅 변경표

| 월 | Seasonal Adjust | Water Days | Run Time | 비고 |
|----|----------------|------------|---------|------|
| **7월** | **130%** | **A/B: 매일, C: 월/수/금** | A/B 10분, C 20분 | ← 지금 적용할 것 |
| **8월** | **140~150%** | **격일~매일** | A/B 10~15분, C 20분 유지 | 폭염 시 매일 |
| 9월 | 100% | 월/수/금 | 10분 | 기온 하락 후 |
| 10월 | 50~60% | 화/목 | 10분 | 강수 재개 |
| 11월 | — | — | — | 시스템 OFF |

> Program C (화단)는 **월/수/금 6:15 AM, 20분**으로 변경

---

## 봄철 Auto 세팅 → 여름용 전환 요약

현재 컨트롤러가 봄철 Auto 세팅으로 되어 있다면, 여름용으로 바꿀 때는 **Seasonal Adjust, Water Days, Start Time, Run Time**을 모두 확인한다. 특히 Start Time은 프로그램별로 하나만 남기고 나머지는 OFF로 둔다.

| 항목 | 봄철 기준 | 여름용 목표 |
|------|-----------|-------------|
| Seasonal Adjust | 70~100% | 130% |
| Program A | 월/수/금, 6:00 AM, 10분 | 매일, 5:00 AM, 10분 |
| Program B | 월/수/금, 6:45 AM, 10분 | 매일, 5:30 AM, 10분 |
| Program C | 화/목 또는 월/수/금, 7:30 AM, 10분 | 월/수/금, 6:15 AM, 20분 |
| 다이얼 위치 | AUTO | AUTO 유지 |

Program C는 Bark/화단 드립 구역이라 잔디보다 물이 천천히 들어간다. 그래서 빈도는 월/수/금으로 유지하되, Run Time은 20분으로 길게 잡는다.

---

## 7월 여름용 세팅 — 조작 순서

### ① Seasonal Adjust → 130%

```
1. 다이얼 → "Seasonal Adjust" 위치
2. 현재 % 확인
3. ▲ 버튼으로 130%까지 올리기 (5% 단위)
4. 자동 저장 (별도 저장 불필요)
```

### ② Program A 설정 → 매일 / 5:00 AM / 10분

```
1. Program A 선택
2. Start Times → Start Time 1 = 5:00 AM, 나머지 Start Time = OFF
3. Water Days → 월/화/수/목/금/토/일 모두 ON
4. Run Times → St. 2 = 10분, St. 4 = 10분
5. SAVE
```

### ③ Program B 설정 → 매일 / 5:30 AM / 10분

```
1. Program B 선택
2. Start Times → Start Time 1 = 5:30 AM, 나머지 Start Time = OFF
3. Water Days → 월/화/수/목/금/토/일 모두 ON
4. Run Times → St. 6 = 10분, St. 7 = 10분, St. 8 = 10분
5. SAVE
```

### ④ Program C 설정 → 월/수/금 / 6:15 AM / 20분

```
1. Program C 선택
2. Start Times → Start Time 1 = 6:15 AM, 나머지 Start Time = OFF
3. Water Days → 월/수/금 ON, 화/목/토/일 OFF
4. Run Times → St. 1 = 20분, St. 3 = 20분, St. 5 = 20분
5. SAVE
```

### ⑤ 다이얼 → AUTO 확인

```
세팅 완료 후 다이얼이 AUTO에 있는지 확인
```

---

## 세팅 후 실제 관수량 계산

```
7월 기준:
A/B: Run Time 10분 × Seasonal Adjust 130% = 실제 13분/스테이션
A/B: 13분 × 7회/주 = 91분/주 → 약 0.76인치/주
C: Run Time 20분 × Seasonal Adjust 130% = 실제 26분/스테이션
C: 26분 × 3회/주 = 78분/주

여름 목표: 주당 1~1.5인치
→ A/B 잔디가 부족하면 Run Time을 15분으로 올리거나, 8월엔 Seasonal Adjust 추가 상향
→ C 화단은 Bark 아래 흙이 계속 마르면 20분 유지 후 빈도 조정 검토
```

---

## A/B 잔디 Run Time 올리는 방법 (필요 시)

```
1. 다이얼 → "Set Watering Times"
2. Program A 선택
3. 각 스테이션 → ▲ 버튼으로 10분 → 15분
4. SAVE
5. Program B도 동일하게 반복
```

---

## 잔디 스트레스 현장 체크

컨트롤러 조정 전후로 마당에서 직접 확인:

| 확인 방법 | 결과 | 대응 |
|----------|------|------|
| 발자국이 15분 이상 남음 | 수분 부족 | Manual Run 즉시 |
| 잎이 청회색으로 변색 | 심각한 건조 | Run Time 늘리기 |
| 잎이 말리거나 접힘 | 건조 스트레스 | Seasonal Adjust 상향 |
| 발자국 5분 내 회복 | 수분 양호 | 현재 설정 유지 |

---

## Manual Run (긴급 관수) 방법

```
1. 다이얼 → "Manual Run" (또는 "Run One Station")
2. 스테이션 선택
3. Run Time 설정
4. START 버튼
※ 자동 스케줄에 영향 없음
```

---

## 8월 조정 체크리스트

- [ ] Seasonal Adjust → 140~150%
- [ ] 발자국 테스트 주 2회 이상 실시
- [ ] 폭염(90°F+) 지속 시 Water Days → 격일 또는 매일
- [ ] A/B 잔디 Run Time → 15분 검토
- [ ] C 화단은 Bark 아래 흙 상태 확인 후 20분 유지 여부 판단

---

## 11월 시스템 OFF 준비

- [ ] 다이얼 → OFF
- [ ] Backflow 테스트 예약: Yard Works Inc. **253-177-8238**
- [ ] Winterize 일정 확인

---

**참조**: `02-Sprinkler-Master/spring-schedule-2026.md` — 봄 세팅 기록
**참조**: `03-Summer-Troubleshoot/summer-schedule-plan.md` — 월별 계획 원본
