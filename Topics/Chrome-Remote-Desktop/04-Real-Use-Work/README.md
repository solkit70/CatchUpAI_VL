---
title: "M4 — 집 밖에서 원격 작업하기"
created: 2026-09-23 14:13:42
module: M4
tags:
  - chrome-remote-desktop
  - remote-work
  - readme
---

## M4 — 실사용 ① 집을 비우고 작업하기

> 연결되는지 확인하는 데서 그치지 않고, 집 밖에서 실제 작업을 끝내고 결과를 검증한다.

**상태**: 🟡 진행 중 · **예상 학습 시간**: 2시간. 2026-09-23 스타벅스에서 iPad·매장 Wi-Fi로 첫 외부 작업을 약 20분간 진행했다. 문서 편집 내용이 남아 있음을 확인했고, 연결은 10초 미만으로 추정되며 끊김은 없었다. 재접속 시 Windows 잠금 화면과 PIN 요구를 확인했으며, iPhone 접속과 회선·기기 비교가 남아 있다.

## 학습 순서

1. [examples/real-session-log.md](examples/real-session-log.md) — 실제 외부 세션에서 완료한 일과 아직 확인하지 않은 일을 구분한다.
2. [examples/device-network-matrix.md](examples/device-network-matrix.md) — M2 기준선과 M4 외부 Wi-Fi 결과를 기기·회선별로 비교한다.
3. [guides/working-on-small-screen.md](guides/working-on-small-screen.md) — iPhone에서 첫 접속과 작은 화면 조작을 따라 한다.

느릴 때의 문제 해결 문서는 실습 결과를 더 확인한 뒤 작성한다. 아직 없는 문서로 연결되는 링크는 만들지 않는다.

## 현재 확인된 결과

| 항목 | 결과 |
|---|---|
| 외부 장소·기기·회선 | 스타벅스 · iPad · 매장 Wi-Fi |
| 실제 작업 | 문서 편집·내용 유지 확인, 테스트 폴더 정리, OBS 실행·상태 확인 |
| 원격 작업 관리자 | 열어 확인함 · 프로세스 종료는 미실측 |
| 접속·입력 품질 | 접속 10초 미만 추정 · 끊김 0회 · 한글 입력 지연 크게 느끼지 못함 |
| 안전 종료 | Windows Lock → 잠금 확인 → Disconnect 적용 · 재접속 시 Windows 잠금 화면과 PIN 요구 확인 |

## 이동

이전: [M3 — 보안 점검](../03-Security-Checklist/README.md). M3에서 확인한 안전 종료 순서를 그대로 적용한다. [M4 WorkLog](../vl_worklog/20260923_M4_Chrome-Remote-Desktop.md)에 실습 근거와 미확인 항목을 기록한다.
