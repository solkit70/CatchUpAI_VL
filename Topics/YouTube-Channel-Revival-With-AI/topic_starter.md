---
title: "YouTube-Channel-Revival-With-AI — Topic Starter"
created: 2026-09-10 09:00:00
methodology: VibeLearn AI
tags:
  - cua-vl
  - vibelearn-ai
  - youtube
  - presentation
  - builders-lounge
---

# VibeLearn AI Topic Starter — YouTube-Channel-Revival-With-AI

> 브레인덤프 원문과 진행 계획을 바탕으로 채운 Topic 정보다.
> 원본: [[2026-09-08 유튜브 채널 살리기 발표 브레인덤프 (원문)]] · [[2026-09-08 토픽 진행 계획]]

## 📌 Topic 기본 정보

### Topic 이름

```
Topic 이름: YouTube-Channel-Revival-With-AI
```

### Topic 설명

```
설명: 구독자 4,300명 부근에서 횡보하다 마이너스로 꺾였던 유튜브 채널을 AI와 함께
되살린 과정을, 감이 아니라 YouTube Analytics 데이터로 검증해 정리한다.
2026-06 `The-AI-Powered-Creator` 토픽(채널 2년 여정 P1~P4)의 속편이며,
이번에는 P5 — 「되살리기 한 시즌」을 정의한다.
```

### 학습 목적

```
학습 목적:
- Builders Lounge 5차 모임(2026-09-16) 10분 발표 자료를 만든다 — 최우선 산출물
- "반응이 좋다"는 체감을 처음으로 숫자로 말할 수 있게 한다
- YouTube Analytics API 수집을 자동화해, 다음에도 다시 돌릴 수 있는 자산으로 남긴다
- 「사람이 병목인가」에 대한 자기 생각의 변화를 데이터와 함께 정리해 Substack 글로 쓴다
```

### 예상 학습 기간

```
예상 기간: 6일 (2026-09-10 목 ~ 2026-09-16 수) · 총 17시간
```

## 🎯 학습 목표

```
- [ ] YouTube Analytics API + Data API v3 를 OAuth 로 연결해 채널 지표를 직접 수집할 수 있다
- [ ] 일·주 단위 구독자 추이를 뽑아 횡보 시작 시점과 마이너스 전환 시점을 날짜와 숫자로 특정할 수 있다
- [ ] 가설 4개(자막 / 사람이 나오는 영상 / 분할 편집 / 조회수-구독 시차)에 대해
      데이터로 「맞다·아니다·알 수 없다」를 판정할 수 있다
- [ ] 1편의 Phase 분석 형식을 이어받아 P5 구간 분석 문서를 만들 수 있다
- [ ] 10분 발표용 슬라이드 10~12장과 발표 노트를 완성할 수 있다
```

## 🛠️ 학습 환경

### 운영 체제

```
OS: Windows 11 Home
버전: 10.0.26200
```

### 주요 도구 및 기술 스택

```
- Python 3.13
- google-api-python-client / google-auth-oauthlib  (YouTube API 인증·호출)
- YouTube Analytics API  (성과 지표)
- YouTube Data API v3    (영상 메타데이터)
- YouTube Studio CSV export  (노출·CTR — API 에 없는 지표)
- pandas (선택 — 집계)
- Obsidian (문서·발표 자료)
- 기존 자산: Google Cloud 프로젝트 + OAuth 클라이언트
  (`C:/Users/dougg/gcp-oauth.keys.json` — 캘린더 MCP 용으로 만들어 둔 것)
```

### 사전 지식 (Prerequisites)

```
필수:
- Python 기본 문법과 스크립트 실행
- OAuth 2.0 의 개념 (클라이언트 · 스코프 · 토큰)
- 유튜브 스튜디오 사용 경험 (지표 화면·CSV export 위치)

권장:
- pandas 로 표 집계
- 1편 토픽 `The-AI-Powered-Creator` 의 Phase 분석 형식
- 발표 슬라이드 작성 경험 (창발 6/26 발표)
```

## 📚 참조 자료

### 이 Topic 의 1차 자료

```
- 브레인덤프 원문: vl_materials/2026-09-08 유튜브 채널 살리기 발표 브레인덤프 (원문).md
- 진행 계획:      vl_materials/2026-09-08 토픽 진행 계획.md
```

### 이어받는 선행 토픽

```
- Ingest/CatchUpAI_VL/Topics/The-AI-Powered-Creator/
  - vl_materials/youtube-channel-growth-analysis.md   (P1~P4 Phase 분석 — P5 를 같은 형식으로 잇는다)
  - vl_materials/youtube-analytics/                   (CSV export 폴더 구조 — 같은 구조로 다시 받는다)
  - 06-Slide-Deck/                                    (발표 덱 형식 참고)
```

### 볼트 안의 근거 자료

```
- AI/Tasks/Task Board.md
  - 「유튜브 CSV 수동 분석」 — 가설 4개의 출처
  - 「유튜브 채널 관리 애플리케이션」 백로그 — 지표 한계(시청 페이지 구독만 집계) 정리
- Ingest/YouTube/_status  — 채널 아카이브 496편, API 결과 검산 기준
- _Settings_/Skills/video-subtitles/  — "스킬을 만들어서 AI로 자막을 달았다"의 증거물
- AI/RemotionStudio/*/video-slide-plan.md — 휴먼 터치의 물증 (AI 오류를 사람이 잡은 기록)
```

### 공식 문서

```
- YouTube Analytics API: https://developers.google.com/youtube/analytics
- YouTube Data API v3:   https://developers.google.com/youtube/v3
- Google Cloud Console:  https://console.cloud.google.com
```

## 🎓 학습 접근 방식

### 선호하는 학습 스타일

```
- [ ] 이론 먼저, 실습 나중
- [x] 실습 중심, 필요한 이론만
- [ ] 이론과 실습 병행
```

### 시간 투자 계획

```
- 총 학습 시간: 17시간 / 6일
- 학습 가능 요일: 매일 (발표가 9/16 수요일)
- 1회당 학습 시간: 2~5시간
```

### 특별히 집중하고 싶은 영역

```
- 실제 지표로 주장을 뒷받침하는 것 — 이 Topic 의 존재 이유다
- 재실행 가능한 수집 스크립트 (다음 분기에도 다시 돌릴 수 있어야 한다)
- 10분 안에 들어가는 발표 구성 — 덜어내는 연습
```

## ⚠️ 이 Topic 만의 제약

**① 마감이 고정돼 있다.** 2026-09-16 (수) 19:00 Builders Lounge 5차 모임.
학습이 늦어져도 발표는 그날이다. **M1 이 밀리면 범위를 줄인다.**

**② 같은 항목이 이미 세 번 밀렸다.** 「유튜브 CSV 수동 분석」은 9/5 → 9/6 → 9/9 로 연기됐고
**9/9 에도 착수하지 못했다.** 이 Topic 의 M1 이 바로 그 항목이다.

**③ 기억과 기록이 어긋난 지점이 이미 두 개 있다.**

| 항목 | 기억 | 기록 |
|---|---|---|
| 횡보 시작 구독자 수 | *"내 기억엔 4,300명 부근"* | 미확인 — 원문에도 *"정확하게 자료로 말해야 함"* |
| 되살리기 시작 시점 | 브레인덤프 *"한달(?)"* | Task Board 8/28 *"두 달 전 시작한"* |

**발표에서 숫자를 말하는 이상, 원문의 기억은 전부 데이터로 대조한 뒤에 쓴다.**

**④ 영상별 구독 지표에는 구조적 한계가 있다.** 「그 영상의 시청 페이지에서 구독을 누른 횟수」만
집계된다. 구독자 증가는 **기여의 하한선**으로만 읽고, 구독자 감소는 원인 추적에 쓰지 않는다.
