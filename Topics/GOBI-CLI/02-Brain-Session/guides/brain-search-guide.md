# GOBI CLI — Brain Search & Ask 가이드

> **모듈**: M2 — Brain & Session 명령어 마스터
> **작성일**: 2026-03-29
> **버전**: GOBI CLI v0.6.15

---

## 1. gobi brain search

공개된 Brain을 **텍스트 + 의미 기반(Semantic Similarity)**으로 검색합니다.

### 기본 사용법

```bash
gobi brain search --query "검색어"
gobi brain search --query "검색어" --json    # JSON 출력
```

### 실습 결과 (2026-03-29)

```bash
# 영어 검색
gobi brain search --query "getting started"
# → similarity 최고: 0.409 (낮은 편)

# 한국어 검색
gobi brain search --query "건강 앱"
# → similarity 최고: 0.605 (높음 — 내용이 일치할수록 상승)

# 기술 검색
gobi brain search --query "CLI tool"
# → similarity 최고: 0.396
```

### 출력 구조 (JSON)

```json
{
  "success": true,
  "data": [
    {
      "vault": {
        "id": 70,
        "vaultId": "happy-light-dz3ttx",
        "name": "Happy Light",
        "description": "...",
        "tags": ["profile"]
      },
      "owner": {
        "id": 25,
        "name": "이문기"
      },
      "similarity": 0.605
    }
  ]
}
```

### 핵심 인사이트

| 발견 | 내용 |
|------|------|
| **의미 기반 검색** | 키워드 일치보다 의미 유사도로 랭킹 |
| **한국어 우수** | 한국어 쿼리가 한국어 Brain에서 훨씬 높은 similarity |
| **항상 20개 반환** | 페이지네이션 없이 고정 20개 |
| **공개 Brain만** | 비공개 Brain은 검색 불가 |

---

## 2. gobi brain ask

특정 Brain에 질문하여 **새로운 Session을 생성**합니다.

### 기본 사용법

```bash
gobi brain ask \
  --vault-slug <vaultSlug> \
  --question "질문 내용"

# 옵션
gobi brain ask \
  --vault-slug <vaultSlug> \
  --question "질문" \
  --mode auto        # auto(기본값) 또는 manual
```

### 실습 결과

```bash
gobi brain ask \
  --vault-slug changsoo_vault-df7y0c \
  --question "What is this brain about?" \
  --json

# 응답:
{
  "session": {
    "id": 677,
    "sessionId": "9b73ebfd-f32b-4171-b411-25c56f507ab1",   ← UUID
    "mode": "manual",
    "messageCount": 0
  },
  "userMessage": {
    "id": "13a3d6a7-...",
    "content": "What is this brain about?",
    "role": "user"
  }
}
```

### 중요: Session ID 형식

`gobi brain ask` 는 **두 가지 ID**를 반환합니다:

| 필드 | 형식 | 예시 |
|------|------|------|
| `session.id` | 숫자 | `677` |
| `session.sessionId` | UUID | `9b73ebfd-f32b-4171-b411-25c56f507ab1` |

> ⚠️ `gobi session reply/get`에서 사용할 정확한 ID 형식은 이슈 섹션 참조

### vault-slug 찾는 방법

```bash
# brain search 결과의 vaultId 필드가 vault-slug
gobi brain search --query "내 이름" --json
# → data[].vault.vaultId 값 사용
```

---

## 3. 알려진 이슈 (v0.6.15)

### ⚠️ session list / get / reply → HTTP 404

```bash
gobi session list
# Error: API error (HTTP 404): Cannot GET /chat/my-sessions?limit=20

gobi session get 677
# Error: API error (HTTP 404): Cannot GET /chat/677?limit=20

gobi session reply 677 --content "..."
# Error: API error (HTTP 404): Cannot POST /chat/677/reply
```

**원인 추정**: CLI v0.6.15의 session 관련 API 엔드포인트가 서버와 불일치
**확인 방법**: gobispace.com 웹에서 생성된 session 직접 확인
**우회 방법**: 웹 플랫폼(gobispace.com)에서 session 관리

---

> **다음 문서**: [session-management.md](session-management.md)
> **작성자**: Changsoo (Claude Code 활용)
> **방법론**: VibeLearn AI v2.0
