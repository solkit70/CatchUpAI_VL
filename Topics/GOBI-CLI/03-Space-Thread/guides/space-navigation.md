# GOBI CLI — Space 탐색 가이드

> **모듈**: M3 — Space & Post 협업 기능
> **작성일**: 2026-03-29
> **CVL 업데이트**: 2026-05-10 (v2.0.12 — Thread→Post 전면 변경, 신규 명령어 반영)
> **버전**: GOBI CLI v2.0.12

> ⚠️ **v2.0 Breaking Change**: `Thread` → `Post` 전면 명칭 변경
> - `list-threads` → `list-posts`
> - `get-thread` → `get-post`
> - `create-thread` → `create-post`
> - `edit-thread` → `edit-post`
> - `delete-thread` → `delete-post`

---

## Space란?

팀 협업 커뮤니티 공간입니다. **Post(포스트)와 Reply(답글)**로 소통하며,
GitHub Issues 또는 Slack 채널에 비유할 수 있습니다.

> **v2.0 변경**: `Thread` → `Post` (명칭 전면 변경)

---

## gobi space list

내가 멤버로 속한 Space 목록을 조회합니다.

```bash
gobi space list
gobi --json space list
```

### 실습 결과 (2026-03-29 기록, v2.0에서도 동일)

```
Spaces (3):
- [changbal] Changbal (창발)
    → 미국 시애틀 IT 전문가 커뮤니티. "창의와 발명", "창발"의 의미
- [gobi] Gobi
    → GOBI 플랫폼 공식 Space
- [cmds] CMDSPACE
    → 커맨드스페이스 by 구요한
```

### JSON 구조 핵심 필드

```json
{
  "slug": "changbal",        ← --space-slug에 사용
  "name": "Changbal (창발)",
  "description": "..."
}
```

---

## gobi space warp

활성 Space를 선택합니다. 선택 후 `--space-slug` 없이도 명령어 실행 가능합니다.

```bash
# 인터랙티브 선택
gobi space warp

# slug 직접 지정 (인터랙티브 불필요)
gobi space warp changbal
```

> **주의**: `warp`는 인터랙티브 터미널에서만 정상 작동.
> 자동화 환경에서는 `--space-slug` 옵션을 각 명령어에 직접 지정 권장.

### --space-slug 전역 옵션

Space를 선택하지 않아도 `--space-slug`를 각 명령어에 직접 지정 가능:

```bash
gobi space list-posts --space-slug changbal
gobi space create-post --space-slug gobi --title "제목"
```

---

## gobi space feed

Space의 **통합 피드**를 최신순으로 조회합니다. (v2.0 신규)

```bash
gobi space feed
gobi --json space feed
gobi space feed --space-slug changbal
```

---

## gobi space list-posts

Space의 Post 목록을 조회합니다. (구 `list-threads`)

```bash
gobi space list-posts --space-slug <slug>
gobi space list-posts --space-slug <slug> --limit 5
gobi --json space list-posts --space-slug <slug>
```

### 일반 출력 vs JSON 출력 비교

**일반 출력:**
```
Posts (9 items):
- [123] "직장 생활을 계속 하는게 나을까요?" by Changsoo Park (2 replies)
- [214] "[TMI] 오늘 발표 중 가장 쓸데없지만..." by Minsuk Kang (1 replies)
```

**JSON 출력 (추가 정보):**
```json
{
  "id": 123,
  "title": "...",
  "richText": [...],          ← 서식 있는 텍스트
  "topics": [                 ← AI가 분류한 토픽 태그
    {"name": "AI", "slug": "ai"}
  ],
  "replyCount": 2,
  "primaryVault": {...},      ← 작성자의 Vault 정보
  "editedAt": null,
  "createdAt": "2026-03-16T..."
}
```

### 페이지네이션

```bash
# 다음 페이지 (cursor 값은 이전 응답의 마지막 항목 날짜)
gobi space list-posts --space-slug gobi \
  --cursor "2026-03-28T00:27:27.492Z"
```

---

## gobi space get-post

특정 Post의 내용과 모든 Reply를 조회합니다. (구 `get-thread`)

```bash
gobi space get-post <postId> --space-slug <slug>
gobi space get-post <postId> --space-slug <slug> --limit 10
```

### 실습 결과 (v0.6.x 기록 — 명령어만 변경됨)

```bash
gobi space get-post 123 --space-slug changbal

# 출력:
# Post: 지금의 직장 생활을 계속 하는게 나을까요?
# By: Changsoo Park on 2026-03-16T20:22:21.752Z
#
# [본문 내용]
#
# Replies (2 items):
#   - Jin Young Kim: 저도 공감합니다... (2026-03-19T...)
#   - Minsuk Kang: AI와 전쟁중입니다. ㅎㅎ (2026-03-17T...)
```

---

## gobi space list-topics

Space에서 사용되는 **토픽 태그 목록**을 조회합니다. (v2.0 신규)

```bash
gobi --json space list-topics --space-slug changbal
```

---

## gobi space list-topic-posts

특정 토픽의 Post 목록을 조회합니다. (v2.0 신규)

```bash
gobi --json space list-topic-posts <topicSlug> --space-slug changbal
```

---

## v0.6.x → v2.0 명령어 변환표

| 구 명령어 (v0.6.x) | 새 명령어 (v2.0) |
|-------------------|----------------|
| `space list-threads` | `space list-posts` |
| `space get-thread <id>` | `space get-post <id>` |
| `space create-thread` | `space create-post` |
| `space edit-thread <id>` | `space edit-post <id>` |
| `space delete-thread <id>` | `space delete-post <id>` |
| (없음) | `space feed` (신규) |
| (없음) | `space list-topics` (신규) |
| (없음) | `space list-topic-posts <slug>` (신규) |

---

> **다음 문서**: [thread-management.md](thread-management.md)
> **작성자**: Changsoo (Claude Code 활용)
> **방법론**: VibeLearn AI v2.0
> **CVL 기준**: v2.0.12 (2026-05-10)
