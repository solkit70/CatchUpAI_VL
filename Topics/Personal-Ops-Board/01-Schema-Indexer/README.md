---
title: "M1 — 스키마 + 인덱서"
created: 2026-10-02 10:43:41
tags:
  - personal-ops-board
  - vibelearn-ai
---

## M1 — 스키마 + 인덱서

**상태**: 구현·검증·학습 문서 정리 완료. **예상 학습 시간**: 3시간. 인덱서는 읽기 전용이며, 실제 할 일과 앱 코드는 비공개 볼트에 둔다. 이 폴더에는 공개용 계약·합성 입력·실행 안내만 있다.

## 읽고 실행하는 순서

1. [파서 계약과 결정 반영표](concepts/parser-contract.md): 입력 보존·검증 규칙·결정 1~10의 범위
2. [합성 fixture 기대 결과](examples/README.md): 원본 밖에서 실행할 사례
3. [인덱서 실행 안내](guides/run-indexer.md): PowerShell 실행과 결과 판정
4. [성능 결정 ADR 009](../architecture/decisions/009-링크는%20직접%20확인하고%20색인은%20지연%20생성.md#결정): 직접 확인과 지연 색인의 이유
5. [검증 기록](../vl_worklog/20261002_M1_Personal-Ops-Board.md#검증): 회귀·실제 입력·원본 무변경

## 현재 결과와 한계

10/2 A1 검증은 현재 입력 69개·valid 68·error 1·warning 16이었다. 파싱 오류를 포함한 모든 입력이 결과에 남았고 원본은 변하지 않았다. 오류의 원본 수정, 취소 사유를 보드에 표시하는 정책, 에이전트 구현은 별도 작업이다.

[이전 M0](../00-Start-Record/README.md) · [Topic 안내](../README.md) · 다음 M2: [로드맵](../vl_roadmap/20260927_RoadMap_Personal-Ops-Board.md#-전체-로드맵-구조)
