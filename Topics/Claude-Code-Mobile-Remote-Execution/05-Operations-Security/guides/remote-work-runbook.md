# 원격 작업 운영 런북

## 클라이언트 앱 역할 구분

모바일 또는 iPad에서 원격 작업을 하려면 Tailscale과 Termius가 모두 필요하다. 둘은 같은 역할이 아니다.

| 도구 | 설치 위치 | 역할 |
|---|---|---|
| Tailscale | iPhone, iPad, Windows 노트북 | 기기들을 같은 사설망에 넣고 `100.x.x.x` 주소로 통신하게 함 |
| Termius | iPhone, iPad | Tailscale 경로를 통해 Windows OpenSSH Server에 로그인하는 SSH 클라이언트 |
| OpenSSH Server | Windows 노트북 | Termius의 SSH 접속을 받아 shell 세션을 열어 줌 |
| Claude Code | Windows `catchupai` 계정 | 실제 코드/문서 작업을 실행 |

Termius만 설치하면 SSH 앱은 준비된 것이지만, `100.109.17.103`까지 가는 네트워크 경로가 없다. 각 모바일 기기마다 Tailscale을 설치하고 `Connected` 상태로 만들어야 한다.
## 원격 작업 전

원격 작업은 접속 성공보다 작업 범위 통제가 더 중요하다. 모바일 화면은 작고 복구가 불편하므로, 시작 전에 실행 호스트와 작업 경로를 먼저 확인한다.

```cmd
hostname
whoami
cd
claude --version
```

기대값:

| 명령 | 기대값 |
|---|---|
| `hostname` | `Changsoo` |
| `whoami` | `changsoo\catchupai` |
| `cd` | `C:\Users\catchupai` 또는 의도한 작업 경로 |
| `claude --version` | `2.1.241` 또는 현재 설치 버전 |

## Vault 작업 시작 절차

```cmd
cd C:\AI_study\2026\Changsoo_Vault
git -C Ingest\CatchUpAI_VL status --short
```

판단:

| 상태 | 행동 |
|---|---|
| 예상한 변경만 있음 | 작업 진행 |
| 모르는 변경이 많음 | 작업 중단 후 노트북에서 확인 |
| Git 저장소 경계가 헷갈림 | `Ingest\CatchUpAI_VL` 기준으로 재확인 |
| Claude Code가 다른 계정에서 실행됨 | 중단 |

## Claude Code 실행 전 체크

모바일 SSH에서 Claude Code를 실행할 때는 작고 검증 가능한 작업부터 시작한다. 대규모 파일 정리, 삭제, 이동, 자동 포맷팅은 모바일 환경에서 바로 실행하지 않는다.

권장 시작 순서:

```cmd
cd C:\AI_study\2026\Changsoo_Vault\Ingest\CatchUpAI_VL
git status --short
claude
```

Claude Code에 요청할 때는 다음을 명시한다.

```text
현재 작업 경로를 먼저 확인하고, 변경 전 대상 파일 목록을 보여 주세요.
파일 삭제나 대량 이동은 하지 마세요.
변경 후 git status를 보여 주세요.
```

## 원격 작업 중

| 상황 | 운영 원칙 |
|---|---|
| 긴 작업 | 중간 결과를 자주 저장하고 확인 |
| 파일 생성 | 목적 폴더가 맞는지 먼저 확인 |
| 파일 삭제 | 모바일에서는 원칙적으로 금지 |
| 인증/설치 요청 | 즉시 중단하고 노트북에서 검토 |
| 네트워크 지연 | 명령을 반복 입력하지 말고 결과 대기 |
| Claude Code 제안 | 변경 범위와 대상 파일을 확인한 뒤 승인 |

## 원격 작업 후

작업을 끝내기 전에 변경 상태를 확인한다.

```cmd
git -C C:\AI_study\2026\Changsoo_Vault\Ingest\CatchUpAI_VL status --short
```

필수 확인:

| 항목 | 확인 |
|---|---|
| 변경 파일 | 예상한 파일만 변경됐는가 |
| 생성 파일 | 실험/작업 목적에 맞는 위치인가 |
| 민감 정보 | 비밀번호, token, 개인키가 기록되지 않았는가 |
| WorkLog | 학습/운영 기록이 남았는가 |
| 세션 종료 | Termius 연결을 닫았는가 |

## 모바일에서 하지 않을 작업

| 작업 | 이유 |
|---|---|
| 대량 삭제 | 작은 화면에서 검토 실수 위험 |
| Git reset/rebase | 복구 난이도 높음 |
| 보안 설정 변경 | 접속 불능 또는 노출 위험 |
| OS 업데이트/드라이버 변경 | 모바일로 복구 어려움 |
| SSH/방화벽 변경 | 연결이 끊기면 원격 복구 불가 |

## 좋은 원격 작업 후보

| 작업 | 이유 |
|---|---|
| 문서 초안 작성 | 변경 범위가 명확함 |
| 작은 코드 수정 | 결과 검증 가능 |
| 로그 확인 | 읽기 중심 작업 |
| 단일 테스트 실행 | 실패 범위가 제한됨 |
| WorkLog 업데이트 | 학습 흐름 유지 |


