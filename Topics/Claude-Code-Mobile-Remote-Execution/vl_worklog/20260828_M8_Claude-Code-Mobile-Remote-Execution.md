# WorkLog - M8: Claude Code 네이티브 Remote Control 검증과 구조 비교

**날짜**: 2026-08-28
**Topic**: Claude-Code-Mobile-Remote-Execution
**모듈**: M8 - 네이티브 Remote Control 검증과 구조 비교
**작성자**: Claude Code with VibeLearn AI

## 오늘의 학습 목표

- Remote Control의 연결 구조를 설명하고 SSH 방식과 대조한다.
- 이 환경에서 활성화·연결 상태를 실측한다.
- 두 방식의 경계를 판별한다 — 무엇이 Remote Control로 가능하고 무엇이 SSH를 필요로 하는가.
- 상황별 선택 기준을 만든다.

## 진행 내용

### 1. 발견 경위

사용자가 iPad Claude 앱의 `Code` 탭 스크린샷을 보내며 "Claude Code 자체에 Remote Control이 있는 것 같다"고 알려왔다. 화면에는 이 세션을 포함한 두 개의 로컬 세션이 `Connected` 상태로 떠 있었다. Topic 전체(M1~M7)와 Vault 어디에도 `Remote Control` 관련 기록이 없음을 검색으로 확인했다.

**원래 학습하려던 것이 이 기능이었다.** SSH 경로로 우회해 7개 모듈을 완주한 뒤에야 직행 경로를 발견한 셈이다.

### 2. 공식 문서 확인

`code.claude.com/docs/en/remote-control`에서 전체 문서를 확보했다. 핵심은 세 가지다. 로컬이 아웃바운드 HTTPS만 사용하고 인바운드 포트를 열지 않는다는 것, 실행과 파일 접근은 로컬에 머문다는 것, 그리고 **트랜스크립트는 Anthropic 서버에 저장된다**는 것이다.

시작 방법이 네 가지(`claude remote-control` 서버 모드, `claude --remote-control` 인터랙티브, 진행 중 세션에서 `/remote-control`, VS Code 확장)이고 각각 성격이 다르다는 점도 정리했다.

### 3. 이 환경 실측

`ListAgents`로 세션 목록을 조회해 피어 세션(`changsoo-modular-teapot`)이 Remote Control로 연결되어 있음을 확인했다. 자동 생성 이름 규칙(`호스트명-형용사-명사`)과 대화 이력 기반 제목이 나란히 관찰되어 문서의 제목 결정 순서가 실제로 그렇게 동작함을 확인했다.

버전과 환경변수를 점검하다 두 가지 문제를 찾았다. **PATH CLI가 2.1.143인데 VS Code 확장은 2.1.250**이고, **셸에 `ANTHROPIC_API_KEY`가 설정되어 있어** 터미널에서 `claude remote-control`이 거부된다.

### 4. 경계 테스트

6건을 수행했다. 실행 위치·MCP 유지·인바운드 포트 없음은 확인됐고, **계정 경계와 트랜스크립트 저장 위치**에서 SSH 구조 대비 후퇴가 확인됐다. 교차 세션 메시징 실동작은 피어 세션에 개입하게 되어 보류했다.

### 5. 산출물 작성

`08-Native-Remote-Control/` 아래 4개 문서를 작성하고 README로 묶었다.

## 문제 해결 로그

| 문제 | 원인 | 해결/기록 |
|---|---|---|
| `claude remote-control --help` 거부 | 셸에 `ANTHROPIC_API_KEY` 설정 | 원인 특정. 다른 용도 확인 후 처리 판단 필요 |
| 터미널 CLI가 낡음 (2.1.143) | 확장만 자동 업데이트됨 | 버전 게이트 7건 목록화. CLI 업데이트 필요 |
| 앱은 되는데 터미널은 안 되는 이유 | 확장은 `.credentials.json`의 claude.ai 로그인 사용 | 인증 경로가 다름을 문서화 |
| 교차 세션 메시징 미검증 | 피어 세션 작업에 개입 우려 | 미검증 항목으로 분리 기록 |

## DoD 체크리스트

- [x] Remote Control 연결 구조 문서화 (Mermaid 다이어그램 포함)
- [x] 활성화·연결 절차 실측 기록
- [x] 경계 테스트 6건 수행 및 결과 기록
- [x] SSH 방식과의 비교표 작성
- [x] 상황별 선택 기준 작성
- [x] 로드맵 추적표·성공 기준 갱신
- [x] WorkLog 작성

**완료율**: 7/7

## Daily Retrospective

### What went well

이 세션 자체가 Remote Control로 돌고 있어 별도 실험 환경 없이 실측할 수 있었다. `ListAgents` 출력과 iPad 스크린샷이 서로를 교차 검증해 주는 구조가 되었다.

### What could be improved

M1 단계에서 **공식 문서의 기능 목록을 먼저 훑었다면** 7개 모듈을 돌기 전에 발견했을 것이다. "어떻게 구현할까"로 바로 들어가기 전에 "이미 있는 기능인가"를 확인하는 단계가 로드맵에 없었다.

### Insights

1. **SSH를 먼저 배운 것이 헛되지 않았다.** 인바운드 포트를 열지 않는다는 점이 왜 중요한지는 M2에서 포트포워딩을 보안 2점으로 매겨 본 사람만 안다. 비교 대상이 없으면 편의성만 보인다.
2. **편한 경로가 항상 안전한 경로는 아니다.** Remote Control은 계정 격리를 우회하고 트랜스크립트를 서버에 남긴다. SSH 구조가 지키던 두 가지다.
3. **"이미 쓰고 있었는데 몰랐다"가 가장 흔한 학습 실패다.** 도구가 빠르게 바뀌는 영역에서는 만들기 전에 확인하는 습관이 필요하다.
4. 실무 함정은 대개 환경변수에 있다. 앱과 터미널이 다르게 동작하면 버전보다 환경을 먼저 본다.

### Tomorrow's focus

- 터미널 CLI 업데이트 후 `claude remote-control` 서버 모드 재검증
- Remotion 영상 브리프를 두 경로 비교 구성으로 개정

## 참조 및 산출물

- [08-Native-Remote-Control/README.md](../08-Native-Remote-Control/README.md)
- [concepts/native-remote-control-model.md](../08-Native-Remote-Control/concepts/native-remote-control-model.md)
- [lab/remote-control-verification.md](../08-Native-Remote-Control/lab/remote-control-verification.md)
- [comparisons/ssh-vs-native-remote-control.md](../08-Native-Remote-Control/comparisons/ssh-vs-native-remote-control.md)
- [decisions/which-path-when.md](../08-Native-Remote-Control/decisions/which-path-when.md)
- 공식 문서: https://code.claude.com/docs/en/remote-control
