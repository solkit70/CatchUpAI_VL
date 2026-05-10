# GOBI CLI — Session 관리 가이드

> **모듈**: M2 — Vault & Global & Session
> **작성일**: 2026-03-29
> **CVL 업데이트**: 2026-05-10 (v2.0.12 — 404 이슈 해결, create-reply 반영)
> **버전**: GOBI CLI v2.0.12

---

## Session이란?

Brain과의 **1:1 AI 대화 세션**입니다. 웹 UI 또는 `gobi brain ask`(구 명령어)로 시작되며,
v2.0 CLI에서는 기존 세션을 조회하고 답장을 보낼 수 있습니다.

> ✅ **v2.0 개선**: v0.6.15에서 발생하던 `session list/get/reply` HTTP 404 이슈가 **해결됨**
> ⚠️ **v2.0 변경**: `gobi session reply` → `gobi session create-reply`

---

## Session 명령어 (v2.0 정상 작동)

### gobi session list

```bash
gobi session list            # 내 Session 목록 (최신 활동순)
gobi session list --limit 5  # 5개만 표시
gobi --json session list     # JSON 출력
```

**출력 예시**:
```json
{
  "success": true,
  "data": [
    {
      "id": "9b73ebfd-f32b-4171-b411-25c56f507ab1",
      "title": "What is this brain about?",
      "messageCount": 3,
      "updatedAt": "2026-05-10T..."
    }
  ]
}
```

### gobi session get

```bash
gobi session get <sessionId>             # Session 전체 내용
gobi session get <sessionId> --limit 10  # 메시지 10개만
gobi --json session get <sessionId>      # JSON 출력
```

### gobi session create-reply

```bash
# v2.0: create-reply (구 reply)
gobi session create-reply <sessionId> --content "후속 질문 내용"

# rich-text 사용 시
gobi session create-reply <sessionId> \
  --rich-text '[{"type":"text","text":"후속 질문"}]'
```

---

## Session 생성 흐름 (v2.0 기준)

v2.0 CLI에서는 `gobi brain ask`가 제거되었습니다. 새 Session은 **웹 UI**에서 시작합니다.

```
웹 UI (gobispace.com) → Session 시작
         ↓
CLI: gobi session list          → Session ID 확인
         ↓
CLI: gobi session get <id>      → 대화 내용 확인
         ↓
CLI: gobi session create-reply <id> --content "..."  → 답장
```

---

## v0.6.15 → v2.0 변경 요약

| 항목 | v0.6.15 | v2.0.12 |
|------|---------|---------|
| `session list` | ⚠️ HTTP 404 | ✅ 정상 작동 |
| `session get` | ⚠️ HTTP 404 | ✅ 정상 작동 |
| `session reply` | ⚠️ HTTP 404 | **명령어 변경**: `session create-reply` |
| 답장 옵션 | `--content` (구 `--message`) | `--content` 또는 `--rich-text` |
| Session 시작 | `gobi brain ask` | 웹 UI (CLI 제거됨) |

---

## 올바른 명령어 예시

```bash
# 1. 활성 Session 목록 확인
gobi --json session list

# 2. 특정 Session 내용 상세 조회
gobi --json session get 9b73ebfd-f32b-4171-b411-25c56f507ab1

# 3. 대화 이어가기
gobi session create-reply 9b73ebfd-f32b-4171-b411-25c56f507ab1 \
  --content "GOBI CLI v2.0의 주요 변경사항을 요약해줘"
```

---

> **작성자**: Changsoo (Claude Code 활용)
> **방법론**: VibeLearn AI v2.0
> **CVL 기준**: v2.0.12 (2026-05-10)
