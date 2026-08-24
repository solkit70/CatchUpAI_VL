# WorkLog - M4: 모바일 원격 실행 1차 실험 설계 및 수행

**날짜**: 2026-08-23
**Topic**: Claude-Code-Mobile-Remote-Execution
**모듈**: M4 - 모바일 원격 실행 1차 실험 설계 및 수행
**학습 시간**: 약 2.5시간

## 오늘의 학습 목표

- [x] 모바일에서 집 노트북 터미널에 접근하는 1차 실험을 설계한다.
- [ ] Claude Code를 원격 세션에서 실행하고 간단한 vault 작업을 수행한다.
- [ ] 명령 실행 위치와 파일 변경 결과를 검증한다.
- [ ] 접속 끊김, 절전, 권한 문제를 관찰하고 기록한다.

## 진행 내용

### 1. Pre-M4 준비 상태 확인

서버 쪽 준비는 완료된 상태에서 M4를 시작했다.

| 항목 | 값 |
|---|---|
| Windows 사용자 | `dougg` |
| Windows whoami | `changsoo\dougg` |
| Hostname | `Changsoo` |
| Tailscale IPv4 | `100.109.17.103` |
| OpenSSH Server | `sshd` running, automatic |
| Tailscale service | running, automatic |

### 2. 실험 산출물 생성

M4 실험 절차와 기록 파일을 생성했다.

### 4. SSH 전용 로컬 사용자 생성

기존 `dougg` 계정 비밀번호를 사용하지 않기 위해 사용자가 Windows 설정 앱에서 로컬 계정 `catchupai`를 직접 생성했다. Codex는 비밀번호를 알지 않으며, 계정 상태만 확인했다.

| 확인 | 결과 |
|---|---|
| Local user | `catchupai` |
| Enabled | `True` |
| Group | `Users` |
| Account type | Standard local user |
### 5. iPhone Termius SSH 접속 성공

사용자가 iPhone Termius에서 Tailscale IP `100.109.17.103`로 접속했고, `catchupai@CHANGSOO C:\Users\catchupai>` 프롬프트를 확인했다. 최초에는 username이 `catchupat`로 잘못 입력되어 인증 실패가 발생했으나, `catchupai`로 수정 후 접속에 성공했다.
### 6. 실행 위치 검증 성공 및 Claude Code 미설치 확인

Termius SSH 세션에서 `hostname`, `whoami`, `cd`를 실행해 실제 명령이 Windows 노트북 `Changsoo`의 `catchupai` 계정에서 실행되는 것을 확인했다. `where claude`와 `claude --version`은 실패했으며, 이는 Claude Code가 기존 `dougg` 계정에는 설치되어 있지만 새 SSH 전용 계정 `catchupai`에는 아직 설치되어 있지 않기 때문이다.

| 명령 | 결과 |
|---|---|
| `hostname` | `Changsoo` |
| `whoami` | `changsoo\catchupai` |
| `cd` | `C:\Users\catchupai` |
| `where claude` | Could not find files |
| `claude --version` | not recognized |
### 7. catchupai 계정 Claude Code 설치 및 PATH 해결

사용자가 Termius SSH 세션에서 `catchupai` 계정에 Claude Code를 설치했다. 설치 위치는 `C:\Users\catchupai\.local\bin\claude.exe`였고, 직접 경로 실행은 성공했다. 이후 PATH에 `C:\Users\catchupai\.local\bin`을 추가하고 재접속하자 `claude --version`이 `2.1.241`로 출력되었다.
### 8. 파일 변경 위치 검증 완료

사용자가 iPhone Termius SSH 세션에서 M4 lab 폴더로 이동해 `m4-remote-write-test.txt`를 생성했다. Codex가 같은 vault 경로에서 `Get-Content`로 파일을 읽어 모바일에서 실행한 파일 변경이 실제 Windows 노트북 파일 시스템에 반영되었음을 확인했다.

| 항목 | 결과 |
|---|---|
| 생성 파일 | `04-Remote-Execution-Lab/lab/m4-remote-write-test.txt` |
| 파일 내용 | `M4 remote write test from iPhone SSH` |
| 검증 방식 | iPhone에서 생성 후 노트북 쪽 Codex 세션에서 읽기 |
## 문제 해결 로그

### 문제 1: OpenSSH Server 설치 중복 큐

**상태**: Pre-M4에서 해결 완료

**요약**: Windows Optional Feature에서 OpenSSH Server가 중복으로 세 번 추가되어 설치가 지연되었다. 중복된 두 항목을 취소하고 하나만 남겨 설치를 완료했다.

## DoD 체크리스트

- [x] 실험 절차서 작성
- [x] 사용자 승인 후 원격 접속 방식 적용
- [x] 모바일에서 집 머신 터미널 접근 확인
- [x] Claude Code 또는 안전한 shell 작업 실행 확인
- [x] 파일 변경 위치 검증
- [x] 실패/복구 로그 작성
- [x] README.md와 WorkLog 작성

**완료율**: 7/7

## Daily Retrospective

### What went well

- Tailscale + Windows OpenSSH Server + Termius 구조로 iPhone에서 집 노트북에 접속하는 흐름을 완성했다.
- hostname, whoami, cd로 실행 위치를 명확히 검증했다.
- catchupai 전용 계정에서 Claude Code를 설치하고 PATH 문제까지 해결했다.
- 모바일에서 만든 파일을 노트북 vault에서 다시 읽어 파일 변경 위치를 확인했다.

### What could be improved

- 초기 Termius username 오타와 Claude Code PATH 문제처럼 입력/환경변수 실수가 생기기 쉬우므로 M5 운영 런북에 체크리스트로 정리해야 한다.
- 현재는 password 인증 기반이므로, 장기 운영 전에는 SSH key 인증 전환 여부를 검토해야 한다.

### Insights

- 모바일 Claude Code 원격 실행 구조의 본질은 모바일 앱이 아니라 안전한 원격 터미널 경로와 실행 호스트 준비성이다.
- 새 SSH 전용 계정은 보안상 좋지만, 기존 사용자 계정의 개발 도구가 자동으로 공유되지 않으므로 별도 설치와 PATH 구성이 필요하다.

### Tomorrow's focus

- M5에서 보안, 운영, 백업, 절전, SSH key 전환, 계정 권한, 원격 작업 전후 체크리스트를 런북으로 정리한다.

## 참조 및 산출물

**생성된 파일/폴더**:
- `04-Remote-Execution-Lab/README.md`
- `04-Remote-Execution-Lab/lab/experiment-plan.md`
- `04-Remote-Execution-Lab/lab/mobile-ssh-claude-code-test.md`
- `04-Remote-Execution-Lab/lab/validation-results.md`
- `04-Remote-Execution-Lab/troubleshooting/remote-session-issues.md`
- `vl_worklog/20260823_M4_Claude-Code-Mobile-Remote-Execution.md`

**작성자**: Codex
**방법론**: VibeLearn AI






