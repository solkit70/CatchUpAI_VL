# WorkLog - M9: Codex Remote 검증과 세팅

**날짜**: 2026-08-28
**Topic**: Claude-Code-Mobile-Remote-Execution
**모듈**: M9 - Codex Remote 검증과 세팅
**작성자**: Claude Code with VibeLearn AI
**상태**: **1단계 완료** (문서 조사·비교) / 2단계 대기 (설치·세팅)

## 오늘의 학습 목표

- Codex Remote의 연결 구조를 파악하고 Claude Code Remote Control과 대조한다.
- SSH · Claude RC · Codex Remote 3자 비교표를 만든다.
- 이 환경의 세팅 요건을 점검하고 절차서를 준비한다.
- (2단계) 설치·페어링·실사용 검증 — **사용자 요청으로 분리**

## 진행 내용

### 1. 범위 조정

사용자가 "문서 조사와 3자 비교부터 하고 설치·세팅은 나중에"로 요청해 모듈을 두 단계로 나눴다. 1단계는 조사와 문서화, 2단계는 실제 세팅이다.

### 2. 공식 문서 조사

`learn.chatgpt.com/docs/remote-connections`(구 `developers.openai.com/codex/remote-connections`, 308 리다이렉트)와 실무 워크플로우 블로그를 확인했다.

가장 중요한 발견은 **호스트 주체가 다르다**는 것이다. Claude Code는 `claude` 프로세스 자신이 원격 세션을 열지만, Codex는 **ChatGPT 데스크톱 앱**이 호스트다. 문서가 *"you can't set it up from the Codex CLI or IDE extension"* 이라고 명시한다. M7에서 검증한 Codex CLI는 이 기능과 무관하다.

### 3. Codex 고유 기능 정리

Handoff(대화 + Git 상태 이전), SSH 호스트 등록, Computer Use 세 가지가 Claude Code에 없다. 특히 **SSH 호스트 등록은 M1~M7에서 만든 Tailscale + Windows OpenSSH 구조를 그대로 등록 대상으로 쓸 수 있다**는 뜻이라, 세 경로가 배타적이지 않고 겹쳐 쓰인다는 것을 보여준다.

### 4. 데이터 취급 비대칭 확인

Claude Code 문서는 트랜스크립트가 Anthropic 서버에 저장된다고 명시하고 보존 정책을 링크한다. **Codex Remote 문서에는 이에 해당하는 서술이 없다.** 저장하지 않는다는 뜻이 아니라 문서로 판단할 수 없다는 뜻이다. 세팅 전에 ChatGPT 계정의 데이터 관리 설정을 확인하기로 절차서에 넣었다.

### 5. 환경 점검

`codex-cli 0.149.1`은 있으나 **ChatGPT 데스크톱 앱이 미설치**다. `winget`도 없어 웹에서 직접 받아야 한다. 플랜은 Plus로 확인됐다.

### 6. 산출물 작성

`09-Codex-Remote/` 아래 4개 문서를 작성했다. 절차서에는 M8과 같은 형식의 경계 테스트 7항목을 미리 넣어 두어, 세팅 시 그대로 채우면 실기록이 되도록 했다.

## 문제 해결 로그

| 문제 | 원인 | 해결/기록 |
|---|---|---|
| `developers.openai.com/codex/remote-connections` 308 리다이렉트 | 문서가 `learn.chatgpt.com`으로 이전 | 리다이렉트 URL로 재요청 |
| Codex CLI가 있는데 원격 기능이 안 보임 | CLI와 무관한 기능 — 데스크톱 앱이 호스트 | 구조 차이를 문서화 |
| `winget`으로 설치 확인 불가 | 이 시스템에 winget 없음 | `Get-AppxPackage` + 레지스트리 Uninstall 키로 확인 |
| Codex 측 데이터 저장 범위 불명 | 공식 문서에 서술 없음 | 추정하지 않고 "명시 없음"으로 기록. 세팅 전 계정 설정 확인을 절차에 추가 |

## DoD 체크리스트

**1단계**

- [x] Codex Remote 연결 구조 문서화 (Mermaid 다이어그램 포함)
- [x] Handoff · SSH 호스트 등록 · Computer Use 정리
- [x] SSH · Claude RC · Codex Remote 3자 비교표 작성
- [x] 이 환경의 세팅 요건 점검
- [x] 설치·페어링 절차서 작성 (경계 테스트 7항목 포함)
- [x] 운용 규칙 잠정안 작성
- [x] WorkLog 작성

**2단계 (대기)**

- [ ] ChatGPT 데스크톱 앱 설치
- [ ] 호스트 등록 + 모바일 QR 페어링
- [ ] 경계 테스트 7항목 수행
- [ ] 절차서를 실기록으로 전환
- [ ] 운용 규칙 확정

**1단계 완료율**: 7/7

## Daily Retrospective

### What went well

M8에서 만든 문서 형식(구조 → 실측 → 비교 → 결정)을 그대로 재사용해 빠르게 정리됐다. 경계 테스트 항목을 절차서에 미리 넣어 둔 덕분에 2단계가 채우기만 하면 되는 형태가 됐다.

### What could be improved

설치를 미룬 상태라 비교표의 일부 항목은 **문서 기반 추정**이다. 실측으로 교체해야 할 항목을 표시해 두긴 했지만, 추정과 실측이 한 표에 섞여 있는 것은 이상적이지 않다.

### Insights

1. **"CLI가 있으니 되겠지"가 틀렸다.** Codex CLI와 Codex Remote는 별개다. 같은 브랜드의 기능이라도 진입점이 다를 수 있다.
2. **문서에 없는 것을 없다고 읽으면 안 된다.** Anthropic은 트랜스크립트 저장을 명시하고 OpenAI는 침묵한다. 침묵이 더 안전하다는 뜻이 아니라, 판단 근거가 없다는 뜻이다.
3. **세 경로가 배타적이지 않다.** Codex Remote가 SSH 호스트를 등록할 수 있다는 것은 M1~M7의 결과물이 상위 계층에서 재사용된다는 의미다. 앞선 학습이 계속 쓰이고 있다.
4. 편의 기능은 대체로 **격리를 대가로 지불한다.** Claude RC도 Codex Remote도 일상 계정 세션에 붙는다. SSH 구조의 `catchupai` 격리는 두 경로 모두에 없다.

### Tomorrow's focus

- ChatGPT 모바일 앱 상태 확인 및 계정 데이터 관리 설정 점검
- ChatGPT 데스크톱 앱 설치 → 호스트 등록 → QR 페어링
- 경계 테스트 7항목 수행 후 절차서를 실기록으로 전환

## 참조 및 산출물

- [09-Codex-Remote/README.md](../09-Codex-Remote/README.md)
- [concepts/codex-remote-model.md](../09-Codex-Remote/concepts/codex-remote-model.md)
- [comparisons/three-way-remote-comparison.md](../09-Codex-Remote/comparisons/three-way-remote-comparison.md)
- [lab/setup-procedure.md](../09-Codex-Remote/lab/setup-procedure.md)
- [decisions/codex-remote-usage-rules.md](../09-Codex-Remote/decisions/codex-remote-usage-rules.md)
- 공식 문서: https://learn.chatgpt.com/docs/remote-connections
- 실무 워크플로우: https://developers.openai.com/blog/mastering-codex-remote-for-engineering
