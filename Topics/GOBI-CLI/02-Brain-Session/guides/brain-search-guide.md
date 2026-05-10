# GOBI CLI — Brain Search & Ask (v2.0 상태)

> **모듈**: M2 — Vault & Global & Session
> **작성일**: 2026-03-29
> **CVL 업데이트**: 2026-05-10 (v2.0.12 상태 반영)
> **버전**: GOBI CLI v2.0.12

> ⚠️ **v2.0 변경**: `gobi brain search` / `gobi brain ask`는 v2.0에서 **CLI 명령어 목록에서 제거됨**.
> 검색은 웹 UI(gobispace.com) 또는 `gobi global feed`를 사용하세요.

---

## 1. gobi brain search — v2.0에서 CLI 제거됨

v0.6.x 시절 공개된 Brain을 **텍스트 + 의미 기반(Semantic Similarity)**으로 검색하던 명령어.
v2.0에서는 CLI 명령어 목록에서 제거되었습니다.

### 대안

| 목적 | v2.0 대안 |
|------|----------|
| 공개 vault/brain 검색 | 웹 UI: gobispace.com |
| 팀 포스트 피드 탐색 | `gobi space feed` |
| 글로벌 피드 탐색 | `gobi global feed` |
| 토픽별 포스트 탐색 | `gobi space list-topics` → `gobi space list-topic-posts <slug>` |

### v0.6.x 실습 기록 (참고용)

```bash
# 구 명령어 — v2.0에서는 동작하지 않음
# gobi brain search --query "건강 앱"
# → similarity 최고: 0.605

# JSON 출력 구조:
# {
#   "data": [
#     { "vault": { "vaultId": "...", "name": "..." }, "similarity": 0.605 }
#   ]
# }
```

---

## 2. gobi brain ask — v2.0에서 CLI 제거됨

특정 Brain에 질문하여 Session을 생성하던 명령어. v2.0에서 CLI 목록에서 제거됨.

### 대안

| 목적 | v2.0 대안 |
|------|----------|
| Brain에 AI 질문 | 웹 UI: gobispace.com → Session 메뉴 |
| Session 목록 확인 | `gobi session list` (v2.0에서 정상 작동) |
| Session 이어가기 | `gobi session create-reply <id>` |

### v0.6.x 실습 기록 (참고용)

```bash
# 구 명령어 — v2.0에서는 동작하지 않음
# gobi brain ask \
#   --vault-slug changsoo_vault-df7y0c \
#   --question "What is this brain about?" \
#   --json

# 응답 구조:
# {
#   "session": {
#     "id": 677,
#     "sessionId": "9b73ebfd-...",
#     "mode": "manual"
#   }
# }
```

---

## 3. v2.0 Session 관리 (404 이슈 해결됨)

> ✅ v0.6.15에서 발생했던 `session list/get/reply` HTTP 404 이슈가 **v2.0에서 해결됨**

### 현재 올바른 명령어

```bash
# Session 목록 조회 (v2.0에서 정상 작동)
gobi --json session list

# Session 내용 조회
gobi --json session get <sessionId>

# Session에 답장 (v2.0: create-reply)
gobi session create-reply <sessionId> --content "후속 질문"
```

---

## 4. vault-slug 찾는 방법 (v2.0)

```bash
# 내 vault 목록에서 slug 확인
gobi --json vault list

# 결과:
# {
#   "data": [
#     { "slug": "changsoo_vault-df7y0c", "name": "Changsoo Vault" }
#   ]
# }
```

---

## 5. v2.0 지식 검색 대안 워크플로우

```
목표: 팀/커뮤니티 지식 탐색

1. 공개 피드 확인
   gobi --json global feed

2. 특정 Space 포스트 검색
   gobi --json space list-posts --space-slug <slug>

3. 토픽별 탐색
   gobi --json space list-topics
   gobi --json space list-topic-posts <topicSlug>

4. 북마크로 저장
   gobi saved create-post --source <postId>
```

---

> **작성자**: Changsoo (Claude Code 활용)
> **방법론**: VibeLearn AI v2.0
> **CVL 기준**: v2.0.12 (2026-05-10)
> **다음 문서**: [session-management.md](session-management.md)
