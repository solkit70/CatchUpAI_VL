# Claude/Codex/Gemini 병행 사용 규칙

## 기본 원칙

iPad Termius에서 여러 SSH 탭을 열어 Claude Code, Codex CLI, Gemini CLI를 동시에 실행할 수 있다. 하지만 세 도구가 같은 Windows 사용자(`catchupai`)와 같은 repository를 바라보면 파일 변경 충돌이 생길 수 있다. 병행 실행은 가능하지만 병행 편집은 제한해야 한다.

## 권장 운영 모드

| 모드 | 설명 | 사용 시점 |
|---|---|---|
| 단일 편집자 모드 | 하나의 AI CLI만 파일을 수정하고 나머지는 질문/검토만 수행 | 기본값 |
| 역할 분리 모드 | Claude는 구현, Codex는 리뷰, Gemini는 아이디어/요약처럼 역할을 분리 | 같은 파일을 동시에 고치지 않을 때 |
| 순차 핸드오프 모드 | 한 CLI가 작업 완료 후 `git status`와 변경 요약을 남기고 다음 CLI가 이어받음 | 큰 작업을 나눌 때 |
| 읽기 전용 보조 모드 | 보조 CLI는 `rg`, `type`, `git diff` 등 읽기 중심 명령만 수행 | 충돌 위험이 높은 repo 작업 |

## 금지 규칙

- 같은 파일을 두 CLI가 동시에 수정하지 않는다.
- 한 CLI가 긴 작업 중일 때 다른 CLI에서 `git add .`를 실행하지 않는다.
- 모바일 세션에서 private key, API key, password를 화면에 표시하지 않는다.
- Codex/Gemini/Claude가 제안한 설치 명령을 바로 실행하지 말고, 계정과 PATH 영향 범위를 먼저 확인한다.
- 작업 중인 CLI가 있는 상태에서 같은 repository를 다른 탭에서 무심코 format/lint 전체 적용하지 않는다.

## 세션 시작 체크리스트

```bat
cd C:\AI_study\2026\Changsoo_Vault\Ingest\CatchUpAI_VL
git status --short
whoami
hostname
```

세션 시작 시 `git status --short`를 먼저 확인한다. 변경 파일이 이미 있으면 어떤 CLI가 만든 변경인지 확인한 뒤 작업을 이어간다.

## 세션 종료 체크리스트

```bat
git status --short
git diff --stat
```

작업을 끝낼 때는 어떤 파일을 수정했는지, 커밋/푸시가 필요한지, 다음 CLI가 이어받아도 되는지 기록한다. 모바일에서는 특히 `git add .` 대신 명시적 파일 경로를 사용한다.

## 권장 역할 분담

- Claude Code: VibeLearn AI 프로세스 진행, 문서 작성, 코드/파일 편집
- Codex CLI: 변경 리뷰, 명령 검증, OpenAI/Codex 관련 setup 확인
- Gemini CLI: 대안 아이디어, 요약, Google/Gemini API key 기반 확인

## 영상화 포인트

이 M7 사례는 "모바일에서 하나의 SSH 접속을 열었다"에서 끝나는 이야기가 아니다. 같은 iPad Termius 안에서 Claude Code, Codex, Gemini를 모두 붙일 수 있지만, 안전하게 쓰려면 계정별 설치, 인증 방식, PATH, API key, 파일 충돌 규칙을 이해해야 한다. 이 차이를 영상에서 보여주면 단순 설치 가이드보다 실전성이 높다.
