# Windows 실행 호스트 준비 상태 점검

## 점검 목적

현재 Windows 노트북이 모바일 원격 Claude Code 실행 호스트로 사용할 수 있는 상태인지 확인했다. 이번 점검은 읽기 전용 상태 확인이며, 설치, 로그인, 방화벽 변경, 서비스 활성화는 수행하지 않았다.

## 시스템 정보

| 항목 | 결과 |
|---|---|
| Windows 제품명 | Windows 10 Home |
| Windows version | 2009 |
| PowerShell | 5.1.26100.9168 |
| 전원 계획 | Balanced |
| 절전 기능 | S0 Low Power Idle, Network Connected 지원 |
| Hibernate | 지원 |
| Fast Startup | 지원 |

## 도구 상태

| 도구 | 상태 | 확인 결과 | 판단 |
|---|---|---|---|
| Claude Code | 설치됨 | `2.1.143 (Claude Code)` | 로컬 Claude Code 실행 가능성 높음 |
| Claude command | 감지됨 | `C:\Users\dougg\AppData\Roaming\npm\claude.ps1` | npm 전역 설치 형태 |
| Git | 설치됨 | `git version 2.45.2.windows.1` | Git 클라이언트 사용 가능 |
| Node.js | 설치됨 | `v22.15.0` | Claude Code 런타임 조건 충족 가능 |
| npm | 설치됨 | `11.6.2` | 패키지 관리 가능 |
| OpenSSH Client | 설치됨 | `OpenSSH_for_Windows_9.5p2` | outbound SSH 가능 |
| OpenSSH Server | 미감지 | `sshd` 서비스 없음 | inbound SSH 준비 안 됨 |
| ssh-agent | 있음, 비활성 | `Stopped`, `Disabled` | SSH key 운영 시 활성화 검토 필요 |
| Tailscale | 미감지 | command/service 없음 | M4 전 설치/로그인 결정 필요 |
| OpenSSH firewall rule | 미감지 | `*OpenSSH*` rule 없음 | Server 활성화 시 방화벽 검토 필요 |

## 해석

로컬 Claude Code 실행 호스트 관점에서는 기본 도구가 대부분 준비되어 있다. Claude Code, Git, Node.js/npm이 설치되어 있으므로 현재 노트북에서 직접 작업하는 데는 큰 문제가 없어 보인다.

원격 접속 호스트 관점에서는 아직 준비가 부족하다. OpenSSH Client는 있지만 OpenSSH Server인 `sshd` 서비스가 없고, Tailscale도 감지되지 않았다. iPhone에서 이 노트북으로 접속하려면 M4 전에 사설망 도구와 SSH 서버를 별도로 준비해야 한다.

## M4 전 승인 필요 항목

아래 작업은 상태 확인을 넘어 시스템 설정을 바꾸므로 별도 승인 후 진행해야 한다.

- Tailscale 설치
- Tailscale 로그인 및 장치 등록
- Windows OpenSSH Server 설치
- `sshd` 서비스 시작 및 자동 시작 설정
- Windows 방화벽의 SSH inbound rule 추가 또는 활성화
- SSH key 생성/등록
- `ssh-agent` 활성화
- 노트북 절전/전원 설정 변경

## 리스크

1. **절전 리스크**: S0 Low Power Idle Network Connected가 지원되지만, 실제 외부 접속 유지 여부는 테스트가 필요하다.
2. **SSH Server 부재**: 현재 상태로는 iPhone에서 Windows 노트북 shell로 SSH 접속할 수 없다.
3. **Tailscale 부재**: M2에서 추천한 1차 구조를 바로 실행할 수 없다.
4. **방화벽 규칙 부재**: OpenSSH Server 설치 후에도 inbound rule이 필요할 수 있다.
5. **권한 리스크**: OpenSSH Server 설치/서비스 설정은 관리자 권한이 필요할 가능성이 높다.

## 참조 명령

```powershell
claude --version
git --version
node --version
npm --version
ssh -V
Get-Service sshd, ssh-agent
Get-Command tailscale
Get-Service *tailscale*
powercfg /a
powercfg /getactivescheme
Get-NetFirewallRule -DisplayName '*OpenSSH*'
```
