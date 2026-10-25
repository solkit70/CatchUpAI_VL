# VibeLearn AI Topic Starter

> 이 파일은 새로운 Topic 학습을 시작할 때 작성하는 템플릿입니다.
>
> **사용 방법**:
> 1. 이 파일을 복사하여 `[TopicName]_topic_starter.md`로 저장
> 2. 아래 항목들을 채워서 작성
> 3. AI에게 이 파일을 전달하여 Topic 폴더 구조 생성 요청
> 4. 생성된 폴더에서 학습 시작!

---

## 📌 Topic 기본 정보

### Topic 이름
**형식**: 영문, 하이픈 또는 언더스코어 사용 (공백 없음)
**예시**: `MCP-Basics`, `Docker_Fundamentals`, `FastAPI-Tutorial`

```
Topic 이름: Muse-My-Workflow
```

### Topic 설명
**목적**: 이 Topic이 무엇인지 한두 문장으로 설명

```
설명: Meta Muse 를 박창수의 작업 전체에 맞춰 쓰는 방법을 찾는다. 밖(휴대폰 · 음성)과
집(Obsidian 볼트 · Claude Code)을 끊김 없이 잇는 해법을 실험으로 찾아 매일 쓰는 사용법과
규칙으로 굳히고, 그 과정을 영상과 다른 사람을 위한 AI 교육 재료로 만든다.

개정: v1 (2026-10-18) 「노트북이 없을 때 Muse 로 일하고 집에서 볼트로 옮기기」
→ v2 (2026-10-25 박창수) 볼트와 Muse 를 잇는 해법 찾기 · 과정 영상 · 교육 커리큘럼 활용을 더함
```

### 학습 목적
**왜 이것을 배우는가?**

```
학습 목적:
- 밖에서는 Muse 로 일하고 집에서는 볼트로 이어 가는 흐름을 만든다 — 원격으로 집 컴퓨터를 조종(Chrome Remote Desktop 등)할 필요가 없게 한다 (2026-10-14 박창수 구술)
- Muse 는 사용자에게 클라우드 컴퓨터 한 대를 주는 것과 같다. 대부분 md 로 된 볼트를 Muse 쪽과 자동 · 수동으로 맞추거나 private GitHub 로 함께 보게 해서, 집과 밖에서 중단 없이 일할 수 있는 가능한 최대한의 해법을 찾는다 (2026-10-25 박창수)
- 박창수의 작업 가운데 Muse 에 맡기면 좋은 일 · 초안만 맡길 일 · 맡기면 안 되는 일을 근거와 함께 가른다
- 찾은 방법을 시험으로 끝내지 않고, 매일 쓰는 사용 가이드 · 프롬프트 모음 · 규칙으로 굳힌다
- 이 과정을 영상으로 만들고, 여기서 배운 노하우를 다른 사람을 위한 AI 교육 커리큘럼을 만들 때 쓸 수 있게 정리한다 (2026-10-25 박창수)
```

### 예상 학습 기간
**현실적으로 예상되는 기간**

```
예상 기간: 6주 (2026-10-18 ~ 11/29, 주당 4~5시간) — 제안값, 기간 확인 단계에서 조정.
처음 확정한 2주(총 약 9시간)는 1주차에 M1 만 끝났고 범위가 넓어져(2026-10-25) 다시 검토한다.
남은 학습 약 15시간 + 1주일 실제 사용 + 영상 제작. 일요일 라이브 방송을 학습 세션으로 쓴다.
```

---

## 🎯 학습 목표

**이 Topic을 완료했을 때 달성하고 싶은 구체적 목표**

```
- [x] 박창수의 작업 목록을 만들고, 작업마다 Muse 적합도(맡김 / 초안만 / 맡기지 않음)를 근거와 함께 판정한다 (M1, 2026-10-18)
- [ ] 직접 써서 확인한 사실(음성 입력 · 메일 · 캘린더 · 알림)과 늘어난 커넥터로 적합도 지도와 연결 규칙을 보강한다
- [ ] Muse ↔ 볼트 옮기기(밖 → 집, 집 → 밖)와 VibeLearn AI 지시 따르기를 직접 시험해, 되는 것 · 안 되는 것을 이유와 함께 기록한다
- [ ] 볼트 연결 해법(클라우드 저장소 사본 · private GitHub · 원격 콘솔 · 데스크톱 앱 등)을 「끊김 없는 시나리오」로 비교하고, 내부 자료를 지키는 범위에서 가장 끊김 없는 조합을 골라 실제로 가동한다
- [ ] 1주일 실제 사용 기록을 남기고, 매일 쓰는 「집 ↔ 밖」 사용 가이드 · 프롬프트 모음 · 규칙을 만든다
- [ ] 배운 것을 다른 사람을 가르칠 때 쓰는 교육 블록(레벨별 수업 카드 · 실습 · 안전 규칙 · 막힐 때 FAQ)으로 정리한다
- [ ] 이 과정을 한 · 영 영상으로 만든다
```

**권장**: 3-5개의 명확하고 검증 가능한 목표

---

## 🛠️ 학습 환경

### 운영 체제
```
OS: Windows 11 (집 PC — i7-1355U · 16GB RAM · GPU 없음) + 휴대폰 (밖에서 Muse 사용)
버전: Meta Muse 무료 — 웹 · 휴대폰 앱 (2026-10-11 Live #31 에서 설치). Windows 데스크톱 앱은 2026-10-07 발표, 출시 전
```

### 주요 도구 및 기술 스택
**이 Topic 학습에 필요한 도구들**

```
- Meta Muse (무료 · 웹 / 휴대폰) — 커넥터: Gmail · Google Calendar (직접 사용 확인), Dropbox · GitHub 등 (시험 예정)
- Obsidian 볼트 (박창수의 2nd Brain)
- VS Code + Claude Code / Codex — Roadmap 은 Claude Code, 일일 학습은 Claude Code 와 Codex 를 함께 쓴다 (2026-10-18 박창수)
- 볼트 연결 시험용 (설치 · 생성 · 연결 전에 박창수 확인): Dropbox 무료 · GitHub private 레포 · Claude Code 웹 / 휴대폰 앱 · Python (볼트 사본 만들기 스크립트)
- GitHub (CatchUpAI_VL 공개 레포)
- Remotion (AI/RemotionStudio — 과정 영상)
- gobi-cli (Builders Lounge 글 작업 비교용)
```

### 사전 지식 (Prerequisites)
**이 Topic을 학습하기 전에 알아야 할 것**

```
필수:
- Muse 설치와 기본 사용 — Live #31 에서 완료 (가상 과제 2개)
- 박창수의 볼트 구조와 작업 흐름 (Roundup · Journal · Initiatives · VibeLearn AI Topic)

권장:
- VibeLearn AI 방법론 (topic_starter → Roadmap → 일일 학습)
- 내부 자료 규칙 — visibility: internal · 🔒 표시 문서는 볼트 밖으로 내보내지 않는다
- Claude-Code-Mobile-Remote-Execution Topic — 「모바일은 조작 콘솔, 실행은 집 PC」 원격 방식 (2026-08 검증)
- remotion-video 스킬 — 영상 제작 3단계 승인 (슬라이드 플랜 → 오디오 → 렌더링)
```

---

## 📚 참조 자료 (Optional)

### 공식 문서
```
- Meta — Introducing Muse (Secure VM · Sentinel · 기억): https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/
- Meta Help — How Muse works with Connectors: https://www.meta.com/help/artificial-intelligence/1687253048996149/
- Meta Help — How to manage your Muse data (System Files · 내려받기 · 학습 끄기): https://www.meta.com/help/superintelligence/2225571704857152/
- Meta — Everything We Announced at Meta Connect 2026 (Mac 컴퓨터 사용 · GitHub 등 새 커넥터): https://www.meta.com/blog/meta-connect-2026-everything-we-announced/
- Dropbox Help — Connect Dropbox to Meta Muse: https://help.dropbox.com/integrations/connect-to-meta-muse
- Windows Experience Blog — Muse for Windows 예정 (2026-10-07): https://blogs.windows.com/windowsexperience/2026/10/07/building-windows-for-hybrid-intelligence/
```

### 튜토리얼 및 강의
```
- 이 레포의 이전 Topic: Topics/AI-Agent-Apps-Compare/ (M3 Muse 설치 · 첫 사용, M6 영상)
- 이 레포의 이전 Topic: Topics/Claude-Code-Mobile-Remote-Execution/ (원격 콘솔 세 가지 — 비교 기준)
- 이 레포의 교육 과정 Topic: Topics/Senior-AI-Enablement/06-Curriculum-v1/ (레벨별 코스 · 수업 카드 형식 — 교육 블록 참고)
```

### 관련 GitHub 저장소
```
- CatchUpAI_VL (VibeLearn AI 공개 레포): https://github.com/solkit70/CatchUpAI_VL
```

### 추가 학습 자료
**파일, 문서, 동영상 등을 `vl_materials/` 폴더에 저장 가능**

```
vl_materials/ 폴더에 추가할 자료:
- 아이디어 원문 요약 — Journal/2026-10-14 「밖에서는 Muse, 집에서는 내 2nd Brain」 · 2026-10-18 「차 안은 음성, 행사장 · 카페는 문자」 · 2026-10-25 「볼트를 Muse 와 이어 붙이기」
- 2026-10-25 볼트 연결 해법 첫 조사 — 공식 자료 링크 · 확인 날짜 (M4 출발점)
- Muse 화면 · 내보내기 결과 캡처 (개인 정보 가림)
- 1주일 실제 사용 기록
- 영상 재료 목록 (모듈마다 WorkLog 에서 모은다)
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
- 주당 학습 시간: 4~5시간
- 학습 가능 요일: 일요일 라이브 방송 + 박창수 일정에 맞춰 (밖에 있는 시간에 Muse 실사용)
- 1회당 학습 시간: 1~2시간
```

### 특별히 집중하고 싶은 영역
```
- 실제 내 일에 쓰는 것 — 시험용 가상 과제는 처음 확인할 때만 쓴다
- 볼트와 Muse 를 잇는 가장 끊김 없는 방법 — 한 도구로 다 하려 하지 않고 작업 종류마다 맞는 길을 고른다
- Muse 에 올리면 안 되는 것(내부 자료 · 의뢰인 정보 · 개인 정보 · 다른 사람 정보)의 기준과 연결 규칙
- 영상과 교육에 쓸 재료를 진행하면서 함께 남긴다 — 막힌 곳 · 쉬운 설명 · 화면 · 수치
```
