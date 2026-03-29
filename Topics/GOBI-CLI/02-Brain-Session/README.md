# M2 — Brain & Session 명령어 마스터

> **모듈 번호**: M2
> **상태**: ✅ 완료
> **예상 학습 시간**: 4-5시간
> **실제 소요 시간**: ~2시간 (2026-03-29)

---

## 이 모듈에서 배우는 것

Brain 검색/질문, BRAIN.md 작성 및 발행, Brain Updates CRUD, Session 관리 명령어를 실습합니다.
이 모듈을 마치면 GOBI CLI의 핵심 지식 관리 기능을 사용할 수 있습니다.

---

## 학습 순서 (이 순서대로 읽으세요)

| 순서 | 문서 | 설명 |
|------|------|------|
| 1 | [guides/brain-search-guide.md](guides/brain-search-guide.md) | brain search + brain ask 사용법 및 실습 결과 |
| 2 | [guides/brain-publish-guide.md](guides/brain-publish-guide.md) | BRAIN.md 작성 → publish + brain updates CRUD |
| 3 | [guides/session-management.md](guides/session-management.md) | session 명령어 + v0.6.15 이슈 상세 |
| 4 | [examples/sample-brain.md](examples/sample-brain.md) | 재사용 가능한 BRAIN.md 템플릿 |

---

## M2 핵심 요약

```
brain search  →  공개 Brain 의미 기반 검색 (similarity 점수)
brain ask     →  Brain AI에 질문 → Session 생성
brain publish →  BRAIN.md → vault 발행
brain updates →  post / list / edit / delete CRUD 전체 완료
session       →  ⚠️ list/get/reply 모두 HTTP 404 (v0.6.15 이슈)
```

**중요 발견**:
- `gobi brain search` : 한국어 쿼리가 한국어 Brain에서 훨씬 높은 유사도
- `gobi brain ask` → `--content` (not `--message`) 옵션 사용
- `gobi brain ask` 에서 Session ID는 숫자(`id`)와 UUID(`sessionId`) 두 종류 반환
- `publish` vs `post-update` 는 목적이 다름 (지식 베이스 갱신 vs 진행 상황 공유)

---

## M2 DoD 체크리스트

- [x] `gobi brain search` 다양한 쿼리로 실험 완료
- [x] `gobi brain ask` 로 Session 생성 성공
- [x] `gobi session list/get/reply` 실습 시도 (⚠️ v0.6.15 API 이슈 확인 및 문서화)
- [x] `BRAIN.md` 작성 후 `gobi brain publish` 발행 성공
- [x] `gobi brain post-update / list-updates / edit-update / delete-update` CRUD 완료
- [x] `brain-search-guide.md` 작성 완료 (실제 출력 결과 포함)
- [x] `session-management.md` 작성 완료 (이슈 상세 포함)
- [x] `brain-publish-guide.md` + `sample-brain.md` 작성 완료
- [x] `02-Brain-Session/README.md` 작성 완료

---

## 이전 / 다음 모듈

| | 모듈 | 링크 |
|--|------|------|
| ◀ 이전 | M1 — 설치 & 인증 & 핵심 개념 | [../01-Setup-Auth/README.md](../01-Setup-Auth/README.md) |
| 다음 ▶ | M3 — Space & Thread 협업 기능 | `../03-Space-Thread/README.md` |

---

> **방법론**: VibeLearn AI v2.0
> **작성자**: Changsoo (Claude Code 활용)
