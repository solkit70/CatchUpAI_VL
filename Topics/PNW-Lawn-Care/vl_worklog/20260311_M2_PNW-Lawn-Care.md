# WorkLog - M2: Rain Bird ESP-ME3 마스터

**날짜**: 2026-03-11
**Topic**: PNW-Lawn-Care
**모듈**: M2 - Rain Bird ESP-ME3 마스터
**학습 시간**: 시작 (새벽) - 진행 중

---

## 🎯 오늘의 학습 목표

- [x] Programs A/B/C/D 전략 이해 → `concepts/program-strategy.md`
- [x] Seasonal Adjust 계절별 가이드 → `concepts/seasonal-adjust-guide.md`
- [x] Advanced Cycles/Cycle+Soak 이해 → `concepts/advanced-cycles-guide.md` *(2026-03-12 수정: Cycle+Soak은 App+LNK2 전용임을 확인)*
- [x] 야외 실습 가이드 작성 → `outdoor-tasks-20260311.md`
- [x] 현재 설정 감사 템플릿 → `current-settings-audit.md`
- [x] **[2026-03-12 추가] 첫 가동 가이드** → `concepts/first-startup-guide.md`
- [ ] 야외 실습 수행 → **⚠️ Task 0(첫 가동)부터 수행 필수**
  - [ ] **Task 0**: 오리엔테이션 영상 확인 → 메인 밸브 개방 → 컨트롤러 ON → 스테이션 1 테스트
  - [ ] 잔디 면적 걸음 측정
  - [ ] 컨트롤러 현재 설정 읽기
  - [ ] 모든 스테이션 수동 테스트
- [ ] `spring-schedule-2026.md` 작성 → 야외 후
- [ ] `station-test-log.md` 작성 → 야외 후

---

## 📚 진행 내용 (새벽 세션)

### 1. M2 개념 학습 + 문서화

**시간**: 새벽

**학습 내용**:

#### Programs A/B/C/D 전략
- A = 앞마당 잔디 (5:00 AM), B = 뒷마당 잔디 (5:30 AM) 순차 실행
- A/B 동시 실행 시 수압 저하 → 시간차 배분 필수
- C = 화단/드립 (7:00 AM, 화/목), D = 예비

#### Seasonal Adjust
- 현재(3월) 권장: **70%**
- 여름 피크(7-8월): 130-160%
- 겨울: 0% (OFF)
- 조정법: 다이얼 → Seasonal Adjust → ▲▼ 5% 단위

#### Advanced Cycles
- 앞마당 경사에 적용: 10분 × 3회 + Soak 15분 = 총 60분
- 신축 토양 다짐 해소에도 효과적

**결과**:
- `concepts/program-strategy.md` ✅
- `concepts/seasonal-adjust-guide.md` ✅
- `concepts/advanced-cycles-guide.md` ✅

### 2. 야외 실습 준비 문서

- `outdoor-tasks-20260311.md` ✅ — 5개 Task 체크리스트
- `current-settings-audit.md` ✅ — 야외 실습 후 채울 템플릿
- `README.md` ✅ — 모듈 현황 정리

---

## 💡 중간 Retrospective (새벽 세션)

### What went well
- 실내에서 할 수 있는 개념 학습 + 문서화 완료
- 야외 실습 가이드를 상세히 작성 → 혼자서도 수행 가능
- M1의 잔디 상태 분석과 연결하여 맞춤 설정값 도출

### Insights
- **Start Time 1개 규칙**: 가장 흔한 실수 예방 — 이것만 기억해도 절반은 성공
- **A→B 순차 실행**: 수압 분산 = 커버리지 품질 유지
- **Cycle+Soak**: 컨트롤러 자체에는 없고 Rain Bird App + LNK2 WiFi 모듈 필요 (중요 수정)
- **⚠️ [2026-03-12 추가] 첫 가동 컨텍스트**: 2025년 10월 입주, 겨울 5-6개월 동안 스프링클러 OFF 상태 유지. 3월이 이 집에서 첫 가동. 집 오리엔테이션 영상에 밸브 위치 정보 있음 — 야외 실습 전에 반드시 영상 먼저 확인!

### 야외 실습 후 할 일
- [ ] `current-settings-audit.md` 완성
- [ ] `spring-schedule-2026.md` 작성 + 실제 설정 변경
- [ ] `station-test-log.md` 작성
- [ ] M2 DoD 최종 확인

---

## 📎 현재까지 산출물

- `02-Sprinkler-Master/README.md` *(2026-03-12 Step 0 추가)*
- `02-Sprinkler-Master/outdoor-tasks-20260311.md` *(2026-03-12 Task 0 첫 가동 추가)*
- `02-Sprinkler-Master/current-settings-audit.md` (템플릿)
- `02-Sprinkler-Master/concepts/program-strategy.md`
- `02-Sprinkler-Master/concepts/seasonal-adjust-guide.md`
- `02-Sprinkler-Master/concepts/advanced-cycles-guide.md` *(주의: Cycle+Soak은 App 전용임을 추가 확인 필요)*
- `02-Sprinkler-Master/concepts/first-startup-guide.md` ✅ **2026-03-12 신규 추가**

**방법론**: VibeLearn AI
