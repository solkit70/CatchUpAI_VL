# M2 — Vault/Global/Personal 명령어

> **모듈 번호**: M2
> **상태**: 완료, CVL 업데이트 완료
> **최초 작성일**: 2026-03-29
> **CVL 업데이트**: 2026-06-27 (GOBI CLI v2.0.35 — session CLI 제거, personal로 대체)

## 이 모듈에서 배우는 것

v0.6.x의 `brain` 중심 명령어가 v2.0.12에서 `vault`, `global` 중심으로, v2.0.35에서 `personal`, `artifact`가 추가되며 재편된 흐름을 학습합니다.

> ⚠️ **v2.0.35 주의**: `session` 명령어 전체가 CLI에서 제거됨.
> 이 모듈의 session 관련 내용은 역사적 기록이며, 현재는 웹 UI에서만 1:1 AI 대화가 가능합니다.

## 학습 순서

| 순서 | 문서 | 설명 |
|------|------|------|
| 1 | [guides/brain-search-guide.md](guides/brain-search-guide.md) | `brain search/ask` CLI 제거 이후의 대안 검색/대화 워크플로우 |
| 2 | [guides/brain-publish-guide.md](guides/brain-publish-guide.md) | `PUBLISH.md` 작성, `vault publish`, `global create-post` 흐름 |
| 3 | [guides/session-management.md](guides/session-management.md) | ⚠️ session은 v2.0.35에서 CLI 제거됨 — 역사적 참고용 |
| 4 | [examples/sample-brain.md](examples/sample-brain.md) | 과거 `BRAIN.md` 템플릿. v2.0에서는 `PUBLISH.md`로 변환해서 참고 |

## M2 핵심 요약 (v2.0.35 기준)

```text
vault publish        -> PUBLISH.md를 Vault 프로필로 발행
global create-post   -> 공개 피드에 개인 포스트 작성
global list-posts    -> 내 포스트 또는 글로벌 피드 조회
personal create-post -> 프라이빗 메모/포스트 작성 (나만 보임) [v2.0.35 신규]
personal feed        -> 내 프라이빗 피드 조회 [v2.0.35 신규]

── v2.0.35에서 CLI 제거됨 ──
session list/get/create-reply  -> ❌ 웹 UI에서만 가능
saved create-note              -> ❌ personal create-post로 대체
draft add/list                 -> ❌ 웹 UI에서만 가능
```

## 버전별 변경 이력

| 이전 표현 | v2.0.12 표현 | v2.0.35 (현재) |
|---|---|---|
| `gobi brain publish` | `gobi vault publish` | 동일 |
| `BRAIN.md` | `PUBLISH.md` | 동일 |
| `gobi brain post-update` | `gobi global create-post` | 동일 |
| `gobi brain list-updates` | `gobi global list-posts --mine` | 동일 |
| `gobi session reply` | `gobi session create-reply` | **CLI 전체 제거** |
| (없음) | `gobi saved create-note` | **CLI 전체 제거** → `personal create-post` |
| (없음) | (없음) | `gobi personal *` 신규 추가 |

## M2 DoD 체크리스트

- [x] `brain search/ask` 제거 또는 웹 UI 전환 상태 정리
- [x] `PUBLISH.md`와 `gobi vault publish` 흐름 정리
- [x] `global create-post/list-posts/edit-post/delete-post` 흐름 정리
- [x] `session list/get/create-reply` 흐름 정리 (v2.0.12 기준)
- [x] v0.6.15 session 404 이슈가 v2.0.12에서 해결됐다가 v2.0.35에서 CLI 전체 제거된 경위 정리
- [x] `personal` 명령어 신규 추가 반영 (v2.0.35)
- [x] 관련 가이드 문서 v2.0.35 기준 업데이트

## 이전 / 다음 모듈

| | 모듈 | 링크 |
|--|------|------|
| 이전 | M1 — 설치 & 인증 & 핵심 개념 | [../01-Setup-Auth/README.md](../01-Setup-Auth/README.md) |
| 다음 | M3 — Space Post & Reply 협업 기능 | [../03-Space-Thread/README.md](../03-Space-Thread/README.md) |

> **방법론**: VibeLearn AI v2.0
> **작성자**: Changsoo (Claude Code 활용)
