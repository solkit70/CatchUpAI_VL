# GOBI CLI — Quick Reference Card

> **버전**: GOBI CLI v0.6.15 (CVL 업데이트 완료)
> **작성일**: 2026-04-24
> **상태**: 전체 명령어 참조 (v0.6.15 최신화)

---

## 인증 (Auth)

```bash
gobi auth login          # 로그인 (브라우저 열림)
gobi auth status         # 현재 인증 상태 확인
gobi auth logout         # 로그아웃
```

---

## 초기화 (Init)

```bash
gobi init                # Vault 선택 + BRAIN.md 생성 (인터랙티브 필수)
```

> `.gobi/settings.yaml`에 `vaultSlug` 저장됨

---

## 동기화 (Sync) 🆕

```bash
# 로컬 <-> 서버 양방향 동기화
gobi sync

# 정교한 옵션
gobi sync --upload-only      # 로컬 변경사항만 업로드
gobi sync --download-only    # 서버 변경사항만 다운로드
gobi sync --dry-run          # 변경 예정 사항 미리보기
gobi sync --full             # 전체 재검사 (캐시 무시)
gobi sync --path "app/home.html"  # 특정 파일/폴더만 동기화
gobi sync --conflict server  # 충돌 시 서버 버전 우선 (ask|server|client|skip)
```

---

## 지각 (Sense) 🆕

```bash
# 활동 기록 조회 (활동 시간, 종류 등)
gobi sense activities --limit 10

# 전사 기록 조회 (녹음/회의 전사 텍스트)
gobi sense transcriptions --limit 5
```

---

## Brain 명령어

### 검색 & 질의

```bash
# Brain 검색 (시맨틱 유사도)
gobi brain search --query "검색어"
gobi brain search --query "검색어" --json    # JSON 출력

# Brain에 AI 질의 (Session 생성)
gobi brain ask --vault-slug <slug> --question "질문"
gobi brain ask --vault-slug <slug> --question "질문" --json
```

### 발행

```bash
# BRAIN.md 발행 (현재 폴더의 BRAIN.md 기준)
gobi brain publish

# 발행 취소
gobi brain unpublish
```

### Updates (팀 피드)

```bash
# Update 게시
gobi brain post-update --vault-slug <slug> --content "내용"

# Update 목록 (본인 것)
gobi brain list-updates --vault-slug <slug>
gobi brain list-updates --vault-slug <slug> --limit 5

# Update 수정
gobi brain edit-update <updateId> --vault-slug <slug> --content "수정 내용"

# Update 삭제
gobi brain delete-update <updateId> --vault-slug <slug>
```

---

## Session 명령어

> ⚠️ **v0.6.15 Known Issue**: `list/get/reply` 명령어 모두 HTTP 404 반환
> → 웹(gobispace.com)에서 확인 필요

```bash
gobi session list                         # ⚠️ HTTP 404 (v0.6.15 이슈)
gobi session get <sessionId>              # ⚠️ HTTP 404 (v0.6.15 이슈)
gobi session reply <sessionId> \
  --content "답장 내용"                   # ⚠️ HTTP 404 (v0.6.15 이슈)
```

---

## Space 명령어

### Space 탐색

```bash
# Space 목록
gobi space list
gobi space list --json

# 활성 Space 선택 (인터랙티브)
gobi space warp
gobi space warp <slug>    # 직접 지정
```

> 💡 **팁**: `--space-slug` 옵션으로 warp 없이 바로 지정 가능

### Thread 조회

```bash
# Thread 목록
gobi space list-threads --space-slug <slug>
gobi space list-threads --space-slug <slug> --limit 10
gobi space list-threads --space-slug <slug> --json

# 페이지네이션
gobi space list-threads --space-slug <slug> \
  --cursor "2026-03-28T00:27:27.492Z"

# Thread 상세 조회 (본문 + Replies)
gobi space get-thread <threadId> --space-slug <slug>
gobi space get-thread <threadId> --space-slug <slug> --limit 20
```

### Thread CRUD

```bash
# Thread 생성
gobi space create-thread \
  --space-slug <slug> \
  --title "제목" \
  --content "본문" \
  --json    # id 반환

# Thread 수정
gobi space edit-thread <threadId> \
  --space-slug <slug> \
  --title "수정 제목" \
  --content "수정 본문"

# Thread 삭제
gobi space delete-thread <threadId> --space-slug <slug>
```

### Reply CRUD

```bash
# Reply 생성
gobi space create-reply <threadId> \
  --space-slug <slug> \
  --content "답글 내용" \
  --json    # id 반환

# Reply 수정
gobi space edit-reply <replyId> \
  --space-slug <slug> \
  --content "수정 내용"

# Reply 삭제
gobi space delete-reply <replyId> --space-slug <slug>
```

---

## 공통 옵션

| 옵션 | 설명 |
|------|------|
| `--json` | JSON 형식 출력 |
| `--limit N` | 결과 수 제한 |
| `--cursor <value>` | 페이지네이션 커서 |
| `--space-slug <slug>` | Space 직접 지정 |
| `--vault-slug <slug>` | Vault 직접 지정 |

---

## BRAIN.md 구조

```markdown
---
title: <vault-slug>
tags: ["tag1", "tag2"]
description: 한 줄 설명
thumbnail: (선택) 이미지 URL
prompt: You are a ... assistant. Help users with ...
---

# Brain 제목

[Brain 본문 내용 — 마크다운 형식]
```

---

## 버전별 이슈 (v0.6.15)

| 이슈 | 심각도 | 설명 |
|------|--------|------|
| `session list/get/reply` HTTP 404 | High | 서버 엔드포인트 미매칭 |
| `session update` 명령어 없음 | Medium | v0.6.15에 미구현 |
| `--message` 옵션 → `--content` | Low | 문서 오류 (실제 옵션은 `--content`) |

---

## 실습에서 확인된 실제 ID들

| 항목 | ID | Space |
|------|----|----|
| Thread (M3 CRUD 테스트) | 731 | changbal |
| Reply (M3 CRUD 테스트) | 732 | changbal |
| Thread (M4 Capstone 완료) | 735 | changbal |
| Brain Ask Session (M2) | 677 | gobi-cli-study |
| Brain Ask Session (M4) | 679 | gobi-cli-study |

---

## 설치

```bash
# 설치
npm install -g @gobi-ai/cli

# 버전 확인
gobi --version
# → 0.6.15

# 도움말
gobi --help
gobi <command> --help
```

---

> **작성자**: Changsoo (Claude Code 활용)
> **방법론**: VibeLearn AI v2.0
> **관련 모듈**: M1~M4 전체
