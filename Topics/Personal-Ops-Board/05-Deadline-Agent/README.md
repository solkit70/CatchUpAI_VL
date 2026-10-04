---
title: "M5 — Deadline Agent"
created: 2026-10-03 05:00:00 -07:00
tags:
  - personal-ops-board
  - vibelearn-ai
---

## M5 — Deadline Agent

**상태**: 구현·합성 회귀·수동 생성 및 10/3 cron 시각 실행 2회 완료. 다음 날 자동 갱신은 10/4 운영 확인 대기. **예상 학습 시간**: 3시간. Deadline 생성기는 인덱스 캐시를 읽어 비공개 `AI/Tasks/views/warnings.md`만 원자적으로 교체한다. 실제 task 원본과 priority board는 수정하지 않는다.

## 학습 순서와 실행

1. [경고 단계와 요구](concepts/warning-levels.md): EARS 요구, 경고 임계값, 대기 task 처리
2. [합성 경계 사례](examples/README.md): 오늘·기한 초과·D-3·D-7·D-8 및 제외 조건
3. [수동 실행 및 회귀 검사](guides/run-deadline.md): 합성 날짜 고정 실행과 결과 확인
4. [모듈 링크 점검기](scripts/check_links.py): M5 학습 문서의 상대 Markdown 링크 확인
5. [설계 결정 ADR 012](../architecture/decisions/012-M5-결정적-마감-경고.md#결정): 결정적 코드와 AI4PKM cron 선택 이유
6. [M5 WorkLog](../vl_worklog/20261003_M5_Personal-Ops-Board.md#검증): 요구별 검증 증거와 미확인 운영 조건

## 현재 동작

`todo`, `doing`, `waiting` task에서 날짜가 지난 건, 오늘 마감, 항목별 `warn_days` 기간에 든 건을 각각 보여 준다. `warn_days` 생략 기본값은 3일이며 `waiting.due`는 독촉일이다. `done`, `paused`, 마감일 없는 task는 알리지 않는다. 경고가 없으면 빈 상태를 표시한다. 인덱스의 파싱 오류나 잘못된 마감일이 있으면 실행을 실패 처리하고 기존 경고 파일을 보존한다.

cron은 원래 매일 오전 5시 실행이다. 절전으로 10/3 05:00을 놓쳐 05:05와 05:15로 옮겨 시험했고, 두 예약 실행과 `warnings.md` 갱신을 확인했다. 10/4 방송 시험을 위해 현재 cron은 05:15로 임시 설정되어 있으며, 시험 후 05:00으로 복구해야 한다. `ai4pkm -o`는 cron scheduler와 다른 활성 file watcher도 함께 시작한다. 내일은 PC가 깨어 있는 상태에서 05:15 전에 실행기를 시작하고 예약 실행을 확인한다.

[이전 M4](../04-Workflow-Integration/README.md) · [Topic 안내](../README.md) · 다음 M6: [로드맵](../vl_roadmap/20260927_RoadMap_Personal-Ops-Board.md#-전체-로드맵-구조)
