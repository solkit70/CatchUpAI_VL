# Guide Response

## 현재 상태 요약

- 문제 신호: `version_mismatch`
- 사용자 메시지: 매뉴얼은 GOBI CLI 2.0.12 기준인데 제 환경은 node 16과 gobi 0.6.15라 명령어가 다르게 보입니다.
- GOBI CLI 버전: 0.6.15
- 인증 상태: authenticated
- 활성 Space: changbal

## 판단 근거

- 선택된 trigger rule: `environment_version_mismatch`
- 이유: 사용자 환경과 매뉴얼 기준 버전이 다를 수 있으므로 먼저 버전과 실행 환경을 확인해야 합니다.
- 선택된 manual: `gobi-cli-environment-version-check`

## 구 명령어 변환

- `gobi init` -> `gobi vault init`
- `BRAIN.md` -> `PUBLISH.md`
- `thread` -> `post`

## 실행 단계

1. `node --version`, `npm --version`, `gobi --version`을 먼저 실행해 현재 환경을 확인합니다.
2. GOBI CLI가 2.0.12 미만이면 `npm install -g @gobi-ai/cli`로 업데이트한 뒤 새 터미널을 엽니다.
3. 업데이트 전에는 v2.0.12 전용 명령어를 단정하지 말고, `gobi --help`에 실제 표시되는 명령어를 기준으로 안내합니다.

## 완료 신호

- `node --version`, `npm --version`, and `gobi --version` match the manual's supported environment before the user follows product steps.

## 실패 시 fallback

- If `gobi --version` is below 2.0.12, avoid v2-only commands until the CLI is updated.
- If Node.js is below 18, update Node before reinstalling GOBI CLI.

## Source Attribution

- `Topics/GOBI-CLI/01-Setup-Auth/concepts/installation-guide.md`
