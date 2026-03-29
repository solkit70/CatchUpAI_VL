# GOBI CLI — Thread & Reply 관리 가이드

> **모듈**: M3 — Space & Thread 협업 기능
> **작성일**: 2026-03-29
> **버전**: GOBI CLI v0.6.15

---

## Thread CRUD 전체 흐름

```
create-thread → get-thread 확인
     ↓
create-reply → edit-reply → delete-reply
     ↓
edit-thread
     ↓
delete-thread (필요 시)
```

---

## 1. create-thread

Space에 새 Thread를 작성합니다.

```bash
gobi space create-thread \
  --space-slug <slug> \
  --title "Thread 제목" \
  --content "Thread 본문 (마크다운 지원)"
```

### 실습 결과

```bash
gobi space create-thread \
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

---

## 2. create-reply

Thread에 답글을 작성합니다.

```bash
gobi space create-reply <threadId> \
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
#   "parentThreadId": 731,
#   "createdAt": "2026-03-29T13:47:49.049Z"
# }
```

---

## 3. edit-thread

Thread 내용을 수정합니다 (본인만 가능).

```bash
gobi space edit-thread <threadId> \
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

### 실습 결과 확인 (get-thread)

```bash
gobi space get-thread 731 --space-slug changbal

# Thread: VibeLearn AI로 GOBI CLI 학습 중입니다 👋
# By: Changsoo Park
# [수정된 본문]
#
# Replies (1 items):
#   - Changsoo Park: [수정된 reply] (수정됨)
```

---

## 5. delete-reply / delete-thread

```bash
# Reply 삭제
gobi space delete-reply <replyId> --space-slug <slug>
# → Reply 732 deleted.

# Thread 삭제 (본인만, 주의: 복구 불가)
gobi space delete-thread <threadId> --space-slug <slug>
# → Thread <id> deleted.
```

---

## 전체 명령어 옵션 요약

| 명령어 | 필수 옵션 | 선택 옵션 |
|--------|----------|----------|
| `list-threads` | `--space-slug` | `--limit`, `--cursor` |
| `get-thread <id>` | `--space-slug` | `--limit`, `--cursor` |
| `create-thread` | `--space-slug`, `--content` | `--title`, `--auto-attachments` |
| `edit-thread <id>` | `--space-slug` | `--title`, `--content` |
| `delete-thread <id>` | `--space-slug` | - |
| `create-reply <threadId>` | `--space-slug`, `--content` | `--auto-attachments` |
| `edit-reply <id>` | `--space-slug` | `--content` |
| `delete-reply <id>` | `--space-slug` | - |

---

## M2 session vs M3 thread 비교

| 항목 | session (Brain 대화) | thread (팀 토론) |
|------|---------------------|----------------|
| **대상** | AI Brain | 팀 멤버 |
| **시작** | `brain ask` | `space create-thread` |
| **답장** | `session reply` (⚠️ v0.6.15 이슈) | `space create-reply` ✅ |
| **조회** | `session get` (⚠️ 이슈) | `space get-thread` ✅ |
| **수정** | N/A | `edit-thread`, `edit-reply` ✅ |
| **삭제** | N/A | `delete-thread`, `delete-reply` ✅ |

→ **Space/Thread 명령어는 M2 Session과 달리 모두 정상 작동** ✅

---

> **작성자**: Changsoo (Claude Code 활용)
> **방법론**: VibeLearn AI v2.0
