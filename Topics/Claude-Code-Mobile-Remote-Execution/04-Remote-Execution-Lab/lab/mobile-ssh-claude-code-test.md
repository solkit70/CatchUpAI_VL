# 모바일 SSH 및 Claude Code 테스트 기록

## 테스트 전 상태

| 항목 | 값 |
|---|---|
| 실행 호스트 | `Changsoo` |
| SSH 사용자 | `catchupai` |
| Tailscale IP | `100.109.17.103` |
| MagicDNS | `changsoo.tail8af0a9.ts.net` |
| OpenSSH Server | `Running`, `Automatic` |

## iPhone 접속 절차

1. iPhone에서 Tailscale 앱을 설치한다.
2. `solkit70@gmail.com` tailnet에 로그인한다.
3. Tailscale 앱에서 iPhone이 `Connected` 상태인지 확인한다.
4. SSH 앱에서 새 host를 만든다.
5. Host 또는 Address에 `100.109.17.103`을 입력한다.
6. Port는 `22`로 둔다.
7. Username은 `catchupai`를 입력한다.
8. 첫 테스트는 사용자가 직접 만든 `catchupai` 로컬 계정 비밀번호로 로그인한다.

## 접속 후 실행할 명령

```powershell
hostname
whoami
$PWD.Path
claude --version
```

## 사용자 실행 결과

| 확인 항목 | 예상값 | 실제값 | 상태 |
|---|---|---|---:|
| SSH 접속 | 성공 | `catchupai@CHANGSOO C:\Users\catchupai>` prompt 확인 | 완료 |
| `hostname` | `Changsoo` | `Changsoo` | 완료 |
| `whoami` | `changsoo\catchupai` | `changsoo\catchupai` | 완료 |
| 현재 경로 | Windows 경로 | `C:\Users\catchupai` | 완료 |
| `claude --version` | Claude Code 버전 | `2.1.241` | 완료 |

## 관찰 메모

- 대기
- catchupai 계정에는 Claude Code가 아직 설치되어 있지 않다. where claude와 claude --version 모두 실패했다.


