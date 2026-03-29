# GOBI CLI — Session 관리 가이드

> **모듈**: M2 — Brain & Session 명령어 마스터
> **작성일**: 2026-03-29
> **버전**: GOBI CLI v0.6.15

---

## Session이란?

`gobi brain ask`로 시작되는 **Brain과의 1:1 AI 대화 세션**입니다.

```
gobi brain ask  →  Session 생성  →  gobi session reply  →  대화 계속
```

---

## Session 명령어 (v0.6.15 상태)

### gobi session list

```bash
gobi session list            # 내 Session 목록
gobi session list --limit 5  # 5개만 표시
```

> ⚠️ **v0.6.15 이슈**: HTTP 404 반환 — API 엔드포인트 불일치

### gobi session get

```bash
gobi session get <sessionId>             # Session 내용 조회
gobi session get <sessionId> --limit 10  # 메시지 10개만
```

> ⚠️ **v0.6.15 이슈**: HTTP 404 반환

### gobi session reply

```bash
gobi session reply <sessionId> --content "후속 질문"
```

> ⚠️ **v0.6.15 이슈**: HTTP 404 반환

---

## Session 생성 흐름 (brain ask)

```bash
# 1. Session 생성
gobi brain ask \
  --vault-slug <vaultSlug> \
  --question "첫 번째 질문" \
  --json

# JSON 응답에서 sessionId 확인:
# "session": {
#   "id": 677,                                        ← 숫자 ID
#   "sessionId": "9b73ebfd-f32b-4171-b411-25c56f507ab1"  ← UUID
# }

# 2. 대화 이어가기 (정상 작동 시)
gobi session reply 677 --content "Tell me more..."

# 3. 대화 내용 확인 (정상 작동 시)
gobi session get 677
```

---

## v0.6.15 이슈 상세

### 이슈 요약

| 명령어 | 기대 동작 | 실제 결과 |
|--------|----------|----------|
| `gobi session list` | Session 목록 반환 | HTTP 404 |
| `gobi session get <id>` | Session 내용 반환 | HTTP 404 |
| `gobi session reply <id>` | 답장 전송 | HTTP 404 |
| `gobi brain ask` | Session 생성 | ✅ 정상 작동 |

### 오류 메시지

```
Error: API error (HTTP 404): Cannot GET /chat/my-sessions?limit=20
Error: API error (HTTP 404): Cannot GET /chat/677?limit=20
Error: API error (HTTP 404): Cannot POST /chat/677/reply
```

### 원인 분석

- `gobi brain ask` → Session **생성은 성공** (ID 677, 678 반환 확인)
- session 조회/답장 관련 API 엔드포인트가 서버에서 변경된 것으로 추정
- CLI v0.6.15가 구버전 엔드포인트를 사용 중

### 우회 방법

1. **웹 플랫폼**: https://www.gobispace.com → Session 메뉴에서 관리
2. **GitHub 이슈**: https://github.com/gobi-ai/gobi-cli/issues 에 보고

---

## 올바른 session reply 옵션 (Roadmap 수정 사항)

Roadmap에는 `--message` 플래그로 나와 있었으나 실제는 `--content`:

```bash
# ❌ Roadmap의 잘못된 예시
gobi session reply <id> --message "내용"

# ✅ 실제 올바른 옵션
gobi session reply <id> --content "내용"
```

---

> **작성자**: Changsoo (Claude Code 활용)
> **방법론**: VibeLearn AI v2.0
