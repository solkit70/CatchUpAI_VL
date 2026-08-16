# VibeLearn-AI-Chromebook 학습 로드맵

**생성일**: 2026-08-16
**방법론**: VibeLearn AI v2.0
**버전**: 1.1 (2026-08-16 개정)

> **v1.1 변경**: 전 모듈의 Definition of Done을 **산출물 개수 세기에서 질문 기반으로 전환**했다. M1 회고에서 나온 제안을 반영한 것이다. 상세는 [모듈별 상세 계획](#-모듈별-상세-계획) 서두 참조.

---

## 📚 학습 개요

### Topic 소개

미국 교육 시스템의 AI 사용 규범과 학교 지급 Chromebook의 관리 구조를 학습한 뒤, 그 제약 위에서 실제로 동작하는 브라우저 전용 2트랙 VibeLearn AI를 설계·구축하고, 매뉴얼·온보딩 프로세스·소개 영상까지 완성한다.

VibeLearn AI는 CLI로 AI를 쓰는 사용자(VS Code + Claude Code/Codex)를 전제로 만들어졌다. 그런데 미국 학교는 학생들에게 Chromebook을 지급하고, 이 환경에서는 현재 시스템을 거의 그대로 쓸 수 없다. 이 Topic은 그 간극을 메운다.

### 학습 목표

- [ ] 미국의 AI 교육 규범을 연방(DoL AI Literacy Framework, 권고) → 주(가이던스 34개 주+PR / 학군 정책 의무화 6개 주) → 학군(AUP, 실질 구속력) 3층으로 구분해 설명할 수 있다
- [ ] CIPA·COPPA·FERPA가 각각 무엇을 금지하는지, 학생 대상 AI 도구 설계에 어떤 제약을 만드는지 설명할 수 있다
- [ ] 관리형 Chromebook에서 무엇이 가능하고 무엇이 차단되는지 근거와 함께 판정표로 제시할 수 있다
- [ ] 교사가 GoGuardian 등으로 학생 기기를 어떻게 관리하는지 설명하고, 그것이 도구 설계에 주는 제약을 반영할 수 있다
- [ ] 현재 VibeLearn AI가 Chromebook에서 막히는 지점을 기술적 차단과 정책적 차단으로 분리해 문서화할 수 있다
- [ ] 브라우저 전용 2트랙(학생=Gemini / 성인=Claude·Codespaces) 아키텍처를 설계하고 그 결정 근거를 ADR로 남길 수 있다
- [ ] Chromebook판 VibeLearn AI를 실제로 구축하고, 로컬 파일·CLI 없이 새 Topic 하나를 처음부터 끝까지 완주시킬 수 있다
- [ ] 학생용·교사용·IT 관리자용 매뉴얼과 15분 온보딩 프로세스를 만들 수 있다
- [ ] Remotion으로 학습 과정 영상과 사용법 튜토리얼 영상을 제작할 수 있다

### 예상 학습 기간

**5-6주** (주당 15-20시간, 세션당 3-5시간) — 총 78시간 (버퍼 20% 포함)

STEP 1 적정성 검토 결과 복잡도는 "복잡"이나 사전 지식이 이례적으로 강해 3-4주도 가능했다. 전체 범위 유지와 외부 의존성(실기기 확보, 협조 교사 섭외, 학교 IT 피드백) 여유 확보를 위해 5-6주로 확정했다.

### 학습 환경

- **OS**: Windows 11 (제작) / 검증 대상 ChromeOS 관리형 Chromebook
- **도구**: VS Code + Claude Code, Git/GitHub, Remotion(gpt-image-2 + edge-tts)
- **조사 대상**: Google Admin Console, Workspace for Education, Gemini in Classroom·Gems, GoGuardian/Securly/Lightspeed, claude.ai/code, GitHub Codespaces
- **사전 지식**: VibeLearn AI 방법론(완전 숙지), GitHub, Remotion 파이프라인(보유) / 신규 — 미국 K-12 AI 정책, CIPA·COPPA·FERPA, ChromeOS 관리 모델

---

## 🗺️ 전체 로드맵 구조

| 모듈  | 모듈명                         | 난이도 | 예상 시간 | 산출물 폴더                       |
| --- | --------------------------- | --- | ----- | ---------------------------- |
| M1  | 미국 교육환경의 AI 사용 규범           | ⭐⭐  | 8h    | `01-US-AI-Education-Policy/` |
| M2  | 학교 지급 Chromebook의 관리 실체     | ⭐⭐  | 8h    | `02-Chromebook-Management/`  |
| M3  | 현재 VibeLearn AI가 막히는 지점 해부  | ⭐⭐  | 5h    | `03-Gap-Analysis/`           |
| M4  | 브라우저 전용 대안 조사 및 2트랙 설계      | ⭐⭐⭐ | 8h    | `04-Architecture-Design/`    |
| M5  | Chromebook판 VibeLearn AI 구축 | ⭐⭐⭐ | 16h   | `05-Build/`                  |
| M6  | 매뉴얼 + 온보딩 프로세스              | ⭐⭐  | 12h   | `06-Manual-Onboarding/`      |
| M7  | 레포지토리 전략 확정 및 배포            | ⭐⭐  | 5h    | `07-Repo-Strategy/`          |
| M8  | Remotion 영상 제작              | ⭐⭐⭐ | 16h   | `08-Videos/`                 |

**총 예상 시간**: 78시간 (버퍼 20% 포함)

**모듈 흐름**: 정책 이해(M1) → 기기 이해(M2) → 갭 진단(M3) → 설계(M4) → **구축(M5, 실질적 Capstone)** → 문서화(M6) → 배포(M7) → 홍보(M8)

> **이 Topic의 순서 원칙**: 기기 제약보다 정책·규범이 설계를 더 강하게 결정한다. M1·M2를 M3보다 먼저 두는 이유이며, 이 순서는 바꾸지 않는다.

---

## 📖 모듈별 상세 계획

### Definition of Done을 읽는 법 (v1.1)

각 모듈의 DoD는 세 층으로 되어 있다.

| 층 | 의미 |
|---|---|
| **핵심 질문** | 이 모듈이 답해야 할 질문. **여기에 답할 수 있으면 모듈은 끝난 것이다** |
| **답을 뒷받침하는 증거** | 그 답이 근거 있는 것임을 보이는 산출물. 목표가 아니라 증거다 |
| **기록** | README, WorkLog, Retrospective |

**왜 이렇게 바꿨나** — M1을 진행하며 DoD를 "`concepts/` 5개 문서 작성"처럼 개수로 잡은 것이 문제였다. 1차 출처를 확보하니 내용이 늘어 실제로는 7개가 됐고, 개수는 학습의 완료 여부와 무관했다. **개수를 채우려 문서를 쪼개거나, 개수를 맞췄다고 답하지 못한 채 넘어가는 것을 둘 다 막으려면 질문으로 잡아야 한다.**

증거 항목에도 개수가 남아 있지만(예: "판정 항목 15개 이상") 이것은 **품질 하한선**이지 목표가 아니다. 질문에 답하는 데 20개가 필요하면 20개를 만든다.

> **방법론 개선 제안**: 이 변경이 유효하다면 `templates/roadmap_prompt_template.md`의 "6. Definition of Done (체크리스트 5-8개)" 항목도 같은 방향으로 고칠 가치가 있다. Topic 완료 후 Final Retrospective에서 판단할 것.

### M1 - 미국 교육환경의 AI 사용 규범

**난이도**: ⭐⭐
**예상 시간**: 8h
**산출물 폴더**: `01-US-AI-Education-Policy/`

**학습 질문**: 미국 학생은 AI를 어디까지 쓰도록 권장되고 어디서 막히는가? 그 규칙은 누가 만드는가?

#### 학습 목표

- [ ] 연방·주·학군 3층 구조에서 각 층이 무엇을 정하고 어느 층이 실제 구속력을 갖는지 구분해 설명할 수 있다
- [ ] DoL National AI Literacy Framework의 5개 콘텐츠 영역을 나열하고 각각이 무엇을 요구하는지 설명할 수 있다
- [ ] CIPA·COPPA·FERPA가 각각 무엇을 대상으로 무엇을 금지하는지 표로 구분할 수 있다
- [ ] 주요 AI 도구 4종의 연령 게이트와 교육용 예외 조항을 비교표로 제시할 수 있다
- [ ] AI4K12 Five Big Ideas를 학년대별 참여 수준과 연결해 설명할 수 있다

#### 주요 개념

1. **3층 규범 구조**: 연방(권고, 구속력 없음) → 주(가이던스 + 일부 법률) → 학군 AUP(실제 구속력). 오해하기 쉬운 점 — 연방 프레임워크는 "지침"이지 "규칙"이 아니다. 학생이 실제로 부딪히는 벽은 거의 항상 학군 AUP다.
2. **DoL National AI Literacy Framework** (2026-02-13): 5개 콘텐츠 영역(AI 원리 이해 / 활용처 탐색 / 효과적 지시 / 출력 평가 / 책임 있는 사용) + 7개 전달 원칙. 학교에 한정되지 않고 **전체 노동력과 비영리·지역단체**를 대상으로 한다 — 이 Topic의 대상 확장 매핑이 여기에 붙는다.
3. **CIPA / COPPA / FERPA**: CIPA는 E-Rate 자금을 받는 학교에 필터링·모니터링 의무를 부과한다(기기 제약의 법적 뿌리). COPPA는 13세 미만 아동의 데이터 수집에 부모 동의를 요구한다. FERPA는 학생 교육 기록의 공개를 제한한다. 셋은 대상과 금지 행위가 다르다 — 뭉뚱그리면 설계 판단을 그르친다.
4. **연령 게이트**: 도구별 정책이 제각각이며 "교육용 버전"의 존재 여부가 갈린다. Claude은 18세 미만 전면 불가(부모 동의로도 예외 없음)이고, Gemini는 Workspace for Education 경로로 K-12 전 연령이 열려 있다.
5. **AI4K12 Five Big Ideas**: Perception / Representation & Reasoning / Learning / Natural Interaction / Societal Impact. 4단계 참여 수준(인식 → 개념적 이해 → 윤리적 설계 → 실세계 적용)과 조합해 학년대별 목표를 잡는다.

#### 실습 과제

**실습 1: 3층 규범 지도 작성** ⭐
- **목적**: 규칙을 만드는 주체와 구속력의 차이를 손으로 정리해 체화한다
- **단계**:
  1. DoL Framework 원문에서 5개 영역 + 7개 원칙을 추출해 정리
  2. ExcelinEd·FutureEd 트래커에서 주별 가이던스 현황과 2026 회기 법안 동향 확인
  3. 학군 AUP 실물 3개 이상을 찾아 공통 조항 추출 (특히 "AI Assisted" 표기 요구)
  4. 3층을 Mermaid 다이어그램으로 표현하고 각 층에 "누가 정하나 / 구속력 / 위반 시" 3열 표 첨부
- **예상 시간**: 100분
- **검증**: 임의의 규칙 하나를 제시했을 때 어느 층 소관인지 즉시 판정 가능

**실습 2: 법률 프레임 + 연령 게이트 비교표** ⭐⭐
- **목적**: 설계 단계에서 바로 참조할 판정 기준을 만든다
- **단계**:
  1. CIPA·COPPA·FERPA 각각의 적용 대상 / 금지 행위 / 위반 결과를 1차 출처로 확인
  2. "학생 데이터가 외부 AI로 나갈 때 어느 법이 걸리는가" 시나리오 5개를 만들어 판정
  3. Claude / ChatGPT / Gemini for Education / Copilot의 연령 정책과 교육용 예외를 공식 문서로 확인
  4. 두 표를 `concepts/`에 저장하고 각 셀에 출처 링크 + 조사 시점(2026-08) 명기
- **예상 시간**: 130분
- **검증**: M4 아키텍처 설계 시 이 표만 보고 도구 채택 가부 판정 가능

**실습 3: 대상 확장 매핑** ⭐⭐⭐
- **목적**: 이번 Topic 이후에도 재사용할 AI 교육 지식 자산을 만든다
- **단계**:
  1. DoL 5개 콘텐츠 영역을 세로축으로 놓는다
  2. 가로축에 K-12 학생 / 대학생·성인 학습자 / 시니어 / 시민단체·비IT 배경 4개 대상을 놓는다
  3. 각 교차점에 규범·제약·진입점·주의사항을 채운다
  4. 대상별 1페이지 요약을 `audiences/` 하위에 개별 파일로 분리
- **예상 시간**: 120분
- **검증**: 임의의 대상 하나를 골랐을 때 "무엇부터 가르치고 무엇을 조심할지" 즉답 가능

#### 산출물

```
01-US-AI-Education-Policy/
├── README.md                          ← 학습 순서 안내 + 전체 문서 링크 (필수)
├── concepts/
│   ├── three-layer-governance.md      # 연방·주·학군 3층 구조
│   ├── dol-ai-literacy-framework.md   # DoL 프레임워크 5영역 7원칙
│   ├── legal-frame-cipa-coppa-ferpa.md # 법률 프레임 비교표
│   ├── age-gates-by-tool.md           # AI 도구별 연령 게이트 비교표
│   └── ai4k12-five-big-ideas.md       # AI4K12 커리큘럼 기준
├── audiences/                         ← 재사용 자산 (Topic 종료 후에도 유지)
│   ├── README.md
│   ├── k12-students.md
│   ├── adult-learners.md
│   ├── seniors.md
│   └── community-nonprofit.md
└── guides/
    └── how-to-check-district-policy.md # 특정 학군 정책 확인 절차
```

#### Definition of Done

**핵심 질문 — 아래에 답할 수 있으면 이 모듈은 끝난 것이다**

- [x] Q1. 미국 학생의 AI 사용 규칙은 누가 만들고, 어느 층이 실제로 구속하는가?
- [x] Q2. CIPA·COPPA·FERPA는 각각 무엇을 금지하며, 학생 AI 도구 설계에 어떤 제약을 만드는가?
- [x] Q3. 어떤 AI 도구를 K-12 학생에게 쓸 수 있는가? 그 판정 절차는?
- [x] Q4. 학군은 학생의 AI 사용을 실제로 어떻게 규율하는가?
- [x] Q5. 이 규범을 학생 밖 대상(교사·성인·시니어·시민단체)에게 적용하면 무엇이 달라지는가?

**답을 뒷받침하는 증거**

- [x] 모든 정책 주장에 1차 출처 링크 + 조사 시점 명기, 2차 자료만 근거인 항목은 "⚠️ 미확인" 표기
- [x] 3층 구조 판정 절차 (임의의 규칙을 어느 층 소관인지 즉시 판정 가능)
- [x] 법률 3종 비교표 + 판정 시나리오
- [x] 도구별 연령 게이트 비교표
- [x] 대상별 접근법 (DoL 5개 영역 × 대상 매트릭스)

**기록**

- [x] README.md (학습 순서 + 상대 경로 링크 + 이전/다음 모듈 링크)
- [x] WorkLog + Daily Retrospective + Module Retrospective

#### Self-Assessment

**개념 이해**:
- [ ] "미국 학생이 학교에서 ChatGPT를 쓸 수 있나?"에 층위를 구분해 답할 수 있다
- [ ] CIPA와 COPPA를 혼동하지 않고 각각의 적용 상황을 예시로 설명할 수 있다

**실무 활용**:
- [ ] 새 AI 도구를 제시받았을 때 K-12 학생에게 쓸 수 있는지 판정 절차를 제시할 수 있다
- [ ] 시니어 대상 AI 교육을 요청받았을 때 K-12와 무엇이 달라야 하는지 설명할 수 있다

**문제 해결**:
- [ ] 정책 정보가 낡았을 가능성을 감지하고 재확인 경로를 제시할 수 있다

#### 예상 시간 배분

- 개념 학습 및 원문 조사: 140분 (29%)
- 실습 1 (3층 지도): 100분
- 실습 2 (법률·연령 표): 130분
- 실습 3 (대상 매핑): 120분
- 문서화 및 README: 60분
- **합계**: 8h (버퍼 20% 포함)

#### 참조 자료

- [State K-12 AI Policy in 2026 (ExcelinEd)](https://excelined.org/2026/05/26/state-k-12-ai-policy-in-2026-milestones/): 주별 가이던스 현황 개괄
- [Legislative Tracker: 2026 State AI in Education Bills (FutureEd)](https://www.future-ed.org/legislative-tracker-2026-state-ai-in-education-bills/): 27개 주 71개 법안 추적
- [AI4K12](https://ai4k12.org/): Five Big Ideas 원본 가이드라인
- [Vetting Generative AI Tools for Use in Schools (FPF)](https://fpf.org/wp-content/uploads/2024/10/Ed_AI_legal_compliance.pdf_FInal_OCT24.pdf): 법률 준수 관점 도구 검증 프레임
- [Claude 최소 연령 정책](https://support.claude.com/en/articles/13117299-minimum-age-requirement-access-restriction): 18+ 정책 1차 출처
- [Gemini in Classroom 전 연령 확대](https://workspaceupdates.googleblog.com/2026/08/gemini-in-google-classroom-is-expanding-to-users-of-all-ages-with-contextualized-Gemini-starter-prompts-for-students.html): 2026-08-10 공지

---

### M2 - 학교 지급 Chromebook의 관리 실체

**난이도**: ⭐⭐
**예상 시간**: 8h
**산출물 폴더**: `02-Chromebook-Management/`

**학습 질문**: 학교가 나눠준 Chromebook에는 무엇이 설치·강제돼 있고, 교사는 그것을 어떻게 관리하는가?

#### 학습 목표

- [ ] ChromeOS의 3개 런타임을 구분하고 관리 정책이 각각을 어떻게 차단하는지 설명할 수 있다
- [ ] Google Admin Console의 OU 구조와 강제 정책이 학생 기기에 적용되는 경로를 설명할 수 있다
- [ ] GoGuardian·Securly·Lightspeed의 필터링 방식 차이(네트워크 레벨 vs 기기 에이전트)를 비교할 수 있다
- [ ] 교사가 학생 기기에 대해 실제로 행사할 수 있는 통제 권한을 나열할 수 있다
- [ ] 신규 AI 도구가 학군 승인을 받는 절차를 단계별로 설명할 수 있다

#### 주요 개념

1. **ChromeOS 3개 런타임**: Chrome 브라우저(항상 가능) / Android 앱 ARC(정책으로 차단 가능) / Linux Crostini(관리형 기기 기본 비활성). 오해하기 쉬운 점 — "Chromebook에서 Linux를 켜면 된다"는 조언은 개인 기기 이야기다. 학교 기기에서는 학생 권한으로 켤 수 없고, 우회는 정책 위반이다.
2. **Admin Console과 OU**: zero-touch enrollment로 등록된 기기는 조직 단위(OU)별 정책을 강제로 받는다. 관리자는 학년·학교별 OU를 나눠 서로 다른 정책을 적용하며, 18세 미만 그룹만 따로 떼어 특정 기능을 끌 수 있다.
3. **확장 프로그램 allowlist**: 관리자가 허용한 확장만 설치 가능하다. Claude Code나 임의의 개발 도구 확장을 학생이 넣을 방법이 없다.
4. **필터링 계층 이원화**: 네트워크 레벨(학교망에 붙은 모든 기기, 에이전트 불필요) vs 기기 레벨 에이전트(집에서도 작동). CIPA는 E-Rate 자금 조건으로 이 필터링을 요구한다.
5. **교사 통제 권한**: GoGuardian Teacher 기준 — 학생 화면 실시간 열람, 탭 강제 종료, 화면 잠금, 개별 채팅, Google Docs·Gmail·검색 활동 가시성. 이것이 설계 제약을 만든다. **학생이 쓰는 도구는 교사가 관찰 가능한 표면 위에 있어야 채택된다.**
6. **도구 승인 절차**: 학군 사전 승인 목록 확인 → DPA(데이터 처리 계약) 체결 → 벤더 컴플라이언스 문서 검증(FERPA·COPPA 준수 증빙). 벤더가 컴플라이언스 문서 제공을 거부하면 그 자체가 탈락 사유다.

#### 실습 과제

**실습 1: 관리형 기기 가부 판정표** ⭐⭐
- **목적**: M3 갭 분석의 판정 기준을 미리 확보한다
- **단계**:
  1. 후보 행위 15개 이상을 나열 (터미널 실행, git clone, VS Code 설치, npm 실행, 파일 로컬 저장, 확장 설치, Android 앱 설치, 외부 사이트 접근 등)
  2. 각 항목에 가능/조건부/불가 판정과 근거(정책 문서 링크) 부여
  3. "조건부"인 항목은 어떤 조건인지(관리자 설정 필요 등) 명기
  4. 판정표를 `concepts/managed-device-capability-matrix.md`로 저장
- **예상 시간**: 120분
- **검증**: M3에서 이 표만 참조해 현 시스템 의존성을 전부 판정 가능

**실습 2: 필터링·모니터링 3사 비교** ⭐⭐
- **목적**: 학생 트랙 설계 시 어떤 관찰 표면 위에 올려야 하는지 판단한다
- **단계**:
  1. GoGuardian / Securly / Lightspeed 공식 문서에서 필터링 아키텍처, 교사 기능, CIPA 대응 방식 추출
  2. 비교표 작성 (필터링 위치 / 교사 실시간 통제 / Google Workspace 가시성 / 지원 OS)
  3. "학생이 Gemini in Classroom을 쓸 때 교사에게 무엇이 보이는가"를 세 도구 기준으로 정리
- **예상 시간**: 100분
- **검증**: 학생 트랙 설계 시 "이건 교사가 볼 수 있나?"에 즉답 가능

**실습 3: 도구 승인 절차 시뮬레이션** ⭐⭐⭐
- **목적**: M6 IT 관리자용 문서에 무엇을 담아야 하는지 역산한다
- **단계**:
  1. 실제 학군의 AI 도구 승인 절차 문서 2개 이상 확보
  2. 요구되는 항목을 체크리스트로 추출 (DPA 조항, 데이터 저장 위치, 학생 데이터 상업적 이용 금지 명시 등)
  3. "Chromebook판 VibeLearn AI"를 가상으로 이 체크리스트에 통과시켜 보고, 부족한 항목을 M6 요구사항으로 기록
- **예상 시간**: 100분
- **검증**: M6에서 만들 IT 관리자용 문서의 목차가 이 실습에서 도출됨

#### 산출물

```
02-Chromebook-Management/
├── README.md
├── concepts/
│   ├── chromeos-runtimes.md              # Chrome / ARC / Crostini 3층
│   ├── admin-console-and-ou.md           # 등록·OU·강제 정책
│   ├── managed-device-capability-matrix.md # 가부 판정표 (M3 입력)
│   └── filtering-monitoring-vendors.md   # GoGuardian/Securly/Lightspeed 비교
├── guides/
│   ├── teacher-control-surface.md        # 교사가 행사 가능한 통제 권한
│   └── district-tool-approval-process.md # 도구 승인 절차 + 체크리스트
└── troubleshooting/
    └── why-linux-is-unavailable.md       # 학생이 Crostini를 못 켜는 이유
```

#### Definition of Done

**핵심 질문 — 아래에 답할 수 있으면 이 모듈은 끝난 것이다**

- [ ] Q1. 학교 지급 Chromebook에서 무엇이 가능하고 무엇이 차단되는가? 각각의 근거는 무엇인가?
- [ ] Q2. 교사는 학생 기기에 대해 실제로 무엇을 할 수 있는가?
- [ ] Q3. 신규 AI 도구가 학군 승인을 받으려면 어떤 관문을 거치는가?
- [ ] Q4. **CIPA가 요구하는 법적 최소선과 실제 학군의 감시 수준은 얼마나 벌어져 있는가?** (M1 이월 질문)

**답을 뒷받침하는 증거**

- [ ] 가부 판정표 — 후보 행위 15개 이상, 각 항목에 가능/조건부/불가 판정과 근거 링크. "조건부"는 어떤 조건인지 명기
- [ ] 필터링 3사 비교표 — 필터링 위치(네트워크 vs 에이전트) / 교사 실시간 통제 / Workspace 가시성 / 지원 OS
- [ ] "학생이 Gemini in Classroom을 쓸 때 교사에게 무엇이 보이는가"를 3사 기준으로 정리
- [ ] 도구 승인 체크리스트 도출 → M6 요구사항으로 기록
- [ ] Oklahoma 외 주 모델 정책 2건 이상 대조 (M1 이월 — 대표성 검증)

**기록**

- [ ] README.md (학습 순서 + 상대 경로 링크 + 이전/다음 모듈 링크)
- [ ] WorkLog + Daily Retrospective

#### Self-Assessment

**개념 이해**:
- [ ] "학교 Chromebook에서 왜 터미널을 못 쓰나"를 정책 수준에서 설명할 수 있다
- [ ] 네트워크 필터링과 기기 에이전트의 차이를 예시로 설명할 수 있다

**실무 활용**:
- [ ] 교사에게 "이 도구를 쓰면 학생 활동이 이렇게 보입니다"라고 설명할 수 있다
- [ ] IT 관리자가 물어볼 질문 5개를 예상하고 답변을 준비할 수 있다

**문제 해결**:
- [ ] 학생이 "Linux 켜는 법"을 물으면 우회 대신 정당한 대안을 제시할 수 있다

#### 예상 시간 배분

- 개념 학습 및 공식 문서 조사: 130분 (27%)
- 실습 1 (판정표): 120분
- 실습 2 (필터링 비교): 100분
- 실습 3 (승인 절차): 100분
- 문서화 및 README: 60분
- **합계**: 8h (버퍼 20% 포함)

#### 참조 자료

- [Privacy & Security (Google for Education)](https://edu.google.com/intl/ALL_us/our-values/privacy-security/): FERPA·COPPA 준수 및 관리 기능 1차 출처
- [K-12 Web Filter Comparison 2026](https://kybergate.com/blog/k12-web-filter-comparison-guide-2026/): 3사 비교 출발점 (2차 자료, 공식 문서로 교차 확인 필요)
- [GoGuardian Admin](https://www.goguardian.com/at-home-filtering-allows-complete-content-filtering-for-chromebooks-in-school-or-at-home.html): 필터링 아키텍처
- [Vetting Generative AI Tools for Use in Schools (FPF)](https://fpf.org/wp-content/uploads/2024/10/Ed_AI_legal_compliance.pdf_FInal_OCT24.pdf): 승인 절차 체크리스트 근거

> ⚠️ **외부 의존성 알림**: 이 모듈 진행 중 실물 Chromebook 확보 또는 협조 교사 섭외를 병행할 것. M4 시작 시점까지 미확보 시 검증이 시뮬레이션에 그친다.

---

### M3 - 현재 VibeLearn AI가 막히는 지점 해부

**난이도**: ⭐⭐
**예상 시간**: 5h
**산출물 폴더**: `03-Gap-Analysis/`

#### 학습 목표

- [ ] 현재 VibeLearn AI의 실행 의존성을 빠짐없이 인벤토리로 나열할 수 있다
- [ ] 각 의존성에 M2 판정표를 적용해 Chromebook 가부를 판정할 수 있다
- [ ] 기술적 차단과 정책적 차단을 분리해 기록할 수 있다
- [ ] "왜 현재 버전은 Chromebook에서 쓰기 힘든가"를 제3자가 읽고 납득할 문서로 쓸 수 있다

#### 주요 개념

1. **의존성 인벤토리**: 눈에 보이는 도구뿐 아니라 암묵적 전제까지 포함한다. `CLAUDE.md` 자동 로드는 "CLI가 작업 디렉터리를 읽는다"는 전제 위에 있고, `Topics/{Topic}/vl_*` 상대 경로는 "로컬 파일시스템이 있다"는 전제 위에 있다.
2. **기술적 차단 vs 정책적 차단**: 기술적 차단은 대안 기술로 우회 가능하다(터미널 없음 → 클라우드 터미널). 정책적 차단은 우회 불가다(18세 미만 Claude 사용 불가). 둘을 섞으면 해결 가능한 것과 불가능한 것을 구분하지 못한다.
3. **차단의 연쇄**: 하나의 차단이 여러 기능을 동시에 무너뜨린다. git 불가 → 버전 관리 + 백업 + 공유가 한꺼번에 사라진다.

#### 실습 과제

**실습 1: 의존성 전수 인벤토리** ⭐⭐
- **목적**: 빠뜨린 전제 없이 전부 드러낸다
- **단계**:
  1. `C:\AI_study\2026\VibeLearn-AI` 전체를 훑어 실행에 필요한 것을 나열 (CLI, 파일시스템, git/`gh`, `scripts/*.ps1`, `translate-claude.py` + Python, pre-commit hook, `CLAUDE.md`/`AGENTS.md`/`GEMINI.md` 자동 로드, VS Code 확장, `.claude/skills/`)
  2. 각 항목에 "이게 없으면 무엇이 안 되는가"를 1줄로 기록
  3. 암묵적 전제(상대 경로, 로컬 편집, 다중 파일 동시 읽기)를 별도 섹션으로 추가
- **예상 시간**: 70분
- **검증**: GETTING_STARTED.md의 4단계 워크플로우를 따라가며 각 단계가 어느 의존성에 걸리는지 매핑 가능

**실습 2: 가부 판정 및 차단 분류** ⭐⭐
- **목적**: 해결 가능한 것과 불가능한 것을 갈라낸다
- **단계**:
  1. M2의 `managed-device-capability-matrix.md`를 적용해 각 의존성에 가능/조건부/불가 판정
  2. 불가 항목을 기술적 차단 / 정책적 차단으로 분류
  3. 차단의 연쇄를 Mermaid 다이어그램으로 표현
  4. 정책적 차단 항목에 대해 "대안 경로가 존재하는가" 판단
- **예상 시간**: 80분
- **검증**: M4 설계 시 "이건 왜 못 쓰나"에 근거를 대며 답변 가능

**실습 3: 진단 보고서 작성** ⭐⭐⭐
- **목적**: 사용자가 명시 요청한 산출물이자, M8 영상 ①의 핵심 서사가 된다
- **단계**:
  1. 두 실습 결과를 서사로 재구성 — "이 시스템은 무엇을 전제했나 → 학교 환경은 무엇을 제공하나 → 어디서 어긋나나"
  2. 가장 치명적인 차단 3개를 선정하고 그 이유를 설명
  3. 비전문가(교사, 학부모)도 이해할 수 있는 수준으로 요약 1페이지 추가
- **예상 시간**: 70분
- **검증**: VibeLearn AI를 모르는 사람이 읽고 "그래서 못 쓰는구나"를 이해

#### 산출물

```
03-Gap-Analysis/
├── README.md
├── concepts/
│   ├── dependency-inventory.md      # 의존성 전수 목록 + 암묵적 전제
│   └── blocker-classification.md    # 기술적 차단 vs 정책적 차단
└── guides/
    ├── why-current-version-fails.md # 진단 보고서 (핵심 산출물)
    └── summary-for-non-technical.md # 교사·학부모용 1페이지 요약
```

#### Definition of Done

**핵심 질문 — 아래에 답할 수 있으면 이 모듈은 끝난 것이다**

- [ ] Q1. 현재 VibeLearn AI는 무엇을 전제하고 있는가? (드러난 의존성 + **암묵적 전제**)
- [ ] Q2. 각 전제 중 학교 Chromebook에서 무너지는 것은 무엇이며, 기술적 차단인가 정책적 차단인가?
- [ ] Q3. 그중 우회 가능한 것과 불가능한 것은 무엇인가?
- [ ] Q4. VibeLearn AI를 모르는 사람에게 "왜 못 쓰는가"를 납득시킬 수 있는가?

**답을 뒷받침하는 증거**

- [ ] 의존성 인벤토리 — 암묵적 전제(상대 경로, 로컬 편집, 다중 파일 동시 읽기) 별도 섹션 포함
- [ ] 모든 불가 항목이 기술적/정책적으로 분류되고, 정책적 차단은 대안 경로 유무까지 판단됨
- [ ] 차단의 연쇄를 Mermaid로 표현
- [ ] 가장 치명적인 차단 3개 선정 및 근거
- [ ] 진단 보고서 + **비전문가(교사·학부모)용 1페이지 요약**

**기록**

- [ ] README.md (학습 순서 + 상대 경로 링크 + 이전/다음 모듈 링크)
- [ ] WorkLog + Daily Retrospective

#### Self-Assessment

**개념 이해**:
- [ ] 기술적 차단과 정책적 차단의 차이를 각각 예시로 설명할 수 있다
- [ ] 현 시스템의 암묵적 전제 3개를 즉시 나열할 수 있다

**실무 활용**:
- [ ] 다른 CLI 도구를 제시받아도 같은 방식으로 Chromebook 적합성을 진단할 수 있다

**문제 해결**:
- [ ] "이 차단은 우회 가능한가"를 판단하는 기준을 제시할 수 있다

#### 예상 시간 배분

- 개념 정리: 60분 (20%)
- 실습 1 (인벤토리): 70분
- 실습 2 (판정·분류): 80분
- 실습 3 (보고서): 70분
- 문서화 및 README: 40분
- **합계**: 5h (버퍼 20% 포함)

#### 참조 자료

- 로컬: `C:\AI_study\2026\VibeLearn-AI` 전체 (README.md, GETTING_STARTED.md, CLAUDE.md, templates/, scripts/, extras/)
- M1 산출물: `01-US-AI-Education-Policy/concepts/age-gates-by-tool.md`
- M2 산출물: `02-Chromebook-Management/concepts/managed-device-capability-matrix.md`

---

### M4 - 브라우저 전용 대안 조사 및 2트랙 아키텍처 설계

**난이도**: ⭐⭐⭐
**예상 시간**: 8h
**산출물 폴더**: `04-Architecture-Design/`

#### 학습 목표

- [ ] 학생 트랙 후보(Gemini in Classroom, Gems, Drive/Docs)를 실제로 시험하고 가능·불가능을 확인할 수 있다
- [ ] 성인 트랙 후보(claude.ai/code, Codespaces)의 진입 요건과 비용을 확인할 수 있다
- [ ] 파일 영속성 문제에 대한 해법을 비교하고 하나를 근거와 함께 선택할 수 있다
- [ ] 2트랙 아키텍처를 다이어그램과 ADR로 문서화할 수 있다
- [ ] 교사 감독 가능성과 학군 승인 용이성을 설계 제약으로 반영할 수 있다

#### 주요 개념

1. **파일 영속성 문제 (이 모듈의 핵심 난제)**: VibeLearn AI의 루프는 "AI가 Roadmap을 읽고 → 학습을 안내하고 → WorkLog를 쓴다"이다. 브라우저 채팅에는 파일시스템이 없다. 이 루프를 어떻게 닫을 것인가가 학생 트랙의 성패를 가른다.
2. **Gem의 위치**: Gem은 시스템 프롬프트를 담는 그릇이지 파일 저장소가 아니다. 또한 유료 Workspace for Education 등급에만 번들된다. 따라서 **프롬프트 팩이 1차, Gem은 선택 계층**이어야 한다.
3. **관찰 가능성 제약**: 학생 트랙은 교사가 볼 수 있는 표면(Google Workspace 내부) 위에 있어야 채택된다. 외부 사이트로 나가는 순간 필터링과 승인 문제가 동시에 발생한다.
4. **트랙 분기 기준**: 연령(18세)이 1차 기준이지만 실제로는 "관리형 기기인가"도 함께 본다. 18세 이상이라도 학교 관리 기기를 쓰면 제약을 받는다.
5. **ADR (Architecture Decision Record)**: 결정·대안·근거·결과를 남기는 형식. 나중에 "왜 이렇게 했나"를 재구성할 수 있게 한다.

#### 실습 과제

**실습 1: 학생 트랙 실측** ⭐⭐
- **목적**: 문서가 아니라 실제 동작으로 확인한다
- **단계**:
  1. Gemini에서 VibeLearn 프롬프트 팩 초안을 실제로 돌려본다
  2. Google Drive/Docs에 Topic 폴더 구조를 만들고 AI가 그 내용을 읽을 수 있는지 확인
  3. WorkLog를 쓰는 경로를 시험 (Docs 직접 편집 / AI 출력 복사 / Drive 연동)
  4. 각 경로의 마찰(클릭 수, 복사-붙여넣기 횟수)을 측정해 기록
- **예상 시간**: 120분
- **검증**: 학생이 1회 세션을 도는 데 필요한 조작 횟수를 숫자로 제시 가능
- **⚠️ 실기기 미확보 시**: Chrome 브라우저 + 개인 Google 계정으로 대체하고 "관리형 환경 미검증" 명기

**실습 2: 성인 트랙 실측** ⭐⭐
- **목적**: 진입 장벽과 비용을 확인한다
- **단계**:
  1. claude.ai/code의 요건 확인 (Pro/Max 필요, GitHub 연결 필수, 리서치 프리뷰 상태)
  2. GitHub Codespaces를 브라우저에서 실행해 VibeLearn 레포를 열고 실제로 세션을 도는지 확인
  3. 학생팩 인증 경로와 무료 한도(180 core-hour/월) 확인
  4. 두 경로의 요건·비용·제약 비교표 작성
- **예상 시간**: 100분
- **검증**: "교사가 시작하려면 무엇이 필요한가"를 3단계로 답변 가능

**실습 3: 아키텍처 결정 및 ADR 작성** ⭐⭐⭐
- **목적**: 설계를 확정하고 근거를 남긴다
- **단계**:
  1. 파일 영속성 해법 후보 3개 이상을 나열하고 마찰·승인 난이도·교사 가시성으로 채점
  2. 하나를 선택하고 ADR 작성 (결정 / 맥락 / 대안 / 근거 / 결과 / 폐기된 선택지)
  3. 2트랙 전체 구조를 Mermaid 다이어그램으로 작성
  4. M5 구축 요구사항 목록을 도출
- **예상 시간**: 120분
- **검증**: M5 착수 시 이 문서만 보고 무엇을 만들지 결정 가능

#### 산출물

```
04-Architecture-Design/
├── README.md
├── concepts/
│   ├── file-persistence-problem.md   # 핵심 난제 정의 및 해법 비교
│   └── two-track-architecture.md     # 2트랙 구조 + Mermaid 다이어그램
├── examples/
│   ├── student-track-trial.md        # 학생 트랙 실측 기록 (마찰 측정)
│   └── adult-track-trial.md          # 성인 트랙 실측 기록
├── decisions/
│   ├── ADR-001-file-persistence.md
│   ├── ADR-002-track-split-criteria.md
│   └── ADR-003-gem-as-optional-layer.md
└── guides/
    └── m5-build-requirements.md      # M5 구축 요구사항 (도출된 결과)
```

#### Definition of Done

**핵심 질문 — 아래에 답할 수 있으면 이 모듈은 끝난 것이다**

- [ ] Q1. 브라우저에서 **"AI가 Roadmap을 읽고 → 학습을 안내하고 → WorkLog를 쓰는"** 루프를 어떻게 닫을 것인가?
- [ ] Q2. 학생이 1회 세션을 도는 데 실제로 몇 번의 조작이 필요한가?
- [ ] Q3. **Gemini 대화 공유 링크가 학교 계정에서 작동하는가?** (M1 이월 — 학군 AUP가 Level 1부터 요구)
- [ ] Q4. 교사가 학생 활동을 볼 수 있는가? 학군 승인을 통과할 수 있는 형태인가?
- [ ] Q5. 왜 이 설계를 택했고 무엇을 버렸는가?

**답을 뒷받침하는 증거**

- [ ] 학생·성인 트랙 실측 기록 — **마찰 수치(클릭 수, 복사-붙여넣기 횟수)를 숫자로** 제시
- [ ] ADR 3개 이상 (파일 영속성 / 트랙 분기 기준 / Gem의 위치). **폐기된 선택지 포함**
- [ ] 2트랙 구조 Mermaid 다이어그램
- [ ] M5 구축 요구사항 목록 — 이 문서만 보고 무엇을 만들지 결정 가능한 수준
- [ ] 선택한 해법이 실패할 경우의 폴백 명시
- [ ] 실기기 미확보 시 "⚠️ 관리형 환경 미검증" 표기 + M6 이후 보정 항목 목록

**기록**

- [ ] README.md (학습 순서 + 상대 경로 링크 + 이전/다음 모듈 링크)
- [ ] WorkLog + Daily Retrospective

#### Self-Assessment

**개념 이해**:
- [ ] 파일 영속성 문제가 왜 이 프로젝트의 핵심인지 설명할 수 있다
- [ ] Gem을 1차가 아닌 선택 계층에 둔 이유를 설명할 수 있다

**실무 활용**:
- [ ] 학생이 1회 세션을 도는 절차를 조작 단위로 설명할 수 있다
- [ ] AI에게 M5 구축을 지시할 수 있을 만큼 요구사항이 구체적이다

**문제 해결**:
- [ ] 선택한 해법이 실패할 경우의 폴백을 제시할 수 있다

#### 예상 시간 배분

- 개념 정리 및 후보 조사: 100분 (21%)
- 실습 1 (학생 트랙 실측): 120분
- 실습 2 (성인 트랙 실측): 100분
- 실습 3 (ADR·설계): 120분
- 문서화 및 README: 40분
- **합계**: 8h (버퍼 20% 포함)

#### 참조 자료

- [Claude Code on the web](https://code.claude.com/docs/en/claude-code-on-the-web): 요건·제한 1차 출처
- [GitHub Codespaces with GitHub Classroom](https://docs.github.com/en/education/manage-coursework-with-github-classroom/integrate-github-classroom-with-an-ide/using-github-codespaces-with-github-classroom): 학생 무료 한도
- [Gemini in Classroom 공지](https://workspaceupdates.googleblog.com/2026/08/gemini-in-google-classroom-is-expanding-to-users-of-all-ages-with-contextualized-Gemini-starter-prompts-for-students.html)
- M1·M2·M3 산출물 전체

---

### M5 - Chromebook판 VibeLearn AI 구축 (실질적 Capstone)

**난이도**: ⭐⭐⭐
**예상 시간**: 16h
**산출물 폴더**: `05-Build/` + 신규 레포 실체

#### 학습 목표

- [ ] CLI 전제를 걷어낸 브라우저판 프롬프트 팩 4종을 작성할 수 있다
- [ ] Gem 시스템 프롬프트를 작성하고 길이·구조 제약 안에서 동작시킬 수 있다
- [ ] Drive Topic 폴더 템플릿을 만들고 학생이 복제해 쓸 수 있게 할 수 있다
- [ ] WorkLog에 AI 사용 표기 필드를 기본 탑재할 수 있다
- [ ] 로컬 파일·CLI 없이 새 Topic 하나를 처음부터 끝까지 완주시킬 수 있다

#### 주요 개념

1. **프롬프트 팩**: 기존 `templates/`의 4종(topic_starter / roadmap / daily_learning / workflow_guide)을 브라우저 사용자가 복사-붙여넣기로 쓸 수 있게 재작성한 것. 상대 경로·CLI 명령·파일 자동 로드 전제를 전부 제거한다.
2. **AI 사용 표기 필드**: M1에서 확인한 학군 AUP의 "AI Assisted" 표기 요구를 WorkLog 템플릿에 기본 항목으로 넣는다. 학생이 나중에 덧붙이는 게 아니라 처음부터 기록되게 한다.
3. **마찰 최소화**: 학생 트랙의 성패는 조작 횟수다. M4에서 측정한 마찰 수치를 목표로 삼아 줄인다.
4. **축소 워크플로우**: Gemini는 파일·코드 도구가 Claude Code보다 약하다. 학생 트랙은 "코딩"이 아니라 **학습 기록·회고** 중심으로 범위를 재정의한다.

#### 실습 과제

**실습 1: 브라우저판 프롬프트 팩 4종 작성** ⭐⭐
- **목적**: 학생 트랙의 핵심 자산을 만든다
- **단계**:
  1. 기존 `templates/` 4종을 읽고 CLI 전제 문장을 전부 표시
  2. 각각을 브라우저용으로 재작성 (경로 → Drive 위치 안내, CLI 명령 → 클릭 절차)
  3. 각 프롬프트 끝에 "다음 단계" 안내를 명시해 학생이 길을 잃지 않게 함
  4. WorkLog 템플릿에 AI 사용 표기 필드 추가
- **예상 시간**: 240분
- **검증**: 각 프롬프트를 Gemini에 붙여넣어 의도한 응답이 나오는지 확인

**실습 2: Gem 지침 + Drive 템플릿 구축** ⭐⭐⭐
- **목적**: 선택 계층과 파일 기반을 완성한다
- **단계**:
  1. Gem 시스템 프롬프트 작성 (4단계 워크플로우 + 9개 모듈 항목 + 안전 지침)
  2. 길이 제약 확인 후 압축
  3. Drive에 Topic 폴더 템플릿 생성 (topic_info / roadmap / worklog 폴더 + 예시 파일)
  4. 교사가 Classroom으로 배포하는 절차 확인
- **예상 시간**: 240분
- **검증**: Gem 없이도(프롬프트 팩만으로) 동작하고, Gem이 있으면 더 편해지는지 양쪽 확인

**실습 3: 성인 트랙 구성 + End-to-End 완주** ⭐⭐⭐
- **목적**: 실제로 작동하는지 증명한다
- **단계**:
  1. claude.ai/code · Codespaces 진입 절차와 설정 문서화
  2. **로컬 파일과 CLI를 일절 쓰지 않고** 브라우저만으로 새 Topic 하나를 개설 → Roadmap 생성 → 첫 WorkLog 작성까지 완주
  3. 막힌 지점을 전부 기록하고 프롬프트 팩에 반영
  4. 2회차 완주로 개선 효과 확인
- **예상 시간**: 300분
- **검증**: 완주 성공 + 조작 횟수가 M4 측정치보다 감소

#### 산출물

```
05-Build/
├── README.md
├── prompt-pack/                    ← 신규 레포로 이전될 핵심 자산
│   ├── 01-topic-starter.md
│   ├── 02-roadmap.md
│   ├── 03-daily-learning.md
│   └── 04-worklog-template.md      # AI 사용 표기 필드 포함
├── gem/
│   └── vibelearn-gem-instructions.md
├── drive-template/
│   └── folder-structure-guide.md
├── adult-track/
│   ├── claude-code-web-setup.md
│   └── codespaces-setup.md
└── examples/
    └── end-to-end-trial.md         # 완주 기록 + 마찰 수치 비교
```

#### Definition of Done

**핵심 질문 — 아래에 답할 수 있으면 이 모듈은 끝난 것이다**

- [ ] Q1. **로컬 파일과 CLI 없이 새 Topic 하나를 처음부터 끝까지 완주시킬 수 있는가?** (이 모듈의 실질적 합격선)
- [ ] Q2. 학생이 학군 AUP의 공개 의무(**레벨 0~4 + 대화 링크**)를 자연스럽게 충족하는가?
- [ ] Q3. Gem 없이 프롬프트 팩만으로도 동작하는가? (무료 등급 학교 대응)
- [ ] Q4. 처음 보는 사람에게 사용법을 3분 안에 설명할 수 있는가?

**답을 뒷받침하는 증거**

- [ ] 프롬프트 팩 4종 — Gemini에 붙여넣어 의도한 응답이 나오는지 확인 완료
- [ ] Gem 지침 — 길이 제약 통과, Gem 유무 양쪽 동작 확인
- [ ] Drive 폴더 템플릿 + 교사의 Classroom 배포 절차
- [ ] WorkLog 템플릿에 AI 사용 표기 필드(레벨 + 링크) 기본 탑재
- [ ] **End-to-End 완주 기록** — 막힌 지점 전부 기록 후 프롬프트 팩에 반영, 2회차로 개선 확인
- [ ] 마찰 수치가 M4 측정치보다 감소했음을 숫자로 제시

**기록**

- [ ] README.md (학습 순서 + 상대 경로 링크 + 이전/다음 모듈 링크)
- [ ] WorkLog + Daily Retrospective

#### Self-Assessment

**개념 이해**:
- [ ] 학생 트랙에서 무엇을 덜어냈고 왜 덜어냈는지 설명할 수 있다

**실무 활용**:
- [ ] 처음 보는 사람에게 프롬프트 팩 사용법을 3분 안에 설명할 수 있다
- [ ] 학생이 막힐 지점을 미리 예상하고 대비책을 프롬프트에 넣었다

**문제 해결**:
- [ ] 완주 중 막힌 지점을 원인별로 분류하고 개선안을 냈다

#### 예상 시간 배분

- 개념 정리 및 기존 템플릿 분석: 160분 (17%)
- 실습 1 (프롬프트 팩): 240분
- 실습 2 (Gem·Drive): 240분
- 실습 3 (성인 트랙·완주): 300분
- 문서화 및 README: 120분
- **합계**: 16h (버퍼 20% 포함)

#### 참조 자료

- 로컬 `C:\AI_study\2026\VibeLearn-AI\templates\` 4종 (변환 원본)
- M4 산출물 `guides/m5-build-requirements.md`
- [Claude Code on the web](https://code.claude.com/docs/en/claude-code-on-the-web)

---

### M6 - 매뉴얼 + 온보딩 프로세스

**난이도**: ⭐⭐
**예상 시간**: 12h
**산출물 폴더**: `06-Manual-Onboarding/`

#### 학습 목표

- [ ] 학생용·교사용·IT 관리자용 매뉴얼 3종을 대상에 맞는 언어로 작성할 수 있다
- [ ] IT 관리자용 문서에 학군 승인을 통과할 컴플라이언스 근거를 담을 수 있다
- [ ] 학생이 15분 안에 첫 Topic을 만드는 온보딩 경로를 설계할 수 있다
- [ ] 교사가 학급 전체에 배포하는 절차를 문서화할 수 있다
- [ ] 3종 매뉴얼을 KR/EN으로 제공할 수 있다

#### 주요 개념

1. **대상별 언어 분리**: 학생에게는 절차, 교사에게는 수업 설계, IT 관리자에게는 위험과 준수. 같은 도구를 설명하되 답해야 할 질문이 완전히 다르다.
2. **승인 통과용 문서**: IT 관리자용은 안내문이 아니라 **심사 자료**다. M2 실습 3에서 도출한 체크리스트 항목을 하나씩 충족시킨다. "이 도구가 무엇을 하고 무엇을 하지 않는지"를 데이터 흐름 수준에서 명시한다.
3. **15분 온보딩**: 첫 성공 경험까지의 시간이 채택을 좌우한다. 설명을 줄이고 첫 결과물을 빨리 손에 쥐게 한다.
4. **KR/EN 병행**: 기존 `Topics/VibeLearn-AI/`의 선례를 따른다. 미국 학교가 1차 대상이므로 EN이 원본, KR이 번역이다.

#### 실습 과제

**실습 1: 3종 매뉴얼 작성 (EN)** ⭐⭐
- **목적**: 대상별로 답해야 할 질문에 답한다
- **단계**:
  1. 각 대상이 물을 질문 10개씩을 먼저 나열
  2. 학생용 — 절차 중심, 스크린샷 위주, 전문 용어 배제
  3. 교사용 — 수업 설계, 학생 진도 확인법, 흔한 질문 대응
  4. IT 관리자용 — 데이터 흐름도, FERPA·COPPA·CIPA 관점 서술, 사전 점검 체크리스트(Gemini 활성화, Gems 공유 허용, OU 설정)
- **예상 시간**: 300분
- **검증**: M2에서 도출한 승인 체크리스트 항목이 전부 커버됨

**실습 2: 온보딩 프로세스 설계 및 실측** ⭐⭐⭐
- **목적**: 15분 목표를 실제로 달성한다
- **단계**:
  1. 학생 온보딩 단계를 최소화해 설계 (목표: 15분 내 첫 Topic 생성)
  2. 교사 학급 배포 경로 설계 (Classroom 과제 형태 포함)
  3. 방법론을 모르는 제3자에게 문서만 주고 실제로 관찰
  4. 걸린 시간과 막힌 지점을 기록해 문서 개선
- **예상 시간**: 200분
- **검증**: 제3자가 15분 내 첫 Topic 생성 성공

**실습 3: KR 번역 및 정합성 확인** ⭐⭐
- **목적**: 양쪽 언어 버전을 동등하게 유지한다
- **단계**:
  1. 3종 매뉴얼 + 온보딩 문서를 KR로 번역
  2. 용어 일관성 확인 (기존 `templates/translation_glossary.en-ko.md` 참조)
  3. 상호 링크(`→ English Version`) 추가
- **예상 시간**: 120분
- **검증**: 양쪽 버전의 섹션 구조가 일치

#### 산출물

```
06-Manual-Onboarding/
├── README.md
├── manuals/
│   ├── student-guide.en.md / .md
│   ├── teacher-guide.en.md / .md
│   └── it-admin-compliance.en.md / .md   # 승인 심사 자료
├── onboarding/
│   ├── student-15min-quickstart.en.md / .md
│   └── teacher-class-rollout.en.md / .md
└── examples/
    └── onboarding-observation-log.md      # 제3자 관찰 기록
```

#### Definition of Done

**핵심 질문 — 아래에 답할 수 있으면 이 모듈은 끝난 것이다**

- [ ] Q1. **방법론을 모르는 제3자가 문서만 보고 15분 안에 첫 Topic을 만들 수 있는가?** (이 모듈의 실질적 합격선)
- [ ] Q2. 학교 IT 관리자가 이 문서로 승인 심사를 통과시킬 수 있는가?
- [ ] Q3. 교사가 이 자료로 학급에 배포할 수 있는가? 학군 연간 연수 자료로도 쓸 수 있는가?
- [ ] Q4. 학부모가 읽고 이해할 수 있는가?

**답을 뒷받침하는 증거**

- [ ] 매뉴얼 **4종**(학생·교사·IT 관리자·**가정**) EN + KR. 각 대상이 물을 질문 10개씩을 먼저 도출한 뒤 작성
- [ ] IT 문서가 **Oklahoma 8개 평가 영역 순서**로 구성되고 전 항목 커버 (M1·M2 이월)
- [ ] IT 문서 서두에 EO 14277 Sec. 6(a) 인용 + "신규 벤더 없음" 논지 (M1 이월)
- [ ] **ED Dear Colleague Letter 5원칙 대응표** (Educator-led / Ethical / Accessible / Transparent / Data-protective)
- [ ] IT 체크리스트에 Gemini in Classroom 활성화 + 18세 미만 OU 차단 여부 포함
- [ ] **제3자 온보딩 관찰 실시** — 걸린 시간과 막힌 지점 기록, 문서에 반영
- [ ] 연령 정책을 작성 시점 기준으로 재확인

**기록**

- [ ] README.md (학습 순서 + 상대 경로 링크 + 이전/다음 모듈 링크)
- [ ] WorkLog + Daily Retrospective

#### Self-Assessment

**개념 이해**:
- [ ] 세 대상이 각각 무엇을 가장 궁금해하는지 설명할 수 있다

**실무 활용**:
- [ ] IT 관리자의 반대 질문에 문서를 근거로 답변할 수 있다
- [ ] 교사에게 15분 안에 도구를 소개할 수 있다

**문제 해결**:
- [ ] 온보딩에서 막힌 지점을 문서 문제인지 설계 문제인지 구분할 수 있다

#### 예상 시간 배분

- 대상별 질문 도출: 100분 (14%)
- 실습 1 (매뉴얼 3종): 300분
- 실습 2 (온보딩·관찰): 200분
- 실습 3 (KR 번역): 120분
- 문서화 및 README: 100분
- **합계**: 12h (버퍼 20% 포함)

#### 참조 자료

- M2 산출물 `guides/district-tool-approval-process.md`
- M1 산출물 `concepts/legal-frame-cipa-coppa-ferpa.md`
- 로컬 `C:\AI_study\2026\VibeLearn-AI\templates\translation_glossary.en-ko.md`
- 선례: `Topics/VibeLearn-AI/02-User-Guide/guides/quick-start-30min.md`

---

### M7 - 레포지토리 전략 확정 및 배포

**난이도**: ⭐⭐
**예상 시간**: 5h
**산출물 폴더**: `07-Repo-Strategy/`

#### 학습 목표

- [ ] 별도 레포와 단일 레포의 장단점을 기준표로 비교해 결정할 수 있다
- [ ] 신규 레포를 생성하고 M5·M6 산출물을 이전할 수 있다
- [ ] 두 레포 간 방법론 코어 동기화 규칙을 문서화할 수 있다
- [ ] 처음 클론한 사람이 README만 보고 시작할 수 있게 구성할 수 있다

#### 주요 개념

1. **결정 기준**: 대상 독자의 전제 차이 / 불필요한 자산의 소음 / 릴리스 주기 / 검토 표면 크기. 이 Topic의 사전 분석은 **별도 레포**를 권고했다 — 특히 기존 레포의 pre-commit hook·PowerShell·Python 파이프라인이 학교 IT 검토에서 승인 장벽이 된다는 점이 결정적이다.
2. **결합 유지 장치**: 레포를 나누면 방법론 코어가 갈라질 위험이 생긴다. 4단계 워크플로우와 9개 모듈 항목이 바뀌면 양쪽을 함께 고치는 규칙을 두 레포에 명문화한다.
3. **검토 표면**: 학교가 채택하려면 IT가 전체를 읽을 수 있어야 한다. 파일 수와 실행 코드가 적을수록 유리하다.

#### 실습 과제

**실습 1: 결정 기준표 작성 및 확정** ⭐⭐
- **목적**: 권고안을 검증하고 확정한다
- **단계**:
  1. 기준 5개 이상을 세우고 두 선택지를 채점
  2. 권고안(별도 레포)이 유지되는지 확인, 뒤집히면 근거 기록
  3. 결정을 ADR로 작성
- **예상 시간**: 60분
- **검증**: 나중에 "왜 나눴나"에 문서로 답변 가능

**실습 2: 신규 레포 생성 및 이전** ⭐⭐
- **목적**: 실제로 배포한다
- **단계**:
  1. GitHub에 `VibeLearn-AI-Chromebook` 레포 생성
  2. M5 프롬프트 팩·Gem 지침·Drive 템플릿, M6 매뉴얼·온보딩 이전
  3. README 작성 (EN 원본 + KR) — 30초 안에 "이게 뭐고 누구를 위한 것인지" 전달
  4. LICENSE, 초기 커밋, 푸시
- **예상 시간**: 120분
- **검증**: 클론 후 README만 보고 시작 가능

**실습 3: 동기화 규칙 문서화** ⭐⭐
- **목적**: 두 레포가 갈라지는 것을 막는다
- **단계**:
  1. 방법론 코어에 해당하는 항목 목록 확정
  2. 변경 시 양쪽 동시 수정 규칙 작성
  3. 양쪽 README에 상호 링크 추가
  4. 원본 VibeLearn-AI 레포에도 동일 규칙 반영
- **예상 시간**: 60분
- **검증**: 두 레포 어느 쪽을 봐도 다른 쪽의 존재와 관계를 알 수 있음

#### 산출물

```
07-Repo-Strategy/
├── README.md
├── decisions/
│   └── ADR-004-separate-repository.md
└── guides/
    ├── repo-sync-rules.md          # 방법론 코어 동기화 규칙
    └── migration-log.md            # 무엇을 어디서 어디로 옮겼는지
```

#### Definition of Done

**핵심 질문 — 아래에 답할 수 있으면 이 모듈은 끝난 것이다**

- [ ] Q1. 별도 레포와 단일 레포 중 무엇이 맞는가? 그 근거를 학교 IT 관점에서 설명할 수 있는가?
- [ ] Q2. **처음 클론한 사람이 README만 보고 시작할 수 있는가?**
- [ ] Q3. 두 레포의 방법론 코어가 갈라지지 않게 하려면 무엇이 필요한가?

**답을 뒷받침하는 증거**

- [ ] 결정 기준표 (기준 5개 이상, 두 선택지 채점) + ADR (근거 + **폐기된 선택지**)
- [ ] 신규 레포 생성 및 초기 푸시 완료
- [ ] README EN 원본 + KR — 30초 안에 "이게 뭐고 누구를 위한 것인지" 전달
- [ ] 방법론 코어 항목 목록 확정 + 동시 수정 규칙을 **양쪽 레포에** 명문화
- [ ] 양쪽 README 상호 링크 (어느 쪽을 봐도 다른 쪽의 존재와 관계를 알 수 있음)
- [ ] 이전 내역 기록 (무엇을 어디서 어디로)

**기록**

- [ ] README.md (학습 순서 + 상대 경로 링크 + 이전/다음 모듈 링크)
- [ ] WorkLog + Daily Retrospective

#### Self-Assessment

**개념 이해**:
- [ ] 레포를 나눈 이유를 학교 IT 관점에서 설명할 수 있다

**실무 활용**:
- [ ] 방법론이 바뀌었을 때 무엇을 어디까지 동기화할지 판단할 수 있다

**문제 해결**:
- [ ] 두 레포가 갈라졌을 때 감지하는 방법을 제시할 수 있다

#### 예상 시간 배분

- 개념 정리: 40분 (13%)
- 실습 1 (결정): 60분
- 실습 2 (레포 생성·이전): 120분
- 실습 3 (동기화 규칙): 60분
- 문서화 및 README: 20분
- **합계**: 5h (버퍼 20% 포함)

#### 참조 자료

- `vl_materials/00-Project-Plan.md` — M7 권고안 및 근거
- 원본 레포 `C:\AI_study\2026\VibeLearn-AI` 구조

---

### M8 - Remotion 영상 제작

**난이도**: ⭐⭐⭐
**예상 시간**: 16h
**산출물 폴더**: `08-Videos/`

#### 학습 목표

- [ ] 학습 과정을 서사로 재구성해 슬라이드 플랜을 작성할 수 있다
- [ ] 사용법 튜토리얼을 실제 화면 흐름에 맞춰 구성할 수 있다
- [ ] `remotion-video` 스킬의 3단계 승인 워크플로우를 준수해 렌더링할 수 있다
- [ ] KR/EN 양쪽 영상을 동등한 품질로 완성할 수 있다

#### 주요 개념

1. **3단계 승인 워크플로우**: 슬라이드 플랜 → 오디오 → 렌더링. 각 단계에서 승인을 받고 진행한다. 순서를 건너뛰면 재작업 비용이 크다.
2. **두 영상의 역할 분리**: 영상 ①은 **왜**(문제 발견과 해결 과정), 영상 ②는 **어떻게**(실제 사용법). 섞으면 둘 다 흐려진다.
3. **서사의 출처**: 영상 ①의 핵심 서사는 M3의 진단 보고서다. "이 시스템은 무엇을 전제했나 → 학교는 무엇을 제공하나 → 어디서 어긋나나 → 그래서 이렇게 만들었다".
4. **제작 스펙**: 이미지 gpt-image-2, 오디오 edge-tts. 기존 `Topics/VibeLearn-AI/03-Intro-Video/` 품질을 기준선으로 삼는다.

#### 실습 과제

**실습 1: 영상 ① 학습 과정 (KR/EN)** ⭐⭐⭐
- **목적**: 왜 이것이 필요했는지 전달한다
- **단계**:
  1. M3 진단 보고서를 서사로 재구성해 슬라이드 플랜 작성 → **승인**
  2. 스크립트 작성 후 edge-tts로 오디오 생성 → **승인**
  3. gpt-image-2로 이미지 생성, Remotion 컴포지션 구성
  4. KR/EN 렌더링
- **예상 시간**: 420분
- **검증**: MP4 재생 + 오디오 싱크 확인

**실습 2: 영상 ② 사용법 튜토리얼 (KR/EN)** ⭐⭐⭐
- **목적**: 처음 쓰는 사람이 따라할 수 있게 한다
- **단계**:
  1. M6 온보딩 문서 기반으로 슬라이드 플랜 작성 → **승인**
  2. 스크립트 + 오디오 → **승인**
  3. 실제 화면 흐름을 반영한 컴포지션 구성
  4. KR/EN 렌더링
- **예상 시간**: 420분
- **검증**: 영상만 보고 첫 Topic 생성 가능

**실습 3: 배포 준비** ⭐⭐
- **목적**: 공개 가능한 상태로 만든다
- **단계**:
  1. YouTube 메타데이터 작성 (제목·설명·태그, KR/EN)
  2. 썸네일 생성
  3. 신규 레포 README에 영상 링크 추가
- **예상 시간**: 120분
- **검증**: 업로드 직전 상태까지 완료

#### 산출물

```
08-Videos/
├── README.md
├── video1-journey/
│   ├── slides-plan.kr.md / .en.md
│   ├── script.kr.md / .en.md
│   ├── audio-kr/ , audio-en/
│   ├── images/
│   └── vibelearn-chromebook-journey-kr.mp4 / -en.mp4
├── video2-tutorial/
│   └── (동일 구조)
└── youtube-metadata.md
```

#### Definition of Done

**핵심 질문 — 아래에 답할 수 있으면 이 모듈은 끝난 것이다**

- [ ] Q1. **영상만 보고 첫 Topic을 만들 수 있는가?** (사용법 영상의 합격선)
- [ ] Q2. 왜 Chromebook판이 필요했는지가 전달되는가? (학습 과정 영상)
- [ ] Q3. 두 영상의 역할 차이를 한 문장씩으로 설명할 수 있는가?

**답을 뒷받침하는 증거**

- [ ] **3단계 승인 워크플로우 준수** — 슬라이드 플랜 → 오디오 → 렌더링, 각 단계 승인
- [ ] 영상 렌더링 완료 — **최소 사용법 1편 KR/EN**(필수), 학습 과정 1편 KR/EN(일정 여유 시)
- [ ] 오디오 싱크 및 재생 확인
- [ ] 도입부에 ED DCL 인용 "learn with – rather than exclusively from – AI" (M1 이월)
- [ ] 연방 정책 계보 + DOL Attachment II 그래픽 활용
- [ ] YouTube 메타데이터(KR/EN) + 썸네일
- [ ] 신규 레포 README에 영상 링크 추가

**기록**

- [ ] README.md (학습 순서 + 상대 경로 링크 + 이전 모듈 링크)
- [ ] WorkLog + Daily Retrospective + **Topic Retrospective**

#### Self-Assessment

**개념 이해**:
- [ ] 두 영상의 역할 차이를 한 문장씩으로 설명할 수 있다

**실무 활용**:
- [ ] 슬라이드 플랜만 보고 최종 영상의 흐름을 예측할 수 있다

**문제 해결**:
- [ ] 렌더링 실패 시 원인을 단계별로 좁힐 수 있다

#### 예상 시간 배분

- 서사 구성 및 기획: 120분 (13%)
- 실습 1 (영상 ①): 420분
- 실습 2 (영상 ②): 420분
- 실습 3 (배포 준비): 120분
- 문서화 및 README: 80분
- **합계**: 16h (버퍼 20% 포함)

> **범위 조정 1순위**: 일정이 밀리면 영상 ①을 후속 작업으로 미루고 영상 ②(사용법)만 KR/EN으로 완성한다. 사용법 영상이 채택에 더 직접적으로 기여한다.

#### 참조 자료

- `_Settings_/Skills/remotion-video/SKILL.md` — 스킬 진입점, 3단계 워크플로우
- 선례: `Topics/VibeLearn-AI/03-Intro-Video/` — 품질 기준선, KR/EN 구조
- M3 산출물 `guides/why-current-version-fails.md` — 영상 ① 서사 원본
- M6 산출물 `onboarding/` — 영상 ② 내용 원본

---

## 📝 WorkLog 작성 가이드

각 학습 세션마다 WorkLog를 작성하여 진행 상황을 추적합니다.

**파일명 규칙**: `vl_worklog/YYYYMMDD_MX_VibeLearn-AI-Chromebook.md`
- 예: `vl_worklog/20260817_M1_VibeLearn-AI-Chromebook.md`

**WorkLog 필수 섹션**:
1. 오늘의 학습 목표 (체크리스트)
2. 진행 내용 (실습별 상세 기록)
3. 문제 해결 로그
4. DoD 체크리스트 (모듈 완료 기준)
5. Daily Retrospective
6. 참조 및 산출물

**이 Topic 고유 항목**: M1·M2 진행 중에는 확인한 1차 출처 URL과 조사 일자를 WorkLog에 함께 남긴다. 나중에 정책이 바뀌었을 때 무엇을 다시 확인해야 하는지 추적하기 위함이다.

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

`vl_worklog/YYYYMMDD_VibeLearn-AI-Chromebook_Final_Retrospective.md`:
- 전체 학습 여정 통계
- VibeLearn AI 방법론 효과성 평가
- 산출물 품질 평가
- 향후 학습 개선 사항
- **추가**: `01-US-AI-Education-Policy/audiences/`를 향후 AI 교육 Topic으로 잇기 위한 인계 메모

---

## 📂 전체 폴더 구조

```
VibeLearn-AI-Chromebook/
├── topic_starter.md
├── vl_prompts/
│   ├── roadmap_prompt.md
│   └── daily_learning_prompt.md
├── vl_roadmap/
│   └── 20260816_RoadMap_VibeLearn-AI-Chromebook.md
├── vl_worklog/
│   ├── YYYYMMDD_M1_VibeLearn-AI-Chromebook.md
│   └── ...
├── vl_materials/
│   └── 00-Project-Plan.md
├── 01-US-AI-Education-Policy/
├── 02-Chromebook-Management/
├── 03-Gap-Analysis/
├── 04-Architecture-Design/
├── 05-Build/
├── 06-Manual-Onboarding/
├── 07-Repo-Strategy/
└── 08-Videos/
```

---

## 📊 학습 진행 상황 추적

| 모듈 | 시작일 | 종료일 | 상태 | DoD 달성률 | 비고 |
|------|--------|--------|------|-----------|------|
| M1 | 2026-08-16 | 2026-08-16 | ✅ | **100% (8/8)** | 1차 출처 11건 확보. 산출물 15개 문서. 후속 모듈 인계 17건. FCC CIPA만 미확보 |
| M2 | 2026-08-16 | | 🔄 | 25% (Q1/4) | 세션 1: 가부 판정표 24개 항목 완성. Q2·Q3·Q4는 세션 2. 실기기 확보 병행 |
| M3 | | | ⏳ | 0% | |
| M4 | | | ⏳ | 0% | 실기기 필요 시점 |
| M5 | | | ⏳ | 0% | 실질적 Capstone |
| M6 | | | ⏳ | 0% | 제3자 관찰 필요 |
| M7 | | | ⏳ | 0% | |
| M8 | | | ⏳ | 0% | 범위 조정 1순위 |

**범례**: ⏳ 대기 · 🔄 진행 중 · ✅ 완료

---

## 🎯 성공 기준

### 최종 질문 — 이 Topic이 성공했는지 가르는 것

- [ ] **Chromebook만 가진 미국 학생이 VibeLearn AI로 실제 학습을 완주할 수 있는가?**
- [ ] **학교가 이 도구를 승인할 수 있는가?**
- [ ] **처음 보는 사람이 혼자 시작할 수 있는가?**

### 검증 통과 기준

- [ ] 전 모듈의 핵심 질문에 답함 (M1~M8)
- [ ] **End-to-End 검증** — 로컬 파일·CLI 없이 브라우저만으로 새 Topic 완주 (M5)
- [ ] **제3자 온보딩 검증** — 방법론을 모르는 사람이 15분 내 첫 Topic 생성 (M6)
- [ ] **승인 가능성 검증** — IT 관리자용 문서가 Oklahoma 8개 루브릭 + ED DCL 5원칙을 모두 커버 (M6)
- [ ] 신규 GitHub 레포 배포, 클론 후 README만으로 시작 가능 (M7)
- [ ] 사용법 영상 KR/EN 완성 (M8)

### 기록과 자산

- [ ] 8개 산출물 폴더, 각각 README.md 포함
- [ ] Topic Retrospective 작성
- [ ] Self-Assessment 평균 ⭐⭐⭐⭐ 이상
- [ ] `audiences/` 산출물이 향후 AI 교육 활동에 재사용 가능한 상태로 정리됨 ✅ (M1 완료)

---

## ⚠️ 진행 중 관리할 위험

| 위험 | 조기 신호 | 대응 |
|---|---|---|
| 실물 Chromebook 미확보 | M2 종료 시점까지 미섭외 | M4를 Chrome 브라우저 기반으로 진행, "미검증" 표기, M6 이후 실사용 피드백으로 보정 |
| 정책 정보 노후화 | 출처 문서의 최종 수정일이 6개월 이상 경과 | 재확인 후 조사 시점 갱신, 불확실하면 "⚠️ 미확인" 표기 |
| 파일 영속성 해법 실패 | M4 실습 1에서 마찰 수치가 과도 | Drive 수동 편집 전제의 저마찰 설계로 폴백 |
| M8 일정 초과 | M7 종료가 5주차를 넘김 | 영상 ①을 후속 작업으로 이관, 영상 ②만 완성 |
| Gems 등급 제약 | 무료 Fundamentals 환경에서 Gem 사용 불가 확인 | 이미 반영됨 — 프롬프트 팩이 1차, Gem은 선택 계층 |

---

**생성자**: Claude with VibeLearn AI
**Roadmap 버전**: 1.0
**방법론 버전**: VibeLearn AI 2.0
