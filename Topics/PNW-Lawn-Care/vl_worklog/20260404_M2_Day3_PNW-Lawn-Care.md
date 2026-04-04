# WorkLog - 2026-04-04: ESP-ME3 Program B/C 설정 완료 + Scotts Halts 이해

**날짜**: 2026-04-04
**Topic**: PNW-Lawn-Care
**모듈**: M2 - Rain Bird ESP-ME3 마스터 (Day 3)
**학습 시간**: (기록 예정)

---

## 🎯 오늘의 목표

- [x] Program A에서 Bark 스테이션(1, 3, 5) 제거 → St. 2, 4만 남기기
- [x] Program B 설정: 뒷마당 잔디 (St. 6, 7, 8) / 6:45 AM / 월/수/금 / 10분
- [x] Program C 설정: Bark/화단 (St. 1, 3, 5) / 7:30 AM / 화/목 / 10분
- [x] Program A Water Days: 3-day cycle → 월/수/금
- [x] Scotts Turf Builder Halts 제품 심층 이해
- [ ] 다이얼 → AUTO 전환 (5월 초로 연기 — 의도적 결정)
- [ ] current-settings-audit.md 최종 업데이트

---

## ✅ 어제 (2026-04-03) 완료된 작업 (기록)

- [x] **Scotts Turf Builder Halts Crabgrass Preventer with Lawn Food 살포**
  - 제품: Pre-emergent + 비료 2-in-1 (5,000 sq ft / 13.35 lb)
  - 날씨: 양호 (살포 적합)
- [x] **Manual Run 워터링 완료**
  - 전 스테이션 (8개) × 10분 = 총 80분 관수
  - 목적: Pre-emergent 활성화 (토양에 장벽막 형성)

---

## 📚 진행 내용

### 1. Scotts Turf Builder Halts 심층 이해

#### 제품 정보

| 항목 | 내용 |
|------|------|
| 제품명 | Scotts Turf Builder Halts Crabgrass Preventer with Lawn Food |
| 기능 | Pre-emergent 제초제 + 비료 (2-in-1) |
| 커버리지 | 5,000 sq ft / 13.35 lb |
| 활성 성분 | Pendimethalin (Pre-emergent) |

#### Pre-emergent 원리

Pre-emergent는 이미 자란 잡초를 죽이는 것이 아니라, **씨앗이 발아하는 것을 막는 토양 장벽**을 만든다. 즉:

- ✅ 효과있음: 씨앗 단계의 잡초 (Crabgrass, Annual Bluegrass 등)
- ❌ 효과없음: 이미 자란 잡초, 다년생 잡초 뿌리
- ❌ 부작용: 잔디 씨앗도 발아 막힘 → **살포 후 4개월간 Overseeding 금지**

#### 워터링 요건 (왜 살포 후 바로 물을 줬는가)

살포 직후 워터링(0.5인치 이상)이 필수인 이유:
1. Pendimethalin이 토양 표면 아래로 침투해야 함
2. 수분 없이 햇빛에 노출되면 성분이 분해됨 (광분해)
3. 토양 장벽이 올바르게 형성되려면 물로 활성화 필요

어제 Manual Run 10분 × 8 스테이션 = 약 0.5~1인치 관수 → **올바른 조치** ✅

#### PNW 적용 타이밍

| 조건 | 상태 |
|------|------|
| 살포 최적 시기 | 토양 온도 50°F(10°C) 이하일 때 (Crabgrass 발아 전) |
| 2026-04-03 살포 | 4월 초 PNW → 적절한 타이밍 ✅ |
| 효과 지속 기간 | 약 4개월 (여름 Crabgrass 시즌 커버) |
| 비 예보 주의 | 살포 후 24~48시간 내 강한 비 → 유실 위험 |

#### 살포 후 주의사항

- ❌ **4개월간 Overseeding 금지** — Pre-emergent가 잔디 씨앗도 막음
- ✅ **잔디 깎기**: 살포 2~3일 후부터 가능
- ✅ **애완동물/어린이**: 완전히 건조 후 입장 허용
- ✅ **다음 시비**: 6~8주 후 (이미 비료 포함이므로 중복 살포 금지)

#### 비료 성분 (N-P-K 추정)

Scotts Halts는 봄 비료 + Pre-emergent 조합. 일반적으로:
- 질소(N) 비율이 높아 봄 성장 촉진
- Slow-release 타입으로 6~8주 지속 효과

---

### 2. ESP-ME3 Program 설정 실습

#### Program A 수정 — Bark 스테이션 제거

**목표**: St. 1, 3, 5를 Program A에서 0분(OFF)으로 설정 → St. 2, 4만 남기기

**ESP-ME3 조작법**:
1. 다이얼 → SET WATERING TIMES
2. Program A 선택 확인
3. St. 1 → Run Time → + − 버튼으로 0분 설정
4. St. 3 → 0분
5. St. 5 → 0분
6. St. 2, 4 → 10분 유지 확인
7. ◄ ► 동시에 3초 → SAVE

| 스테이션 | 변경 전 | 변경 후 |
|---------|---------|---------|
| St. 1 | 10분 | **0분** ✅ |
| St. 2 | 10분 | 10분 유지 |
| St. 3 | 10분 | **0분** ✅ |
| St. 4 | 10분 | 10분 유지 |
| St. 5 | 10분 | **0분** ✅ |
| St. 6 | 10분 | **0분** (→ Program B로 이동) |
| St. 7 | 10분 | **0분** (→ Program B로 이동) |
| St. 8 | 10분 | **0분** (→ Program B로 이동) |

**실습 결과**: (실습 후 기록)

---

#### Program A Water Days 변경

**목표**: 3-day cycle → 월/수/금

**조작법**:
1. 다이얼 → WATER DAYS
2. Program A 선택
3. Specific Days 선택
4. 월(Mon) / 수(Wed) / 금(Fri) 선택
5. SAVE

**실습 결과**: (실습 후 기록)

---

#### Program B 신규 설정 — 뒷마당 잔디

**목표**: St. 6, 7, 8 / Start Time 6:40 AM / 월/수/금 / 10분

**조작법**:
1. 다이얼 → SET WATERING TIMES
2. Program B 선택 (◄ ► 버튼으로 전환)
3. Start Time → 6:40 AM 설정
4. St. 6 → 10분
5. St. 7 → 10분
6. St. 8 → 10분
7. WATER DAYS → 월/수/금
8. SAVE

**실습 결과**: (실습 후 기록)

---

#### Program C 신규 설정 — Bark/화단

**목표**: St. 1, 3, 5 / Start Time 7:30 AM / 화/목 / 20분

**조작법**:
1. 다이얼 → SET WATERING TIMES
2. Program C 선택
3. Start Time → 7:30 AM
4. St. 1 → 20분
5. St. 3 → 20분
6. St. 5 → 20분
7. WATER DAYS → 화/목
8. SAVE

**실습 결과**: (실습 후 기록)

---

#### 다이얼 → AUTO 전환

모든 설정 완료 후:
- 다이얼을 AUTO 위치로 전환
- 이제부터 스케줄에 따라 자동 운영

**실습 결과**: (실습 후 기록)

---

## 최종 설정 요약 (목표)

| Program | 대상 | 스테이션 | Start Time | Water Days | Run Time |
|---------|------|---------|------------|-----------|---------|
| A | 앞마당 잔디 | 2, 4 | 6:00 AM | 월/수/금 | 10분 |
| B | 뒷마당 잔디 | 6, 7, 8 | 6:40 AM | 월/수/금 | 10분 |
| C | Bark/화단 | 1, 3, 5 | 7:30 AM | 화/목 | 20분 |

---

## 💡 Daily Retrospective

### What went well
- Program A / B / C 설정을 컨트롤러 앞에서 직접 완료 — ESP-ME3 조작법 완전 습득
- AUTO 전환 시점에 대해 날씨 데이터 기반으로 합리적 판단 (서두르지 않기로 결정)
- Scotts Halts 살포 후 워터링 타이밍이 정확했음 (Pre-emergent 활성화 완료)

### Insights
- ESP-ME3 Start Time은 **15분 단위**로만 설정 가능 (6:40 → 6:45 AM으로 설정)
- Water Days 설정 시 Specific Days + 3-day Cycle 화면이 함께 나오는데, Specific Days가 우선 적용됨
- **비료 살포 후 건조 주의**: Scotts Halts 비료 성분이 토양에 있으므로 수분 부족 시 Fertilizer Burn 위험

### AUTO 전환 결정 (의도적 연기)

**결정**: 다이얼은 OFF 유지, **5월 초에 AUTO 전환**

**근거**:
- 4월 PNW는 자연 강수로 충분 (불필요한 관수 방지)
- 그저께까지 비 → 토양 수분 충분
- 4월 12일(토) 비 예보 있음

### 4월 워터링 계획 (수동 대응)

| 날짜 | 행동 |
|------|------|
| 4/8~9 (수) | 토양 체크: 손가락 2~3cm 꽂아서 건조하면 Manual Run |
| 4/12 (토) | 비 예보 — 자연 관개 |
| 5월 초 | 다이얼 → **AUTO** 전환 + Seasonal Adjust 80%로 조정 |

**토양 체크 방법**: 잔디에 손가락 2~3cm 꽂아서 건조하면 Manual Run 1회 (10분 × 필요 구역)

### Next action
- [ ] **4/8~9 (수)**: 토양 수분 체크 → 건조 시 Manual Run
- [ ] **5월 초**: 다이얼 → AUTO 전환
- [ ] **5월 초**: Seasonal Adjust 80%로 조정
- [ ] **5월 중순~6월 초**: 2차 시비 — Scotts Turf Builder (순수 비료, Pre-emergent 없는 버전)
  - Scotts Halts 비료 효과는 6~8주 후 소진
  - ⚠️ Pre-emergent 포함 제품(Halts 등) 중복 사용 금지 — 일반 비료만 사용
  - Scotts Halts Pre-emergent는 4개월간 토양에 활성 유지 중
- [ ] Overseeding 가능 시기: 4개월 후 (8월 초 이후) — Pre-emergent 효과 종료 후
- [ ] M3 여름 관리 시작 (5월경)

---

## 📎 업데이트할 산출물

- `02-Sprinkler-Master/current-settings-audit.md` — Program B/C 설정 완료 후 업데이트
- `02-Sprinkler-Master/spring-schedule-2026.md` — 최종 스케줄 반영

---

**방법론**: VibeLearn AI
**다음 WorkLog**: M3 시작 또는 여름 관리 이슈 발생 시
