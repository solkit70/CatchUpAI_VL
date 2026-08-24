# M4 - 모바일 원격 실행 1차 실험 설계 및 수행

## 목적

이 모듈은 iPhone에서 집 Windows 노트북의 터미널에 접속하고, 명령 실행과 파일 변경이 실제로 노트북에서 일어나는지 검증한다. 목표는 단순 접속 성공이 아니라 `모바일은 조작 화면`, `Windows 노트북은 실행 호스트`, `vault는 노트북 파일 시스템`이라는 구조를 직접 확인하는 것이다.

## 현재 준비 상태

| 항목 | 상태 | 값 |
|---|---:|---|
| 실행 호스트 | 준비 완료 | Windows 노트북 `Changsoo` |
| Windows 사용자 | 확인 완료 | `dougg` |
| Tailscale IPv4 | 확인 완료 | `100.109.17.103` |
| MagicDNS | 확인 완료 | `changsoo.tail8af0a9.ts.net` |
| OpenSSH Server | 준비 완료 | `sshd` running, automatic |
| SSH 방화벽 | 준비 완료 | Tailscale 대역만 허용 |

## 학습 순서

1. `lab/experiment-plan.md`에서 실험 절차와 성공 기준을 확인한다.
2. `lab/mobile-ssh-claude-code-test.md`에 따라 iPhone에서 SSH 접속을 수행한다.
3. `lab/validation-results.md`에 명령 실행 위치, Claude Code 실행 여부, 파일 변경 결과를 기록한다.
4. 문제가 발생하면 `troubleshooting/remote-session-issues.md`에 증상과 해결 과정을 남긴다.

## 산출물

| 파일 | 역할 |
|---|---|
| `lab/experiment-plan.md` | M4 전체 실험 절차서 |
| `lab/mobile-ssh-claude-code-test.md` | iPhone SSH 접속 및 Claude Code 실행 테스트 기록 |
| `lab/validation-results.md` | 실행 위치와 파일 변경 검증 결과 |
| `troubleshooting/remote-session-issues.md` | 접속/인증/세션 문제 해결 로그 |

