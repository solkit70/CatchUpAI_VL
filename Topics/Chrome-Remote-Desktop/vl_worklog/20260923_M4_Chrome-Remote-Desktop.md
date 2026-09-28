---
title: "M4 WorkLog — 외부 실사용 첫 세션"
created: 2026-09-23 14:08:53
author:
  - "Codex"
topic: "Chrome-Remote-Desktop"
module: "M4"
tags:
  - vibelearn-ai
  - worklog
  - chrome-remote-desktop
---

## 세션 개요

| 항목 | 값 |
|---|---|
| 날짜 | 2026-09-23 (수) |
| 모듈 | M4 — 실사용 ① 집을 비우고 작업하기 |
| 사용자 보고 실습 시간 | 약 20분 · 시작·종료 시각 미기록 |
| 상태 | 🟡 진행 중 · iPad 외부 작업과 iPhone 모바일 데이터 접속·저장·잠금·재접속 확인, 정량 비교 대기 |

## 오늘의 학습 목표

- [x] 집 밖에서 원격 접속해 볼트 문서를 편집·저장한 결과를 확인한다 — 스타벅스에서 작업, 문서 내용 유지 확인
- [x] 테스트 폴더 정리와 OBS 상태 확인 결과를 기록한다 — 사용자 보고, 구체적 OBS 상태값은 미기록
- [x] 사용 기기·회선, 접속 시간, 한글 입력 지연과 끊김을 첫 실측표로 정리한다 — iPad·스타벅스 Wi-Fi·10초 미만·지연 크지 않음·끊김 0회
- [x] 안전 종료 후 노트북 잠금 상태를 확인한다 — 재접속 시 Windows 잠금 화면과 Windows PIN 요구 확인
- [ ] 느린 상황에 대비해 원격 작업 관리자 접근을 검증한다 — 프로세스 강제 종료는 별도 안전 실험

## 진행 내용

### 활동 1 — 원격 실사용 첫 세션

**사용자 보고 원문**: [[2026-09-23#Chrome Remote Desktop M4 실사용 실습 (구술 원문)|Journal 원문]]에 그대로 보존했다.

**결과**: 사용자는 원격 접속 후 문서를 편집하고 테스트 폴더를 정리했으며, OBS를 실행해 상태를 확인했다고 보고했다. Task Manager도 열어 확인했고, 전체 세션은 약 20분이었다. 한글 입력 지연은 크게 느끼지 못했다. **Windows Lock → 잠금 확인 → Disconnect** 순서가 잘 작동했다고 보고했다.

**처음 보고에서 빠졌던 세부 정보**: 실습 장소·기기·회선, 접속 시간, 끊김 횟수와 편집 내용 유지 여부는 아래 활동 2에서 보충됐다. OBS에서 확인한 구체적 상태, Disconnect 뒤 물리 화면 또는 재접속 직후의 Windows 잠금 상태는 아직 별도로 보고되지 않았다. Task Manager에서 프로세스를 종료했다는 보고도 없으므로 추정해서 완료로 기록하지 않는다.

### 활동 2 — 외부 환경·저장·접속 품질 보충 확인

**사용자 보고 원문**: [[2026-09-23#Chrome Remote Desktop M4 외부 접속 결과 보충 (구술 원문)|Journal 원문]]에 그대로 보존했다.

**결과**: 사용자는 집 밖 스타벅스에서 **iPad와 매장 Wi-Fi**로 작업했다. 편집한 문서의 내용이 남아 있음을 확인했다. 접속까지는 **10초 미만으로 추정**, 사용 중 끊김은 **0회**, 한글 입력 지연과 다른 불편은 크게 느끼지 못했다. Disconnect 후 재접속도 가능했다.

**확인 범위**: 재접속 가능 여부와 Windows 잠금 유지 여부는 구분한다. 재접속 직후 Windows PIN 요구는 아래 활동 3에서 추가로 확인됐다. 별도의 CPU·메모리 고부하 상황이나 프로세스 종료는 실측하지 않았다.

### 활동 3 — 재접속 잠금 확인과 iPhone 실습 준비

**사용자 보고 원문**: [[2026-09-23#Chrome Remote Desktop M4 재접속 잠금과 iPhone 접속 요청 (구술 원문)|Journal 원문]]에 보존했다.

**결과**: 사용자는 Disconnect 후 다시 접속했을 때 **Windows 잠금 화면이 나타나 Windows PIN을 입력해야 했다**고 확인했다. 이는 M4 외부 세션에서도 Windows Lock → 잠금 확인 → Disconnect 순서 뒤 Windows 잠금이 유지됐다는 근거다. 노트북 물리 화면을 귀가 후 확인했다는 보고는 아니므로 그 사실까지 확대하지 않는다.

**다음 실습**: 사용자는 iPhone에서도 접속하기를 원한다. iPhone 접속 자체는 아직 실측되지 않았으므로, [작은 화면 작업 안내](../04-Real-Use-Work/guides/working-on-small-screen.md)에 따라 먼저 Safari 웹 경로로 접속한 뒤 실제 결과를 기록한다.

### 2026-09-27 방송 중 준비 업데이트 — iPhone 설정 완료, 실측 보류

사용자는 iPhone에서 Chrome Remote Desktop의 Safari 설정과 홈 화면 추가를 마쳤다. 다만 라이브 방송에서는 실제 접속을 하지 않기로 했으므로, LTE·5G 접속, 문서 입력·저장, 접속 시간·끊김, Windows Lock → Disconnect 결과는 아직 확인하지 않았다. 이 준비만으로 M4의 외부 실사용 DoD를 완료로 바꾸지 않는다. 따라 할 iPhone 안내는 [connect-from-iphone.md](../02-Install-and-First-Connect/guides/connect-from-iphone.md)에 분리했다.

### 활동 4 — iPhone 모바일 데이터 첫 실측

방송 후 사용자는 iPhone의 Wi-Fi를 끄고 홈 화면의 Remote Desktop으로 노트북에 접속했다. 메모장에서 한글 한 줄을 입력·저장했고, 영문 입력도 가능했다고 보고했다. Windows 잠금 → 잠금 화면 확인 → 잠금 해제 → Disconnect → 재접속도 모두 작동했다고 보고했다. 이후 사용자는 저장 내용이 남아 있음을 확인했고, 접속은 약 2초로 추정했으며, 사용 중 끊김이 없었다고 보충했다. 이 시간은 타이머 측정값이 아니다. 사용자 원문: [[Journal/2026-09-27#Chrome Remote Desktop iPhone 모바일 데이터 실습 (구술 원문)|첫 보고]] · [[Journal/2026-09-27#Chrome Remote Desktop iPhone 실측 결과 보충 (구술 원문)|결과 보충]].

처음 입력할 때 Windows의 “Do you want allow this app to make changes to your device?” 권한 확인창이 나타났고, 사용자가 **Yes**를 선택한 뒤 한글·영문 입력이 가능해졌다. 사용자가 제공한 [현장 사진](../02-Install-and-First-Connect/images/005_iPhone_test_Windows_UAC_Command_Processor.jpg)에는 `Windows Command Processor`와 확인된 게시자 `Microsoft Windows`가 보인다. 사진은 14:39에 촬영됐고 RustDesk 설치·서비스 등록도 같은 시각이므로, 설치 과정의 권한 요청이었을 가능성이 높다. 이는 시간에 근거한 추정이며 CRD 입력 자체의 권한 요청으로 설명하지 않는다. [기기·회선 실측표](../04-Real-Use-Work/examples/device-network-matrix.md)에 확인한 값과 추정·미기록 값을 분리했다. 계정 메뉴에서 잠금을 찾기 어려운 최신 Windows 11 화면을 반영해 [iPhone 안내](../02-Install-and-First-Connect/guides/connect-from-iphone.md#5-안전하게-종료하기)의 잠금 경로를 수정했다.

## 문제 해결 로그

이 세션에서 연결 오류나 큰 한글 입력 지연은 보고되지 않았다. CPU·메모리 과다 사용 상황이나 원격 프로세스 종료는 아직 실측되지 않았다.

## DoD 체크리스트

- [x] 외출 상태에서 작업 한 건 완료 — 스타벅스에서 문서 편집, 내용 유지 확인
- [ ] 기기 3 × 회선 2 이상 실측표 — 보유 장비에 맞는 범위 확인·조정 필요
- [x] 「밖에서 되는 일 / 안 되는 일」 목록 — 이번에 된 일·실패 없음·미실측 범위를 구분해 기록
- [x] 세션 종료 후 잠금 실측 확인 — Disconnect 뒤 재접속 시 Windows 잠금 화면·PIN 요구 확인
- [x] README · 링크 · WorkLog · Retrospective — 9/27 iPhone 결과와 안내 수정 반영, 상대 링크 검사 통과
- [ ] 따라 하기 검증 — 작은 화면 요령 문서가 실제로 도움이 되는가

**완료율**: 4/6 — 외부 문서 작업, 가능/미실측 목록, 종료 후 재접속 시 Windows 잠금, 문서·링크 점검을 확인했다. 기기·회선 정량 비교와 수정된 안내의 따라 하기 재검증은 남아 있다.

## Daily Retrospective

### What went well

- 문서 편집, 테스트 폴더 정리, OBS 상태 확인, Task Manager 열기, 안전 종료까지 약 20분 안에 시도했다.
- 한글 입력 지연은 크게 느끼지 못했다고 보고했다.

### What could be improved

- 다음 실측에는 같은 작업을 iPhone 또는 다른 회선에서 반복해 iPad·스타벅스 Wi-Fi 결과와 비교해야 한다.
- 로드맵의 기기 3종 × 회선 2종 조건이 실제 보유 장비에 맞는지 확인해야 한다. Android 기기는 보유하지 않는다.

### Insights

- M3에서 검증한 안전 종료 순서를 실제 작업 끝에 적용했다. 이번에는 원격 작업 관리자 화면까지 열어 볼 수 있었다.

### Tomorrow's focus

- iPhone Safari에서 같은 Google 계정으로 첫 접속하고, 한 줄 입력·저장·안전 종료가 되는지 확인한다. 이어 보유 장비 기준의 회선 비교 범위를 정한다.
- 원격 작업 관리자에서는 우선 CPU·메모리 사용량을 확인한다. 중요한 시스템 프로세스나 Chrome Remote Desktop 호스트를 시험 삼아 종료하지 않는다.

### 9/27 추가 회고

- iPhone 모바일 데이터에서도 입력·저장 내용 유지와 잠금·재접속 흐름이 동작했다. 접속은 약 2초 추정, 사용 중 끊김은 없었다. Windows 11 계정 메뉴에서 잠금을 찾는 안내가 실제 화면과 달라 전원 메뉴 경로로 수정했다.
- 권한 확인창은 사진으로 요청 프로그램과 게시자를 확인했다. RustDesk 설치와 같은 시각이라 그 설치 과정이 원인일 가능성이 높으나 확정하지 않는다. 다음 비교 실습에서는 같은 작업의 접속 시간을 타이머로 재고 입력 지연도 함께 기록한다.

## 참조 및 산출물

- [M4 모듈 안내](../04-Real-Use-Work/README.md)
- [첫 외부 세션 기록](../04-Real-Use-Work/examples/real-session-log.md)
- [기기·회선 실측표](../04-Real-Use-Work/examples/device-network-matrix.md)
- [작은 화면 작업 안내](../04-Real-Use-Work/guides/working-on-small-screen.md)
- [M4 로드맵](../vl_roadmap/20260920_RoadMap_Chrome-Remote-Desktop.md#M4--실사용--집을-비우고-작업하기)
- [M2 첫 접속 실측](../02-Install-and-First-Connect/examples/first-connect-log.md)
- [M3 안전 종료 실측](20260923_M3_Chrome-Remote-Desktop.md#활동-5--ipad에서-windows-잠금-후-연결-종료재접속)

**작성자**: Codex
**방법론**: VibeLearn AI
