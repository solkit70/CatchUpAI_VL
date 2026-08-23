# WorkLog - M2: 기술 구조 비교와 홈서버 옵션 평가

**날짜**: 2026-08-23
**Topic**: Claude-Code-Mobile-Remote-Execution
**모듈**: M2 - 기술 구조 비교와 홈서버 옵션 평가
**학습 시간**: 약 2시간

## 오늘의 학습 목표

- [x] SSH 직접 접속, Tailscale/ZeroTier, 클라우드 개발 환경, 홈서버 구조를 비교한다.
- [x] 맥미니/맥 스튜디오 서버와 노트북 클라이언트 구조의 장단점을 평가한다.
- [x] 보안, 비용, 안정성, 이동성, 관리 난이도 기준으로 추천안을 만든다.
- [x] 내 환경의 1차 실험 구조를 하나 선정한다.

## 진행 내용

### 1. 공식 문서 기반 조사

**목적**: 각 후보 구조의 실제 지원 범위와 전제를 확인했다.

**과정**:
1. Microsoft OpenSSH for Windows 문서에서 Windows 10/11의 OpenSSH client/server 구조를 확인했다.
2. Tailscale SSH 문서에서 관리형 Tailscale SSH의 서버 컴포넌트 지원 범위를 확인했다.
3. ZeroTier remote desktop 문서에서 ZeroTier IP를 통한 SSH/RDP 접근 흐름을 확인했다.
4. Apple Remote Login 문서에서 macOS SSH/SFTP 접근과 사용자 제한 설정을 확인했다.
5. GitHub Codespaces 문서에서 cloud-hosted development environment 구조를 확인했다.

**결과**:
- 현재 Windows 노트북 1차 실험은 `Tailscale SSH`가 아니라 `Tailscale 사설망 + Windows OpenSSH Server`로 설계하는 것이 맞다고 판단했다.

### 2. 원격 실행 구조 패턴 문서 작성

**목적**: 후보 구조의 역할과 한계를 개념적으로 정리했다.

**결과**:
- `02-Architecture-Comparison/concepts/remote-architecture-patterns.md`

### 3. 기술 구조 비교표 작성

**목적**: 후보 구조를 같은 기준으로 비교했다.

**결과**:
- `02-Architecture-Comparison/comparisons/structure-comparison-table.md`

### 4. 맥미니/맥 스튜디오 홈서버 도입 판단표 작성

**목적**: 구매 전 서버 도입 판단 기준을 만들었다.

**결과**:
- `02-Architecture-Comparison/comparisons/mac-mini-vs-mac-studio-server.md`

### 5. 1차 실험 추천안 작성

**목적**: M3-M4에서 실제로 이어갈 구조를 정했다.

**결과**:
- `02-Architecture-Comparison/decisions/recommended-first-experiment.md`
- 1차 추천: `iPhone -> Tailscale -> Windows OpenSSH Server -> Claude Code -> Vault`

## 문제 해결 로그

### 문제 1: Tailscale SSH와 SSH over Tailscale 혼동 가능성

**증상**: "Tailscale로 SSH"라고 말하면 Tailscale의 관리형 SSH 기능인지, Tailscale 사설망 위에서 일반 SSH를 쓰는 것인지 혼동될 수 있다.

**원인**: Tailscale SSH는 별도 기능이고, Windows 실행 호스트에서는 공식 지원 범위를 그대로 적용하기 어렵다.

**해결**: M2 산출물에서 `Tailscale SSH`와 `SSH over Tailscale`을 분리했다. 현재 1차 실험은 `Tailscale 사설망 + Windows OpenSSH Server`로 정의했다.

## DoD 체크리스트

- [x] 최소 5개 기술 구조 비교
- [x] 맥미니/맥 스튜디오 홈서버 구조 비교
- [x] 노트북 이동 작업기 + 홈서버 상시 실행 구조 설명
- [x] 현재 환경 기준 1차 추천 구조 선정
- [x] 선택하지 않은 구조의 보류 이유 기록
- [x] README.md와 WorkLog 작성

**완료율**: 6/6 (100%)

## Daily Retrospective

### What went well

- 1차 실험 구조가 명확해졌다. 바로 장비를 구매하지 않고 현재 Windows 노트북으로 구조를 검증한 뒤 맥미니/맥 스튜디오를 판단하는 순서가 합리적이다.
- Tailscale 관련 용어를 분리해 이후 M3-M4에서 설정 범위가 모호해지지 않게 했다.

### What could be improved

- 실제 사용자의 Tailscale/ZeroTier 계정 보유 여부, iPhone 앱 설치 여부, Windows OpenSSH 상태는 아직 확인하지 않았다. 이는 M3에서 환경 점검으로 처리해야 한다.

### Insights

- 맥미니는 Claude Code 상시 실행 호스트로 현실적인 2차 후보이다.
- 맥 스튜디오는 Claude Code보다 Remotion 렌더링과 대형 미디어 작업이 서버 역할에 포함될 때 설득력이 생긴다.
- GitHub Codespaces는 좋은 원격 개발 환경이지만, 로컬 vault 조작 실험과는 목표가 다르다.

### Tomorrow's focus

- M3에서 현재 Windows 노트북의 Claude Code, Git, Node.js/npm, OpenSSH, Tailscale 상태를 점검한다.
- 설치나 보안 설정 변경 전 Go/No-Go 체크리스트를 만든다.

## 참조 및 산출물

**생성된 파일/폴더**:
- `02-Architecture-Comparison/README.md`: M2 학습 순서와 결론
- `02-Architecture-Comparison/concepts/remote-architecture-patterns.md`: 원격 실행 구조 패턴
- `02-Architecture-Comparison/comparisons/structure-comparison-table.md`: 기술 구조 비교표
- `02-Architecture-Comparison/comparisons/mac-mini-vs-mac-studio-server.md`: 홈서버 도입 판단표
- `02-Architecture-Comparison/decisions/recommended-first-experiment.md`: 1차 실험 추천안

**참조 자료**:
- Microsoft OpenSSH for Windows overview: https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh-overview
- Microsoft OpenSSH install and first use: https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse
- Tailscale SSH docs: https://tailscale.com/docs/features/tailscale-ssh
- ZeroTier Remote Desktop docs: https://docs.zerotier.com/remotedesktop/
- Apple Remote Login support: https://support.apple.com/guide/mac-help/allow-a-remote-computer-to-access-your-mac-mchlp1066/mac
- GitHub Codespaces docs: https://docs.github.com/en/codespaces/about-codespaces/what-are-codespaces

**작성자**: Codex
**방법론**: VibeLearn AI
