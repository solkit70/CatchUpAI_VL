---
title: "Artifacts · Routines 사용 패턴 — 이럴 땐 이렇게"
created: 2026-09-27 16:40:00
author:
  - "Claude Code"
tags:
  - claude-artifacts-routines
  - m5
  - patterns
---

## 읽는 법

**실측으로 확인된 것만 패턴으로 적었다.** 각 카드의 근거 표기: `[실측 날짜]` = 이 Topic 에서 직접 해 보고 확인, `[문서]` = 공식 문서, `[추론]` = 아직 확인 전(패턴이 아니라 후보). 카드마다 실물이나 기록 링크가 있다.

## 1. 공유가 목적이면 정적 페이지부터

| | |
|---|---|
| **상황** | 로그인하지 않는 사람(팀 밖, 가족, 행사 참가자)에게 링크 하나로 보여 줘야 한다 |
| **하는 것** | db 없는 **정적 페이지**로 만들어 공유한다. 편집·데이터가 필요한 도구는 따로 두고, 공유용은 그 도구에서 뽑은 스냅샷으로 |
| **하지 않는 것** | db 를 쓰는 편집 도구를 그대로 공유 링크로 보내기 — 로그인 안 한 사람에겐 「Sign in」 또는 빈 껍데기다 |
| **실물** | 부스 매니저(db, 편집용) + 부스 현황판(정적, 공유용) 두 장으로 나눴다 → [M1 상태표](../../01-Inventory-and-Questions/guides/inventory.md) |
| **근거** | `[실측 9/13]` 시크릿 창 6건 — db·private 3건은 Sign in, 나머지 3건 열림 · `[실측 9/13]` M2 2×2 실험 → [sharing-matrix](../../02-Artifacts-Sharing-and-Versions/guides/sharing-matrix.md) · `[실측 9/27]` db·user·assets 선언은 공개 링크 불가 |

## 2. AI 세션이 Artifact 데이터를 고칠 땐 `if_version`

| | |
|---|---|
| **상황** | 사람들이 페이지에서 쓰고 있는 db 를 Claude 세션이 읽고 고친다 (현황 갱신, 일괄 수정) |
| **하는 것** | 읽을 때 받은 `version` 을 쓸 때 `if_version` 으로 붙인다. 거부되면 다시 읽고 다시 계획한다 |
| **하지 않는 것** | 버전 없이 덮어쓰기. 그리고 **페이지 쪽**에서 「읽고 +1 해서 쓰기」로 여러 사람이 올리는 숫자 만들기 — 페이지 쓰기는 마지막에 쓴 사람이 이긴다 |
| **실물** | [db 카운터](https://claude.ai/artifact/8p4xaEhHXB6PQyzDZfy3os) → [db-roundtrip](../../03-Artifacts-Capabilities-Lab/guides/db-roundtrip.md) |
| **근거** | `[실측 9/27]` 사람이 화면에서 v2 → v4 로 바꾼 뒤 세션의 v2 쓰기 `version_mismatch` 거부, v4 로 재시도 통과 · `[문서]` db.d.ts 「Do NOT build monotonic counters from read-modify-update」 |

## 3. 알림 루틴은 「조건부」와 「항상」을 목적으로 고른다

| | |
|---|---|
| **상황** | 루틴이 무언가를 확인하고 메일을 보낸다 |
| **하는 것** | **자주 돌고 대부분 「없음」이면 조건부**(알림 피로 방지) — 단 실패는 **다른 채널**(푸시·실패 메일)로 알리게 프롬프트에 쓴다. **드물게 돌거나 실행 자체를 확인해야 하면 항상 보낸다** |
| **하지 않는 것** | 조건부 알림만 걸고 실패 처리를 비워 두기 — 성공과 실패가 똑같이 「소식 없음」이 된다 |
| **실물** | [WBLP 주간 확인](https://claude.ai/code/routines/trig_01LKgvHWt4ZfJbTqJgn5KvVT) (조건부) · [내일 일정 미리보기](https://claude.ai/code/routines/trig_01TyCwrfL1H3vsmdkmcDS8xk) (항상) |
| **근거** | `[실측 9/21]` WBLP 3주 연속 실패가 「공고 없음」과 구분되지 않았다 → [wblp-routine-audit](../../04-Routines-Lab/guides/wblp-routine-audit.md) · `[실측 9/27]` 0건이어도 메일 → 실행이 메일함에서 바로 확인됨 → [second-routine](../../04-Routines-Lab/guides/second-routine.md) |

## 4. 볼트를 쓰면 로컬, 외부만 보면 클라우드

| | |
|---|---|
| **상황** | 「매일/매주 X 해 줘」를 받았다 |
| **하는 것** | 볼트 파일을 읽거나 쓰면 **로컬 AI4PKM cron**, PC 가 꺼져도 외부(웹 · 메일 · 캘린더)만 보면 **클라우드 루틴**. 둘 다면 나눈다 |
| **하지 않는 것** | 볼트 파일이 필요한 일을 클라우드 루틴으로 만들기 — 루틴은 선택한 GitHub 레포만 clone 한다 |
| **실물** | GDR · TIU (로컬) · WBLP · 일정 미리보기 (클라우드) → [판단표](../../04-Routines-Lab/concepts/local-vs-cloud.md) |
| **근거** | `[문서]` 「Each repository is cloned at the start of a run」 · `[실측 9/27]` 레포 없는 루틴 로그 「No sources configured」 |

## 5. 클라우드 루틴이 외부에 못 닿으면 환경의 네트워크부터

| | |
|---|---|
| **상황** | 내 PC 에서는 되던 확인이 루틴에서는 실패한다 |
| **하는 것** | ① `list_runs` · `get_run_log` 로 로그를 연다 ② 같은 요청을 내 PC 에서 재현한다 ③ 환경의 **Network access** 를 본다 (`Default` = Trusted = 허용 목록만). 커넥터(Gmail · 캘린더)는 허용 목록과 무관하다 |
| **하지 않는 것** | 로그를 안 열고 프롬프트부터 고치기 · 실행 목록의 초록색을 성공으로 믿기 |
| **실물** | WBLP 복구 → [routine-did-not-run](../../04-Routines-Lab/troubleshooting/routine-did-not-run.md) |
| **근거** | `[실측 9/21]` `connect_rejected (organization policy)` · 로컬 `curl` HTTP 200 · 허용 목록 추가 후 113초 만에 성공 · `[문서]` 「A green status … does not mean the task in your prompt succeeded」 · `[실측 9/27]` 커넥터만 쓴 루틴은 Trusted 그대로 성공 |

## 6. 남과 공유한 링크는 「최신 버전 공유」로 두고 시크릿 창으로 확인

| | |
|---|---|
| **상황** | 공유 중인 페이지를 고쳤다 |
| **하는 것** | Share 메뉴에서 공유 버전을 **Latest(최신)** 로 둔다. 확인은 **시크릿 창**으로 — 작성자 브라우저는 항상 최신을 보여 주므로 증거가 아니다 |
| **하지 않는 것** | 고친 뒤 내 화면만 보고 「반영됐다」고 알리기 |
| **실물** | [Builders Lounge 입장 안내](https://claude.ai/artifact/Vs9GEkCtEXsyRdT5kvyF7s) — 9/25 Version 4 발행 뒤 사용자가 공유 버전을 Latest 로 바꿈 |
| **근거** | `[실측 9/7]` 다른 사람에게는 옛 버전이 보였다 → [shared-link-shows-old-version](../../02-Artifacts-Sharing-and-Versions/troubleshooting/shared-link-shows-old-version.md) · `[실측 9/25]` Share 메뉴에서 Latest 선택 (M2 에서 「토글이 안 보인다」로 남았던 질문의 답) |

## 후보 — 아직 패턴이 아닌 것

| 후보 | 왜 아직 |
|---|---|
| 회의 중에 그 자리에서 만들어 그 회의에서 쓴다 | 부스 매니저가 9/3 회의 중 만들어졌다는 기록은 있지만 [M1 상태표], 「그래서 더 잘 쓰였다」를 비교한 실측이 없다 `[추론]` |
| 지시에 목적·제약만 넣고 도구 이름은 AI 가 고르게 둔다 | 9/1 사례 한 건. 반례를 찾아보지 않았다 `[추론]` |


English companion: [patterns_en](patterns_en.md)
