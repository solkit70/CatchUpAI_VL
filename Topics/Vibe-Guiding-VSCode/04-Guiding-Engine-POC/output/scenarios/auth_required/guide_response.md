# Guide Response

## 현재 상태 요약

- 문제 신호: `auth_required`
- 사용자 메시지: gobi auth status 결과 로그인이 되어 있지 않습니다.
- GOBI CLI 버전: 2.0.12
- 인증 상태: logged_out
- 활성 Space: unknown

## 판단 근거

- 선택된 trigger rule: `auth_required`
- 이유: GOBI CLI 인증 상태가 작업을 진행하기에 충분하지 않습니다.
- 선택된 manual: `gobi-cli-auth-status`

## 실행 단계

1. `gobi auth login`을 실행하고 표시되는 device-code flow를 완료합니다.
2. `gobi auth status`로 로그인 사용자가 표시되는지 확인합니다.

## 완료 신호

- `gobi auth status` shows an authenticated user.

## 실패 시 fallback

- Run `gobi auth login` again.
- Complete the device-code flow in the browser.

## Source Attribution

- `Topics/GOBI-CLI/01-Setup-Auth/concepts/installation-guide.md`
