---
title: "여름 스프링클러 세팅 가이드 2026"
created: 2026-07-01
system: "Rain Bird ESP-ME3"
location: "Tehaleh, WA (Zone 8b)"
---

# 여름 스프링클러 세팅 가이드 2026

> **용도**: 컨트롤러 앞에서 보면서 바로 세팅 변경용

---

## 현재 Program 구성 (변경하지 않음)

| Program | 대상 | 스테이션 | Start Time |
|---------|------|---------|------------|
| A | 앞마당 잔디 | St. 2, 4 | 6:00 AM |
| B | 뒷마당 잔디 | St. 6, 7, 8 | 6:45 AM |
| C | Bark/화단 드립 | St. 1, 3, 5 | 7:30 AM |

> Start Time은 여름에도 새벽 유지 — 낮 관수는 증발 손실 30~50% ❌

---

## 월별 세팅 변경표

| 월 | Seasonal Adjust | Water Days | Run Time | 비고 |
|----|----------------|------------|---------|------|
| **7월** | **130%** | **월~금 (5회)** | 10분 | ← 지금 적용할 것 |
| **8월** | **140~150%** | **격일~매일** | 10~15분 | 폭염 시 매일 |
| 9월 | 100% | 월/수/금 | 10분 | 기온 하락 후 |
| 10월 | 50~60% | 화/목 | 10분 | 강수 재개 |
| 11월 | — | — | — | 시스템 OFF |

> Program C (화단)는 Water Days 변경 없이 **화/목 유지**

---

## 7월 즉시 적용 — 조작 순서

### ① Seasonal Adjust → 130%

```
1. 다이얼 → "Seasonal Adjust" 위치
2. 현재 % 확인
3. ▲ 버튼으로 130%까지 올리기 (5% 단위)
4. 자동 저장 (별도 저장 불필요)
```

### ② Water Days → 월~금 (Program A, B)

```
1. 다이얼 → "Water Days"
2. Program A 선택
3. Specific Days 선택
4. 월/화/수/목/금 선택 (토/일 제외)
5. SAVE
6. ◄ ► 버튼으로 Program B 선택
7. 동일하게 월/화/수/목/금 설정
8. SAVE
※ Program C는 화/목 그대로 유지
```

### ③ 다이얼 → AUTO 확인

```
세팅 완료 후 다이얼이 AUTO에 있는지 확인
```

---

## 세팅 후 실제 관수량 계산

```
7월 기준:
Run Time 10분 × Seasonal Adjust 130% = 실제 13분/스테이션
13분 × 5회/주 = 65분/주 → 약 0.54인치/주

여름 목표: 주당 1~1.5인치
→ 부족 시 Run Time을 15분으로 올리거나, 8월엔 Seasonal Adjust 추가 상향
```

---

## Run Time 올리는 방법 (필요 시)

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
- [ ] Run Time → 15분 검토

---

## 11월 시스템 OFF 준비

- [ ] 다이얼 → OFF
- [ ] Backflow 테스트 예약: Yard Works Inc. **253-177-8238**
- [ ] Winterize 일정 확인

---

**참조**: `02-Sprinkler-Master/spring-schedule-2026.md` — 봄 세팅 기록
**참조**: `03-Summer-Troubleshoot/summer-schedule-plan.md` — 월별 계획 원본
