# M2 — Vault/Global/Session 명령어

> **모듈 번호**: M2
> **상태**: 완료, CVL 업데이트 완료
> **최초 작성일**: 2026-03-29
> **CVL 업데이트**: 2026-05-10 (GOBI CLI v2.0.12)

## 이 모듈에서 배우는 것

v0.6.x의 `brain` 중심 명령어가 v2.0.12에서 어떻게 `vault`, `global`, `session` 중심으로 재편되었는지 학습합니다. `BRAIN.md`와 `brain publish`가 아니라 `PUBLISH.md`와 `gobi vault publish`를 기준으로 문서를 읽어야 합니다.

## 학습 순서

| 순서 | 문서 | 설명 |
|------|------|------|
| 1 | [guides/brain-search-guide.md](guides/brain-search-guide.md) | `brain search/ask` CLI 제거 이후의 대안 검색/대화 워크플로우 |
| 2 | [guides/brain-publish-guide.md](guides/brain-publish-guide.md) | `PUBLISH.md` 작성, `vault publish`, `global create-post` 흐름 |
| 3 | [guides/session-management.md](guides/session-management.md) | `session list/get/create-reply` 사용과 v2.0.12 변경점 |
| 4 | [examples/sample-brain.md](examples/sample-brain.md) | 과거 `BRAIN.md` 템플릿. v2.0에서는 `PUBLISH.md`로 변환해서 참고 |

## M2 핵심 요약

```text
vault publish       -> PUBLISH.md를 Vault 프로필로 발행
global create-post  -> 개인/글로벌 피드에 포스트 작성
global list-posts   -> 내 포스트 또는 글로벌 피드 조회
session list/get    -> 1:1 AI 대화 확인
session create-reply -> 기존 Session에 답장
```

## v0.6.x에서 바뀐 점

| 이전 표현 | 현재 표현 |
|---|---|
| `gobi brain publish` | `gobi vault publish` |
| `BRAIN.md` | `PUBLISH.md` |
| `gobi brain post-update` | `gobi global create-post` |
| `gobi brain list-updates` | `gobi global list-posts --mine` |
| `gobi session reply` | `gobi session create-reply` |

## M2 DoD 체크리스트

- [x] `brain search/ask` 제거 또는 웹 UI 전환 상태 정리
- [x] `PUBLISH.md`와 `gobi vault publish` 흐름 정리
- [x] `global create-post/list-posts/edit-post/delete-post` 흐름 정리
- [x] `session list/get/create-reply` 흐름 정리
- [x] v0.6.15 session 404 이슈가 v2.0.12 기준에서 어떻게 달라졌는지 정리
- [x] 관련 가이드 문서 v2.0.12 기준 업데이트

## 이전 / 다음 모듈

| | 모듈 | 링크 |
|--|------|------|
| 이전 | M1 — 설치 & 인증 & 핵심 개념 | [../01-Setup-Auth/README.md](../01-Setup-Auth/README.md) |
| 다음 | M3 — Space Post & Reply 협업 기능 | [../03-Space-Thread/README.md](../03-Space-Thread/README.md) |

> **방법론**: VibeLearn AI v2.0
> **작성자**: Changsoo (Claude Code 활용)
