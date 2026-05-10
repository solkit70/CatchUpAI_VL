# M3 — Space Post & Reply 협업 기능

> **모듈 번호**: M3
> **상태**: 완료, CVL 업데이트 완료
> **최초 작성일**: 2026-03-29
> **CVL 업데이트**: 2026-05-10 (GOBI CLI v2.0.12)

## 이 모듈에서 배우는 것

Space 탐색, Post 생성/수정/삭제, Reply CRUD 흐름을 학습합니다. v2.0.12에서는 v0.6.x의 `Thread` 명칭이 `Post`로 바뀌었으므로 `list-threads`, `get-thread`, `create-thread` 대신 `list-posts`, `get-post`, `create-post`를 사용합니다.

## 학습 순서

| 순서 | 문서 | 설명 |
|------|------|------|
| 1 | [guides/space-navigation.md](guides/space-navigation.md) | `space list/warp/feed/list-posts/get-post` 흐름 |
| 2 | [guides/thread-management.md](guides/thread-management.md) | Post & Reply CRUD 전체 흐름과 v0.6.x 명령어 변환표 |

## M3 핵심 요약

```text
space list          -> 접근 가능한 Space 목록 확인
space warp          -> 활성 Space 선택
space feed          -> Space 통합 피드 확인
space list-posts    -> Post 목록 조회
space get-post      -> Post 본문과 Reply 조회
space create-post   -> 새 Post 작성
space create-reply  -> Post에 Reply 작성
space edit-post     -> Post 수정
space delete-post   -> Post 삭제
```

## v0.6.x에서 바뀐 점

| 이전 표현 | 현재 표현 |
|---|---|
| Thread | Post |
| `gobi space list-threads` | `gobi space list-posts` |
| `gobi space get-thread` | `gobi space get-post` |
| `gobi space create-thread` | `gobi space create-post` |
| `gobi space edit-thread` | `gobi space edit-post` |
| `gobi space delete-thread` | `gobi space delete-post` |

## M3 DoD 체크리스트

- [x] `gobi space list/warp/feed` 흐름 정리
- [x] `gobi space list-posts/get-post` 흐름 정리
- [x] `gobi space create-post/edit-post/delete-post` 흐름 정리
- [x] `gobi space create-reply/edit-reply/delete-reply` 흐름 정리
- [x] v0.6.x Thread 명령어와 v2.0.12 Post 명령어 변환표 정리
- [x] 관련 가이드 문서 v2.0.12 기준 업데이트

## 이전 / 다음 모듈

| | 모듈 | 링크 |
|--|------|------|
| 이전 | M2 — Vault/Global/Session 명령어 | [../02-Brain-Session/README.md](../02-Brain-Session/README.md) |
| 다음 | M4 — 실전 워크플로우 + Quick Reference | [../04-Capstone/README.md](../04-Capstone/README.md) |

> **방법론**: VibeLearn AI v2.0
> **작성자**: Changsoo (Claude Code 활용)
