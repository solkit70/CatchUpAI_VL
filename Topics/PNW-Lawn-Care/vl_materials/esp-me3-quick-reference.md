# ESP-ME3 빠른 참조 치트시트

**출처**: Quick Reference Card + Special Features PDF
**정리일**: 2026-03-03

---

## 기본 5단계 프로그래밍 (Quick Reference)

```
1. 다이얼 → Date/Time     → 날짜, 시간 입력
2. 다이얼 → Start Times   → 프로그램 선택 → 시작 시간 입력 (1개만!)
3. 다이얼 → Run Times     → 각 스테이션 가동 시간 입력
4. 다이얼 → Water Days    → 물 주는 날 선택
5. 다이얼 → Auto          → 완료! (자동 모드)
```

---

## 프로그래밍 차트 (내 스프링클러 구성 기록용)

| 스테이션 | 이름/위치 | 프로그램 | Start Time | Run Time | Water Days |
|---------|---------|---------|-----------|---------|-----------|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |
| 6 | | | | | |
| 7 | | | | | |
| 8 | | | | | |
| 9 | | | | | |
| 10 | | | | | |
| 11 | | | | | |
| 12 | | | | | |

> M2 학습 후 실제 마당 스테이션 정보 채울 것

---

## 수동 관수 (Manual Watering)

| 방법 | 다이얼 위치 | 사용 상황 |
|------|-----------|---------|
| 단일 스테이션 | Manual Watering → 스테이션 번호 | 특정 구역 즉시 물 주기 |
| 모든 스테이션 테스트 | Manual Watering → Test All | 시스템 전체 점검 |
| 프로그램 실행 | Manual Watering → Program A/B/C/D | 특정 프로그램 즉시 실행 |
| 즉시 중지 | 어디서든 OFF 버튼 또는 Rain 버튼 | 긴급 중지 |

---

## ALERT 표시 의미

| 표시 | 의미 |
|------|------|
| ALERT (깜박) | 프로그래밍 오류 — 설정 확인 필요 |
| ALERT (고정) | 전기 오류 — 배선 또는 솔레노이드 점검 |
| FLOW 경보 | 유량 이상 — 파열 또는 막힘 |

---

## 특수 기능 (Special Features)

### 프로그램 저장 (Save Programming)

데이터 손실 방지를 위해 설정 완료 후 반드시 저장!

1. 다이얼을 **Date/Time**으로 돌리기
2. ◄▶ 버튼 동시에 3초 이상 누르기
3. 화면에 SAVED 표시 → 저장 완료

### 프로그램 복원 (Restore Programming)

실수로 설정을 망쳤을 때 저장된 설정으로 되돌리기

1. 다이얼을 **Start Times**으로 돌리기
2. ◄▶ 버튼 동시에 3초 이상 누르기
3. 화면에 RESTORED 표시 → 복원 완료

---

### 스테이션별 Master Valve 설정

특정 스테이션 사용 시에만 Master Valve 열기 (물 절약)

1. 다이얼을 **Run Times**으로 돌리기
2. 원하는 스테이션 선택
3. MV 옵션 ON/OFF 토글

---

### Rain Sensor Bypass (빗물 센서 우회)

센서가 비를 감지해 자동 관수 중단했을 때 강제 실행

1. 다이얼 위치 무관
2. **Rain 버튼** 길게 누르기
3. 화면에 BYPASS 표시 → 우회 활성화
4. 다시 누르면 우회 해제

**활용**: 센서 오작동, 조경 작업 중 테스트

---

### 공장 초기화 (Reset to Factory Defaults)

⚠️ **모든 설정 삭제** — 처음부터 다시 설정해야 함

1. 다이얼을 **Seasonal Adjust**으로 돌리기
2. ◄▶ 버튼 동시에 10초 이상 누르기
3. 화면에 **CLEARED** 표시 → 초기화 완료

**초기화 전에 반드시 설정 사진 촬영 또는 차트에 기록!**

---

### Flow Sensor Bypass (유량 센서 우회)

센서 교정 또는 점검 중 오경보 방지

1. 전용 Flow 버튼 또는 설정 메뉴에서 접근
2. BYPASS 활성화 → 유량 경보 무시

---

### Interstation Delay (스테이션 간 지연)

한 스테이션 끝나고 다음 스테이션 시작 전 대기 시간 추가

**활용**: 솔레노이드 워밍업, 물 압력 안정화

1. 다이얼을 **Run Times**으로 돌리기
2. DELAY 또는 SOAK 옵션 선택
3. 지연 시간 입력 (초 단위)

---

## 자주 쓰는 조합 (Tehaleh WA 봄 설정)

```
프로그램 A — 잔디 (이른 아침)
  Start Time: 5:00 AM (1개만!)
  Run Time: 각 구역 10-20분
  Water Days: Mon, Wed, Fri
  Seasonal Adjust: 70% (봄)

프로그램 B — 화단/드립 (잔디와 별도)
  Start Time: 6:30 AM
  Run Time: 각 드립 구역 20-30분
  Water Days: Tue, Thu
  Seasonal Adjust: 70%
```

---

**상세 내용**: esp-me3-complete-guide.md
**음성 제어**: alexa-smart-home-guide.md
