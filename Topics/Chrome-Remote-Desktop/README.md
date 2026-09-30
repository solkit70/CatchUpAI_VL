# Chrome-Remote-Desktop — 밖에서도 집 컴퓨터로 일하기

> **구글 Chrome Remote Desktop(크롬 리모트 데스크톱)으로 집 컴퓨터를 밖에서 쓰는 방법을, IT 지식이 없는 사람도 그대로 따라 할 수 있게 직접 설치 · 실사용 · 보안 점검까지 해 보고 정리한 Topic.** 두 가지 목적이 있다 — ① 집을 비워도 작업 환경(문서 · 방송 · 영상 제작)을 쓰기, ② 밖에서도 집 컴퓨터의 **AI 작업을 확인하고 다음 지시를 내리기**.

| | |
|---|---|
| 기간 | 2026-09-20 로드맵 → 진행 중 (2주 계획 · ~10/4) |
| 상태 | ✅ **M1 · M2 · M3 · M5 · M6 완료** · 🟡 M4 실사용 기록 3/6 · 🟡 M7 공개 안내 영상 제작 중 |
| 환경 | 집 컴퓨터(호스트): Windows 11 노트북 · 밖에서 쓰는 기기: **iPad 사파리**(iOS 앱은 2025-09 종료 → 웹으로 접속) · Android 는 기기가 없어 **미검증** |
| 대상 | **모든 사람** — 기준선은 「IT 지식이 없는 일반인」 |
| 한 줄 결과 | **집 컴퓨터를 켜 두고 절전만 꺼 두면, 카페에서도 약 5초 만에 들어가 글을 쓰고 저장하고, 원격으로 다시 시작해도 1~2분 뒤 다시 들어갈 수 있다.** 대신 떠나기 전에 반드시 Windows 를 잠근다 |

## 무엇을 알아냈나

- **원리는 TV 리모컨이다.** 일은 집 컴퓨터가 하고, iPad 는 화면을 보며 조종한다. 그래서 집 컴퓨터가 **켜져 있고 인터넷에 연결돼 있어야** 한다. 공유기 설정(포트 열기)은 필요 없다 → [원격 접속이란](01-Concepts-and-Choice/concepts/what-is-remote-access.md) · [공유기 설정이 필요 없는 이유](01-Concepts-and-Choice/concepts/why-no-router-setup.md)
- **설치는 두 번이다.** 「Chrome 에 추가」(브라우저 기능) 다음에 「컴퓨터용 프로그램 설치」가 이어진다. 초보자가 가장 많이 헷갈리는 곳 → [Windows 설치 따라 하기](02-Install-and-First-Connect/guides/install-host-windows.md)
- **비밀번호가 두 개다.** 원격 접속 **PIN**(크롬 리모트 데스크톱에 들어갈 때)과 **Windows 로그인**(잠금 화면을 풀 때)은 다르다. 이 두 겹이 집 컴퓨터를 지킨다 → [iPad · iPhone 연결](02-Install-and-First-Connect/guides/connect-from-iphone.md)
- **화면이 꺼지는 것 ≠ 컴퓨터가 잠드는 것.** 화면 끄기는 괜찮지만 **절전**에 들어가면 밖에서 연결이 안 된다 → [전원 · 잠금 설정](03-Security-Checklist/guides/windows-power-and-lock.md)
- **연결 끊기 ≠ 잠그기.** 연결만 끊으면 집 화면이 열린 채로 남을 수 있다. **먼저 Windows 를 잠그고** 연결을 끊는다 → [보안 점검](03-Security-Checklist/README.md) · [월간 점검표](03-Security-Checklist/examples/monthly-checklist.md)
- **카페에서 실제로 됐다 (2026-09-27).** 카페 Wi-Fi 에서 연결 약 5초(체감), 문서 읽기 · 원격 입력 · 잠금 · 연결 끊기 · 다시 들어가 결과 그대로 확인 → [실측 기록](05-Remote-AI-Review-Loop/examples/loop-session-log.md)
- **원격 재부팅 뒤에도 다시 들어갈 수 있다 (2026-09-30, 두 번 실측).** 원격 화면에서 시작 → 전원 → 다시 시작 → **1~2분 뒤** 잠금 화면으로 다시 연결 → 원격 로그인까지 됐다. 호스트 프로그램이 Windows 와 함께 자동으로 켜지기 때문이다. **예상과 달랐던 점**: 재부팅 중에도 목록에는 컴퓨터가 계속 「Online」으로 보였다 — 표시를 믿지 말고 1~2분 기다렸다가 다시 누른다
- **AI 도구의 원격 기능은 「창문」, 크롬 리모트 데스크톱은 「현관문」.** Claude Code 같은 AI 앱의 원격 기능은 그 앱 안만 보인다. 크롬 리모트 데스크톱은 집 컴퓨터 전체가 보여서, **앱의 원격 기능이 멈췄을 때 들어가 앱을 다시 켜거나 컴퓨터를 다시 시작**할 수 있다 → [도구 비교](06-Alternatives-and-GrokBot/guides/comparison-table.md)
- **Grok Bot 은 다른 종류다.** 내 집 컴퓨터가 아니라 **서비스 회사의 클라우드 컴퓨터**에서 AI 가 일한다. 크롬 리모트 데스크톱으로 그 컴퓨터를 고칠 수는 없다 → [두 가지 종류](06-Alternatives-and-GrokBot/concepts/two-categories.md) · [CRD vs Grok Bot](06-Alternatives-and-GrokBot/guides/crd-vs-grokbot.md)
- **대안(RustDesk)은 설치를 보류했다.** 사양이 낮은 노트북에 CPU · 메모리를 더 쓰는 앱을 늘리지 않기로 했다. 크롬 리모트 데스크톱에 문제가 반복될 때 다시 본다 → [예비 도구](06-Alternatives-and-GrokBot/guides/backup-tool-setup.md) · [CRD 가 안 될 때](06-Alternatives-and-GrokBot/troubleshooting/when-crd-fails.md)

## 모듈 (학습 순서)

| # | 모듈 | 상태 | 핵심 산출물 |
|---|---|---|---|
| 1 | [원격 접속이란 · 무엇을 고를까](01-Concepts-and-Choice/README.md) | ✅ 9/20 | [원격 접속이란](01-Concepts-and-Choice/concepts/what-is-remote-access.md) · [선택 기준](01-Concepts-and-Choice/guides/choice-criteria.md) · [내 구성도](01-Concepts-and-Choice/examples/my-setup-diagram.md) |
| 2 | [설치와 첫 연결](02-Install-and-First-Connect/README.md) | ✅ 9/23 | [Windows 설치](02-Install-and-First-Connect/guides/install-host-windows.md) · [iPad · iPhone 연결](02-Install-and-First-Connect/guides/connect-from-iphone.md) · [다른 노트북에서](02-Install-and-First-Connect/guides/connect-from-laptop.md) · [휴대폰에서](02-Install-and-First-Connect/guides/connect-from-phone.md) · [연결이 안 될 때](02-Install-and-First-Connect/troubleshooting/cannot-connect.md) |
| 3 | [보안 점검](03-Security-Checklist/README.md) | ✅ 9/23 | [무엇이 위험해지나](03-Security-Checklist/concepts/what-gets-risky.md) · [전원 · 잠금](03-Security-Checklist/guides/windows-power-and-lock.md) · [구글 계정 점검](03-Security-Checklist/guides/google-account-checks.md) · [원격 지원 주의](03-Security-Checklist/guides/remote-support-caution.md) · [월간 점검표](03-Security-Checklist/examples/monthly-checklist.md) · [잠겼거나 수상할 때](03-Security-Checklist/troubleshooting/locked-out-or-suspicious.md) |
| 4 | [실사용 ① 집을 비우고 작업하기](04-Real-Use-Work/README.md) | 🟡 3/6 | [작은 화면에서 일하기](04-Real-Use-Work/guides/working-on-small-screen.md) · [실사용 기록](04-Real-Use-Work/examples/real-session-log.md) · [기기 · 회선 표](04-Real-Use-Work/examples/device-network-matrix.md) |
| 5 | [실사용 ② 밖에서 AI 작업 확인하기](05-Remote-AI-Review-Loop/README.md) | ✅ 9/27 | [밖에서 승인하기](05-Remote-AI-Review-Loop/guides/approve-from-phone.md) · [나가기 전에](05-Remote-AI-Review-Loop/guides/before-you-leave.md) · [밖에서 되는 것](05-Remote-AI-Review-Loop/examples/what-works-outside.md) · [카페 실측](05-Remote-AI-Review-Loop/examples/loop-session-log.md) · [입력이 안 될 때](05-Remote-AI-Review-Loop/troubleshooting/typing-and-input.md) |
| 6 | [대안 비교 · Grok Bot](06-Alternatives-and-GrokBot/README.md) | ✅ 9/27 | [도구 비교표](06-Alternatives-and-GrokBot/guides/comparison-table.md) · [두 가지 종류](06-Alternatives-and-GrokBot/concepts/two-categories.md) · [CRD vs Grok Bot](06-Alternatives-and-GrokBot/guides/crd-vs-grokbot.md) |
| 7 | [Capstone — 누구나 따라 하는 안내 영상](07-Public-Guide-Video/README.md) | 🟡 제작 중 | [슬라이드 플랜 v4](07-Public-Guide-Video/examples/slide-plan.md) — 27장 · 약 15~16분 · iPad 기준 · PART 4 「AI 에게 일 시키는 사람에게 더 좋은 이유」 |

> 처음 온 사람이라면 **[Windows 설치 따라 하기](02-Install-and-First-Connect/guides/install-host-windows.md) → [iPad · iPhone 연결](02-Install-and-First-Connect/guides/connect-from-iphone.md) → [전원 · 잠금 설정](03-Security-Checklist/guides/windows-power-and-lock.md)** 세 장이면 시작할 수 있다.

## 따라 하기 한 바퀴

```mermaid
flowchart LR
  A["집 컴퓨터<br/>절전 끄기"] --> B["설치 두 번<br/>Chrome 추가 → 프로그램"]
  B --> C["이름 · PIN"]
  C --> D["iPad 사파리로<br/>연결"]
  D --> E["메모장에 한 줄<br/>쓰고 저장"]
  E --> F["Windows 잠그기"]
  F --> G["연결 끊기"]
  G --> H["다시 들어가<br/>결과 확인"]
```

집에서 이 한 바퀴를 먼저 해 보고, 그다음 실제로 쓸 장소(카페 등)에서 짧게 시험한다.

## 확인 못 한 것

- **Android** — 기기가 없어 앱 방식은 시험하지 않았다
- **M4 실사용** — 휴대폰 데이터(LTE)와 다른 회선 비교 등 3항목이 남았다
- **노트북 덮개를 닫았을 때** — 기기마다 동작이 달라 일반화하지 않았다
- **재부팅 복귀**는 이 노트북에서 두 번 확인한 결과다. Windows 업데이트 설치 중이거나 부팅 전 비밀번호(BitLocker PIN)를 쓰는 컴퓨터는 다를 수 있다
- **RustDesk** 등 대안 도구는 설치하지 않고 공식 자료로만 비교했다

## 기록

- 로드맵: [`vl_roadmap/20260920_RoadMap_Chrome-Remote-Desktop.md`](vl_roadmap/20260920_RoadMap_Chrome-Remote-Desktop.md)
- WorkLog: [`vl_worklog/`](vl_worklog/) — M1(9/20) · M2(9/20 · 9/23) · M3 · M4(9/23) · M5 · M6 · M7(9/27)
- Topic 시작: [`topic_starter.md`](topic_starter.md)
- 방법론: [VibeLearn AI](https://github.com/solkit70/VibeLearn-AI)
