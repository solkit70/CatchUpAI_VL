---
title: "M2 — 가설 검증"
created: 2026-09-10 13:00:00
status: 완료
tags:
  - vibelearn-ai
  - m2
---

# M2 — 가설 검증

**상태**: ✅ **완료** (2026-09-10) — 가설 4는 발표 후로 이월
**예상 3h / 실제 약 3h**

## 📚 학습 순서

1. [design/hypothesis-design.md](design/hypothesis-design.md) — 🔴 **먼저 읽는다.** 판정 기준을 데이터보다 먼저 정한 이유와 그 기준
2. [analysis/verdicts.md](analysis/verdicts.md) — **판정 4건.** 발표에 그대로 올릴 문장이 각 절 끝에 있다
3. [scripts/classify_and_test.py](scripts/classify_and_test.py) — 그룹을 나눠 비교하는 스크립트
4. [scripts/shorts_over_time.py](scripts/shorts_over_time.py) — Shorts 업로드를 멈춘 뒤의 조회 추이

## 판정 결과

| # | 가설 | 판정 | 수치 |
|---|---|---|---|
| **0** | Shorts 는 구독으로 이어지지 않는다 | ✅ **맞다** | **52.2배** |
| 1 | 자막이 구독 전환을 높인다 | ⏳ **알 수 없다** | 공개 자막 영상 6편 |
| 2 | 사람이 나오는 영상이 낫다 | ~~🔶 약한 차이~~ → 🔴 **M3 에서 ➖ 차이 없다로 뒤집힘** | ~~1.71~~ → **0.86배** |
| 3 | 분할 편집이 효과가 있다 | ➖ **차이 없다** / ⭐ 사례는 강함 | 1.21배 |
| 4 | 조회-구독 시차 | ⏳ **발표 후** | — |

## 이 모듈에서 바로잡은 것 3가지

**① 표본이 500편에서 잘려 있었다.**
Studio CSV 내보내기는 상위 500편까지다(`Showing top 500 results`).
API 로 전체를 받아 다시 계산했다 — **중복 제거 후 505편**. 결론은 안 바뀌었지만
**「전체 기준」이라 말할 수 있게 됐다.**

**② 「자막」을 유튜브 자막 트랙으로 오해했다.**
`captions.list` API 로 확인하려다 사용자 지적으로 멈췄다 —
**영상에 구워 넣은 자막**이라 API 로는 안 보인다. 볼트 작업 기록으로만 셀 수 있다.

**③ 구독 해지로 유입 경로를 추적하려 했다.**
해지는 **누른 페이지**에 기록된다. Shorts 로 들어온 사람이 롱폼에서 해지하면
그 기록은 롱폼에 남는다. **「Shorts 해지 1건」은 아무것도 증명하지 못한다.**

> 📌 셋 다 **사용자 지적으로 바로잡혔다.** 이 Topic 의 주제(「사람의 개입이 퀄리티를 결정한다」)가
> 조사 과정 자체에서 그대로 재현됐다 — **M4·M5 에서 쓸 재료다.**

## ✅ Definition of Done

- [x] 🟥 **가설 3개(자막·사람 등장·분할 편집)에 판정**
- [x] 🟥 **판정마다 표본 수와 한계 명시**
- [x] 판정 기준을 데이터 보기 **전에** 정한 기록 (`design/hypothesis-design.md`)
- [x] 가설 4는 「발표 후」로 명시
- [x] 가설 0(Shorts) 추가 판정 — M1 에서 새로 나온 것
- [ ] `findings/memory-vs-data.md` — **M1 의 P5 분석 문서에 이미 있어 생략**
- [x] WorkLog + Daily Retrospective

## 🔗 이동

- **이전**: [01-Data-Pipeline/](../01-Data-Pipeline/README.md)
- **다음**: [03-Revival-Inventory/](../03-Revival-Inventory/README.md) — 되살리기 작업 인벤토리
  - 🔴 **M3 에서 가설 2를 재판정한다** — 「사람 등장」을 눈으로 분류한 뒤
- **로드맵**: [20260910_RoadMap_YouTube-Channel-Revival-With-AI.md](../vl_roadmap/20260910_RoadMap_YouTube-Channel-Revival-With-AI.md)
