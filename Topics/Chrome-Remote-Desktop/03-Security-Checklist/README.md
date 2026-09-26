---
title: "M3 — 보안 점검"
created: 2026-09-23 05:15:04
module: M3
tags:
  - chrome-remote-desktop
  - security
  - readme
---

## M3 — 보안 점검 · 편해진 만큼 열린 문 닫기

> 원격 접속을 켜 두는 이유와 위험을 함께 이해하고, 계정·화면·전원 상태를 실제로 확인한다.

**상태**: ✅ 완료 (2026-09-23 · DoD 6/6) · **예상 학습 시간**: 2시간. Disconnect만으로는 잠기지 않지만 Windows Lock → Disconnect 뒤에는 잠금이 유지되고 원격 Windows PIN 해제가 되는 것을 확인했다. 계정 점검, 월간 반복 일정, 사용자 따라 하기 검증과 Module Retrospective까지 마쳤다.

## 학습 순서

1. [concepts/what-gets-risky.md](concepts/what-gets-risky.md) — 원격 접속을 켜면 새로 생기는 위험과 두 개의 열쇠를 이해한다
2. [guides/google-account-checks.md](guides/google-account-checks.md) — 2단계 인증, 로그인 기기, 최근 보안 활동, 복구 정보를 점검한다
3. [guides/windows-power-and-lock.md](guides/windows-power-and-lock.md) — 컴퓨터는 깨어 있게 두고 화면은 보호하도록 전원과 잠금을 확인한다
4. [guides/remote-support-caution.md](guides/remote-support-caution.md) — 일회성 지원 코드와 내 기기 접속의 위험을 구분한다
5. [examples/monthly-checklist.md](examples/monthly-checklist.md) — 개인정보를 남기지 않고 매달 상태를 점검한다
6. [troubleshooting/locked-out-or-suspicious.md](troubleshooting/locked-out-or-suspicious.md) — 로그인 실패·낯선 계정 활동이 보일 때 확인 순서를 따른다

## 현재 상태

| 항목 | 상태 |
|---|---|
| Chrome Remote Desktop 서비스 | ✅ 실행 중 · 자동 시작 |
| 전원 연결 시 절전 | ✅ 안 함 |
| 전원 연결 시 화면 끄기 | ✅ 10분 |
| 로그인 요구 | ✅ Every Time 표시 · 지문 로그인 정상 |
| 원격 세션 종료 후 잠금 | ✅ Disconnect만 하면 작업 화면 그대로. Windows Lock → Disconnect 뒤 잠금 유지 · 재접속 후 Windows PIN 해제 정상 |
| Google 계정 보안 4항목 | ✅ 2단계 인증 켜짐 · 최근 활동과 Mac 포함 기기 목록은 사용자 판단상 이상 없음 · 복구 이메일·전화 사용 가능 및 확인 완료 |
| 월간 점검 | ✅ 점검표 작성 · 기본 Google Calendar 매월 1일 10:00–10:20 (시애틀 시간), 2026-10-01 시작 |

## 이동

이전: [M2 — 설치와 첫 연결](../02-Install-and-First-Connect/README.md)

다음 M4는 아직 시작하지 않았다. 외출 중에도 검증된 **Windows Lock → Disconnect** 순서로 종료한다. Disconnect만으로 노트북이 잠긴다고 가정하지 않는다.
