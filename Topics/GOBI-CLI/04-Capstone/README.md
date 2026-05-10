# M4 — 실전 워크플로우 + Quick Reference

> **모듈 번호**: M4
> **상태**: 완료, CVL 업데이트 완료
> **최초 작성일**: 2026-03-29
> **CVL 업데이트**: 2026-05-10 (GOBI CLI v2.0.12)

## 이 모듈에서 배우는 것

M1~M3에서 배운 명령어를 연결해 v2.0.12 기준 End-to-End 워크플로우를 구성합니다. 현재 기준 워크플로우는 `auth status`, `global feed`, `session list/get/create-reply`, `space create-post`, `global create-post`, `vault sync`를 중심으로 합니다.

## 학습 순서

| 순서 | 문서 | 설명 |
|------|------|------|
| 1 | [guides/complete-workflow.md](guides/complete-workflow.md) | v2.0.12 기준 6단계 E2E 시나리오와 트러블슈팅 |
| 2 | [guides/quick-reference.md](guides/quick-reference.md) | 전체 명령어 한 페이지 참조 |

## M4 핵심 요약

```text
Step 1: gobi auth status
Step 2: gobi global feed / gobi space feed
Step 3: gobi session list/get/create-reply
Step 4: gobi space create-post / create-reply
Step 5: gobi global create-post
Step 6: gobi vault sync
```

## M4 DoD 체크리스트

- [x] `gobi auth status` 인증 확인 흐름 정리
- [x] `gobi global feed`와 `gobi space feed` 확인 흐름 정리
- [x] `gobi session list/get/create-reply` 대화 흐름 정리
- [x] `gobi space create-post/create-reply` 협업 게시 흐름 정리
- [x] `gobi global create-post` 공유 흐름 정리
- [x] `gobi vault sync` 파일 동기화 흐름 정리
- [x] `complete-workflow.md` v2.0.12 기준 업데이트
- [x] `quick-reference.md` v2.0.12 기준 업데이트

## 이전 / 다음 모듈

| | 모듈 | 링크 |
|--|------|------|
| 이전 | M3 — Space Post & Reply 협업 기능 | [../03-Space-Thread/README.md](../03-Space-Thread/README.md) |
| 완료 | GOBI-CLI Topic 인덱스 | [../README.md](../README.md) |

> **방법론**: VibeLearn AI v2.0
> **작성자**: Changsoo (Claude Code 활용)
