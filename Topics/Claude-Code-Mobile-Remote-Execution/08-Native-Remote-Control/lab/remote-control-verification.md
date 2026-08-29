# 실측 기록 - 네이티브 Remote Control

**측정일**: 2026-08-28
**측정 환경**: Windows 11, `dougg` 계정, `C:/AI_study/2026/Changsoo_Vault`

## 요약

이 세션 자체가 Remote Control로 연결된 상태였다. 별도 실험 환경을 만들 필요 없이 현재 동작 중인 구조를 그대로 계측했다. 가장 중요한 발견 두 가지는 **터미널 CLI와 VS Code 확장의 버전이 100판 이상 벌어져 있다는 것**과 **`ANTHROPIC_API_KEY`가 설정되어 있어 터미널에서 시작하는 Remote Control은 차단된다는 것**이다.

## 1. 연결 상태 확인

`ListAgents`로 같은 계정의 세션 목록을 조회했다.

```text
This session is changsoo-vault-75 [eaded4]
Peer sessions (1):
  changsoo-modular-teapot [31da2e]  ·  Remote Control  ·  idle
```

iPad 스크린샷의 Claude 앱 `Code` 탭에서도 같은 두 세션이 보였다.

| 앱에 표시된 이름 | 상태 | 경로 |
|---|---|---|
| `changsoo-modular-teapot` | Connected | `solkit70/CatchUpAI_VL` |
| `Live-CoMC-App topic` | Connected | (이 세션) |

`changsoo-modular-teapot`은 **자동 생성 이름**의 전형적인 형태다 — `호스트명 + 형용사 + 명사`. `Live-CoMC-App topic`은 대화 이력에서 유도된 제목이다. 문서가 설명한 제목 결정 순서(명시적 이름 → `/rename` → 대화 이력 → 자동 생성)가 실제로 그렇게 작동하고 있음을 두 세션이 나란히 보여준다.

터미널 상단 배너도 연결을 알린다.

```text
Remote Control is active · Continue here, on your phone, or at claude.ai/code
```

## 2. 버전 확인 — 여기서 문제가 나왔다

```text
$ claude --version
2.1.143 (Claude Code)

$ ls ~/.vscode/extensions/ | grep anthropic
anthropic.claude-code-2.1.247-win32-x64
anthropic.claude-code-2.1.250-win32-x64
```

**PATH의 CLI는 2.1.143, VS Code 확장은 2.1.250이었다.** (→ 2026-08-28 CLI를 2.1.250으로 업데이트해 해소. 아래 7절 참조) 이 세션은 확장에서 돌고 있으므로 최신 기능을 쓰고 있지만, 터미널에서 `claude`를 치면 100판 이상 낡은 바이너리가 실행된다.

이 차이가 실제로 문제가 되는 기능들이다.

| 기능 | 요구 버전 | 2.1.143에서 |
|---|---|---|
| `remote-control --continue` / `--session-id` | v2.1.200+ | ❌ 인자 거부 |
| VS Code 자동 연결 토글 | v2.1.203+ | ❌ |
| 모바일에서 `/config key=value` | v2.1.181+ | ❌ |
| 모바일에서 `/mcp` 요약 | v2.1.166+ | ❌ |
| 교차 세션 메시징 | v2.1.224+ | ❌ |
| 기기에서 effort 조절 | v2.1.234+ | ❌ |
| 자동 생성 제목의 언어 매칭 | v2.1.176+ | ❌ |

**조치**: 터미널 CLI를 업데이트해야 한다. `claude update` 또는 설치 방식에 맞는 갱신이 필요하다.

## 3. Remote Control 자격 검사 — 차단 확인

```text
$ claude remote-control --help
Error: Remote Control requires claude.ai subscription auth.
ANTHROPIC_API_KEY is set, so this session is using API-key auth —
unset it (or run in a shell without it) to use Remote Control.
```

환경변수를 점검했다.

| 변수 | 상태 |
|---|---|
| `ANTHROPIC_API_KEY` | **SET** (길이 108) ← 차단 원인 |
| `ANTHROPIC_BASE_URL` | unset |
| `CLAUDE_CODE_OAUTH_TOKEN` | unset |
| `CLAUDE_CODE_USE_BEDROCK` / `_VERTEX` | unset |
| `DISABLE_TELEMETRY` / `DO_NOT_TRACK` / `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` / `DISABLE_GROWTHBOOK` | 모두 unset |

**차단 요인은 `ANTHROPIC_API_KEY` 하나뿐이다.** 나머지 조건은 전부 통과다. 그런데도 이 세션이 Remote Control로 붙어 있는 이유는 **VS Code 확장이 `~/.claude/.credentials.json`의 claude.ai 로그인을 쓰기 때문**이다. 터미널 셸에만 API key가 설정되어 있다.

이건 실무에서 헷갈리기 딱 좋은 지점이다. "앱에서는 되는데 터미널에서는 안 된다"는 증상이 나오면 원인은 버전이 아니라 **셸 환경변수**일 가능성이 높다.

## 4. 설정 파일 상태

| 파일 | `remoteControlAtStartup` | `disableRemoteControl` | `env` 블록 |
|---|---|---|---|
| `~/.claude/settings.json` | 미설정 | 미설정 | 없음 |
| `Changsoo_Vault/.claude/settings.json` | 미설정 | 미설정 | 없음 |
| `Changsoo_Vault/.claude/settings.local.json` | 미설정 | 미설정 | 없음 |

`~/.claude/remote-settings.json`이 존재하지만 내용은 `{}`다. `~/.claude.json`에는 사용 흔적이 남아 있다.

```json
"remoteControlUpsellSeenCount": 2,
"remoteControlSurfacesSeen": ["mobile"]
```

`remoteControlSurfacesSeen: ["mobile"]` — 모바일 표면만 사용한 기록이다. 브라우저(`claude.ai/code`)로는 아직 붙어본 적이 없다는 뜻으로 읽힌다.

## 5. 경계 테스트 결과

| # | 항목 | 결과 | 근거 |
|---|---|---|---|
| 1 | 실행 위치가 로컬인가 | ✅ 로컬 | 이 세션에서 실행한 모든 Bash·파일 편집이 `C:\AI_study\...` 에 반영됨 |
| 2 | 로컬 MCP·스킬·권한이 유지되는가 | ✅ 유지 | Gmail MCP 호출, `vibelearn-ai` 스킬 로드, `settings.json` 권한 모두 정상 동작 |
| 3 | 인바운드 포트가 열리는가 | ✅ 안 열림 | 아웃바운드 HTTPS 폴링 구조. 공유기 설정 변경 없이 iPad에서 연결됨 |
| 4 | 계정 경계 | ⚠️ **다름** | Remote Control은 `dougg` 세션. SSH 방식은 `catchupai` 계정 |
| 5 | 터미널 CLI에서 시작 가능한가 | ❌ 차단 | `ANTHROPIC_API_KEY` 설정으로 자격 검사 실패 |
| 6 | 트랜스크립트 저장 위치 | ⚠️ **Anthropic 서버** | 공식 문서 명시. 로컬에만 남지 않는다 |

### 4번이 M4~M7 결과에 미치는 영향

SSH 방식은 `catchupai`라는 **별도 Windows 계정**으로 접속하도록 설계했다. M7에서 확인했듯 `dougg`의 npm global 설치·PATH·로그인 상태는 `catchupai`로 공유되지 않는다. Remote Control은 이 격리를 우회한다 — `dougg` 세션에 그대로 붙기 때문이다.

**보안 설계 관점에서는 후퇴다.** M5의 보안 체크리스트는 "모바일에서 들어오는 세션은 제한된 계정에서 돈다"는 전제 위에 서 있었다. Remote Control에는 그 계층이 없다.

### 6번이 이 Vault에 갖는 의미

`Changsoo_Vault`에는 개인정보가 있다. 메일링 리스트(이메일 32건), 주택 워런티 기록, 가족 의료 일정, 세무 자료가 포함된다. Remote Control이 연결된 동안 **작업 내용이 트랜스크립트로 Anthropic 서버에 저장된다.**

이건 결함이 아니라 설계다. 기기 간 동기화와 재연결에 필요하다. 다만 **이 Vault에서 민감한 작업을 할 때는 의식하고 써야 한다.** 완전히 끄려면 `disableRemoteControl` 설정을 쓴다.

## 6. 조치 후 재검증 (2026-08-28, 같은 날)

### CLI 업데이트

`autoUpdates`가 `false`로 꺼져 있었다. 설치 방식은 npm global(`@anthropic-ai/claude-code`)이다.

```text
$ npm install -g @anthropic-ai/claude-code@latest
changed 2 packages in 13s

$ claude --version
2.1.250 (Claude Code)
```

**2.1.143 → 2.1.250.** VS Code 확장과 같은 버전이 되어 버전 게이트 7건이 모두 해소됐다.

### API key 차단 원인 격리

업데이트 후에도 `claude remote-control`은 같은 이유로 거부됐다. 환경변수를 뺀 서브셸에서 실행해 원인을 확정했다.

```text
$ env -u ANTHROPIC_API_KEY claude remote-control --help
Remote Control - Control local sessions from claude.ai/code or the Claude mobile app

USAGE
  claude remote-control [options]
OPTIONS
  --name <name>                 Name for the session (shown in claude.ai/code)
  -c, --continue                Reattach to the session ... within roughly the last 4 hours
  --session-id <id>             Reattach to a specific session by ID
  --permission-mode <mode>      acceptEdits, auto, bypassPermissions, default, dontAsk, plan
  ...
```

**환경변수 하나만 빼면 정상 동작한다.** `--continue`, `--session-id` 등 v2.1.200+ 플래그도 모두 보인다.

`--permission-mode`가 서버 모드에 있다는 것은 문서에 없던 발견이다. 원격에서 생성되는 세션의 권한 모드를 시작 시점에 정할 수 있다는 뜻이라, **모바일에서 승인을 일일이 누르기 번거로울 때 쓸 수 있는 지점**이다. 다만 `bypassPermissions`는 위험하므로 이 Vault에서는 쓰지 않는다.

### 인증 상태 정밀 확인 — 앞선 판단을 정정한다

`claude auth status`와 `.claude.json`의 승인 기록을 확인했다.

```json
{ "loggedIn": true, "authMethod": "claude.ai", "subscriptionType": "pro",
  "apiKeySource": "ANTHROPIC_API_KEY" }
```

```text
customApiKeyResponses.approved: []
customApiKeyResponses.rejected: [3건, 현재 키 포함]
```

**터미널 세션도 이미 claude.ai 구독으로 인증되어 있었다.** 환경변수의 키는 3개 모두 거부 목록에 있어 모델 요청에 쓰인 적이 없다. Claude Code는 `ANTHROPIC_API_KEY`를 발견하면 사용 여부를 한 번 묻는데, 매번 거절한 기록이다.

키 종류도 확인했다.

| 값 | 접두사 | 종류 |
|---|---|---|
| `ANTHROPIC_API_KEY` | `sk-ant-api03-` | **과금용 API 키** |
| `.credentials.json` accessToken | `sk-ant-oat01-` | OAuth 구독 토큰 |

**정정할 것** — 앞 절에서 "API key 정리가 Remote Control의 전제"라고 썼는데, 인과가 반대다. Remote Control은 **claude.ai 구독 인증에서만 동작하고 API key 인증은 아예 지원하지 않는다.** 터미널이 막힌 이유는 과금 방식 때문이 아니라, Claude Code가 **환경변수의 존재만 보고** 그 세션을 API key 인증으로 판정하기 때문이다. 실제로는 거부된 키인데도 그렇다.

### 조치 — 사용자 환경변수 삭제 (2026-08-28)

사용자가 API를 쓸 계획이 없다고 확인해 User 스코프 환경변수를 제거했다.

```text
User    : 삭제됨
Machine : 없음
Process : 기존 셸에만 잔존 (재시작 시 소멸)
```

삭제 후 `claude auth status` 출력에서 `apiKeySource` 항목이 사라졌다. 구독 인증만 남았다.

값은 세션 스크래치패드에 백업했다(볼트·git 밖). 키 자체는 `console.anthropic.com`에서 폐기(revoke)하는 것이 안전하다 — 식별용 접두사는 `sk-ant-api03-f`, 끝 6자는 `cPxgAA`다.

### 환경변수 설정 위치 (삭제 전 기준)

| 스코프 | 상태 |
|---|---|
| User | **SET** (길이 108) ← 여기 |
| Machine | 없음 |
| Process | User에서 상속 |

Windows **사용자 환경변수**로 등록되어 있어 모든 새 셸에 상속된다. 선택지는 셋이다.

| 방안 | 방법 | 판단 |
|---|---|---|
| 그대로 두고 필요할 때만 해제 | `env -u ANTHROPIC_API_KEY claude remote-control` | **권장.** 다른 도구가 이 키를 쓰고 있을 수 있다 |
| Claude Code 전용 셸 프로파일 분리 | 해당 프로파일에서만 `unset` | 자주 쓰면 유용 |
| 사용자 환경변수 삭제 | 시스템 환경변수 편집 | 다른 용도 확인 전에는 위험 |

**2026-08-28 결론**: 사용자가 API를 사용할 계획이 없어 세 번째 방안(삭제)을 택했다. VS Code 확장과 터미널 CLI 모두 `.credentials.json`의 claude.ai 로그인을 쓰므로 이 키와 무관했다.

## 7. 검증하지 못한 것

| 항목 | 사유 |
|---|---|
| 교차 세션 메시징 실동작 | 피어 세션(`changsoo-modular-teapot`)에 메시지를 보내면 다른 작업에 개입하게 되어 보류 |
| `claude remote-control` 서버 모드 **실제 세션 생성** | `--help`까지는 확인. 실제 서버를 띄워 모바일에서 붙는 것은 미수행 |
| 브라우저(`claude.ai/code`) 연결 | 아직 사용 이력 없음 |
| 장시간 작업 중 연결 끊김 복구 | 의도적 네트워크 차단이 필요해 별도 세션에서 진행 권장 |
| 모바일 푸시 알림 | `/config`에서 켜야 함. 미설정 상태 |

## 다음 조치

- [x] **터미널 CLI 업데이트** — 2.1.143 → 2.1.250 완료 (2026-08-28)
- [x] **`ANTHROPIC_API_KEY` 제거** — User 스코프 환경변수 삭제 완료 (2026-08-28). 3개 키 모두 거부 상태였고 실제 과금 이력 없음
- [x] **`autoUpdates` 재활성화** — `~/.claude.json`에서 `false` → `true`. `claude doctor`로 `Auto-updates: enabled` 확인
- [ ] **API 키 폐기(revoke)** — `console.anthropic.com`에서 `sk-ant-api03-f...cPxgAA` 폐기. 환경변수는 지웠지만 키 자체는 아직 유효
- [ ] **`/config`에서 모바일 푸시 설정** — 긴 작업의 실질적 가치가 여기서 나온다
- [ ] **서버 모드 실제 세션 생성 테스트** — 모바일에서 붙어 보기
- [ ] **민감 작업 시 Remote Control 해제 기준 적용** → [../decisions/which-path-when.md](../decisions/which-path-when.md)
