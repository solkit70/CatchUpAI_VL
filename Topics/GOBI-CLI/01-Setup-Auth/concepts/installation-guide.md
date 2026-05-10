# GOBI CLI — 설치 & 인증 가이드

> **모듈**: M1 — 설치 & 인증 & 핵심 개념
> **작성일**: 2026-03-29
> **CVL 업데이트**: 2026-05-10 (v2.0.12 반영)
> **환경**: Windows 11, Node.js v22.15.0, npm v11.6.2
> **GOBI CLI 버전**: v2.0.12

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

# 또는 Homebrew (macOS/Linux)
brew tap gobi-ai/tap && brew install gobi

# 설치 확인
gobi --version    # → 2.0.12
gobi --help       # → 전체 명령어 목록
```

---

## Step 2: 인증 (device-code flow)

> ⚠️ **v2.0 변경**: 구 Google OAuth 브라우저 팝업 → **device-code flow** (헤드리스 환경 지원)

```bash
# 인증 상태 먼저 확인
gobi auth status

# 미인증 상태라면:
gobi auth login
# → 터미널에 URL + user code 출력
# → 브라우저에서 URL 열어 code 입력 → CLI가 완료까지 자동 폴링
```

**인증 완료 후 확인**:
```bash
gobi --json auth status
# {"success": true, "data": {"authenticated": true, "email": "solkit70@gmail.com"}}
```

---

## Step 3: Vault 초기화 (`gobi vault init`)

> ⚠️ **v2.0 변경**: `gobi init` → `gobi vault init` / `BRAIN.md` → `PUBLISH.md`

```bash
# 프로젝트 폴더에서 실행 (인터랙티브)
gobi vault init
```

**실행 흐름**:
```
? How would you like to set up your vault?
❯ Select an existing vault    ← 기존 vault 사용
  Create a new vault          ← 새 vault 생성

# "Create a new vault" 선택 시:
? Vault name: gobi-cli-study
→ Created vault "gobi-cli-study"
→ Updated .gobi/settings.yaml
→ Created PUBLISH.md
```

**생성되는 파일**:
```
<프로젝트 폴더>/
├── .gobi/
│   ├── settings.yaml    ← vaultSlug: gobi-cli-study
│   └── syncfiles        ← sync 대상 패턴 (선택적)
└── PUBLISH.md           ← vault 발행용 원본 파일 (frontmatter 포함)
```

**PUBLISH.md 초기 내용**:
```markdown
---
title: gobi-cli-study
tags: []
description:
thumbnail:
prompt:
---
```

> **참고**: `PUBLISH.md`는 구 `BRAIN.md`를 대체합니다. 동일한 frontmatter 구조 사용.

---

## Step 4: Space 선택

```bash
# 인터랙티브 Space 선택
gobi space warp

# 또는 slug 직접 지정
gobi space warp changbal
```

`gobi space warp` 완료 후 `.gobi/settings.yaml`:
```yaml
vaultSlug: gobi-cli-study
selectedSpaceSlug: changbal
```

---

## Step 5: 로그아웃 (필요 시)

```bash
gobi auth logout
```

---

## 빠른 점검 체크리스트

```bash
node --version          # v18+ 확인
gobi --version          # 2.0.12 확인
gobi auth status        # 인증 확인
cat .gobi/settings.yaml # vaultSlug, selectedSpaceSlug 존재 확인
```

---

## 에이전트 주의사항

| 명령어 | 인터랙티브 여부 | 에이전트 실행 가능 |
|--------|---------------|-----------------|
| `gobi auth login` | device-code (URL 출력) | 사용자에게 URL 전달 후 완료 대기 ✅ |
| `gobi vault init` | 완전 인터랙티브 | ❌ 사용자 직접 실행 필요 |
| `gobi space warp` | 완전 인터랙티브 | ❌ 사용자 직접 실행 필요 |
| 그 외 모든 명령어 | 비인터랙티브 | ✅ 자동화 가능 |

---

> **다음 문서**: [core-concepts.md](core-concepts.md)
> **작성자**: Changsoo (Claude Code 활용)
> **방법론**: VibeLearn AI v2.0
> **CVL 기준**: v2.0.12 (2026-05-10)
