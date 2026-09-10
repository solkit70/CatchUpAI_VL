---
title: "M1 — 데이터 파이프라인과 P5 정의"
created: 2026-09-10 10:30:00
status: 진행 중
tags:
  - vibelearn-ai
  - youtube-analytics
---

# M1 — 데이터 파이프라인과 P5 정의

**상태**: 🔄 진행 중 (2026-09-10 시작)
**예상 학습 시간**: 5시간
**난이도**: ⭐⭐⭐

> 이 모듈이 이 Topic 의 바닥이다. 여기서 나온 숫자로 발표의 모든 주장이 선다.
> **최소 완료선**은 둘 — ① CSV 4종 확보 ② 횡보·마이너스 시점을 날짜와 숫자로 특정.

## 📚 학습 순서

1. [concepts/analytics-api-basics.md](concepts/analytics-api-basics.md) — Analytics API 와 Data API 는 무엇이 다른가, `dimensions × metrics` 가 왜 CSV 와의 결정적 차이인가
2. [concepts/metric-limitations.md](concepts/metric-limitations.md) — 🔴 **읽고 시작한다.** 영상별 구독 지표를 왜 「기여의 하한선」으로만 읽어야 하는지
3. [troubleshooting/oauth-setup.md](troubleshooting/oauth-setup.md) — **실습 2의 실행 안내.** Console 클릭 순서와 예상되는 막힘
4. [scripts/youtube_analytics.py](scripts/youtube_analytics.py) — 수집 스크립트. 실습 3에서 돌린다
5. [analysis/phase5-growth-analysis.md](analysis/phase5-growth-analysis.md) — 이 모듈의 결론. 1편 형식을 그대로 잇는다

## 🎯 실습 3개

| # | 과제 | 난이도 | 시간 | 지금 상태 |
|---|---|---|---|---|
| 1 | **YouTube Studio CSV 확보** | ⭐ | 30분 | ⏳ 사용자 작업 |
| 2 | **OAuth 연결과 첫 호출** | ⭐⭐ | 60분 | ⏳ Console 설정 대기 |
| 3 | **수집 스크립트와 P5 분석** | ⭐⭐⭐ | 120분 | 🔄 스크립트 작성 완료, 실행 대기 |

> ⏰ **실습 2에서 30분 넘게 막히면 중단하고 실습 3을 CSV 로 진행한다.**
> 발표가 API 설정에 인질로 잡히면 안 된다.

## 📁 폴더

```
01-Data-Pipeline/
├── README.md                     ← 지금 이 파일
├── concepts/
│   ├── analytics-api-basics.md
│   └── metric-limitations.md
├── scripts/
│   └── youtube_analytics.py      — 재실행 가능한 수집기
├── data/
│   ├── youtube-analytics/        — Studio CSV (1편과 같은 구조)
│   └── raw/                      — API 응답 원본 JSON
├── analysis/
│   └── phase5-growth-analysis.md — P5 구간 분석
├── troubleshooting/
│   └── oauth-setup.md
└── .secrets/                     — 🔴 토큰. .gitignore 로 제외됨
```

## ✅ Definition of Done

- [ ] 🟥 **CSV 4종을 1편과 같은 폴더 구조로 확보** ← 최소 완료선
- [ ] 🟥 **횡보 시작·마이너스 전환 시점을 날짜와 숫자로 특정** ← 최소 완료선
- [ ] OAuth 연결 성공 — `reports.query` 200 응답
- [ ] 노출·CTR 이 API 에 있는지 없는지 **판정 기록**
- [ ] `youtube_analytics.py` 로 4개 조합 중 3개 이상 수집 자동화
- [ ] `phase5-growth-analysis.md` 초안 완성 (1편 표 양식)
- [ ] 496편 아카이브와 대조 검산 완료
- [ ] WorkLog + Daily Retrospective 작성

## 🔴 이 모듈에서 반드시 확인할 것

발표에서 숫자를 말하는 이상, **브레인덤프의 기억은 전부 데이터로 대조한 뒤에 쓴다.**

| 항목 | 기억 | 데이터 |
|---|---|---|
| 횡보 시작 구독자 수 | *"내 기억엔 4,300명 부근"* | ⏳ |
| 마이너스 전환 시점 | 미상 | ⏳ |
| 되살리기 시작 시점 | 원문 *"한달(?)"* vs Task Board *"두 달 전"* | ⏳ |
| 전고점 돌파 이후 추이 | 8/28 4,304명 | ⏳ |

## 🔗 이동

- **이전**: (없음 — 첫 모듈)
- **다음**: [02-Hypothesis-Testing/](../02-Hypothesis-Testing/README.md) — 가설 검증
- **로드맵**: [20260910_RoadMap_YouTube-Channel-Revival-With-AI.md](../vl_roadmap/20260910_RoadMap_YouTube-Channel-Revival-With-AI.md)
