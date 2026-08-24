# M5 - 보안, 운영, 백업 가이드 정리

## 목적

M4에서 검증한 `iPhone -> Tailscale -> Windows OpenSSH Server -> catchupai -> Claude Code -> local vault` 구조를 장기 운영 가능한 형태로 정리한다. 이 모듈은 새 설정을 바로 적용하는 단계가 아니라, 운영 규칙과 변경 후보를 문서화하는 단계다.

## 현재 운영 구조

| 계층 | 현재 값 | 운영 판단 |
|---|---|---|
| 모바일 클라이언트 | iPhone + Termius | 1차 실험 성공 |
| 사설망 | Tailscale tailnet | 공개 포트 없이 접근 |
| 실행 호스트 | Windows 노트북 `Changsoo` | 현재 1차 실행 서버 |
| SSH 계정 | `catchupai` 표준 로컬 사용자 | 기존 관리자 계정과 분리 |
| 인증 방식 | Password | 단기 실험 가능, 장기 운영 전 SSH key 검토 |
| Claude Code | `catchupai` 계정에 설치, `2.1.241` | 원격 실행 가능 |
| 작업 대상 | `Changsoo_Vault` | 작업 전후 Git/파일 상태 확인 필요 |

## 산출물

| 파일 | 역할 |
|---|---|
| `guides/security-checklist.md` | Tailscale, OpenSSH, Windows 계정, Claude Code 보안 기준 |
| `guides/remote-work-runbook.md` | 원격 작업 전/중/후 운영 절차 |
| `guides/github-push-and-local-review.md` | GitHub 계정 고정 push와 push 없는 결과 확인 방법 |
| `guides/github-push-video-lessons.md` | GitHub push 설정 실수와 영상화 포인트 |
| `guides/mobile-client-setup-lessons.md` | iPad 추가 설정 실수와 Tailscale/Termius 역할 구분 영상 노트 |
| `guides/ipad-korean-input-lessons.md` | iPad Termius Claude Code 한글 입력 자모 분리 문제와 우회 방법 |
| `guides/home-server-operations.md` | 맥미니/맥 스튜디오 홈서버 도입 시 운영 체크리스트 |
| `troubleshooting/recovery-playbook.md` | 접속 실패, 인증 실패, 절전, PATH, vault 문제 복구 절차 |

## 운영 원칙

1. 공개 인터넷에 SSH 포트를 열지 않는다.
2. SSH는 Tailscale 사설망 안에서만 허용한다.
3. 원격 작업은 `catchupai` 같은 전용 표준 계정으로 시작한다.
4. vault 작업 전후에는 현재 경로와 변경 파일을 확인한다.
5. 장기 운영 전에는 password 인증에서 SSH key 인증으로 전환하는 것을 우선 검토한다.
6. 맥미니/맥 스튜디오 서버 도입은 “상시 실행 안정성”을 얻는 대신 운영 책임이 늘어난다는 점을 전제로 판단한다.

## 이전/다음 모듈

- 이전 모듈: [04-Remote-Execution-Lab/](../04-Remote-Execution-Lab/README.md)
- 다음 모듈: [06-Publishing-Video-Plan/](../06-Publishing-Video-Plan/README.md)

