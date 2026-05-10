# Guide Response

## 현재 상태 요약

- 문제 신호: `cli_missing`
- 사용자 메시지: gobi 명령을 찾을 수 없습니다.
- GOBI CLI 버전: unknown
- 인증 상태: unknown
- 활성 Space: unknown

## 판단 근거

- 선택된 trigger rule: `cli_missing`
- 이유: GOBI CLI가 설치되어 있지 않거나 PATH에 반영되지 않았습니다.
- 선택된 manual: `gobi-cli-install`

## 실행 단계

1. 터미널에서 `npm install -g @gobi-ai/cli`를 실행합니다.
2. 새 터미널을 열고 `gobi --version`으로 설치 결과를 확인합니다.

## 완료 신호

- `gobi --version` prints a GOBI CLI version such as 2.0.12.

## 실패 시 fallback

- Open a new terminal after installing.
- Check Node/npm installation and PATH.

## Source Attribution

- `Topics/GOBI-CLI/01-Setup-Auth/concepts/installation-guide.md`
