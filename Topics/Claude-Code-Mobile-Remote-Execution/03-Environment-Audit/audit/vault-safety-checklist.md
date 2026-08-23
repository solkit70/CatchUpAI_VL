# Vault 안전 체크리스트

## 점검 목적

원격 Claude Code 실험은 로컬 파일을 실제로 변경할 수 있으므로, 실험 전 vault 경계와 Git 상태를 명확히 해야 한다.

## 경로 확인

| 항목              | 경로                                                               | 상태           |
| --------------- | ---------------------------------------------------------------- | ------------ |
| Vault root      | `C:\AI_study\2026\Changsoo_Vault`                                | 존재           |
| VibeLearn repo  | `C:\AI_study\2026\Changsoo_Vault\Ingest\CatchUpAI_VL`            | 별도 Git 저장소   |
| 현재 Topic        | `Ingest\CatchUpAI_VL\Topics\Claude-Code-Mobile-Remote-Execution` | 존재           |
| Topic 파일 수      | 15 files                                                         | M1-M3 산출물 포함 |
| 이전 잘못된 Topic 경로 | `Topics\Claude-Code-Mobile-Remote-Execution`                     | 존재하지 않음      |

## Git 경계

Vault root의 `.git` 디렉터리는 존재하지만 `info`만 있는 불완전한 디렉터리라 일반 Git 저장소로 인식되지 않았다. 실제 VibeLearn 작업은 `Ingest/CatchUpAI_VL` 하위 Git 저장소에서 관리된다.

`Ingest/CatchUpAI_VL` 기준으로 현재 Topic은 아직 untracked 상태다.

```text
?? Topics/Claude-Code-Mobile-Remote-Execution/
```

이 상태는 M4 원격 실험 전에 중요하다. 원격에서 Claude Code를 실행하면 untracked 산출물과 기존 변경분이 섞일 수 있으므로, 실험 전 Git 상태를 다시 확인해야 한다.

## 기존 변경분 주의

`Ingest/CatchUpAI_VL` 저장소에는 이번 Topic 외에도 기존 변경분이 있다. 일부 `Topics/Live-CoMC-App/...` 파일과 worklog가 modified/untracked 상태로 보였다. 이 변경분은 이번 작업과 무관하므로 건드리지 않는다.

## 원격 실험 전 체크리스트

- [ ] `Ingest/CatchUpAI_VL`에서 `git status --short` 확인
- [ ] 이번 Topic 외 기존 변경분을 건드리지 않기
- [ ] M4 테스트 파일은 `Topics/Claude-Code-Mobile-Remote-Execution/04-Remote-Execution-Lab/` 아래로 제한
- [ ] 테스트 파일 이름에 날짜와 module을 포함
- [ ] 원격 실험 전후 변경 파일 목록 기록
- [ ] Claude Code에게 작업 경로를 명시적으로 지시
- [ ] 루트 `Topics/`가 아니라 `Ingest/CatchUpAI_VL/Topics/`를 사용

## M4에서 허용할 안전한 테스트 범위

허용:
- 현재 Topic의 M4 폴더 생성
- M4 실험 절차서 작성
- 안전한 테스트 로그 파일 작성
- `git status` 확인
- `pwd`, `hostname`, `whoami`, `dir` 같은 읽기 중심 명령

별도 확인 필요:
- 기존 파일 대량 수정
- vault root 전체 검색/변경
- Git add/commit/push
- Tailscale 설치/로그인
- OpenSSH Server 설치/서비스 시작
- 방화벽 규칙 변경

금지:
- 기존 사용자 변경분 되돌리기
- `git reset --hard`
- 공개 포트 개방
- 불명확한 경로에서 Claude Code 실행

## 결론

현재 Topic 자체는 올바른 VibeLearn 경로에 있다. 다만 Git 관리 경계가 `Ingest/CatchUpAI_VL` 하위 저장소이므로, 원격 실험에서는 반드시 이 폴더를 기준으로 작업해야 한다.
