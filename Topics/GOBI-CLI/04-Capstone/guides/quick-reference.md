# GOBI CLI — Quick Reference Card

> **버전**: GOBI CLI v2.0.19
> **작성일**: 2026-04-24
> **CVL 업데이트**: 2026-05-29 (v2.0.12 → v2.0.19 vault CRUD + 미디어 첨부 추가)
> **상태**: 전체 명령어 참조 (v2.0.19 최신화)

---

## 인증 (Auth)

```bash
gobi auth login          # 로그인 (device-code flow — URL + 코드 출력)
gobi auth status         # 현재 인증 상태 확인
gobi auth logout         # 로그아웃
```

> **v2.0 변경**: 구 Google OAuth 브라우저 팝업 → device-code flow (헤드리스 지원)

---

## Vault 명령어 (구 Init + Brain publish + Sync)

```bash
gobi vault init               # Vault 초기화 + PUBLISH.md 생성 (인터랙티브)
gobi vault create <slug>      # 새 Vault 생성 (--name으로 표시 이름 지정) 🆕 v2.0.19
gobi vault rename <newName>   # Vault 이름 변경 (표시 이름만, PUBLISH.md title 무관) 🆕 v2.0.19
gobi vault delete <slug>      # Vault 삭제 ⚠️ 비가역적, 콘텐츠 먼저 정리 필요 🆕 v2.0.19
gobi vault set-primary <slug> # Primary Vault 설정 🆕 v2.0.19
gobi vault list               # 내 Vault 목록
gobi vault publish            # PUBLISH.md 발행 (구 brain publish)
gobi vault unpublish          # 발행 취소 (구 brain unpublish)
gobi vault status             # 발행 상태 확인
gobi vault sync               # 로컬 ↔ 서버 동기화 (구 gobi sync)
```

> `.gobi/settings.yaml`에 `vaultSlug` 저장됨
> **v2.0 변경**: `gobi init` → `gobi vault init` / `BRAIN.md` → `PUBLISH.md` / `gobi sync` → `gobi vault sync`
> **v2.0.19 추가**: vault create / rename / delete / set-primary

### Vault Sync 옵션

```bash
gobi vault sync --upload-only       # 로컬 변경사항만 업로드
gobi vault sync --download-only     # 서버 변경사항만 다운로드
gobi vault sync --dry-run           # 변경 예정 사항 미리보기
gobi vault sync --path "폴더/파일"  # 특정 경로만 동기화
gobi vault sync --conflict server   # 충돌 시 서버 우선 (ask|server|client|skip)
```

---

## Global Feed (개인 포스트, 구 Brain Updates)

```bash
gobi global feed                       # 공개 글로벌 피드 조회
gobi global create-post \
  --title "제목" --content "내용"      # 개인 포스트 작성 (구 brain post-update)
gobi global create-post \
  --attach photo.png                   # 이미지 첨부 (최대 4장, 5MB) 🆕 v2.0.19
gobi global create-post \
  --repost-post-id <id>               # 기존 포스트 리포스트 🆕 v2.0.19
gobi global create-post \
  --draft-id <id>                      # draft → post 변환 🆕 v2.0.19
gobi global list-posts --mine          # 내 포스트 목록 (구 brain list-updates)
gobi global edit-post <id> \
  --content "수정 내용"                # 포스트 수정 (구 brain edit-update)
gobi global delete-post <id>           # 포스트 삭제 (구 brain delete-update)
```

> **v2.0.19 추가**: `--attach` (미디어 첨부) / `--repost-post-id` (리포스트) / `--draft-id` / `--auto-attachments` / `--rich-text`

---

## Session 명령어 (v2.0에서 404 이슈 해결됨)

```bash
gobi session list                              # Session 목록 (✅ v2.0 정상 작동)
gobi session get <sessionId>                   # Session 내용 (✅ v2.0 정상 작동)
gobi session create-reply <sessionId> \
  --content "답장 내용"                        # 대화 이어가기 (구 session reply)
```

> **v2.0 변경**: `session reply` → `session create-reply`
> ✅ v0.6.15에서 발생하던 HTTP 404 이슈 **해결됨**

---

## Space 명령어 (구 Thread → Post)

### Space 탐색

```bash
gobi space list                          # Space 목록
gobi --json space list                   # JSON 출력

gobi space warp                          # 활성 Space 선택 (인터랙티브)
gobi space warp <slug>                   # 직접 지정

gobi space feed                          # 통합 피드 (최신순) — v2.0 신규
```

> 💡 **팁**: `--space-slug` 옵션으로 warp 없이 바로 지정 가능

### Post 조회 (구 Thread)

```bash
gobi space list-posts --space-slug <slug>          # Post 목록 (구 list-threads)
gobi space list-posts --space-slug <slug> --limit 10
gobi --json space list-posts --space-slug <slug>

# 페이지네이션
gobi space list-posts --space-slug <slug> \
  --cursor "2026-03-28T00:27:27.492Z"

gobi space get-post <postId> --space-slug <slug>   # Post 상세 (구 get-thread)
gobi space get-post <postId> --space-slug <slug> --limit 20
```

### Post CRUD (구 Thread CRUD)

```bash
# Post 생성 (구 create-thread)
gobi space create-post \
  --space-slug <slug> \
  --title "제목" \
  --content "본문" \
  --json

# Post 수정 (구 edit-thread)
gobi space edit-post <postId> \
  --space-slug <slug> \
  --title "수정 제목" \
  --content "수정 본문"

# Post 삭제 (구 delete-thread)
gobi space delete-post <postId> --space-slug <slug>
```

### Reply CRUD

```bash
gobi space create-reply <postId> \
  --space-slug <slug> --content "답글 내용"

gobi space edit-reply <replyId> \
  --space-slug <slug> --content "수정 내용"

gobi space delete-reply <replyId> --space-slug <slug>
```

### 토픽 탐색 (v2.0 신규)

```bash
gobi space list-topics --space-slug <slug>           # 토픽 태그 목록
gobi space list-topic-posts <topicSlug>              # 토픽별 Post 목록
```

---

## Saved (개인 노트 + 북마크, v2.0 신규)

```bash
gobi saved create-note --content "노트 내용"    # 개인 노트 작성
gobi saved list-notes                           # 노트 목록
gobi saved create-post --source <postId>        # 포스트 북마크
gobi saved list-posts                           # 북마크 목록
```

---

## Draft (에이전트 guidance, v2.0 신규)

```bash
gobi draft add "제목" "내용"          # draft 추가
gobi draft list                       # draft 목록
gobi draft get <id>                   # draft 상세
gobi draft delete <id>                # draft 삭제
gobi draft action <id> <index>        # suggested action 실행
```

---

## Media (미디어 생성, v2.0 신규)

```bash
gobi media generate-image --prompt "..."        # 이미지 생성
gobi media create-video --avatar-id <id> ...    # 아바타 영상 생성
gobi media list-avatars                         # 아바타 목록
gobi media list-voices                          # 음성 목록
```

---

## Sense (활동 & 전사 데이터)

```bash
# v2.0: --start-time / --end-time 필수 (ISO 8601 UTC)
gobi sense list-activities \
  --start-time 2026-05-10T00:00:00Z \
  --end-time   2026-05-11T00:00:00Z

gobi sense list-transcriptions \
  --start-time 2026-05-10T00:00:00Z \
  --end-time   2026-05-11T00:00:00Z
```

---

## 공통 옵션

| 옵션 | 설명 |
|------|------|
| `--json` (전역, 서브커맨드 앞) | JSON 형식 출력: `gobi --json <cmd>` |
| `--limit N` | 결과 수 제한 |
| `--cursor <value>` | 페이지네이션 커서 |
| `--space-slug <slug>` | Space 직접 지정 |
| `--vault-slug <slug>` | Vault 직접 지정 |

> ⚠️ `--json`은 **전역 옵션** — 반드시 서브커맨드 앞에 위치: `gobi --json session list`

---

## PUBLISH.md 구조 (구 BRAIN.md)

```markdown
---
title: vault 이름
tags: ["tag1", "tag2"]
description: 한 줄 설명
thumbnail: (선택) 이미지 URL
prompt: You are a ... assistant. Help users with ...
---

# Vault 소개

[Vault 본문 내용 — 마크다운 형식]
```

---

## v0.6.15 → v2.0.12 주요 변경 요약

| 구분 | v0.6.15 | v2.0.12 |
|------|---------|---------|
| 초기화 | `gobi init` | `gobi vault init` |
| 발행 파일 | `BRAIN.md` | `PUBLISH.md` |
| 발행 | `gobi brain publish` | `gobi vault publish` |
| 팀 공유 | `gobi brain post-update` | `gobi global create-post` |
| Brain 검색/질의 | `gobi brain search/ask` | **CLI에서 제거** (웹 UI) |
| 팀 토론 | `space create-thread` | `space create-post` |
| 대화 답장 | `session reply` | `session create-reply` |
| 파일 동기화 | `gobi sync` | `gobi vault sync` |
| Session 404 | ⚠️ HTTP 404 | ✅ 해결됨 |

---

## 실습에서 확인된 실제 ID들 (v0.6.x 기록)

| 항목 | ID | Space |
|------|----|----|
| Thread/Post (M3 CRUD 테스트) | 731 | changbal |
| Reply (M3 CRUD 테스트) | 732 | changbal |
| Thread/Post (M4 Capstone 완료) | 735 | changbal |
| Brain Ask Session (M2) | 677 | gobi-cli-study |
| Brain Ask Session (M4) | 679 | gobi-cli-study |

---

## 설치

```bash
npm install -g @gobi-ai/cli

gobi --version    # → 2.0.12
gobi --help
gobi <command> --help
```

---

> **작성자**: Changsoo (Claude Code 활용)
> **방법론**: VibeLearn AI v2.0
> **CVL 기준**: v2.0.12 (2026-05-10)
> **관련 모듈**: M1~M4 전체
