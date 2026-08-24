# WorkLog - M5: 보안, 운영, 백업 가이드 정리

**날짜**: 2026-08-24
**Topic**: Claude-Code-Mobile-Remote-Execution
**모듈**: M5 - 보안, 운영, 백업 가이드 정리
**학습 시간**: 약 1.5시간

## 오늘의 학습 목표

- [x] 원격 Claude Code 운영 시 지켜야 할 보안 규칙을 정리한다.
- [x] 절전, 네트워크, 세션, 백업, vault 동기화 운영 절차를 만든다.
- [x] 홈서버 도입 시 운영 체크리스트를 만든다.
- [x] 하지 말아야 할 위험한 운영 방식을 명시한다.

## 진행 내용

### 1. M4 결과 기반 운영 구조 정리

M4에서 성공한 구조를 기준으로 운영 문서를 작성했다.

| 계층 | 값 |
|---|---|
| 모바일 클라이언트 | iPhone + Termius |
| 사설망 | Tailscale |
| 실행 호스트 | Windows 노트북 `Changsoo` |
| SSH 계정 | `catchupai` |
| Claude Code | `2.1.241` |
| 작업 경로 | `C:\AI_study\2026\Changsoo_Vault` |

### 2. 보안 체크리스트 작성

Tailscale, Windows OpenSSH, `catchupai` 계정, password 인증, SSH key 전환 후보를 기준으로 보안 체크리스트를 작성했다.

### 3. 원격 작업 운영 런북 작성

원격 작업 전/중/후 체크리스트를 작성했다. 특히 실행 위치 확인, vault 경로 확인, Git 상태 확인, 모바일에서 금지할 작업을 명시했다.

### 4. 홈서버 운영 체크리스트 작성

맥미니/맥 스튜디오를 홈서버로 도입할 경우의 운영 조건과 초기 세팅 순서를 정리했다.

### 5. 복구 플레이북 작성

Tailscale, SSH, 인증, Claude Code PATH, vault 경로, 절전/세션 끊김 문제를 계층별로 분리해 복구 절차를 작성했다.

### 6. GitHub push 계정 고정과 로컬 확인 방법 문서화

사용자는 GitHub 계정이 두 개 있고, Windows GUI 환경에서는 push 시 계정 선택 팝업이 뜬다. 모바일 SSH 환경에서는 이 팝업을 처리하기 어려우므로, 주 사용 계정 `solkit70` 기준으로 repo별 SSH alias를 고정하는 방식을 문서화했다. 또한 GitHub에 push하지 않고도 `git status`, `git diff`, Termius SFTP, 로컬 commit, Tailscale dev server로 결과를 확인하는 방법을 정리했다.
### 7. iPad 클라이언트 설정 실수와 영상화 포인트 정리

사용자가 iPad에 Termius만 설치한 상태에서 Host 접속을 시도했고 `connection timed out`이 발생했다. 원인은 iPad에 Tailscale이 설치/연결되어 있지 않았기 때문이다. 이 사례를 `mobile-client-setup-lessons.md`에 별도 정리해, M6 Remotion AI 영상화 후보에서 “네트워크 계층과 터미널 계층의 차이”를 설명하는 장면으로 활용할 수 있게 했다.
### 8. GitHub solkit70 SSH push 설정 완료

사용자가 `catchupai` 계정에서 생성한 public key를 GitHub `solkit70` 계정에 등록했다. 이후 origin remote를 `git@github-solkit70:solkit70/CatchUpAI_VL.git`로 변경했고, iPad Termius의 `catchupai` 세션에서 `git ls-remote origin HEAD`가 성공했다. `catchupai` 계정으로 `dougg` 소유 repo에 접근하면서 Git `dubious ownership` 보호가 발생했으나, 해당 repo를 `safe.directory`로 등록해 해결했다.

현재 작업 트리에는 이번 Topic 외의 변경도 있으므로, 모바일에서 push할 때는 `git add .`를 쓰지 않고 `Topics/Claude-Code-Mobile-Remote-Execution` 경로만 명시적으로 stage해야 한다.
### 9. GitHub push 설정 실수와 영상화 포인트 정리

GitHub 계정이 두 개인 환경에서 모바일 원격 push가 GUI 계정 선택 팝업에 의존하면 운영이 막힌다는 점을 별도 영상 노트로 정리했다. 실제 과정에서 HTTPS remote, SSH alias, Termius 자동 링크 변환, Git `dubious ownership`, `git add .` 위험이 모두 드러났으므로, 이 사례를 M6 영상 스토리라인에 반영할 수 있게 `github-push-video-lessons.md`로 정리했다.
### 10. iPad Claude Code 한글 입력 문제 정리

사용자가 iPad Termius에서 Claude Code를 실행한 뒤 한글 `프로세스`를 입력하자 `ㅍㅡㄹㅗㅅㅔㅅㅡ`처럼 자모가 분리되어 입력되는 문제를 발견했다. 영어 입력은 정상 동작했다. 이 문제는 iPadOS/Termius/Claude Code TUI의 IME composition 처리 문제로 보이며, 관련 GitHub issue도 확인했다. 우회 방법으로 영어 지시, 메모 앱에서 한글 작성 후 붙여넣기, 한글 지시 파일을 만들어 Claude Code가 읽게 하는 방식을 정리했다.
## 문제 해결 로그

### 문제 1: 장기 운영 전 password 인증 리스크

**증상**: 현재 구조는 password 기반 SSH 인증으로 동작한다.

**판단**: Tailscale 대역 안에서만 SSH가 열려 있고 `catchupai` 표준 계정을 사용하므로 단기 실험에는 허용 가능하다. 장기 운영 전에는 SSH key 전환을 우선 검토해야 한다.

**해결 방향**: M5 문서에 SSH key 전환 권장안을 별도 승인 필요 작업으로 분리했다.

## DoD 체크리스트

- [x] 보안 체크리스트 작성
- [x] 원격 작업 운영 런북 작성
- [x] 맥미니/맥 스튜디오 서버 운영 체크리스트 작성
- [x] 금지할 운영 방식 명시
- [x] 세션 끊김/절전/백업 문제 복구 절차 작성
- [x] README.md와 WorkLog 작성

**완료율**: 6/6

## Daily Retrospective

### What went well

- M4의 실제 실패 사례를 M5 운영 문서에 반영해 추상적인 보안 문서가 아니라 실사용 런북으로 만들었다.
- password 인증을 무조건 금지하지 않고, 현재 실험 단계와 장기 운영 단계를 분리해서 판단했다.
- 맥미니/맥 스튜디오 홈서버 도입을 구매 판단이 아니라 운영 책임 관점에서 정리했다.

### What could be improved

- SSH key 전환은 문서화만 했고 실제 적용은 하지 않았다. 장기 운영 전에 별도 승인 후 실습하는 것이 좋다.
- Tailscale ACL/Grants도 문서화만 했고 실제 tailnet 정책 변경은 하지 않았다.

### Insights

- 원격 Claude Code 운영의 핵심 위험은 Claude Code 자체보다 인증, 계정 권한, 작업 경로, 백업 상태다.
- 모바일 원격 작업은 작은 성공에는 매우 유용하지만, 대량 변경과 보안 설정 변경에는 적합하지 않다.

### Tomorrow's focus

- M6에서 최종 추천 구조, 후속 개선 과제, Remotion AI 영상화 후보를 정리한다.

## 참조 및 산출물

**생성된 파일/폴더**:
- `05-Operations-Security/README.md`
- `05-Operations-Security/guides/security-checklist.md`
- `05-Operations-Security/guides/remote-work-runbook.md`
- `05-Operations-Security/guides/github-push-and-local-review.md`
- `05-Operations-Security/guides/home-server-operations.md`
- `05-Operations-Security/troubleshooting/recovery-playbook.md`
- `vl_worklog/20260824_M5_Claude-Code-Mobile-Remote-Execution.md`

**참조**:
- Tailscale security best practices: https://tailscale.com/docs/reference/best-practices/security
- Tailscale access control: https://tailscale.com/docs/features/access-control
- Microsoft OpenSSH key management: https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_keymanagement
- Microsoft OpenSSH server configuration: https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh-server-configuration
- Microsoft Windows power settings: https://support.microsoft.com/en-us/windows/experience/power-battery/power-settings-in-windows-11

**작성자**: Codex
**방법론**: VibeLearn AI






