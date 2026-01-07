# Hello Skill

**작성일**: 2026-01-07
**목적**: Claude Skills의 기본 구조를 이해하기 위한 첫 번째 예제 Skill

---

## 📌 개요

Hello Skill은 가장 간단한 형태의 Claude Skill입니다. 사용자에게 인사하고 이름을 물어본 후 개인화된 메시지를 출력합니다.

---

## 🎯 학습 목표

이 Skill을 통해 다음을 배울 수 있습니다:

- SKILL.md 파일의 기본 구조 (메타데이터 + 지침)
- description의 중요성 (Claude가 자동 활성화하는 기준)
- Skill 설치 및 사용 방법
- Personal Skills 폴더 관리

---

## 📁 파일 구조

```
hello-skill/
├── SKILL.md          # Skill 정의 파일
└── README.md         # 이 파일 - 설명서
```

---

## 📝 SKILL.md 구조

### 메타데이터 (YAML Front Matter)

```yaml
---
name: hello-skill
description: 사용자에게 인사하고 간단한 메시지를 출력합니다. 테스트용 첫 번째 Skill입니다.
---
```

**핵심 포인트**:
- `name`: Skill의 고유 이름 (소문자, 하이픈만 사용)
- `description`: Claude가 이 Skill을 언제 활성화할지 결정하는 기준
  - "무엇을"하는지 명확히: "사용자에게 인사하고 메시지를 출력"
  - "언제" 사용하는지: "테스트용 첫 번째 Skill"

### 지침 (Instructions)

SKILL.md 본문에는 Claude가 따를 구체적인 지침을 작성합니다:

1. 사용자에게 인사말 출력
2. 이름 물어보기
3. 개인화된 메시지 출력
4. Claude Skills 정보 제공

---

## 🔧 설치 방법

### Personal Skills 폴더에 설치

```bash
# 1. Personal Skills 폴더 생성
mkdir -p ~/.claude/skills/hello-skill

# 2. SKILL.md 파일 복사
cp SKILL.md ~/.claude/skills/hello-skill/SKILL.md

# 3. Claude Code 재시작 (VS Code Extension 또는 CLI)
```

### 설치 확인

Claude Code를 재시작한 후 다음을 입력:

```
What Skills are available?
```

응답에 "hello-skill"이 포함되어 있으면 설치 성공!

---

## 🚀 사용 방법

### 자동 활성화 (권장)

Claude에게 다음과 같이 요청하면 자동으로 이 Skill이 활성화됩니다:

```
Hello Skill을 실행해줘
```

또는

```
첫 번째 Skill을 테스트하고 싶어
```

**왜 자동 활성화되나요?**
- description에 "테스트용 첫 번째 Skill"이라는 키워드가 있음
- Claude가 사용자 요청과 description의 의미적 일치를 판단
- 일치하면 자동으로 SKILL.md를 로드하여 지침 실행

### 예상 대화 흐름

**사용자**: "Hello Skill을 실행해줘"

**Claude**:
```
안녕하세요! 👋

저는 당신의 첫 번째 Claude Skill입니다.

이름을 알려주시겠어요?
```

**사용자**: "김철수"

**Claude**:
```
반갑습니다, 김철수님! 🎉

Claude Skills는 Claude Code에서 사용할 수 있는 커스텀 기능입니다.
- 자동으로 활성화됩니다 (description 기반)
- 마크다운 파일로 간단히 작성 가능
- 반복 작업을 자동화할 수 있습니다

이 Skill을 통해 Claude Skills의 기본 구조를 이해하셨기를 바랍니다!
```

---

## 🎓 학습 포인트

### 1. SKILL.md만 있으면 충분

- 별도의 코드 파일 불필요
- 마크다운으로 지침만 작성
- Claude가 지침을 읽고 실행

### 2. description이 가장 중요

- Claude가 Skill을 선택하는 **유일한** 기준
- "무엇을" + "언제" 명확히 작성
- 구체적이고 명확할수록 정확한 활성화

### 3. Personal Skills 폴더

- `~/.claude/skills/[skill-name]/SKILL.md`
- 모든 프로젝트에서 사용 가능
- 재시작 시 자동 로드

### 4. Progressive Disclosure

- Discovery 단계: 메타데이터만 로드 (name, description)
- Activation 단계: 요청과 일치하면 SKILL.md 전체 로드
- Execution 단계: 지침 실행

---

## 🔄 수정 및 테스트

### Skill 수정

1. SKILL.md 파일 편집
2. Claude Code 재시작
3. 테스트

### 디버깅 팁

- description이 명확한가? → 수정 후 재시작
- Claude가 활성화하지 않는가? → description에 더 구체적인 키워드 추가
- 지침이 명확한가? → 단계별로 구체화

---

## 📊 비교: Skill vs Slash Command

| 특징 | Hello Skill | Slash Command |
|------|------------|---------------|
| **호출 방법** | 자동 (description 기반) | 명시적 (`/hello`) |
| **파일** | SKILL.md | .claude/slash-commands.json |
| **복잡도** | 단순 (마크다운만) | 단순 (JSON) |
| **재사용성** | 모든 프로젝트 | 모든 프로젝트 또는 프로젝트별 |
| **적합한 용도** | 자동화된 워크플로우 | 명시적 프롬프트 템플릿 |

---

## ✅ 검증 체크리스트

- [ ] SKILL.md 파일 작성 완료
- [ ] Personal Skills 폴더에 설치 완료
- [ ] Claude Code 재시작 완료
- [ ] "What Skills are available?" 로 설치 확인
- [ ] "Hello Skill을 실행해줘" 로 동작 확인
- [ ] 이름 입력 후 개인화된 메시지 출력 확인

---

## 🚀 다음 단계

이 Hello Skill을 이해했다면:

1. **실습 3**: CUA_VL Skill vs Repository 비교 분석
2. **M2**: Skill A - CUA_VL Skill 개발 (실전 Skill)
3. **M3**: Skill B - YouTube→MD Skill 개발 (복잡한 Skill)

---

**작성자**: CUA_VL Claude Skills 학습
**버전**: 1.0
**최종 업데이트**: 2026-01-07
