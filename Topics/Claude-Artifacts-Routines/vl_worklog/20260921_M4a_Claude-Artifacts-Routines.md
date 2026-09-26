---
title: "M4a — 유일한 루틴이 3주째 조용히 실패하고 있었다 · 환경의 네트워크 모드였다"
created: 2026-09-21 11:00:00
author:
  - "Claude Code"
topic: "Claude-Artifacts-Routines"
module: "M4"
tags:
  - vibelearn-ai
  - worklog
  - claude-artifacts-routines
---

## 세션 개요

| 항목 | 값 |
|---|---|
| 날짜 | 2026-09-21 (월) — 사용자가 「routine job 이 계속 실패한다, 왜인지 분석해 달라」 |
| 시작 · 종료 | 09:55 · 10:45 |
| **실소요** | **약 50분.** 그중 사용자가 웹 UI 에서 환경 설정을 찾는 데 약 12분 (캡처 3회) |
| 직전 WorkLog 「개선할 점」 체크 | M2: *"공개 후 Share 메뉴 토글 유무 — 사용자 확인"* → 이번 세션 범위 밖, 미확인 그대로 |
| 모듈 | **M4 — Routines.** 로드맵 순서(M3 뒤)를 건너뛰고 **실습 1(WBLP 루틴 점검)만** 먼저 |
| 결과 | 3주 실패 원인 확정 → 복구 → 첫 알림 메일 → 프롬프트 결함 수정. 문서 3편 |

## 오늘의 학습 목표

- [x] 기존 WBLP 루틴의 실행 이력을 읽고 "조건 충족 시에만 이메일"이 실제로 그렇게 동작했는지 확인·개선 — **실행 이력 4회 실측, 개선 2건**
- [ ] 트리거·환경·알림·비용을 공식 문서 근거로 — 문서 클리핑은 아직
- [ ] 두 번째 루틴 발행 / [ ] 로컬 vs 클라우드 판단표

## 진행 내용

### 1. 로그 읽기 — 세 번 다 같은 자리 (15분)

`schedule` 스킬 → `RemoteTrigger get` · `list_runs` · `get_run_log`. 9/7 · 9/14 · 9/21 세션 로그를 전부 열었다. 셋 다 첫 도구 호출에서 `www.amazon.jobs:443 — connect_rejected (organization policy)`, WebFetch 는 `EGRESS_BLOCKED`. 9/14 로그에는 루틴이 스스로 조회한 프록시 허용 목록이 있었다 — 패키지 저장소와 Anthropic API 뿐.

### 2. 로컬 재현 — 상대 문제가 아니다 (5분)

같은 URL 을 내 PC 에서 `curl -L` → **HTTP 200, hits 7.** 이 한 번으로 「아마존이 봇을 막는다」 가설이 사라졌다. 그리고 결과에 **미국 기술직 4건**이 있었다 — 루틴이 정상이었다면 9/14 · 9/21 에 메일이 갔어야 하는 공고들.

### 3. 환경 설정 찾기 — 12분 (사용자 캡처 3회)

「Environments 탭」이 어디 있는지가 문제였다. Settings → Claude Code 페이지(캡처 1·2)에는 없었고, 그 페이지 하단의 *"Cloud sessions are managed separately"* 가 힌트였다. **New → `Default` 칩 → Cloud → 편집** 에서 **Network access: Trusted** 를 발견(캡처 3). 사용자가 amazon.jobs 를 허용에 추가하고 저장.

### 4. 수동 실행 → 113초 뒤 성공 (5분)

`RemoteTrigger run` → 4개 쿼리 전부 HTTP 200 → 루틴이 미국 기술직 4건(Berwick PA ×2 · Canton MS · Boardman OR)을 잡아 **Gmail 발송.** 워싱턴은 0.

### 5. 덤 — 루틴이 프롬프트 결함을 찾아냈다 (10분)

복구 실행 로그에서 루틴이 `loc_query=Washington` 이 무시된다는 것(`location: null`)을 스스로 확인하고 `normalized_location[]` 로 재시도했다. 내 PC 에서 4개 파라미터를 검증(무시 2 · 작동 2)한 뒤 `RemoteTrigger update` 로 프롬프트를 고쳤다 — URL 4개 · 기준선 9/21 · 파라미터 경고 · 네트워크 실패 시 행동. Datacenter Topic 문서 3곳도 같이.

## 문제 해결 로그

| 증상 | 원인 | 조치 |
|---|---|---|
| 루틴 3주 연속 실패, 푸시만 옴 | 환경 `Default` 의 Network access = Trusted → amazon.jobs 차단 | 환경에서 도메인 허용 (사용자, 웹 UI) |
| 환경 설정 위치를 못 찾음 | Settings → Claude Code 에는 없음 | New 세션 패널의 환경 칩 → Cloud → 편집 |
| 쿼리 ②가 ①과 같은 결과 · ④에 스페인 | API 가 `loc_query` · `country[]` 를 무시 | `normalized_location[]` · `normalized_country_code[]` 로 교체, 로컬 검증 |
| `sleep` 로 대기가 막힘 | 도구 정책 | 백그라운드 `until` 루프로 대기 |

## Insights (인사이트)

**「조건 충족 시에만 알림」은 실패까지 조용하게 만든다.** 이 루틴은 잘 설계됐다 — 매주 「없음」 메일을 안 보내니 알림을 무시하지 않게 된다. 그런데 바로 그 설계 때문에 3주 동안 **실패한 주와 진짜로 공고가 없던 주가 똑같이 보였다.** 루틴은 매번 푸시로 「확인 못 했다」고 했지만, 푸시 한 줄이 「환경 정책이 도메인을 막는다」로 읽히려면 사람이 로그를 열어야 했다. 조용한 자동화에는 **「실패는 다른 채널로」 + 「로그는 주기적으로 사람이」** 두 규칙이 붙어야 한다.

**환경과 루틴은 다른 층이고, 다른 도구로 고친다.** 루틴 API 로는 `environment_id` 를 고를 수 있을 뿐 환경의 네트워크 규칙은 웹 UI 전용이다. M4 개념 ①「루틴 = 서버에서 도는 Claude Code 세션」에 한 줄이 붙는다 — **그 서버의 네트워크 규칙 아래서.** 내 PC 에서 되던 것이 클라우드에서 안 되면 첫 의심은 이것.

**AI 가 자기 실패를 진단해 두었는데 사람이 3주 뒤에야 읽었다.** 9/14 로그에서 루틴은 이미 프록시 상태를 조회하고 「amazon.jobs 를 allowlist 해야 한다」고 적었다. 복구 실행에서는 파라미터 결함까지 스스로 찾아 우회했다. 부족했던 건 진단이 아니라 **진단을 읽는 사람의 루틴**이었다. M5(사용 패턴)에 넣을 것: 루틴 실행 로그를 월 1회 `get_run_log` 로 훑는 로컬 루틴.

## DoD 체크리스트 (M4 — 실습 1 부분)

- [ ] 공식 문서 클리핑 1건 이상 — **아직**
- [x] WBLP 루틴 실행 이력 실측 + 개선 여부 결정 — 4회 실측 · 개선 2건(환경 · 프롬프트) 실행
- [ ] 🔴 두 번째 루틴 발행 — 아직
- [ ] 로컬 vs 클라우드 판단표 — 아직
- [x] README · 링크 검사 통과 — `04-Routines-Lab/README.md`
- [x] WorkLog(실소요) · Daily Retrospective

**1.5/6 — M4 는 열린 채로 둔다.** 실습 1 만 사고 대응으로 앞당겨 끝났다.

## Daily Retrospective

### What went well
- 로그 → 로컬 재현 → 환경 순으로 좁혀서 **한 번에 원인을 맞혔다.** 프롬프트를 먼저 고치기 시작했으면 헛수고였을 것이다
- 복구 직후 수동 실행으로 **다음 주를 기다리지 않고** 검증했고, 그 실행이 프롬프트 결함까지 드러냈다

### What could be improved
- 환경 설정 위치를 **먼저 확인하고 안내했어야** 했다. 「Settings → Environments 탭」이라고 추정으로 말해서 사용자가 두 번 헛걸음했다. 문서를 못 읽었으면 「캡처를 보내 달라」부터가 맞다
- 루틴이 9/7 에 이미 「allowlist 필요」라고 적었는데 2주를 흘렸다 — Topic M4 를 미뤄 둔 대가

### Insights → 영상(M6)에 쓸 장면
1. 세 개의 실행 로그가 같은 줄에서 죽는 화면
2. 내 PC 의 `HTTP 200 · hits 7` 한 줄
3. 「Edit cloud environment — Network access: Trusted」 캡처
4. 복구 실행이 스스로 `location: null` 을 찾아내는 로그

## 참조 및 산출물

**신규**: `04-Routines-Lab/README.md` · `guides/wblp-routine-audit.md` · `troubleshooting/routine-did-not-run.md`
**수정**: 루틴 프롬프트(`RemoteTrigger update`) · `Datacenter-Workforce-Programs` 문서 3곳 파라미터 · `AI/Research/2026-09-01 오늘의 취업 지원 실행 계획` ⑥ 절
**도구**: `schedule` 스킬 · `RemoteTrigger` (get · list_runs · get_run_log · run · update)
