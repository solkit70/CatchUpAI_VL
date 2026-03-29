# GOBI CLI — Space 탐색 가이드

> **모듈**: M3 — Space & Thread 협업 기능
> **작성일**: 2026-03-29
> **버전**: GOBI CLI v0.6.15

---

## Space란?

Vault 내 **팀 협업 공간**입니다. 관련 Brain과 Thread를 묶는 단위로,
GitHub Repository 또는 Slack 채널에 비유할 수 있습니다.

---

## gobi space list

내가 멤버로 속한 Space 목록을 조회합니다.

```bash
gobi space list
gobi space list --json
```

### 실습 결과 (2026-03-29)

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
gobi space list-threads --space-slug changbal
gobi space create-thread --space-slug gobi --title "제목"
```

---

## gobi space list-threads

Space의 Thread 목록을 조회합니다.

```bash
gobi space list-threads --space-slug <slug>
gobi space list-threads --space-slug <slug> --limit 5
gobi space list-threads --space-slug <slug> --json
```

### 일반 출력 vs JSON 출력 비교

**일반 출력:**
```
Threads (9 items):
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
  "primaryVault": {...},      ← 작성자의 Brain 정보
  "editedAt": null,
  "createdAt": "2026-03-16T..."
}
```

### 페이지네이션

```bash
# 다음 페이지 (cursor 값은 이전 응답의 마지막 항목 날짜)
gobi space list-threads --space-slug gobi \
  --cursor "2026-03-28T00:27:27.492Z"
```

---

## gobi space get-thread

특정 Thread의 내용과 모든 Reply를 조회합니다.

```bash
gobi space get-thread <threadId> --space-slug <slug>
gobi space get-thread <threadId> --space-slug <slug> --limit 10
```

### 실습 결과

```bash
gobi space get-thread 123 --space-slug changbal

# 출력:
# Thread: 지금의 직장 생활을 계속 하는게 나을까요?
# By: Changsoo Park on 2026-03-16T20:22:21.752Z
#
# [본문 내용]
#
# Replies (2 items):
#   - Jin Young Kim: 저도 공감합니다... (2026-03-19T...)
#   - Minsuk Kang: AI와 전쟁중입니다. ㅎㅎ (2026-03-17T...)
```

---

> **다음 문서**: [thread-management.md](thread-management.md)
> **작성자**: Changsoo (Claude Code 활용)
> **방법론**: VibeLearn AI v2.0
