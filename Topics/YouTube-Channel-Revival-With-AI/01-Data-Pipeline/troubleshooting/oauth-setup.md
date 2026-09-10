---
title: "YouTube API OAuth 설정 — 막힌 지점과 해결"
created: 2026-09-10 10:20:00
tags:
  - youtube-analytics
  - oauth
  - troubleshooting
---

## 이 문서

M1 실습 2의 실행 안내이자 기록이다. **다음에 다시 겪지 않으려고** 막힌 지점을 그때그때 적는다.

## 🔴 먼저 — 계정과 채널을 헷갈리면 안 된다

| | 값 |
|---|---|
| **유튜브 구글 계정** | `seochang2011@gmail.com` (**볼트 계정과 다르다**) |
| **분석 대상 채널** | **Catch Up AI** `@catchupai` · 구독자 **4,320명** (2026-09-10 화면 확인) |
| 같은 계정의 다른 채널 | Wild Forager(기본, 1,010) · 미생 영어(1) · AI Madang(0) · Joosik Investment(16) |

**원래 Wild Forager 하나뿐이던 계정에 채널 4개를 더 붙인 구조다.**
그래서 OAuth 동의 때 **채널 선택 화면이 한 번 더 뜬다.** 여기서 Catch Up AI 를 고르지 않으면
`channel==MINE` 이 Wild Forager 로 풀린다.

> ✅ 볼트의 아카이브(`Ingest/YouTube/_status`, 496편)도 `@catchupai` 기준이라
> **대조 검산 대상이 일치한다.**

## 확인된 출발점 (2026-09-10)

| 항목 | 값 | 확인 방법 |
|---|---|---|
| OAuth 클라이언트 파일 | `C:/Users/dougg/gcp-oauth.keys.json` | 파일 존재 확인 |
| 클라이언트 종류 | **`installed`** (데스크톱 앱) | JSON 최상위 키 |
| Google Cloud 프로젝트 | `gen-lang-client-0588975117` | JSON `project_id` |
| redirect_uris | `http://localhost` | JSON |
| 파이썬 패키지 | ✅ 설치 완료 | `google-api-python-client`, `google-auth-oauthlib` |

> ⚠️ **계획서에 적어 뒀던 경로가 틀렸다.** `C:/Users/dougg/.config/google-calendar-mcp/gcp-oauth.keys.json`
> 이라고 썼는데, 그 폴더에는 **`tokens.json` 만** 있고 클라이언트 파일은 홈 디렉터리에 있다.
> 관련 문서 4개를 정정했다.

> ✅ **데스크톱 앱 클라이언트라 일이 쉬워진다.** 웹 앱이었다면 redirect URI 등록이 필요했을 텐데,
> `installed` 는 `run_local_server()` 가 임시 포트를 열고 바로 받는다.

## 🔴 계획 변경 — 캘린더 프로젝트를 재사용하지 않는다 (2026-09-10)

**막혔다.** `gen-lang-client-0588975117` 프로젝트의 OAuth 동의 화면을 열려고 하니
*"You need additional access"* 가 떴다.

```
Missing or blocked permissions
  · clientauthconfig.clients.get / .list
  · oauthconfig.verification.get
  · resourcemanager.projects.get
  · serviceusage.quotas.get
```

**원인**: 그 프로젝트는 **다른 구글 계정 소유**다. 지금 콘솔에 로그인한
`seochang2011@gmail.com` 에게는 권한이 없다.

> 📌 **계획서의 「이미 있는 자산을 재사용하면 M1 이 짧아진다」가 두 번 틀렸다.**
> 처음엔 **경로**가 틀렸고, 이번엔 **소유 계정**이 틀렸다. 파일이 있다는 것만 보고
> 「내 것이니 쓸 수 있다」고 넘겨짚은 결과다. **자산을 근거로 계획을 세울 때는
> 존재뿐 아니라 «내가 그것에 권한이 있는가»까지 확인한다.**

**Request access 를 누르지 않는다.** 승인해 줄 관리자를 기다릴 이유가 없다.

✅ **오히려 잘 됐다.** 유튜브 계정이 소유한 프로젝트에 클라이언트를 새로 만들면
**캘린더 MCP 프로젝트를 아예 건드리지 않게 된다** — 달력이 깨질 여지가 원천적으로 사라진다.

## 해야 할 것 — 순서대로

> 전부 **`seochang2011@gmail.com`** 으로 로그인한 상태에서 한다.
> 콘솔 왼쪽 위 프로젝트 선택기가 **`My Project`** 인지 확인한다.

### 1. API 두 개 켜기 ✅ 완료 (2026-09-10)

`My Project` 의 `사용 설정된 API` 목록에서 확인됨.

- [x] **YouTube Analytics API**
- [x] **YouTube Data API v3**

### 2. OAuth 동의 화면 구성 (`My Project`)

https://console.cloud.google.com/apis/credentials/consent

- [ ] 프로젝트가 **`My Project`** 인지 먼저 확인
- [ ] 아직 없으면 만든다 — **User Type: 외부(External)**
- [ ] 앱 이름 아무거나 (예: `YouTube Channel Analysis`), 지원 이메일·개발자 이메일 = `seochang2011@gmail.com`
- [ ] **범위(Scopes) 추가** — `범위 추가 또는 삭제` 에서 아래 둘

```
https://www.googleapis.com/auth/yt-analytics.readonly
https://www.googleapis.com/auth/youtube.readonly
```

- [x] ✅ **확인 완료 (2026-09-10)** — 게시 상태가 이미 **`In production`** 이고 User type 은 **External** 이다.
      **테스트 사용자 등록이 필요 없다.** 캘린더 MCP 를 붙이던 며칠 전에 프로덕션으로 전환해 둔 것이
      여기서 그대로 이득이 됐다. 🔴 `Back to testing` 을 누르지 않는다 — 되돌리면 오히려
      테스트 사용자를 일일이 등록해야 한다.
      · OAuth user cap 0 / 100 — 여유 충분
      · 승인 안 된 민감 범위라 동의 때 「확인되지 않은 앱」 경고가 뜬다. 정상이다

### 2-1. OAuth 클라이언트 만들기 (`My Project`)

https://console.cloud.google.com/apis/credentials

- [ ] `사용자 인증 정보 만들기` → **`OAuth 클라이언트 ID`**
- [ ] 애플리케이션 유형 → 🔴 **`데스크톱 앱`** (웹 앱 아님)
- [ ] 이름 아무거나 → 만들기
- [ ] **JSON 다운로드**
- [ ] 받은 파일을 아래 경로에 **`client_secret.json`** 이라는 이름으로 저장

```
C:\AI_study\2026\Changsoo_Vault\Ingest\CatchUpAI_VL\Topics\YouTube-Channel-Revival-With-AI\01-Data-Pipeline\.secrets\client_secret.json
```

> ✅ 스크립트가 **이 위치를 먼저 찾는다.** 코드를 고칠 필요 없다.
> `.secrets/` 는 `.gitignore` 로 제외돼 있다.

### 3. 인증 실행

```powershell
cd "C:\AI_study\2026\Changsoo_Vault\Ingest\CatchUpAI_VL\Topics\YouTube-Channel-Revival-With-AI\01-Data-Pipeline"
python scripts\youtube_analytics.py --check
```

브라우저가 열린다. 🔴 **여기가 이 모듈에서 가장 조심할 지점이다.**

1. **계정 선택** → `seochang2011@gmail.com`
   ⚠️ 볼트 사용자 이메일(`solkit70@gmail.com`)이 **아니다.** 유튜브 계정은 따로다
2. **채널 선택 화면** → 반드시 **Catch Up AI** 를 고른다
   이 계정에는 채널이 5개 있고, 기본은 **Wild Forager** 다. 아무 생각 없이 넘기면
   구독자 1,010명짜리 다른 채널의 지표를 받아 온다
3. 권한 허용

성공하면 이렇게 나온다.

```
채널   : Catch Up AI  @catchupai
구독자 : 4320   영상 xxx편
✅ 인증 확인 완료.
```

엉뚱한 채널로 인증되면 **스크립트가 스스로 멈춘다** — 잘못된 채널의 지표로 발표를 만드는
사고를 막으려고 검증을 넣어 뒀다.

### 4. 노출·CTR 이 API 에 있는지 판정

```powershell
python scripts\youtube_analytics.py --probe-impressions
```

- ❌ 실패하면 → **CSV 를 버리면 안 되는 이유**가 확인된 것이다. 아래 「확인 결과」에 적는다
- ✅ 성공하면 → CSV 부담이 줄어든다

### 5. 수집

```powershell
python scripts\youtube_analytics.py --all --start 2026-01-01
```

## 예상되는 막힘

### 🔴 「Google에서 확인하지 않은 앱입니다」

`yt-analytics.readonly` 와 `youtube.readonly` 는 **민감한 범위**다. 앱이 검증되지 않았으면
경고 화면이 뜬다.

**본인 계정이면 통과할 수 있다** — `고급` → `<앱 이름>(안전하지 않음)으로 이동`.
캘린더 MCP 를 붙일 때 이미 같은 화면을 지났다.

### 🔴 `403 accessNotConfigured`

API 를 안 켰다. **1번으로 돌아간다.** 켠 직후에는 1~2분 반영이 걸리기도 한다.

### 🔴 `403 insufficientPermissions` / `invalid_scope`

스코프가 동의 화면에 없거나, **예전 토큰이 남아 있어 옛 스코프로 재사용**되는 경우다.

```powershell
Remove-Item .secrets\youtube_token.json
python scripts\youtube_analytics.py --check
```

### ⚠️ 캘린더가 갑자기 안 될 때

**이 스크립트는 `C:\Users\dougg\.config\google-calendar-mcp\tokens.json` 을 건드리지 않는다.**
토큰을 `01-Data-Pipeline\.secrets\youtube_token.json` 에만 쓴다. 그래도 이상하면
캘린더 MCP 쪽 인증을 다시 돌린다.

### ⚠️ 데이터가 며칠 비어 있다

Analytics 데이터는 **보통 며칠 지연**된다. 발표에 넣을 때는 **집계 마감일을 명시**한다
(*"9/14 기준"* 처럼).

## 확인 결과 (실행하면서 채운다)

| 항목 | 결과 | 날짜 |
|---|---|---|
| API 두 개 사용 설정 | ⏳ | |
| 스코프 추가 | ⏳ | |
| `--check` 성공 | ⏳ | |
| **노출·CTR 이 API 에 있는가** | ⏳ | |
| 캘린더 MCP 정상 동작 | ⏳ | |
| 496편 아카이브와 영상 수 대조 | ⏳ | |

## 막힌 기록

> 실제로 막힌 것을 여기에 적는다. 「무엇을 했더니 무엇이 나왔고 어떻게 풀었다」 순서로.

(아직 없음)
