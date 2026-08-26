# M7 - iPad Termius에서 Codex/Gemini CLI 세팅 검증

## 요약

M7은 기존 Claude Code 모바일 원격 실행 구조가 다른 AI CLI에도 확장되는지 확인하는 모듈이다. iPad Termius에서 `catchupai` Windows SSH 계정으로 접속한 뒤 Claude Code뿐 아니라 Codex CLI와 Gemini CLI도 실행 가능한 상태까지 확인했다.

## 최종 상태

| CLI | iPad Termius `catchupai` 세션 실행 | 인증 방식 | 계정/키 기준 | 비고 |
|---|---:|---|---|---|
| Claude Code | 확인 | Claude 로그인 | `solkit70@gmail.com` | 기존 M4에서 검증 |
| Codex CLI | 확인 | ChatGPT 로그인 | `douggy.park@yahoo.com` | VS Code Extension과 CLI는 별도 설치 필요 |
| Gemini CLI | 확인 | API key | `GEMINI_API_KEY` | SSH/headless 환경에서는 API key 방식이 안정적 |

## 핵심 학습

1. VS Code Extension 설치와 CLI 설치는 별개다. `codex` VS Code Extension이 있어도 PowerShell/SSH 세션에서 `codex` 명령이 생기지는 않는다.
2. Windows 사용자가 다르면 npm global 설치 경로와 로그인 정보가 다르다. `dougg`에서 되는 CLI가 `catchupai`에서 자동으로 되는 것은 아니다.
3. Codex는 CLI 설치 후 `codex login` 또는 SSH 환경에서는 `codex login --device-auth`로 로그인한다. 현재 OpenAI 계정은 `douggy.park@yahoo.com` 기준으로 정리했다.
4. Gemini는 SSH/headless 환경에서 Google OAuth보다 API key 방식이 더 안정적이다. API key는 Google AI Studio에서 발급하고 `GEMINI_API_KEY` 사용자 환경변수로 설정한다.
5. Termius 테마에 따라 Gemini 출력 글자가 배경과 비슷하게 보여 읽기 어려울 수 있다. Dark 계열 테마 변경 또는 `NO_COLOR=1`이 실무 우회 방법이다.

## 산출물

- [checks/ipad-termius-cli-check.md](checks/ipad-termius-cli-check.md)
- [guides/multi-cli-session-rules.md](guides/multi-cli-session-rules.md)

## 이전/다음

- 이전 모듈: [../06-Publishing-Video-Plan/README.md](../06-Publishing-Video-Plan/README.md)
- 다음 단계: Topic Retrospective 최종 고정 후 Remotion 영상 작업 검토
