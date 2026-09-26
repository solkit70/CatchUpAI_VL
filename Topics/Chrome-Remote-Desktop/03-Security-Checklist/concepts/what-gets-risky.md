---
title: "원격 접속을 켜면 무엇이 위험해지나"
created: 2026-09-23 05:15:04
module: M3
tags:
  - chrome-remote-desktop
  - security
  - concepts
---

## 먼저 알아둘 것 — 열쇠는 두 개다

Chrome Remote Desktop의 내 기기 접속에는 **Google 계정**과 **호스트 PIN**이라는 두 개의 열쇠가 있다. Google 계정이 첫 번째 문이므로 비밀번호만으로 로그인하게 두지 않고 2단계 인증을 확인해야 하며, PIN은 생일·전화번호처럼 추측하기 쉬운 숫자를 피해야 한다. **Google 계정의 2단계 인증**과 **Chrome Remote Desktop 호스트 PIN**은 서로 다른 단계다. 호스트 PIN을 Google 로그인용 2단계 인증 수단으로 혼동하지 않는다.

> “Using a second step to sign in … makes your Google Account much more secure.”

출처: [Google 계정 도움말 — 2단계 인증으로 개인 정보 보호](https://support.google.com/accounts/answer/10956730?hl=ko)

## 위험 1 — 계정이 뚫리면 첫 번째 문이 열린다

**왜 먼저 보나**: Google 계정에 낯선 기기가 로그인해 있으면 Chrome Remote Desktop뿐 아니라 계정의 다른 정보도 위험할 수 있다. 따라서 2단계 인증 여부, 로그인된 기기, 최근 보안 활동, 복구 정보를 한 묶음으로 확인한다.

기기 목록에는 한 기기에서 만든 여러 세션이 따로 보일 수 있다. 이름만 보고 바로 제거하지 말고, 기기 종류·브라우저·시간·대략적인 위치를 보고 내 활동인지 판단한다. 출처: [Google 계정에 접근한 기기 확인](https://support.google.com/accounts/answer/3067630?hl=ko)

Google 계정의 로그인 기기·보안 활동 화면은 계정 보안을 점검하는 자료다. 그것만으로 개별 Chrome Remote Desktop 접속 기록이 모두 남는다고 단정하지 않는다.

## 위험 2 — 원격 연결을 끊어도 집 화면이 그대로일 수 있다

**왜 확인하나**: 원격 세션 종료와 Windows 잠금은 같은 동작이 아니다. 밖에서 연결을 끊은 뒤 집 노트북이 잠기지 않으면, 그 자리에 있는 사람이 열려 있던 문서나 앱을 볼 수 있다.

확실한 방법은 추측하지 않고 직접 보는 것이다. 2026-09-23 실측에서는 iPad에서 Disconnect한 직후에도 노트북에 메모장 화면이 그대로 남았고 재접속도 됐다. 이는 [M3 WorkLog의 잠금 실측](../../vl_worklog/20260923_M3_Chrome-Remote-Desktop.md#활동-4--ipad-disconnect-직후-잠금-실측)에 기록돼 있다.

## 위험 3 — 항상 접속 가능하게 하다가 화면까지 계속 켜 둔다

**왜 나누나**: 컴퓨터가 절전 상태가 되면 밖에서 접속할 수 없지만, 화면을 계속 켜 둘 필요는 없다. 전원 연결 중에는 **절전은 안 함**, **화면 끄기는 10분**처럼 서로 다른 값으로 설정한다.

화면이 꺼지는 것과 Windows가 실제로 잠기는 것은 별도로 검증한다. 자리를 비울 때는 [Microsoft의 기기 보안 안내](https://support.microsoft.com/en-us/security/securing-your-device)에 나온 수동 잠금 방법을 사용할 수 있다. 이 노트북에서는 iPad에서 Windows를 잠근 뒤 Disconnect해도 잠금이 유지됐고, 재접속 후 Windows PIN으로 해제하는 것까지 [실측했다](../../vl_worklog/20260923_M3_Chrome-Remote-Desktop.md#활동-5--ipad에서-windows-잠금-후-연결-종료재접속).

배터리 사용 중에는 짧은 절전을 유지하는 편이 배터리 보호에 유리하다. 이 노트북의 2026-09-23 현재값은 화면 끄기 3분, 절전 3분이며, 원격 접속을 기다릴 때는 전원 어댑터를 연결해야 한다.

## 이 모듈에서 확인할 세 문장

- Google 계정은 첫 번째 열쇠이고, 호스트 PIN은 두 번째 열쇠다.
- 세션 종료는 컴퓨터 종료도, 자동 잠금도 아니다.
- 원격 접속을 위해 컴퓨터는 깨어 있게 하되 화면은 계속 켜 두지 않는다.

→ 다음: [Google 계정 보안 점검](../guides/google-account-checks.md)
