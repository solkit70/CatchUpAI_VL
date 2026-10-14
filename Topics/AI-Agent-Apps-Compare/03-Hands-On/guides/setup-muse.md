---
title: "Muse 웹 첫 사용 및 권한 확인"
source: "https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/"
author:
  - "박창수"
  - "Codex"
created: "2026-10-11 06:47:40"
tags:
  - ai-agent-apps-compare
  - muse
  - setup-guide
---

# Muse 웹 첫 사용 및 권한 확인

[English](setup-muse.en.md)

## 목적과 범위

이 가이드는 Windows 브라우저에서 Muse에 접속해 첫 화면과 설정 위치를 확인하는 절차를 정리한다. 가입·로그인·연결 승인 등 계정 작업은 사용자가 직접 한다. 기본 시연은 공개 자료만 쓰며, 실제 메일·일정·계정별 설정은 이 공개 자료에 기록하지 않는다.

## 시작 절차

1. 브라우저에서 [muse.ai](https://muse.ai)를 연다. 계정 생성 또는 로그인 화면이 나오면 사용자가 직접 진행한다.
2. 첫 화면에 도달하면 이름, 웹 접속 여부, 기본 사용량 화면을 확인한다. 사용량 제한이나 업그레이드 안내가 나오더라도 이 Topic에서는 새 유료 플랜에 가입하지 않는다.
3. **Settings → Data controls**에서 모델 개선 사용 관련 항목을 찾는다. Meta는 상호작용을 모델 학습에 사용하지 않도록 선택할 수 있다고 안내한다. 화면의 계정별 선택 상태는 공개 레포에 복사하지 않는다.
4. **Settings → Permissions**에서 Connector defaults와 Web access defaults를 확인한다. “Ask for some actions”는 모든 동작 전에 묻는다는 뜻으로 해석하지 않는다.
5. 필요한 경우 커넥터별 권한 목록을 읽기·쓰기·삭제·외부 알림으로 나눠 살펴본다. 실제 계정에 연결할지는 사용자가 결정하며, 쓰기·삭제 권한은 필요한 범위를 먼저 정한다.
6. 공개 자료 과제를 실행한 뒤 Muse 답변의 Sources 패널을 연다. 각 핵심 주장에 회사 공식 도메인의 자료가 연결되는지 확인한다.

## 첫 공개 자료 과제

```text
Meta의 공식 공개 자료에서 Muse의 기능 세 가지와 무료 사용 범위를 찾아 요약해 주세요. 각 사실에 공식 출처 링크를 붙이고, 공식 자료에서 확인되지 않는 내용은 확인되지 않았다고 표시해 주세요. Gmail이나 Google Calendar를 열지 말고, 일정을 만들거나 변경하거나 삭제하지 마세요. 메일을 보내지도 마세요.
```

처음 답변의 출처가 제3자 자료라면 공식 자료를 찾도록 후속 질문을 한다. “공식 자료만 사용했다”는 답변만으로 공식성을 판단하지 말고, Sources 패널의 도메인과 페이지 제목을 직접 본다.

## 화면 참고: 개인정보 설정과 기본 권한

아래는 실습 중 촬영한 화면의 정리본이다. 계정별 선택 상태, 연결 수, 네트워크 프로토콜 상태는 가렸다.

![Muse Data controls 화면. 계정별 선택 상태는 가림 처리했다.](../assets/muse-screenshots/data-controls.png)

![Muse 권한 기본값 화면. 실제 선택 표시와 계정별 수치는 가림 처리했다.](../assets/muse-screenshots/permission-defaults.png)

![Direct network protocols 화면. 계정별 스위치 상태는 가림 처리했다.](../assets/muse-screenshots/direct-network-protocols.png)

## 권한 확인 원칙

- 앱 연결은 첫 공개 자료 과제에 필요하지 않다.
- 연결을 선택했다면 동의 화면과 Muse 안의 작업별 권한을 각각 읽는다.
- 읽기와 쓰기 권한은 다르다. 메일·일정 생성, 변경, 삭제, 초대·알림 등은 별도 항목일 수 있다.
- 실제 화면에서 확인하지 않은 기본값이나 승인 동작을 일반화하지 않는다.
- 방송이나 화면 공유에서는 계정명·이메일·개인 데이터가 노출되지 않도록 한다.

## 확인한 공식 자료

- [Meta — Introducing Muse](https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/): Secure VM, Sentinel, 백그라운드 작업, 기억 기반 제안, 개인정보 제어.
- [Meta Help Center — About Muse subscriptions](https://www.meta.com/help/subscriptions/1021145227643680/): 무료 사용량 제한 및 구독 계획. 제공 조건은 지역·계정에 따라 다를 수 있다.
