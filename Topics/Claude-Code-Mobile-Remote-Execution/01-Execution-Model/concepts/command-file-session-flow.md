# 명령, 파일, 인증, 세션 흐름

## 명령 실행 위치

모바일에서 입력한 텍스트는 원격 접속 통로를 통해 집 머신의 shell에 전달된다. `pwd`, `git status`, `npm test`, `claude` 같은 명령은 iPhone이 아니라 집 머신에서 실행된다. 따라서 명령 결과는 집 머신의 OS, PATH, 설치된 도구, 현재 작업 디렉터리에 따라 달라진다.

Claude Code CLI 문서는 `claude`, `claude "query"`, `claude -p "query"` 같은 명령 사용 방식을 제공한다. 이 명령들은 원격 접속한 shell에서 실행하면 그 shell이 열려 있는 머신의 프로젝트를 기준으로 동작한다.

> "`claude` | Start interactive REPL"  
> 출처: Anthropic Claude Code CLI reference

## 파일 변경 위치

Claude Code가 읽고 쓰는 파일은 실행 호스트의 파일이다. iPhone의 로컬 파일 앱이나 iCloud 파일이 자동으로 대상이 되는 것이 아니다. 집 노트북의 `C:\AI_study\2026\Changsoo_Vault`에서 Claude Code를 실행하면, 파일 변경도 그 vault 안에서 발생한다.

이 구분은 문제 해결에서 중요하다. 모바일 화면에 파일이 보이지 않거나 변경 결과가 기대와 다르면, 먼저 "Claude Code가 어느 머신의 어느 디렉터리에서 실행 중인가"를 확인해야 한다.

## 인증 흐름

인증은 여러 층으로 나뉜다.

| 인증 대상       | 예시                                               | 확인할 것                        |
| ----------- | ------------------------------------------------ | ---------------------------- |
| 원격 접속       | SSH key, Tailscale login, ZeroTier authorization | 모바일이 집 머신에 접속 가능한가           |
| OS 계정       | Windows/macOS 사용자 계정                             | 해당 계정이 vault에 접근 가능한가        |
| Claude Code | Claude.ai 또는 Anthropic Console 인증                | 집 머신에서 Claude Code가 인증되어 있는가 |
| Git/원격 저장소  | GitHub token, SSH key                            | 원격 작업 중 push/pull이 필요한가      |

M1에서는 인증 설정을 바꾸지 않는다. 이후 M3-M4에서 환경 점검과 실험 설계 후 별도 승인을 받고 진행한다.

## 세션 흐름

세션은 모바일 앱 연결과 집 머신의 shell process를 구분해서 봐야 한다. 단순 SSH 접속에서는 모바일 앱이 끊기면 shell session도 종료될 수 있다. session manager가 있으면 모바일 연결이 끊겨도 서버 측 process를 유지할 수 있지만, Windows와 macOS에서 가능한 방식은 별도로 검토해야 한다.

## 실패 지점과 확인 방법

| 실패 지점 | 증상 | 확인 방법 |
|---|---|---|
| 집 머신 절전 | 외부에서 접속 불가 | 전원/절전 설정, Wake 설정 확인 |
| 네트워크 경로 문제 | SSH 또는 VPN 연결 실패 | 같은 사설망 장치 목록, ping/접속 테스트 확인 |
| 인증 실패 | password/key rejected | SSH key, 계정 권한, Tailscale device authorization 확인 |
| 잘못된 작업 디렉터리 | 파일이 없거나 다른 repo가 보임 | `pwd`, `dir`, `git status` 확인 |
| Claude Code 미설치/미인증 | `claude` 명령 실패 | `claude --version`, `claude doctor` 또는 공식 문서 기준 확인 |
| 세션 종료 | 모바일 앱 전환 후 작업 중단 | session 유지 방식, shell process 상태 확인 |
| vault 동기화 충돌 | Obsidian/Git 변경 충돌 | 작업 전후 `git status`, 동기화 상태 확인 |

## M1에서 확정한 운영 원칙

- 원격 접속 설정 변경은 M4 전까지 하지 않는다.
- 공개 포트 개방은 기본 실험안으로 채택하지 않는다.
- 모든 실험 전 `어느 머신`, `어느 디렉터리`, `어느 계정`인지 확인한다.
- vault 변경 전 작업 범위를 작게 잡고 Git 상태를 확인한다.

## 참조

- Anthropic Claude Code setup: https://docs.anthropic.com/en/docs/claude-code/getting-started
- Anthropic Claude Code CLI reference: https://docs.anthropic.com/en/docs/claude-code/cli-usage
