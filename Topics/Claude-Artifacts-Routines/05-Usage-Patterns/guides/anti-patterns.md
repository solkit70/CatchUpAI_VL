---
title: "Artifacts · Routines 안티패턴 — 실제로 겪은 것만"
created: 2026-09-27 16:45:00
author:
  - "Claude Code"
tags:
  - claude-artifacts-routines
  - m5
  - anti-patterns
---

## 규칙

**겪은 것만 적는다.** 항목마다 날짜와 출처를 붙인다. 새 사고가 나면 이 표 맨 아래에 한 줄 더하고, 대응하는 [패턴 카드](patterns.md)가 있으면 번호를 적는다.

## 목록

| # | 날짜 | 한 일 (하지 말 것) | 무엇이 일어났나 | 대신 | 패턴 | 출처 |
|---|---|---|---|---|---|---|
| 1 | 9/7 | 페이지를 고친 뒤 **내 화면만 보고** 공유 | 다른 사람에게는 옛 버전이 보였다 (공유 버전 고정) | 공유 버전 Latest + 시크릿 창 확인 | 6 | [M2 troubleshooting](../../02-Artifacts-Sharing-and-Versions/troubleshooting/shared-link-shows-old-version.md) |
| 2 | 9/13 | **db 를 쓰는 페이지**를 로그인 안 하는 사람에게 링크로 | 「Sign in to view this page」 — 공개해도 데이터는 로그인 사용자만 | 공유용 정적 스냅샷을 따로 | 1 | [M1 상태표](../../01-Inventory-and-Questions/guides/inventory.md) · [M2 sharing-matrix](../../02-Artifacts-Sharing-and-Versions/guides/sharing-matrix.md) |
| 3 | 9/13 | 만든 아티팩트 URL 을 **볼트에 안 적음** | 실물 7건 중 3건이 볼트 어디에도 없었다 (그중 둘은 바로 이 기능 설명 페이지) | 만들면 그날 Task Board · Roundup 에 URL | — | [M1 상태표](../../01-Inventory-and-Questions/guides/inventory.md) |
| 4 | 9/12 | 정적 스냅샷 내용을 고치면서 **「마지막 동기화」 문구는 그대로** | 9/12 편집분인데 배너는 「09-10 15:20」 | 스냅샷을 고칠 때 날짜 표시도 같이 | 1 | [M1 상태표 A2](../../01-Inventory-and-Questions/guides/inventory.md) |
| 5 | 9/7~9/21 | 조건부 알림 루틴에 **실패 알림을 약하게** 둠 (푸시 한 줄) | 3주 연속 실패가 「공고 없음」과 똑같이 보였다. 루틴은 9/14 로그에 이미 원인을 적어 두었다 | 실패는 메일 등 다른 채널로 · 로그를 월 1회 사람이 | 3 | [wblp-routine-audit](../../04-Routines-Lab/guides/wblp-routine-audit.md) |
| 6 | 9/21 | 외부 API 파라미터를 **확인 없이** 프롬프트에 (`loc_query=`, `country[]=`) | amazon.jobs 가 두 파라미터를 조용히 무시 — 두 쿼리가 같은 결과 | 파라미터마다 로컬에서 적용 여부 확인 (`filterFacets`) | 5 | [wblp-routine-audit](../../04-Routines-Lab/guides/wblp-routine-audit.md) |
| 7 | 9/21 | 환경 설정 위치를 **추정으로** 안내 | 사용자가 두 번 헛걸음 (캡처 3회, 12분) | 모르면 문서 확인 또는 캡처부터 요청 | 5 | [M4a WorkLog](../../vl_worklog/20260921_M4a_Claude-Artifacts-Routines.md) |
| 8 | 9/27 | 운영 중 아티팩트를 감시하는 세션에서 **실습용 발행을 연달아** | 세션 감시 한도 10개 → 부스 매니저·현황판 감시와 댓글 자동 답이 밀려남 | 실습용 발행은 다른 세션에서 | — | [M3 troubleshooting](../../03-Artifacts-Capabilities-Lab/troubleshooting/cdn-and-storage-gotchas.md) |
| 9 | 9/3 (9/27 점검) | 배치도 이미지를 **HTML 안에 base64 로** | 페이지 246KB · 한 줄이 약 10만 자 — 편집·검토가 무거워짐 | 이미지는 assets 로 올려 `/_blob/<id>` 참조 | — | [부스 매니저 점검](../../03-Artifacts-Capabilities-Lab/guides/bighug-artifacts-review.md) |
| 10 | 9/13 (9/27 정정) | 문서 한 문장만 읽고 기능을 **「이 계정에서 불가」로 닫음** (댓글) | 9/27 실측에서 댓글 · Send to Claude 가 작동했다 — 2주 동안 틀린 결론이 기록에 남아 있었다 | 「불가」도 최소 예제 하나로 실측한 뒤 닫는다 | — | [M2 sharing-matrix 정정](../../02-Artifacts-Sharing-and-Versions/guides/sharing-matrix.md) · [M3 lab-log](../../03-Artifacts-Capabilities-Lab/guides/lab-log.md) |

## 겪을 뻔한 것 (문서로만 확인)

| 한 일 | 위험 | 근거 |
|---|---|---|
| 페이지에서 「읽고 +1 해서 쓰기」 카운터를 여러 사람이 동시에 | 한 번이 사라질 수 있다 (마지막에 쓴 사람이 이김) | `[문서]` db.d.ts · 동시 클릭 실측은 안 함 |
| 루틴에 커넥터를 기본값 그대로 전부 포함 | 포함된 커넥터는 쓰기까지 묻지 않고 한다 | `[문서]` Routines — 두 번째 루틴은 Calendar · Gmail 만 남겼다 |
