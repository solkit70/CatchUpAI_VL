# M9 - Codex Remote 검증과 세팅

**상태**: **1단계 완료** (문서 조사 · 3자 비교) / **2단계 진행 중** (설치·페어링 완료, 경계 테스트 7항목 중 4건 부분 성공) / **브라우저 조작 실측 완료** (2026-08-30)

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
| **Computer Use** | 브라우저·데스크톱 조작. **브라우저는 앱 내장**. Windows는 잠금 해제 + 포그라운드 필요, **모바일에서 화면은 못 본다** |

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
- [lab/setup-procedure.md](lab/setup-procedure.md) — 설치·페어링 절차서 (경계 테스트 7항목)
- [lab/browser-control-verification.md](lab/browser-control-verification.md) — **내장 브라우저 원격 조작 실측** (2026-08-30)
- [decisions/codex-remote-usage-rules.md](decisions/codex-remote-usage-rules.md) — 운용 규칙 잠정안

## 다음 단계

1. ChatGPT 모바일 앱 설치·로그인 상태 확인
2. ChatGPT 계정 데이터 관리 설정 확인
3. 설치된 ChatGPT 데스크톱 앱에서 로그인 후 호스트 등록
4. 호스트 등록 + QR 페어링
5. 경계 테스트 7항목 수행
6. 절차서를 실기록으로 전환, 운용 규칙 확정

**SSH 호스트 등록은 아직 제외**한다. M5 보안 체크리스트를 다시 건드리므로 별도 승인이 필요하다.

Computer Use는 **브라우저 부분만 실측을 마쳤다**(2026-08-30). 브라우저 밖의 데스크톱 조작(앱 클릭·입력)은 위험도가 더 높아 그대로 남겨 둔다.

## 브라우저 조작 실측 — 조작은 되는데 화면을 못 본다

> 상세: [lab/browser-control-verification.md](lab/browser-control-verification.md)

**밖에서 지시하면 집 컴퓨터에서는 실제로 페이지가 열린다. 그런데 아이패드 앱에는 그 화면이 안 뜬다.** 텍스트로 *"열었습니다"* 라는 응답만 온다. 결과를 눈으로 확인하려면 결국 컴퓨터 앞으로 가야 한다.

Windows의 잠금 해제·포그라운드 제약은 **준비 조건**이지만 이건 다르다 — 밖에서 쓰려고 켜는 기능인데 **밖에서는 결과를 못 본다.** 목적 자체가 무너진다.

**문서 오류도 하나 잡았다.** *"Chrome 확장 설치가 필요하다"* 고 적어 뒀던 것은 틀렸다. 브라우저는 **앱에 내장**되어 있고(`Ctrl+Shift+B`), Chrome 확장은 **쓰던 Chrome 세션이 필요할 때** 쓰는 별개 물건이다.

**그리고 로그인 세션 이전은 가볍게 볼 일이 아니다.** 내장 브라우저에 기존 로그인을 쓰려면 Chrome의 **저장된 비밀번호 · 쿠키 · 방문 기록**을 통째로 가져와야 하고, Windows App-Bound Encryption 때문에 **관리자 승인**까지 받아야 한다. 이 Vault 기준으로는 **가져오지 않는 쪽이 기본값**이고, 필요한 사이트만 내장 브라우저 안에서 직접 로그인한다.

## 이전/다음

- 이전 모듈: [../08-Native-Remote-Control/README.md](../08-Native-Remote-Control/README.md)

