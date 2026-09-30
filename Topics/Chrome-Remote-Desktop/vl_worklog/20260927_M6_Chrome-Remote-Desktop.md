---
title: "M6 WorkLog — 대안 비교와 추가 설치 보류"
created: 2026-09-27 00:00:00
author:
  - "Codex"
topic: "Chrome-Remote-Desktop"
module: "M6"
tags:
  - vibelearn-ai
  - worklog
  - chrome-remote-desktop
---

## 세션 개요

| 항목 | 값 |
|---|---|
| 날짜 | 2026-09-27 |
| 모듈 | M6 — 대안 비교 · 추가 설치 판단과 Grok Bot |
| 상태 | ✅ 완료 — 첫 독자 검증까지 완료 |

## 오늘의 학습 목표

- [x] 여섯 대안을 같은 기준으로 공식 자료에서 비교한다.
- [x] 후보를 하나 정하고, 추가 설치를 하지 않는 이유와 재검토 조건을 기록한다.
- [x] CRD와 Grok Bot이 다른 범주임을 공식 자료로 정리한다.
- [x] 앞서 설치한 Windows RustDesk의 서비스·프로세스·설치 항목을 제거한다.
- [x] 설치 없는 CRD 장애 점검 순서를 문서화한다.

## 진행 내용

### 활동 1 — 공식 자료 비교

RustDesk, AnyDesk, TeamViewer, Windows RDP, Parsec, Tailscale+VNC를 M1의 다섯 기준으로 다시 확인했다. 무료라는 말만으로 고르지 않았다. Windows 11 Home에서는 RDP 호스트가 불가능하고, AnyDesk·TeamViewer·Parsec에는 개인/업무 용도 경계가 있다. 자세한 표는 [comparison-table.md](../06-Alternatives-and-GrokBot/guides/comparison-table.md)에 기록했다.

### 활동 2 — 두 번째 카드 선정

RustDesk를 기능 기준의 후보로 정했다. 공식 문서는 Windows와 iPhone/iPad 클라이언트를 지원하고, 공용 서버 또는 자체 ID·중계 서버를 선택할 수 있다고 안내한다. 그러나 사용자 결정으로 이번에는 추가 도구를 설치하지 않는다. 기능상의 후보와 실제로 쓸 수 있는 백업 수단을 구분한다.

### 활동 3 — Grok Bot 경계 정리

Grok Bot은 내 집 PC의 원격 화면 도구가 아니라 지속형 클라우드 컴퓨터에서 AI가 일하는 방식이다. 집 PC가 꺼져도 작업이 계속될 수 있지만, 클라우드 컴퓨터의 파일·브라우저 로그인 공유 범위는 별도로 관리해야 한다. [two-categories.md](../06-Alternatives-and-GrokBot/concepts/two-categories.md)와 [crd-vs-grokbot.md](../06-Alternatives-and-GrokBot/guides/crd-vs-grokbot.md)에 정리했다.

### 활동 4 — iPad 사용 보고와 검증 범위

사용자는 RustDesk를 iPad에 설치하고 테스트까지 마쳤으며, iPhone에는 설치하지 않았다고 보고했다. 테스트의 회선·접속 시간·문서 저장·종료 절차는 아직 받지 않았으므로 이 Topic의 외부 접속 실측으로 계산하지 않는다. 앞서 작성한 iPhone 설치 안내는 9/27 사용자 결정에 따라 [설치 보류 기록](../06-Alternatives-and-GrokBot/guides/backup-tool-setup.md)으로 고쳤다.

### 활동 5 — Windows 호스트 설치

2026-09-27 14:39 PDT에 RustDesk 공식 GitHub 릴리스 1.4.9의 Windows x86-64 실행 파일을 다운로드했다. Authenticode 서명이 유효하며 서명자는 PURSLANE, SHA-256은 `EAEDEB0088E687BF46F7C46A9C6EA5493CE51F3134DFD6ACBEDB47B5B9136274`였다. 공식 문서의 `--silent-install`로 설치한 뒤 `C:\Program Files\RustDesk\RustDesk.exe` 버전 1.4.9+67, Windows RustDesk 서비스 `RUNNING`, `--get-id` 명령의 9자리 ID 반환을 확인했다. ID 자체와 일회성 비밀번호는 기록하지 않았다. 이 확인은 호스트 설치와 준비 상태만 뜻하며, iPhone에서 실제로 접속됐다는 근거는 아니다. 출처: [RustDesk 공식 클라이언트 설치 안내](https://rustdesk.com/docs/en/client/) · [공식 1.4.9 릴리스](https://github.com/rustdesk/rustdesk/releases/tag/1.4.9).

설치 도중 iPhone CRD 실습 화면에 Windows UAC가 나타났다. 사용자가 제공한 [사진](../02-Install-and-First-Connect/images/005_iPhone_test_Windows_UAC_Command_Processor.jpg)의 촬영 시각은 14:39:23이고, Windows System 로그의 RustDesk 서비스 등록은 14:39:56~58이다. 사진에는 요청 프로그램 `Windows Command Processor`, 게시자 `Microsoft Windows`가 표시된다. 설치 명령과 사진·서비스 등록 시각이 겹쳐 **RustDesk 설치 과정의 권한 요청으로 추정**한다. 부모 프로세스는 확인하지 못했으므로 단정하지 않으며, CRD의 일반적인 한글 입력 단계로 안내하지 않는다.

### 활동 6 — 사용자 결정과 Windows 설치 제거

사용자는 로컬 문서·영상이 계속 쌓이는 노트북에 원격 앱을 더 설치하면 CPU·메모리와 저장 공간 부담이 늘 수 있으므로, **RustDesk는 설치하지 않고 비교 분석 문서만 남기겠다**고 결정했다. 앞선 설치는 Codex가 진행했음을 사용자에게 알리고 Windows의 등록된 `--uninstall` 명령으로 제거했다. 15:06 PDT 확인에서 RustDesk 서비스·프로세스·`C:\Program Files\RustDesk\RustDesk.exe`·Windows 설치 목록 항목은 모두 없었다. iPhone 앱은 설치하지 않았고 원격 접속 성공을 주장하지 않는다.

제거 프로그램이 `%LOCALAPPDATA%\rustdesk` 약 78MB, `%APPDATA%\RustDesk` 약 0.07MB, `%TEMP%\rustdesk-1.4.9-x86_64.exe` 약 24MB를 남겼다. 해당 폴더는 모두 이번 설치 시각에 생성된 것을 확인했으나, `Remove-Item`을 이용한 정리는 자동 승인 검토에서 `blocked by policy`로 거부됐다. 실행 프로그램과 서비스는 제거됐지만 저장 공간 약 102MB는 아직 회수되지 않았다. 자세한 경로는 [설치 보류 결정](../06-Alternatives-and-GrokBot/guides/backup-tool-setup.md#설치와-제거-기록)에 기록했다.

## DoD 체크리스트

- [x] 비교표 6도구 × 5기준, 확인한 사실에 공식 출처 첨부
- [x] 추가 설치 보류 이유와 재검토 조건 기록 — CPU·메모리·저장 공간, 업데이트 관리 부담
- [x] Grok Bot 비교와 내 경우의 판단 작성
- [x] CRD 장애 시 새 앱 설치 없이 확인할 순서 작성
- [x] README·링크·WorkLog·Retrospective 최종 점검 — 상대 링크 144개 정상, M6 폴더 빈 폴더 없음
- [x] 따라 하기 검증 — 사용자가 Claude/Codex 원격 기능은 지원되는 AI 작업의 보완 경로, CRD는 전체 화면 원격 제어, RustDesk는 CRD 문제가 반복되고 리소스 여유가 확인될 때 재검토하는 선택지라고 확인했다.

### 첫 독자 피드백 — AI 도구의 원격 기능과 자원 기준

사용자는 비교표를 무료 원격 제어 도구 중심으로 조사했고, 무료이며 기능상 충분했던 CRD를 선택했다고 설명했다. Grok Bot은 유료이고, 이미 VS Code에서 Claude와 Codex를 사용해 AI Agent 기능은 충족한다고 판단해 선택하지 않았다. RustDesk는 사양이 낮은 노트북에서 CPU·메모리·저장 공간을 더 쓰는 앱을 늘리지 않으려 보류했으며, 기존 Claude/Codex의 원격 기능도 필요 시 보완 선택지가 될 수 있다고 덧붙였다. 원문은 [[Journal/2026-09-27#Chrome Remote Desktop 대안 선택 기준과 리소스 고민 (구술 원문)|9/27 Journal]]에 보존했다.

이 피드백으로 확인된 판단을 비교표에 반영했다. AI 코딩 세션에 접근하는 기능과 전체 Windows 화면에 접속하는 CRD는 용도가 다르며, 현재 사용 중인 VS Code 세션에서 Claude/Codex 원격 기능이 실제로 지원되는지는 확인되지 않았다고 명시했다. CRD 장애 때 어떤 종류의 작업을 기존 AI 원격 기능으로 이어갈 수 있고, 어떤 경우에는 RustDesk 재검토가 필요한지 짧게 확인한 뒤 따라 하기 검증을 마친다.

**완료율**: 6/6 — 2026-09-27. 첫 독자 피드백을 반영해 AI 도구 원격 기능 범위를 표에 추가했고, 사용자가 보완된 구분을 확인했다. RustDesk 외부 접속은 이번 범위에서 제외했다.

## Daily Retrospective

### What went well

- 방송 중에는 정책·공식 문서 조사와 선택 근거만 다뤄, 기기 설치나 비밀값 입력을 요구하지 않았다.
- “무료”와 “개인 용도 무료”를 구분했고, Windows 11 Home에서 RDP 호스트가 불가능한 점을 다시 확인했다.

### What could be improved

- 국가·준거법, 일부 상용 도구의 상세 연결 경로는 이번 공식 문서 범위에서 확인하지 못했다. 빈칸을 추측으로 채우지 않았다.
- Codex가 사용자에게 설치 필요 여부를 재확인하기 전에 Windows RustDesk를 설치했다. 설치가 iPhone CRD 실습 중 권한 확인창을 띄웠을 가능성도 있다. 다음에는 추가 상주 앱이 실제로 필요한지 사용자 선호와 로컬 자원 조건을 먼저 확인한다.

### 다음 순서

- M6 DoD 6/6을 마쳤다. 다음 순서는 M7 안내 영상의 12~18장 슬라이드 플랜 리뷰다. M5의 집 밖 실측은 사용자가 원한 대로 다음 외출 기회로 미룬다.
- 저장 공간 정리가 필요하면 남은 RustDesk 사용자 폴더와 임시 설치 파일을 사용자가 직접 확인한다.

## 참조 및 산출물

- [RustDesk 클라이언트](https://rustdesk.com/docs/en/client/)
- [RustDesk 자체 서버](https://rustdesk.com/docs/en/self-host/)
- [Microsoft Remote Desktop](https://learn.microsoft.com/en-us/windows-server/remote/remote-desktop-services/remotepc/remote-desktop-allow-access)
- [Tailscale 요금제](https://tailscale.com/pricing)
- [Parsec 요금제](https://parsec.app/pricing)
- [AnyDesk 요금제](https://anydesk.com/en/pricing)
- [TeamViewer 시작](https://www.teamviewer.com/en/products/remote/get-started/)
- [Grok Bot 개요](https://docs.x.ai/grok-bot/overview)
