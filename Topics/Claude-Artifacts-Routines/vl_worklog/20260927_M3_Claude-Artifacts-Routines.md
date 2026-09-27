---
title: "M3 준비 — Chrome의 Claude 탭과 ChatGPT for Chrome 연결"
created: 2026-09-27 07:52:59
author:
  - "Codex"
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

## 참조 및 산출물

- Roadmap: [M3 상세 계획](../vl_roadmap/20260913_RoadMap_Claude-Artifacts-Routines.md)
- 이전 Artifact 학습: [M2 공유·버전 결과](../02-Artifacts-Sharing-and-Versions/README.md)
- 부분 선행 실습: [M4a 루틴 점검](20260921_M4a_Claude-Artifacts-Routines.md)
- 이번 세션의 새 Artifact·예제·URL: 없음
