# M4 — 실전 워크플로우 + 교과서 완성 (Capstone)

> **모듈 번호**: M4
> **상태**: ✅ 완료
> **예상 학습 시간**: 2-3시간
> **실제 소요 시간**: ~1시간 (2026-03-29)

---

## 이 모듈에서 배우는 것

M1~M3에서 배운 모든 명령어를 연결하는 End-to-End 워크플로우를 실습합니다.
`인증 확인 → Brain 검색 → Brain 질의 → Thread 게시 → Update 전파`의 5단계 시나리오를 완성합니다.
전체 명령어 Quick Reference도 작성하여 참조 가이드로 활용합니다.

---

## 학습 순서 (이 순서대로 읽으세요)

| 순서 | 문서 | 설명 |
|------|------|------|
| 1 | [guides/complete-workflow.md](guides/complete-workflow.md) | End-to-End 5단계 시나리오 + 자동화 스크립트 + 트러블슈팅 |
| 2 | [guides/quick-reference.md](guides/quick-reference.md) | 전체 명령어 한 페이지 참조 (auth/brain/session/space) |

---

## M4 핵심 요약

```
Step 1: gobi auth status           → 인증 확인 ✅
Step 2: gobi brain search          → 우리 Brain 1위 확인 (similarity 0.911) ✅
Step 3: gobi brain ask             → Session 679 생성 ✅
Step 4: gobi space create-thread   → Thread 735 생성 (changbal) ✅
Step 5: gobi brain post-update     → 완료 소식 전파 ✅
```

**M1~M4 전 모듈 완료** ✅

---

## M4 DoD 체크리스트

- [x] `gobi auth status` — 인증 확인
- [x] `gobi brain search` — gobi-cli-study Brain similarity 0.911 1위 확인
- [x] `gobi brain ask` — Session 679 생성 및 답변 확인
- [x] `gobi space create-thread` — Thread 735 생성 (changbal)
- [x] `gobi brain post-update` — 학습 완료 Update 게시
- [x] `complete-workflow.md` 작성 완료
- [x] `quick-reference.md` 작성 완료
- [x] `Topics/GOBI-CLI/README.md` 작성 완료 (Topic 전체 인덱스)
- [x] M4 WorkLog 작성 완료
- [x] Topic Retrospective 작성 완료

---

## 이전 / 다음 모듈

| | 모듈 | 링크 |
|--|------|------|
| ◀ 이전 | M3 — Space & Thread 협업 기능 | [../03-Space-Thread/README.md](../03-Space-Thread/README.md) |
| ✅ 완료 | GOBI-CLI Topic 완료 | [../README.md](../README.md) |

---

> **방법론**: VibeLearn AI v2.0
> **작성자**: Changsoo (Claude Code 활용)
