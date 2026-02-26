# VibeLearn AI Skill - Claude 사용자를 위한 선택적 확장

**버전**: 1.1
**생성일**: 2026-01-25
**대상**: Claude Code / Claude Desktop 사용자

---

## 📌 개요

이 폴더는 **Claude 사용자**를 위한 **선택적** 확장 기능입니다.

VibeLearn AI Skill을 설치하면 폴더 자동 생성, 파일 탐색 등의 자동화 기능을 사용할 수 있습니다.

> **중요**: 이 Skill은 **선택 사항**입니다.
> VibeLearn AI 방법론은 프롬프트 기반으로 **모든 AI 도구**에서 사용 가능합니다.
> Skill 없이도 `templates/workflow_guide.md`를 참고하여 동일한 학습을 진행할 수 있습니다.

---

## 🎯 Skill vs 프롬프트 비교

| 항목 | Skill 사용 | 프롬프트 사용 |
|------|-----------|--------------|
| **지원 도구** | Claude만 | 모든 AI |
| **폴더 자동 생성** | ✅ | ❌ (수동) |
| **파일 자동 탐색** | ✅ | ❌ (수동) |
| **시간 절약** | ~70% | 기준선 |
| **설치 필요** | ✅ | ❌ |

---

## 📥 설치 방법

### 사전 요구 사항

- Claude Code (VS Code Extension) 또는 Claude Desktop
- VibeLearn-AI Repository 다운로드 완료

### Step 1: Personal Skills 폴더 확인

**Windows**:
```
%USERPROFILE%\.claude\skills\
```

**macOS/Linux**:
```
~/.claude/skills/
```

폴더가 없으면 생성하세요:
```bash
# Windows (PowerShell)
mkdir -p "$env:USERPROFILE\.claude\skills"

# macOS/Linux
mkdir -p ~/.claude/skills
```

### Step 2: Skill 폴더 생성 및 복사

```bash
# Windows (PowerShell)
mkdir "$env:USERPROFILE\.claude\skills\cua-vl"
cp "extras\claude-skill\SKILL.md" "$env:USERPROFILE\.claude\skills\cua-vl\"

# macOS/Linux
mkdir -p ~/.claude/skills/cua-vl
cp extras/claude-skill/SKILL.md ~/.claude/skills/cua-vl/
```

### Step 3: SKILL.md 경로 설정

SKILL.md 파일을 열고 `{VibeLearn AI_ROOT}`를 실제 경로로 변경하세요:

```markdown
# 변경 전
파일: {VibeLearn AI_ROOT}/templates/topic_starter.md

# 변경 후 (예시)
파일: C:\Projects\VibeLearn-AI\templates\topic_starter.md
# 또는
파일: ~/Projects/VibeLearn-AI/templates/topic_starter.md
```

### Step 4: Claude 재시작

- **Claude Code**: VS Code 재시작 또는 Extension 재로드
- **Claude Desktop**: 앱 재시작

### Step 5: 설치 확인

Claude에게 다음과 같이 물어보세요:

```
"VibeLearn AI Skill이 설치되어 있나요?"
```

또는 직접 명령어 실행:

```
/cua-vl start
```

---

## 🚀 사용 방법

### 핵심 명령어

| 명령어 | 설명 | 자연어 요청 |
|--------|------|------------|
| `/cua-vl start` | 새 Topic 시작 | "새 Topic을 시작하고 싶어" |
| `/cua-vl roadmap` | Roadmap 생성 | "Roadmap을 만들고 싶어" |
| `/cua-vl daily` | 일일 학습 시작 | "오늘 학습을 시작하겠습니다" |

### 사용 예시

```
사용자: "Docker 학습을 위한 새 Topic을 시작하고 싶어"

VibeLearn AI Skill:
1. "어떤 Topic을 시작하시겠습니까?"
2. [사용자: Docker-Fundamentals]
3. ✅ 폴더 자동 생성
4. topic_starter.md 템플릿 제공
5. 다음 단계 안내
```

---

## 📊 기대 효과

### 시간 절약 측정 결과

| 작업 | Skill 없음 | Skill 사용 | 절약 |
|------|-----------|-----------|------|
| Topic 시작 | 5분 | 1분 | 80% |
| Roadmap 생성 | 10분 | 3분 | 70% |
| 일일 학습 시작 | 5분 | 2분 | 60% |
| **전체** | **20분** | **6분** | **70%** |

---

## 🔧 문제 해결

### Q1: Skill이 활성화되지 않아요

**확인 사항**:
1. `~/.claude/skills/cua-vl/SKILL.md` 파일이 존재하는지 확인
2. SKILL.md의 `{VibeLearn AI_ROOT}` 경로가 올바른지 확인
3. Claude 재시작 시도

**해결책**:
- 정확한 명령어 사용: `/cua-vl start`
- 경로가 올바른지 확인

### Q2: 폴더 생성 오류

**원인**: 경로 설정 오류 또는 권한 문제

**해결책**:
1. SKILL.md의 `{VibeLearn AI_ROOT}` 경로 확인
2. 해당 경로에 쓰기 권한이 있는지 확인
3. 수동으로 폴더 생성 후 재시도

### Q3: 템플릿 파일을 찾을 수 없어요

**원인**: VibeLearn AI Repository 경로 오류

**해결책**:
1. SKILL.md의 모든 `{VibeLearn AI_ROOT}` 경로 확인
2. `templates/` 폴더가 존재하는지 확인
3. 경로 수정 후 Claude 재시작

---

## 📁 파일 구조

```
extras/claude-skill/
├── SKILL.md      # Skill 정의 파일 (설치 대상)
└── README.md     # 이 파일 (설치 가이드)
```

### 설치 후 구조

```
~/.claude/skills/
└── cua-vl/
    └── SKILL.md    # 설치된 Skill
```

---

## 🔄 업데이트

### Skill 업데이트 방법

1. 최신 VibeLearn-AI Repository 다운로드
2. `extras/claude-skill/SKILL.md`를 `~/.claude/skills/cua-vl/`에 복사
3. `{VibeLearn AI_ROOT}` 경로 재설정
4. Claude 재시작

---

## 📞 지원

### Skill 없이 사용하기

Skill 설치가 어려우면 프롬프트 기반으로 사용하세요:

- **워크플로우 가이드**: `templates/workflow_guide.md`
- **모든 AI 도구에서 사용 가능**

### 문의

- 이메일: solkit70@gmail.com
- GitHub: [VibeLearn-AI Repository]

---

**버전**: 1.1
**작성일**: 2026-01-25
**대상**: Claude Code / Claude Desktop 사용자
