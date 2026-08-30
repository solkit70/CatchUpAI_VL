# 전체 산출물 정리와 최종 추천 구조

## 학습 순서대로 정리한 전체 산출물

### M1 — 실행 구조 이해와 첫 모델링
- [01-Execution-Model/concepts/mobile-to-local-execution.md](../../01-Execution-Model/concepts/mobile-to-local-execution.md) — 모바일 조작과 로컬 실행의 역할 분리
- [01-Execution-Model/concepts/command-file-session-flow.md](../../01-Execution-Model/concepts/command-file-session-flow.md) — 명령/파일/인증/세션 흐름
- [01-Execution-Model/diagrams/execution-flow.md](../../01-Execution-Model/diagrams/execution-flow.md) — 전체 실행 흐름 다이어그램

### M2 — 기술 구조 비교와 홈서버 옵션 평가
- [02-Architecture-Comparison/concepts/remote-architecture-patterns.md](../../02-Architecture-Comparison/concepts/remote-architecture-patterns.md) — 원격 실행 구조 패턴
- [02-Architecture-Comparison/comparisons/structure-comparison-table.md](../../02-Architecture-Comparison/comparisons/structure-comparison-table.md) — 기술 구조 비교표
- [02-Architecture-Comparison/comparisons/mac-mini-vs-mac-studio-server.md](../../02-Architecture-Comparison/comparisons/mac-mini-vs-mac-studio-server.md) — 맥미니/맥 스튜디오 비교
- [02-Architecture-Comparison/decisions/recommended-first-experiment.md](../../02-Architecture-Comparison/decisions/recommended-first-experiment.md) — 1차 실험 추천안 결정

### M3 — 현재 Windows 노트북 환경 점검
- [03-Environment-Audit/audit/windows-host-readiness.md](../../03-Environment-Audit/audit/windows-host-readiness.md) — 로컬 도구 상태 점검
- [03-Environment-Audit/audit/vault-safety-checklist.md](../../03-Environment-Audit/audit/vault-safety-checklist.md) — vault 작업 경계
- [03-Environment-Audit/decisions/preflight-go-no-go.md](../../03-Environment-Audit/decisions/preflight-go-no-go.md) — M4 진행 전 Go/No-Go 기준

### M4 — 모바일 원격 실행 1차 실험 설계 및 수행
- [04-Remote-Execution-Lab/lab/experiment-plan.md](../../04-Remote-Execution-Lab/lab/experiment-plan.md) — 실험 절차서
- [04-Remote-Execution-Lab/lab/mobile-ssh-claude-code-test.md](../../04-Remote-Execution-Lab/lab/mobile-ssh-claude-code-test.md) — iPhone SSH 접속/실행 기록
- [04-Remote-Execution-Lab/lab/validation-results.md](../../04-Remote-Execution-Lab/lab/validation-results.md) — 실행 위치·파일 변경 검증 결과
- [04-Remote-Execution-Lab/troubleshooting/remote-session-issues.md](../../04-Remote-Execution-Lab/troubleshooting/remote-session-issues.md) — 접속/세션 문제 로그

### M5 — 보안, 운영, 백업 가이드 정리
- [05-Operations-Security/guides/security-checklist.md](../../05-Operations-Security/guides/security-checklist.md) — 보안 체크리스트
- [05-Operations-Security/guides/remote-work-runbook.md](../../05-Operations-Security/guides/remote-work-runbook.md) — 원격 작업 운영 런북
- [05-Operations-Security/guides/github-push-and-local-review.md](../../05-Operations-Security/guides/github-push-and-local-review.md) — GitHub push 계정 고정과 결과 확인 방법
- [05-Operations-Security/guides/home-server-operations.md](../../05-Operations-Security/guides/home-server-operations.md) — 맥미니/맥 스튜디오 운영 체크리스트
- [05-Operations-Security/troubleshooting/recovery-playbook.md](../../05-Operations-Security/troubleshooting/recovery-playbook.md) — 복구 플레이북
- [05-Operations-Security/guides/mobile-client-setup-lessons.md](../../05-Operations-Security/guides/mobile-client-setup-lessons.md) — iPad 클라이언트 설정 실수 (영상화 사례 1)
- [05-Operations-Security/guides/github-push-video-lessons.md](../../05-Operations-Security/guides/github-push-video-lessons.md) — GitHub push 설정 실수 (영상화 사례 2)
- [05-Operations-Security/guides/ipad-korean-input-lessons.md](../../05-Operations-Security/guides/ipad-korean-input-lessons.md) — iPad 한글 IME 자모 분리 문제 (영상화 사례 3)

### M8 — 네이티브 Remote Control 검증과 구조 비교 (2026-08-28 추가)

- [08-Native-Remote-Control/README.md](../../08-Native-Remote-Control/README.md) — 모듈 요약과 결론
- [08-Native-Remote-Control/concepts/native-remote-control-model.md](../../08-Native-Remote-Control/concepts/native-remote-control-model.md) — 연결 구조와 요건
- [08-Native-Remote-Control/lab/remote-control-verification.md](../../08-Native-Remote-Control/lab/remote-control-verification.md) — 실측과 경계 테스트
- [08-Native-Remote-Control/comparisons/ssh-vs-native-remote-control.md](../../08-Native-Remote-Control/comparisons/ssh-vs-native-remote-control.md) — 두 방식 비교
- [08-Native-Remote-Control/decisions/which-path-when.md](../../08-Native-Remote-Control/decisions/which-path-when.md) — 상황별 선택 기준

### M9 — Codex Remote 검증과 세팅 (2026-08-30 추가)

- [09-Codex-Remote/README.md](../../09-Codex-Remote/README.md) — 모듈 요약과 현재 상태
- [09-Codex-Remote/lab/setup-procedure.md](../../09-Codex-Remote/lab/setup-procedure.md) — 설치, iPad 연결, 읽기 테스트 기록
- [09-Codex-Remote/decisions/codex-remote-usage-rules.md](../../09-Codex-Remote/decisions/codex-remote-usage-rules.md) — Codex Remote 운용 규칙
- [vl_worklog/20260830_M9_Claude-Code-Mobile-Remote-Execution.md](../../vl_worklog/20260830_M9_Claude-Code-Mobile-Remote-Execution.md) — Classic 앱 혼선부터 iPad 연결 성공까지의 실제 문제 해결 기록

> ⚠️ **아래 "최종 추천 구조"는 M7 시점 기준이다.** M8에서 Claude Code 네이티브 Remote Control을 확인했고, M9에서 Codex도 새 ChatGPT Desktop/Codex 앱을 통해 iPad Remote 연결이 가능함을 확인했다. SSH 구조는 Gemini 실행, 임의 셸 작업, 계정 격리, 홈서버, 세밀한 운영 통제 용도로 여전히 유효하다. Claude는 Claude Remote Control, Codex는 Codex Remote, 범용 셸은 SSH로 구분해 선택한다.

## 최종 추천 구조

```text
iPhone / iPad (Termius)
  -> Tailscale private network
  -> Windows laptop "Changsoo" (Windows OpenSSH Server)
  -> catchupai local account
  -> Claude Code 2.1.241
  -> C:\AI_study\2026\Changsoo_Vault
```

이 구조는 M2에서 후보로 선정되었고, M4에서 iPhone 기준으로 실제 접속·실행·파일 변경까지 검증되었으며, M5에서 보안/운영 규칙까지 문서화되어 **1차 실험 목표를 완전히 달성**했다. 공개 포트를 열지 않고, 전용 계정(`catchupai`)으로 권한을 분리했으며, 작업 전후 `git status` 확인을 운영 규칙으로 고정했다.

### 왜 이 구조가 최종 추천인가

1. **구매 없이 검증 가능** — 현재 보유한 Windows 노트북만으로 전체 흐름(모바일 조작 → 원격 실행 → 파일 변경 → GitHub push)을 실제로 완결했다.
2. **공격 표면 최소화** — Tailscale 사설망 안에서만 SSH를 열어 공개 인터넷 노출이 없다.
3. **역할 분리 검증됨** — M1에서 정의한 "모바일은 조작, 로컬 머신은 실행"이라는 모델이 M4 실측 결과와 정확히 일치했다(명령 실행 위치, 파일 생성 위치를 모두 노트북에서 교차 확인).
4. **재현 가능한 실패 사례 확보** — iPad Tailscale 미설치, GitHub 계정 두 개, 한글 IME 문제 등 실제로 겪은 실패가 그대로 운영 가이드와 영상 소재가 되었다.

### 맥미니/맥 스튜디오 홈서버 판단

M2 결론을 유지한다: 맥미니/맥 스튜디오는 **지금 구매할 대상이 아니라, 상시 실행 호스트가 실제로 필요해졌을 때 재검토할 2차 후보**다. 현재 노트북 기반 구조가 이미 목표(모바일 원격 Claude Code 실행)를 충족하므로, 아래 조건 중 하나가 발생하기 전까지는 노트북 구조를 유지한다.

- 노트북을 상시 켜두는 것이 생활/업무에 지장을 줄 때
- 노트북 절전/이동으로 인한 접속 끊김이 반복될 때
- Remotion 렌더링처럼 상시 고부하 작업을 서버에 맡길 필요가 생길 때 (이 경우 맥 스튜디오까지 재검토)

### 인증 방식 판단

Password 인증은 1차 실험 단계에서는 허용 가능했지만(Tailscale 사설망 안에서만 노출), 장기 운영 전에는 Windows OpenSSH 로그인용 SSH key 인증으로 전환하는 것을 최종 추천안으로 유지한다. 이는 이미 완료한 GitHub push용 SSH key 설정과 별도이며, 자세한 근거는 [security-checklist.md](../../05-Operations-Security/guides/security-checklist.md)를 참조.

## 완료 조건 충족

현재 추천 구조는 Claude Code 기준 SSH 검증에 더해 iPad Termius에서 Codex/Gemini CLI 실행 가능 여부를 확인했고, 이후 Claude Remote Control과 Codex Remote까지 추가 검증했다. M9에서는 새 ChatGPT Desktop/Codex 앱에서 iPad Remote 연결, 현재 위치 구조 읽기, 최소 파일 쓰기 테스트가 성공했다. 남은 범위는 푸시 알림, 잠자기 복구 확인, 운용 규칙 최종 확정, Remotion 영상 제작 전 보안 검토다.

## 참조

- [M2 1차 실험 추천안](../../02-Architecture-Comparison/decisions/recommended-first-experiment.md)
- [M4 검증 결과](../../04-Remote-Execution-Lab/lab/validation-results.md)
- [M5 운영 구조 요약](../../05-Operations-Security/README.md)






