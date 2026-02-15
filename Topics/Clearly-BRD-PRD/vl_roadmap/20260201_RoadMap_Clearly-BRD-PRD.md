# Clearly-BRD-PRD 학습 로드맵

**생성일**: 2026-02-01
**방법론**: CUA_VL (Catch Up AI Vibe Learning)
**버전**: 1.0

---

## 📚 학습 개요

### Topic 소개
Clearly 앱을 활용한 BRD(Business Requirements Document)와 PRD(Product Requirements Document) 작성 방법론을 학습하고, 실습으로 Catch Up AI 홈페이지를 위한 BRD/PRD를 작성하는 Output 중심 학습

### 학습 목표
- Clearly 앱의 기능과 사용 방법 이해
- BRD와 PRD의 개념 및 차이점 이해
- Vibe Coding에서 요구사항 문서의 중요성 이해
- 실습을 통해 Catch Up AI 홈페이지 BRD/PRD 작성

### 예상 학습 기간
3-5일

### 학습 환경
- OS: Windows 11
- 도구: 웹 브라우저, VS Code + Claude Code Extension, Obsidian, Git
- 사전 지식: Vibe Coding 기본 이해, 웹 애플리케이션 기본 개념

---

## 🗺️ 전체 로드맵 구조

| 모듈 | 모듈명 | 난이도 | 예상 시간 | 산출물 폴더 |
|------|--------|--------|----------|------------|
| M1 | Clearly 개요 및 핵심 개념 | ⭐ | 2-3h | 01-Clearly-Overview/ |
| M2 | Catch Up AI BRD/PRD 실습 | ⭐⭐ | 3-4h | 02-CatchUpAI-BRD-PRD/ |
| M3 | 문서화 및 사용 가이드 | ⭐⭐ | 2-3h | (Topic 루트) |

**총 예상 시간**: 7-10시간 (3-5일)

---

## 📖 모듈별 상세 계획

### M1 - Clearly 개요 및 핵심 개념

**난이도**: ⭐
**예상 시간**: 2-3h
**산출물 폴더**: `01-Clearly-Overview/`

#### 학습 목표
- [ ] Clearly 앱의 목적과 핵심 가치를 1-2문장으로 설명할 수 있다
- [ ] BRD와 PRD의 차이점을 명확히 구분하여 설명할 수 있다
- [ ] Vibe Coding에서 요구사항 문서가 왜 중요한지 설명할 수 있다
- [ ] Clearly의 Plain Mode와 Technical Mode 차이를 이해한다
- [ ] Clearly 앱에 로그인하고 기본 인터페이스를 탐색할 수 있다

#### 주요 개념

1. **Clearly**: AI 기반 BRD/PRD 생성 플랫폼. Q&A 위자드를 통해 비기술자도 쉽게 요구사항 문서 작성 가능

2. **BRD (Business Requirements Document)**: 비즈니스 관점에서 "왜(Why)"와 "무엇(What)"을 정의하는 문서. 경영진/이해관계자 대상

3. **PRD (Product Requirements Document)**: "무엇(What)"과 "어떻게(How)"를 상세히 정의하는 문서. 개발팀/디자이너 대상

4. **Vibe Coding**: 코드를 직접 작성하는 대신, AI에게 비전을 전달하여 코드를 생성하는 개발 방법론. 요구사항 품질 = AI 결과물 품질

5. **Plain Mode vs Technical Mode**:
   - Plain Mode: 비기술자용, AI 코딩 도구용 프롬프트 생성
   - Technical Mode: 개발자용, 스프린트 작업 목록 생성

#### 실습 과제

**실습 1: 클리핑 자료 분석** ⭐
- **목적**: 수집된 학습 자료를 체계적으로 이해
- **단계**:
  1. `vl_materials/web_clippings/` 폴더의 핵심 파일 5개 읽기 (Landing, How to Use, BRD, PRD, Vibe Coding)
  2. 각 페이지의 핵심 내용을 노트로 정리
  3. BRD vs PRD 비교표 작성
- **예상 시간**: 45분
- **검증**: 비교표 완성 여부

**실습 2: Clearly 앱 탐색** ⭐
- **목적**: 실제 앱 인터페이스 익히기
- **단계**:
  1. https://www.clearlyreqs.com/ 접속 및 로그인
  2. 대시보드 탐색
  3. "New Project" 클릭하여 프로젝트 생성 화면 확인
  4. Plain Mode와 Technical Mode 선택 화면 확인
- **예상 시간**: 30분
- **검증**: 대시보드 접근 성공

**실습 3: 개념 정리 문서 작성** ⭐⭐
- **목적**: 학습 내용을 교과서 품질로 정리
- **단계**:
  1. `01-Clearly-Overview/` 폴더 생성
  2. `concepts/` 하위 폴더에 핵심 개념 문서 작성
  3. `README.md` 작성 (모듈 개요)
- **예상 시간**: 60분
- **검증**: README.md 및 개념 문서 생성 완료

#### 산출물
```
01-Clearly-Overview/
├── README.md                    # 모듈 개요
├── concepts/
│   ├── what-is-clearly.md       # Clearly 소개
│   ├── brd-vs-prd.md           # BRD vs PRD 비교
│   └── vibe-coding-role.md     # Vibe Coding에서의 역할
└── guides/
    └── clearly-quick-start.md  # Clearly 빠른 시작 가이드
```

#### Definition of Done
- [ ] 클리핑 자료 5개 파일 읽기 완료
- [ ] BRD vs PRD 비교표 작성 완료
- [ ] Clearly 앱 로그인 및 대시보드 탐색 완료
- [ ] `01-Clearly-Overview/` 폴더 생성
- [ ] README.md 작성
- [ ] 핵심 개념 문서 최소 2개 작성
- [ ] WorkLog 작성 완료
- [ ] Daily Retrospective 작성

#### Self-Assessment

**개념 이해** (5분):
- [ ] Clearly가 무엇인지 1문장으로 설명 가능
- [ ] BRD와 PRD의 차이를 비유와 함께 설명 가능
- [ ] Vibe Coding에서 요구사항 문서가 왜 중요한지 설명 가능

**실무 활용** (5분):
- [ ] Clearly 앱에서 새 프로젝트 생성 화면까지 이동 가능
- [ ] Plain Mode와 Technical Mode 중 어떤 것을 선택해야 하는지 판단 가능

**문제 해결** (5분):
- [ ] BRD/PRD 작성 시 어떤 정보가 필요한지 나열 가능

#### 예상 시간 배분
- 개념 학습 (클리핑 자료 분석): 45분 (25%)
- 실습 1 (자료 분석): 45분
- 실습 2 (앱 탐색): 30분
- 실습 3 (문서화): 60분
- **합계**: 3시간 (버퍼 포함)

#### 참조 자료
- [Clearly 공식 사이트](https://www.clearlyreqs.com/): 앱 접속
- `vl_materials/web_clippings/`: 클리핑된 학습 자료
- [BRD vs. PRD: ClickUp Guide](https://clickup.com/blog/brd-vs-prd/): BRD/PRD 외부 참조

---

### M2 - Catch Up AI BRD/PRD 실습

**난이도**: ⭐⭐
**예상 시간**: 3-4h
**산출물 폴더**: `02-CatchUpAI-BRD-PRD/`

#### 학습 목표
- [ ] Clearly의 AI Wizard를 활용하여 BRD를 생성할 수 있다
- [ ] 생성된 BRD를 검토하고 필요한 수정을 할 수 있다
- [ ] BRD를 기반으로 PRD를 생성할 수 있다
- [ ] Catch Up AI 2026 홈페이지의 요구사항을 명확히 정의할 수 있다

#### 주요 개념

1. **AI Wizard**: Clearly의 대화형 인터페이스. 질문에 답하면서 요구사항을 체계적으로 정리

2. **Contextual Tips**: 각 질문에 대한 설명과 샘플 답변 제공 (비기술자도 이해 가능)

3. **Project Goals & Success Metrics**: BRD의 핵심 - 프로젝트가 달성해야 할 목표와 성공 지표

4. **Target Audience**: 누구를 위한 제품인지 정의

5. **Key Features**: PRD의 핵심 - 구체적인 기능 사양

#### Catch Up AI 홈페이지 요구사항 (실습용)

**비즈니스 목표**:
- Catch Up AI 2026년 콘텐츠/활동 소개
- 방문자가 주요 프로젝트와 방법론을 이해하도록 안내

**주요 콘텐츠**:
1. Vibe Coding 방법론 연구
2. Vibe Learning 방법론 연구 (CUA_VL)
3. Vibe Guiding 방법론 연구
4. AI4PKM 프로젝트 진행
5. 시애틀 지역 AI 생태계 소식 공유

**타겟 오디언스**:
- AI에 관심 있는 개발자/비개발자
- 새로운 학습 방법론에 관심 있는 사람
- 시애틀 지역 AI 커뮤니티

#### 실습 과제

**실습 1: Catch Up AI BRD 생성** ⭐⭐
- **목적**: Clearly를 사용하여 실제 BRD 생성 경험
- **단계**:
  1. Clearly에서 새 프로젝트 생성
  2. 프로젝트 이름: "Catch Up AI 2026 Homepage"
  3. Plain Mode 선택 (홈페이지는 복잡한 개발이 아님)
  4. AI Wizard 질문에 답변 (위 요구사항 참고)
  5. 생성된 BRD 검토 및 필요시 수정
  6. BRD 내보내기 (Export)
- **예상 시간**: 60분
- **검증**: BRD 문서 생성 및 내보내기 완료

**실습 2: Catch Up AI PRD 생성** ⭐⭐
- **목적**: BRD를 기반으로 PRD 생성
- **단계**:
  1. 동일 프로젝트에서 PRD 생성 진행
  2. 상세 기능 사양 입력
  3. 사용자 스토리 추가
  4. 생성된 PRD 검토
  5. PRD 내보내기
- **예상 시간**: 60분
- **검증**: PRD 문서 생성 및 내보내기 완료

**실습 3: 문서 정리 및 저장** ⭐
- **목적**: 생성된 문서를 로컬에 저장하고 정리
- **단계**:
  1. `02-CatchUpAI-BRD-PRD/` 폴더 생성
  2. BRD 문서 저장 (`brd/`)
  3. PRD 문서 저장 (`prd/`)
  4. README.md 작성 (프로젝트 개요, 문서 설명)
- **예상 시간**: 30분
- **검증**: 폴더 구조 및 파일 저장 완료

#### 산출물
```
02-CatchUpAI-BRD-PRD/
├── README.md                    # 프로젝트 개요
├── brd/
│   └── catchupai-2026-brd.md   # Clearly에서 생성한 BRD
├── prd/
│   └── catchupai-2026-prd.md   # Clearly에서 생성한 PRD
└── notes/
    └── wizard-experience.md    # AI Wizard 사용 경험 기록
```

#### Definition of Done
- [ ] Clearly에서 "Catch Up AI 2026 Homepage" 프로젝트 생성
- [ ] AI Wizard를 통해 BRD 생성 완료
- [ ] BRD 검토 및 필요한 수정 완료
- [ ] PRD 생성 완료
- [ ] BRD/PRD 내보내기 완료
- [ ] `02-CatchUpAI-BRD-PRD/` 폴더에 문서 저장
- [ ] README.md 작성
- [ ] WorkLog 작성 완료
- [ ] Daily Retrospective 작성

#### Self-Assessment

**개념 이해** (5분):
- [ ] AI Wizard가 어떤 질문을 하는지 설명 가능
- [ ] BRD에서 PRD로 어떻게 연결되는지 설명 가능

**실무 활용** (5분):
- [ ] 새로운 프로젝트에 대해 BRD를 작성할 수 있다
- [ ] 생성된 BRD/PRD의 품질을 판단할 수 있다

**문제 해결** (5분):
- [ ] AI Wizard 답변이 부족할 때 어떻게 보완하는지 알고 있다

#### 예상 시간 배분
- 실습 1 (BRD 생성): 60분
- 실습 2 (PRD 생성): 60분
- 실습 3 (문서 정리): 30분
- 버퍼 및 문서화: 30분
- **합계**: 3시간 (버퍼 포함)

#### 참조 자료
- [Clearly 앱](https://clearly-711582759542.us-west1.run.app/): 실습 진행
- [Catch Up AI 현재 홈페이지](https://catchupai.net/): 참고용
- `01-Clearly-Overview/`: M1 학습 내용

---

### M3 - 문서화 및 사용 가이드

**난이도**: ⭐⭐
**예상 시간**: 2-3h
**산출물 폴더**: Topic 루트 (README.md 등)

#### 학습 목표
- [ ] Clearly 사용 경험을 다른 사람이 따라할 수 있는 가이드로 정리할 수 있다
- [ ] 학습 전체 과정을 회고하고 인사이트를 도출할 수 있다
- [ ] Topic 전체 산출물을 교과서 품질로 완성할 수 있다

#### 주요 개념

1. **교과서 품질**: 다른 학습자가 이 문서만으로 Clearly 사용법을 배울 수 있는 수준

2. **Step-by-step Guide**: 스크린샷/설명과 함께 단계별로 따라할 수 있는 가이드

3. **Best Practices**: 실습 과정에서 발견한 팁과 주의사항

4. **Topic Retrospective**: 전체 학습 여정에 대한 회고

#### 실습 과제

**실습 1: Clearly 사용 가이드 작성** ⭐⭐
- **목적**: 다른 사람을 위한 사용 가이드 완성
- **단계**:
  1. M1, M2 경험을 바탕으로 단계별 가이드 작성
  2. 주요 화면 설명 추가
  3. 팁과 주의사항 정리
  4. 추천 사용 시나리오 작성
- **예상 시간**: 60분
- **검증**: 가이드 문서 완성

**실습 2: Topic README 완성** ⭐
- **목적**: Topic 전체를 소개하는 README 작성
- **단계**:
  1. Topic 루트의 README.md 작성/업데이트
  2. 폴더 구조 설명
  3. 학습 흐름 설명
  4. 주요 산출물 링크
- **예상 시간**: 30분
- **검증**: README.md 완성

**실습 3: Topic Retrospective 작성** ⭐⭐
- **목적**: 전체 학습 여정 회고
- **단계**:
  1. `vl_worklog/20260201_Clearly-BRD-PRD_Final_Retrospective.md` 작성
  2. 전체 학습 여정 통계 (소요 시간, 완료율)
  3. CUA_VL 방법론 효과성 평가
  4. 산출물 품질 평가
  5. 향후 개선 사항
- **예상 시간**: 30분
- **검증**: Retrospective 문서 완성

#### 산출물
```
Clearly-BRD-PRD/
├── README.md                    # Topic 전체 소개 (업데이트)
├── 01-Clearly-Overview/         # M1 산출물
├── 02-CatchUpAI-BRD-PRD/        # M2 산출물
└── vl_worklog/
    └── YYYYMMDD_Clearly-BRD-PRD_Final_Retrospective.md
```

#### Definition of Done
- [ ] Clearly 사용 가이드 문서 완성
- [ ] Topic README.md 완성
- [ ] 모든 산출물 폴더 정리 완료
- [ ] Topic Retrospective 작성
- [ ] 전체 링크 검증
- [ ] WorkLog 작성 완료

#### Self-Assessment

**개념 이해** (5분):
- [ ] Clearly 사용법을 다른 사람에게 설명할 수 있다
- [ ] BRD/PRD 작성 프로세스를 설명할 수 있다

**실무 활용** (5분):
- [ ] 새로운 프로젝트에 Clearly를 적용할 수 있다
- [ ] 작성한 가이드로 다른 사람을 안내할 수 있다

**교과서 품질** (5분):
- [ ] 산출물만으로 다른 사람이 학습 가능
- [ ] 모든 예제가 실제로 동작함을 검증

#### 예상 시간 배분
- 실습 1 (사용 가이드): 60분
- 실습 2 (README): 30분
- 실습 3 (Retrospective): 30분
- 최종 검토: 30분
- **합계**: 2.5시간 (버퍼 포함)

#### 참조 자료
- M1, M2의 모든 산출물
- WorkLog 파일들
- CUA_VL README.md (회고 가이드)

---

## 📝 WorkLog 작성 가이드

각 학습 세션마다 WorkLog를 작성하여 진행 상황을 추적합니다.

**파일명 규칙**: `vl_worklog/YYYYMMDD_MX_Clearly-BRD-PRD.md`
- 예: `vl_worklog/20260201_M1_Clearly-BRD-PRD.md`

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
`vl_worklog/YYYYMMDD_MX_Retrospective.md`:
- 계획 대비 실제 비교
- 핵심 학습 내용
- 발생한 문제와 해결
- Roadmap 정확도 평가
- 다음 모듈 준비사항

### Topic Retrospective (전체 완료 시, 30-60분)
`vl_worklog/YYYYMMDD_Clearly-BRD-PRD_Final_Retrospective.md`:
- 전체 학습 여정 통계
- CUA_VL 방법론 효과성 평가
- 산출물 품질 평가
- 향후 학습 개선 사항

---

## 📂 전체 폴더 구조

```
Clearly-BRD-PRD/
├── topic_info.md                 # Topic 정보
├── README.md                     # Topic 전체 소개
├── vl_prompts/
│   ├── roadmap_prompt.md
│   └── daily_learning_prompt.md
├── vl_roadmap/
│   └── 20260201_RoadMap_Clearly-BRD-PRD.md  # 이 파일
├── vl_worklog/
│   ├── 20260201_M1_Clearly-BRD-PRD.md
│   ├── 20260202_M2_Clearly-BRD-PRD.md
│   ├── 20260203_M3_Clearly-BRD-PRD.md
│   └── 20260203_Clearly-BRD-PRD_Final_Retrospective.md
├── vl_materials/
│   └── web_clippings/            # Clearly 웹사이트 클리핑
├── 01-Clearly-Overview/
│   ├── README.md
│   ├── concepts/
│   │   ├── what-is-clearly.md
│   │   ├── brd-vs-prd.md
│   │   └── vibe-coding-role.md
│   └── guides/
│       └── clearly-quick-start.md
└── 02-CatchUpAI-BRD-PRD/
    ├── README.md
    ├── brd/
    │   └── catchupai-2026-brd.md
    ├── prd/
    │   └── catchupai-2026-prd.md
    └── notes/
        └── wizard-experience.md
```

---

## 📊 학습 진행 상황 추적

| 모듈 | 시작일 | 종료일 | 상태 | DoD 달성률 | 비고 |
|------|--------|--------|------|-----------|------|
| M1 | 2026-02-01 | 2026-02-01 | ✅ | 100% | 산출물 4개 완성 |
| M2 | 2026-02-08 | 2026-02-15 | ✅ | 100% | BRD v3 + PRD v2 + Claude Code Output 완성, 3 Sessions |
| M3 | 2026-02-15 | 2026-02-15 | ✅ | 100% | 사용 가이드 + Topic README + Retrospective 완성 |

**범례**:
- ⏳ 대기
- 🔄 진행 중
- ✅ 완료

---

## 🎯 성공 기준

전체 Topic 완료 기준:
- [ ] 모든 모듈 완료 (DoD 100%)
- [ ] 최소 2개 산출물 폴더 생성 (`01-Clearly-Overview/`, `02-CatchUpAI-BRD-PRD/`)
- [ ] Catch Up AI BRD 완성
- [ ] Catch Up AI PRD 완성
- [ ] Clearly 사용 가이드 완성
- [ ] Topic Retrospective 작성
- [ ] Self-Assessment 평균 ⭐⭐⭐⭐ 이상

---

**생성자**: Claude with CUA_VL
**Roadmap 버전**: 1.0
**방법론 버전**: CUA_VL 2.0
