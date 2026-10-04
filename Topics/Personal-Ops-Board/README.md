---
title: "Personal Ops Board"
created: 2026-10-02 10:43:41
tags:
  - personal-ops-board
  - vibelearn-ai
---

## Personal Ops Board

마크다운을 원본으로 두고 AI 에이전트가 보드와 제안을 만드는 개인 일정 관리 앱을 개발한다. VibeLearn AI에 Kiro식 스펙·설계 갱신을 접목하는 실험이며, 기능 구현과 아키텍처 기록을 함께 진행한다. 실제 코드·할 일·생성 캐시는 비공개 볼트 `AI/Tasks/`에만 둔다.

## 학습 순서와 현재 상태

| 순서 | 모듈 | 상태 | 읽을 문서 |
|---|---|---|---|
| 1 | M0 시작의 기록 | 문서·링크 정리와 사용자 검토 완료 | [M0 안내](00-Start-Record/README.md) |
| 2 | M1 스키마·인덱서 | 구현·검증·문서 정리 완료 | [M1 안내](01-Schema-Indexer/README.md) |
| 3 | M2 Board 에이전트 | 구현·합성 검증·실제 입력 렌더링·CLI 1회 trigger 검증 완료, 자동 감시는 비활성 | [M2 안내](02-Board-Agent/README.md) |
| 4 | M3 Migration | handoff 적용, 전체 이관 진행 중 | [M3 안내](03-Migration/README.md) |
| 5 | M4 Workflow Integration | 완료 — 실제 POST 변경·다음 날 지속성 검증 (10/3) | [M4 안내](04-Workflow-Integration/README.md) |
| 6 | M5 Deadline Agent | 구현·합성 회귀 및 10/3 cron 시각 실행 2회 완료; 10/4 다음 날 갱신 확인 대기 | [M5 안내](05-Deadline-Agent/README.md) |
| 7 | M6 Board UI | 구현·합성 검증·로컬 read-only 화면 확인; 빠른 입력은 분류·프로젝트·출처 링크 입력 후 items 저장 | [M6 안내](06-Board-UI/README.md) · [전체 로드맵](vl_roadmap/20260927_RoadMap_Personal-Ops-Board.md#-전체-로드맵-구조) |

현재 기능은 읽기 전용 인덱서와 결정적 Board·Deadline renderer다. POST-HANDOFF에서 `items/`가 task 원본이고 Board renderer는 비공개 `priority-board.md`, Deadline renderer는 `warnings.md`를 생성한다. 기존 Task Board는 원본 snapshot 및 완료 기록 링크를 제공하는 읽기 전용 진입점이다. handoff는 적용됐지만 48개 보류와 41개 미승인 제안이 남아 전체 M3 task migration은 진행 중이다. M5는 마감·독촉일 경고 규칙과 합성 회귀를 구현했으며 10/3 예약 시각 실행 2회가 확인됐다. 10/4 다음 날 갱신 확인을 위해 cron을 05:15로 임시 조정했고, 확인 후 원래 05:00으로 되돌린다. 한 주 실전 운영과 방법론 최종 평가는 M9·M10에서 확인한다.
M6에서는 단일 HTML과 loopback Python server 기반 UI를 만들고, Markdown 본문 보존·stale edit 거부·개별 proposal 승인·합성 회귀 56건·HTTP 종단 간 fixture 검증·read-only 실제 화면 조회까지 확인했다. 빠른 입력은 사용자의 결정에 따라 분류 및 project/source 링크를 함께 입력해 `items/`에 바로 저장한다. 라이브에서 안전하게 따라 할 disposable fixture와 POB-01~08 시나리오를 준비했으며, fixture 브라우저 시나리오를 실행해 발견한 빠른 입력 화면 오류도 수정했다. 사용자의 매뉴얼 실행과 Retrospective는 남아 있다.

## 결과와 설계 기록

- [현재 아키텍처](architecture/ARCHITECTURE.md#21-m1-인덱서): 원본·캐시·에이전트 권한과 구현 상태
- [M1 작업 기록](vl_worklog/20261002_M1_Personal-Ops-Board.md#검증): 당시 입력 성능·파싱 보존·회귀 검사 기록. 현재 index 상태는 아키텍처 문서에서 확인
- [방법론 실험 노트](vl_materials/VibeLearn%20AI%20새%20버전%20실험%20노트.md#접목-원장--kiro-요소별로): 접목 방식과 평가할 항목

M1은 10/2 A1 검증에서 전체 실행 0.221초로 5초 목표를 통과했다. 당시 실제 입력에 있던 YAML 오류는 숨기지 않고 보존했으며, 원본을 자동 수정하지 않았다. 이후 스키마 반영과 item 수정이 진행되어 현재 index 결과는 71개 유효·오류 0·수용된 정보성 warning 11건이다. 성능 측정은 당시 PC와 입력에 대한 결과다.
