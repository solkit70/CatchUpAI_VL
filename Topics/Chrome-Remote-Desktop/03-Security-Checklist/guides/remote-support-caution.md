---
title: "원격 지원 코드 공유 시 주의사항"
created: 2026-09-23 11:55:27
module: M3
tags:
  - chrome-remote-desktop
  - security
  - guide
---

## 왜 내 기기 접속과 구분하나

**내 기기 접속**은 본인이 등록한 컴퓨터에 Google 계정과 호스트 PIN으로 들어가는 방식이다. **원격 지원**은 화면을 공유하는 쪽이 일회성 코드를 만들고 접속자를 승인하는 별도 방식이다. 내가 다른 사람의 컴퓨터에 접속할 수도, 다른 사람이 내 컴퓨터에 접속하도록 허용할 수도 있다. 평소 내 기기에 접속하려고 지원 코드를 만들 필요는 없다. 출처: [Google Chrome Remote Desktop 도움말](https://support.google.com/chrome/answer/1649523?co=GENIE.Platform%3DDesktop&hl=en)

## 지원을 받을 때의 안전 순서

**왜 조심하나**: 지원을 승인하면 상대가 앱·파일·이메일·브라우저 기록을 볼 수 있는 수준의 접근을 받는다. 따라서 모르는 사람이나 신원을 확인하지 못한 상대에게 코드를 전달하지 않는다. 출처: [Google — 컴퓨터 공유 절차](https://support.google.com/chrome/answer/1649523?co=GENIE.Platform%3DDesktop&hl=en)

1. 정말 도움을 받아야 하는 상황인지, 상대가 신뢰할 수 있는 사람인지 먼저 확인한다.
2. 공유 전 민감한 문서와 알림을 닫고, `remotedesktop.google.com/support`에서 **지원받기** 절차를 시작한다.
3. 생성된 코드는 의도한 상대에게만 전달한다. 코드나 승인 화면을 공개 캡처·WorkLog에 남기지 않는다.
4. 상대가 코드를 입력하면 표시되는 이메일을 확인한 다음, 맞을 때만 **공유**를 누른다.
5. 끝나면 **공유 중지(Stop Sharing)**를 누르고 지원 세션이 종료됐는지 확인한다.

Google은 지원 코드가 한 번만 작동하고, 공유가 계속되면 주기적으로 확인을 요청한다고 설명한다. 그러나 일회성이라는 이유로 낯선 상대에게 코드를 보내도 안전해지는 것은 아니다. 출처: [Google 공식 안내](https://support.google.com/chrome/answer/1649523?co=GENIE.Platform%3DDesktop&hl=en)

## 이 Topic의 확인 범위

원격 지원 코드를 실제로 생성하거나 타인에게 공유하는 실습은 하지 않았다. 이 문서는 공식 절차와 위험을 구분해 설명한 것이며, 내 기기 접속의 실측 결과는 [Windows 전원과 잠금](windows-power-and-lock.md)에 따로 기록한다.
