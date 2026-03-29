# M3 — Space & Thread 협업 기능

> **모듈 번호**: M3
> **상태**: ✅ 완료
> **예상 학습 시간**: 3-4시간
> **실제 소요 시간**: ~1.5시간 (2026-03-29)

---

## 이 모듈에서 배우는 것

Space 탐색, Thread 생성/수정/삭제, Reply CRUD 전체 흐름을 실습합니다.
M2의 Session 명령어(API 이슈)와 달리 Space/Thread 명령어는 모두 정상 작동합니다.

---

## 학습 순서 (이 순서대로 읽으세요)

| 순서 | 문서 | 설명 |
|------|------|------|
| 1 | [guides/space-navigation.md](guides/space-navigation.md) | space list / warp / list-threads / get-thread |
| 2 | [guides/thread-management.md](guides/thread-management.md) | Thread & Reply CRUD 전체 흐름 + 실습 결과 |

---

## M3 핵심 요약

```
space list          → 3개 Space 확인 (changbal, gobi, cmds)
space warp          → 활성 Space 선택 (인터랙티브)
space list-threads  → Thread 목록 (JSON에 topics, richText 포함)
space get-thread    → Thread 내용 + Replies 조회
create-thread       → Thread 생성 (ID: 731 생성 확인)
create-reply        → Reply 추가 (ID: 732)
edit-thread         → Thread 수정 (editedAt 필드 추가됨)
edit-reply          → Reply 수정 ✅
delete-reply        → Reply 삭제 ✅
```

**M2 Session과의 차이**:
- Space/Thread 명령어는 **모두 정상 작동** ✅
- M2 session list/get/reply는 HTTP 404 이슈 존재

---

## M3 DoD 체크리스트

- [x] `gobi space list` — 3개 Space 확인
- [x] `gobi space warp` — `--space-slug` 옵션으로 우회 실습
- [x] `gobi space list-threads` — changbal, gobi Space Thread 목록 확인
- [x] `gobi space get-thread` — 기존 Thread 내용 + Reply 조회
- [x] `gobi space create-thread` — 새 Thread 생성 (ID: 731)
- [x] `gobi space create-reply` — Reply 추가 (ID: 732)
- [x] `gobi space edit-thread` — Thread 내용 수정
- [x] `gobi space edit-reply` — Reply 수정
- [x] `gobi space delete-reply` — Reply 삭제
- [x] `space-navigation.md` 작성 완료
- [x] `thread-management.md` 작성 완료

---

## 이전 / 다음 모듈

| | 모듈 | 링크 |
|--|------|------|
| ◀ 이전 | M2 — Brain & Session | [../02-Brain-Session/README.md](../02-Brain-Session/README.md) |
| 다음 ▶ | M4 — 실전 워크플로우 + 교과서 완성 | `../04-Capstone/README.md` |

---

> **방법론**: VibeLearn AI v2.0
> **작성자**: Changsoo (Claude Code 활용)
