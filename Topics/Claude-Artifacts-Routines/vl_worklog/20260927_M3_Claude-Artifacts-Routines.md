---
title: "M3 준비 — Chrome의 Claude 탭과 ChatGPT for Chrome 연결"
created: 2026-09-27 07:52:59
author:
  - "Codex"
  - "Claude Code"
topic: "Claude-Artifacts-Routines"
module: "M3"
tags:
  - vibelearn-ai
  - worklog
  - claude-artifacts-routines
  - live-broadcast
---

## 세션 개요

| 항목 | 값 |
|---|---|
| 날짜 | 2026-09-27 — Live #29 종료 전 |
| 실소요 | 방송 종료 정리 전이라 별도 계측하지 않음 |
| 직전 WorkLog의 개선할 점 확인 | M4a의 「환경 설정 위치를 추정으로 안내하지 말고 화면으로 확인한다」를 적용했다. ChatGPT 데스크톱 앱의 **Settings → Computer use** 화면에서 Chrome 확장 설치 상태를 확인했다. |
| 모듈 | **M3 — Artifacts 런타임 기능 실험** |
| 결과 | **준비 완료, 실습 미시작.** Chrome에서 Claude 탭을 열고 ChatGPT for Chrome 확장을 설치·고정해 사이드 패널을 열었다. |

## 오늘의 학습 목표

- [x] Claude 웹을 열어 이후 M3 실습을 할 브라우저 경로 준비
- [x] ChatGPT for Chrome 확장 설치·고정 및 사이드 패널 표시 확인
- [x] VS Code Codex Extension과 ChatGPT 데스크톱의 브라우저 제어 범위를 구분
- [ ] 5종 최소 예제 발행·확인
- [ ] db 왕복과 `if_version` 거부 실측
- [ ] 기존 Artifact 재검토·수정

## 진행 내용

### 1. Claude 웹 작업 환경 준비

Chrome에서 `claude.ai/new?redirect=claude.com&via=cookie`를 열었다. 이후 작업은 Claude 웹에서 Artifact를 실제로 만들고 확인하는 방식으로 이어 갈 수 있는 상태가 되었다.

### 2. ChatGPT for Chrome 연결

ChatGPT 데스크톱 앱의 **Settings → Computer use**에서 Google Chrome 제어와 확장 설치 상태를 확인했다. Chrome에서 **ChatGPT for Chrome** 확장을 설치·고정했고, 브라우저 오른쪽 사이드 패널에 ChatGPT가 표시되는 것까지 확인했다.

이 연결은 ChatGPT 데스크톱 앱의 Work/Codex 대화에서 Chrome을 선택해 브라우저 작업을 보조하는 경로다. VS Code의 Codex Extension은 이 확장이 붙은 Chrome 탭이나 로그인 세션을 직접 제어하지 않는다. 따라서 M3의 Claude 웹 실습은 현재 준비된 Chrome/ChatGPT 데스크톱 경로에서 진행한다.

### 3. 방송 종료에 따른 범위 중단

라이브 방송 종료 시점이라 Artifact 생성·발행은 시작하지 않았다. 특히 db 카운터, 다른 계정/시크릿 창 확인, `read_db`·`write_db`·`if_version` 실험, 기존 부스 Artifact 수정은 **아직 실측값이 없다.** 준비 작업을 M3 완료나 기능 실험 완료로 처리하지 않는다.

## 문제 해결 로그

| 상황 | 확인 결과 | 처리 |
|---|---|---|
| ChatGPT 데스크톱 앱에서 Computer use 위치를 찾기 어려움 | Settings의 Integrations 아래 **Computer use**에 있음 | 화면에서 Chrome 확장 설치 상태를 확인 |
| VS Code Codex Extension에서 같은 Chrome을 사용할 수 있는지 | 현재 ChatGPT for Chrome 확장/Browser 제어는 VS Code Codex Extension에 제공되지 않음 | Claude 웹 실습은 ChatGPT 데스크톱 + Chrome 경로로 유지 |

## DoD 체크리스트

로드맵 M3의 Definition of Done:

- [ ] 5종 예제 발행 · URL 기록 · 시크릿 창 결과
- [ ] db 왕복 + `if_version` 거부 로그
- [ ] 🔴 실물 1건: 부스 매니저 또는 현황판을 실제로 수정·재발행했다 (또는 "수정 불필요" 근거)
- [ ] 선택표 완성
- [ ] README · 링크 검사 통과
- [x] WorkLog · 다음 세션 재개 지점 기록

**완료율**: M3 핵심 DoD 0/6 (준비 기록은 완료했으나 실습 산출물은 0건)

## Daily Retrospective

### What went well

브라우저 제어가 가능한 경로와 VS Code Extension의 범위를 방송 중 화면으로 확인했다. 다음 세션에는 설치·권한 찾기에 시간을 쓰지 않고 Claude Artifact 실습부터 시작할 수 있다.

### What could be improved

준비 과정만으로는 M3의 capability 동작을 하나도 검증하지 못했다. 다음 세션에는 화면 연결 확인을 반복하지 않고 첫 Artifact 발행을 최우선으로 한다.

### Insights

브라우저를 제어하는 도구와 웹 서비스에서 실물을 만드는 도구는 별개다. 연결이 준비되었다는 사실과 Artifact 기능이 작동한다는 사실을 같은 완료로 기록하면 안 된다.

### Tomorrow's focus

1. Claude 웹에서 M3 실습 1의 **db 카운터**를 만들고 발행한다.
2. URL, capability 선언, 시크릿 창 결과를 `lab-log.md`에 기록한다.
3. 카운터로 `read_db` → `write_db` → 이전 version의 `if_version` 거부를 실측한다.
4. 그 뒤 나머지 4종 최소 예제와 기존 Builders Lounge Artifact 재검토 범위를 정한다.

## 이어서 — VS Code Claude Code 확장 세션 (2026-09-27 오후)

사용자: 「M3 런타임 기능 실험 은 Codex 에서 작업을 하려다가 VS Code 내에서 Codex Extension 으로 진행하는데 어려움이 있어서 중단 한 겁니다. 이곳은 VS Code 의 Claude Extension 인데요. 여기서 M3 단원을 다시 진행 해 주세요.」

**경로 전환**: Claude Code 세션에는 `Artifact`(발행 · asset 업로드) 와 `ArtifactData`(db 읽기·쓰기) 도구가 직접 있다. 브라우저를 조작하지 않고 세션이 발행·db 실측을 하고, 사람은 URL 을 열어 화면만 확인한다. 오전의 Chrome + ChatGPT 경로는 쓰지 않았다.

| 순서 | 한 일 | 결과 |
|---|---|---|
| 0 | `artifact-capabilities` 스킬 로드 · `db.d.ts` · `user.d.ts` · `comments.d.ts` · `assets.d.ts` 확인 | runtime contract **0.2.60** |
| 1 | 실습 1 — 5종 최소 예제 작성·발행 | 5개 URL → [lab-log](../03-Artifacts-Capabilities-Lab/guides/lab-log.md) |
| 2 | 실습 2 — db 왕복 (세션 쪽) | get(없음) → set v1 → update(if_version 1) v2 → **update(옛 if_version 1) `version_mismatch` 거부, 아무것도 안 쓰임** → [db-roundtrip](../03-Artifacts-Capabilities-Lab/guides/db-roundtrip.md) |
| 3 | 세션에서 03 보관함에 이미지 1장 업로드 | `/_blob/8bba69ce…` |
| 4 | 발견 | 한 세션의 아티팩트 감시는 10개 — 예제 발행으로 부스 매니저·현황판 감시가 밀려남 → [troubleshooting](../03-Artifacts-Capabilities-Lab/troubleshooting/cdn-and-storage-gotchas.md) |

**DoD (갱신)**

- [x] 5종 예제 발행 · URL 기록 · 화면 확인 — ①~⑤ 모두 기대대로 (사용자). 다른 계정 확인은 생략 (사용자: 「간단하게」)
- [x] db 왕복 + `if_version` 거부 로그 — 세션 쓰기 → 화면 확인 → 화면 +1 두 번(v4) → 세션 읽기 → **실제 충돌에서 옛 v2 쓰기 거부** → v4 로 재시도 통과(v5)
- [x] 실물 1건 — 부스 매니저 점검, **수정 불필요 근거** (행사 종료 · 놓친 것 2개: 배치도 base64 → assets, 활동 로그에 user id) → [bighug-artifacts-review](../03-Artifacts-Capabilities-Lab/guides/bighug-artifacts-review.md)
- [x] 선택표 · README · 링크 검사 (정상 20 · 깨짐 0)

**M3 DoD 6/6 — ✅ 완료** (실소요: 오후 세션 약 1시간)

### Daily Retrospective (오후)

- **잘된 점**: 직전 개선점(「화면 연결 확인을 되풀이하지 말고 첫 Artifact 발행부터」)을 지켰다 — 세션의 Artifact 도구로 첫 호출부터 발행했다. 사람이 +1 을 누른 덕에 **사람과 AI 가 같은 문서를 고치는 실제 충돌**을 만들 수 있었다
- **개선할 점**: 예제를 한 세션에서 연달아 발행해 운영 중인 아티팩트 감시가 밀려났다 — 실습용 발행은 다른 세션에서. 실습 3 을 「대상 고르기」로 사용자에게 넘겼는데 무엇을 하는지 설명이 부족했다 — 선택지보다 목적을 먼저 말한다
- **인사이트**: Artifact 에 AI 를 붙일 때 첫 안전장치는 `if_version` 이다. 그리고 「Send to Claude」 댓글은 페이지와 세션을 잇는 가장 가벼운 통로다
- **다음**: M4 Routines 나머지(공식 문서 · 두 번째 루틴 · 판단표) → M5 → M6 영상
- [x] WorkLog

## 참조 및 산출물

- Roadmap: [M3 상세 계획](../vl_roadmap/20260913_RoadMap_Claude-Artifacts-Routines.md)
- 이전 Artifact 학습: [M2 공유·버전 결과](../02-Artifacts-Sharing-and-Versions/README.md)
- 부분 선행 실습: [M4a 루틴 점검](20260921_M4a_Claude-Artifacts-Routines.md)
- 이번 세션의 새 Artifact·예제·URL: 없음
