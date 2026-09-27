---
title: "iPhone에서 Chrome Remote Desktop으로 집 컴퓨터에 접속하기"
created: 2026-09-27 00:00:00
author:
  - "Codex"
module: M2
status: "설정 완료 — LTE 접속 실측 대기"
tags:
  - chrome-remote-desktop
  - guides
  - iphone
  - mobile
---

# iPhone에서 Chrome Remote Desktop으로 집 컴퓨터에 접속하기

**걸리는 시간**: 약 10분 · **준비물**: iPhone, 집 컴퓨터에 설정한 같은 Google 계정, Chrome Remote Desktop PIN. 이 문서는 iPhone 전용 안내이며, 실제 iPhone 접속 결과는 아직 기록하지 않았다.

## 현재 실습 상태

2026-09-27 라이브 방송 중 iPhone에서 Safari 설정과 **홈 화면에 추가**까지 마쳤다. LTE·5G 접속, 문서 한 줄 입력·저장, Windows 잠금 후 Disconnect는 방송에서 하지 않기로 했으므로 아직 미실측이다.

## 먼저 알아둘 것

iPhone에서는 App Store 앱이 보이지 않을 수 있다. Google의 현재 안내는 앱이 없을 때 브라우저에서 `remotedesktop.google.com/access`로 이동하라고 한다. Safari에서 홈 화면에 추가하면 주소 표시줄이 사라져 원격 화면을 더 넓게 볼 수 있다.

## 1. Safari에서 원격 화면 열기

1. **Safari**를 연다. Chrome이 아니라 Safari를 쓴다.
2. 주소창에 `remotedesktop.google.com/access`를 입력한다.
3. 집 노트북 호스트에 설정한 것과 **같은 Google 계정**으로 로그인한다.
4. 목록에서 `CatchUpAI_laptop`을 찾는다. 이름 아래에 **온라인**이라고 표시되어야 한다.

기기가 안 보이면 설치 실패로 단정하지 않는다. 가장 먼저 로그인한 Google 계정이 같은지 확인하고, 그다음 집 노트북의 전원·인터넷·절전 상태를 확인한다.

## 2. PIN을 입력해 연결하기

1. `CatchUpAI_laptop`을 탭한다.
2. Chrome Remote Desktop용 PIN을 입력하고 화살표를 탭한다.
3. `Remember my PIN on this device`가 보이면, **개인 iPhone에 잠금 화면이 설정된 경우에만** 선택한다. 다른 사람과 함께 쓰거나 잠금이 없는 기기에서는 선택하지 않는다.

PIN은 방송 화면·채팅·캡처·WorkLog에 적지 않는다. 화면이 뜨면 집 노트북의 실제 데스크톱이 보이는지 먼저 확인한다.

## 3. 홈 화면에 추가하기

1. Safari의 공유 버튼 `□↑`을 탭한다.
2. 메뉴를 아래로 내려 **홈 화면에 추가**를 탭한다.
3. 제안된 이름을 확인하고 **추가**를 탭한다.
4. 이후 홈 화면의 `Remote Desktop` 아이콘으로 열어 쓴다.

공유 메뉴에는 최근 연락처 이름과 사진이 보일 수 있다. 방송이나 문서용으로 화면을 캡처할 때는 그 부분과 계정 이메일·PIN·기기 이름을 반드시 가린다.

## 4. iPhone LTE에서 첫 실측하기

1. iPhone의 **Wi-Fi를 끈다**. LTE·5G만 남아 있어야 집 밖과 비슷한 조건이다.
2. 홈 화면의 `Remote Desktop` 아이콘으로 다시 접속한다.
3. 집 컴퓨터에서 메모장을 열고, 한글 한 줄을 입력한 뒤 저장한다.
4. 접속까지 걸린 시간, 입력 지연, 끊김 횟수를 기록한다.

작은 화면에서는 기본 트랙패드 모드가 정확한 클릭에 유리하다. 세션 메뉴에서 Windows용 터치 입력 모드도 바꿔 볼 수 있으나, 첫 실측에서는 익숙한 모드 하나로 문서 입력·저장을 먼저 끝낸다.

## 5. 안전하게 종료하기

1. 원격 Windows에서 **Lock**을 실행한다.
2. iPhone 화면에서 Windows 잠금 화면이 보이는지 확인한다.
3. 그다음 세션 메뉴에서 **Disconnect**를 선택한다.
4. 가능하면 다시 접속해 Windows PIN을 요구하는지 확인한다.

Disconnect만으로는 Windows가 잠기지 않는 것이 이 Topic의 기존 실측 결과다. 따라서 Lock을 먼저 실행해야 집 노트북의 물리 화면을 보호할 수 있다.

## 문제가 생기면

- 기기 목록이 비어 있음: Google 계정이 다를 가능성이 가장 크다.
- 기기가 어둡거나 오프라인: 집 노트북 전원·인터넷·절전 상태를 확인한다.
- PIN이 기억나지 않음: PIN을 추측해 반복 입력하지 말고, 집 컴퓨터에서 Chrome Remote Desktop 설정을 확인한다.

→ 전체 모바일 안내: [connect-from-phone.md](connect-from-phone.md) · 문제 해결: [../troubleshooting/cannot-connect.md](../troubleshooting/cannot-connect.md) · M3 안전 종료 실측: [../../vl_worklog/20260923_M3_Chrome-Remote-Desktop.md#활동-5--ipad에서-windows-잠금-후-연결-종료재접속](../../vl_worklog/20260923_M3_Chrome-Remote-Desktop.md#활동-5--ipad에서-windows-잠금-후-연결-종료재접속)

## 출처

- [Google Chrome 고객센터 — iPhone 및 iPad에서 Chrome 원격 데스크톱 사용](https://support.google.com/chrome/answer/1649523?hl=ko&co=GENIE.Platform%3DiOS) — 앱이 없을 때 브라우저 접속, PIN 입력, 홈 화면 추가, 입력 모드와 세션 종료 절차
