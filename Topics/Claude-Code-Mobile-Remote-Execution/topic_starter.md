# VibeLearn AI Topic Starter

> This file starts a new VibeLearn AI learning topic.

## Topic Basic Information

### Topic Name

```
Topic 이름: Claude-Code-Mobile-Remote-Execution
```

### Topic Description

```
설명: 모바일에서 Claude Code를 조작하고, 실제 명령과 파일 작업은 집의 로컬 노트북 또는 맥미니/맥 스튜디오 홈서버에서 실행되도록 구성하는 원격 AI 코딩 환경 학습 및 실험.
```

### Learning Purpose

```
학습 목적:
- 모바일 지시가 로컬/홈서버 머신에서 실행되는 기술 구조를 이해한다.
- 현재 Windows 노트북 기준으로 외부에서 안전하게 Claude Code 작업을 실행하는 1차 실험 환경을 만든다.
- 맥미니 또는 맥 스튜디오를 상시 서버로 두고 노트북을 이동 작업기로 사용하는 구조를 비교 평가한다.
- 성공한 구성을 운영 가이드와 재사용 가능한 학습 산출물로 정리한다.
- 내용이 충분하면 Remotion AI 영상 제작 단계로 확장한다.
```

### Expected Duration

```
예상 기간: 2주 (총 8-12시간)
```

## Learning Goals

```
- [ ] 모바일에서 Claude Code를 조작하는 구조를 다이어그램과 설명으로 정리할 수 있다.
- [ ] 명령이 집/로컬 머신에서 실행되는 네트워크, 인증, 세션, 파일 시스템 흐름을 설명할 수 있다.
- [ ] 가능한 기술 구조(SSH, Tailscale/ZeroTier, 클라우드 개발 환경, 홈서버, 노트북 클라이언트 구조)를 비교표로 평가할 수 있다.
- [ ] 현재 Windows 노트북에서 모바일 원격 접속 기반 Claude Code 실행 실험을 완료할 수 있다.
- [ ] 맥미니/맥 스튜디오 홈서버 도입 시 필요한 장비, 운영 방식, 보안/백업 전략을 설계할 수 있다.
- [ ] 최종 운영 가이드와 영상화 가능한 스토리라인을 만들 수 있다.
```

## Learning Environment

### Operating System

```
OS: Windows 11 현재 노트북, iPhone 모바일 클라이언트, 향후 macOS 기반 맥미니/맥 스튜디오 서버 후보
버전: 확인 필요
```

### Main Tools And Tech Stack

```
- Claude Code
- PowerShell / Windows Terminal
- Git
- Node.js / npm
- SSH
- Tailscale 또는 ZeroTier
- iPhone SSH/terminal client
- macOS Remote Login / SSH 후보
- Obsidian vault
- Remotion AI / Remotion video workflow 후보
```

### Prerequisites

```
필수:
- Git 기본 사용법
- 터미널 기본 명령어
- 로컬 파일 시스템과 vault 작업 구조 이해

권장:
- SSH 키 인증 개념
- VPN 또는 사설 네트워크 개념
- macOS 원격 로그인 기본 개념
- 홈 네트워크, 절전 설정, 백업 전략에 대한 기본 이해
```

## Reference Materials

### Official Documentation

```
- Claude Code 공식 문서: 진행 시 최신 공식 문서 확인
- Tailscale 공식 문서: 진행 시 최신 공식 문서 확인
- OpenSSH 공식/플랫폼 문서: 진행 시 최신 문서 확인
- Apple macOS Remote Login 문서: 맥 서버 구조 조사 시 확인
- Remotion 공식 문서: 영상 제작 단계 진입 시 확인
```

### Materials Folder

```
vl_materials/ 폴더에 추가할 자료:
- 조사한 기술 구조 비교 자료
- 공식 문서 링크 메모
- 환경 점검 결과
- 보안 체크리스트
- 실험 로그
```

## Learning Approach

### Preferred Style

```
- [ ] 이론 먼저, 실습 나중
- [x] 실습 중심, 필요한 이론만
- [ ] 이론과 실습 병행
```

### Time Plan

```
- 주당 학습 시간: 4-6시간
- 학습 가능 요일: 사용자가 세션마다 지정
- 1회당 학습 시간: 1-3시간
```

### Focus Areas

```
- 모바일 지시와 로컬 실행의 역할 분리
- 보안 우선 원격 접속 구조
- 현재 Windows 노트북 기반 1차 실험
- 맥미니/맥 스튜디오 홈서버 구조 비교
- 노트북 이동 작업기와 홈서버 상시 실행 구조
- 운영 가이드와 영상화 가능한 설명 구조
```
