---
title: "M1 — 실물이 4건이 아니라 7건이었다 · 질문 9개"
created: 2026-09-13 06:20:00
author:
  - "Claude Code"
topic: "Claude-Artifacts-Routines"
module: "M1"
tags:
  - vibelearn-ai
  - worklog
  - claude-artifacts-routines
---

## 세션 개요

| 항목 | 값 |
|---|---|
| 날짜 | 2026-09-13 (일) — **Live #27 2부 ② 방송 중** |
| 시작 · 종료 | 05:50 (Topic 개설 시작) · M1 착수 06:20 · **07:10 마감** |
| **실소요** | **Topic 개설 30분 + M1 50분 = 80분.** 그중 사용자 대기 약 10분(기간 확정 · 로드맵 승인 · 시크릿 창 확인). 로드맵 예상 2h 대비 M1 은 50분 |
| 직전 WorkLog 「개선할 점」 체크 | 첫 세션 — 대신 **Live-CoMC-App Retrospective 개선 제안 4건**을 이 Topic 의 규칙으로 적용: 실소요 기록(이 표) · 회고 체크(이 행) · 실물 DoD(examples/artifact-list.json) · 근거 표기(`[실측]/[문서]/[추론]` — inventory.md) |
| 모듈 | **M1 — 실물 재검토와 질문 목록** |
| 결과 | 실습 1·2·3 완료. 시크릿 창 6건 실측(사용자) — **db 있음·private 는 Sign in, 나머지 열림, 예측 6/6 일치.** M1 ✅ |

## 오늘의 학습 목표

- [x] 실물 상태표 — 아티팩트 `list` 실행, 6건 확인, 표 작성
- [x] 시크릿 창 결과 칸 — 사용자가 방송 중 Chrome 시크릿 창 6탭으로 확인 (07:05). 예측 6/6 일치
- [x] 질문 목록 9개 · 담당 · 근거 종류 · 우선순위
- [x] 영상 서사 3문장 (선택)

## 진행 내용

### 실습 1 — 실물 상태표

`Artifact` 도구 `action: list` → **6건** `[실측 06:22]`. 사례 인덱스(방송 전 작성)는 3건으로 셌다. 빠진 3건:

| 실물 | 날짜 | 무엇 |
|---|---|---|
| 내가 없을 때 도는 것 🔁 | 9/2 | **Routines 설명 페이지** — WBLP 사례·한계표. private |
| 터미널에서 나온 웹페이지 🔗 | 9/1 | **Artifacts 설명 페이지** — 공유 범위·버전·댓글. private |
| 요양보호사, 우리가 할 수 있을까 🏡 | 9/8 | Caregiver 조사 결과 한 페이지 (가족 공유) |

둘은 `read` 로 본문을 받아 읽었다. 9/1~9/2 에 **경험만으로** 쓴 단정 문장 8개를 뽑아 M2·M4 검증 목록으로 옮겼다 → [inventory.md](../01-Inventory-and-Questions/guides/inventory.md). 특히 A5 의 *"내 컴퓨터에 접근하지 못합니다"* 는 M4 실습 2 후보 (a)(Personal Ops Board Deadline 루틴)의 성립 여부를 가른다.

비인증 접근을 흉내 내려고 6개 URL 에 `curl` 을 보냈으나 **HTTP 000** — 이 세션의 셸은 외부망이 막혀 있다 `[실측]`. 시크릿 창 칸은 사용자 몫으로 남겼다. 추정으로 채우지 않았다.

### 실습 2 — 질문 9개

→ [questions.md](../01-Inventory-and-Questions/guides/questions.md). 우선순위 1(db 공유 — 원문) → 8(루틴의 볼트 접근 — POB 설계 직결) → 6(db 왕복) 순.

### 실습 3 — 서사 씨앗

→ [story-seed.md](../01-Inventory-and-Questions/guides/story-seed.md). Journal 9/1·9/3 원문 3인용. "마주침 → 몰라도 됐음 → 즉석 제작".

## 문제 해결 로그

| 문제 | 원인 | 처리 |
|---|---|---|
| curl 이 모든 아티팩트 URL 에 000 | 세션 셸 외부망 차단 | 시크릿 창 확인을 사용자 과제로. 세션이 못 하는 실측을 한 것처럼 적지 않는다 |
| 사례 인덱스가 3건으로 셌다 | 볼트 기록만 봤고 갤러리를 안 봤다 | 인덱스에 「6건」 정정 예정(M1 마감 시). 교훈: **실물 목록은 실물 저장소(갤러리)에서 뽑는다** |

## Insights (인사이트)

### 볼트에 안 적힌 실물이 절반이었다

6건 중 3건이 Task Board·Journal 어디에도 URL 이 없었다. 만든 날 Roundup 이 그것을 문장으로는 적었을지 몰라도 **링크로는 안 남겼다.** 아티팩트는 갤러리에 살고 볼트는 그 그림자였다.
> 이 Topic 의 첫 패턴 후보: **발행한 아티팩트 URL 은 발행한 그날 볼트에 적는다** (M5).

### 예측이 6/6 맞았다 — 그래서 더 의심한다

시크릿 창 결과가 「db 있음 → Sign in, 없음 → 열림, private → Sign in」으로 정확히 갈렸다. 경험이 맞았다는 뜻이지 **이유를 안다는 뜻은 아니다.** "db 가 있으면 인증이 필요하다"가 구조(익명 사용자에게 db 쓰기를 줄 수 없다)인지 설정(공유 범위 기본값)인지는 여전히 `[추론]` 이다. M2 가 문서로 가른다.

### 설명 페이지가 먼저 있었다

두 기능을 "자세히 공부하고 싶다"는 원문 뒤에, 이미 두 기능을 남에게 설명하는 페이지를 9/1·9/2 에 만들어 둔 상태였다. 경험으로 쓴 설명이고 문서 대조는 없었다 — **그래서 이 Topic 은 "새로 배우기"가 아니라 "내가 이미 남에게 한 말을 검증하기"에 가깝다.** M2·M4 의 검증 목록 8개가 그것이다.

## DoD 체크리스트 (M1)

- [x] 실물 상태표 — 6+1건 · capabilities · 마지막 수정
- [x] **시크릿 창 실측 포함** — 6/6 (db·private 3건 Sign in · 3건 열림)
- [x] 질문 목록 9개 · 담당 모듈 · 근거 종류
- [x] 🔴 실물 1건: `examples/artifact-list.json`
- [x] README · 링크 검사 (아래)
- [x] WorkLog — 실소요 기록
- [x] Daily Retrospective (아래)

**완료율**: 7/7 (100%) — 07:10 마감

## Daily Retrospective

**What went well**: 문서를 읽기 전에 갤러리를 먼저 열어 본 순서. 이것이 "실물 7건"과 "검증 목록 8개"를 만들었다 — 로드맵 M1 의 설계 의도 그대로.
**What could be improved**: 방송 전에 만든 사례 인덱스가 갤러리를 안 보고 볼트만 뒤졌다. 30분 전의 나도 같은 실수를 했다.
**Insights**: 위 두 절.
**Tomorrow's focus**: ① M2 실습 1 — 공식 문서 클리핑, 질문 1 「db 페이지는 왜 Sign in 을 요구하나」 문서로 답하기 (오늘 실측이 출발점) ② A2 배너 문구 갱신은 M3 실습 3 에서 ③ 사례 인덱스 「6건」 정정 ✅ 완료

## 참조 및 산출물

- `01-Inventory-and-Questions/README.md` · `guides/{inventory,questions,story-seed}.md` · `examples/artifact-list.json`
- `Materials_For_Topics/Claude-Artifacts-Routines/2026-09-13 {시작 프롬프트 (원문),사례 인덱스}.md`
- 실물: 아티팩트 6건 (inventory.md 링크) · 루틴 1건
