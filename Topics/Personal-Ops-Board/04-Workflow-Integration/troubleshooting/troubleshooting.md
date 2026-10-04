---
title: "M4 — 라운드업 연동 문제 해결"
created: 2026-10-02 20:00:00 -07:00
tags:
  - personal-ops-board
  - workflow-integration
---

## 라운드업 연동 문제 해결

| 증상 | 우선 확인 | 조치 |
|---|---|---|
| task 변경이 Roundup에 보이지만 item은 그대로다 | 현재 handoff 상태, 사용된 GDR/GWR 지침, 해당 item 경로 | 변경이 승인된 것인지 확인한다. POST-HANDOFF라면 확인된 필드만 item에 반영하고, 추측이 필요하면 사용자에게 묻는다. |
| index에 새 변경이 없다 | item frontmatter 파싱 결과와 index 실행 로그 | 원본을 자동 교정하지 않는다. 구문 오류를 수정 승인받고 index를 재실행한다. |
| Board가 오래된 상태다 | index 생성 시각·오류, renderer 실행 결과 | index 오류가 없을 때 renderer를 실행한다. 실패하면 이전 정상 Board를 보존하고 운영 실패로 기록한다. |
| task가 Board에서 사라졌다 | item status, exclusion/warning 분류, archive 링크 | `items/` 원본과 index를 비교한다. 원본 자체가 바뀌었다면 snapshot 및 ledger의 rollback 절차를 따른다. |
| 실행 결과 task 변경이 없다 | Roundup의 task-change 결과 | 정상 no-op으로 기록한다. 이것만으로 POST 변경 쓰기 경로가 검증됐다고 표시하지 않는다. |
| 미분류 warning이 나타났다 | warning 종류와 파일 경로 | 자동으로 허용하거나 필드를 추정하지 않는다. 원인을 분류하고 사용자 판단이 필요한 경우 중단한다. |

상태 확인과 복구 순서는 [프롬프트 변경 절차](../guides/prompt-change-procedure.md) 및 [M3 migration checklist](../../03-Migration/guides/migration-checklist.md)를 따른다. 비공개 task 본문을 공개 로그나 테스트 fixture에 복사하지 않는다.
