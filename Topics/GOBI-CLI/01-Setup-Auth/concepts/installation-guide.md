# GOBI CLI — 설치 & 인증 가이드

> **모듈**: M1 — 설치 & 인증 & 핵심 개념
> **작성일**: 2026-03-29
> **환경**: Windows 11, Node.js v22.15.0, npm v11.6.2
> **GOBI CLI 버전**: v0.6.15

---

## 사전 요구사항

| 항목 | 최소 버전 | 확인 명령어 | 상태 |
|------|----------|------------|------|
| Node.js | 18+ | `node --version` | v22.15.0 ✅ |
| npm | - | `npm --version` | v11.6.2 ✅ |
| GOBI 계정 | - | gobispace.com | ✅ |

---

## Step 1: 설치

```bash
# 전역 설치
npm install -g @gobi-ai/cli

# 설치 확인
gobi --version    # → 0.6.15
gobi --help       # → 전체 명령어 목록
```

> **주의**: `prebuild-install@7.1.3 deprecated` 경고가 나올 수 있으나 정상 설치됩니다.

---

## Step 2: 인증 확인

```bash
# 인증 상태 확인 (먼저 실행)
gobi auth status

# 출력 예시 (이미 로그인된 경우):
# Authenticated as Changsoo Park (solkit70@gmail.com)
# Run 'gobi init' to set up, then 'gobi space warp' to select a space.

# 미로그인 상태라면:
gobi auth login    # 브라우저 열림 → 로그인 완료
```

---

## Step 3: Vault 초기화 (gobi init)

```bash
# 프로젝트 폴더로 이동
cd <프로젝트 폴더>

# 초기화 (인터랙티브)
gobi init
```

**실행 흐름**:
```
? How would you like to set up your vault?
❯ Select an existing vault    ← 기존 vault 사용
  Create a new vault          ← 새 vault 생성

# "Create a new vault" 선택 시:
? Vault name: gobi-cli-study
→ Created vault "gobi-cli-study" (gobi-cli-study)
→ Vault set to "gobi-cli-study" (gobi-cli-study)
→ Updated .gobi/settings.yaml
→ Created BRAIN.md
```

**생성되는 파일**:
```
<프로젝트 폴더>/
├── .gobi/
│   └── settings.yaml    ← vaultSlug: gobi-cli-study
└── BRAIN.md             ← Brain 발행용 원본 파일 (frontmatter 포함)
```

**BRAIN.md 초기 내용**:
```markdown
---
title: gobi-cli-study
tags: []
description:
thumbnail:
prompt:
---
```

---

## Step 4: 로그아웃 (필요 시)

```bash
gobi auth logout
```

---

## 빠른 점검 체크리스트

```bash
node --version      # v18+ 확인
gobi --version      # 설치 확인
gobi auth status    # 인증 확인
ls .gobi/           # settings.yaml 존재 확인 (gobi init 후)
```

---

> **다음 문서**: [core-concepts.md](core-concepts.md)
> **작성자**: Changsoo (Claude Code 활용)
> **방법론**: VibeLearn AI v2.0
