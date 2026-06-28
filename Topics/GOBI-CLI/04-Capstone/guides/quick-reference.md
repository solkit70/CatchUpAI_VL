# GOBI CLI — Quick Reference Card

> **버전**: GOBI CLI v2.0.35
> **작성일**: 2026-04-24
> **CVL 업데이트**: 2026-06-27 (v2.0.19 → v2.0.35 — session/saved/draft 제거, personal/artifact/채널/미디어 추가)
> **상태**: 전체 명령어 참조 (v2.0.35 최신화)

---

## 인증 (Auth)

```bash
gobi auth login          # 로그인 (device-code flow — URL + 코드 출력)
gobi auth status         # 현재 인증 상태 확인
gobi auth logout         # 로그아웃
```

> **v2.0 변경**: 구 Google OAuth 브라우저 팝업 → device-code flow (헤드리스 지원)

---

## Vault 명령어

```bash
gobi vault init               # Vault 초기화 + PUBLISH.md 생성 (인터랙티브)
gobi vault create <slug>      # 새 Vault 생성 (--name으로 표시 이름 지정) 🆕 v2.0.19
gobi vault rename <newName>   # Vault 이름 변경 (표시 이름만, PUBLISH.md title 무관) 🆕 v2.0.19
gobi vault delete <slug>      # Vault 삭제 ⚠️ 비가역적, 콘텐츠 먼저 정리 필요 🆕 v2.0.19
gobi vault list               # 내 Vault 목록
gobi vault status             # 발행 상태 + 메타데이터 확인
gobi vault publish            # PUBLISH.md 발행 (구 brain publish)
gobi vault unpublish          # 발행 취소 (구 brain unpublish)
gobi vault sync               # 로컬 ↔ 서버 동기화 (구 gobi sync)
```

> ⚠️ `vault set-primary`는 v2.0.35에서 **제거됨**
> `.gobi/settings.yaml`에 `vaultSlug` 저장됨
> **v2.0 변경**: `gobi init` → `gobi vault init` / `BRAIN.md` → `PUBLISH.md` / `gobi sync` → `gobi vault sync`

### Vault Sync 옵션

```bash
gobi vault sync --upload-only       # 로컬 변경사항만 업로드
gobi vault sync --download-only     # 서버 변경사항만 다운로드
gobi vault sync --dry-run           # 변경 예정 사항 미리보기
gobi vault sync --path "폴더/파일"  # 특정 경로만 동기화
gobi vault sync --conflict server   # 충돌 시 서버 우선 (ask|server|client|skip)
```

---

## Global Feed (공개 개인 포스트, 구 Brain Updates)

```bash
gobi global feed                       # 공개 글로벌 피드 조회
gobi global create-post \
  --title "제목" --content "내용"      # 개인 포스트 작성 (구 brain post-update)
gobi global create-post \
  --attach photo.png                   # 이미지 첨부 (최대 4장, 5MB) 🆕 v2.0.19
gobi global create-post \
  --repost-post-id <id>               # 기존 포스트 리포스트 🆕 v2.0.19
gobi global create-post \
  --draft-id <id>                      # draft → post 변환 (draft는 v2.0.35에서 제거됨)
gobi global list-posts --mine          # 내 포스트 목록 (구 brain list-updates)
gobi global edit-post <id> \
  --content "수정 내용"                # 포스트 수정 (구 brain edit-update)
gobi global delete-post <id>           # 포스트 삭제
gobi global create-reply <postId>      # 글로벌 포스트에 답글
```

> **v2.0.19 추가**: `--attach` / `--repost-post-id` / `--auto-attachments` / `--rich-text`

---

## Personal Feed (프라이빗 개인 포스트) 🆕 v2.0.35

나만 볼 수 있는 프라이빗 포스트. Global 피드에는 노출되지 않음.

```bash
gobi personal feed                     # 개인 프라이빗 피드 조회
gobi personal create-post \
  --content "내용"                     # 프라이빗 포스트 작성
gobi personal list-posts               # 내 프라이빗 포스트 목록
gobi personal search-posts <query>     # 개인 포스트 검색 (from:/topic: 연산자 지원)
gobi personal get-post <postId>        # 포스트 상세 (+ 답글)
gobi personal edit-post <postId>       # 포스트 수정
gobi personal delete-post <postId>     # 포스트 삭제
gobi personal create-reply <postId>    # 포스트에 답글 (답글은 부모 스코프 자동 상속)
gobi personal edit-reply <replyId>     # 답글 수정
gobi personal delete-reply <replyId>   # 답글 삭제
gobi personal react <postId> <emoji>   # 이모지 반응 (멱등)
gobi personal unreact <postId> <emoji> # 이모지 반응 취소
```

> **용도**: 내가 나만 보는 메모/스크래치패드 포스트. Global feed와 동일 데이터 모델, scope만 다름.

---

## Space 명령어

### Space 탐색

```bash
gobi space list                          # Space 목록
gobi --json space list                   # JSON 출력

gobi space warp                          # 활성 Space 선택 (인터랙티브)
gobi space warp <slug>                   # 직접 지정

gobi space feed                          # 통합 피드 (최신순)
gobi space get [spaceSlug]               # Space 상세 정보
```

> 💡 **팁**: `--space-slug` 옵션으로 warp 없이 바로 지정 가능

### Post 조회 (구 Thread)

```bash
gobi space list-posts --space-slug <slug>          # Post 목록 (구 list-threads)
gobi space list-posts --space-slug <slug> --limit 10
gobi --json space list-posts --space-slug <slug>

gobi space get-post <postId> --space-slug <slug>   # Post 상세 (구 get-thread)

# Post 검색 🆕 v2.0.35
gobi space search-posts "키워드" --space-slug <slug>
gobi space search-posts "from:이름 topic:AI" --space-slug <slug>
# 검색 연산자: from:<name>, topic:<tag> (공백 포함 시 따옴표: from:"Jane Doe")
```

### Post CRUD (구 Thread CRUD)

```bash
# Post 생성 (구 create-thread)
gobi space create-post \
  --space-slug <slug> \
  --title "제목" \
  --content "본문"

# Post 수정
gobi space edit-post <postId> \
  --space-slug <slug> \
  --content "수정 내용"

# Post 삭제
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

### 이모지 반응 🆕 v2.0.35

```bash
gobi space react <postId> <emoji> --space-slug <slug>    # 반응 추가 (멱등)
gobi space unreact <postId> <emoji> --space-slug <slug>  # 반응 취소
# <postId>는 post 또는 reply의 numeric id — 피드 출력의 [p:N]/[r:N] 형식
```

### 채널 관리 🆕 v2.0.35

```bash
gobi space list-channels --space-slug <slug>             # 채널 목록 (멤버: 내 채널, 어드민: 전체)
gobi space get-channel <channelId> --space-slug <slug>   # 채널 상세 (에이전트 채널도 포함)
gobi space list-channel-members <channelId> \
  --space-slug <slug>                                    # 채널 멤버 목록
```

### 토픽 탐색

```bash
gobi space list-topics --space-slug <slug>           # 토픽 태그 목록
gobi space list-topic-posts <topicSlug>              # 토픽별 Post 목록
```

---

## Artifact (버전관리 콘텐츠) 🆕 v2.0.35

포스트에 첨부되는 버전관리 창작물. 종류: `image` | `video` | `gif` | `markdown` | `meeting_summary`
항상 사람 소유. revision이 draft/published 트리를 형성 (published는 최대 1개).

```bash
# 생성
gobi artifact create \
  --kind markdown --content "내용" \
  --post-id <postId>                # 포스트에 첨부
gobi artifact create \
  --kind image --file photo.png     # 이미지 아티팩트

# 수정 (새 draft revision 추가)
gobi artifact revise <artifactId> \
  --content "수정 내용"
gobi artifact revise <artifactId> \
  --from <revisionId>               # 특정 revision에서 분기

# 발행 / 되돌리기
gobi artifact publish <artifactId>  # 최신 draft → published
gobi artifact revert <artifactId>   # published를 이전 revision으로 되돌리기

# 조회
gobi artifact get <artifactId>      # 아티팩트 + 현재 revision
gobi artifact list                  # 내 아티팩트 목록
gobi artifact history <artifactId>  # 전체 revision 트리 (소유자만)

# 다운로드 / 삭제
gobi artifact download <artifactId> --out output.md
gobi artifact delete <artifactId>
```

---

## Media (미디어 생성)

### 파일 업로드 🆕 v2.0.35

```bash
gobi media upload <file>            # 로컬 파일 업로드 → media ID 반환
```

### 이미지 생성/편집

```bash
gobi media generate-image \
  --prompt "..." \
  --type image                      # image(기본) | thumbnail | asset
  # aspect-ratio: 1:1 | 16:9 | 9:16 | 4:3 | 3:4

gobi media edit-image \
  --prompt "수정 내용" \
  --image-id <id>                   # 이미지-to-이미지 편집 🆕 v2.0.35

gobi media inpaint-image \
  --prompt "..." \
  --image-id <id> --mask-id <id>   # 마스크 영역 인페인팅 🆕 v2.0.35

# 이미지 작업 상태 / 다운로드
gobi media get-image-status <jobId>     # 생성 작업 상태 🆕 v2.0.35
gobi media download-image <jobId>       # 생성 이미지 다운로드 🆕 v2.0.35
```

### 영상 생성

```bash
gobi media create-video \
  --avatar-id <id> \
  --voice-id <id> \
  --script "..."                    # 아바타 영상 생성

gobi media create-cinematic \
  --prompt "..."                    # 텍스트 프롬프트로 시네마틱 영상 🆕 v2.0.35

gobi media list-videos              # 내 영상 목록 🆕 v2.0.35
gobi media get-video <videoId>      # 영상 메타데이터 🆕 v2.0.35
gobi media get-video-status <videoId>    # 영상 생성 상태 🆕 v2.0.35
gobi media download-video <videoId>      # 완성 영상 다운로드 🆕 v2.0.35
```

### 아바타

```bash
gobi media list-avatars             # 아바타 목록
gobi media list-voices              # 음성 목록
gobi media design-avatar            # 아바타 디자인 작업 시작 🆕 v2.0.35
gobi media confirm-avatar           # 아바타 변형 확정 🆕 v2.0.35
gobi media design-avatar-from-selfie \
  --file selfie.jpg                 # 셀피 기반 아바타 디자인 🆕 v2.0.35
gobi media get-avatar-job-status <jobId>  # 아바타 작업 상태 🆕 v2.0.35
```

---

## Sense (활동 & 전사 데이터)

```bash
# --start-time / --end-time 필수 (ISO 8601 UTC)
gobi sense list-activities \
  --start-time 2026-06-01T00:00:00Z \
  --end-time   2026-06-27T00:00:00Z

gobi sense list-transcriptions \
  --start-time 2026-06-01T00:00:00Z \
  --end-time   2026-06-27T00:00:00Z
```

---

## 자가 업데이트

```bash
gobi update     # gobi-cli를 최신 버전으로 자동 업데이트 (🆕 v2.0.19)
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

> ⚠️ `--json`은 **전역 옵션** — 반드시 서브커맨드 앞에 위치: `gobi --json space list`

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

## v2.0.19 → v2.0.35 주요 변경 요약

| 구분 | v2.0.19 | v2.0.35 |
|------|---------|---------|
| session | `gobi session list/get/create-reply` | **제거됨** |
| saved | `gobi saved create-note/list-notes` | **제거됨** |
| draft | `gobi draft add/list/action` | **제거됨** |
| vault | `vault set-primary` 포함 | `set-primary` **제거됨** |
| personal | 없음 | **신규** (프라이빗 포스트) |
| artifact | 없음 | **신규** (버전관리 콘텐츠) |
| space | search/react/채널 없음 | `search-posts`, `react/unreact`, 채널 3개 **신규** |
| media | 4개 서브커맨드 | 18개 서브커맨드 (업로드/편집/시네마틱/아바타 대폭 추가) |

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
| 대화 답장 | `session reply` | `session create-reply` (→ v2.0.35에서 완전 제거) |
| 파일 동기화 | `gobi sync` | `gobi vault sync` |
| Session 404 | ⚠️ HTTP 404 | ✅ v2.0.12 해결 → v2.0.35에서 CLI 자체 제거 |

---

## 실습에서 확인된 실제 ID들

| 항목 | ID | Space |
|------|----|----|
| Thread/Post (M3 CRUD 테스트) | 731 | changbal |
| Reply (M3 CRUD 테스트) | 732 | changbal |
| Thread/Post (M4 Capstone 완료) | 735 | changbal |

---

## 설치

```bash
npm install -g @gobi-ai/cli

gobi --version    # → 2.0.35
gobi --help
gobi <command> --help

# 업데이트
gobi update       # → 최신 버전으로 자동 업데이트
```

---

> **작성자**: Changsoo (Claude Code 활용)
> **방법론**: VibeLearn AI v2.0
> **CVL 기준**: v2.0.35 (2026-06-27)
> **관련 모듈**: M1~M4 전체
