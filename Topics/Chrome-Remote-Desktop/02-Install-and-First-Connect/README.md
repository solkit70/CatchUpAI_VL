---
title: "M2 — 설치와 첫 연결"
created: 2026-09-20 20:50:00
module: M2
tags:
  - chrome-remote-desktop
  - readme
---

# M2 — 설치와 첫 연결 · 호스트와 밖에서 쓰는 기기

> **집에 켜 둘 컴퓨터에 문을 만들고, 밖에서 쓰는 기기로 실제로 들어가 본다.**
> 2026-09-20 실제로 설치·접속한 기록이며, 화면 캡처는 전부 그날 것이다.

## 읽는 순서

| 순서 | 문서 | 무엇을 하나 | 걸리는 시간 |
|---|---|---|---|
| 1 | [guides/install-host-windows.md](guides/install-host-windows.md) | 집 컴퓨터(Windows)에 설치 · 이름 · PIN | 10~15분 |
| 2 | [guides/connect-from-iphone.md](guides/connect-from-iphone.md) | **iPhone 전용** — Safari 웹앱으로 연결 · LTE 실측 · 안전 종료 | 10분 |
| 3 | [guides/connect-from-phone.md](guides/connect-from-phone.md) | iPad·Android를 포함한 폰·태블릿 공통 안내 | 15~20분 |
| 4 | [guides/connect-from-laptop.md](guides/connect-from-laptop.md) | 다른 컴퓨터 브라우저에서 접속 · 남의 컴퓨터일 때 주의 | 5분 |
| 참고 | [troubleshooting/cannot-connect.md](troubleshooting/cannot-connect.md) | 안 될 때 — 증상별로 어디를 보나 | 막혔을 때 |
| 기록 | [examples/first-connect-log.md](examples/first-connect-log.md) | 첫 접속 실측 (기기·회선·시간·체감) | — |

## 이 모듈에서 실제로 부딪힌 것 (처음 하는 사람이 똑같이 부딪힐 것)

1. **기기 이름 칸에 Windows 사용자 이름(본명)이 미리 들어 있다** — 그냥 Next 누르면 본명이 등록된다
2. **같은 컴퓨터가 목록에 두 번 보인다** (Remote devices / This device) — 두 대가 아니다
3. **iPad 는 App Store 에 앱이 없다** — 2025-09 폐지. Safari + 홈 화면 추가
4. **iOS 공유 메뉴에 연락처 이름·사진이 뜬다** — 캡처를 문서·영상에 쓸 때 가려야 한다
5. PIN 최소 6자리는 **도움말엔 없고 설치 화면에 있다**
6. **iPhone 실습 중 Windows 권한 확인창이 나타났다** — 사진에는 `Windows Command Processor` · 게시자 `Microsoft Windows`가 보인다. 같은 시각 RustDesk 설치가 진행돼, CRD 입력 자체가 원인인지는 확인되지 않았다
7. **최신 Windows 11 계정 메뉴에는 잠금이 보이지 않을 수 있다** — 시작 메뉴의 전원 아이콘에서 Lock/잠금을 찾는다

## 확인된 사실 (2026-09-20)

| | |
|---|---|
| 호스트 | Windows 11 Home 노트북 · 버전 151.0.7922.13 · 서비스 `chromoting` 자동 시작 |
| 접속 | iPad(Safari Web App) — 집 Wi-Fi ✅ · **폰 핫스팟 LTE ✅** · VPN 켜진 상태 ✅ |
| 입력 | 영문 ✅ · **한글 ✅** · Ctrl+S 저장 ✅ |
| 체감 | 빠름 (정적 화면 기준) |

2026-09-27 iPhone 보강 실습에서는 Wi-Fi를 끄고 모바일 데이터로 접속해 메모장 한글·영문 입력과 한 줄 저장·내용 유지, Windows 잠금·해제·Disconnect·재접속을 확인했다. 접속은 약 2초 추정, 끊김은 0회였다. → [iPhone 전용 안내](guides/connect-from-iphone.md#현재-실습-상태) · [M4 기록](../vl_worklog/20260923_M4_Chrome-Remote-Desktop.md#활동-4--iphone-모바일-데이터-첫-실측)

## 미검증 범위와 다음 확인

- **Android 앱 방식은 미검증 범위**다. 사용자가 Android 기기를 보유하지 않아 필수 실습에서 제외했으며, Android 기기를 빌리거나 새로 준비할 필요는 없다
- 다른 컴퓨터 브라우저 접속은 두 번째 컴퓨터가 생기면 하는 선택 확장 실습이다
- **실습 3 — 일부러 막아 보기** 중 PIN 오입력과 iPad Wi-Fi 단절은 2026-09-23에 실측했다. 결과는 [문제 해결 기록](troubleshooting/cannot-connect.md)에 반영했다. 절전·다른 계정 실험은 사용자가 나중에 진행하기로 했다

## 캡처 목록 (`images/`)

| 파일 | 내용 | 마스킹 |
|---|---|---|
| `01_remotedesktop_access.png` | 접속 페이지 첫 화면 | — |
| `02_remotedesktop_addToChrome.png` | 확장 프로그램 추가 | — |
| `03_remotedesktop_acceptNinstall.png` | 설치 동의 | — |
| `04_remotedesktop_name_masked.png` | 이름 입력 (기본값 자리 가림) | ✅ 본명 |
| `05_remotedesktop_pin.png` | PIN 설정 (점으로 표시됨) | 불필요 |
| `06_remotedesktop_device3.png` | 기기 목록 Online | — |
| `001_iPad_access.PNG` | iPad 기기 목록 + 홈 화면 추가 안내 | — |
| `002_iPad_pin.PNG` | iPad PIN 입력 | 불필요 |
| `003_iPad_addToHomeScreen_masked.png` | 공유 메뉴 | ✅ 연락처 |
| `004_iPad_addToHomeScreen2_masked.png` | 홈 화면에 추가 · Open as Web App | ✅ 연락처 |
| [`005_iPhone_test_Windows_UAC_Command_Processor.jpg`](images/005_iPhone_test_Windows_UAC_Command_Processor.jpg) | iPhone 실습 중 노트북에 나타난 Windows UAC 확인창 · `Windows Command Processor`/`Microsoft Windows` 표시 | ✅ 위치 EXIF 제거 · 화면 반사·주변부는 영상 편집 때 확인 |

> `04_remotedesktop_name.png` · `06_remotedesktop_device.png` · `003/004` 원본은 본명·연락처가 보이므로 **문서·영상에 쓰지 않는다.**

`005` 사진의 원본은 다운로드 폴더에 그대로 두었고, 이 폴더의 복사본에서 위치를 포함한 EXIF 메타데이터를 제거했다. 사진의 UAC를 「iPhone에서 글자를 입력하면 항상 뜨는 창」으로 설명하지 않는다. 촬영 시각과 RustDesk 설치 시각이 겹쳐, 설치 프로그램의 권한 요청이었을 가능성이 높지만 부모 프로세스는 확인하지 못했다.

## 다음 모듈

→ `03-Security-Checklist/` — 편해진 만큼 열린 문 닫기 (2단계 인증 · 절전 · 끊을 때 잠금 · 접속 기록)

← [../01-Concepts-and-Choice/README.md](../01-Concepts-and-Choice/README.md) · [로드맵](../vl_roadmap/20260920_RoadMap_Chrome-Remote-Desktop.md) · [WorkLog](../vl_worklog/20260920_M2_Chrome-Remote-Desktop.md)
