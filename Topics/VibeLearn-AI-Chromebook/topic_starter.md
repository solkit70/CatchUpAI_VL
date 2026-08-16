# VibeLearn AI Topic Starter — VibeLearn-AI-Chromebook

**방법론**: VibeLearn AI v2.0
**생성일**: 2026-08-16
**상태**: 🔄 Roadmap 대기

---

## 📌 Topic 기본 정보

### Topic 이름

```
Topic 이름: VibeLearn-AI-Chromebook
```

### Topic 설명

```
설명: 미국 교육 시스템의 AI 사용 규범과 학교 지급 Chromebook의 관리 구조를
학습한 뒤, 그 제약 위에서 실제로 동작하는 브라우저 전용 2트랙 VibeLearn AI를
설계·구축하고, 매뉴얼·온보딩 프로세스·소개 영상까지 완성한다.
```

### 학습 목적

```
학습 목적:
- 미국 학생이 AI를 어디까지 쓰도록 권장되고 어디서 막히는지, 그 규칙을 누가
  만드는지를 연방·주·학군 3층 구조로 이해한다 (향후 AI 교육 활동의 기반)
- 학교 지급 Chromebook에 무엇이 강제돼 있고 교사가 그것을 어떻게 관리하는지
  실체를 파악한다
- 그 제약 위에서 Chromebook만 가진 학생·교사가 실제로 쓸 수 있는 VibeLearn AI를
  만들어 배포한다
- 학생뿐 아니라 시니어·시민단체 활동가·비IT 배경 성인까지 확장 가능한
  AI 교육 지식 자산을 남긴다
```

### 예상 학습 기간

```
예상 기간: 3-4주 (세션당 3-5시간)
```

---

## 🎯 학습 목표

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

---

## 🛠️ 학습 환경

### 운영 체제

```
OS: Windows 11 (제작 환경)
검증 대상: ChromeOS (관리형 Chromebook)
```

### 주요 도구 및 기술 스택

```
제작 측:
- VS Code + Claude Code
- Git / GitHub (신규 레포 VibeLearn-AI-Chromebook 생성 예정)
- Remotion (remotion-video 스킬, gpt-image-2 + edge-tts)

조사·검증 대상:
- ChromeOS 관리 스택 (Google Admin Console, OU 정책, 확장 allowlist)
- Google Workspace for Education (Classroom, Drive, Gemini in Classroom, Gems)
- 필터링·모니터링 (GoGuardian / Securly / Lightspeed)
- claude.ai/code (Claude Code on the web)
- GitHub Codespaces
```

### 사전 지식 (Prerequisites)

```
필수:
- VibeLearn AI 방법론 (제작자 본인, 완전 숙지)
- GitHub 기본 사용법
- Markdown 문서 작성

권장:
- Remotion 영상 파이프라인 경험 (보유 — Topics/VibeLearn-AI/03-Intro-Video)
- 기존 VibeLearn-AI Topic 완주 경험 (보유)

신규 학습 필요:
- 미국 K-12 AI 정책 지형 (연방·주·학군)
- CIPA / COPPA / FERPA 법률 프레임
- ChromeOS 관리 모델 및 Admin Console
- Google Workspace for Education 관리자 설정
- Gemini Gems 작성·공유
```

---

## 📚 참조 자료

### 정책·규범 (M1)

```
- US DoL National AI Literacy Framework (2026-02-13): 5개 콘텐츠 영역 + 7개 전달 원칙
- State K-12 AI Policy in 2026 (ExcelinEd): https://excelined.org/2026/05/26/state-k-12-ai-policy-in-2026-milestones/
- Legislative Tracker: 2026 State AI in Education Bills (FutureEd): https://www.future-ed.org/legislative-tracker-2026-state-ai-in-education-bills/
- AI4K12 Five Big Ideas: https://ai4k12.org/
- Vetting Generative AI Tools for Use in Schools (Future of Privacy Forum): https://fpf.org/wp-content/uploads/2024/10/Ed_AI_legal_compliance.pdf_FInal_OCT24.pdf
- Claude 최소 연령 정책: https://support.claude.com/en/articles/13117299-minimum-age-requirement-access-restriction
- Gemini in Google Classroom 전 연령 확대 (2026-08-10): https://workspaceupdates.googleblog.com/2026/08/gemini-in-google-classroom-is-expanding-to-users-of-all-ages-with-contextualized-Gemini-starter-prompts-for-students.html
```

### 기기·관리 (M2)

```
- Privacy & Security (Google for Education): https://edu.google.com/intl/ALL_us/our-values/privacy-security/
- K-12 Web Filter Comparison 2026: https://kybergate.com/blog/k12-web-filter-comparison-guide-2026/
- GoGuardian Admin (Chromebook 필터링): https://www.goguardian.com/at-home-filtering-allows-complete-content-filtering-for-chromebooks-in-school-or-at-home.html
```

### 대안 플랫폼 (M4)

```
- Claude Code on the web: https://code.claude.com/docs/en/claude-code-on-the-web
- GitHub Codespaces with GitHub Classroom: https://docs.github.com/en/education/manage-coursework-with-github-classroom/integrate-github-classroom-with-an-ide/using-github-codespaces-with-github-classroom
- Firebase Studio (2026-06-22 신규 가입 중단 — 제외 근거): https://firebase.google.com/docs/studio
```

### 관련 GitHub 저장소

```
- VibeLearn AI (원본, 배포용): https://github.com/solkit70/VibeLearn-AI
  로컬: C:\AI_study\2026\VibeLearn-AI
- CatchUpAI_VL (학습 기록): https://github.com/solkit70/CatchUpAI_VL
- VibeLearn-AI-Chromebook (M7에서 신규 생성 예정)
```

### 기존 학습 케이스 (참고용)

```
- Topics/VibeLearn-AI/ — 01-System-Overview → 02-User-Guide → 03-Intro-Video(KR/EN)
  구조 선례. 이번 Topic이 따르는 패턴
- Topics/Remotion-VideoCreation/ — 영상 제작 파이프라인
```

### vl_materials/ 폴더

```
vl_materials/ 폴더에 추가할 자료:
- 00-Project-Plan.md — 이 Topic의 전체 계획서 (사전 리서치 근거 포함)
- 수집한 주·학군 AI 정책 원문 및 캡처
- Admin Console / 필터링 도구 설정 화면 참조 자료
```

---

## 🎓 학습 접근 방식

### 선호하는 학습 스타일

```
- [ ] 이론 먼저, 실습 나중
- [x] 실습 중심, 필요한 이론만 (권장)
- [ ] 이론과 실습 병행
```

단, M1·M2는 성격상 조사·정리 비중이 높다. 이 두 모듈의 "실습"은 코딩이 아니라
**1차 출처 확인 → 판정표·비교표 작성**으로 정의한다.

### 시간 투자 계획

```
- 주당 학습 시간: 15-20시간
- 페이스: 집중적으로 빠르게
- 1회당 학습 시간: 3-5시간
```

### 특별히 집중하고 싶은 영역

```
- 미국 AI 교육 환경의 구조적 이해 (향후 학생·시니어·시민단체 대상
  AI 교육 활동의 지식 기반)
- 정책 제약을 회피가 아니라 설계 입력으로 다루기
- 학교 IT 관리자가 승인할 수 있는 수준의 컴플라이언스 문서 작성
- 영상 완성도 (기존 VibeLearn AI 소개 영상 수준)
```

---

## ⚠️ 알려진 제약 (Topic 시작 시점)

```
- 실물 Chromebook 미보유 → M4 시작 전까지 실기기 확보 또는 협조 교사 섭외 필요.
  불가 시 "미검증" 표기 후 진행
- Claude은 18세 미만 사용 불가 → K-12 학생 트랙에서 Claude 경로 배제
- Gems는 유료 Workspace for Education 등급에만 번들 → 학생 트랙은
  프롬프트 팩 우선, Gem은 선택 계층
- 정책 정보는 빠르게 낡음 → 모든 문서에 조사 시점(2026-08) 명기 + 1차 출처 링크
```

---

## 🎯 최종 산출물

```
1. Topics/VibeLearn-AI-Chromebook/01~08/  : 모듈별 교과서 품질 문서
2. 신규 GitHub 레포 VibeLearn-AI-Chromebook : 프롬프트 팩, 매뉴얼, 온보딩,
   Gem 지침, IT 관리자용 컴플라이언스 문서
3. 01-US-AI-Education-Policy/audiences/    : 대상별(학생·성인·시니어·시민단체)
   AI 교육 접근법 — 이번 Topic 이후에도 재사용되는 자산
4. 08-Videos/                              : Remotion 제작 KR/EN 영상 2편
```

---

**Topic 소유자**: Catch Up AI (solkit70@gmail.com)
**방법론**: VibeLearn AI v2.0
