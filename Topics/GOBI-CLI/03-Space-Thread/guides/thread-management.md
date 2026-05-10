# GOBI CLI — Post & Reply 관리 가이드

> **모듈**: M3 — Space & Post 협업 기능
> **작성일**: 2026-03-29
> **CVL 업데이트**: 2026-05-10 (v2.0.12 — Thread → Post 명칭 변경)
> **버전**: GOBI CLI v2.0.12

> ⚠️ **v2.0 Breaking Change**: `thread` → `post` 전면 변경
> `create-thread` → `create-post`, `get-thread` → `get-post` 등 모든 명령어 영향.

---

## Post CRUD 전체 흐름

```
create-post → get-post 확인
     ↓
create-reply → edit-reply → delete-reply
     ↓
edit-post
     ↓
delete-post (필요 시)
```

---

## 1. create-post

Space에 새 Post를 작성합니다.

```bash
gobi space create-post \
  --space-slug <slug> \
  --title "Post 제목" \
  --content "Post 본문 (마크다운 지원)"
```

### 실습 결과 (원본 기록 보존)

```bash
# 원본 실습은 v0.6.15 create-thread로 작성됨 (2026-03-29)
# v2.0 동등 명령어:
gobi space create-post \
  --space-slug changbal \
  --title "VibeLearn AI로 GOBI CLI 학습 중입니다 👋" \
  --content "안녕하세요! ..." \
  --json

# 응답:
# {
#   "id": 731,
#   "title": "VibeLearn AI로 GOBI CLI 학습 중입니다 👋",
#   "replyCount": 0,
#   "createdAt": "2026-03-29T13:47:40.049Z"
# }
```

**반환값 핵심**: `id` → 이후 reply/edit/delete에 사용

### 추가 옵션 (v2.0 신규)

```bash
gobi space create-post \
  --vault-slug changsoo_vault-df7y0c \   # vault에 귀속
  --auto-attachments \                    # [[wikilinks]] 자동 업로드
  --draft-id <id>                         # draft와 연결
```

---

## 2. create-reply

Post에 답글을 작성합니다.

```bash
gobi space create-reply <postId> \
  --space-slug <slug> \
  --content "답글 내용 (마크다운 지원)"
```

### 실습 결과

```bash
gobi space create-reply 731 \
  --space-slug changbal \
  --content "CRUD 테스트 중입니다. ✅" \
  --json

# 응답:
# {
#   "id": 732,
#   "content": "CRUD 테스트 중입니다. ✅",
#   "parentPostId": 731,
#   "createdAt": "2026-03-29T13:47:49.049Z"
# }
```

---

## 3. edit-post

Post 내용을 수정합니다 (본인만 가능).

```bash
gobi space edit-post <postId> \
  --space-slug <slug> \
  --title "수정된 제목" \
  --content "수정된 내용"
```

> `--title`과 `--content` 중 하나만 수정해도 됩니다.

---

## 4. edit-reply

Reply 내용을 수정합니다 (본인만 가능).

```bash
gobi space edit-reply <replyId> \
  --space-slug <slug> \
  --content "수정된 내용"
```

### 실습 결과 확인 (get-post)

```bash
gobi space get-post 731 --space-slug changbal

# Post: VibeLearn AI로 GOBI CLI 학습 중입니다 👋
# By: Changsoo Park
# [수정된 본문]
#
# Replies (1 items):
#   - Changsoo Park: [수정된 reply] (수정됨)
```

---

## 5. delete-reply / delete-post

```bash
# Reply 삭제
gobi space delete-reply <replyId> --space-slug <slug>
# → Reply 732 deleted.

# Post 삭제 (본인만, 주의: 복구 불가)
gobi space delete-post <postId> --space-slug <slug>
# → Post <id> deleted.
```

---

## 전체 명령어 옵션 요약

| 명령어 | 필수 옵션 | 선택 옵션 |
|--------|----------|----------|
| `list-posts` | `--space-slug` | `--limit`, `--cursor` |
| `get-post <id>` | `--space-slug` | `--limit`, `--cursor`, `--full` |
| `create-post` | `--space-slug`, `--content` | `--title`, `--vault-slug`, `--auto-attachments`, `--draft-id` |
| `edit-post <id>` | `--space-slug` | `--title`, `--content`, `--vault-slug` |
| `delete-post <id>` | `--space-slug` | - |
| `create-reply <postId>` | `--space-slug`, `--content` | `--vault-slug`, `--auto-attachments` |
| `edit-reply <id>` | `--space-slug` | `--content` |
| `delete-reply <id>` | `--space-slug` | - |

---

## v2.0 명령어 변환 빠른 참조

| 구 명령어 (v0.6.x) | 새 명령어 (v2.0+) |
|-------------------|------------------|
| `space list-threads` | `space list-posts` |
| `space get-thread <id>` | `space get-post <id>` |
| `space create-thread` | `space create-post` |
| `space edit-thread <id>` | `space edit-post <id>` |
| `space delete-thread <id>` | `space delete-post <id>` |

---

## M2 session vs M3 post 비교 (v2.0 기준)

| 항목 | session (1:1 대화) | post (커뮤니티 토론) |
|------|-------------------|---------------------|
| **대상** | 개인 대화 | Space 멤버 전체 |
| **시작** | `gobi brain ask` (웹 UI) | `space create-post` |
| **답장** | `session create-reply` | `space create-reply` ✅ |
| **조회** | `session get` | `space get-post` ✅ |
| **수정** | N/A | `edit-post`, `edit-reply` ✅ |
| **삭제** | N/A | `delete-post`, `delete-reply` ✅ |

---

> **작성자**: Changsoo (Claude Code 활용)
> **방법론**: VibeLearn AI v2.0
> **CVL 기준**: v2.0.12 (2026-05-10)
