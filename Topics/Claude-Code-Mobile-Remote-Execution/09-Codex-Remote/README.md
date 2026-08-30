# M9 - Codex Remote 검증과 세팅

**상태**: **1단계 완료** (문서 조사 · 3자 비교) / **2단계 대기** (설치 · 세팅 · 실사용 검증)

## 요약

M8에서 Claude Code 네이티브 Remote Control을 다룬 뒤, Codex에도 같은 성격의 기능이 있다는 것을 확인해 추가한 모듈이다. 사용자 요청에 따라 **문서 조사와 비교를 먼저 마치고 설치·세팅은 분리**했다.

## 핵심 발견 — 구조가 다르다

**Codex Remote의 호스트는 ChatGPT 데스크톱 앱이다.** Codex CLI가 아니다. 공식 문서가 못 박는다.

> "Mobile setup starts from the app; you can't set it up from the Codex CLI or IDE extension."

M7에서 검증한 `codex-cli 0.149.1`은 이 기능과 무관하다. Claude Code가 `/remote-control` 한 줄로 끝나는 것과 달리, **Codex는 데스크톱 앱 설치가 전제**라 진입 비용이 한 단계 더 있다.

## Codex Remote만 갖는 세 가지

| 기능 | 내용 |
|---|---|
| **Handoff** | 대화와 **Git 상태**를 로컬↔원격 호스트로 이전. worktree 생성/재사용. Claude Code에 대응 기능 없음 |
| **SSH 호스트 등록** | 앱이 `~/.ssh/config`의 호스트를 등록해 그 위의 `codex`를 구동. **M1~M7 구조를 그대로 재활용 가능** |
| **Computer Use** | 브라우저·데스크톱 조작. Windows는 잠금 해제 + 포그라운드 필요 |

SSH 호스트 등록이 특히 흥미롭다. 세 경로가 배타적이지 않고 **겹쳐 쓰인다**는 뜻이다.

## 데이터 취급에 비대칭이 있다

| | 문서의 서술 |
|---|---|
| Claude Code | *"the session transcript ... is stored on Anthropic servers"* + 보존 정책 링크 |
| Codex Remote | **해당 서술 없음** |

**"명시가 없다"를 "저장하지 않는다"로 읽으면 안 된다.** 릴레이가 세션 상태를 기기 간에 동기화하므로 어떤 형태로든 서버를 거친다. 다만 무엇이 얼마나 남는지 문서만으로는 알 수 없다.

개인정보가 있는 이 Vault 기준으로는 **알고 쓰는 쪽이 낫다.** 세팅 전에 ChatGPT 계정의 데이터 관리 설정을 확인하기로 했다.

## 환경 점검 (2026-08-28)

| 항목 | 상태 |
|---|---|
| ChatGPT 플랜 | **Plus** (개인 계정) ✅ |
| Codex CLI | `0.149.1` — 이 기능과 무관 |
| **ChatGPT 데스크톱 앱** | ✅ 설치됨: `OpenAI.ChatGPT-Desktop 1.2026.190.0` (2026-08-30) |
| `winget` | ❌ 사용 불가 → 웹에서 직접 다운로드 필요 |

## 산출물

- [concepts/codex-remote-model.md](concepts/codex-remote-model.md) — 연결 구조, Handoff, Computer Use, 모바일 명령어, 요건과 제약
- [comparisons/three-way-remote-comparison.md](comparisons/three-way-remote-comparison.md) — **SSH · Claude RC · Codex Remote 3자 비교표**
- [lab/setup-procedure.md](lab/setup-procedure.md) — 설치·페어링 절차서 (실행 대기, 경계 테스트 7항목 포함)
- [decisions/codex-remote-usage-rules.md](decisions/codex-remote-usage-rules.md) — 운용 규칙 잠정안

## 다음 단계

1. ChatGPT 모바일 앱 설치·로그인 상태 확인
2. ChatGPT 계정 데이터 관리 설정 확인
3. 설치된 ChatGPT 데스크톱 앱에서 로그인 후 호스트 등록
4. 호스트 등록 + QR 페어링
5. 경계 테스트 7항목 수행
6. 절차서를 실기록으로 전환, 운용 규칙 확정

**Computer Use와 SSH 호스트 등록은 1차 세팅에서 제외**한다. 전자는 화면 조작 권한이라 위험이 크고, 후자는 M5 보안 체크리스트를 다시 건드리므로 별도 승인이 필요하다.

## 이전/다음

- 이전 모듈: [../08-Native-Remote-Control/README.md](../08-Native-Remote-Control/README.md)

