# VibeLearn AI Roadmap 생성 프롬프트

**버전**: 2.0
**생성일**: 2026-08-16
**방법론**: VibeLearn AI
**Topic**: VibeLearn-AI-Chromebook

---

## 📌 사용 방법

이 프롬프트는 `topic_starter.md`에서 입력한 Topic 정보를 바탕으로 학습 로드맵을 자동 생성합니다.

**사용 절차**:
1. Topic 폴더가 생성되면 이 파일이 `[TopicName]/vl_prompts/`에 복사됨
2. Topic 정보가 이미 주입된 상태
3. 이 파일 전체를 AI에게 전달
4. AI가 VibeLearn AI 표준 로드맵 생성
5. 생성된 로드맵을 `vl_roadmap/YYYYMMDD_RoadMap_{Topic}.md`에 저장

---

## [1단계] Topic 정보 (자동 주입됨)

> **주의**: 이 섹션은 `topic_starter.md`의 정보로 자동으로 채워집니다.
> 수정이 필요하면 `topic_starter.md` 파일을 편집하세요.

### 기본 정보

**Topic 이름**: `VibeLearn-AI-Chromebook`

**Topic 설명**:
```
미국 교육 시스템의 AI 사용 규범과 학교 지급 Chromebook의 관리 구조를 학습한 뒤,
그 제약 위에서 실제로 동작하는 브라우저 전용 2트랙 VibeLearn AI를 설계·구축하고,
매뉴얼·온보딩 프로세스·소개 영상까지 완성한다.

배경: VibeLearn AI는 CLI로 AI를 쓰는 사용자(VS Code + Claude Code/Codex)를
전제로 만들어졌다. 그런데 미국 학교는 학생들에게 Chromebook을 지급하고,
이 환경에서는 현재 시스템을 거의 그대로 쓸 수 없다.
```

**학습 목적**:
```
- 미국 학생이 AI를 어디까지 쓰도록 권장되고 어디서 막히는지, 그 규칙을 누가
  만드는지를 연방·주·학군 3층 구조로 이해한다 (향후 AI 교육 활동의 기반)
- 학교 지급 Chromebook에 무엇이 강제돼 있고 교사가 그것을 어떻게 관리하는지
  실체를 파악한다
- 그 제약 위에서 Chromebook만 가진 학생·교사가 실제로 쓸 수 있는 VibeLearn AI를
  만들어 배포한다
- 학생뿐 아니라 시니어·시민단체 활동가·비IT 배경 성인까지 확장 가능한
  AI 교육 지식 자산을 남긴다
```

**예상 학습 기간**: `3-4주 (세션당 3-5시간, 주당 15-20시간)`

---

### 환경 및 사전 지식

**운영 체제**: `Windows 11 (제작 환경) / 검증 대상은 ChromeOS 관리형 Chromebook`

**주요 도구 및 기술 스택**:
```
제작 측:
- VS Code + Claude Code
- Git / GitHub (신규 레포 VibeLearn-AI-Chromebook 생성 예정)
- Remotion (remotion-video 스킬, 이미지 gpt-image-2 + 오디오 edge-tts)

조사·검증 대상:
- ChromeOS 관리 스택 (Google Admin Console, OU 정책, 확장 allowlist)
- Google Workspace for Education (Classroom, Drive, Gemini in Classroom, Gems)
- 필터링·모니터링 (GoGuardian / Securly / Lightspeed)
- claude.ai/code (Claude Code on the web)
- GitHub Codespaces
```

**사전 지식**:
```
필수:
- VibeLearn AI 방법론 (제작자 본인, 완전 숙지)
- GitHub 기본 사용법
- Markdown 문서 작성

권장:
- Remotion 영상 파이프라인 경험 (보유 — Topics/VibeLearn-AI/03-Intro-Video)
- 기존 VibeLearn-AI Topic 완주 경험 (보유)

신규 학습 필요:
- 미국 K-12 AI 정책 지형 (연방·주·학군 3층)
- CIPA / COPPA / FERPA 법률 프레임
- ChromeOS 관리 모델 및 Google Admin Console
- Google Workspace for Education 관리자 설정
- Gemini Gems 작성·공유
```

---

### 산출물 및 참조

**학습 목표** (달성하고 싶은 것):
```
- [ ] 미국의 AI 교육 규범을 연방(DoL AI Literacy Framework) → 주(35개 이상 주
      가이던스) → 학군(AUP) 3층으로 구분해 설명할 수 있다
- [ ] CIPA·COPPA·FERPA가 각각 무엇을 금지하는지, 학생 대상 AI 도구 설계에
      어떤 제약을 만드는지 설명할 수 있다
- [ ] 관리형 Chromebook에서 무엇이 가능하고 무엇이 차단되는지 근거와 함께
      판정표로 제시할 수 있다
- [ ] 교사가 GoGuardian 등으로 학생 기기를 어떻게 관리하는지 설명하고, 그것이
      도구 설계에 주는 제약을 반영할 수 있다
- [ ] 현재 VibeLearn AI가 Chromebook에서 막히는 지점을 기술적 차단과 정책적
      차단으로 분리해 문서화할 수 있다
- [ ] 브라우저 전용 2트랙(학생=Gemini / 성인=Claude·Codespaces) 아키텍처를
      설계하고 그 결정 근거를 ADR로 남길 수 있다
- [ ] Chromebook판 VibeLearn AI를 실제로 구축하고, 로컬 파일·CLI 없이
      새 Topic 하나를 처음부터 끝까지 완주시킬 수 있다
- [ ] 학생용·교사용·IT 관리자용 매뉴얼과 15분 온보딩 프로세스를 만들 수 있다
- [ ] Remotion으로 학습 과정 영상과 사용법 튜토리얼 영상을 제작할 수 있다
```

**참조 자료**:
```
정책·규범:
- US DoL National AI Literacy Framework (2026-02-13): 5개 콘텐츠 영역 + 7개 전달 원칙
- State K-12 AI Policy in 2026 (ExcelinEd): https://excelined.org/2026/05/26/state-k-12-ai-policy-in-2026-milestones/
- Legislative Tracker: 2026 State AI in Education Bills (FutureEd): https://www.future-ed.org/legislative-tracker-2026-state-ai-in-education-bills/
- AI4K12 Five Big Ideas: https://ai4k12.org/
- Vetting Generative AI Tools for Use in Schools (FPF): https://fpf.org/wp-content/uploads/2024/10/Ed_AI_legal_compliance.pdf_FInal_OCT24.pdf
- Claude 최소 연령 정책: https://support.claude.com/en/articles/13117299-minimum-age-requirement-access-restriction
- Gemini in Google Classroom 전 연령 확대 (2026-08-10): https://workspaceupdates.googleblog.com/2026/08/gemini-in-google-classroom-is-expanding-to-users-of-all-ages-with-contextualized-Gemini-starter-prompts-for-students.html

기기·관리:
- Privacy & Security (Google for Education): https://edu.google.com/intl/ALL_us/our-values/privacy-security/
- K-12 Web Filter Comparison 2026: https://kybergate.com/blog/k12-web-filter-comparison-guide-2026/
- GoGuardian Admin: https://www.goguardian.com/at-home-filtering-allows-complete-content-filtering-for-chromebooks-in-school-or-at-home.html

대안 플랫폼:
- Claude Code on the web: https://code.claude.com/docs/en/claude-code-on-the-web
- GitHub Codespaces with Classroom: https://docs.github.com/en/education/manage-coursework-with-github-classroom/integrate-github-classroom-with-an-ide/using-github-codespaces-with-github-classroom
- Firebase Studio (2026-06-22 신규 가입 중단 — 제외 근거): https://firebase.google.com/docs/studio

저장소:
- VibeLearn AI (원본): https://github.com/solkit70/VibeLearn-AI — 로컬 C:\AI_study\2026\VibeLearn-AI
- CatchUpAI_VL (학습 기록): https://github.com/solkit70/CatchUpAI_VL

기존 케이스:
- Topics/VibeLearn-AI/ — 01-System-Overview → 02-User-Guide → 03-Intro-Video(KR/EN) 구조 선례
- Topics/Remotion-VideoCreation/ — 영상 제작 파이프라인
```

**vl_materials/ 폴더**:
```
- 00-Project-Plan.md — 이 Topic의 전체 계획서. 사전 리서치로 확인된 전제
  (정책층·기기층 사실 표), 모듈 구성 제안 M1~M8, 위험과 대응, 검증 방법 포함.
  로드맵 생성 시 이 문서를 우선 참조할 것
- 수집한 주·학군 AI 정책 원문 및 캡처 (M1 진행 중 추가)
- Admin Console / 필터링 도구 설정 화면 참조 자료 (M2 진행 중 추가)
```

---

### ⚠️ 이 Topic 고유의 로드맵 설계 제약

일반 기술 학습 Topic과 다른 점이 있으므로 로드맵 생성 시 반영할 것:

1. **정책 학습이 기술 학습보다 먼저 온다.** 기기 제약보다 정책·규범이 설계를 더
   강하게 결정한다. M1(정책) → M2(기기 관리) → M3(갭 분석) 순서를 유지한다.
2. **M1·M2의 "실습"은 코딩이 아니다.** 1차 출처 확인 → 판정표·비교표 작성으로
   정의한다. 실습 70-80% 원칙은 "직접 조사하고 표를 만든다"로 충족한다.
3. **모든 정책 주장에 1차 출처 링크와 조사 시점(2026-08)을 남긴다.** 2차 블로그만
   근거인 항목은 "미확인"으로 표기한다.
4. **실물 Chromebook 미보유가 알려진 위험이다.** M4 시작 전까지 실기기 확보 또는
   협조 교사 섭외가 필요하며, 불가 시 "미검증" 표기 후 진행한다.
5. **마지막 모듈은 Capstone이 아니라 영상 제작(Remotion)이다.** 실질적 Capstone은
   M5(실제 구축)이며, M8은 결과물을 알리는 단계다.

---

## [2단계] AI에게 요청할 작업

위에 주입된 Topic 정보를 바탕으로 **VibeLearn AI 방법론**에 맞는 학습 로드맵을 생성해주세요.

---

### 🔍 STEP 1: 학습 기간 적정성 검토 (필수)

**로드맵 생성 전 반드시 수행:**

사용자가 입력한 학습 기간 `3-4주 (세션당 3-5시간, 주당 15-20시간)`이 해당 Topic에 적절한지 분석하고 피드백을 제공하세요.

#### 분석 기준:
1. **Topic 복잡도 평가**
   - 간단 (예: CLI 도구, 기본 개념): 3-7일 적정
   - 중간 (예: 프레임워크, 라이브러리): 2-4주 적정
   - 복잡 (예: 대규모 시스템, 다중 기술): 1-3개월 적정

2. **사전 지식 고려**
   - 사전 지식이 충분: 기간 단축 가능
   - 사전 지식 부족: 기간 연장 필요

3. **학습 목표 범위**
   - 기본 이해 수준: 짧은 기간
   - 실무 적용 수준: 중간 기간
   - 전문가 수준: 긴 기간

#### 피드백 형식:

```markdown
## 📊 학습 기간 적정성 분석

**사용자 입력 기간**: 3-4주 (세션당 3-5시간, 주당 15-20시간)
**Topic 복잡도**: [간단/중간/복잡]
**권장 기간**: [X주 또는 Y일]

**분석 결과**:
- ✅ **적정함**: 입력하신 기간이 이 Topic 학습에 적합합니다.
- ⚠️ **너무 짧음**: 이 Topic은 일반적으로 [권장 기간]이 필요합니다. 현재 기간으로는 핵심만 빠르게 학습하게 됩니다.
- ⚠️ **너무 김**: 이 Topic은 보통 [권장 기간]이면 충분합니다. 여유 있게 학습하거나 심화 내용까지 다룰 수 있습니다.

**조치 제안**:
- [적정함인 경우] 계획대로 진행합니다.
- [너무 짧은 경우] 1) 기간 연장 권장 또는 2) 학습 범위 축소 (기본만)
- [너무 긴 경우] 1) 기간 단축 또는 2) 심화 내용 추가

**사용자 확인 필요**:
위 분석 결과를 확인하시고 다음 중 선택해주세요:
1. "그대로 진행" - 입력한 기간으로 진행
2. "기간 조정" - 권장 기간으로 변경
3. "범위 조정" - 기간은 유지하되 학습 범위 조정
```

**중요**: 사용자가 확인하고 최종 결정할 때까지 로드맵 생성을 중단하고 대기하세요.

---

### 🗺️ STEP 2: 로드맵 생성 요구사항

사용자가 기간을 최종 확정한 후 아래 요구사항에 따라 로드맵을 생성하세요.

#### 전체 구조

**학습 기간**: `{최종 확정된 기간}`에 맞춰 조정
- 3일 이하: 3-5개 모듈
- 1-2주: 5-7개 모듈
- 1개월 이상: 7-10개 모듈

**모듈 구성 원칙**:
- 각 모듈은 독립적으로 완료 가능한 단위
- 난이도는 점진적 상승 (Basics → Intermediate → Advanced)
- 마지막 모듈은 Capstone 프로젝트 (통합 실습)

**명명 규칙**:
- 모듈: `M1`, `M2`, `M3`, ...
- 산출물 폴더: `01-{TopicName}/`, `02-{TopicName}/`, ...

---

#### 각 모듈 필수 포함 사항

각 모듈은 다음 9가지 항목을 반드시 포함해야 합니다:

##### 1. 모듈 기본 정보
```markdown
### MX - {모듈명}

**난이도**: ⭐/⭐⭐/⭐⭐⭐ (1-3)
**예상 시간**: X시간
**산출물 폴더**: `0X-{모듈명}/`
```

##### 2. 학습 목표 (3-5개)
- 검증 가능하게 작성 ("~을 이해한다" X, "~을 구현할 수 있다" O)
- 체크리스트 형식 `- [ ]`
- 구체적이고 측정 가능한 목표

##### 3. 주요 개념
- 핵심 용어 정의 (3-5개)
- 각 개념에 대한 1-2문장 설명
- 오해하기 쉬운 포인트 명시

##### 4. 실습 과제 (2-3개)
각 실습마다:
- **과제명**: 명확한 이름
- **목적**: 왜 이 실습을 하는가
- **단계**: 구체적인 실행 단계 (1, 2, 3, ...)
- **예상 시간**: X분
- **난이도**: ⭐/⭐⭐/⭐⭐⭐
- **검증 방법**: 성공 여부를 어떻게 확인하는가

##### 5. 산출물
- 생성할 폴더 구조
- 필수 파일 목록 (README.md, 코드, 문서 등)
- 권장 하위 폴더 (`concepts/`, `examples/`, `guides/`, `troubleshooting/`)

##### 6. Definition of Done (완료 기준)
체크리스트 형식으로 5-8개:
```markdown
- [ ] 모든 학습 목표 달성
- [ ] 실습 과제 X개 완료
- [ ] 핵심 명령어/API Y개 실행 성공
- [ ] 산출물 폴더 생성 및 README 작성
- [ ] WorkLog 작성 완료
- [ ] Daily Retrospective 작성
```

##### 7. Self-Assessment (자가 평가)
AI 시대에 맞는 평가 기준 (3-5문항):
```markdown
**개념 이해** (5분):
- [ ] 이 기술/기능이 무엇인지 1-2문장으로 설명 가능
- [ ] 왜 필요한지 예시와 함께 설명 가능

**실무 활용** (5분):
- [ ] AI에게 이 기술을 사용한 작업 요청 가능
- [ ] AI가 생성한 코드의 품질 판단 가능

**문제 해결** (5분):
- [ ] 문제 발생 시 AI에게 디버깅 방향 제시 가능
```

##### 8. 예상 시간 배분
```markdown
- 개념 학습: X분 (20-30%)
- 실습 1: X분
- 실습 2: X분
- 문서화: X분
- **합계**: X시간 (버퍼 20% 포함)
```

##### 9. 참조 자료
- 공식 문서 링크 (필수)
- 튜토리얼/예제 (권장)
- 각 링크마다 1줄 설명

---

#### 실습 설계 원칙 (중요!)

실습 과제를 설계할 때 다음 원칙을 **반드시** 준수하세요:

##### 1. 실습 우선
- 이론 설명: 20-30%
- 실습 시간: 70-80%
- "개념 설명 → 즉시 실습" 패턴 반복

##### 2. 점진적 복잡도
- 실습 1: 간단 (⭐) - "Hello World" 수준
- 실습 2: 중간 (⭐⭐) - 실용적 기능
- 실습 3: 고급 (⭐⭐⭐) - 선택사항, 심화

##### 3. 검증 가능성
- 모든 실습은 실행 결과로 성공 여부 확인 가능
- 예: "로그 출력", "파일 생성", "API 응답 성공"
- 명확한 성공 기준 제시

##### 4. AI 시대 학습 범위
**인간이 알아야 할 것**:
- 개념적 이해 (무엇, 왜, 언제)
- 아키텍처 및 구조
- AI에게 효과적으로 지시하는 방법
- 기본 사용 패턴 (3-5개 핵심 기능)

**암기 불필요**:
- 상세 API 파라미터 목록
- 모든 옵션과 플래그
- 내부 구현 디테일

##### 5. 산출물 중심
- 매 모듈마다 폴더 생성 (`01-xxx/`, `02-xxx/`)
- **"교과서 품질"**: 다른 학습자가 이것만으로 학습 가능한 수준
- **README.md는 반드시 포함** — 아래 내용을 갖춰야 함:
  - 모듈 번호/제목/상태/예상 학습 시간 헤더
  - 이 폴더의 모든 문서를 **학습 순서대로** 번호 매겨 나열
  - 각 문서에 **상대 경로 링크** (예: `[concepts/overview.md](concepts/overview.md)`)
  - 각 문서마다 1줄 설명 (무엇을 배우는 문서인지)
  - 이전/다음 모듈 링크
  - **처음 이 폴더를 여는 사람이 README만 보고 순서대로 학습 가능한 수준**

##### 6. 환경 고려
- 사용자가 입력한 OS/도구에 맞는 명령어 사용
- Windows: PowerShell 명령어
- macOS/Linux: Bash 명령어
- 경로 표기도 OS에 맞게 조정

---

#### VibeLearn AI 방법론 통합

로드맵에 다음 VibeLearn AI 요소들을 통합하세요:

##### 1. WorkLog 가이드
```markdown
## WorkLog 작성 가이드

각 학습 세션마다 WorkLog를 작성하여 진행 상황을 추적합니다.

**파일명 규칙**: `vl_worklog/YYYYMMDD_MX_{Topic}.md`
- 예: `vl_worklog/20260817_M1_VibeLearn-AI-Chromebook.md`

**WorkLog 필수 섹션**:
1. 오늘의 학습 목표 (체크리스트)
2. 진행 내용 (실습별 상세 기록)
3. 문제 해결 로그
4. DoD 체크리스트 (모듈 완료 기준)
5. Daily Retrospective
6. 참조 및 산출물
```

##### 2. Retrospective 가이드
```markdown
## Retrospective 가이드

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
`vl_worklog/YYYYMMDD_{Topic}_Final_Retrospective.md`:
- 전체 학습 여정 통계
- VibeLearn AI 방법론 효과성 평가
- 산출물 품질 평가
- 향후 학습 개선 사항
```

##### 3. 폴더 구조
```
{Topic}/
├── topic_starter.md           # Topic 정보 (참조)
├── vl_prompts/
│   ├── roadmap_prompt.md      # 이 파일
│   └── daily_learning_prompt.md
├── vl_roadmap/
│   └── YYYYMMDD_RoadMap_{Topic}.md  # 생성될 로드맵
├── vl_worklog/
│   ├── YYYYMMDD_M1_{Topic}.md
│   ├── YYYYMMDD_M2_{Topic}.md
│   └── ...
├── vl_materials/              # Optional: 참조 자료
│   └── 00-Project-Plan.md
├── 01-{Module1}/
│   ├── README.md
│   ├── concepts/
│   ├── examples/
│   ├── guides/
│   └── troubleshooting/
├── 02-{Module2}/
└── ...
```

---

#### 모듈 구성 예시 (참고용)

아래는 일반적인 학습 Topic의 모듈 구성 예시입니다 (Topic에 따라 조정):

**M1 - 개요 및 핵심 개념**
- Topic이 무엇이고 왜 필요한지
- 주요 용어 및 아키텍처 이해
- "Hello World" 수준의 첫 실습

**M2 - 환경 설정**
- 개발 환경 구축
- 필수 도구 설치 및 검증
- 프로젝트 스캐폴딩

**M3 - 기초 기능**
- 핵심 기능 3-5개 학습
- 기본 사용 패턴
- 간단한 예제 구현

**M4 - 중급 기능**
- 고급 기능 활용
- 실제 시나리오 적용
- 에러 처리 및 디버깅

**M5 - 통합 및 응용**
- 기존 프로젝트에 통합
- 실무 패턴 적용
- 성능 최적화 (선택)

**M6 - 배포 및 문서화** (선택)
- 프로덕션 배포
- 문서 작성
- 팀 공유 준비

**MX (마지막) - Capstone 프로젝트**
- 모든 학습 내용 통합
- 완전한 프로젝트 구현
- 최종 산출물 완성

> **이 Topic 적용 시**: 위 예시는 일반 기술 학습용이다. 이 Topic은
> `vl_materials/00-Project-Plan.md`의 "Phase 1: 모듈 구성 제안"(M1~M8)을
> 기준으로 삼고, 위 예시는 각 모듈의 9개 항목 작성 형식 참고용으로만 쓴다.

---

## [3단계] 출력 형식

다음 Markdown 형식으로 로드맵을 생성하고 `vl_roadmap/YYYYMMDD_RoadMap_{Topic}.md`에 저장하세요.

### 로드맵 템플릿 구조

```markdown
# {Topic} 학습 로드맵

**생성일**: YYYY-MM-DD
**방법론**: VibeLearn AI
**버전**: 1.0

---

## 📚 학습 개요

### Topic 소개
{Topic 설명}

### 학습 목표
{topic_starter.md의 학습 목표}

### 예상 학습 기간
{입력한 기간}

### 학습 환경
- OS: {OS}
- 도구: {기술 스택}
- 사전 지식: {Prerequisites}

---

## 🗺️ 전체 로드맵 구조

| 모듈 | 모듈명 | 난이도 | 예상 시간 | 산출물 폴더 |
|------|--------|--------|----------|------------|
| M1 | {모듈명} | ⭐ | Xh | 01-{이름}/ |
| M2 | {모듈명} | ⭐⭐ | Xh | 02-{이름}/ |
| ... | ... | ... | ... | ... |

**총 예상 시간**: X시간

---

## 📖 모듈별 상세 계획

### M1 - {모듈명}

**난이도**: ⭐
**예상 시간**: Xh
**산출물 폴더**: `01-{모듈명}/`

#### 학습 목표
- [ ] 목표 1
- [ ] 목표 2
- [ ] 목표 3

#### 주요 개념
1. **개념1**: 설명
2. **개념2**: 설명
3. **개념3**: 설명

#### 실습 과제

**실습 1: {과제명}** ⭐
- **목적**: {목적}
- **단계**:
  1. 단계 1
  2. 단계 2
  3. 단계 3
- **예상 시간**: X분
- **검증**: {검증 방법}

**실습 2: {과제명}** ⭐⭐
{동일 형식}

#### 산출물
```
01-{모듈명}/
├── README.md              ← 학습 순서 안내 + 전체 문서 링크 (필수)
├── concepts/
│   └── concept1.md
├── examples/
│   └── example1.py
└── guides/
    └── guide1.md
```

> **README.md 작성 기준**: 이 폴더를 처음 여는 학습자가 README만 보고
> 어떤 문서를 어떤 순서로 읽어야 하는지 즉시 알 수 있어야 합니다.
>
> **필수 포함 내용**:
> 1. 모듈 헤더 (번호, 제목, 상태, 예상 학습 시간)
> 2. 학습 순서대로 번호 매긴 문서 목록 + 상대 경로 링크 + 1줄 설명
> 3. 이전/다음 모듈 링크
>
> **예시**:
> ```markdown
> ## 📚 학습 순서
> 1. [concepts/overview.md](concepts/overview.md) — 전체 개념 개요
> 2. [concepts/detail.md](concepts/detail.md) — 핵심 개념 상세
> 3. [examples/hello.py](examples/hello.py) — 첫 번째 실습
> 4. [guides/setup.md](guides/setup.md) — 환경 설정 가이드
> ```

#### Definition of Done
- [ ] 항목 1
- [ ] 항목 2
- [ ] 항목 3
- [ ] 항목 4
- [ ] 항목 5

#### Self-Assessment
**개념 이해**:
- [ ] 질문 1
- [ ] 질문 2

**실무 활용**:
- [ ] 질문 3
- [ ] 질문 4

#### 예상 시간 배분
- 개념 학습: X분
- 실습 1: X분
- 실습 2: X분
- 문서화: X분
- **합계**: Xh

#### 참조 자료
- [공식 문서](URL): 설명
- [튜토리얼](URL): 설명

---

{M2, M3, ... 동일 형식으로 반복}

---

## 📝 WorkLog 작성 가이드

{위의 WorkLog 가이드 내용}

---

## 🔍 Retrospective 가이드

{위의 Retrospective 가이드 내용}

---

## 📂 전체 폴더 구조

{위의 폴더 구조 내용}

---

## 📊 학습 진행 상황 추적

| 모듈 | 시작일 | 종료일 | 상태 | DoD 달성률 | 비고 |
|------|--------|--------|------|-----------|------|
| M1 | | | ⏳ | 0% | |
| M2 | | | ⏳ | 0% | |
| ... | | | | | |

**범례**:
- ⏳ 대기
- 🔄 진행 중
- ✅ 완료

---

## 🎯 성공 기준

전체 Topic 완료 기준:
- [ ] 모든 모듈 완료 (DoD 100%)
- [ ] 최소 {N}개 산출물 폴더 생성
- [ ] Topic Retrospective 작성
- [ ] Self-Assessment 평균 ⭐⭐⭐⭐ 이상
- [ ] Capstone 프로젝트 완성

---

**생성자**: Claude with VibeLearn AI
**Roadmap 버전**: 1.0
**방법론 버전**: VibeLearn AI 2.0
```

---

## ✅ 로드맵 품질 체크리스트

생성된 로드맵이 다음 기준을 충족하는지 확인하세요:

### 구조
- [ ] 학습 기간에 맞는 적절한 모듈 개수
- [ ] 점진적 난이도 상승 (Basics → Advanced)
- [ ] 마지막 Capstone 모듈 포함
- [ ] 각 모듈의 독립성 확보

### 각 모듈
- [ ] 학습 목표 3-5개 (검증 가능)
- [ ] 주요 개념 3-5개 (명확한 정의)
- [ ] 실습 과제 2-3개 (구체적 단계)
- [ ] 산출물 구조 명시
- [ ] DoD 체크리스트 5-8개
- [ ] Self-Assessment 3-5문항
- [ ] 시간 배분 명시 (버퍼 포함)
- [ ] 참조 자료 링크
- [ ] 9가지 필수 항목 모두 포함

### VibeLearn AI 통합
- [ ] WorkLog 가이드
- [ ] Retrospective 가이드 (3단계)
- [ ] 폴더 구조 명시
- [ ] 진행 상황 추적 테이블

### 실습 설계
- [ ] 실습 우선 (70-80% 실습, 20-30% 이론)
- [ ] 검증 가능한 결과
- [ ] 환경 고려 (OS별 명령어)
- [ ] AI 시대 학습 범위 적용
- [ ] 산출물 = 교과서 품질

---

## 🎯 최종 체크

로드맵 생성 완료 후:

1. [ ] `vl_roadmap/YYYYMMDD_RoadMap_{Topic}.md` 파일로 저장
2. [ ] 전체 모듈 개수 확인 (기간에 맞는가?)
3. [ ] 품질 체크리스트 검증
4. [ ] 사용자에게 로드맵 검토 요청
5. [ ] 피드백 반영 및 조정
6. [ ] 첫 번째 모듈(M1) 시작 준비

---

**생성자**: Claude with VibeLearn AI
**Template 버전**: 2.0
**생성일**: 2026-08-16
**방법론**: VibeLearn AI
