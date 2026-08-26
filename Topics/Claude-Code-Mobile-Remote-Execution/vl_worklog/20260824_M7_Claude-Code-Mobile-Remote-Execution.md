# WorkLog - M7: iPad Termius에서 Codex/Gemini CLI 세팅 검증

**날짜**: 2026-08-24  
**Topic**: Claude-Code-Mobile-Remote-Execution  
**모듈**: M7 - iPad Termius에서 Codex/Gemini CLI 세팅 검증  
**작성자**: Codex with VibeLearn AI

## 오늘의 학습 목표

- iPad Termius의 `catchupai` SSH 세션에서 Codex CLI 실행 가능 여부를 확인한다.
- iPad Termius의 `catchupai` SSH 세션에서 Gemini CLI 실행 가능 여부를 확인한다.
- Claude Code, Codex, Gemini를 동시에 열 때의 운영 규칙을 정리한다.
- Topic 완료 조건을 M7 검증 이후 상태로 갱신한다.

## 진행 내용

### 1. Codex CLI 상태 확인

`dougg` Windows 사용자에서는 처음에 VS Code Extension만 설치되어 있었고 PowerShell에서 `codex` 명령을 인식하지 못했다. `npm install -g @openai/codex`로 CLI를 별도 설치한 뒤 `codex --version`에서 `codex-cli 0.149.1`을 확인했고, `codex login`으로 ChatGPT 로그인까지 완료했다. OpenAI/ChatGPT 계정은 `douggy.park@yahoo.com` 기준으로 정리했다.

### 2. `catchupai` 세션 확장

`catchupai`는 별도 Windows 사용자이므로 `dougg`의 npm global 설치와 인증이 자동으로 공유되지 않는다. Termius의 `catchupai` SSH 세션에서도 Codex와 Gemini를 사용할 수 있게 세팅했고, 사용자가 두 CLI 모두 실행 가능하다고 확인했다.

### 3. Gemini API key 방식 확인

Gemini는 SSH/headless 환경에서 API key 방식으로 접속하는 것이 적합했다. Google AI Studio에서 API key를 발급하고 `GEMINI_API_KEY` 환경변수로 사용하는 흐름을 정리했다. API key 값은 문서화하지 않았고, 영상 녹화에서도 노출 금지 대상으로 분리했다.

### 4. Termius 화면 가독성 문제 기록

Gemini 실행 후 Termius 배경색과 display text 색이 비슷해 글자가 잘 보이지 않는 문제가 있었다. Termius 테마를 Dark 계열로 바꾸거나 `NO_COLOR=1`을 사용하는 우회 방법을 기록했다.

### 5. 병행 사용 규칙 작성

`guides/multi-cli-session-rules.md`에 Claude Code, Codex, Gemini를 동시에 열 때의 기본 규칙을 작성했다. 핵심 원칙은 동시에 여러 CLI를 열 수는 있지만 같은 파일을 동시에 수정하지 않는 것이다.

## 문제 해결 로그

| 문제 | 원인 | 해결/기록 |
|---|---|---|
| `codex` 명령 미인식 | VS Code Extension과 CLI는 별도 | npm global로 `@openai/codex` 설치 |
| `codex --login` 실패 | 현재 CLI는 subcommand 방식 | `codex login` 사용 |
| `where codex` 출력 없음 | PowerShell `where` 사용 혼동 | `where.exe codex`, `Get-Command codex` 사용 |
| Gemini SSH 인증 | 브라우저 OAuth보다 API key 방식이 안정적 | `GEMINI_API_KEY` 환경변수 사용 |
| Gemini 화면 글자 가독성 | Termius 테마 색상 충돌 | Dark 테마 또는 `NO_COLOR=1` |

## DoD 체크리스트

- [x] iPad Termius에서 Codex 실행 가능 여부 기록
- [x] iPad Termius에서 Gemini 실행 가능 여부 기록
- [x] 미설치/미인식 시 원인과 다음 조치 기록
- [x] Claude/Codex/Gemini 병행 사용 규칙 작성
- [x] Topic 완료 조건을 M7 검증 이후로 갱신
- [x] WorkLog 작성

**완료율**: 6/6

## Module Retrospective - M7

### 학습 목표 달성도

- [x] iPad Termius의 새 SSH 탭에서 Codex CLI 설치/인식 여부를 확인한다.
- [x] iPad Termius의 새 SSH 탭에서 Gemini CLI 설치/인식 여부를 확인한다.
- [x] Claude Code, Codex, Gemini를 동시에 열 때의 세션/작업 디렉터리/파일 충돌 위험을 정리한다.
- [x] Codex/Gemini 미설치 또는 PATH 미등록 상태에서 다음 조치 기준을 만든다.

### 핵심 인사이트

1. 모바일 원격 실행 구조의 핵심은 특정 AI CLI가 아니라 SSH 접속 계층이다. Claude Code가 되는 구조라면 Codex/Gemini도 계정별 설치와 인증만 맞추면 같은 방식으로 확장할 수 있다.
2. Windows에서는 사용자 계정 경계가 중요하다. `dougg`에서 설치한 CLI, PATH, 로그인 상태가 `catchupai`로 자동 공유되지 않는다.
3. 영상에서는 성공 장면보다 시행착오가 더 교육적이다. VS Code Extension과 CLI 차이, PowerShell `where` 혼동, Codex login 명령 변경, Gemini API key 방식, Termius 색상 문제는 모두 실제 학습자가 겪을 수 있는 포인트다.

### 다음 단계

M7 완료로 Topic의 기술 검증 범위는 충족했다. 다음 단계는 Topic Retrospective 최종 정리와 Remotion 영상 제작 착수 여부 승인이다.

## Topic Retrospective - Claude-Code-Mobile-Remote-Execution

### 전체 학습 목표 달성도

- [x] 모바일에서 Claude Code를 조작하는 구조를 이해한다.
- [x] 명령이 집/로컬 노트북에서 실행되는 방식을 파악한다.
- [x] 가능한 구조를 비교하고 내 환경에 맞는 1차 실험 구조를 선택한다.
- [x] 현재 Windows 노트북에서 모바일 원격 접속 기반 Claude Code 실행 실험을 완료할 수 있다.
- [x] 맥미니/맥 스튜디오 홈서버 도입 시 필요한 장비, 운영 방식, 보안/백업 전략을 설계할 수 있다.
- [x] 최종 운영 가이드와 영상화 가능한 스토리라인을 만들 수 있다.
- [x] iPad Termius에서 Claude Code, Codex, Gemini를 각각 실행 가능한 모바일 AI CLI 작업 환경으로 검증한다.

### 가장 중요한 성과

모바일 기기는 작업이 실행되는 컴퓨터가 아니라 조작 콘솔이라는 점을 실제로 확인했다. iPad Termius에서 보낸 명령은 Tailscale 사설망을 통해 Windows 노트북의 OpenSSH 서버로 들어가고, 실제 파일 변경과 CLI 실행은 `catchupai` Windows 사용자 환경에서 일어난다. 이 구조를 Claude Code뿐 아니라 Codex와 Gemini까지 확장해 확인했기 때문에, 이제 이 Topic은 단일 도구 실험이 아니라 모바일 원격 AI 작업 구조 실험으로 완결되었다.

### 후속 과제

- Windows OpenSSH 로그인용 SSH key 전환
- Tailscale MFA/ACL/Grants 점검
- 영상 공개 전 IP, 계정명, 이메일, API key, private key 노출 검토
- Remotion 영상 제작용 스크린샷/녹화 자료 정리

### 영상화 판단

영상화 진행 가치가 있다. 실제 실패 사례가 충분하고, 시청자가 따라 하면서 겪을 수 있는 문제들이 명확히 문서화되었다. 다만 영상 제작 전에는 Go/No-Go 체크리스트의 보안 항목과 사용자 최종 승인을 다시 확인한다.
