---
title: "M2 WorkLog — 설치와 첫 연결 (호스트와 밖에서 쓰는 기기)"
created: 2026-09-20 20:55:00
author:
  - "Claude Code"
topic: "Chrome-Remote-Desktop"
module: "M2"
tags:
  - vibelearn-ai
  - worklog
  - chrome-remote-desktop
---

## 세션 개요

| 항목 | 값 |
|---|---|
| 날짜 | 2026-09-20 (일) — 오후 설치 · 저녁 iPad 접속 |
| 모듈 | **M2 — 설치와 첫 연결** |
| 실소요 | 약 2시간 (설치·문서 1h10m + iPad 접속·문서 50m) — 계획 2h |
| 결과 | 문서 5편 + README · 캡처 10장 · **DoD 5/6 — 🟡 진행 중** (두 번째 기기 남음) |

## 오늘의 학습 목표

- [x] 집 컴퓨터에 Chrome Remote Desktop 호스트를 설치하고 이름·PIN 을 설정할 수 있다
- [ ] 폰/태블릿/노트북 중 **최소 2개**에서 접속할 수 있다 — iPad 1개 완료, Android 폰·다른 컴퓨터 남음
- [x] 접속이 안 될 때 확인할 4가지를 순서대로 점검할 수 있다
- [x] 설치 단계를 화면 캡처와 함께 다른 사람이 따라 할 수 있게 적을 수 있다

## 진행 내용

### 활동 1 — 호스트 설치 (실습 1, 30분)

가이드([install-host-windows.md](../02-Install-and-First-Connect/guides/install-host-windows.md))를 먼저 쓰고, 사용자가 그대로 따라 설치했다. 설치 전에 호스트가 없는 것을 확인했으므로 **진짜 첫 설치**다.

| 실측 | 값 |
|---|---|
| 걸린 시간 | 약 9분 (15:17~15:26, 캡처 포함) |
| 호스트 버전 · 경로 | 151.0.7922.13 · `Program Files (x86)` 쪽 |
| 서비스 | `chromoting` 실행 중 · **자동 시작** (재부팅해도 대기) |
| 설정 파일 `host.json` | 존재 — 일반 사용자 권한으로는 **읽기 거부** (계정 정보가 보호되고 있다는 뜻) |

**가이드가 실제와 달랐던 곳 두 군데를 고쳤다**: ① 「다운로드 → 설치」가 아니라 **「확장 프로그램 추가 → 설치 파일 실행」 두 단계** ② PIN 최소 6자리가 **설치 화면에 명시**돼 있다 (M1 에서 「도움말에 없다」고 적었던 것을 보완).

### 활동 2 — 캡처 검토에서 나온 것 (15분)

캡처를 한 장씩 보다가 **문서에 그대로 들어갈 뻔한 것 두 가지**를 잡았다.

1. **기기 이름이 본명이었다.** 이름 입력 칸에 Windows 사용자 이름이 기본값으로 들어 있었고, 그대로 Next 를 눌러 본명이 등록됐다. 사용자는 `CatchUpAI` → `CatchUpAI_laptop` 으로 바꿨다 (채널·활동명이라 오히려 알려져도 좋다는 판단). 이름 화면 캡처는 본명 자리를 가린 `_masked` 본으로 교체
2. **「Remote devices」와 「This device」에 같은 컴퓨터가 두 번 보인다.** 사용자가 직접 「한쪽 이름을 바꾸면 다른 쪽도 바뀐다」로 같은 기기임을 확인했다 — 이 확인 방법 자체를 문서에 넣었다

### 활동 3 — 구글 계정 변경 (10분)

사용자가 「호스트의 구글 계정을 바꿀 수 있나」를 물었다. 조사 결과 **「계정 전환」은 없고 삭제 → 다른 계정으로 재설정**이며 PIN 도 새로 만들어진다. 사용자가 실제로 바꿨고, 15:38 에 호스트 프로세스가 재시작된 것으로 확인했다. 이 절차와 「호스트 1대 = 계정 1개, 동시 접속 불가, 잠깐 남에게 보여 줄 땐 Remote Support」를 문서화했다.

### 활동 4 — iPad 접속 (실습 2, 40분)

**첫 막힘: App Store 에 앱이 없다.** 사용자가 Perplexity 로 「iOS 는 웹앱 방식」이라는 답을 받아 왔고, 공식 도움말과 보도로 확인했다 — **구글이 2025-09 iOS 앱을 폐지**했다. Android 는 앱이 그대로라 「나만 안 되나」 싶어지는 자리다. Safari(Chrome 아님 — 홈 화면 추가가 Safari 에서만 제대로 됨)로 진행.

| 실측 | 값 |
|---|---|
| 접속 | 20:05 Safari → PIN → 접속, 약 2분 |
| 홈 화면 추가 | 「Remote Desktop」 · **Open as Web App** 켬 |
| 회선 | 집 Wi-Fi (VPN 켜진 상태) ✅ → **폰 핫스팟 LTE ✅** — 체감 차이 없음, 빠름 |
| 입력 | 영문 ✅ · **한글 ✅** · Ctrl+S ✅ · 트랙패드 모드 ✅ |

캡처에서 새로 알게 된 것: **사이트가 먼저 홈 화면 추가를 안내**한다 · PIN 화면에 「자주 안 쓰면 기억한 PIN 이 지워질 수 있다, 홈 화면에 추가하면 유지」 · 「Open as Web App」 토글이 꺼져 있으면 그냥 즐겨찾기가 된다.

### 활동 5 — 문서화 (25분)

[connect-from-phone.md](../02-Install-and-First-Connect/guides/connect-from-phone.md) · [connect-from-laptop.md](../02-Install-and-First-Connect/guides/connect-from-laptop.md)(실측 대기) · [first-connect-log.md](../02-Install-and-First-Connect/examples/first-connect-log.md) · [cannot-connect.md](../02-Install-and-First-Connect/troubleshooting/cannot-connect.md) · [README](../02-Install-and-First-Connect/README.md).

## 문제 해결 로그

| 증상 | 원인 | 조치 |
|---|---|---|
| 기기 이름에 본명 등록 | 입력 칸 기본값 = Windows 사용자 이름 | 연필 아이콘으로 변경 · 캡처 마스킹 · 가이드에 경고 |
| 같은 컴퓨터가 두 줄 | Remote devices / This device 두 시점 | 이름 변경 동기화로 동일 기기 확인 · 문서화 |
| iPad App Store 에 앱 없음 | 2025-09 iOS 앱 폐지 | Safari + 홈 화면 추가 (Open as Web App) |
| **iPad 공유 메뉴 캡처에 연락처 4명의 이름·사진** | iOS 공유 시트 기본 동작 | 해당 줄 가린 `_masked` 본 생성 · 원본은 문서에 안 씀 · troubleshooting #3 으로 기록 |
| 마스킹 텍스트 한글이 네모로 깨짐 | PIL 기본 폰트 | 맑은 고딕 지정 |
| 「노트북 브라우저 접속」을 못 함 | 집 컴퓨터 자체가 노트북 | 두 번째 컴퓨터가 있을 때로 미룸 (M4 와 겹침) — 가이드는 작성 |

## DoD 체크리스트

- [x] 호스트 설치 완료 · 기기 목록에 「온라인」
- [ ] 최소 2개 기기에서 접속 성공 (하나는 LTE/5G) — **iPad(LTE ✅) 1개.** Android 폰 남음
- [x] 설치 가이드에 캡처 7장 이상 · 마스킹 확인 — 10장 (본명 1 · 연락처 2 마스킹)
- [x] `cannot-connect.md` 에 증상 4개 이상 — 실제 겪은 4 + 점검표 6
- [x] README · 링크 확인 · WorkLog · Retrospective
- [x] **따라 하기 검증** — 설치 6단계 전부 실제 화면 캡처 · 막히는 자리 5곳이 「왜」와 함께 적혀 있다

**5/6 — 🟡 진행 중.** 남은 것: Android 폰 접속(10분) · 실습 3 일부러 막아 보기(절전·다른 계정은 M3 에서 같이).

## Daily Retrospective

### What went well
- **가이드를 먼저 쓰고 그대로 따라 하게 한 것**이 「따라 하기 검증」 그 자체였다. 실제와 다른 곳(두 단계 설치 · PIN 6자리 명시)이 바로 드러났고, 그 자리에서 고쳤다
- 캡처를 **한 장씩 눈으로 확인한 것**이 개인 정보 두 건(본명 · 연락처)을 잡았다. 자동으로 넣었으면 그대로 공개될 뻔했다
- 걱정했던 **한글 입력과 LTE 속도가 둘 다 문제없었다.** 「모바일은 한글이 깨진다」는 내가 갖고 있던 옛 정보였다

### What could be improved
- 두 번째 기기를 오늘 못 했다. 집 컴퓨터가 노트북이라 「노트북에서 접속」이 성립하지 않는다는 것을 **로드맵 쓸 때 놓쳤다** — 환경란에 「호스트 = 집 데스크톱」이라고 적어 놓고 실제로는 노트북이었다. 로드맵 환경란을 고친다
- 실습 3(일부러 막아 보기)을 못 했다. 절전·다른 계정은 M3 와 겹치니 그쪽에서 하고, PIN 오입력·인터넷 끊기는 다음 세션 첫 10분에 한다

### Insights

**「기본값」이 가장 위험한 자리다.**
본명 등록도, 연락처 노출도, 사용자가 무언가를 잘못 입력해서가 아니라 **화면이 알아서 채워 준 것을 그대로 두어서** 생겼다. IT 지식이 없는 사람일수록 기본값을 그대로 둔다. 그래서 안내 영상에서 「여기는 그냥 Next 누르지 마세요」라고 **멈춰 세우는 자리**를 정확히 짚어 줘야 한다. 이게 M7 영상의 구조가 될 것 같다 — 「하는 법」이 아니라 **「멈출 곳」** 중심.

**외부 AI 답변도 출처를 확인하고 쓴다.**
「iOS 앱이 없어졌다」는 Perplexity 답을 그대로 문서에 넣지 않고 공식 도움말과 보도로 확인했다. 결과는 맞았지만, 이 확인 과정이 있어야 「2025-09 폐지」라는 날짜를 문서에 쓸 수 있다.

### Tomorrow's focus — M2 마무리 + M3 시작

1. **Android 폰**에서 앱 방식으로 접속 (10분) → 2개 기기 DoD 충족, iOS 와 조작 차이 기록
2. 실습 3 중 **PIN 오입력 · 인터넷 끊기** 증상 캡처 (10분)
3. M3 — 2단계 인증 확인 · 절전/잠금 설정 · **끊었을 때 집 화면이 잠기는지** (절전·다른 계정 시험을 여기서 같이)
4. 로드맵 환경란 「호스트 = 집 데스크톱」 → 「노트북」으로 정정

## 참조 및 산출물

**신규**: `02-Install-and-First-Connect/` — `README.md` · `guides/install-host-windows.md` · `guides/connect-from-phone.md` · `guides/connect-from-laptop.md` · `examples/first-connect-log.md` · `troubleshooting/cannot-connect.md` · `images/` 10장(마스킹 3)
**참조**: [Chrome 원격 데스크톱 도움말 (iOS)](https://support.google.com/chrome/answer/1649523?hl=ko&co=GENIE.Platform%3DiOS) · [iOS 앱 폐지 보도](https://piunikaweb.com/2025/09/06/chrome-remote-desktop-ios-app-discontinued/) · [로드맵](../vl_roadmap/20260920_RoadMap_Chrome-Remote-Desktop.md)
**비용**: 웹 조회 4회 · 합성 없음
