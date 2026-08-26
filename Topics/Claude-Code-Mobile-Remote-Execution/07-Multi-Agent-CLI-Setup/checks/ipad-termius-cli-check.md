# iPad Termius CLI 검증 결과

## 검증 목적

M7의 목적은 iPad Termius에서 하나의 Windows OpenSSH 서버(`catchupai` 계정)에 접속한 뒤 Claude Code, Codex CLI, Gemini CLI를 모두 사용할 수 있는지 확인하는 것이다. 이 검증은 모바일 원격 실행 구조가 특정 AI CLI 하나에만 묶이지 않고, 여러 CLI 작업 도구로 확장 가능한지 판단하기 위한 마지막 확인 단계다.

## 검증 결과

| 항목 | 결과 | 근거 |
|---|---|---|
| Claude Code | 사용 가능 | M4에서 iPhone/iPad Termius + Tailscale + Windows OpenSSH + `catchupai` 세션으로 검증 |
| Codex CLI | 사용 가능 | 사용자 보고: iPad Termius의 `catchupai` 세션에서 Codex 사용 가능 확인 |
| Gemini CLI | 사용 가능 | 사용자 보고: iPad Termius의 `catchupai` 세션에서 Gemini 사용 가능 확인 |
| Codex 인증 | 완료 | `dougg` 기준 `codex login status`가 `Logged in using ChatGPT`; OpenAI 계정은 `douggy.park@yahoo.com` |
| Gemini 인증 | 완료 | API key 방식으로 실행 확인; 키 값은 문서화하지 않음 |

## 확인 중 발견한 시행착오

### Codex Extension과 Codex CLI는 별도

처음에는 VS Code에 Codex Extension이 설치되어 있었지만 PowerShell에서 `codex` 명령을 인식하지 못했다. `where.exe codex`가 `Could not find files`를 반환했고, 이는 CLI가 Windows 환경에 별도 설치되지 않았다는 뜻이었다. 해결은 `npm install -g @openai/codex`로 CLI를 설치하고, `codex login`으로 로그인하는 방식이었다.

### PowerShell의 `where`와 `where.exe`

PowerShell에서 `where codex`는 기대한 Windows 실행 파일 검색과 다르게 동작할 수 있다. Windows 실행 파일 위치 확인은 `where.exe codex` 또는 `Get-Command codex`를 사용하는 것이 정확하다.

### Windows 사용자별 CLI 설치 차이

`dougg` 계정에서 npm global CLI가 설치된 경로는 `C:\Users\dougg\AppData\Roaming\npm`이었다. `catchupai`는 별도 Windows 사용자이므로 같은 CLI를 다시 설치하거나 해당 사용자 PATH를 별도로 구성해야 한다.

### Codex 로그인 명령 변경

`codex --login`은 현재 CLI에서 유효하지 않았다. 현재 방식은 `codex login`이며, SSH/headless 환경에서는 `codex login --device-auth`가 더 적합하다.

### Gemini는 API key 방식이 안정적

Gemini는 SSH/headless 환경에서 브라우저 기반 Google 로그인보다 API key 방식이 더 안정적이었다. API key는 Google AI Studio에서 발급하고 `GEMINI_API_KEY` 사용자 환경변수로 설정한다. API key 값은 절대 문서, GitHub, 영상 녹화에 남기지 않는다.

### Termius 테마 문제

Gemini 실행 후 배경색과 display text 색이 비슷해서 글자가 잘 보이지 않았다. 이는 Gemini 기능 문제가 아니라 Termius 테마/터미널 색상 문제다. Dark 계열 테마로 변경하거나 임시로 `NO_COLOR=1`을 적용하는 방식이 우회책이다.

## 다음 검증 때 사용할 명령

```bat
cd C:\AI_study\2026\Changsoo_Vault\Ingest\CatchUpAI_VL
whoami
hostname
claude --version
where.exe codex
codex --version
codex login status
where.exe gemini
gemini --version
gemini
```

## 결론

M7의 핵심 검증은 통과했다. 이제 iPad Termius는 단순 SSH 클라이언트가 아니라 Claude Code, Codex CLI, Gemini CLI를 모두 실행할 수 있는 모바일 원격 작업 콘솔로 사용할 수 있다.
