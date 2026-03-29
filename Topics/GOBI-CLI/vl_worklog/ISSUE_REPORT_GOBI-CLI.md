# GOBI CLI 이슈 리포트

> **Topic**: GOBI-CLI
> **CLI 버전**: v0.6.15
> **발견일**: 2026-03-29
> **보고자**: Changsoo Park
> **환경**: Windows 11, Node.js v22.15.0, npm v11.6.2

---

## 이슈 목록

| ID | 발견 모듈 | 명령어 | 심각도 | 상태 |
|----|----------|--------|--------|------|
| [#1](#issue-1) | M1 | `gobi session update` | Medium | 확인됨 |
| [#2](#issue-2) | M2 | `gobi session list/get/reply` | High | 확인됨 |
| [#3](#issue-3) | M2 | `gobi session reply --message` | Low | 확인됨 |

---

## Issue #1 — session update 명령어 미존재 {#issue-1}

**발견일**: 2026-03-29 (M1)
**심각도**: Medium

### 현상

Roadmap 및 공식 문서에 `gobi session update` 명령어가 명시되어 있으나, CLI v0.6.15에서 실제로 존재하지 않음.

```bash
gobi session --help

# 실제 출력:
# Commands:
#   get [options] <sessionId>
#   list [options]
#   reply [options] <sessionId>
#   help [command]

# → update 명령어 없음
```

### 기대 동작

```bash
gobi session update <sessionId> --title "새 제목"
# Session 제목을 수정할 수 있어야 함
```

### 영향

- Session 제목 변경 불가
- Roadmap의 학습 목표 중 "session update 실습" 달성 불가

### 권장 조치

- GOBI 팀: CLI에 `session update` 명령어 추가 또는 문서에서 제거
- 학습자: `gobi session --help`로 실제 사용 가능한 명령어 먼저 확인

---

## Issue #2 — session list / get / reply → HTTP 404 {#issue-2}

**발견일**: 2026-03-29 (M2)
**심각도**: High

### 현상

`gobi brain ask`로 Session 생성은 성공하지만, 이후 Session 조회/답장 명령어가 모두 HTTP 404를 반환함.

```bash
# Session 생성 → 성공
gobi brain ask --vault-slug changsoo_vault-df7y0c --question "질문"
# → Session ID: 677 생성 완료

# Session 목록 조회 → 실패
gobi session list
# Error: API error (HTTP 404): Cannot GET /chat/my-sessions?limit=20

# Session 내용 조회 → 실패
gobi session get 677
# Error: API error (HTTP 404): Cannot GET /chat/677?limit=20

# Session 답장 → 실패
gobi session reply 677 --content "후속 질문"
# Error: API error (HTTP 404): Cannot POST /chat/677/reply
```

### 추가 확인

UUID 형식으로도 시도했으나 동일하게 404:
```bash
gobi session get 9b73ebfd-f32b-4171-b411-25c56f507ab1
# Error: API error (HTTP 404): Cannot GET /chat/9b73ebfd-f32b-4171-b411-25c56f507ab1?limit=20
```

### 원인 추정

- CLI v0.6.15의 session 관련 API 엔드포인트(`/chat/...`)가 서버의 실제 엔드포인트와 불일치
- `gobi brain ask`는 다른 엔드포인트를 사용하여 정상 작동
- 서버 API가 업데이트되었으나 CLI가 아직 구버전 엔드포인트를 사용하는 것으로 추정

### 영향

- CLI에서 Session 멀티턴 대화 완전 불가
- Session 내용 확인 불가
- Brain ask로 시작한 대화를 이어갈 방법 없음 (CLI에서)

### 우회 방법

- 웹 플랫폼(https://www.gobispace.com)에서 Session 메뉴를 통해 대화 내용 확인 및 답장 가능

### 권장 조치

- GOBI 팀: CLI session 관련 엔드포인트를 현재 서버 API에 맞게 업데이트 필요
- GitHub 이슈 보고 권장: https://github.com/gobi-ai/gobi-cli/issues

---

## Issue #3 — session reply 옵션 오류 (--message → --content) {#issue-3}

**발견일**: 2026-03-29 (M2)
**심각도**: Low (문서 오류)

### 현상

여러 학습 자료(Roadmap 포함)에 `gobi session reply`의 옵션이 `--message`로 안내되어 있으나, 실제 CLI의 올바른 옵션은 `--content`임.

```bash
# ❌ 잘못된 옵션 (에러 발생)
gobi session reply <sessionId> --message "내용"
# error: unknown option '--message'

# ✅ 올바른 옵션
gobi session reply <sessionId> --content "내용"
```

### 실제 help 출력

```
Usage: gobi session reply [options] <sessionId>

Send a human reply to a session you are a member of.

Options:
  --content <content>     Reply content (markdown supported)
  --rich-text <richText>  Rich-text JSON array
  -h, --help              display help for command
```

### 영향

- `--message` 옵션을 사용하는 학습자는 에러 발생
- 가이드 문서의 신뢰도 저하

### 권장 조치

- 학습 문서: `--message` → `--content`로 수정 (본 리포트의 session-management.md에 이미 반영됨)
- GOBI 팀: 공식 문서/예제에서 `--message` 사용 여부 점검

---

## 추가 관찰 사항 (이슈는 아님)

### 관찰 1: gobi init 인터랙티브 전용

`gobi init`은 파이프/자동화 환경에서 실행 불가. 반드시 인터랙티브 터미널에서 실행해야 함.

```bash
gobi init --json
# Error: User force closed the prompt with 0 null
```

→ CI/CD 환경에서의 자동화 사용 시 주의 필요

### 관찰 2: Roadmap에 없던 명령어 발견 (M1)

v0.6.15에 `gobi sense`와 `gobi sync` 명령어가 추가됨 (Roadmap 미반영).

| 명령어 | 기능 |
|--------|------|
| `gobi sense activities` | 활동 기록 조회 |
| `gobi sense transcriptions` | 전사 기록 조회 |
| `gobi sync` | 로컬 ↔ Webdrive 파일 동기화 |

### 관찰 3: brain list-updates는 전체 사용자 피드

`gobi brain list-updates`는 본인 업데이트만 아닌 **전체 팀/커뮤니티 피드**를 반환함. 본인 업데이트만 보려면 웹 플랫폼 사용 필요.

---

## GitHub 이슈 보고 대상

아래 이슈들은 GOBI CLI GitHub에 보고할 가치 있음:

1. **Issue #2** (High): `session list/get/reply` HTTP 404 → 핵심 기능 장애
2. **Issue #1** (Medium): `session update` 명령어 미존재

**GitHub Issues**: https://github.com/gobi-ai/gobi-cli/issues

---

> **작성자**: Changsoo (Claude Code 활용)
> **방법론**: VibeLearn AI v2.0
> **마지막 업데이트**: 2026-03-29
