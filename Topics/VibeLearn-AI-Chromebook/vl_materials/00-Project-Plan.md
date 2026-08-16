# Chromebook용 VibeLearn AI — 학습 Topic 개설 및 진행 계획

> **작성일**: 2026-08-16 · **상태**: 사용자 승인 완료, Phase 0 미착수

## 🔄 세션 재개 방법 (VS Code 재시작 후)

이 파일의 절대 경로:

```
C:\Users\dougg\.claude\plans\c-ai-study-2026-vibelearn-ai-vibelearn-a-swift-peach.md
```

새 세션에서 아래를 그대로 붙여넣으면 이 계획대로 이어서 진행한다.

```
C:\Users\dougg\.claude\plans\c-ai-study-2026-vibelearn-ai-vibelearn-a-swift-peach.md
파일을 읽고, 그 계획대로 VibeLearn-AI-Chromebook Topic 개설(Phase 0)부터 진행해 주세요.
```

**재개 시 첫 작업**: 이 계획서를 볼트 안으로 복사한다 →
`Ingest/CatchUpAI_VL/Topics/VibeLearn-AI-Chromebook/vl_materials/00-Project-Plan.md`
(Topic 폴더 생성이 Phase 0의 4단계이므로, 폴더를 만든 직후 복사한다)

**진행 상황 체크포인트**

- [ ] Phase 0 — Topic 개설 (스킬 Step 1~9)
- [ ] 계획서 볼트 복사
- [ ] Roadmap STEP 1 기간 적정성 검토 → 사용자 승인
- [ ] Roadmap 생성
- [ ] M1 → M8 순차 진행

---

## Context

VibeLearn AI(https://github.com/solkit70/VibeLearn-AI)는 CLI로 AI를 쓰는 사용자를 전제로 만들어졌다. 제작자 본인은 VS Code + Claude Code/Codex 조합을 쓴다. 그런데 미국 학교는 학생들에게 Chromebook을 지급하고, 이 환경에서는 현재 시스템을 거의 그대로 쓸 수 없다.

목표는 두 겹이다.

1. **제품**: Chromebook만 가진 미국 학생·교사가 VibeLearn AI 방법론을 쓸 수 있게 만들고, 매뉴얼·온보딩·Remotion 소개 영상까지 완성한다.
2. **역량**: 그 과정에서 **미국 교육 시스템이 AI를 어떻게 다루는지**를 체계적으로 학습해 둔다. 학습자(사용자)는 앞으로 학생뿐 아니라 시니어, 시민단체 활동가, IT 배경이 없는 성인 등 다양한 대상에게 AI 교육을 할 계획이며, 이번 Topic이 그 지식 기반의 첫 조각이 된다.

두 번째 축이 첫 번째보다 먼저 온다. **기기 제약보다 정책·규범이 설계를 더 강하게 결정하기 때문이다.** 아래 리서치가 그것을 보여준다.

### 리서치로 확인된 전제

**정책·규범 층**

| 사실 | 영향 |
|---|---|
| 美 노동부가 2026-02-13 **National AI Literacy Framework** 발표 — 5개 콘텐츠 영역(AI 원리 이해 / 활용처 탐색 / 효과적 지시 / 출력 평가 / 책임 있는 사용) + 7개 전달 원칙. 자발적 가이던스 | 학생·성인·시니어를 **하나의 프레임**으로 묶을 수 있는 공용 어휘. 사용자의 확장 계획에 정확히 맞음 |
| 2026년 6월 기준 **35개 이상 주**가 교육부 차원 공식 AI 가이던스 보유. 2026 회기에 27개 주 71개 법안, 11개 주 제정 | 전국 단일 규칙이 없음 → 제품은 "학군 정책에 맞춰 조정 가능한" 형태여야 함 |
| 학군 AI Acceptable Use Policy가 사실상 지역 표준 역할. "AI Assisted" 표기·출처 명시 의무가 일반적 | VibeLearn WorkLog에 **AI 사용 표기 필드**가 기본 탑재돼야 함 |
| CIPA(E-Rate 필터링 의무) · COPPA(13세 미만) · FERPA(학생 기록) 3중 법률 프레임 | 학생 데이터가 외부 AI로 나가는 경로 자체를 설계에서 배제해야 함 |
| **Claude은 18세 미만 사용 불가.** 부모 동의로도 예외 없음 | K-12 학생에게 Claude Code 경로가 법적으로 차단 |
| 2026-08-10부터 **Gemini in Classroom이 K-12 전 연령 확대**, 무료 Fundamentals 등급 포함(관리자 승인 필요) | 학생 트랙의 유일한 현실적 기반 |
| AI4K12 **Five Big Ideas**(Perception / Representation & Reasoning / Learning / Natural Interaction / Societal Impact) + 4단계 참여 수준 | K-12 커리큘럼 정렬 기준 |

**기기·관리 층**

| 사실 | 영향 |
|---|---|
| 관리형 Chromebook에서 Linux(Crostini)는 기본 비활성, 관리자만 해제 | 학생이 터미널·git·VS Code를 얻을 방법 없음 |
| Google Admin Console: zero-touch enrollment, OU별 강제 정책, 확장 프로그램 allowlist | 설치 기반 해법 전부 무효 |
| GoGuardian / Securly / Lightspeed가 필터링·모니터링 계층. GoGuardian Teacher는 교사가 학생 화면 실시간 열람·탭 강제 종료·화면 잠금 가능 | 학생이 쓰는 도구는 **교사가 관찰 가능한 표면** 위에 있어야 채택됨 |
| 도구 도입 전 학군 사전 승인 목록 + DPA(데이터 처리 계약) + 벤더 컴플라이언스 문서 검증 절차 | 제품에 IT 관리자용 컴플라이언스 문서가 동봉돼야 함 |
| Firebase Studio는 2026-06-22부로 신규 가입 중단(2027-03-22 종료) | 후보 제외 |
| GitHub Codespaces: 학생팩 인증 시 월 180 core-hour 무료, 브라우저 VS Code | 18세 이상 트랙 대안 |

### 확정된 방향 (사용자 결정)

- **2트랙 병행**: 학생(18세 미만) = Gemini in Classroom + Drive / 교사·성인 = claude.ai/code 또는 Codespaces
- **Topic 위치**: `Changsoo_Vault/Ingest/CatchUpAI_VL/Topics/VibeLearn-AI-Chromebook/`

---

## 산출물의 세 축

| | 학습 기록 | 최종 제품 | 재사용 지식 |
|---|---|---|---|
| 위치 | `Ingest/CatchUpAI_VL/Topics/VibeLearn-AI-Chromebook/` | 신규 GitHub 레포 `VibeLearn-AI-Chromebook` | 볼트 `Topics/` 노트 |
| 내용 | topic_info, roadmap, worklog, 모듈별 교과서 | 프롬프트 팩, 매뉴얼, 온보딩, Gem 지침, 컴플라이언스 문서 | 미국 AI 교육 정책·환경 정리, 대상별 교육 접근법 |
| 수명 | 이 Topic 한정 | 지속 배포 | 향후 AI 교육 활동 전반의 기반 |

선례: 기존 `Topics/VibeLearn-AI/`가 `01-System-Overview` → `02-User-Guide` → `03-Intro-Video`(KR/EN MP4)로 완결됐다. 같은 패턴을 따른다.

---

## Phase 0: Topic 개설 (스킬 절차 준수)

`_Settings_/Skills/vibelearn-ai/SKILL.md`의 Step 1~9를 순서대로 실행한다. 임의 파일 생성 금지 — 반드시 `Ingest/CatchUpAI_VL/templates/`의 템플릿에서 파생시킨다.

1. `templates/workflow_guide.md` 로드
2. `templates/topic_starter.md` 로드
3. Topic 정보 확정 (아래 초안)
4. 폴더 생성: `Topics/VibeLearn-AI-Chromebook/{vl_prompts,vl_roadmap,vl_worklog,vl_materials}`
5. `topic_starter.md` 작성 — 플레이스홀더 전부 채움
6. `templates/roadmap_prompt_template.md` → `{PLACEHOLDER}` 주입 → `vl_prompts/roadmap_prompt.md`. `[2단계]`·`[3단계]`는 **수정 없이 전체 유지**
7. **게이트**: `vl_prompts/roadmap_prompt.md`를 전체 다시 읽고 STEP 1(학습 기간 적정성 검토)만 수행 → **사용자 승인 전까지 `vl_roadmap/` 파일 생성 금지**
8. 승인 후 Roadmap 생성 + `vl_prompts/daily_learning_prompt.md` 생성
9. 사용자에게 Roadmap 검토 요청

### Topic 정보 초안

- **이름**: `VibeLearn-AI-Chromebook`
- **설명**: 미국 교육 시스템의 AI 사용 규범과 학교 지급 Chromebook의 관리 구조를 학습한 뒤, 그 제약 위에서 동작하는 브라우저 전용 2트랙 VibeLearn AI를 설계·구축하고, 매뉴얼·온보딩·소개 영상까지 완성한다
- **예상 기간**: 3~4주 (세션당 3~5시간) — STEP 1에서 적정성 재검토
- **환경**: Windows 11 + VS Code + Claude Code (제작), 검증 대상은 ChromeOS
- **사전 지식**: 보유 — VibeLearn AI 방법론, GitHub, Remotion 파이프라인 / 신규 — 미국 K-12 AI 정책, ChromeOS 관리 모델, Google Workspace for Education 관리, Gemini Gems

---

## Phase 1: 모듈 구성 제안 (Roadmap 초안)

각 모듈은 9개 필수 항목(기본정보/학습목표/핵심개념/실습과제/산출물/DoD/Self-Assessment/시간배분/참조자료)을 갖춘다. 실습 70~80%.

### M1 — 미국 교육환경의 AI 사용 규범

**학습 질문**: 미국 학생은 AI를 어디까지 쓰도록 권장되고 어디서 막히는가? 그 규칙은 누가 만드는가?

- 3층 구조 파악: 연방(DoL AI Literacy Framework, 권고) → 주(35개 주 가이던스, 일부는 법률) → 학군(AUP, 실제 구속력)
- 법률 프레임 CIPA / COPPA / FERPA가 각각 무엇을 금지하는지
- 주요 AI 도구 연령 게이트 비교표 (Claude 18+ / ChatGPT / Gemini for Education / Copilot)
- AI4K12 Five Big Ideas와 4단계 참여 수준 — 학년대별로 무엇을 가르치기로 돼 있는가
- 학업 정직성: "AI Assisted" 표기 관행, AI 사용 공개 규범

**추가 산출물 — 대상 확장 매핑** (사용자의 향후 AI 교육 계획 기반)
DoL 프레임워크의 5개 콘텐츠 영역을 축으로, 대상별 규범·제약·진입점을 정리한다.

| 대상 | 정리할 것 |
|---|---|
| K-12 학생 | 학교 정책, 연령 게이트, 교사 감독 전제 |
| 대학생·성인 학습자 | 도구 선택 자유도, 학업 정직성 |
| 시니어 | 진입 장벽, 기존 프로그램(Cyber-Seniors 등), 속도·용어 조정 |
| 시민단체·비IT 배경 | 업무 맥락 결합, 비용 제약, "AI 운전면허" 식 접근 |

→ `01-US-AI-Education-Policy/` (하위 `audiences/` 포함). 이 폴더는 이번 Topic이 끝나도 남는 재사용 자산이며, 향후 별도 AI 교육 Topic의 입력이 된다.

### M2 — 학교 지급 Chromebook의 관리 실체

**학습 질문**: 학교가 나눠준 Chromebook에는 무엇이 설치·강제돼 있고, 교사는 그것을 어떻게 관리하는가?

- ChromeOS 3개 런타임(Chrome / Android ARC / Linux Crostini)과 관리 정책이 각각을 어떻게 끄는지
- Google Admin Console: zero-touch enrollment, OU 구조, 강제 정책, 확장 allowlist, Chrome Education Upgrade
- 필터링·모니터링 계층 비교: GoGuardian / Securly / Lightspeed — 네트워크 레벨 vs 기기 에이전트, CIPA 준수 방식
- **교사 측 관리 도구**: GoGuardian Teacher(실시간 화면 열람, 탭 강제 종료, 화면 잠금, 채팅), Google Classroom, Gemini in Classroom 관리자 게이트
- 신규 도구 승인 절차: 학군 사전 승인 목록 → DPA → 벤더 컴플라이언스 문서 검증
- 실습: 관리형 기기에서 가능/불가능 항목을 근거와 함께 판정표로 작성

→ `02-Chromebook-Management/`

### M3 — 현재 VibeLearn AI가 막히는 지점 해부

M1·M2에서 얻은 기준으로 현 시스템 의존성을 전수 판정한다: CLI 실행, 로컬 파일시스템(`Topics/{Topic}/vl_*` 상대경로), git·`gh`, `scripts/*.ps1`·`translate-claude.py`, pre-commit hook, `CLAUDE.md` 자동 로드, VS Code 확장. 기술적 차단과 정책적 차단(18+, 도구 미승인, 데이터 반출)을 분리해 기록한다.

→ `03-Gap-Analysis/` — 사용자가 명시 요청한 "왜 현재 버전은 Chromebook에서 쓰기 힘든가" 문서

### M4 — 브라우저 전용 대안 조사 및 2트랙 아키텍처 설계

학생 트랙(Gemini in Classroom, Gems, Drive/Docs)과 성인 트랙(claude.ai/code, Codespaces)을 각각 검증·비교한다. 최대 난제인 **파일 영속성**(AI가 Roadmap을 읽고 WorkLog를 쓰는 루프를 브라우저에서 어떻게 닫는가)에 대한 결정을 ADR로 남긴다. 교사 감독 가능성과 학군 승인 용이성을 설계 제약으로 명시한다.

→ `04-Architecture-Design/`

### M5 — Chromebook판 실제 구축 (최대 모듈)

- 학생 트랙: Gem 시스템 프롬프트, Drive Topic 폴더 템플릿, 프롬프트 팩 4종(topic_starter / roadmap / daily / worklog)을 복사-붙여넣기 최소화 형태로 재작성. WorkLog에 AI 사용 표기 필드 기본 탑재
- 성인 트랙: claude.ai/code · Codespaces 진입 절차와 설정
- 기존 `templates/`에서 CLI 전제를 걷어낸 브라우저판 파생

→ 신규 레포 실체 + `05-Build/`

### M6 — 매뉴얼 + 온보딩 프로세스

학생용 / 교사용 / **학교 IT 관리자용** 3종. 관리자용에는 M1·M2에서 얻은 컴플라이언스 근거(FERPA·COPPA·CIPA 관점에서 이 도구가 무엇을 하고 안 하는지)와 사전 점검 체크리스트(Gemini 활성화, Gems 공유 허용, OU 설정)를 넣는다 — 학군 승인 절차를 통과시키기 위한 필수 자료다. 온보딩은 학생 15분 첫 Topic 경로와 교사 학급 배포 경로로 나눈다. KR + EN 병행.

→ `06-Manual-Onboarding/`

### M7 — 레포지토리 전략 확정 및 배포

> **권고: 별도 레포 `VibeLearn-AI-Chromebook`**
> ① 대상 독자와 전제가 정반대다(CLI 있음 vs 없음). 한 레포에 두면 모든 문서가 "당신이 어느 쪽이냐"부터 물어야 한다. ② 기존 레포의 pre-commit hook·PowerShell·Python 번역 파이프라인은 브라우저 사용자에게 소음이고, **학교 IT 검토 시 승인 장벽**이 된다 — 이게 결정적이다. ③ 릴리스 주기가 다르다. ④ 표면이 작아야 학군이 검토·채택한다.
> 결합 유지 장치: 양쪽 README 상호 링크 + 방법론 코어(4단계 워크플로우·9개 모듈 항목) 변경 시 동시 수정 규칙을 두 레포에 명문화.

→ GitHub 레포 생성 + 초기 푸시

### M8 — Remotion 영상 제작

`remotion-video` 스킬로 진행하며 3단계 승인(슬라이드 플랜 → 오디오 → 렌더링) 준수. 이미지 gpt-image-2, 오디오 edge-tts.
- 영상 ①: 학습 과정 — "미국 학교의 AI 환경은 이렇게 생겼고, 그래서 Chromebook판을 이렇게 만들었다"
- 영상 ②: 사용법 튜토리얼 — "Chromebook에서 VibeLearn AI 시작하기"

→ `08-Videos/` (KR/EN)

---

## 위험과 대응

| 위험 | 대응 |
|---|---|
| **실물 Chromebook 없음** — 학생 트랙 검증이 시뮬레이션에 그침 | M4 시작 전까지 실기기 확보 또는 협조 교사 섭외를 확정. 불가 시 Chrome 브라우저 + 정책 문서 기반으로 진행하되 "미검증" 표기 후 M6 이후 실사용 피드백으로 보정 |
| 정책이 주·학군마다 제각각이라 일반화 위험 | M1 산출물을 "정답표"가 아니라 **판정 기준과 확인 방법**으로 쓴다. 특정 학군 사례는 사례로만 표기 |
| 정책 정보가 빠르게 낡음 | 각 문서에 조사 시점(2026-08) 명기 + 1차 출처 링크 필수. 재확인 방법을 함께 기록 |
| Gems가 무료 Fundamentals 등급에 없음 | 학생 트랙을 **프롬프트 팩 우선**으로 설계, Gem은 선택 계층 |
| 브라우저에서 파일 루프가 안 닫힘 | M4의 핵심 결정 사항. Drive 수동 편집 전제의 저마찰 설계가 폴백 |
| Gemini의 파일·코드 도구가 Claude Code보다 약함 | 학생 트랙을 "코딩"이 아닌 **학습 기록·회고** 중심 축소 워크플로우로 재정의 |

---

## 검증 방법

- **Phase 0**: `Topics/VibeLearn-AI-Chromebook/` 4개 폴더 + `topic_starter.md` + `vl_prompts/roadmap_prompt.md` 생성 확인. `roadmap_prompt.md`에 `{PLACEHOLDER}` 잔여물이나 literal `` `n `` 없는지 grep
- **M1·M2**: 모든 주장에 1차 출처(정부·벤더 공식 문서) 링크가 붙어 있는지. 2차 블로그만 근거인 항목은 미확인으로 표기
- **모듈별**: 각 모듈 README.md가 학습 순서대로 번호 매긴 문서 목록 + 상대경로 링크 + 이전/다음 모듈 링크를 갖추는지 (CLAUDE.md 규정)
- **M5 end-to-end**: Chrome 브라우저에서 프롬프트 팩만 써서 새 Topic 하나를 처음부터 끝까지 완주 (로컬 파일·CLI 일절 금지)
- **M6**: 방법론을 모르는 제3자에게 온보딩 문서만 주고 15분 내 첫 Topic 생성 관찰
- **M7**: 신규 레포 클론 후 README만 보고 시작 가능한지
- **M8**: 렌더링 MP4 재생 + 자막·오디오 싱크 확인

## 볼트 규칙 준수

- 학습 진행에 따라 `AI/Tasks/Task Board.md` 동기화
- 커밋 메시지는 CatchUpAI_VL 관례 (`설명 - YYYY-MM-DD`)
- 위키 링크는 실존 파일만, 섹션 링크 우선
- M1의 `audiences/` 산출물은 향후 AI 교육 Topic으로 이어지도록 볼트 `Topics/` 노트에서 링크
