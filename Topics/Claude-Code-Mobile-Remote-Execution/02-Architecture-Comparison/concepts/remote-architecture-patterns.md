# 원격 Claude Code 실행 구조 패턴

## 패턴 1: 직접 SSH

직접 SSH는 모바일 SSH 클라이언트가 집 머신의 SSH 서버에 바로 접속하는 구조다. 개념은 단순하지만 집 네트워크의 공인 IP, 포트 포워딩, 방화벽, 동적 DNS, 공격 노출면을 함께 관리해야 한다.

Windows에서는 OpenSSH가 Windows 10 build 1809 이상과 Windows 11에서 기능으로 제공된다. Microsoft 문서는 SSH가 client-server 구조이며, `ssh`는 클라이언트, `sshd`는 원격 관리 대상 시스템에서 실행되는 서버 구성요소라고 설명한다.

## 패턴 2: 사설망 VPN + SSH

Tailscale 또는 ZeroTier 같은 사설망 도구를 쓰면 집 머신과 iPhone을 같은 가상 사설망에 넣고, 그 안에서 SSH를 사용할 수 있다. 이 방식은 일반적으로 공개 포트 개방을 피할 수 있어 1차 실험에 적합하다.

주의할 점은 `Tailscale SSH`와 `SSH over Tailscale`이 다르다는 것이다. Tailscale SSH는 Tailscale이 SSH 인증과 정책을 관리하는 기능이고, 공식 문서상 서버 컴포넌트는 Linux와 macOS open source `tailscale` + `tailscaled` CLI 장치에 한정된다. 현재 Windows 노트북에서는 Tailscale 네트워크 위에 Windows OpenSSH Server를 얹는 구조가 더 현실적이다.

ZeroTier도 유사하게 장치 간 가상 네트워크를 제공하고, ZeroTier IP로 SSH 또는 RDP에 접속하는 방식을 문서화한다. ZeroTier 문서는 port forwarding이나 별도 VPN 세팅을 신경 쓰지 않아도 ZeroTier가 처리한다고 설명한다.

## 패턴 3: 클라우드 개발 환경

GitHub Codespaces는 로컬 노트북이 아니라 GitHub가 호스팅하는 클라우드 개발 환경에서 코드를 실행한다. GitHub 문서에 따르면 codespace는 클라우드에 호스팅되는 개발 환경이며, Docker container가 VM 위에서 실행된다. 브라우저, VS Code, command shell을 통해 접근할 수 있다.

이 구조는 모바일 접근성과 재현성은 좋지만, 현재 vault와 로컬 노트북 파일을 직접 다루는 목적에는 어긋날 수 있다. 특히 Obsidian vault가 로컬 디스크에 있고 Claude Code가 그 vault를 직접 편집해야 한다면, cloud 환경으로 옮기는 설계가 별도로 필요하다.

## 패턴 4: 현재 Windows 노트북 실행 호스트

현재 보유한 Windows 노트북을 실행 호스트로 쓰는 방식은 비용이 가장 낮고 빠르게 검증할 수 있다. 단점은 노트북이 이동 중이거나 절전 상태이면 집 서버 역할을 안정적으로 수행하기 어렵다는 점이다.

1차 실험에서는 이 구조가 적절하다. 먼저 모바일 원격 조작, 인증, 파일 변경 위치, Claude Code 실행 흐름을 확인하고, 문제가 운영 안정성인지 기술 구조 자체인지 분리할 수 있다.

## 패턴 5: 맥미니/맥 스튜디오 홈서버

맥미니 또는 맥 스튜디오를 집에 상시 켜두고, iPhone과 노트북은 모두 클라이언트로 쓰는 구조다. Apple 문서에 따르면 macOS는 Remote Login을 켜면 SSH 또는 SFTP로 다른 컴퓨터에서 접근할 수 있고, 접근 허용 사용자를 제한할 수 있다. 다만 Apple은 Remote Login이 Mac을 덜 안전하게 만들 수 있다고 명시하므로, 계정/네트워크/권한 제한이 필수다.

맥미니는 상시 서버, Claude Code 실행, Obsidian vault 작업, 가벼운 자동화에 적합하다. 맥 스튜디오는 영상 렌더링, 대형 미디어 작업, 로컬 AI/그래픽 부하를 홈서버에 함께 맡길 때 고려할 수 있다.

## 패턴 6: 노트북 이동 작업기 + 홈서버 상시 실행

이 구조에서는 홈서버가 실제 실행 호스트이고, 노트북은 집 밖에서 접속하는 고급 클라이언트다. 장점은 작업 위치가 서버 한 곳으로 모이고, 노트북 분실/절전/이동과 실행 환경이 분리된다는 점이다.

단점은 서버 운영 책임이 생긴다는 것이다. 전원, 절전, 백업, 원격 로그인, OS 업데이트, 계정 권한, 물리 보안, 네트워크 장애 대응을 관리해야 한다.

## 참조

- Microsoft OpenSSH for Windows overview: https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh-overview
- Microsoft OpenSSH install and first use: https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse
- Tailscale SSH docs: https://tailscale.com/docs/features/tailscale-ssh
- ZeroTier Remote Desktop docs: https://docs.zerotier.com/remotedesktop/
- Apple Remote Login support: https://support.apple.com/guide/mac-help/allow-a-remote-computer-to-access-your-mac-mchlp1066/mac
- GitHub Codespaces docs: https://docs.github.com/en/codespaces/about-codespaces/what-are-codespaces
