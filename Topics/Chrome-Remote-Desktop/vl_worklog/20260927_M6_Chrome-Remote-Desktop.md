---
title: "M6 WorkLog — 대안 비교와 Grok Bot 조사"
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
| 모듈 | M6 — 대안 비교 · 무료·안전한 두 번째 카드와 Grok Bot |
| 상태 | 🟡 진행 중 — 방송 중 조사·후보 선정 완료, 실제 설치는 보류 |

## 오늘의 학습 목표

- [x] 여섯 대안을 같은 기준으로 공식 자료에서 비교한다.
- [x] 실제 설치 후보를 하나 정하고, 선택 이유와 설치 전 경계를 기록한다.
- [x] CRD와 Grok Bot이 다른 범주임을 공식 자료로 정리한다.
- [ ] RustDesk를 Windows와 iPhone/iPad에 설치하고 외부 접속·문서 저장을 실측한다.

## 진행 내용

### 활동 1 — 공식 자료 비교

RustDesk, AnyDesk, TeamViewer, Windows RDP, Parsec, Tailscale+VNC를 M1의 다섯 기준으로 다시 확인했다. 무료라는 말만으로 고르지 않았다. Windows 11 Home에서는 RDP 호스트가 불가능하고, AnyDesk·TeamViewer·Parsec에는 개인/업무 용도 경계가 있다. 자세한 표는 [comparison-table.md](../06-Alternatives-and-GrokBot/guides/comparison-table.md)에 기록했다.

### 활동 2 — 두 번째 카드 선정

RustDesk를 후보로 정했다. 공식 문서는 Windows와 iPhone/iPad 클라이언트를 지원하고, 공용 서버 또는 자체 ID·중계 서버를 선택할 수 있다고 안내한다. 이번에는 공용 서버로 설치·접속부터 검증한다. 자체 서버는 보안·운영 범위를 넓히므로 보류한다.

### 활동 3 — Grok Bot 경계 정리

Grok Bot은 내 집 PC의 원격 화면 도구가 아니라 지속형 클라우드 컴퓨터에서 AI가 일하는 방식이다. 집 PC가 꺼져도 작업이 계속될 수 있지만, 클라우드 컴퓨터의 파일·브라우저 로그인 공유 범위는 별도로 관리해야 한다. [two-categories.md](../06-Alternatives-and-GrokBot/concepts/two-categories.md)와 [crd-vs-grokbot.md](../06-Alternatives-and-GrokBot/guides/crd-vs-grokbot.md)에 정리했다.

### 활동 4 — iPad 검증 상태와 iPhone 설치 안내

사용자는 RustDesk를 iPad에 설치하고 테스트까지 마쳤으며, iPhone에는 아직 설치하지 않았다고 보고했다. 테스트의 회선·접속 시간·문서 저장·종료 절차는 아직 받지 않았으므로 완료로 추정하지 않는다. iPhone용 App Store 설치와 첫 연결·안전 종료 절차를 [backup-tool-setup.md](../06-Alternatives-and-GrokBot/guides/backup-tool-setup.md#iphone에-rustdesk-설치하기)에 추가했다.

## DoD 체크리스트

- [x] 비교표 6도구 × 5기준, 확인한 사실에 공식 출처 첨부
- [ ] 대안 1개 실제 설치·접속 성공, 문서 편집·저장까지
- [x] Grok Bot 비교와 내 경우의 판단 작성
- [x] CRD 장애 시 전환 순서 초안 작성
- [ ] README·링크·WorkLog·Retrospective 최종 점검
- [ ] 따라 하기 검증 — 설치 가이드를 처음 보는 사람이 따라 할 수 있는가

**완료율**: 3/6. 설치와 외부 접속을 아직 실측하지 않았으므로 M6 완료가 아니다.

## Daily Retrospective

### What went well

- 방송 중에는 정책·공식 문서 조사와 선택 근거만 다뤄, 기기 설치나 비밀값 입력을 요구하지 않았다.
- “무료”와 “개인 용도 무료”를 구분했고, Windows 11 Home에서 RDP 호스트가 불가능한 점을 다시 확인했다.

### What could be improved

- 국가·준거법, 일부 상용 도구의 상세 연결 경로는 이번 공식 문서 범위에서 확인하지 못했다. 빈칸을 추측으로 채우지 않았다.

### Tomorrow's focus

- 방송 후 RustDesk를 Windows와 iPhone/iPad에 설치하고, 외부 회선으로 접속해 문서 한 줄 저장·Windows 잠금·Disconnect까지 실측한다.
- 결과를 CRD M4 기록과 비교하고 README 링크를 점검한다.

## 참조 및 산출물

- [RustDesk 클라이언트](https://rustdesk.com/docs/en/client/)
- [RustDesk 자체 서버](https://rustdesk.com/docs/en/self-host/)
- [Microsoft Remote Desktop](https://learn.microsoft.com/en-us/windows-server/remote/remote-desktop-services/remotepc/remote-desktop-allow-access)
- [Tailscale 요금제](https://tailscale.com/pricing)
- [Parsec 요금제](https://parsec.app/pricing)
- [AnyDesk 요금제](https://anydesk.com/en/pricing)
- [TeamViewer 시작](https://www.teamviewer.com/en/products/remote/get-started/)
- [Grok Bot 개요](https://docs.x.ai/grok-bot/overview)
