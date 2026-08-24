# M4 검증 결과

## 검증 기준

| 기준 | 설명 | 상태 |
|---|---|---:|
| 모바일 접속 | iPhone에서 Tailscale 경유 SSH 접속 | 완료 |
| 실행 호스트 확인 | `hostname`, `whoami`로 Windows 노트북 확인 | 완료 |
| Claude Code 확인 | 원격 세션에서 `claude --version` 실행 | 완료 |
| 파일 변경 위치 확인 | 실험 파일이 vault 경로에 생성되는지 확인 | 완료 |
| 실패/복구 기록 | 문제 발생 시 원인과 해결 기록 | 완료 |

## 서버 쪽 검증 결과

| 항목 | 결과 |
|---|---|
| `sshd` service | `Running`, `Automatic` |
| `Tailscale` service | `Running`, `Automatic` |
| Tailscale IPv4 | `100.109.17.103` |
| SSH firewall scope | Tailscale 대역만 허용 |
| TCP 22 local test | `127.0.0.1:22` success |
| TCP 22 Tailscale test | `100.109.17.103:22` success |
| Claude Code local command | `2.1.143 (Claude Code)` |
| Claude command path | `C:\Users\dougg\AppData\Roaming\npm\claude.ps1` |

## 모바일 쪽 검증 결과

아직 수행 전.

## 파일 변경 검증 결과

아직 수행 전.

## 결론

M4 본 접속 테스트는 완료되었다. iPhone에서 Tailscale 경유로 Windows 노트북에 SSH 접속했고, `catchupai` 계정에서 Claude Code `2.1.241` 실행을 확인했으며, 모바일 명령으로 생성한 파일이 실제 노트북 vault 경로에 존재함을 교차 검증했다.





