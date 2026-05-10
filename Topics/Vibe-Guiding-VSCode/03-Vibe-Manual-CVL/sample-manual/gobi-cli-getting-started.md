---
title: "GOBI CLI Space Post Guide"
manual_id: "gobi-cli-space-create-post"
product: "GOBI CLI"
version_scope: "v2.0.12+"
difficulty: "beginner"
guide_type: "space_post"
retrieval_keywords:
  - gobi
  - space
  - post
  - create-post
  - thread
  - create-thread
deprecated_terms:
  - thread
  - create-thread
  - list-threads
  - get-thread
sources:
  - "[[Ingest/CatchUpAI_VL/Topics/GOBI-CLI/03-Space-Thread/guides/space-navigation#GOBI CLI — Space 탐색 가이드|Space Navigation]]"
  - "[[Ingest/CatchUpAI_VL/Topics/GOBI-CLI/03-Space-Thread/guides/thread-management#1. create-post|Post Management]]"
---

## Goal

GOBI CLI v2.0.12에서 Space에 새 Post를 작성한다. 사용자가 예전 표현인 Thread를 쓰더라도, 현재 명령어는 `gobi space create-post`임을 안내한다.

## When To Use

사용자가 Space에 글을 올리고 싶지만 명령어를 모를 때 사용한다. 또한 사용자가 `create-thread`, `list-threads`, `get-thread` 같은 v0.6.x 명령어를 언급할 때도 이 매뉴얼을 사용한다.

## Prerequisites

| 조건 | 확인 명령 |
|---|---|
| GOBI CLI 설치됨 | `gobi --version` |
| 인증됨 | `gobi auth status` |
| Space 접근 가능 | `gobi space list` |
| 대상 Space slug 확인 | `gobi space list` 출력의 slug |

## Steps

### 1. Space 목록 확인

```bash
gobi space list
```

출력에서 사용할 Space의 slug를 확인한다. 자동화 환경에서는 `gobi space warp`보다 각 명령어에 `--space-slug`를 직접 지정하는 방식이 더 안정적이다.

### 2. Post 생성

```bash
gobi space create-post \
  --space-slug <slug> \
  --title "Post 제목" \
  --content "Post 본문" \
  --json
```

v2.0.12에서는 `create-thread`가 아니라 `create-post`를 사용한다. 사용자가 "Thread를 만들고 싶다"고 말해도 guide response는 Post 기준 명령어를 제시해야 한다.

### 3. 생성 결과 확인

응답에서 `id`를 확인한다.

```json
{
  "id": 731,
  "title": "Post 제목",
  "replyCount": 0
}
```

### 4. Post 조회

```bash
gobi space get-post <postId> --space-slug <slug>
```

## Completion Signal

`create-post` 응답에 Post `id`가 반환되고, 같은 `id`를 `gobi space get-post <postId> --space-slug <slug>`로 조회할 수 있으면 성공이다.

## Known Failures And Fallbacks

| failure | likely cause | fallback |
|---|---|---|
| `create-thread` command not found | v0.6.x 문서를 보고 있음 | `gobi space create-post` 사용 |
| Space slug를 모름 | Space 목록을 확인하지 않음 | `gobi space list` 실행 |
| 인증 오류 | 로그인 안 됨 또는 토큰 만료 | `gobi auth login`, 이후 `gobi auth status` |
| 권한 오류 | 해당 Space 권한 없음 | 다른 Space slug 확인 또는 GOBI Web에서 권한 확인 |
| Post 생성 후 찾을 수 없음 | 다른 Space slug로 조회함 | 생성할 때 사용한 `--space-slug`와 같은 slug로 `get-post` 실행 |

## Beginner Path

초보자는 먼저 `gobi space list`로 slug를 복사한 뒤, `create-post` 명령어에 그대로 붙여 넣는다. `warp`는 인터랙티브 상태가 필요하므로 자동화나 AI Agent 작업에서는 `--space-slug`를 직접 쓰는 편이 낫다.

## Intermediate Path

중급 사용자는 `--json` 출력을 사용해 Post `id`를 후속 `get-post`, `create-reply`, `edit-post` 명령어에 넘긴다. M4 POC에서는 이 `id` 반환 여부를 completion signal로 사용한다.

## Source Notes

이 매뉴얼은 `Topics/GOBI-CLI/03-Space-Thread/guides/space-navigation.md`와 `Topics/GOBI-CLI/03-Space-Thread/guides/thread-management.md`의 v2.0.12 CVL 업데이트를 기준으로 한다. 구 Thread 명령어는 retrieval keyword로만 유지하고, 실제 guide response에는 Post 명령어를 사용한다.
