# VibeLearn AI Topic Starter — Senior-AI-Enablement

> 이 파일은 새로운 Topic 학습을 시작할 때 작성하는 템플릿입니다.
>
> **작성일**: 2026-10-11 (Live #31 방송 중)
> **소스**: 사용자 구상 원문 「시니어 AI 활용 시스템과 교육 과정 구상 (원문)」 (비공개 `Materials_For_Topics/Senior-AI-Enablement/`) + 10/9 방송 준비 구술 + 기존 Topic 기록
> **공개 레포 주의**: 이 폴더는 GitHub 에 공개된다. 실제 참가자·고객의 이름, 연락처, 상담 내용은 옮기지 않는다 (「유타주의 한 선생님」처럼 익명으로 쓴다).

---

## 📌 Topic 기본 정보

### Topic 이름
```
Topic 이름: Senior-AI-Enablement
(시니어를 위한 AI 활용 시스템 + 교육 과정)
```

### Topic 설명
```
설명: 컴퓨터가 낯설거나 AI 를 막 시작한 시니어가, 자기 경험과 노하우를 「내 컴퓨터의 내 기록」으로 쌓으면서
AI 와 함께 하고 싶은 일을 해 나갈 수 있도록 돕는 「시스템(프로세스 + 스킬 + 기존 도구 조합)」과
그 시스템을 익히게 하는 「교육 과정」을 함께 설계하고 시범 운영하는 Topic.
VS Code · Claude Code · VibeLearn AI 같은 기존 도구를 기본으로 하되 새 앱 개발도 선택지에 둔다(기준은 진입 장벽).
시니어가 부딪히는 어려움을 프로세스와 스킬로 낮춘다. VibeLearn AI 자체도 시니어용으로 무엇을 바꿔야 하는지 도출한다.
```

### 학습 목적
```
학습 목적:
- 시니어는 도메인 지식과 노하우가 많고, 은퇴 후 제2의 일을 찾는 분도 많다. AI 가 그 경험을 몇 배로 키워 주는 도구가 되게 한다
- 「기록을 로컬에 쌓고 AI 와 계속 이어 간다」는 접근을 시니어가 감당할 수 있는 형태로 만든다
- 지금까지 유타주 선생님·Shoreline 식당 운영 선생님·상담 고객과 해 본 실제 시도에서 드러난 부족한 부분을 메운다
- 여러 사례를 거쳐 「일반 교육 과정」을 먼저 만들고, 대상이 정해지면 그 대상에 맞게 변형하는 방식을 확립한다
```

### 예상 학습 기간
```
예상 기간: 8주 확정 (주당 6~8시간, 약 50시간) — 2026-10-11 사용자 확인
(근거: 시스템 설계 + 교육 과정 + 시범 운영이 한 Topic 에 묶여 있어 「복잡」에 해당)
```

---

## 🎯 학습 목표

```
- [ ] 시니어가 어디서 막히는지를 실제 사례(익명)와 기존 기록으로 정리한 「어려움 지도」를 만든다
- [ ] 「내 기록 공간 → 자료 준비 → VibeLearn AI 학습/프로젝트 → 가벼운 일 처리 → 보기(HTML)」로 이어지는 시스템 흐름과 구조를 설계한다
- [ ] 사전 자료(Material) 준비 프로세스와 기록 저장소 구조를 시니어가 따라 할 수 있는 형태로 만든다
- [ ] VibeLearn AI 를 쓸 필요가 없는 일(가벼운 일 처리)의 흐름을 따로 정의한다
- [ ] 문서를 md 가 아닌 보기 쉬운 형태(HTML 등)로 전달하는 방법을 정하고 시험한다
- [ ] 일반 교육 과정(개념 + 조작법)을 만들고, 대상별로 변형하는 방법을 정리한다
- [ ] 실제 시니어 1명 이상과 시범 운영한 결과로 시스템과 과정을 고친다
- [ ] VibeLearn AI 를 시니어용으로 바꿀 항목 목록을 낸다 (새 버전 여부는 별도 판단)
```

---

## 🛠️ 학습 환경

### 운영 체제
```
OS: Windows 11 (설계·제작자) / 대상자 컴퓨터: Windows · macOS 혼재 (크롬북·태블릿은 현재 방식 불가)
```

### 주요 도구 및 기술 스택
```
- VS Code · Claude Code (현재 방식의 기본 도구)
- VibeLearn AI (Topic → Roadmap → WorkLog 흐름)
- 마크다운 + HTML 변환 (옵시디언 없이 보기 위한 방법)
- Claude Code Skills / 프로세스 문서 (시스템을 구성하는 수단)
- 필요 시 Obsidian, 원격 접속(Chrome Remote Desktop 등) — 비교 대상
- 클라우드 개인 에이전트(Muse 등 무료 범위) — 입구 후보로 검토 (AI-Agent-Apps-Compare 연계, 2026-10-11 사용자 리뷰)
```

### 사전 지식 (Prerequisites)
```
필수:
- VibeLearn AI 의 Topic → Roadmap → WorkLog 흐름
- 기존 가이드북 내용 (VibeCoding-Starter-Guide)

권장:
- 실제 시니어 교육 경험(지금까지의 유타주·Shoreline 사례 기록)
- 접근성(큰 글씨 · 단순 화면)에 대한 기본 감각
```

---

## 📚 참조 자료 (Optional)

### 공식 문서
```
- (공식 문서는 M 단계에서 확인: Claude Code 설치·권한 설명, VS Code 접근성 설정)
```

### 튜토리얼 및 강의
```
- 참가자용 가이드북: Topics/VibeCoding-Starter-Guide/07-Guidebook/01-participant-guidebook.md
- 시니어를 위한 AI와 함께 앱 개발하기 (YouTube): https://youtu.be/T9BCpJ_ffzQ
```

### 관련 GitHub 저장소
```
- VibeLearn-AI: https://github.com/solkit70/VibeLearn-AI.git (로컬 C:\AI_study\2026\VibeLearn-AI)
- CatchUpAI_VL: https://github.com/solkit70/CatchUpAI_VL
```

### 추가 학습 자료
```
vl_materials/ 폴더에 추가할 자료:
- 00-구상-정리와-추가-고려사항.md — 구상 원문을 구조화하고 AI 가 추가로 제안한 고려사항 (이미 작성)
- 시니어 사례 기록(익명) · 어려움 지도 · 대상 유형별 필요 자료

기존 Topic 중 재사용할 것:
- VibeCoding-Starter-Guide (가이드북) · VibeCoding-Onboarding-Program (신청서) · Vibe-Guiding-VSCode (Guiding 엔진)
- FDE-Forward-Deployed-Engineer · AI-Agent-Apps-Compare (Muse·Dots·Grok Bot·Instinct 비교) · Materials_For_Topics 의 AI 활용 가이드 프로그램 개요(레벨 구성)
```

---

## 🎓 학습 접근 방식 (Optional)

### 선호하는 학습 스타일
```
- [ ] 이론 먼저, 실습 나중
- [x] 실습 중심, 필요한 이론만 (권장)
- [ ] 이론과 실습 병행
```

### 시간 투자 계획
```
- 주당 학습 시간: 6~8시간 (가안)
- 학습 가능 요일: 주중 + 일요일 라이브 방송
- 1회당 학습 시간: 1~3시간
```

### 특별히 집중하고 싶은 영역
```
- 「처음에 어떻게 다가갈 것인가」 — 첫 30분 안에 작은 성공을 경험하게 하는 입구
- 설치·조작 장벽을 줄이는 프로세스 (코드가 아니라 절차와 스킬로)
- 내 기록을 담는 장소와 프로세스 (현재 가장 비어 있는 부분)
- 시니어마다 관심사가 다르므로 하나의 코스가 아닌 「공통 기본 + 대상별 변형」 구조
```

### 지킬 것
```
- 판단 기준은 하나: 「시니어가 처음에 진입 장벽을 덜 느끼는가」. 스킬이든 앱이든 문서든 형태는 진행하며 정한다 (사용자 확정, 2026-10-11; 초기의 「새 앱 금지」는 철회)
- 모든 시니어를 대상으로 하지 않는다. 「기록할 만한 경험·지식이 있고 그것으로 무언가 하고 싶은 열정이 있는 분」이 중심 대상이다 (구술 10/9)
- 첫 대상은 A 유형 가능성이 크다: 오랫동안 자기 사업을 운영해 쓰던 컴퓨터 기능만 쓰는 페더럴웨이 시니어, 5명 이내 (10/11)
- 약 10일 뒤(10/21 전후) 의견 접수 모임에서 쓸 개략 설명 자료가 가장 가까운 마감이다
- 이 Topic 안에서 설계·시험을 끝내고, 완료되면 별도 GitHub Repository 로 배포하는 것이 희망이다
- 공개 레포이므로 참가자·고객의 이름과 상담 내용은 쓰지 않는다 (고객 상담 기록은 🔒 내부 자료)
- AI 가 추가한 제안은 「제안」으로 표시하고 사용자 확인 전에는 결정으로 쓰지 않는다
- 사용자 구술 원문은 Materials_For_Topics 에 그대로 두고, 이 Topic 의 문서는 거기서 파생시킨다
```

---

## 🚀 다음 단계

1. ✅ Topic 폴더 생성 — `vl_prompts/` · `vl_roadmap/` · `vl_worklog/` · `vl_materials/`
2. ✅ `vl_materials/00-구상-정리와-추가-고려사항.md` 작성
3. `vl_prompts/roadmap_prompt.md` → STEP 1 학습 기간 검토 → 사용자 확인 → 로드맵 초안 → 승인 뒤 저장
4. `vl_prompts/daily_learning_prompt.md` 로 첫 세션 시작

---

**Template Version**: 1.0
**Created by**: VibeLearn AI Methodology
