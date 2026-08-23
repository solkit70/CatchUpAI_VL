# 모바일에서 Claude Code를 조작하는 구조

## 핵심 결론

모바일에서 Claude Code를 쓴다는 말은 보통 iPhone이 직접 프로젝트 파일을 읽고 명령을 실행한다는 뜻이 아니다. 더 정확히는 iPhone에서 원격 터미널 또는 원격 접속 앱을 통해 집에 있는 실행 호스트의 터미널을 조작하고, 그 터미널 안에서 Claude Code가 실행되는 구조다.

Anthropic의 Claude Code 문서는 Claude Code를 터미널에서 동작하는 에이전틱 코딩 도구로 설명한다. 또한 설치 후 프로젝트 디렉터리로 이동한 뒤 `claude`를 실행하는 흐름을 제시한다. 즉 Claude Code는 실행되는 머신의 shell, 현재 작업 디렉터리, 파일 시스템을 기준으로 작업한다.

> "Claude Code는 터미널에서 작동하며"  
> 출처: Anthropic Claude Code overview

## 역할 분리

| 구성요소                   | 역할                                  | 실제 실행 위치              |
| ---------------------- | ----------------------------------- | --------------------- |
| iPhone                 | 입력 장치, 원격 터미널 조작, 상태 확인             | 모바일                   |
| SSH/Tailscale/원격 접속 계층 | 모바일과 집 머신 사이의 안전한 통로                | 양쪽 장치 사이              |
| 집 노트북 또는 홈서버           | shell, Claude Code, Git, Node.js 실행 | 집 머신                  |
| Claude Code            | 프로젝트를 읽고 명령을 수행하는 코딩 에이전트           | 집 머신                  |
| Obsidian vault         | Claude Code가 읽고 쓰는 실제 파일            | 집 머신의 디스크 또는 동기화된 저장소 |

## 사용자가 보는 흐름

사용자는 iPhone에서 명령을 입력하지만, 그 명령은 원격 접속 계층을 지나 집 머신의 shell로 전달된다. 그 shell에서 `claude`가 실행되면 Claude Code는 집 머신의 현재 작업 디렉터리를 기준으로 파일을 읽고 쓰며, 필요한 경우 테스트나 Git 명령도 그 머신에서 실행한다.

따라서 "모바일에서 Claude Code를 사용한다"는 표현은 실행 위치를 생략한 말이다. 실무적으로는 "모바일에서 집 머신의 Claude Code 세션을 원격 조작한다"가 더 정확하다.

## 중요한 구분

- 모바일은 입력과 화면 표시를 담당한다.
- 집 머신은 인증된 shell session과 Claude Code process를 담당한다.
- 파일 변경은 집 머신의 vault 또는 repo에서 발생한다.
- 네트워크가 끊기면 모바일 화면은 끊길 수 있지만, session manager 사용 여부에 따라 집 머신의 작업은 계속될 수도 있고 종료될 수도 있다.
- Claude 모바일 앱과 Claude Code 원격 실행은 같은 것이 아니다. Claude Code를 로컬 파일에 접근시키려면 실행 호스트의 터미널에서 Claude Code가 돌아야 한다.

## 이번 Topic에서의 1차 가정

1차 실험은 현재 Windows 노트북을 실행 호스트로 두고, iPhone은 원격 조작 클라이언트로 둔다. 맥미니 또는 맥 스튜디오는 후속 도입 후보로 비교하되, M1에서는 실행 구조를 이해하는 수준으로만 다룬다.

## 참조

- Anthropic Claude Code overview: https://docs.anthropic.com/ko/docs/claude-code/overview
- Anthropic Claude Code setup: https://docs.anthropic.com/en/docs/claude-code/getting-started
- Anthropic Claude Code CLI reference: https://docs.anthropic.com/en/docs/claude-code/cli-usage
