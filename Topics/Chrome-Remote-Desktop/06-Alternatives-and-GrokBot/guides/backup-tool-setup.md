---
title: "RustDesk 두 번째 카드 설치 계획"
created: 2026-09-27 00:00:00
author:
  - "Codex"
tags:
  - chrome-remote-desktop
  - rustdesk
  - guides
---

## 왜 RustDesk를 먼저 검증하나

RustDesk 클라이언트는 Windows와 iPhone/iPad를 지원한다. 공용 서버로 먼저 연결을 검증한 뒤에야, 자체 서버가 필요한지 판단한다. 자체 서버는 ID·중계 인프라를 내가 관리할 수 있지만 포트 개방·업데이트 책임도 함께 생긴다. [RustDesk 클라이언트](https://rustdesk.com/docs/en/client/) · [자체 서버 개요](https://rustdesk.com/docs/en/self-host/)

## 방송 후 실습 순서

1. **Windows 호스트**: RustDesk 공식 다운로드 경로에서 설치 파일을 받고 설치한다. 설치 화면의 기기 ID·비밀번호는 캡처·WorkLog에 기록하지 않는다.
2. **iPhone 또는 iPad 클라이언트**: App Store에서 RustDesk를 설치한다. iOS는 다른 기기를 조작하는 클라이언트로 쓰며, iPhone/iPad 자체를 원격 조작하는 호스트로 가정하지 않는다. [공식 지원 범위](https://rustdesk.com/docs/en/client/)
3. **보안 먼저**: 무인 접속을 켜기 전 영구 비밀번호와 권한을 확인한다. 모르는 사람에게 기기 ID·일회성 비밀번호·화면을 보내지 않는다.
4. **실측**: 집 밖 또는 휴대폰 데이터에서 연결 → 테스트 문서 한 줄 입력 → 저장 → Windows Lock → Disconnect 순서로 마친다.
5. **비교 기록**: 접속 시간, 한글 입력, 끊김, 화면 품질, 안전 종료를 CRD M4 실측과 나란히 기록한다.

## iPhone에 RustDesk 설치하기

1. iPhone에서 [App Store의 RustDesk Remote Desktop](https://apps.apple.com/us/app/rustdesk-remote-desktop/id1581225015)을 열어 **받기**를 누른다. RustDesk 공식 문서도 iPhone/iPad용 앱을 App Store에서 받도록 안내한다.
2. 설치가 끝나면 앱을 연다. 처음에는 공용 서버로 연결할 수 있으므로, 이번 첫 검증에서는 `Network`의 ID/Relay 서버를 바꾸지 않는다.
3. 집 Windows 컴퓨터에서 RustDesk를 열어 **기기 ID**를 확인한다. iPhone 앱의 접속 칸에 그 ID를 넣고 연결한다. 비밀번호·일회성 코드는 방송 화면, 채팅, WorkLog, 캡처에 남기지 않는다.
4. 집 컴퓨터 쪽에서 접속 요청을 승인하거나, 이미 직접 설정한 무인 접속 비밀번호를 iPhone에 직접 입력한다. 모르는 사람이 보낸 ID나 접속 요청은 받지 않는다.
5. 연결되면 테스트 문서에 한 줄을 적어 저장한다. 끝낼 때는 **Windows Lock → 잠금 화면 확인 → Disconnect** 순서로 종료한다.

iPhone/iPad 앱은 다른 기기를 **조작하는 쪽**이다. iPhone 자체를 다른 기기에서 조작하거나 화면 공유하는 호스트 기능은 제공하지 않는다. [App Store 설명](https://apps.apple.com/us/app/rustdesk-remote-desktop/id1581225015)

## 아직 하지 않은 일

이 문서는 iPhone 설치 절차를 포함하지만, 이 환경에서 iPhone 접속·문서 저장을 아직 확인하지 않았다. 실제로 확인한 뒤에만 WorkLog를 완료 상태로 바꾼다. 자체 서버는 이번 최소 검증에 포함하지 않는다.
