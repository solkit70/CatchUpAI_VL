# M3 - 현재 Windows 노트북 환경 점검

**상태**: 완료
**예상 학습 시간**: 1.5h
**Topic**: Claude-Code-Mobile-Remote-Execution

## 학습 순서

1. [audit/windows-host-readiness.md](audit/windows-host-readiness.md) - Windows 노트북이 원격 Claude Code 실행 호스트로 준비되어 있는지 확인한다.
2. [audit/vault-safety-checklist.md](audit/vault-safety-checklist.md) - vault와 Git 경계를 확인하고 안전한 실험 범위를 정의한다.
3. [decisions/preflight-go-no-go.md](decisions/preflight-go-no-go.md) - M4 원격 실행 실험 전 Go/No-Go 기준을 확인한다.

## 핵심 결론

현재 노트북은 Claude Code, Git, Node.js/npm, OpenSSH Client가 설치되어 있어 로컬 실행 호스트로는 준비되어 있다. 다만 M4 원격 접속 실험을 바로 실행하기에는 OpenSSH Server와 Tailscale이 감지되지 않았고, Windows 방화벽의 OpenSSH 규칙도 확인되지 않았다.

따라서 다음 단계는 "바로 원격 접속 실험"이 아니라, M4 시작 전 별도 승인으로 Tailscale 설치/로그인 여부와 Windows OpenSSH Server 설치/활성화 여부를 결정하는 것이다.

## 확인된 상태

| 항목 | 상태 | 메모 |
|---|---|---|
| OS | Windows 10 Home, version 2009 | PowerShell 5.1, build 26100.9168 |
| Claude Code | 설치됨 | `2.1.143 (Claude Code)` |
| Git | 설치됨 | `git version 2.45.2.windows.1` |
| Node.js | 설치됨 | `v22.15.0` |
| npm | 설치됨 | `11.6.2` |
| OpenSSH Client | 설치됨 | `OpenSSH_for_Windows_9.5p2` |
| OpenSSH Server | 미감지 | `sshd` 서비스 없음 |
| ssh-agent | 있음, 비활성 | `Stopped`, `Disabled` |
| Tailscale | 미감지 | command/service 감지 안 됨 |
| OpenSSH firewall rule | 미감지 | DisplayName `*OpenSSH*` 규칙 없음 |
| 전원 상태 | Balanced | S0 Low Power Idle, Network Connected 지원 |

## 다음 모듈 준비

M4에서는 먼저 실험 절차서를 작성하고, 설정 변경이 필요한 항목을 하나씩 승인받아야 한다. 특히 Tailscale 설치/로그인, OpenSSH Server 설치/활성화, 방화벽 규칙 생성, SSH key 설정은 모두 별도 승인 대상이다.

## 이전/다음 모듈

- 이전 모듈: `02-Architecture-Comparison/`
- 다음 모듈: `04-Remote-Execution-Lab/`
