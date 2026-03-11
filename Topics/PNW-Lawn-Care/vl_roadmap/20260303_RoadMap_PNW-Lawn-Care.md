# PNW-Lawn-Care 학습 로드맵

**생성일**: 2026-03-03
**방법론**: VibeLearn AI
**버전**: 1.0

---

## 📚 학습 개요

### Topic 소개

태평양 북서부(PNW) 기후 환경에 맞는 잔디 관리와 Rain Bird ESP-ME3 스프링클러 마스터링.
위치: Tehaleh, WA (Pierce County). 면적: 약 0.3에이커 뒷마당. 학습자: 완전 초보자.

3월은 PNW에서 봄 준비를 시작하기에 **완벽한 타이밍**입니다. 이번 1주로 연간 잔디 관리의 기반을 구축합니다.

### 학습 목표

- [ ] PNW 계절별 잔디 관리 캘린더를 작성할 수 있다
- [ ] Rain Bird ESP-ME3의 모든 기능을 이해하고 직접 설정할 수 있다
- [ ] 잔디 문제(황변, 잡초, 불균일)를 진단하고 해결 방법을 적용할 수 있다
- [ ] 물 절약과 잔디 건강을 동시에 달성하는 스프링클러 스케줄을 설정할 수 있다
- [ ] 가을 월동 준비와 겨울 시스템 보호 절차를 수행할 수 있다

### 예상 학습 기간

1주 (2026-03-03 ~ 2026-03-09), 이번 주 전담

### 학습 환경

- OS: Windows 11
- 도구: Rain Bird ESP-ME3 컨트롤러 (실제 장비), VS Code, 스마트폰 카메라
- 위치: Tehaleh, WA — USDA Zone 8b, Cool-season 잔디
- 사전 지식: 없음 (완전 초보자)

---

## 🗺️ 전체 로드맵 구조

| 모듈 | 모듈명 | 난이도 | 예상 시간 | 산출물 폴더 |
|------|--------|--------|-----------|------------|
| M1 | PNW 잔디 기초 + 봄 준비 | ⭐ | 6h | 01-Spring-Basics/ |
| M2 | Rain Bird ESP-ME3 마스터 | ⭐⭐ | 8h | 02-Sprinkler-Master/ |
| M3 | 여름 관리 + 문제 진단 | ⭐⭐ | 6h | 03-Summer-Troubleshoot/ |
| M4 | 가을+겨울 + 연간 계획 (Capstone) | ⭐⭐⭐ | 4h | 04-Annual-Plan/ |

**총 예상 시간**: 24시간 (버퍼 포함 — 이번 주 충분히 완료 가능)

---

## 📖 모듈별 상세 계획

---

### M1 - PNW 잔디 기초 + 봄 준비

**난이도**: ⭐
**예상 시간**: 6h
**산출물 폴더**: `01-Spring-Basics/`
**권장 시작**: 2026-03-03 (오늘!)

#### 학습 목표

- [ ] PNW 기후 특성과 Cool-season 잔디의 생장 주기를 설명할 수 있다
- [ ] 3월에 해야 할 봄 준비 작업 목록을 작성하고 우선순위를 정할 수 있다
- [ ] 비료, 제초제, 잔디 씨앗의 종류와 선택 기준을 알 수 있다
- [ ] 현재 마당 잔디 상태를 사진과 함께 기록하고 평가할 수 있다

#### 주요 개념

1. **Cool-season Grass**: 켄터키 블루그래스, 퍼레니얼 라이그래스, 톨 페스큐 — PNW 표준 잔디. 봄(10-15°C)과 가을에 왕성히 성장, 여름(26°C+)에는 스트레스 상태.

2. **PNW 기후 리듬**: 10월-4월 비 많음(거의 자연 관개), 5-6월 전환기, 7-8월 건조 (스프링클러 의존). 3월은 봄 준비 최적기.

3. **봄 필수 작업 3가지**:
   - **Dethatching(탈기)**: 잔디 뿌리층 위 쌓인 건초층 제거. 두께 1/2인치(1.25cm) 초과 시 필요.
   - **Aerating(통기)**: 토양 다짐 완화, 뿌리 산소 공급. 봄 또는 가을에 연 1회.
   - **Overseeding(씨앗 보충)**: 얇아진 부분에 씨앗 추가 파종. 발아 온도: 10-15°C.

4. **비료 (Fertilizer) 기초**: N-P-K 수치 (질소-인-칼륨). 봄 첫 비료는 질소 높은 것 (예: 30-0-4) — 녹색 성장 촉진. Slow-release 타입 권장.

5. **잡초 예방**: Pre-emergent herbicide (발아 전 제초제) — 봄 토양 온도 10°C(50°F) 도달 전 살포 효과적.

#### 실습 과제

**실습 1: 마당 현황 조사 및 기록** ⭐
- **목적**: 학습 시작점을 기록하고 문제 지점을 파악
- **단계**:
  1. 스마트폰 카메라로 마당 전체 사진 4방향 촬영
  2. 문제 지점 클로즈업 촬영 (얇은 부분, 잡초, 황변 등)
  3. VS Code에서 `01-Spring-Basics/lawn-audit-20260303.md` 파일 생성
  4. 다음 항목 기록: 잔디 전반 밀도(1-10), 황변 지점, 잡초 종류, 경사 방향
  5. 사진 `01-Spring-Basics/photos/` 폴더에 저장
- **예상 시간**: 45분
- **검증**: 사진 4장 이상, audit 문서 완성

**실습 2: PNW 봄 작업 체크리스트 + 3월 캘린더 작성** ⭐⭐
- **목적**: 실제 내 마당에 맞는 봄 준비 계획 수립
- **단계**:
  1. WSU Extension 자료 읽기 (Spring lawn care PNW 검색)
  2. `01-Spring-Basics/spring-checklist-2026.md` 작성
  3. 다음 항목 포함: 언제(날짜/조건), 무엇(작업), 어떻게(방법/도구), 구매할 것(제품)
  4. 3월-4월 캘린더 형식으로 정리
  5. 내 마당 특이사항(경사, 0.3에이커, Zone 8b) 반영
- **예상 시간**: 90분
- **검증**: 날짜별 작업 계획표 완성, 구매 목록 포함

**실습 3: Cool-season 잔디 연간 생장 주기 다이어그램 작성** ⭐⭐
- **목적**: 연간 리듬을 이해하여 적시적소 관리 계획 수립
- **단계**:
  1. `01-Spring-Basics/concepts/annual-growth-cycle.md` 작성
  2. 월별 잔디 상태, 해야 할 작업, 스프링클러 필요 여부 표로 정리
  3. PNW 강수량 패턴과 연결
- **예상 시간**: 60분
- **검증**: 12개월 표 완성

#### 산출물

```
01-Spring-Basics/
├── README.md                          # 모듈 개요 및 핵심 학습 내용
├── lawn-audit-20260303.md             # 현재 마당 현황 조사 결과
├── spring-checklist-2026.md           # 봄 작업 체크리스트 + 캘린더
├── concepts/
│   ├── annual-growth-cycle.md         # 연간 생장 주기 다이어그램
│   ├── pnw-climate-lawn-guide.md      # PNW 기후 + 잔디 종류 개요
│   └── fertilizer-guide.md            # 비료 선택 가이드 (N-P-K)
├── photos/
│   └── (마당 현황 사진들)
└── guides/
    └── first-spring-shopping-list.md  # 첫 봄 준비 구매 목록
```

#### Definition of Done

- [ ] 마당 현황 사진 4장 이상 촬영 및 저장
- [ ] `lawn-audit-20260303.md` 완성 (현재 상태 평가 포함)
- [ ] `spring-checklist-2026.md` — 3월-4월 날짜별 작업 계획 완성
- [ ] `annual-growth-cycle.md` — 12개월 표 완성
- [ ] `concepts/pnw-climate-lawn-guide.md` 작성
- [ ] `README.md` 작성 (모듈 요약 + 핵심 교훈)
- [ ] WorkLog 작성 완료
- [ ] Daily Retrospective 작성

#### Self-Assessment

**개념 이해** (5분):
- [ ] Cool-season 잔디가 여름에 왜 스트레스를 받는지 설명 가능
- [ ] PNW에서 스프링클러가 필요한 달(월)을 말할 수 있다
- [ ] Dethatching이 필요한 상황을 판단 가능 (두께 기준)

**실무 활용** (5분):
- [ ] AI에게 "내 마당에 맞는 봄 비료 추천해줘" 라고 효과적으로 질문 가능
- [ ] 내 마당 현황 사진을 보고 문제 지점 3가지 이상 식별 가능

**문제 해결** (5분):
- [ ] 잔디 일부가 황변됐을 때 AI에게 진단 요청 방법 설명 가능

#### 예상 시간 배분

- 개념 학습 (PNW 기후, Cool-season 잔디): 60분 (17%)
- 실습 1: 마당 조사: 45분
- 실습 2: 봄 체크리스트 작성: 90분
- 실습 3: 생장 주기 다이어그램: 60분
- 개념 문서 작성: 60분
- 문서화 + WorkLog: 45분
- **합계**: 360분 = 6h (버퍼 포함)

#### 참조 자료

- [WSU Extension — Lawn Care in the Pacific Northwest](https://extension.wsu.edu): 검색어 "spring lawn care Washington"
- [Rain Bird ESP-ME3 공식](https://www.rainbird.com/products/esp-me3-series-controllers): 이후 M2에서 심화 학습
- [PNW Pest Management Handbook](https://pnwhandbooks.org): 잔디 잡초/병해 진단

---

### M2 - Rain Bird ESP-ME3 마스터

**난이도**: ⭐⭐
**예상 시간**: 8h
**산출물 폴더**: `02-Sprinkler-Master/`
**권장 시작**: 2026-03-04

#### 학습 목표

- [ ] ESP-ME3 컨트롤러의 모든 다이얼 위치와 기능을 설명할 수 있다
- [ ] Programs A/B/C/D를 목적에 맞게 분리하여 설정할 수 있다
- [ ] Seasonal Adjust를 계절에 맞게 조정할 수 있다 (5~200%)
- [ ] Advanced Cycles 기능으로 경사지 유출을 방지할 수 있다
- [ ] LNK WiFi 모듈 연결 방법을 알고 스마트 기기와 연동할 수 있다

#### 주요 개념

1. **프로그램 분리 전략 (A/B/C/D)**:
   - Program A: 잔디 (잦은 관수, 짧은 시간)
   - Program B: 관목/화단 (드문 관수, 긴 시간)
   - Program C: 특수 구역 (필요 시)
   - Program D: 보조 / 수동 테스트용

2. **Seasonal Adjust**: 기준(100%) 대비 % 조정. 봄 100%, 여름 130-150%, 가을 60-80%, 겨울 OFF. 전체 프로그램에 일괄 적용.

3. **Advanced Cycles (사이클 분할)**: 1회 긴 관수 → N회 짧은 관수로 분할. 예: 20분 → 4×5분 (10분 침투 후 재관수). 경사지 유출 방지 핵심.

4. **Start Times vs. Run Times**: Start Time = 관수 시작 시각 (프로그램당 최대 6개 설정 가능). Run Time = 각 스테이션별 관수 시간 (1-240분).

5. **수동 테스트 모드**: Manual Watering 다이얼 위치 — 모든 스테이션을 순서대로 테스트. 설치 후 커버리지 확인에 필수.

#### 실습 과제

**실습 1: 컨트롤러 완전 매핑 — 현재 설정 읽기** ⭐
- **목적**: 현재 시스템 상태를 정확히 파악하고 문서화
- **단계**:
  1. `C:\AI_study\2026\Materials\PNW-lawn-care\Sprinkler_Rain-Bird\` 폴더의 사진 자료 모두 검토
  2. 컨트롤러 앞에서 각 다이얼 위치별 기능 확인
  3. 현재 설정 읽기: Program A/B/C/D의 Run Times, Water Days, Start Times
  4. `02-Sprinkler-Master/current-settings-audit.md`에 기록
  5. 스테이션 1-22 런타임 표로 정리 (Programming Chart 사진 참조)
- **예상 시간**: 90분
- **검증**: 현재 설정 완전 문서화, 스테이션별 런타임 표 완성

**실습 2: 봄 스케줄 최적 설정** ⭐⭐
- **목적**: 현재(3월)에 맞는 스프링클러 스케줄을 실제로 설정
- **단계**:
  1. 봄 PNW 잔디 물 요구량 계산: 주당 약 0.5-0.75인치 (3월)
  2. 현재 스테이션 런타임이 적절한지 평가 (Precipitation Rate 고려)
  3. Water Days 설정: 비 있는 날 고려 (3월은 주 2-3회)
  4. Seasonal Adjust를 100%로 설정 (봄 기준)
  5. Advanced Cycles 설정: 경사진 구역에 2-cycle 적용
  6. 실제 컨트롤러에서 설정 변경 후 사진 촬영
  7. `02-Sprinkler-Master/spring-schedule-2026.md` 작성
- **예상 시간**: 120분
- **검증**: 실제 설정 변경 완료, 설정 전/후 사진 촬영, 문서 완성

**실습 3: Manual Test로 모든 스테이션 점검** ⭐⭐
- **목적**: 시스템 정상 동작 확인 및 커버리지 파악
- **단계**:
  1. 날씨 좋은 날 오전에 진행 (스프링클러 작동 확인 가능)
  2. Manual Watering 모드로 스테이션 1부터 순서대로 테스트
  3. 각 스테이션 동작 확인: 올바른 위치, 누수, 커버리지
  4. 문제 스테이션 기록: `02-Sprinkler-Master/station-test-log.md`
  5. 마당에 안 닿는 구역 또는 중복 구역 식별
- **예상 시간**: 90분 (야외 실습)
- **검증**: 모든 스테이션 테스트 완료, 문제 목록 작성

#### 산출물

```
02-Sprinkler-Master/
├── README.md                          # 모듈 개요 + ESP-ME3 핵심 기능 요약
├── current-settings-audit.md          # 현재 설정 완전 문서화
├── spring-schedule-2026.md            # 봄 스케줄 설정 (변경 전/후 비교)
├── station-test-log.md                # 수동 테스트 결과 (문제 스테이션 포함)
├── concepts/
│   ├── esp-me3-complete-guide.md      # 컨트롤러 완전 가이드 (다이얼별 설명)
│   ├── program-strategy.md            # A/B/C/D 프로그램 분리 전략
│   ├── seasonal-adjust-guide.md       # 월별 Seasonal Adjust 권장값
│   └── advanced-cycles-guide.md       # Advanced Cycles 설정 방법 + 언제 쓰는가
├── cheatsheet/
│   └── esp-me3-quick-reference.md     # 빠른 참조 치트시트 (1페이지)
└── photos/
    └── (설정 화면 사진들)
```

#### Definition of Done

- [ ] 현재 설정 완전 문서화 (스테이션 1-22 런타임, 모든 프로그램)
- [ ] 봄 스케줄 설정 완료 (Seasonal Adjust, Water Days, Run Times)
- [ ] Advanced Cycles 경사지 구역에 적용
- [ ] 수동 테스트로 모든 스테이션 점검 완료
- [ ] `esp-me3-quick-reference.md` 치트시트 완성
- [ ] `concepts/seasonal-adjust-guide.md` (12개월 권장값 포함) 작성
- [ ] README.md 작성
- [ ] WorkLog 작성 완료

#### Self-Assessment

**개념 이해** (5분):
- [ ] ESP-ME3 다이얼 7-8개 위치와 기능을 설명 가능
- [ ] Seasonal Adjust를 여름 기준으로 몇 %로 설정해야 하는지 판단 가능

**실무 활용** (5분):
- [ ] 혼자서 Program A의 Water Days를 변경할 수 있다
- [ ] 스프링클러가 작동 안 할 때 첫 번째 확인 사항을 말할 수 있다

**문제 해결** (5분):
- [ ] 특정 스테이션에서 물이 안 나올 때 트러블슈팅 순서를 설명 가능

#### 예상 시간 배분

- 개념 학습 (컨트롤러 이해, 공식 문서): 90분 (19%)
- 실습 1: 설정 읽기 및 문서화: 90분
- 실습 2: 봄 스케줄 설정: 120분
- 실습 3: 수동 테스트 (야외): 90분
- 개념 문서 작성: 60분
- 문서화 + WorkLog: 30분
- **합계**: 480분 = 8h (버퍼 포함)

#### 참조 자료

- [Rain Bird ESP-ME3 공식 페이지](https://www.rainbird.com/products/esp-me3-series-controllers): 매뉴얼 다운로드
- [Rain Bird LNK WiFi Module 가이드](https://www.rainbird.com): 스마트 홈 연동
- 로컬 자료: `C:\AI_study\2026\Materials\PNW-lawn-care\Sprinkler_Rain-Bird\IMG_4408.JPEG` (Quick Reference)
- 로컬 자료: `IMG_4409.JPEG`, `IMG_4410.JPEG` (Programming Charts)

---

### M3 - 여름 관리 + 문제 진단

**난이도**: ⭐⭐
**예상 시간**: 6h
**산출물 폴더**: `03-Summer-Troubleshoot/`
**권장 시작**: 2026-03-06

#### 학습 목표

- [ ] PNW 여름 잔디의 물 요구량을 계산하고 스프링클러를 조정할 수 있다
- [ ] 일반적인 잔디 문제 5가지 이상을 시각적으로 진단할 수 있다
- [ ] 잡초 종류별 방제 방법을 알고 적용 시기를 선택할 수 있다
- [ ] 여름 Seasonal Adjust(130-150%)를 올바르게 설정할 수 있다

#### 주요 개념

1. **여름 관개 공식**: 주당 1~1.5인치 목표. 스프링클러 강수량(inches/hour)에 따라 런타임 계산. 일반 회전 헤드: 약 0.5인치/시간.

2. **잔디 스트레스 신호**: 발자국이 남음 → 수분 부족. 회녹색 변색 → 심각한 건조. 오전 이슬 없음 → 관수 필요.

3. **Dormancy vs. Death**: 여름 고온 건조 시 잔디가 갈색으로 변함 = Dormancy(휴면), 죽은 것 아님. 관수 재개 시 2-4주 내 회복.

4. **일반 잔디 문제 진단**:
   - 황변 원형 패치 → 잔디 곰팡이 (Brown Patch, Dollar Spot)
   - 불규칙 갈색 줄무늬 → 커버리지 불균일 (스테이션 문제)
   - 빠른 잡초 번식 → 잔디 밀도 부족 (Overseeding 필요)
   - 뭉뚱그린 이탄층 → Thatch 과다 (Dethatching 필요)

5. **관개 타이밍**: 새벽 4-8시 관수 = 최적 (증발 최소화, 곰팡이 예방). 저녁 관수 = 곰팡이 위험 증가.

#### 실습 과제

**실습 1: 여름 스케줄 시뮬레이션 문서 작성** ⭐⭐
- **목적**: 7-8월 최고 수요 시 설정 방법을 미리 계획
- **단계**:
  1. 현재 봄 스케줄 기준으로 여름 조정 계획
  2. Seasonal Adjust: 3월(100%) → 7월(140%) → 8월(150%) 단계적 증가 계획
  3. Water Days: 여름에는 주 4-5회 또는 격일 필요
  4. `03-Summer-Troubleshoot/summer-schedule-plan.md` 작성
  5. 월별 설정 변경 일정표 포함
- **예상 시간**: 60분
- **검증**: 7-8월 설정 계획 문서 완성

**실습 2: 잔디 문제 진단 가이드 작성** ⭐⭐
- **목적**: 시각적 증상으로 문제를 진단하는 기준 수립
- **단계**:
  1. 일반적인 PNW 잔디 문제 10가지 조사 (증상/원인/해결책)
  2. `03-Summer-Troubleshoot/concepts/lawn-problem-diagnosis.md` 작성
  3. 표 형식: 증상 | 예상 원인 | 진단 방법 | 해결책 | 시기
  4. 사진 예시는 웹에서 참조 (URL 링크)
  5. 내 마당에서 실제 관찰한 문제 기록 (M1 audit 결과 참조)
- **예상 시간**: 90분
- **검증**: 10가지 이상 문제 진단 가이드 완성

**실습 3: 잡초 관리 계획 수립** ⭐
- **목적**: PNW 주요 잡초 파악 및 연간 방제 계획 작성
- **단계**:
  1. PNW에서 가장 흔한 잔디 잡초 파악 (Dandelion, Clover, Creeping Bentgrass 등)
  2. Pre-emergent vs. Post-emergent 제초제 차이 이해
  3. 내 마당 현황(M1 audit)의 잡초와 매칭
  4. `03-Summer-Troubleshoot/weed-control-plan.md` 작성
- **예상 시간**: 60분
- **검증**: 잡초 목록 + 방제 계획 완성

#### 산출물

```
03-Summer-Troubleshoot/
├── README.md                          # 모듈 개요
├── summer-schedule-plan.md            # 여름 스케줄 계획 (월별 Seasonal Adjust)
├── weed-control-plan.md               # 잡초 관리 연간 계획
├── concepts/
│   ├── lawn-problem-diagnosis.md      # 잔디 문제 진단 가이드 (10가지+)
│   ├── summer-watering-formula.md     # 여름 관개 공식 및 계산법
│   └── dormancy-vs-death.md           # 잔디 휴면 vs. 고사 구별법
└── troubleshooting/
    └── quick-diagnosis-checklist.md   # 빠른 문제 진단 체크리스트
```

#### Definition of Done

- [ ] `summer-schedule-plan.md` — 월별 Seasonal Adjust 계획 완성
- [ ] `lawn-problem-diagnosis.md` — 10가지 이상 문제 진단 가이드 완성
- [ ] `weed-control-plan.md` — 연간 잡초 방제 계획 완성
- [ ] `summer-watering-formula.md` 작성
- [ ] `quick-diagnosis-checklist.md` 작성
- [ ] README.md 작성
- [ ] WorkLog 작성 완료

#### Self-Assessment

**개념 이해** (5분):
- [ ] PNW 여름에 주당 몇 인치 관수가 필요한지 말할 수 있다
- [ ] 관수를 새벽에 해야 하는 이유를 설명 가능

**실무 활용** (5분):
- [ ] 마당 사진을 보고 Brown Patch와 건조 스트레스를 구별 가능
- [ ] 잡초 사진을 AI에게 보내 진단 요청 가능

#### 예상 시간 배분

- 개념 학습: 60분 (17%)
- 실습 1: 여름 스케줄 계획: 60분
- 실습 2: 문제 진단 가이드: 90분
- 실습 3: 잡초 관리 계획: 60분
- 문서화 + WorkLog: 90분
- **합계**: 360분 = 6h

#### 참조 자료

- [WSU Extension Pest Management — Lawn Weeds](https://pnwhandbooks.org): PNW 잡초 목록
- [OSU Extension — Lawn Problems](https://extension.oregonstate.edu): 문제 진단 가이드
- [Rain Bird Seasonal Adjust 가이드](https://www.rainbird.com): Seasonal Adjust 최적화

---

### M4 - 가을+겨울 + 연간 계획 (Capstone)

**난이도**: ⭐⭐⭐
**예상 시간**: 4h
**산출물 폴더**: `04-Annual-Plan/`
**권장 시작**: 2026-03-08

#### 학습 목표

- [ ] 가을 잔디 관리 핵심 작업(Overseeding, 비료, 탈기)을 계획할 수 있다
- [ ] 겨울 전 스프링클러 Winterizing 절차를 이해하고 수행 시기를 알 수 있다
- [ ] 12개월 연간 잔디 관리 캘린더를 완성할 수 있다 (나만의 교과서)
- [ ] Tehaleh, WA 특성에 맞는 맞춤형 관리 가이드를 작성할 수 있다

#### 주요 개념

1. **가을 핵심 작업**: 9-10월은 Cool-season 잔디 두 번째 황금기. Overseeding 최적 시기(토양 20°C). 가을 비료는 칼륨 높은 것 (0-0-20) — 뿌리 강화.

2. **Winterizing (스프링클러 겨울 준비)**:
   - **Blow Out 방법**: 컴프레서로 공기를 밀어 배관 내 물 완전 제거
   - **PNW 시기**: 11월 초 ~ 첫 서리 전
   - Tehaleh, WA 평균 첫 서리: 11월 중순
   - 전문가 서비스 or DIY (컴프레서 렌탈)

3. **ESP-ME3 겨울 설정**: Seasonal Adjust 0% 설정으로 완전 OFF (또는 컨트롤러 자체 OFF). LNK WiFi는 실내 유지.

4. **봄 재가동 (Spring Startup)**:
   - 백플로우 방지기 밸브 열기
   - 한 스테이션씩 순차 가동 (급격한 수압 방지)
   - Manual Test로 겨울 피해 확인
   - Seasonal Adjust를 100%로 설정

5. **연간 비용 예산**: 비료, 씨앗, 제초제, 전문가 서비스 등 연간 비용 추정.

#### 실습 과제

**실습 1: Winterizing 체크리스트 작성** ⭐⭐
- **목적**: 겨울 준비를 실수 없이 수행하기 위한 상세 절차 문서화
- **단계**:
  1. Rain Bird ESP-ME3 Winterizing 공식 절차 조사
  2. Blow Out 방법 상세 단계 문서화
  3. Tehaleh 지역 서리 날짜 조사 → 권장 Winterizing 날짜 결정
  4. `04-Annual-Plan/winterizing-checklist.md` 작성
  5. 봄 재가동 체크리스트도 포함
- **예상 시간**: 60분
- **검증**: Winterizing + Spring Startup 체크리스트 완성

**실습 2: 12개월 연간 관리 캘린더 완성 (Capstone 핵심)** ⭐⭐⭐
- **목적**: 이 Topic의 최종 산출물 — 내 마당 맞춤형 완전 가이드
- **단계**:
  1. M1-M3에서 배운 모든 내용을 종합
  2. `04-Annual-Plan/annual-lawn-calendar-tehaleh.md` 작성
  3. 형식: 월별 → 잔디 상태 / 스프링클러 Seasonal Adjust / 주요 작업 / 비료 / 주의사항
  4. Tehaleh, WA Zone 8b 특성 반영
  5. 3월부터 시작하여 12개월 완성
  6. 구매 필요 제품 목록 포함 (연간)
- **예상 시간**: 90분
- **검증**: 12개월 완전 캘린더 완성 — "다른 Tehaleh 주민도 바로 사용 가능" 수준

**실습 3: Topic 완료 자기 평가 + 향후 계획** ⭐
- **목적**: 학습을 마무리하고 실제 적용 계획 수립
- **단계**:
  1. 모든 DoD 체크리스트 완료 확인
  2. `04-Annual-Plan/self-assessment-complete.md` 작성
  3. 올 봄(2026년 3월-5월) 즉시 실행할 액션 3가지 결정
  4. 여름과 가을에 확인할 사항 목록
  5. 내년 참조할 메모 작성
- **예상 시간**: 30분
- **검증**: 자기 평가 완성, 즉시 실행 액션 3개 확정

#### 산출물

```
04-Annual-Plan/
├── README.md                               # 모듈 개요
├── annual-lawn-calendar-tehaleh.md         # ★ Capstone: 12개월 연간 캘린더 (핵심!)
├── winterizing-checklist.md                # 겨울 준비 + 봄 재가동 체크리스트
├── self-assessment-complete.md             # Topic 완료 자기 평가
├── concepts/
│   ├── fall-lawn-care-guide.md             # 가을 관리 핵심 가이드
│   ├── winter-protection-guide.md          # 겨울 시스템 보호 방법
│   └── annual-budget-estimate.md           # 연간 잔디 관리 예산 추정
└── guides/
    └── spring-reactivation-steps.md        # 봄 시스템 재가동 절차
```

#### Definition of Done

- [ ] `annual-lawn-calendar-tehaleh.md` — 12개월 완전 캘린더 완성 (Capstone)
- [ ] `winterizing-checklist.md` — Blow Out 절차 포함 완성
- [ ] `fall-lawn-care-guide.md` 작성
- [ ] `spring-reactivation-steps.md` 작성
- [ ] `self-assessment-complete.md` 작성
- [ ] 즉시 실행 액션 3가지 확정
- [ ] README.md 작성
- [ ] Topic Final Retrospective 시작 준비
- [ ] WorkLog 작성 완료

#### Self-Assessment

**개념 이해** (5분):
- [ ] Winterizing을 언제(몇 월), 왜 해야 하는지 설명 가능
- [ ] 가을 Overseeding 최적 시기와 이유 설명 가능

**실무 활용** (5분):
- [ ] 연간 캘린더를 보고 지금(3월) 해야 할 일을 바로 파악 가능
- [ ] 이웃에게 PNW 잔디 관리 기본을 10분에 설명 가능

**문제 해결** (5분):
- [ ] 내년 봄 스프링클러 재가동 시 혼자서 수행 가능

#### 예상 시간 배분

- 개념 학습 (가을/겨울 관리): 30분 (13%)
- 실습 1: Winterizing 체크리스트: 60분
- 실습 2: 연간 캘린더 (Capstone): 90분
- 실습 3: 자기 평가: 30분
- 문서화 + WorkLog: 30분
- **합계**: 240분 = 4h

#### 참조 자료

- [Rain Bird — Winterizing Your Irrigation System](https://www.rainbird.com): Blow Out 방법
- [WSU Extension — Fall Lawn Care](https://extension.wsu.edu): 가을 작업 가이드
- [Tacoma/Pierce County 서리 날짜 데이터](https://www.weather.gov): 첫 서리 날짜

---

## 📝 WorkLog 작성 가이드

**파일명 규칙**: `vl_worklog/YYYYMMDD_MX_PNW-Lawn-Care.md`
- 예: `vl_worklog/20260303_M1_PNW-Lawn-Care.md`

**WorkLog 필수 섹션**:
1. 오늘의 학습 목표 (체크리스트)
2. 진행 내용 (실습별 상세 기록)
3. 문제 해결 로그
4. DoD 체크리스트 (모듈 완료 기준)
5. Daily Retrospective
6. 참조 및 산출물

---

## 🔍 Retrospective 가이드

### Daily Retrospective (매일, 5-10분)
WorkLog 내에 작성:
- What went well?
- What could be improved?
- Insights
- Tomorrow's focus

### Module Retrospective (모듈 완료 시, 15-20분)
`vl_worklog/YYYYMMDD_MX_Retrospective.md`

### Topic Retrospective (전체 완료 시, 30-60분)
`vl_worklog/20260309_PNW-Lawn-Care_Final_Retrospective.md`

---

## 📂 전체 폴더 구조

```
Topics/PNW-Lawn-Care/
├── topic_info.md
├── vl_prompts/
│   ├── roadmap_prompt.md
│   └── daily_learning_prompt.md
├── vl_roadmap/
│   └── 20260303_RoadMap_PNW-Lawn-Care.md   ← 이 파일
├── vl_worklog/
│   ├── 20260303_M1_PNW-Lawn-Care.md
│   ├── 20260304_M2_PNW-Lawn-Care.md
│   ├── 20260306_M3_PNW-Lawn-Care.md
│   ├── 20260308_M4_PNW-Lawn-Care.md
│   └── 20260309_PNW-Lawn-Care_Final_Retrospective.md
├── vl_materials/
│   └── (스프링클러 요약, 진단 가이드 등)
├── 01-Spring-Basics/
├── 02-Sprinkler-Master/
├── 03-Summer-Troubleshoot/
└── 04-Annual-Plan/
```

---

## 📊 학습 진행 상황 추적

| 모듈 | 시작일 | 종료일 | 상태 | DoD 달성률 | 비고 |
|------|--------|--------|------|-----------|------|
| M1 | 2026-03-03 | 2026-03-11 | ✅ | 100% | 잔디 면적 측정 보류 (낮에 진행 예정) |
| M2 | 2026-03-11 | | 🔄 | 0% | 스프링클러 직접 조작 포함 |
| M3 | 2026-03-06 | | ⏳ | 0% | 여름 대비 사전 계획 |
| M4 | 2026-03-08 | | ⏳ | 0% | Capstone: 연간 캘린더 |

**범례**: ⏳ 대기 | 🔄 진행 중 | ✅ 완료

---

## 🎯 성공 기준

전체 Topic 완료 기준:
- [ ] 모든 모듈 완료 (DoD 100%)
- [ ] 최소 4개 산출물 폴더 생성
- [ ] `annual-lawn-calendar-tehaleh.md` Capstone 완성
- [ ] Topic Final Retrospective 작성
- [ ] 즉시 실행 액션 3가지 실천 시작

---

**생성자**: Claude with VibeLearn AI
**Roadmap 버전**: 1.0
**방법론**: VibeLearn AI 2.0
**생성일**: 2026-03-03
