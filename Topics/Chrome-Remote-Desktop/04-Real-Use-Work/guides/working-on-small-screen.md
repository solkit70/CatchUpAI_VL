---
title: "iPhone에서 Chrome Remote Desktop으로 작은 화면 작업하기"
created: 2026-09-23 14:18:07
module: M4
tags:
  - chrome-remote-desktop
  - iphone
  - remote-work
---

## 시작 전에

**왜 확인하나**: iPhone에서 집 노트북을 찾으려면 노트북이 켜져 있고 인터넷에 연결돼 있어야 한다. 노트북은 전원에 연결하고 Chrome Remote Desktop에서 온라인으로 표시되는지 확인한다. 덮개 동작은 아직 실측하지 않았으므로 접속을 기다리는 동안 덮개를 닫아 절전에 들어간다고 가정하지 않는다.

iPhone에서는 설치 없이 Safari의 웹 경로를 이용할 수 있다. Google의 [iPhone·iPad 공식 안내](https://support.google.com/chrome/answer/1649523?co=GENIE.Platform%3DiOS&hl=en-AO)는 앱과 함께 브라우저에서 `remotedesktop.google.com/access`를 여는 방법도 제시한다. 이 실습은 이미 iPad에서 사용한 웹 접속 방식을 iPhone에 적용한다.

## iPhone에서 첫 접속

**왜 계정을 확인하나**: 집 노트북은 특정 Google 계정에 등록돼 있으므로 다른 계정으로 로그인하면 목록에 보이지 않을 수 있다.

1. iPhone에서 Safari를 열고 [remotedesktop.google.com/access](https://remotedesktop.google.com/access)에 접속한다. 처음이라면 iPad에서 쓰던 **같은 Google 계정**으로 로그인한다. 2단계 인증 요청이 나오면 본인이 직접 완료하고 인증 코드를 문서나 채팅에 보내지 않는다.
2. **Remote access / 원격 액세스**에서 집 노트북을 선택한다. 목록에 없으면 먼저 Google 계정이 같은지 확인하고, 흐리게 표시되면 노트북이 온라인인지 확인한다.
3. **Chrome Remote Desktop 호스트 PIN**을 입력한다. 이 PIN은 Google 계정의 2단계 인증이나 Windows 로그인 PIN과 다른 단계다.
4. Windows 잠금 화면이 나타나면 **Windows PIN**으로 잠금을 해제한다. PIN 숫자는 캡처·WorkLog에 남기지 않는다.

Google의 [원격 접속 절차](https://support.google.com/chrome/answer/1649523?co=GENIE.Platform%3DiOS&hl=en-AO)는 기기 선택 뒤 호스트 PIN을 입력하며, 연결 후 가상 트랙패드로 컴퓨터를 조작한다고 안내한다.

## 작은 화면에서 조작·검증

**왜 작은 테스트부터 하나**: iPhone에서는 집 모니터의 글씨와 버튼이 작아 잘못 누르기 쉽다. 개인정보가 없는 테스트 문서로 먼저 입력과 저장을 확인한다.

1. 기본 트랙패드 모드에서 화면을 쓸어 포인터를 움직이고, 한 번 탭해 클릭한다. 두 손가락 탭은 오른쪽 클릭, 핀치 동작은 확대·축소다. 필요하면 화면 가장자리의 화살표로 세션 메뉴를 열어 **Input controls / 입력 제어**에서 터치 방식을 바꾼다. 출처: [Google iPhone·iPad 조작 안내](https://support.google.com/chrome/answer/1649523?co=GENIE.Platform%3DiOS&hl=en-AO)
2. 메모장이나 개인정보가 없는 볼트 테스트 문서에 짧은 한글 한 줄을 입력하고 저장한다. 문서를 다시 열어 내용이 남아 있는지 확인한다.
3. 접속까지 걸린 시간, 한글 입력 지연, 끊김 횟수, 글씨·버튼 조작의 불편을 기록한다. iPad와 비교하려면 **같은 한 줄 입력·저장 작업**을 사용한다.

Safari의 공유 메뉴에서 **홈 화면에 추가**를 선택하면 주소창이 없는 웹앱 형태로 열 수 있다. 첫 접속에는 필수가 아니며, Google도 모바일 브라우저 접속 뒤 홈 화면 추가를 안내한다. 출처: [Google iPhone·iPad 공식 도움말](https://support.google.com/chrome/answer/1649523?co=GENIE.Platform%3DiOS&hl=en-AO)

## 끝낼 때

**왜 먼저 잠그나**: 이 노트북에서는 Disconnect만 하면 Windows 작업 화면이 그대로 남았다. 따라서 M3에서 실측한 **Windows Lock → 잠금 화면 확인 → Disconnect** 순서를 사용한다. 재접속하면 Windows 잠금 화면과 PIN 요구가 나오는지 확인하되, 검증을 위해 다시 잠금을 풀었다면 실습을 마칠 때 다시 잠근다.

Google은 모바일에서 앱·탭을 닫거나 메뉴의 Disconnect로 원격 세션을 끝낼 수 있다고 설명한다. 다만 이것이 Windows 잠금을 실행한다는 뜻은 아니다. 출처: [Google 원격 세션 종료 안내](https://support.google.com/chrome/answer/1649523?co=GENIE.Platform%3DiOS&hl=en-AO) · [M3 실측](../../03-Security-Checklist/guides/windows-power-and-lock.md#4-실측-완료--ipad에서-먼저-잠그고-연결-종료)

→ [기기·회선 실측표](../examples/device-network-matrix.md) · [M4 WorkLog](../../vl_worklog/20260923_M4_Chrome-Remote-Desktop.md)
