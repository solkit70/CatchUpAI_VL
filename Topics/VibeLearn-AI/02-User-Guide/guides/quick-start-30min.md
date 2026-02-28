# VibeLearn AI — 30분 Quick Start 가이드

**작성일**: 2026-02-26
**대상**: VibeLearn AI를 처음 접하는 사람 (GitHub 경험 있다고 가정)
**목표**: 이 가이드를 따라하면 30분 안에 첫 학습 세션을 시작할 수 있다

---

## 시작하기 전에: 필요한 것

| 필요 | 있나요? |
|------|---------|
| AI 도구 (Claude Code, Cursor, VS Code + Copilot 등) | ✅/❌ |
| 배우고 싶은 주제 (아무거나) | ✅/❌ |
| GitHub 계정 (선택 — 없어도 됨) | ✅/❌ |

**최소 요건**: AI 도구 + 배우고 싶은 주제 → 이 두 가지만 있으면 됩니다.

---

## Step 1: VibeLearn AI 저장소 받기 (5분)

### Option A: GitHub 클론 (권장)

```bash
git clone https://github.com/solkit70/VibeLearn-AI.git
cd VibeLearn-AI
```

### Option B: ZIP 다운로드

1. https://github.com/solkit70/VibeLearn-AI → 초록색 Code 버튼 클릭
2. "Download ZIP" 선택 → 압축 해제
3. 폴더 이름: `VibeLearn-AI/`

### 완료 확인

다음 파일들이 있어야 합니다:
```
VibeLearn-AI/
├── README.md         ← 방법론 전체 설명
├── GETTING_STARTED.md
└── templates/
    ├── topic_starter.md
    ├── roadmap_prompt_template.md
    └── daily_learning_prompt.md
```

---

## Step 2: AI 도구에서 폴더 열기 (2분)

**VS Code + GitHub Copilot** (가장 보편적):
1. VS Code에서 `VibeLearn-AI/` 폴더 열기
2. GitHub Copilot 확장 설치 확인 (Extensions에서 "GitHub Copilot" 검색)
3. Copilot Chat 패널 (`Ctrl+Alt+I`) 열기

**VS Code + Claude Code** (Extension):
1. VS Code에서 `VibeLearn-AI/` 폴더 열기
2. Claude Code 확장 패널 활성화

**Cursor**:
1. Cursor에서 `VibeLearn-AI/` 폴더 열기

**Claude Code (CLI)**:
```bash
cd VibeLearn-AI
claude
```

---

## Step 3: 배우고 싶은 주제 말하기 (3분)

AI에게 다음을 말하세요:

```
"[주제]를 배우고 싶어.
VibeLearn AI 방법론으로 시작을 도와줘.

현재 위치: [VibeLearn-AI 폴더 경로]
예상 기간: [기간]"
```

**실제 예시**:
```
"Python 기초를 배우고 싶어.
VibeLearn AI 방법론으로 시작을 도와줘.

현재 위치: ~/VibeLearn-AI
예상 기간: 2주"
```

**AI가 하는 일**:
- 몇 가지 질문으로 학습 정보 수집 (목표, 환경 등)
- `Topics/Python-Basics/` 폴더 구조 자동 생성
- `topic_info.md` 작성
- 다음 단계 안내

---

## Step 4: Roadmap 생성 (10분)

AI가 폴더를 만들면, 이어서 말하세요:

```
"Roadmap을 생성해줘."
```

AI가 자동으로:
1. `Topics/Python-Basics/vl_prompts/roadmap_prompt.md` 읽기
2. 학습 기간 적정성 검토 + 피드백
3. 모듈별 Roadmap 생성
4. `vl_roadmap/20260226_RoadMap_Python-Basics.md` 저장

**소요 시간**: 약 5-10분

---

## Step 5: 첫 학습 세션 시작 (10분)

Roadmap이 완성되면:

```
"M1 학습을 시작해줘.
사용 가능한 시간: 2시간"
```

AI가:
1. M1 Roadmap 내용 확인
2. 오늘의 학습 계획 수립
3. 계획 제시 → 당신의 승인 대기
4. 승인 후 → `vl_worklog/20260226_M1_Python-Basics.md` 생성하며 학습 시작

---

## 30분 타임라인 요약

```
00:00 ─── Step 1: 저장소 받기 (5분)
00:05 ─── Step 2: AI 도구에서 폴더 열기 (2분)
00:07 ─── Step 3: 주제 말하기 → 폴더 생성 (3분)
00:10 ─── Step 4: Roadmap 생성 (10분)
00:20 ─── Step 5: 첫 학습 계획 수립 (10분)
00:30 ─── 첫 학습 세션 시작! 🎉
```

---

## 다음 학습부터는 이렇게 시작하세요

매일 학습 시작 시:

```
"오늘 학습을 시작해줘.
Topic: Python-Basics
현재 모듈: M2
가용 시간: 1.5시간
최근 WorkLog: vl_worklog/20260226_M1_Python-Basics.md"
```

AI가:
1. Roadmap + 이전 WorkLog 읽기
2. 오늘의 계획 수립
3. 계획 승인 후 학습 시작

---

## 자주 막히는 곳 & 해결책

### "AI가 폴더를 만들지 못해요"
- VS Code + GitHub Copilot, Claude Code, Cursor처럼 파일 시스템 접근이 가능한 AI 도구가 필요합니다
- ChatGPT 웹은 파일을 직접 생성하지 못합니다 → 에디터 통합 AI 도구 사용 필요

### "Roadmap이 너무 길어요"
- "M1만 먼저 시작하자" → 처음 모듈만 집중하세요
- 모든 모듈을 처음부터 완벽히 이해할 필요 없습니다

### "WorkLog를 어디에 써야 하나요?"
- AI가 자동으로 만들어줍니다
- 직접 편집하고 싶으면 VS Code에서 `vl_worklog/` 폴더의 파일을 열어 수정하세요

### "내 진도가 맞는지 모르겠어요"
- Roadmap의 DoD(Definition of Done) 체크리스트를 확인하세요
- 체크가 다 되면 다음 모듈로 이동

---

## 더 자세히 알고 싶다면

- [VibeLearn AI란?](../../01-System-Overview/concepts/what-is-vibelearn-ai.md) — 시스템 전체 개념
- [4단계 워크플로우](../../01-System-Overview/concepts/workflow-diagram.md) — 전체 프로세스 이해
- [템플릿 시스템 가이드](../../01-System-Overview/guides/template-system.md) — 각 파일의 역할
- [GETTING_STARTED.md](../../../../GETTING_STARTED.md) — 공식 상세 가이드

---

**작성자**: Claude with VibeLearn AI
**검증**: 이 가이드는 실제 VibeLearn-AI Topic 학습 과정에서 검증됨
