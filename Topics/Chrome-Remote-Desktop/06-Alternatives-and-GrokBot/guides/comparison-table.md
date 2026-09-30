---
title: "원격 접속 대안 비교표"
created: 2026-09-27 00:00:00
author:
  - "Codex"
tags:
  - chrome-remote-desktop
  - comparison
  - remote-access
---

## 비교의 기준

M1에서 정한 다섯 질문으로 공식 문서만 비교했다. 정책과 요금은 바뀔 수 있으므로, 각 링크를 다시 열어 본 날짜는 **2026-09-27**이다. 이 표는 성능 실측표가 아니다. 실제 설치·접속 전에는 어느 도구도 “내 환경에서 된다”고 쓰지 않는다.

| 도구 | Q1 무료 범위 | Q2 연결 경로·암호화 | Q3 계정·접속 위험 | Q4 만든 곳·법 | Q5 Windows 11 Home 호스트 |
|---|---|---|---|---|---|
| RustDesk | 클라이언트와 자체 서버 OSS는 무료·오픈소스다. [공식](https://rustdesk.com/docs/en/self-host/) | 기본은 공용 서버, 자체 ID·중계 서버로 바꿀 수 있다. 자체 서버는 직접 연결을 먼저 시도하고 실패 시 중계를 쓴다. [공식](https://rustdesk.com/docs/en/self-host/) | 영구 비밀번호·접속 권한은 설정에서 관리한다. 실제 원격 접속은 검증하지 않았다. [공식](https://rustdesk.com/docs/en/client/) | 제작사 소재지·준거법은 이번 공식 기술 문서에서 확인하지 못했다. 추측하지 않는다. | Windows 클라이언트를 제공한다. 잠시 설치했다가 사용자 결정으로 제거했으며, 외부 접속 가능 여부는 검증하지 않았다. [공식](https://rustdesk.com/docs/en/client/) |
| AnyDesk | 개인 용도는 무료이나 기능·지원이 제한된다. 업무 용도는 라이선스가 필요하다. [공식](https://anydesk.com/en/pricing) | 연결 경로·암호화 상세는 이번 가격 문서만으로 확정하지 않는다. | 무료와 업무 용도의 경계를 먼저 확인해야 한다. 업무로 판정될 수 있는 용도에는 백업 카드로 권하지 않는다. [공식](https://anydesk.com/en/pricing) | AnyDesk Software GmbH로 표시된다. 어느 나라 법이 적용되는지는 법적 고지 확인 전 미기록이다. [공식](https://anydesk.com/en/pricing) | 지원 여부를 이 세션에서 실측하지 않았다. |
| TeamViewer | 개인 용도는 무료다. [공식](https://www.teamviewer.com/en/products/remote/get-started/) | 상세 연결 경로는 이번 시작 문서에서 확정하지 않는다. | 개인/비상업 용도 조건을 벗어나면 적합하지 않을 수 있다. [공식](https://www.teamviewer.com/en/products/remote/get-started/) | 국가·준거법은 공식 법적 고지 확인 전 미기록이다. | 지원 여부를 이 세션에서 실측하지 않았다. |
| Windows 원격 데스크톱(RDP) | Windows 기능이지만 Home 호스트에는 쓸 수 없다. [공식](https://learn.microsoft.com/en-us/windows-server/remote/remote-desktop-services/remotepc/remote-desktop-allow-access) | 외부 접속에는 포트 포워딩 또는 VPN이 필요할 수 있다. [공식](https://learn.microsoft.com/en-us/windows-server/remote/remote-desktop-services/remotepc/remote-desktop-allow-access) | 원격 접속 계정에는 강하고 고유한 비밀번호가 필요하며, NLA를 유지하는 것이 권장된다. [공식](https://learn.microsoft.com/en-us/windows-server/remote/remote-desktop-services/remotepc/remote-desktop-allow-access) | Microsoft 제품이다. 데이터·준거법은 별도 계약·정책 확인 대상이다. | **불가** — Windows Home은 호스트가 될 수 없고 클라이언트로만 쓸 수 있다. [공식](https://learn.microsoft.com/en-us/windows-server/remote/remote-desktop-services/remotepc/remote-desktop-allow-access) |
| Parsec | 게임 용도는 무료이나, 업무에는 라이선스가 필요하다. [공식](https://parsec.app/pricing) | 무료 Personal도 암호화된 P2P 연결을 제공한다. [공식](https://parsec.app/pricing) | 업무 용도 무료 사용이 안 되므로 이 Topic의 백업 카드로는 맞지 않는다. [공식](https://parsec.app/pricing) | Unity Technologies로 표시된다. 국가·준거법은 법적 고지 확인 전 미기록이다. [공식](https://parsec.app/pricing) | Windows 10 이상 호스팅을 표기한다. Home 에디션 실측은 하지 않았다. [공식](https://parsec.app/pricing) |
| Tailscale + VNC | Personal은 비상업 개인용으로 무료다. [공식](https://tailscale.com/pricing) | 기기 사이의 안전한 P2P 연결을 제공하지만, 화면을 보여 주는 VNC는 별도로 설치·관리해야 한다. [공식](https://tailscale.com/pricing) | 계정과 기기 승인, 접근 규칙을 별도로 관리해야 한다. VNC 자체의 비밀번호·암호화도 추가로 확인해야 한다. | Tailscale의 국가·준거법은 법적 고지 확인 전 미기록이다. | Tailscale 자체는 가능해도 VNC 호스트의 실측·보안 설정이 별도라서, 즉시 쓸 두 번째 카드로는 복잡하다. |

## 이번 선택

**기능 기준의 후보는 RustDesk였지만, 지금은 추가 설치하지 않는다.** Windows와 iPhone/iPad 지원, 무료 검증 가능성, 자체 서버 선택지는 장점이다. 그러나 사용자는 로컬 문서·영상이 계속 쌓이는 노트북에서 추가 상주 앱의 CPU·메모리·저장 공간과 업데이트 관리 부담을 피하기로 결정했다. RustDesk를 잠시 설치했다가 제거했으며, iPhone 외부 접속·문서 저장은 검증하지 않았다. 따라서 CRD가 막힐 때 바로 쓸 수 있는 두 번째 원격 수단이 확보된 것은 아니다.

AnyDesk·TeamViewer·Parsec는 개인/업무 용도의 경계가 있어, 방송·영상·볼트 작업의 지속적인 백업 수단으로 바로 선택하지 않는다. RDP는 현재 Windows 11 Home 호스트 조건에서 제외된다. Tailscale+VNC는 좋은 네트워크 기반 도구지만, VNC까지 별도 설계해야 하므로 “CRD가 오늘 안 될 때 몇 분 안에 쓰기”라는 목적에는 맞지 않는다.

## 이미 쓰는 AI 작업 도구의 원격 기능

첫 독자 검토에서 사용자는 별도 원격 데스크톱 앱만이 아니라, 이미 VS Code에서 쓰는 Claude와 Codex의 원격 기능도 CRD 장애 시 대안으로 볼 수 있다고 설명했다. 이들은 전체 Windows 화면을 조작하는 CRD와 같은 범주의 대체제가 아니다. 실행 중이거나 지원되는 AI 코딩 작업에 원격으로 이어서 지시·검토하는 보완 경로다.

| 도구 | 공식 문서상 원격 기능 | 이 환경에서의 의미와 한계 |
|---|---|---|
| Claude Code Remote Control | 로컬 Claude Code 세션을 휴대폰 또는 웹에서 이어서 제어할 수 있다. 기능 제공 여부는 요금제·CLI 버전·조직 정책에 좌우된다. [Anthropic 공식 안내](https://support.claude.com/en/articles/14554000-claude-code-power-user-tips) | 이미 사용 중인 Claude 작업에 이어서 접근할 수 있는 후보. 전체 Windows 앱·파일을 제어하는 범용 원격 데스크톱은 아니다. 실제 계정과 세션에서 사용 가능한지는 별도 확인하지 않았다. |
| Codex Remote | ChatGPT 모바일의 Remote 탭에서 지원되는 데스크톱 Codex 대화를 열 수 있고, 로컬 프로젝트는 호스트 PC에서 실행된다. 지원되는 Windows Codex 앱의 원격 제어·Computer Use 기능은 앱·권한·계정 설정에 따라 달라진다. [OpenAI 공식 안내](https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex) · [Windows 및 요금제 안내](https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan) | 이미 사용 중인 Codex 작업의 원격 지시·검토 후보. 사용자는 VS Code에서 Codex를 쓴다고 했으나, 그 IDE 세션이 모바일 Remote 대상으로 지원되는지는 이 비교로 확정하지 않는다. CRD처럼 임의의 Windows 화면을 모두 조작한다고 보아서는 안 된다. |

따라서 사용자의 선택은 “CRD가 고장 나면 Claude/Codex가 모든 화면 작업을 대신한다”가 아니라, 가벼운 CRD를 주 원격 화면 경로로 두고, 이미 사용 중인 AI 도구의 지원되는 작업은 상황에 따라 보완적으로 활용하며, RustDesk 설치는 자원 여유와 실제 필요가 확인될 때 재검토한다는 것이다. 노트북 사양이 제한적이고 CPU·메모리·저장 공간이 가장 큰 고려사항이므로, 추가 상주 앱을 설치하지 않는 판단을 유지한다.

다시 검토할 조건은 CRD 문제가 반복되고 전원·인터넷·Google 계정·PIN·호스트 상태 확인으로 해결되지 않거나, 기존 Claude/Codex 원격 기능이 필요한 작업을 지원하지 않는 경우다. 이때 먼저 디스크 여유와 백그라운드 리소스 사용량을 확인하고, 그 뒤 RustDesk 설치 여부를 결정한다.
