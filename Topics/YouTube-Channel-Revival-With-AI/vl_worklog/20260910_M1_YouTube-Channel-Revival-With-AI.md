---
title: "WorkLog 2026-09-10 · M1 — 데이터 파이프라인과 P5 정의"
created: 2026-09-10 10:35:00
module: M1
topic: YouTube-Channel-Revival-With-AI
tags:
  - vibelearn-ai
  - worklog
  - youtube-analytics
---

# WorkLog — 2026-09-10 · M1

**Topic**: YouTube-Channel-Revival-With-AI
**모듈**: M1 — 데이터 파이프라인과 P5 정의 (5h)
**발표까지**: **6일** (2026-09-16 수 19:00)

## 오늘의 학습 목표

- [ ] Google Cloud 프로젝트에 YouTube API 두 개를 켜고 스코프를 추가한다
- [ ] `reports.query` 200 응답을 받는다
- [ ] 일 단위 구독자 시계열을 뽑아 주 단위로 집계한다
- [ ] 🟥 **횡보 시작 시점과 마이너스 전환 시점을 날짜와 숫자로 특정한다**
- [ ] 🟥 **Studio CSV 4종을 확보한다**
- [ ] P5 구간 분석 문서 초안을 쓴다

## 진행 내용

### 준비 — 환경 확인 (완료)

| 확인 | 결과 |
|---|---|
| `google-api-python-client` | ❌ 없었음 → ✅ 설치 |
| `google-auth-oauthlib` | ❌ 없었음 → ✅ 설치 |
| `pandas` | ✅ 이미 있음 |
| OAuth 클라이언트 파일 | ✅ 발견 — **경로가 계획서와 달랐다** |

🔴 **계획서에 적힌 OAuth 경로가 틀렸다.**
`C:/Users/dougg/.config/google-calendar-mcp/gcp-oauth.keys.json` 로 적어 뒀는데,
그 폴더에는 **`tokens.json` 만** 있고 클라이언트 파일은 **`C:/Users/dougg/gcp-oauth.keys.json`** 에 있었다.
→ 관련 문서 4개(topic_starter · roadmap_prompt · 진행 계획 2벌) 정정 완료.

✅ **좋은 소식** — 클라이언트가 **`installed`(데스크톱 앱)** 타입이다.
웹 앱이었으면 redirect URI 를 따로 등록해야 했을 텐데, `run_local_server()` 로 바로 된다.
프로젝트는 `gen-lang-client-0588975117` — 캘린더 MCP 와 같은 프로젝트다.

### 실습 3 (선행) — 수집 스크립트 작성 (완료)

실습 2(OAuth)가 사용자 작업을 기다려야 해서, **스크립트를 먼저 써 뒀다.**
인증만 뚫리면 바로 돌아간다.

`scripts/youtube_analytics.py` — 다음을 담았다.

| 기능 | 플래그 | 내용 |
|---|---|---|
| 인증 확인 | `--check` | 채널명·구독자 수 출력 |
| **노출·CTR 판정** | `--probe-impressions` | API 에 있는지 **직접 쳐 보고** 결과를 JSON 으로 남긴다 |
| ① 일 단위 시계열 | `--daily` | `dimensions=day` → 주 단위 집계까지 |
| ② 영상별 성과 | `--videos` | `dimensions=video` + Data API 메타데이터 결합 |
| ③ 유입 경로 | `--traffic` | `insightTrafficSourceType` |

설계에서 신경 쓴 것 셋:

1. **토큰을 `.secrets/youtube_token.json` 에 따로 둔다.** 캘린더 MCP 의 `tokens.json` 을
   건드리지 않는다. `.secrets/.gitignore` 로 제외도 걸어 뒀다.
2. **응답 원본을 `data/raw/*.json` 에 그대로 저장한다.** 집계가 틀리면 원본에서 다시 한다.
3. **주간 집계가 내는 것은 「순증(gained − lost)」이지 구독자 총수가 아니다.** 코드 주석에
   적어 뒀다 — 총수는 Data API 의 현재값에서 거꾸로 누적해야 한다.

### 문서 작성 (완료)

- `README.md` — 학습 순서·실습 상태·DoD·기억 대조표
- `troubleshooting/oauth-setup.md` — Console 클릭 순서와 **예상되는 막힘 4가지**

### ⏳ 사용자 작업 대기

여기서부터는 브라우저와 콘솔이 필요해 내가 대신할 수 없다.

1. **Google Cloud Console** — API 두 개 사용 설정 + 스코프 추가
2. **`--check` 실행** — 브라우저 동의
3. **YouTube Studio CSV export** — 4종

## 문제 해결 로그

| 문제 | 원인 | 해결 |
|---|---|---|
| 파이썬 힙쉬 스크립트에서 `\2026` 이 8진 이스케이프로 먹혀 경로가 `AI_study6` 로 깨짐 | 비 raw 문자열 안의 `\202` | 경로를 **슬래시**로 바꾸고, 이후 스크립트는 파일로 써서 실행 |
| 계획서의 OAuth 경로가 실제와 다름 | 8일 전 작성 시 `.config` 폴더만 보고 추정 | 실제 파일 탐색 후 문서 4개 정정 |

## DoD 체크리스트

- [ ] 🟥 CSV 4종 확보
- [ ] 🟥 횡보·마이너스 시점 특정
- [ ] OAuth 연결 성공
- [ ] 노출·CTR 판정 기록
- [ ] 수집 자동화 3개 조합 이상
- [ ] `phase5-growth-analysis.md` 초안
- [ ] 496편 아카이브 대조
- [x] WorkLog 작성 (이 문서)
- [ ] Daily Retrospective

## Daily Retrospective

### What went well

- **스크립트를 인증보다 먼저 썼다.** 사용자 작업을 기다리는 동안 손을 놓지 않았고,
  인증이 뚫리는 순간 바로 수집이 된다.
- **경로 오류를 실행 전에 잡았다.** 문서에만 있던 틀린 경로였는데, 파일을 실제로 찾아보고
  고쳤다. 안 고쳤으면 사용자가 그 경로에서 헤맸을 것이다.

### What could be improved

- 계획서(9/8)를 쓸 때 **파일 존재를 확인하지 않고 경로를 적었다.** 「이미 있는 자산」을
  근거로 M1 이 짧아진다고까지 썼는데, 그 근거의 경로가 틀렸다.
  → **자산을 근거로 계획을 세울 때는 그 자리에서 존재를 확인한다.**

### Insights

- **데스크톱 앱 클라이언트라는 게 생각보다 큰 이점이다.** 웹 앱이면 redirect URI 등록과
  포트 고정이 필요한데, `installed` 는 임시 포트로 끝난다.
- 「노출·CTR 은 API 에 없다」를 계획서에 **단정으로 적었었다.** 내 기억이지 확인한 사실이
  아니었다. 이번엔 `--probe-impressions` 로 **직접 쳐 보고 결과를 남기게** 만들었다.
  이 Topic 의 주제가 「감이 아니라 데이터로」인데 계획 자체가 감이었으면 앞뒤가 안 맞는다.

### Tomorrow's focus

- Console 설정이 끝나면 `--all` 로 수집 → `phase5-growth-analysis.md` 초안
- 🟥 **기억 대조표 4줄을 숫자로 채운다** — 이게 M1 의 진짜 산출물이다
- M2 로 넘어가기 전에 표본 크기(P5 구간 영상 편수)를 먼저 센다

## 참조 및 산출물

**생성**
- `01-Data-Pipeline/README.md`
- `01-Data-Pipeline/scripts/youtube_analytics.py`
- `01-Data-Pipeline/troubleshooting/oauth-setup.md`
- `01-Data-Pipeline/.secrets/.gitignore`

**정정**
- `topic_starter.md` · `vl_prompts/roadmap_prompt.md` · 진행 계획 2벌 — OAuth 경로

**참조**
- [[2026-09-08 유튜브 채널 살리기 발표 브레인덤프 (원문)]]
- `Topics/The-AI-Powered-Creator/vl_materials/youtube-channel-growth-analysis.md`
- `AI/Tasks/Task Board.md` 「유튜브 채널 관리 애플리케이션」
