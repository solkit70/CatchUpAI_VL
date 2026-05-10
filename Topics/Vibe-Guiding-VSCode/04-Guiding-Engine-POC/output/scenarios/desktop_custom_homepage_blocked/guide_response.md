# Guide Response

## 현재 상태 요약

- 문제 신호: `desktop_custom_homepage_blocked`
- 사용자 메시지: GOBI Desktop에서 custom homepage applet을 만들고 싶은데 현재 메뉴와 Applet 경로를 모르겠습니다.
- GOBI CLI 버전: 2.0.12
- 인증 상태: authenticated
- 활성 Space: unknown

## 판단 근거

- 선택된 trigger rule: `desktop_applet_context_missing`
- 이유: GOBI Desktop Applet 안내 전에 실제 앱 버전, Vault Path, Applet 경로를 확인해야 합니다.
- 선택된 manual: `gobi-desktop-applet-context-check`

## 실행 단계

1. 먼저 GOBI Desktop 버전, Vault Path, Applet 경로, 현재 보이는 Settings 메뉴명을 확인합니다.
2. 확인되지 않은 메뉴 이름이나 버튼 위치는 단정하지 말고, 사용자가 보는 화면 기준으로 다음 단계를 좁힙니다.
3. Applet 경로가 확인되면 custom homepage 파일 위치와 적용 절차를 같은 경로 기준으로 안내합니다.

## 완료 신호

- The user has confirmed the Desktop version, Vault Path, Applet path, and the exact visible menu before following setup steps.

## 실패 시 fallback

- Do not name a menu that has not been confirmed in the user's UI.
- Ask the user to capture the visible settings screen if the Applet path is unknown.

## Source Attribution

- `Topics/GOBI-Guiding/2026-04-13 Gobi Desktop Vibe Guiding 기능 수준 테스트.md`
