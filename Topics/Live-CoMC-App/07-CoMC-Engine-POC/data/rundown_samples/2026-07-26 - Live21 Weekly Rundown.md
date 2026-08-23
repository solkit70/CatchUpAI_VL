---
title: "2026-07-26 - Live21 Weekly Rundown"
created: 2026-07-26 09:30:00
updated: 2026-08-02 22:30:00
status: "📺 방송 완료 — 실험①②③ 전부 진행"
tags:
  - roundup
  - rundown
  - live-broadcast
links:
  - "[[Roundup/2026-07-26 - Weekly Progress and Planning]]"
  - "[[Roundup/2026-07-26 - Weekly Dashboard.canvas]]"
  - "[[Roundup/2026-07-28 - Daily Roundup]]"
  - "[[Roundup/2026-07-29 - Daily Roundup]]"
  - "[[Roundup/2026-07-30 - Daily Roundup]]"
  - "[[Roundup/2026-07-31 - Daily Roundup]]"
  - "[[Roundup/2026-08-01 - Daily Roundup]]"
  - "[[Roundup/2026-08-02 - Daily Roundup]]"
  - "[[Roundup/Weekly/2026-07-19~2026-07-26 - Claude Code]]"
  - "[[Research/2026-08-01 시민단체를 위한 AI 영상 유튜브 업로드 자료 (한국어) by Claude Code]]"
---

# AI in Action Live #21

**방송일**: 2026-08-02 (일) 오후 9시 (KST) / 시애틀 새벽 5시
**제목**: AI를 일상에 적용해 보는 다양한 실험
**주제**: **AI 실험 위주의 라이브 방송으로 복귀**

> **이번 방송의 성격 전환**: 지난 몇 주는 오프라인 행사 참가와 영상 제작 비중이 컸다.
> 이번 방송부터는 **라방을 실생활 적용을 위한 AI 실험 위주로 되돌린다.** 그래서 인사이트
> 코너를 따로 두지 않고, 실험 자체에서 나오는 이야기로 대체한다.

### 이번 실험 3축

| # | 실험 | 성격 |
|---|---|---|
| ① | **AI로 라방 보조 MC 앱 빌드** | 바이브 코딩, VibeLearn AI 시스템으로 진행 |
| ② | **기존 스킬을 OpenAI 신규 모델로 업데이트** | GPT-Live-Transcribe / GPT-Transcribe |
| ③ | **라방을 실생활 적용 AI 실험 위주로 전환** | 방송 운영 방향 자체의 전환 |

## 방송 순서

| 순서 | 파트 | 예상 시간 | 내용 |
|---|---|---|---|
| 0 | 방송 시작 전 | - | Capture 활성화, Rundown Canvas 작성 데모 |
| 1 | 1부: 지난 주 활동 | 20분 | Seattle Tech Week 5일 참가 + 유튜브 업로드 3건 |
| 2 | 2부: 내 주변 AI News | 10분 | Builders Lounge 4차 모임(8/6) 일정 확정 |
| 3 | 3부: 오늘의 실험 | 나머지 전부 | 실험 3축 중심 + 진행 중 Topic들 |
| 4 | 아웃트로 | - | 다음 주 예고, 구독 & 좋아요 |

> ⚠️ **기존 4파트 구성에서 "오늘의 인사이트" 코너를 뺐다.** 이번 주제가 "실험 위주로 복귀"이므로
> 인사이트를 따로 떼어 말하지 않고 실험 진행 중에 자연스럽게 다룬다. 되살리고 싶으면
> 아래 [보류된 인사이트 후보](#보류된-인사이트-후보-이번-방송-미편성) 참조.

---

## 0. 방송 시작 전

- [ ] GOBI Desktop Capture 활성화
- [ ] Fable/agent 세션 사용량 확인
- [ ] VS Code + Claude Code / Codex Extension 준비
- [ ] **이번 주 Rundown을 Canvas로 작성하는 것을 첫 데모로 진행**
- [ ] 🔴 **WA Excise Tax 신고 처리 여부 확인** — 7/31 마감 경과, 주말 처리 항목

### 첫 데모 — Rundown Canvas 작성

VS Code + Claude Code에서 실행할 프롬프트:

```
이번주 Rundown 문서를 Canvas 로 작성해 줘
C:\AI_study\2026\Changsoo_Vault\AI\Roundup\2026-07-26 - Live21 Weekly Rundown.md
```

> 🔴 **슬라이드 오타 주의**: 방송용 슬라이드에는 경로가 `2026-07-19 - Live20 Weekly Rundown.md`로
> 되어 있다. 지난주 파일이므로 **위 Live21 경로로 읽어야 한다.**

---

## 1부: 지난 주 활동 (20분)

> **이번 방송 커버리지**: ①Seattle Tech Week 2026 5일 연속 참가(7/27~31) ②유튜브 업로드 3건(Seattle Tech Week 일정 수립 KR/EN, NGO 실무자를 위한 AI 활용법)

### ① Seattle Tech Week 2026 — 5일 연속 참가

| 날짜 | 행사 |
|---|---|
| 7/27 (월) | AI Startup Secret Sauce with Startup425 and Level Up |
| 7/28 (화) | AI With Agency: Entering the Autonomous Era **by SAP** |
| 7/29 (수) | Startup425 Summit 3 · **Accelerator Demo Day** |
| 7/30 (목) | ACM Seattle KDD (Data Conclave) · 창발: AI Survival Guide |
| 7/31 (금) | INFORMS PNW · AI & the Future of Consumer Experiences by Biuty AI |

**말할 포인트**: 오프라인 활동이 유난히 활발했던 주였다. 대기업(SAP)과 스타트업(Startup425) 행사를 같은 주에 겪으면서 **AI를 어디에 놓는가**의 차이가 선명하게 보였다. 7/29 Demo Day에서는 Builders Lounge 멤버인 박세진님을 우연히 만나 Product 이야기를 나눴다.

### ② 유튜브 업로드 3건

| 영상 | 길이 | 링크 |
|---|---|---|
| Codex vs Claude Code : 이번엔 Codex Win (한국어) | 7:13 | https://youtu.be/EQ1I0YSfMvM |
| Codex vs Claude Code: Codex Win (English) | 7:00 | https://youtu.be/OjSXw0_4ihY |
| **NGO 실무자를 위한 AI 활용법** (8/1 업로드) | 22:22 | **https://youtu.be/IsmHWee25Ag** |

**말할 포인트**: NGO 영상은 인트로·아웃트로를 Remotion으로 새로 만들어 붙였고, 한국어 음성에 영어 자막을 달아 다국어 제목·설명까지 등록했다. 시민단체 실무자를 돕겠다는 제안이 목적이라 **신청 폼**을 설명란에 넣었다.

---

## 2부: 내 주변 AI News (10분)

> **이번 방송 커버리지**: ①Builders Lounge 4차 모임(8/6) 일정·발표자 확정

### Builders Lounge 4차 모임 — 8월 6일 (목) 확정

**일시**: 2026년 8월 6일(목) 19:00~21:00 (문은 18:30 개방)
**장소**: Bellevue City Hall, Room 1E-110 (온/오프 하이브리드)

| 순서 | 내용 | 시간 |
|---|---|---|
| Main Speaker | **김성수님** — Vibe Coding 이후의 시대: 기술과 세계관의 연합으로 탄생한 HebronGuide | 20~30분 |
| Bila AI Agent 소식 | Changsoo Park · 강민석님 | 10분 |
| 자유 Product 소개 | Dokyu Lee님(Quant) / 손민수님(시스템 장애 대응 AI 에이전트 업데이트) / 박창수(유튜브 채널 회생용 Skill) | 각 5~10분 |
| [번외] | 김성진님 — ICML 2026(국제머신러닝학회) 후기 | 짧게 |

📌 전체 공지 및 RSVP: Gobi Space 공지 페이지

**말할 포인트**: 이번 포스터는 **메인 스피커이신 김성수님이 직접 만들어 주셨다.** 비개발자 출신으로 목회 활동을 하시면서 "환대"라는 주제로 재외 한인 정착 커뮤니티 플랫폼 HebronGuide를 만드신 분이라, Builders Lounge 멤버 대부분인 개발자·IT 엔지니어에게 새로운 시각을 줄 발표가 될 것 같다.

---

## 3부: 오늘의 실험 (나머지 시간 전부)

> **이번 방송 커버리지**: ①AI로 라방 보조 MC 앱 만들기 ②기존 스킬을 OpenAI 신규 Transcribe 모델로 업데이트 — 이 두 개를 메인으로 진행하고, 시간이 남으면 아래 대기 목록에서 이어간다

### ★ 실험 1 — AI로 라이브 방송 보조 MC 앱 만들기

**진행 방식**: Claude Code **Plan 모드**로 시작 → VibeLearn AI 시스템으로 Topic화

**투입할 프롬프트 요지**:

> 라이브 방송을 같이 진행할 AI 보조 MC 앱을 만들려고 합니다. VibeLearn AI 시스템을 사용해서
> 학습하면서 최종 목표물을 이 앱 완성으로 끝내는 프로젝트로 진행합니다.
>
> **주요 기능**: 제가 목소리로 특정 주제나 부문에 대해 이야기해 달라고 하면, 이 보조 MC 앱이
> 방송을 진행하는 것.
>
> **참조할 문서 구조** (모두 `AI/Roundup/`에 `YYYY-MM-DD`로 시작):
> - `YYYY-MM-DD - Weekly Progress and Planning.md` — 주간 일정 관리
> - `YYYY-MM-DD - Weekly Dashboard.canvas` — 주간 대시보드
> - `YYYY-MM-DD - Live[N] Weekly Rundown.md` — 방송용 문서
> - `YYYY-MM-DD - Daily Roundup.md` — 매일 기록
>
> 보조 MC 앱은 이 문서들을 참조해서 지시에 따라 방송을 진행하면 됩니다.
> 방송 도구는 VS Code의 Claude Code와 Codex Extension을 사용합니다.

**말할 포인트**: 이 앱이 완성되면 **오늘 이 Rundown 문서 자체가 앱의 입력**이 된다. 지금은 내가 문서를 보며 진행하지만, 앞으로는 앱이 이 문서를 읽고 진행을 도와주는 구조다.

### ★ 실험 2 — 기존 스킬을 OpenAI 신규 Transcribe 모델로 업데이트

OpenAI가 지난주 발표한 신규 전사 모델 2종:

| 모델 | 용도 | 성능 |
|---|---|---|
| **GPT-Live-Transcribe** | 저지연 실시간 전사 | WER 11.65% → **9.60%** |
| **GPT-Transcribe** | 완료된 오디오 파일·배치 처리 | WER 15.21% → **8.98%** |

기존 Whisper 대비 개선되었고, **컨텍스트를 함께 제공하면 정확도가 더 올라간다** (녹음 관련 자유 형식 설명, 고유명사·전문용어 키워드, 예상 언어, 앞선 전사 결과).

**작업 범위**:
- [ ] `video-subtitles` 스킬 — Whisper API → GPT-Transcribe 교체 검토
- [ ] `video-add-chapters`의 `transcribe_video.py` 교체 검토
- [ ] **컨텍스트 주입 기능 연결** — 최근 만든 `glossary.json`의 `prompt_terms`를 그대로 넘길 수 있는지 확인
- [ ] 다른 스킬 중 최신 기능으로 업데이트할 것이 있는지 조사

> 💡 **연결 포인트**: 7/31~8/1에 `video-subtitles` 스킬에 **오인식 방지 3단 체계**(prompt biasing →
> glossary 자동 교정 → 사용자 검토 게이트)를 넣었다. 신규 모델이 컨텍스트 주입을 공식 지원하므로
> 1단계(prompt biasing)를 모델 API 차원에서 제대로 쓸 수 있게 된다.

### ✅ 방송 후 결과 (2026-08-02)

실험①②③ 모두 실제로 진행됐고, 대기목록 #3(Builders Lounge 발표 준비)까지 이어서 완주했다.

| # | 실험 | 결과 |
|---|---|---|
| ① | 라방 보조 MC 앱 만들기 | **Live-CoMC-App** Topic 신규 시작(12주/90h), M1(개념·Rundown 파싱 계약)·M2(파이프라인 아키텍처·App Boundary) 완료 |
| ② | GPT-Transcribe/GPT-Live-Transcribe 업데이트 | `video-add-chapters`·`video-cleaning`·`video-full-process`·`video-subtitles`·`youtube-channel-archiver` 5개 스킬에 전환 가이드 반영 |
| 대기#3 | Builders Lounge 발표 준비 | **Builders-Lounge-AI-Guide-Presentation** Topic M1~M4 전체 완주 — 8/6 발표 준비 완료 |

→ **Source**: [[Roundup/2026-08-02 - Daily Roundup|8/2 Daily Roundup]]

### 대기 목록 (시간이 남으면)

| # | 항목 | 관련 Topic |
|---|---|---|
| 3 | Builders Lounge 발표 준비 | — |
| 4 | 강의 신청 폼에 **NGO 실무자 신청 옵션** 추가 (현재 시니어 대상만) | — |
| 5 | Builders Lounge 공지 및 News Letter 작업 | — |
| 6 | Databricks AI 세미나 녹화 영상 자막 편집 → 유튜브 업로드 | — |
| 7 | Seattle Tech Week 녹화 영상 자막 작업 → 편집 → 업로드 | — |
| 8 | Bila AI Agent M2 진행 (Slack 이슈는 개발자와 협의, GitHub 테스트 지속) | `Bila-AI-Agent` |
| 9 | AI와 글쓰기 — 피터 틸 vs 내 관점 대결 | `Peter-Thiel-Vision` |
| 10 | Slack 채널 내용 자동으로 가져오기 | `Slack-Builders-Lounge-Automation` |
| 11 | catchupai.net에 Builders Lounge 관련 내용 추가 | — |
| 12 | 진행 중 기타 Topic | `GOBI-Guiding`, `VibeCoding-Onboarding-Program`, `Vibe-Guiding-VSCode` |

---

## 아웃트로

- 다음 주 예고: 보조 MC 앱 진행 상황
- **8/6(목) Builders Lounge 4차 모임** 참석 안내
- NGO 실무자를 위한 AI 활용법 영상과 **신청 폼** 안내
- 구독 & 좋아요 CTA

---

## 보류된 인사이트 후보 (이번 방송 미편성)

> 이번 방송은 실험 위주로 가느라 인사이트 코너를 뺐다. 아래는 지난주 Daily Roundup에서
> 쌓인 후보이며, 실험 진행 중 자연스럽게 언급하거나 다음 방송으로 넘긴다.

- **대기업 AI vs 스타트업 AI** — SAP 세미나는 기존 Product 중심, 스타트업 행사는 없는 것을 만들려는 야생성
- **AI는 일을 줄이는가, 더 만드는가** — Usage Limit을 보며 새 task를 계속 만들어 burn out되는 역설
- **완성된 도구를 기다리지 않고 지금 움직이기** — Bila AI 매칭을 기다리지 않고 멤버 간 1:1 교류부터
- **AI Context 데이터 관리의 병목** — GitHub이 매칭 AI Agent를 API로 제공하면 어떨까 하는 제안
- **Vibe Guiding = Event Driven Process** — 이벤트 발생 시 AI Agent가 가이드하는 구조
- **문제를 어떤 레벨로 정의하는가** — "화면을 읽어라" vs "데이터 원천을 찾아라"

## 주간 영상 후보 (이번 방송 코너 미편성)

| 후보 | 상태 | 메시지 |
|---|---|---|
| Seattle Tech Week 일정 수립 | ✅ 업로드 완료 | Codex Win — 화면이 아니라 데이터 원천을 찾아라 |
| NGO 실무자를 위한 AI 활용법 | ✅ 업로드 완료 | 자료 없이 시작해 하루 만에 기획안까지 |
| AI와 사람의 업무 리듬 | 제작 중단 | 보강 아이디어 정리 후 재개 예정 (`ai-workload-0728`) |
| 대기업 AI vs 스타트업 AI | 후보 | 같은 주에 겪은 두 행사의 태도 차이 |
| Vibe Guiding = Event Driven Process | 후보 | 이벤트 기반 AI 가이드 구조 |
| 보조 MC 앱 만들기 (Live-CoMC-App) | 진행 중 (M1~M2 완료) | 12주 프로젝트 완성 과정 자체가 영상 소재, 완료 시점에 편집 |

---

*2026-08-01 방송용 슬라이드 확정본을 반영해 최종본으로 갱신. 1~3부 커버리지를 모두 확정했고,
"오늘의 인사이트" 코너는 이번 주제(실험 위주 복귀)에 맞춰 미편성으로 두고 후보만 보존했다.*

*2026-08-02 방송 완료. 실험①②③ 전부 진행했고 대기목록 #3까지 이어서 완주했다 — 자세한 결과는
[3부 방송 후 결과](#✅-방송-후-결과-2026-08-02) 및 [[Roundup/2026-08-02 - Daily Roundup|8/2 Daily Roundup]] 참고.*
