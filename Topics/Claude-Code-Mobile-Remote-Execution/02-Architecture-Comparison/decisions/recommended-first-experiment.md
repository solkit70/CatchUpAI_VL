# 1차 실험 추천안

## 결정

1차 실험은 다음 구조로 진행한다.

```text
iPhone
  -> Tailscale private network
  -> Windows laptop running OpenSSH Server
  -> shell session
  -> Claude Code
  -> C:\AI_study\2026\Changsoo_Vault
```

이 결정은 구매 없이 현재 환경으로 검증 가능하고, 공개 포트 개방을 피하면서도 M1에서 정의한 핵심 흐름을 실제로 테스트할 수 있기 때문이다.

## 왜 Tailscale + Windows OpenSSH인가

Tailscale은 장치를 사설 네트워크로 묶어 공개 인터넷에 SSH 포트를 직접 노출하지 않는 방향으로 실험할 수 있다. Windows에서는 Microsoft 공식 OpenSSH Server를 실행 호스트에 설치/활성화하고, iPhone SSH 클라이언트에서 Tailscale IP 또는 이름으로 접속하는 구조가 현실적이다.

중요한 구분:
- `Tailscale SSH`: Tailscale이 SSH 인증/정책을 관리하는 기능이다. 공식 문서상 서버 컴포넌트는 Linux와 macOS open source CLI 장치 중심이다.
- `SSH over Tailscale`: Tailscale 사설망을 네트워크 경로로 쓰고, 실제 SSH 서버는 Windows OpenSSH가 담당한다. 현재 Windows 노트북 1차 실험은 이 구조가 맞다.

## 보류한 구조

### 직접 SSH + 포트포워딩

보류한다. 공개 포트 개방, 공유기 설정, 동적 DNS, 계정 공격 노출면을 관리해야 한다. 이번 Topic의 초기 목표는 구조 검증이므로 리스크가 큰 공개 노출 구조는 뒤로 미룬다.

### ZeroTier + Windows OpenSSH

대안으로 유지한다. 기능상 Tailscale과 비슷한 사설망 접근이 가능하지만, 1차 실험에서 두 사설망 도구를 동시에 비교하면 범위가 커진다. Tailscale이 막히거나 계정/네트워크 정책상 부적합하면 ZeroTier로 전환한다.

### GitHub Codespaces

이번 1차 실험에서는 보류한다. Codespaces는 클라우드 개발 환경으로는 좋지만, 집 노트북의 로컬 vault를 직접 Claude Code로 조작한다는 목표와는 다르다.

### 맥미니 홈서버

2차 후보로 둔다. 1차 실험에서 상시 실행 호스트 필요성이 확인되면 구매 후보로 검토한다. Claude Code 중심이면 맥미니가 가장 현실적인 홈서버 후보이다.

### 맥 스튜디오 홈서버

고부하 작업 확인 전까지 보류한다. Remotion 렌더링, 대용량 미디어 작업, 로컬 AI 작업을 상시 처리해야 한다는 근거가 생기면 다시 비교한다.

## M3에서 확인할 항목

M3 환경 점검에서 아래를 확인해야 한다.

- Windows 버전과 PowerShell 버전
- Claude Code 설치/인증 상태
- Node.js/npm 상태
- Git 상태
- OpenSSH Client/Server 설치 여부
- `sshd` 서비스 상태
- Windows 방화벽 규칙 상태
- Tailscale 설치 여부와 로그인 상태
- vault 경로와 git 상태
- 노트북 절전/전원 설정

## M4 실험 성공 기준

M4에서 다음을 만족하면 1차 실험 성공으로 본다.

- iPhone에서 Tailscale 연결 상태 확인
- iPhone SSH 앱에서 Windows 노트북에 접속
- 접속한 shell에서 현재 머신/디렉터리 확인
- Claude Code 또는 안전한 shell 명령 실행
- vault 안의 안전한 테스트 파일 또는 상태 확인
- 작업 전후 Git 상태 기록
- 접속 실패/세션 끊김/절전 문제 기록

## 현재 추천 결론

현재 기준 추천 순서는 다음과 같다.

1. `Tailscale + Windows OpenSSH + Claude Code`: 1차 실험
2. `ZeroTier + Windows OpenSSH`: Tailscale 대안
3. `맥미니 홈서버 + Tailscale/SSH`: 1차 실험 성공 후 2차 구조
4. `맥 스튜디오 홈서버`: Remotion/미디어 고부하가 확인된 후 검토
5. `GitHub Codespaces`: 로컬 vault 중심이 아닌 GitHub repo 중심 작업용 별도 옵션

## 참조

- Microsoft OpenSSH for Windows overview: https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh-overview
- Microsoft OpenSSH install and first use: https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse
- Tailscale SSH docs: https://tailscale.com/docs/features/tailscale-ssh
- ZeroTier Remote Desktop docs: https://docs.zerotier.com/remotedesktop/
- Apple Remote Login support: https://support.apple.com/guide/mac-help/allow-a-remote-computer-to-access-your-mac-mchlp1066/mac
- GitHub Codespaces docs: https://docs.github.com/en/codespaces/about-codespaces/what-are-codespaces
