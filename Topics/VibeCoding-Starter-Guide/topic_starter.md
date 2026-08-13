# VibeLearn AI Topic Starter

---

## 📌 Topic 기본 정보

### Topic 이름

```
Topic 이름: VibeCoding-Starter-Guide
```

### Topic 설명

```
설명: 컴퓨터에 익숙하지 않은 사람도 따라할 수 있는 "바이브 코딩 + VibeLearn AI 시작·활용
가이드" 문서를 만든다. 단순 설치 절차서가 아니라 ①각 도구가 무엇인지 ②바이브 코딩이
무엇인지 ③코딩만이 아니라 파일 정리·학습·프로젝트에도 쓰며 AI를 함께 일하는 동료로
대하면 훨씬 효율적이라는 것 ④VibeLearn AI를 챗봇처럼 쓰지 말고 제대로 활용하는 법
⑤기록이 AI의 연료·컨텍스트가 된다는 것 ⑥AI에게 계획부터 세우게 하라는 것까지 담는다.
설치 기본 경로는 VS Code + Claude 유료 구독 + Claude Code 확장 + VibeLearn AI로 고정한다.
```

### 대상 독자 (이 Topic의 모든 산출물이 지켜야 할 기준)

```
3층 독자를 하나의 문서로 감당한다.

① 학생 — 시애틀 권역 통합한국학교 중고등 학생 1~2명
   8/15 광복절 기념식 발표를 AI로 준비하기 위해 이번 주 대면 세션에서 바로 세팅한다.
② 시니어·경력자 — 도메인 지식은 풍부하지만 바이브 코딩 시작이 어려운 분
   자기 분야 지식을 앱·제품으로 만들어 보고 싶다.
③ 시민단체 실무자 — 업무에 AI를 붙여 효율을 높이고 싶은 분
   "AI로 뭘 만들까"보다 "내 일을 AI와 어떻게 할까"가 관심사다.

→ 공통 전제: IT 엔지니어가 아니다. 컴퓨터가 익숙한 젊은 학생도 있지만, 컴퓨터에
  익숙하지 않은 분도 포함된다. 모든 문서·용어·절차를 이 기준에 맞춘다.
  전문 용어는 최소화하고 꼭 필요한 용어는 처음 나올 때 일상 언어로 풀어 쓴다.
  (예: "터미널 = 컴퓨터에게 글자로 명령을 내리는 창")

**언어 (2026-08-10 확정)**: 한국어 우선으로 완성한다. 영어판은 이후 별도 진행한다.
**배포 (2026-08-10 확정)**: 볼트 마크다운으로만 배포한다. 웹페이지·PDF는 범위 밖.
```

### 학습 목적

```
학습 목적:
- 이번 주 학생 세션에서 바로 쓸 수 있는 설치 가이드를 확보한다
- 설치 이후 "그래서 이걸로 뭘 어떻게 하나"에 답하는 활용 가이드를 만든다
- AI를 챗봇이 아니라 협업 동료로 쓰는 방식(목표 구체화 → 계획부터 → 기록)을 전달한다
- 시니어·시민단체 실무자까지 같은 문서로 안내할 수 있게 한다
- AI 활용 가이드 프로그램의 Level 1 매뉴얼로 그대로 쓸 수 있게 한다
```

### 예상 학습 기간

```
예상 기간: 1-2주 (총 약 15.5시간, 7개 모듈)
  단, 학생 세션이 2026-08-10~08-12로 임박해 M1 → M3 → M4(약 6.5시간)가
  실제 설치에 필요한 최소 묶음이다.
```

---

## 🎯 학습 목표

```
- [ ] 컴퓨터가 낯선 사람도 혼자 따라할 수 있는 설치 가이드를 만들 수 있다 (VS Code + Claude 구독 + Claude Code)
- [ ] VibeLearn AI를 내려받아 첫 Topic을 시작하는 과정을 한 문장 수준으로 안내할 수 있다
- [ ] 바이브 코딩과 AI 협업이 무엇인지 비개발자 언어로 설명할 수 있다
- [ ] VibeLearn AI의 3단계를 "제대로" 쓰는 법(Topic 짓기·승인 게이트·DoD)을 안내할 수 있다
- [ ] 기록과 회고가 왜 AI의 연료가 되는지 실제 사례로 설득할 수 있다
- [ ] 참가자용 가이드북과 진행자용 매뉴얼로 나눠 완성할 수 있다
```

**권장**: 3-5개의 명확하고 검증 가능한 목표

---

## 🛠️ 학습 환경

### 운영 체제

```
OS: Windows 11 (집필 환경)
    가이드 독자 환경은 Windows / macOS 양쪽을 다룬다.
    ⚠️ 크롬북은 VS Code 데스크톱 설치가 불가 — 진행자 매뉴얼에 위험 항목으로 명시
```

### 주요 도구 및 기술 스택

```
- VS Code (코드 에디터)
- Claude 유료 구독 (Claude Code 사용에 필요)
- Claude Code 확장 (VS Code Extension)
- VibeLearn AI (학습 방법론) — https://github.com/solkit70/VibeLearn-AI
- Markdown / Obsidian (가이드 문서 작성)
```

### 사전 지식 (Prerequisites)

```
필수:
- 없음 (진행자 본인이 이미 경험한 내용을 문서화하는 작업)

권장:
- VibeLearn AI 레포 최신 구조 파악 (로컬: C:\AI_study\2026\VibeLearn-AI, HEAD 3d8c18b)
- 유타주 이선생님 세팅 동행 경험
- Build with AI 자료 (별도 Topic으로 학습 완료)
```

---

## 📚 참조 자료

### 공식 문서

```
- Catch Up AI 웹사이트: https://catchupai.net/ (가이드 맨 앞·맨 뒤에 소개)
- VibeLearn AI 저장소: https://github.com/solkit70/VibeLearn-AI
- VibeLearn AI 로컬 클론: C:\AI_study\2026\VibeLearn-AI (설치 절차의 기준 — 볼트 사본은 구버전)
- VS Code: https://code.visualstudio.com
- Claude: https://claude.ai

영상 (본문 인용 시 링크 병기 — 전체 목록은 vl_materials/video-references.md):
- VibeLearn AI 소개 (한국어): https://youtu.be/rbc-6b0woJU
- VibeLearn AI Intro (영어, 영어판 가이드용): https://youtu.be/KAcTebGpU5M
- Build with AI 쉽게 보기 (한국어): https://youtu.be/T9BCpJ_ffzQ
- 시민단체를 위한 AI: https://youtu.be/IsmHWee25Ag
- 기록이 AI를 강하게 만든다 (Live #13 요약): https://youtu.be/eL2TOtFXJNI
```

### 관련 내부 문서

```
- 이번 Topic 진행 계획: Topics/Materials_For_Topics/VibeCoding-Starter-Guide/20260810-topic-plan.md
- AI 활용 가이드 프로그램 Level 1: Topics/Materials_For_Topics/AI-Guidance-Program/project-overview.md
- 집필 원칙 원본: Topics/VibeCoding-Onboarding-Program/vl_roadmap/20260721_RoadMap_VibeCoding-Onboarding-Program.md
- 설치 가이드 재사용: Topics/VibeLearn-AI/02-User-Guide/guides/quick-start-30min.md, faq.md
- 정량 성공 사례: Topics/VibeLearn-AI/02-User-Guide/case-studies/clearly-case.md
- 기록=AI 연료 인용 뱅크: Topics/The-AI-Powered-Creator/02-Records-as-Context/records-as-creator-context.md
- 비개발자 눈높이 설명: Topics/Build-with-AI/01-Source-Map/easy-12-part-summary.md
- 고속도로 비유·계획 먼저: Topics/Build-with-AI/01-Source-Map/reading-notes.md
- 학생 세션 배경: Topics/FedWay-Liberation-Day-2026/vl_materials/20260809-tf-kakaotalk-program-cost-and-student-participation.md
```

### 추가 학습 자료

```
vl_materials/ 폴더 자료:
- video-references.md (작성 완료) — 가이드에 인용할 영상 링크 모음.
  본문에서 영상을 언급할 때는 반드시 이 표의 링크를 함께 넣는다.
- 설치 과정 스크린샷 (VS Code, Claude 가입, Claude Code 확장)
- 학생 세션에서 실제로 막힌 지점 기록
- 참가자 피드백
```

---

## 🎓 학습 접근 방식

### 선호하는 학습 스타일

```
- [x] 실습 중심, 필요한 이론만 (권장)
```

### 시간 투자 계획

```
- 주당 학습 시간: 유동적 (필요할 때마다 진행)
- 1회당 학습 시간: 1-3시간
```

### 특별히 집중하고 싶은 영역

```
- 이번 주: M1(뼈대·용어사전) → M3(설치) → M4(VibeLearn 설치)를 우선 확보
- 전체: M5·M6의 "제대로 활용하는 법"을 레포 원문과 실제 회고 기록에 근거해 쓸 것
       (추측 금지 — 모든 주장에 출처를 붙인다)
- 최종 기준: 모든 산출물이 "대상 독자가 읽고 바로 이해되는가"를 통과할 것
```

---

**Template Version**: 1.0
**작성일**: 2026-08-10
