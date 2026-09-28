---
title: "원격 접속 대안 설치 보류 결정"
created: 2026-09-27 00:00:00
author:
  - "Codex"
tags:
  - chrome-remote-desktop
  - rustdesk
  - decision
---

## 이번 결정

2026-09-27 사용자는 RustDesk를 추가로 설치하지 않고 [대안 비교표](comparison-table.md)와 [Grok Bot 비교](crd-vs-grokbot.md)만 남기기로 결정했다. 로컬에 문서와 영상이 계속 쌓이고 있어, 별도 앱의 CPU·메모리·저장 공간·업데이트 관리 부담을 늘리고 싶지 않다는 이유다. 현재 실측한 원격 화면 도구는 Chrome Remote Desktop(CRD)이며, RustDesk의 iPhone 외부 접속·문서 저장은 검증하지 않았다.

## 설치와 제거 기록

같은 날 앞선 작업에서 Codex가 RustDesk 1.4.9를 Windows에 설치했다. 사용자 결정 뒤 등록된 제거 명령으로 제거했고, **RustDesk 서비스·프로세스·설치 실행 파일·Windows 설치 목록 항목이 없음을 확인**했다. iPhone에는 설치하지 않았다. iPad 앱은 사용자가 앞서 설치·시험했다고 보고한 이력이 있으나, 이번 Windows 호스트와의 연결을 검증한 것은 아니다. 기존 설치·제거 사실은 [M6 WorkLog](../../vl_worklog/20260927_M6_Chrome-Remote-Desktop.md#활동-5--windows-호스트-설치)에 보존한다.

제거 프로그램이 사용자 폴더 두 곳과 임시 설치 파일은 남겼다. 합계 약 102MB로, 실행 중인 서비스나 앱은 아니지만 저장 공간은 차지한다. 에이전트의 파일 삭제 요청은 자동 승인 검토에서 `blocked by policy`로 거부돼 정리하지 못했다. 남은 경로는 `%LOCALAPPDATA%\rustdesk`, `%APPDATA%\RustDesk`, `%TEMP%\rustdesk-1.4.9-x86_64.exe`다. 사용자가 파일 탐색기에서 직접 확인하고 삭제할 수 있도록 기록한다.

## 다시 검토할 조건

CRD 장애가 실제로 반복되고, 전원·인터넷·Google 계정·PIN·호스트 서비스 점검으로 해결되지 않을 때 대안 설치를 다시 검토한다. 그때도 설치 전에 디스크 여유, 백그라운드 프로세스와 메모리 사용량, 업데이트 관리 부담을 먼저 확인한다. RustDesk는 후보일 뿐 현재 사용 가능한 백업 수단으로 표현하지 않는다. 장애 당일의 순서는 [CRD 문제 해결 안내](../troubleshooting/when-crd-fails.md)를 따른다.
