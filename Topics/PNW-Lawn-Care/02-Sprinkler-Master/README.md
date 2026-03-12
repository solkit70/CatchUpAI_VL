# M2: Rain Bird ESP-ME3 마스터

**모듈**: M2 / 4
**상태**: 🔄 진행 중 (2026-03-11 시작)
**위치**: Tehaleh, WA
**총 학습 시간**: 예상 8h (야외 실습 포함)

---

## 이 모듈에서 배울 것

ESP-ME3 컨트롤러를 완전히 이해하고, 내 마당에 맞는 봄 스케줄을 직접 설정합니다.

### 핵심 교훈 1: Programs A/B는 동시에 돌리지 않는다
앞/뒤마당을 동시 실행하면 수압이 낮아져 커버리지가 떨어집니다.
A → B → C 순서로 시간차를 두어 순차 실행.

### 핵심 교훈 2: Start Time은 1개만
가장 흔한 실수: Start Time을 여러 개 설정 → 하루에 여러 번 물이 나옴.
프로그램당 Start Time은 반드시 1개만 유지.

### 핵심 교훈 3: Seasonal Adjust 하나로 계절 대응
각 스테이션 Run Time을 일일이 바꾸지 않아도 됩니다.
Seasonal Adjust % 하나로 전체 관수량 조정.

---

## 📚 학습 순서 (이 순서대로 읽으세요)

### ⚠️ Step 0. 시스템 첫 가동 — 이것부터 (처음 켜는 경우 필수)

> **해당 상황**: 입주 후 처음 사용하거나, 겨울 동안 OFF로 유지했다가 봄에 재가동하는 경우.
> 이 집은 2025년 10월 입주 후 겨울 내내 스프링클러 OFF → **2026년 3월이 첫 가동**.

0. [concepts/first-startup-guide.md](concepts/first-startup-guide.md) ⭐⭐
   - 오리엔테이션 영상에서 밸브 찾기, 메인 밸브 위치 및 천천히 여는 법
   - Backflow preventer 확인, 컨트롤러 전원 ON, 첫 수동 테스트 순서
   - **이 가이드를 완료한 후에 Step 1로 진행하세요**

> [outdoor-tasks-20260311.md](outdoor-tasks-20260311.md) **Task 0** 체크리스트도 함께 사용하세요.

---

### Step 1. 배경 지식 — 컨트롤러 전체 기능 파악

> 먼저 ESP-ME3의 모든 기능을 빠르게 훑어봅니다.

1. [../vl_materials/esp-me3-quick-reference.md](../vl_materials/esp-me3-quick-reference.md)
   - 기본 5단계 프로그래밍 흐름, 수동 관수 방법, ALERT 표시 의미
   - **⭐ 먼저 이것부터** — 1페이지 요약 치트시트

2. [../vl_materials/esp-me3-complete-guide.md](../vl_materials/esp-me3-complete-guide.md)
   - 기본/고급 프로그래밍 전체, Seasonal Adjust, 문제 해결 가이드
   - 필요할 때 참조하는 전체 레퍼런스

---

### Step 2. 전략 — 내 마당 맞춤 설정 계획

> 배경 지식을 바탕으로 내 마당에 맞는 프로그램 전략을 이해합니다.

3. [concepts/program-strategy.md](concepts/program-strategy.md)
   - Programs A/B/C/D 역할 분리, 봄 스케줄 설계 (시작 시간/요일/런타임)
   - 흔한 실수 & 해결책

4. [concepts/seasonal-adjust-guide.md](concepts/seasonal-adjust-guide.md)
   - 월별 권장 Seasonal Adjust % 표 (Tehaleh WA 기준)
   - 현재(3월) 권장값: **70%**, 조정 방법

5. [concepts/advanced-cycles-guide.md](concepts/advanced-cycles-guide.md)
   - Cycle+Soak 원리, 앞마당 경사 구역에 적용하는 방법
   - 설정값: 10분 × 3회 + Soak 15분

---

### Step 3. 야외 실습 — 현황 파악 + 스케줄 설정

> 실제 컨트롤러 앞에서, 그리고 마당을 직접 걸으며 실습합니다.

6. [outdoor-tasks-20260311.md](outdoor-tasks-20260311.md) ⭐
   - **날 밝으면 할 일 전체 목록** (Task 1~5)
   - Task 1: 잔디 면적 걸음 측정
   - Task 2: 컨트롤러 현재 설정 읽기 + 사진 촬영
   - Task 3: 모든 스테이션 수동 테스트
   - Task 4: 특이사항 사진 촬영
   - Task 5: 결과 AI에게 전달 → 봄 스케줄 계산

7. [current-settings-audit.md](current-settings-audit.md)
   - 야외 실습 중 읽은 현재 설정 기록 템플릿
   - ⏳ **야외 실습 후 채울 것**

---

### Step 4. 설정 완료 문서 (야외 실습 후 작성 예정)

> 실습 결과를 문서로 정리하고 최적 봄 스케줄을 확정합니다.

8. spring-schedule-2026.md *(작성 예정)*
   - 봄 스케줄 설정 전/후 비교, 실제 적용된 설정값

9. station-test-log.md *(작성 예정)*
   - 스테이션별 테스트 결과, 이상 발견 내용

---

### 참고. Alexa 음성 제어 연동

10. [../vl_materials/alexa-smart-home-guide.md](../vl_materials/alexa-smart-home-guide.md)
    - LNK WiFi 모듈 연결, Alexa skill 설정, 음성 명령 예시
    - 기본 스케줄 설정 완료 후 진행 권장

---

## 📊 진행 현황

| 단계 | 내용 | 상태 |
|------|------|------|
| **Step 0** | **시스템 첫 가동** (오리엔테이션 영상 → 밸브 개방 → 첫 테스트) | ⏳ 미수행 |
| Step 1 | 배경 지식 (quick-reference, complete-guide) | ✅ 완료 |
| Step 2 | 전략 문서 3개 (program, seasonal, cycles) | ✅ 완료 |
| Step 3 | 야외 실습 수행 | ⏳ Step 0 이후 |
| Step 3 | current-settings-audit 완성 | ⏳ 야외 후 |
| Step 4 | spring-schedule-2026 작성 + 실제 설정 | ⏳ 야외 후 |
| Step 4 | station-test-log 작성 | ⏳ 야외 후 |

---

## 봄 설정 목표값 (야외 실습 후 적용)

| 항목 | 설정값 |
|------|--------|
| Seasonal Adjust | **70%** |
| Program A Start Time | **5:00 AM** (1개만) |
| Program A Water Days | **월/수/금** |
| Program B Start Time | **5:30 AM** |
| Program C Start Time | **7:00 AM** |
| 앞마당 경사 구역 | **Multiple Start Times** 10분×3 (컨트롤러 단독) 또는 **Cycle+Soak** (App+LNK2 연결 시) |

---

**이전 모듈**: [M1: PNW 잔디 기초 + 봄 준비](../01-Spring-Basics/README.md)
**다음 모듈**: M3: 여름 관리 + 문제 진단 *(야외 실습 완료 후 시작)*
**방법론**: VibeLearn AI
