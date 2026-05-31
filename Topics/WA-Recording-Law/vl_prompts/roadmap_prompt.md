# VibeLearn AI Roadmap 생성 프롬프트

**버전**: 2.0
**Topic**: WA-Recording-Law
**생성일**: 2026-05-31
**방법론**: VibeLearn AI

---

## [1단계] Topic 정보 (topic_info.md에서 주입됨)

### 기본 정보

**Topic 이름**: `WA-Recording-Law`

**Topic 설명**:
```
미국 워싱턴 주의 녹화·녹음 관련 법률(RCW 9.73) 학습.
PKM, 콘텐츠 제작, 업무 미팅, 학교 강의 등 실생활 시나리오에서
무엇이 합법이고 불법인지 파악하여 실무 가이드라인 도출.
```

**학습 목적**:
```
- Limitless AI Recorder 등 ambient recording 도구를 안전하게 사용하기 위한 법적 기준 이해
- 유튜브 촬영, 세미나 녹화 등 콘텐츠 제작 활동의 법적 허용 범위 파악
- 업무 미팅, 온라인 미팅 녹음 시 준수해야 할 절차 습득
- PKM 활동에서 녹음·녹화를 안전하게 활용하는 실무 가이드라인 작성
```

**예상 학습 기간**: `1일 (집중 학습, 총 2~2.5시간)`

---

### 환경 및 사전 지식

**운영 체제**: `Windows 11`

**주요 도구 및 기술 스택**:
```
- Claude Code (VS Code)
- Web Browser (법률 조항 조회)
```

**사전 지식**:
```
필수:
- 없음 (법률 입문 수준)

권장:
- 미국 법률 체계 기본 개념 (연방법 vs. 주법)
```

---

### 산출물 및 참조

**학습 목표** (달성하고 싶은 것):
```
- [ ] 워싱턴 주 All-Party Consent 원칙을 연방법(One-Party)과 비교해 설명할 수 있다
- [ ] RCW 9.73.030의 핵심 금지 조항과 예외 조항을 나열할 수 있다
- [ ] 공공장소 vs. 사적 공간에서의 녹음 허용 기준을 판단할 수 있다
- [ ] Limitless AI Recorder 사용 시 안전한 운용 방식을 설계할 수 있다
- [ ] 온라인 미팅, 세미나, 학교 강의 등 6가지 시나리오별 합법/불법 판단이 가능하다
- [ ] 위반 시 형사·민사 처벌 수준을 설명할 수 있다
- [ ] 녹음 전 고지(constructive consent) 방법을 실무에 적용할 수 있다
```

**참조 자료**:
```
- RCFP Washington Recording Guide: https://www.rcfp.org/reporters-recording-guide/washington/
- RCW 9.73 전체: https://app.leg.wa.gov/RCW/default.aspx?cite=9.73
- RCW 9.73.030 (핵심 조항): https://app.leg.wa.gov/RCW/default.aspx?cite=9.73.030
- RCW 9.73.060 (민사 처벌): https://app.leg.wa.gov/RCW/default.aspx?cite=9.73.060
- RCW 9.73.080 (형사 처벌): https://app.leg.wa.gov/RCW/default.aspx?cite=9.73.080
```

**vl_materials/ 폴더**:
```
- WA-Recording-Law-Study.md (사전 학습 문서 — 법률 조항 조사 결과 전문)
- reference-links.md (참고 링크 모음)
```

---

## [2단계] AI에게 요청할 작업

위에 주입된 Topic 정보를 바탕으로 **VibeLearn AI 방법론**에 맞는 학습 로드맵을 생성해주세요.

---

### 🔍 STEP 1: 학습 기간 적정성 검토

**사용자 입력 기간**: 1일 (집중 학습, 약 2~2.5시간)
**Topic 복잡도**: 간단 — 법률 개념 이해 + 시나리오 적용 (프로그래밍 없음, 특정 법률 하나에 집중)
**권장 기간**: 2~3시간 집중 세션

**분석 결과**: ✅ **적정함**
- 특정 법률 하나를 실생활에 적용하는 집중 학습
- 기술 스택 설치/설정 없음, 순수 법률 이해 + 판단 실습
- 5개 모듈 구성으로 적정

→ **기간 그대로 진행**

---

### 🗺️ STEP 2: 로드맵 생성 요구사항

**1일(2~2.5시간) 기준 → 5개 모듈 구성**

#### 특수 고려사항 (이 Topic 전용)

- **기존 사전 학습 문서 활용**: `vl_materials/WA-Recording-Law-Study.md`에 법률 조항 조사 결과가 이미 있음. 이를 활용해 실습 중심으로 구성
- **실습 = 시나리오 판단**: 코드 작성이 아닌 "이 상황에서 녹음해도 되는가?" 판단 실습
- **최종 산출물**: 나만의 1페이지 실무 가이드라인 + 고지 문구 모음
- **산출물 폴더**: 개념 정리 MD + 판단 결과 MD 중심 (코드 파일 없음)

#### 모듈 구성 제안 (5개)
```
M1 — 법률 기초 (연방법 vs 워싱턴 주법)       ⭐    25분
M2 — RCW 9.73 핵심 조항 분석               ⭐⭐   30분
M3 — 공공장소 vs 사적 공간 기준             ⭐⭐   20분
M4 — 시나리오별 합법·불법 판단 실습 (핵심)  ⭐⭐⭐  45분
M5 — 실무 가이드라인 작성 (Capstone)        ⭐⭐   20분
```

---

## [3단계] 출력 형식

다음 VibeLearn AI 표준 형식으로 로드맵을 생성하고
`vl_roadmap/20260531_RoadMap_WA-Recording-Law.md`에 저장하세요.

각 모듈에는 다음 9가지 항목을 포함:
1. 모듈 기본 정보 (난이도, 예상 시간, 산출물 폴더)
2. 학습 목표 (3-5개, 체크리스트)
3. 주요 개념 (3-5개, 정의 + 설명)
4. 실습 과제 (2-3개, 단계별 + 검증 방법)
5. 산출물 폴더 구조
6. Definition of Done
7. Self-Assessment
8. 예상 시간 배분
9. 참조 자료

---

**생성자**: Claude Code with VibeLearn AI
**Template 버전**: 2.0
**방법론**: VibeLearn AI
