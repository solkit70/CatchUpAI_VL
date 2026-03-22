# VibeLearn AI — 30분 Quick Start 가이드
> **[-> English Version](quick-start-30min.en.md)**


**작성일**: 2026-02-26
**대상**: VibeLearn AI를 처음 접하는 사람
**목표**: 이 가이드를 따라하면 30분 안에 첫 학습 세션을 시작할 수 있다

---

## 핵심 메시지

> **이 방법론을 배울 필요가 없습니다.**
> "Python 기초를 배우고 싶어"라고 말하는 것만으로 충분합니다.
> AI가 나머지를 알아서 처리합니다.

**설계 원칙**: VibeLearn AI는 처음 사용자의 진입 장벽을 최소화하도록 설계되었습니다.
만약 AI가 자동으로 처리하지 않는다면, 설계대로 작동하지 않는 것입니다 →
[Issues 리포트](https://github.com/solkit70/VibeLearn-AI/issues)로 알려주세요.

---

## 시작하기 전에: 필요한 것

| 필요 | 있나요? |
|------|---------|
| AI 도구 (VS Code + Copilot, Claude Code, Cursor 등) | ✅/❌ |
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
├── README.md
├── GETTING_STARTED.md
└── templates/
    ├── topic_starter.md
    ├── roadmap_prompt_template.md
    └── daily_learning_prompt.md
```

### Step 1.5: 클론 후 초기 설정 (3분, GitHub 클론 시만 해당)

```bash
# 1. git hook 설치 (commit 시 자동화 파이프라인 활성화)
powershell -ExecutionPolicy Bypass -File scripts/install-hooks.ps1

# 2. Python 패키지 설치
pip install -r requirements.txt

# 3. (선택) 자동 번역 API 키 설정
$env:ANTHROPIC_API_KEY = "sk-ant-..."
```

> ZIP 다운로드로 받은 경우에는 이 단계를 건너뛰어도 됩니다.

---

## Step 2: AI 도구에서 `VibeLearn-AI/` 폴더 열기 (2분)

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

## Step 3: 배우고 싶은 주제 말하기 (20분)

AI에게 이렇게 말하세요:

```
"Python 기초를 배우고 싶어."
```

**이게 전부입니다.** 나머지는 AI가 알아서 합니다:

1. 몇 가지 질문으로 학습 정보 수집 (목표, 기간, 환경 등)
2. `Topics/Python-Basics/` 폴더 구조 자동 생성
3. Roadmap 자동 생성 → `vl_roadmap/` 저장

AI가 모든 설정을 마치면 이렇게 말하세요:

```
"M1 학습을 시작해줘."
```

AI가 첫 번째 모듈 계획을 수립하고 학습을 시작합니다. 가용 시간이나 다른 정보가 필요하면 AI가 직접 물어봅니다.

---

## 30분 타임라인 요약

```
00:00 ─── Step 1: 저장소 받기 (5분)
00:05 ─── Step 1.5: 클론 후 초기 설정 (3분, 클론 시만)
00:08 ─── Step 2: AI 도구에서 폴더 열기 (2분)
00:10 ─── Step 3: "Python 기초를 배우고 싶어." 한 마디 (20분)
           └── AI가 자동으로: 질문 수집 → 폴더 생성 → Roadmap 생성
00:30 ─── "M1 학습을 시작해줘." → 첫 학습 세션 시작! 🎉
```

---

## 다음 날부터는 이렇게만 하세요

매일 AI 도구를 열고 `VibeLearn-AI/` 폴더에서:

```
"오늘 학습을 시작해줘."
```

AI가 Roadmap과 이전 WorkLog를 읽어 어디까지 왔는지 파악하고, 자동으로 이어서 진행합니다. 다른 정보를 입력할 필요가 없습니다.

---

## 자주 막히는 곳 & 해결책

### "AI가 폴더를 만들지 못해요"
- VS Code + GitHub Copilot, Claude Code, Cursor처럼 파일 시스템 접근이 가능한 AI 도구가 필요합니다
- ChatGPT 웹은 파일을 직접 생성하지 못합니다 → 에디터 통합 AI 도구 사용 필요

### "WorkLog를 어디에 써야 하나요?"
- AI가 자동으로 만들어줍니다. 직접 쓸 필요 없습니다

### "내 진도가 맞는지 모르겠어요"
- AI에게 "지금까지 어디까지 했어?"라고 물어보세요. 알아서 파악해줍니다

---

## 익숙해지면: 품질 높이는 팁

처음에는 짧은 한 마디로 시작하는 것이 최선입니다.
VibeLearn AI에 익숙해지면 더 상세한 Context를 제공하여 품질을 높일 수 있습니다.

```
# 기본 (처음 사용자)
"Python 기초를 배우고 싶어."

# 고급 (익숙해진 후)
"Python 기초를 배우고 싶어.
배경: JavaScript 경험 2년, 데이터 분석 목적, 3주 가용, 매일 2시간."
```

더 많은 Context → AI가 더 정확한 Roadmap + 맞춤 학습 계획 생성

---

## 더 자세히 알고 싶다면

- [VibeLearn AI란?](../../01-System-Overview/concepts/what-is-vibelearn-ai.md)
- [4단계 워크플로우](../../01-System-Overview/concepts/workflow-diagram.md)
- [FAQ](faq.md)
- [GETTING_STARTED.md](../../../../GETTING_STARTED.md) — 공식 상세 가이드

---

**작성자**: Claude with VibeLearn AI
**검증**: 이 가이드는 실제 VibeLearn-AI Topic 학습 과정에서 검증됨
