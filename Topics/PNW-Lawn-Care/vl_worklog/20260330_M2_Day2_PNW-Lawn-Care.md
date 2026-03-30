# WorkLog - 2026-03-30: 스프링클러 컨트롤러 점검 + 전 스테이션 가동 확인

**날짜**: 2026-03-30
**Topic**: PNW-Lawn-Care
**모듈**: M2 - Rain Bird ESP-ME3 마스터 (Day 2)
**학습 시간**: ~2시간

---

## 🎯 오늘의 목표

- [x] 집 오리엔테이션 영상/오디오 transcript에서 스프링클러 관련 내용 추출
- [x] ESP-ME3 컨트롤러 현재 설정 전체 읽기
- [x] 문제 설정 수정 (8PM Start Time, Seasonal Adjust, Run Times)
- [x] Manual Run으로 전 스테이션 정상 작동 확인
- [x] 스테이션별 커버 구역 완전 파악

---

## 📚 진행 내용

### 1. 오리엔테이션 영상 Transcript 분석

집 입주 당시 녹화된 영상/오디오 파일에서 스프링클러 관련 내용 추출.
관련 파일 5개를 `vl_materials/house-walkthrough/`에 복사 완료.

**핵심 발견 사항:**
- **야외 Green Box** (초록색 밸브 박스): 야드 내 2개 이상 존재 — 154th St 1 [03:05~03:51]
- **컨트롤러**: 입주 시부터 OFF 상태로 유지 중 — 154th St 7 / IMG_6130
- **Backflow 테스트**: 매년 County 의무 — Yard Works Inc. (253-177-8238)
- **Winterize 문서**: Megan에게 요청 가능

---

### 2. ESP-ME3 컨트롤러 현재 설정 읽기

| 항목 | 확인값 | 문제 여부 |
|------|--------|---------|
| 날짜/시간 | 정확 ✅ | — |
| Start Time 1 | 6:00 AM | ✅ 정상 |
| **Start Time 2** | **8:00 PM** | ❌ **즉시 수정 필요** |
| Start Time 3~6 | OFF | ✅ |
| Run Times (St. 1~8) | 2분 | ❌ 너무 짧음 |
| Water Days | 3-day cycle | 🔶 조정 권장 |
| **Seasonal Adjust** | **100%** | ❌ 봄에 높음 |
| Weather Sensor | SEN ON | ✅ 유지 |
| Flow Sensor | SEN OFF | ✅ 유지 (미설치) |
| Programs B/C/D | 모두 OFF | ✅ (재설정 예정) |

---

### 3. 설정 수정 완료

| 항목 | 변경 전 | 변경 후 |
|------|---------|---------|
| Start Time 2 | 8:00 PM | **OFF** ✅ |
| Run Times (St. 1~8) | 2분 | **10분** ✅ |
| Seasonal Adjust | 100% | **70%** ✅ |
| 설정 저장 | — | **SAVED** ✅ |

> **8PM 제거 이유**: 밤에 물을 주면 잔디가 밤새 젖어있어 PNW 기후에서 곰팡이병(Fungal Disease) 원인이 됨.
> **Seasonal Adjust 70%**: 3월 봄 초기 기준. 10분 Run Time × 70% = 실제 7분 관수.

---

### 4. Manual Run — 전 스테이션 작동 확인

**결과: 8개 스테이션 전체 정상 작동** ✅

| 스테이션 | 커버 구역 | 타입 | 권장 Program |
|---------|---------|------|------------|
| 1 | 앞마당 오른쪽 언덕 (Bark) | 화단/Bark | Program C |
| 2 | 앞마당 오른쪽 잔디 | 잔디 | Program A |
| 3 | 현관 앞 (Bark/화단) | 화단/Bark | Program C |
| 4 | 앞마당 왼쪽 잔디 | 잔디 | Program A |
| 5 | 앞마당 왼쪽 언덕 (Bark) | 화단/Bark | Program C |
| 6 | 뒷마당 왼쪽 | 잔디 | Program B |
| 7 | 뒷마당 오른쪽 | 잔디 | Program B |
| 8 | 뒷마당 중앙 | 잔디 | Program B |
| 9~22 | 미연결 (NoMod) | — | — |

---

### 5. 핵심 발견: 프로그램 재구성 필요

현재 잔디(St. 2, 4, 6, 7, 8)와 Bark/화단(St. 1, 3, 5)이 모두 Program A에 묶여있음.
잔디와 Bark는 **관수 빈도와 시간이 다르므로** 반드시 분리해야 함.

**권장 프로그램 구성:**

| Program | 구역 | 스테이션 | 요일 | Run Time | 이유 |
|---------|------|---------|------|---------|------|
| A | 앞마당 잔디 | 2, 4 | 월/수/금 | 10분 | 잔디: 짧고 자주 |
| B | 뒷마당 잔디 | 6, 7, 8 | 월/수/금 | 10분 | 잔디: 짧고 자주 |
| C | Bark/화단 | 1, 3, 5 | 화/목 | 20분 | Bark: 길게 덜 자주 |

---

## 💡 Daily Retrospective

### What went well
- 오리엔테이션 영상 transcript를 활용해 집 스프링클러 시스템 구조를 먼저 파악
- 컨트롤러 버튼(◄ ► − +) 실제 조작법 완전 습득
- 8PM Start Time이라는 심각한 설정 오류를 발견하고 즉시 수정
- Manual Run으로 8개 스테이션 전체 커버 구역 완전 파악 — 이 정보가 없으면 올바른 프로그램 설정 불가

### Insights
- **잔디 vs Bark 분리**가 생각보다 훨씬 중요. 같은 프로그램에 묶으면 한쪽이 과수 또는 과소관수됨
- ESP-ME3 버튼 조작: ▼▲ 없고 − + 사용. Start Time OFF는 + 버튼 16번(8PM 기준)
- Weather Sensor SEN ON: 수요일 비 예보 때 자동 skip 역할 → 이미 보호받고 있음

### Next action
- [ ] **내일 (3/31 화요일)**: Scotts Turf Builder Halts 살포 → Manual Run 15~20분 워터링
- [ ] **이번 주 중**: Program A에서 Bark 스테이션(1, 3, 5) 제거 → Program C 설정
- [ ] **이번 주 중**: Program B (뒷마당 잔디: St. 6, 7, 8) 설정
- [ ] **Water Days**: 3-day cycle → 월/수/금 변경
- [ ] **모든 설정 완료 후**: 다이얼 → AUTO 전환

---

## 📎 업데이트된 산출물

- `02-Sprinkler-Master/current-settings-audit.md` — 스테이션 매핑 + 현재/권장 설정 완성
- `02-Sprinkler-Master/spring-schedule-2026.md` — 실제 스테이션 기반 업데이트 예정
- `vl_materials/house-walkthrough/` — 오리엔테이션 transcript 5개 추가

---

**방법론**: VibeLearn AI
**다음 WorkLog**: Scotts 살포 + Program B/C 설정 완료 후
