# VibeLearn AI Roadmap 생성 프롬프트

**버전**: 2.0
**생성일**: 2025-12-28
**방법론**: VibeLearn AI

---

## 📌 사용 방법

이 프롬프트는 `topic_starter.md`에서 입력한 Topic 정보를 바탕으로 학습 로드맵을 자동 생성합니다.

**사용 절차**:
1. Topic 폴더가 생성되면 이 파일이 `[TopicName]/vl_prompts/`에 복사됨
2. Topic 정보가 이미 주입된 상태
3. 이 파일 전체를 AI에게 전달하거나, 에이전트가 직접 실행하는 경우 생성된 `vl_prompts/roadmap_prompt.md`를 전체 다시 읽음
4. AI는 먼저 STEP 1의 학습 기간 적정성 검토만 수행하고 사용자 확인을 기다림
5. 사용자가 기간/범위를 확정한 후에만 STEP 2와 STEP 3을 진행하여 Roadmap을 생성하고 `vl_roadmap/YYYYMMDD_RoadMap_{Topic}.md`에 저장

**중요**: 사용자 승인 전에는 Roadmap 파일을 생성하지 마세요.

---

## [1단계] Topic 정보 (자동 주입됨)

> **주의**: 이 섹션은 `topic_starter.md`의 정보로 자동으로 채워집니다.
> 수정이 필요하면 `topic_info.md` 파일을 편집하세요.

### 기본 정보

**Topic 이름**: `VibeCoding-Starter-Guide`

**Topic 설명**:
```
컴퓨터에 익숙하지 않은 사람도 따라할 수 있는 "바이브 코딩 + VibeLearn AI 시작·활용 가이드" 문서를 만든다. 단순 설치 절차서가 아니라 ①각 도구가 무엇인지 ②바이브 코딩이 무엇인지 ③코딩만이 아니라 파일 정리·학습·프로젝트에도 쓰며 AI를 함께 일하는 동료로 대하면 훨씬 효율적이라는 것 ④VibeLearn AI를 챗봇처럼 질문/답변으로 쓰지 말고 제대로 활용하는 법 ⑤기록이 AI의 연료·컨텍스트가 되어 AI가 점점 나를 알게 된다는 것 ⑥AI에게 계획부터 세우게 하라는 것까지 담는다.

설치 기본 경로는 VS Code + Claude 유료 구독 + Claude Code 확장 + VibeLearn AI로 고정한다.

**대상 독자 3층** (모든 산출물이 지켜야 할 기준):
① 학생 — 시애틀 권역 통합한국학교 학생 1~2명. 8/15 광복절 기념식 발표를 AI로 준비하기 위해 2026-08-10~08-12 대면 세션에서 바로 세팅한다.
② 시니어·경력자 — 도메인 지식은 풍부하지만 바이브 코딩 시작이 어려운 분.
③ 시민단체 실무자 — 업무에 AI를 붙여 효율을 높이고 싶은 분.

공통 전제: IT 엔지니어가 아니며 컴퓨터에 익숙하지 않은 사람도 포함된다. 전문 용어는 최소화하고, 꼭 필요한 용어는 처음 나올 때 일상 언어로 풀어 쓴다 (예: "터미널 = 컴퓨터에게 글자로 명령을 내리는 창").

**집필 제1원칙** (VibeCoding-Onboarding-Program 로드맵에서 승계):
- 쉬운 언어: 전문 용어 최소화, 첫 등장 시 일상 언어 풀이 병기
- 한 동작 = 한 단계: "다운로드하고 설치하세요"(X) → "① 파란색 Download 버튼을 누릅니다 ② 내려받은 파일을 두 번 클릭합니다"(O)
- 체크포인트: 단계마다 "이 화면이 보이면 성공"
- 격려 + 현실: 용기를 주되 막히는 지점도 정직하게. 문제를 "오류"가 아니라 "자주 있는 일"로
- 이중 용도: 진행자가 보며 가이드할 수도, 참가자가 혼자 따라할 수도 있게

**확정 사항 (2026-08-10)**: 한국어 우선(영어판은 이후 별도) / 볼트 마크다운으로만 배포(웹페이지·PDF 범위 밖) / 로드맵 순서대로 진행.
```

**학습 목적**:
```
- 이번 주 학생 세션에서 바로 쓸 수 있는 설치 가이드를 확보한다
- 설치 이후 "그래서 이걸로 뭘 어떻게 하나"에 답하는 활용 가이드를 만든다
- AI를 챗봇이 아니라 협업 동료로 쓰는 방식(목표 구체화 → 계획부터 → 기록)을 전달한다
- 시니어·시민단체 실무자까지 같은 문서로 안내할 수 있게 한다
- AI 활용 가이드 프로그램의 Level 1 매뉴얼로 그대로 쓸 수 있게 한다
```

**예상 학습 기간**: `1-2주 (총 약 15.5시간, 7개 모듈)`

---

### 환경 및 사전 지식

**운영 체제**: `Windows 11 (집필 환경) — 가이드 독자 환경은 Windows / macOS 양쪽을 다룬다. ⚠️ 크롬북은 VS Code 데스크톱 설치가 불가하므로 진행자 매뉴얼에 위험 항목으로 명시한다.`

**주요 도구 및 기술 스택**:
```
- VS Code (코드 에디터)
- Claude 유료 구독 (Claude Code 사용에 필요)
- Claude Code 확장 (VS Code Extension)
- VibeLearn AI (학습 방법론) — https://github.com/solkit70/VibeLearn-AI
- Markdown / Obsidian (가이드 문서 작성)
```

**사전 지식**:
```
필수:
- 없음 (진행자 본인이 이미 경험한 내용을 문서화하는 작업)

권장:
- VibeLearn AI 레포 최신 구조 파악 (로컬: C:\AI_study\2026\VibeLearn-AI, HEAD 3d8c18b)
- 유타주 이선생님 세팅 동행 경험
- Build with AI 자료 (별도 Topic으로 학습 완료)
```

---

### 산출물 및 참조

**학습 목표** (달성하고 싶은 것):
```
- [ ] 컴퓨터가 낯선 사람도 혼자 따라할 수 있는 설치 가이드를 만들 수 있다 (VS Code + Claude 구독 + Claude Code)
- [ ] VibeLearn AI를 내려받아 첫 Topic을 시작하는 과정을 한 문장 수준으로 안내할 수 있다
- [ ] 바이브 코딩과 AI 협업이 무엇인지 비개발자 언어로 설명할 수 있다
- [ ] VibeLearn AI의 3단계를 "제대로" 쓰는 법(Topic 짓기·승인 게이트·DoD)을 안내할 수 있다
- [ ] 기록과 회고가 왜 AI의 연료가 되는지 실제 사례로 설득할 수 있다
- [ ] 참가자용 가이드북과 진행자용 매뉴얼로 나눠 완성할 수 있다
```

**참조 자료**:
```
**설치·활용 절차의 기준 (반드시 이쪽을 본다)**
- VibeLearn AI 로컬 클론: `C:\AI_study\2026\VibeLearn-AI` (HEAD `3d8c18b`) — `README.md`, `GETTING_STARTED.md`, `CLAUDE.md`, `templates/`
- VibeLearn AI 저장소: https://github.com/solkit70/VibeLearn-AI
  ⚠️ 볼트 사본(`Ingest/CatchUpAI_VL/`)은 구버전이므로 설치 절차의 근거로 쓰지 않는다.

**재사용 자산 (볼트)**
- `Topics/VibeLearn-AI/02-User-Guide/guides/quick-start-30min.md` — M4의 80%가 여기 있음
- `Topics/VibeLearn-AI/02-User-Guide/guides/faq.md` — Q1·Q2·Q5·Q6·Q13이 비개발자용
- `Topics/VibeLearn-AI/01-System-Overview/concepts/target-users.md` — Persona 2가 이 독자
- `Topics/VibeLearn-AI/02-User-Guide/case-studies/clearly-case.md` — 정량 성공 사례
- `Topics/The-AI-Powered-Creator/02-Records-as-Context/records-as-creator-context.md` — 기록=AI 연료 인용 뱅크 (M6 핵심)
- `Topics/Build-with-AI/01-Source-Map/easy-12-part-summary.md` Part 8 — 이미 시니어 눈높이인 바이브 코딩 설명
- `Topics/Build-with-AI/01-Source-Map/reading-notes.md` Part 2·8·9 — 고속도로 비유, 계획 먼저, "AI는 도깨비 방망이가 아니다"
- 각 Topic의 `vl_worklog/*Final_Retrospective*` — "현실" 근거
- `Topics/VibeCoding-Onboarding-Program/vl_roadmap/20260721_RoadMap_VibeCoding-Onboarding-Program.md` — 집필 원칙 원본
- `Topics/VibeCoding-Onboarding-Program/01-Application-Form/form-questions.md` — 환영 인사
- `Topics/Builders-Lounge-AI-Guide-Presentation/04-Script-Rehearsal/full-script.md` — 박창수 말투
- `Topics/Materials_For_Topics/AI-Guidance-Program/project-overview.md` — 이 Topic의 산출물이 곧 Level 1 매뉴얼
- `_Settings_/Skills/gobi-onboarding/SKILL.md` — 톤·용어표 패턴

**이번 Topic 진행 계획**
- `Topics/Materials_For_Topics/VibeCoding-Starter-Guide/20260810-topic-plan.md` — 모듈 구성과 M5·M6 상세가 여기 있다

**학생 세션 배경**
- `Topics/FedWay-Liberation-Day-2026/vl_materials/20260809-tf-kakaotalk-program-cost-and-student-participation.md`

**공식 사이트**
- VS Code: https://code.visualstudio.com
- Claude: https://claude.ai
```

**vl_materials/ 폴더**:
```
`vl_materials/` 폴더에는 아래 자료를 모은다.
- 설치 과정 스크린샷 (VS Code 설치, Claude 유료 가입, Claude Code 확장 설치·로그인)
- 학생 세션에서 실제로 막힌 지점 기록 (M3 막힘 대비 섹션에 반영)
- 참가자 피드백 및 이후 사례
```

---

## [2단계] AI에게 요청할 작업

위에 주입된 Topic 정보를 바탕으로 **VibeLearn AI 방법론**에 맞는 학습 로드맵을 생성해주세요.

---

### 🔍 STEP 1: 학습 기간 적정성 검토 (필수)

**로드맵 생성 전 반드시 수행:**

사용자가 입력한 학습 기간 `1-2주 (총 약 15.5시간, 7개 모듈)`이 해당 Topic에 적절한지 분석하고 피드백을 제공하세요.

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

**사용자 입력 기간**: 1-2주 (총 약 15.5시간, 7개 모듈)
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
- 예: `vl_worklog/20251228_M1_MCP-Basics.md`

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
├── topic_info.md              # Topic 정보 (참조)
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
│   └── (PDF, 문서, 코드 등)
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
- OS: Windows 11 (집필 환경) — 가이드 독자 환경은 Windows / macOS 양쪽을 다룬다. ⚠️ 크롬북은 VS Code 데스크톱 설치가 불가하므로 진행자 매뉴얼에 위험 항목으로 명시한다.
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
- [ ] 최소 7개 산출물 폴더 생성
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
**생성일**: 2025-12-28
**방법론**: VibeLearn AI
