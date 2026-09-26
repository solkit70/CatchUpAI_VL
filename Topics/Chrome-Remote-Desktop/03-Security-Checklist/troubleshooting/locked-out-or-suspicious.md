---
title: "로그인 실패·낯선 활동이 보일 때"
created: 2026-09-23 11:55:27
module: M3
tags:
  - chrome-remote-desktop
  - security
  - troubleshooting
---

## 먼저 증상을 구분한다

**왜 구분하나**: 원격 접속 실패가 반드시 계정 침입을 뜻하지는 않는다. 내 기기가 오프라인인지, CRD PIN이 틀렸는지, Windows가 잠겨 원격에서 로그인할 수 없는지, Google 계정에 낯선 활동이 있는지를 각각 확인해야 불필요한 계정 변경을 피할 수 있다.

| 보이는 상황 | 먼저 확인할 것 | 다음 조치 |
|---|---|---|
| CRD 기기가 오프라인 | 호스트 전원·인터넷·절전 상태 | 노트북 가까이에서 상태 확인. 밖에서 임의로 전원 설정을 바꾸지 않기 |
| CRD PIN이 틀림 | 계정과 기기 이름이 맞는지, 입력 오타가 없는지 | 올바른 PIN으로 재시도. 실제 PIN은 공유하거나 문서에 적지 않기 |
| Windows 잠금 화면에서 멈춤 | 원격에서 사용 가능한 Windows 로그인 수단 | 노트북 옆에서 먼저 재현·검증. 지문만으로 외부에서 로그인할 수 있다고 가정하지 않기 |
| Google에서 모르는 기기·보안 이벤트 발견 | 세션 세부 정보와 실제 본인 활동 | [Google 공식 계정 보호 절차](https://support.google.com/accounts/answer/6294825?hl=ko)를 따라 확인·보호 |

## 낯선 계정 활동이 있다면

**왜 즉시 확인하나**: Google 계정은 내 기기 원격 접속의 첫 번째 열쇠다. Google은 최근 보안 이벤트에서 본인이 아닌 활동을 표시하고, 기기 목록에서 모르는 기기를 검토한 뒤 안내 절차를 따르도록 설명한다. 출처: [Google — 해킹되거나 도용된 계정 보호](https://support.google.com/accounts/answer/6294825?hl=ko)

1. [Google 계정 보안](https://myaccount.google.com/security)의 최근 보안 활동을 연다.
2. [내 기기](https://google.com/devices)의 세션 세부 정보를 보고, 같은 기기의 여러 세션인지 확인한다. 세션 수 자체를 물리 기기 수나 침입 횟수로 해석하지 않는다. 출처: [Google — 기기 목록 설명](https://support.google.com/accounts/answer/3067630?hl=ko)
3. 본인 활동이 아니라면 Google 화면에서 **내 활동이 아님** 또는 **모르는 기기** 절차를 선택하고 안내에 따라 계정을 보호한다. 계정에 아예 로그인할 수 없으면 [Google 계정 복구](https://accounts.google.com/signin/recovery)를 사용한다.

## 이번 실측에서 확인된 것과 남은 것

2026-09-23에는 잘못된 CRD PIN 뒤 올바른 PIN으로 재접속했고, iPad Wi-Fi 복구 뒤에도 다시 접속했다. Disconnect만 하면 노트북 작업 화면이 그대로 남지만, iPad에서 **Windows Lock → Disconnect**한 뒤에는 잠금이 유지됐다. iPad 재접속 후 **Windows PIN**으로 잠금을 해제해 작업 화면으로 돌아왔으며, 실제 PIN 숫자는 기록하지 않았다. 원래의 오류 화면은 [M2 증상별 점검표](../../02-Install-and-First-Connect/troubleshooting/cannot-connect.md#2026-09-23-추가-실측--pin과-ipad-인터넷)에 요약돼 있다.
