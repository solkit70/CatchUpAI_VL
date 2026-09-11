---
title: "Analytics API 와 Data API — 무엇이 다르고, 왜 CSV 로는 안 되는가"
created: 2026-09-10 16:30:00
tags:
  - m1
  - youtube-api
  - concepts
---

## 왜 API 를 배워야 하나 — CSV 로 시작했다가 막힌 지점

이 조사는 원래 **YouTube Studio 에서 CSV 를 내려받아 보는 것**으로 계획돼 있었다.
실제로 받아 봤고, **두 번 막혔다.**

**① 파일 마지막 줄에 이렇게 적혀 있다.**

```
Showing top 500 results
```

이 채널은 영상이 500편이 넘는다. **100편 넘게 통째로 빠진 채 「전체 분석」을 하게 된다.**
더 나쁜 것은 **오류가 안 난다**는 점이다. 파일은 정상적으로 열리고 숫자도 그럴듯하다.

**② 원하는 조합을 만들 수 없다.**
CSV 는 스튜디오가 **미리 정해 둔 표**다. 「롱폼만」「Shorts 만」「이 영상들만 골라서」
같은 조건을 걸 수 없고, 기간을 바꾸려면 매번 다시 내려받아야 한다.

**API 는 이 두 가지를 다 푼다.** 전체를 받을 수 있고, 조건을 코드로 쓸 수 있다.

## API 가 두 개다 — 역할이 다르다

**하나로는 안 된다.** 둘을 이어 붙여야 원하는 표가 나온다.

| | **YouTube Analytics API** | **YouTube Data API** |
|---|---|---|
| 주는 것 | **성과 지표** — 조회·시청시간·구독 증감 | **메타데이터** — 제목·공개일·길이·공개 상태 |
| 안 주는 것 | 제목조차 안 준다 (영상 ID 만) | 조회수는 「누적 총합」뿐, 기간별이 없다 |
| 호출 | `reports().query(...)` | `videos().list(...)` · `playlistItems().list(...)` |
| 스코프 | `yt-analytics.readonly` | `youtube.readonly` |

> 🔴 **Analytics API 는 영상 제목을 모른다.** `dimensions=video` 로 받으면
> `["dQw4w9WgXcQ", 1234, 56]` 같은 행이 온다. 사람이 읽을 표를 만들려면
> **Data API 로 제목을 따로 받아 ID 로 이어 붙여야** 한다.

## 핵심 개념 — `dimensions × metrics`

Analytics API 의 요청은 **「무엇을 기준으로 쪼개서(dimensions) 무엇을 셀 것인가(metrics)」** 다.
이 두 개를 바꾸는 것만으로 완전히 다른 표가 나온다. **CSV 와의 결정적 차이가 여기다.**

| dimensions | 나오는 표 | 이 조사에서 어디에 썼나 |
|---|---|---|
| `day` | 날짜별 한 줄 | **횡보 시작·마이너스 전환 시점 특정** |
| `month` | 달별 한 줄 | Phase 별 월평균 비교 |
| `video` | 영상별 한 줄 | 가설 검증 전부 |
| `insightTrafficSourceType` | 유입 경로별 한 줄 | 작전 2 전후 비교 |
| *(생략)* | 채널 전체 한 줄 | 합계 확인 |

```python
# 날짜별 — 시계열
ya.reports().query(
    ids="channel==MINE", startDate=start, endDate=end,
    metrics="views,subscribersGained,subscribersLost,estimatedMinutesWatched",
    dimensions="day", sort="day",
).execute()

# 영상별 — 같은 metrics, dimensions 만 바꿨다
ya.reports().query(
    ids="channel==MINE", startDate=start, endDate=end,
    metrics="views,averageViewDuration,averageViewPercentage,subscribersGained",
    dimensions="video", sort="-views", maxResults=200,
).execute()
```

**응답은 `columnHeaders` + `rows` 형태**라, 열 이름과 값을 직접 지퍼처럼 맞춰야 쓸 수 있다.

```python
def rows_of(resp):
    heads = [h["name"] for h in resp.get("columnHeaders", [])]
    return [dict(zip(heads, r)) for r in resp.get("rows", [])]
```

## 🔴 `ids="channel==MINE"` 이 가장 위험한 한 줄이다

`MINE` 은 **인증된 신원의 채널**로 풀린다. 한 구글 계정에 채널이 여러 개면
**동의 과정의 채널 선택 화면을 무심코 넘겼을 때 엉뚱한 채널의 지표를 받아 온다.**

이 계정에는 채널이 **다섯 개** 있었다 — Wild Forager(기본) · 미생 영어 · AI Madang ·
Joosik Investment · **Catch Up AI(분석 대상)**.

**숫자가 그럴듯하게 나오기 때문에 발표 직전까지 눈치채기 어렵다.**
그래서 스크립트가 매 실행마다 채널을 확인하고, 다르면 **그 자리에서 멈춘다.**

```
🔴 엉뚱한 채널로 인증됐다.
   받은 채널  : Wild Forager (@wildforager)
   기대한 채널: Catch Up AI (@catchupai)
```

> 📌 **데이터 분석에서 가장 무서운 건 틀린 답이 아니라 그럴듯한 답이다.**

## 전체를 받는 방법 — 세 단계로 이어 붙인다

500편 제한도 200행 제한도 이 순서로 우회한다.

```
① Data API      업로드 재생목록 페이징 → 전체 영상 ID
② Analytics API filters=video== 로 200개씩 끊어 → 지표
③ Data API      videos.list 50개씩 → 제목·공개일·길이
```

**각 단계에 다른 상한이 있다는 것**이 핵심이다.

| 단계 | 상한 | 대응 |
|---|---|---|
| ① 재생목록 | 페이지당 50 | `nextPageToken` 으로 반복 |
| ② 지표 | **행 200** | `filters=video==id1,id2,...` 로 200개씩 |
| ③ 메타 | 요청당 50 | 50개씩 끊어 반복 |

**⚠️ ①에서 중복이 나온다.** 자세한 것은
[metric-limitations.md](metric-limitations.md) 「API 가 같은 영상을 두 번 준다」 참조.

## 스코프 세 개 — 무엇 때문에 필요한가

```python
SCOPES = [
    "https://www.googleapis.com/auth/yt-analytics.readonly",           # 성과 지표
    "https://www.googleapis.com/auth/yt-analytics-monetary.readonly",  # 수익
    "https://www.googleapis.com/auth/youtube.readonly",                # 메타데이터
]
```

**수익 스코프는 선택이다.** 없어도 나머지는 다 된다. 다만 광고 수익 추이를 보려면 필요하고,
🔒 **받은 수익 데이터는 `data/` 에 남고 그 폴더는 `.gitignore` 로 빠져 있다** —
이 레포는 공개되기 때문이다. **데이터를 갖는 것과 공개하는 것은 다른 결정이다.**

> ⚠️ 스코프를 추가한 뒤에는 **기존 토큰을 지우고 다시 인증**해야 한다.
> 안 그러면 옛 토큰이 그대로 쓰여 새 권한이 안 붙는다.

## 이어서 읽을 것

- 🔴 [metric-limitations.md](metric-limitations.md) — **이 API 가 안 주는 것과 잘못 읽기 쉬운 것.** 코드를 돌리기 전에 읽는다
- [troubleshooting/oauth-setup.md](../troubleshooting/oauth-setup.md) — 콘솔 클릭 순서와 예상되는 막힘
- [scripts/youtube_analytics.py](../scripts/youtube_analytics.py) — 위 내용이 그대로 구현돼 있다
