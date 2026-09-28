# M3 — Artifacts 런타임 기능 실험

**모듈**: M3 · **상태**: ✅ 완료 (2026-09-27) · **실소요**: 약 1시간 (VS Code Claude Code 확장 세션)

Claude Artifact 페이지가 선언할 수 있는 런타임 기능(db · user · assets · comments · 다중 파일)을 가장 작은 예제로 하나씩 발행하고, AI 세션과 사람이 같은 db 문서를 번갈아 고칠 때 무엇이 막아 주는지 실측했다. 기준은 runtime contract **0.2.60**.

## 📚 학습 순서

1. [concepts/capability-selection-table.md](concepts/capability-selection-table.md) — 어떤 일에 어떤 기능을 쓰나 (먼저 읽기)
2. [examples/01-counter-db.html](examples/01-counter-db.html) — ① db 카운터
3. [examples/02-hello-user.html](examples/02-hello-user.html) — ② 지금 보는 사람 (user)
4. [examples/03-image-assets.html](examples/03-image-assets.html) — ③ 이미지 보관함 (assets)
5. [examples/04-comments.html](examples/04-comments.html) — ④ 문단마다 댓글 (comments, composer_only)
6. [examples/05-multi-file/index.html](examples/05-multi-file/index.html) — ⑤ HTML · CSS · JSON 나눠 발행
7. [guides/lab-log.md](guides/lab-log.md) — 5종 발행 URL · 화면 확인 결과
8. [guides/db-roundtrip.md](guides/db-roundtrip.md) — 세션 ↔ 화면 db 왕복 · `if_version` 거부 실측 (핵심)
9. [guides/bighug-artifacts-review.md](guides/bighug-artifacts-review.md) — 실물 점검: 부스 매니저 (수정 없음)
10. [troubleshooting/cdn-and-storage-gotchas.md](troubleshooting/cdn-and-storage-gotchas.md) — 세션 감시 10개 한도 · 걸리기 쉬운 것

## 이 모듈에서 알아낸 것

- **사람이 화면에서 고치는 동안 AI 세션이 같은 데이터를 고치려 하면 `if_version` 이 막는다.** 화면이 v2 → v4 로 바꾼 뒤 세션의 v2 쓰기는 `version_mismatch` 로 거부됐고, 다시 읽은 v4 로는 통과했다
- 페이지 쪽 쓰기는 마지막에 쓴 사람이 이긴다 — 여러 사람이 올리는 숫자를 문서 하나에 +1 하면 안 된다
- 「Send to Claude」 댓글은 세션이 자동으로 답한다. 댓글이 붙는 자리는 연 방법(페이지 버튼 / 댓글 모드)에 따라 다르다
- 한 세션은 아티팩트를 10개까지 감시한다 — 예제를 여러 개 발행하면 운영 중인 아티팩트의 댓글 자동 답이 밀려난다

## 이전 / 다음

← [M2 — 공유·버전](../02-Artifacts-Sharing-and-Versions/README.md) · → [M4 — Routines](../04-Routines-Lab/README.md)
