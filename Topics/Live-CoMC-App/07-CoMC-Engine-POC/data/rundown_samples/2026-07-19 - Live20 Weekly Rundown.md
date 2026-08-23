---
title: "2026-07-19 - Live20 Weekly Rundown"
created: 2026-07-20 09:10:00
tags:
  - roundup
  - rundown
  - live-broadcast
links:
  - "[[Roundup/2026-07-19 - Daily Roundup]]"
  - "[[Roundup/2026-07-20 - Daily Roundup]]"
  - "[[Roundup/2026-07-21 - Daily Roundup]]"
  - "[[Roundup/2026-07-22 - Daily Roundup]]"
  - "[[Roundup/2026-07-23 - Daily Roundup]]"
  - "[[Roundup/2026-07-24 - Daily Roundup]]"
  - "[[Roundup/2026-07-25 - Daily Roundup]]"
  - "[[Roundup/2026-07-19 - Weekly Progress and Planning]]"
  - "[[Roundup/2026-07-19 - Weekly Dashboard.canvas]]"
  - "[[Roundup/Weekly/2026-07-13~2026-07-19 - Codex]]"
---

# 🎙️ AI in Action Live #20

**방송일**: 2026-07-26 (일) 오후 9시 (KST) · Catch Up AI 유튜브  
**제목**: AI를 일상에 적용해 보는 다양한 실험  
**주제**: 나의 작업을 어떻게 자동화 하고 있나?

> 방송 썸네일이 확정되며 이번 방송의 Top 3 실험도 함께 확정됐다 — ①공부하면서 기록하기, 기록을 영상으로 만들기 ②모든 것을 AI로 자동화, 나는 공부만 하면 됨 ③AI와 함께 시민단체 이벤트 기획해 보기. 새로운 것을 새로 벌이기보다, 지금 진행 중인 작업(Seattle Tech Week 기록 영상화, Databricks 자막 작업, 광복절 기념식 AI 섹션 준비)을 그대로 이어서 보여주는 방송이다. 세 실험 모두 "유튜브 영상을 만들기 위한 콘텐츠 제작·수집 과정을 어떻게 자동화하는가"라는 같은 질문의 다른 사례라는 점에서, 평소 하는 작업을 골고루 보여줄 수 있는 회차다.

## 방송 순서 (초안)

| 순서 | 파트 | 예상 시간 | 내용 |
|---|---|---|---|
| 0 | 방송 시작 전 | - | Capture, 캘린더, 주간 영상 후보 확인 |
| 1 | 1부: 지난 주 활동 | TBD | 공부·실험은 재미있지만 기록·영상화는 재미없고 시간이 오래 걸렸다는 문제의식 |
| 2 | 2부: 오늘의 인사이트 | TBD | VibeLearn AI와 AI4PKM으로 재미없는 부분을 자동화하는 구조, Codex Win, 로드맵 우선 설계(시작은 신중하게·재개는 간편하게) |
| 3 | 3부: 내 주변 AI News | TBD | Seattle Tech Week, Spark + AI 참석, BigHug 현장 준비, 페더럴웨이 한인회 광복절 기념식 AI 접목 논의 |
| 4 | 4부: 오늘의 실험 | TBD | Seattle Tech Week 기록 영상화, Databricks 자막 입히기, 광복절 AI 섹션 Research, Bila AI Agent M2 상태, 피터틸 관점 대결 글쓰기, Slack 채널 자동 수집 M1 — 6개 항목, 진행 방식·시작 프롬프트까지 준비 완료 |
| 5 | 주간 영상 | TBD | 공부 기록을 바탕으로 AI가 동영상 제작까지 이어가는 흐름 정리 |
| 6 | 아웃트로 | - | 다음 주 예고 |

## 방송 시작 전

- [ ] GOBI Desktop Capture 활성화
- [ ] Live20 시작 전 Fable/agent 세션 사용량 확인
- [ ] `주간 영상` 후보 확인
- [ ] Seattle Tech Week 참석 결정 상태 확인
- [ ] Seattle Tech Week 기록 자료와 Databricks/Spark + AI 녹화 영상 위치 확인

## 1부: 지난 주 활동 (시간 미정)

> **이번 방송 커버리지**: ①공부와 실험은 재미있었다 ②기록과 영상화는 재미없었고 시간이 더 걸렸다 ③그래서 재미없는 일을 AI 자동화 대상으로 삼았다

이번 방송의 출발점은 예전에 영상을 만들면서 반복해서 느낀 피로감이다. 공부하고 실험하는 과정은 배움이 있어서 재미있었지만, 그 과정을 기록하고 다시 영상으로 만드는 작업은 재미가 없었다. 더 큰 문제는 재미없는 일이 재미있는 일보다 더 오래 걸렸다는 점이다. 그래서 "내가 하고 싶은 일은 공부와 실험이고, 기록·정리·영상화는 누군가 대신 해 주면 좋겠다"는 문제의식이 생겼고, 그 재미없는 부분을 AI로 자동화하는 방향으로 작업이 이어졌다.

이번 주 활동은 이 문제의식을 실제 시스템으로 끌고 온 과정이다. VibeLearn AI는 공부하는 과정과 기록을 자동화하고, AI4PKM은 그 기록을 볼트 안에서 관리하며 Skill과 워크플로우를 오케스트레이션한다. 7/20~7/23에는 Build with AI Remotion 영상 제작, VibeCoding-Onboarding-Program M1 구축, Seattle Tech Week 일정 자동화, Spark + AI / Databricks Bellevue 참석 기록, BigHug 관련 현장 준비가 이어졌다. 이 모든 활동은 단순히 "많이 했다"가 아니라, 공부·실험·현장 활동이 자동으로 기록되고 다시 콘텐츠 제작 재료가 되는지 검증하는 한 주로 정리한다. → [[Roundup/2026-07-23 - Daily Roundup|7/23 Daily Roundup]]

그 결과물 중 하나가 7/24에 완성됐다. Fable Credit 실험 영상이 한국어·영어 두 버전 모두 렌더링부터 유튜브 업로드, SNS 홍보 글까지 하루 안에 끝났다. Fable 5를 유료로 실측한 과정(하루 반나절 새 한도 4번 인상, $100 소진)을 담은 영상으로, "재미없는 정리·영상화를 AI가 대신한다"는 이번 주 메시지를 실제 완결된 콘텐츠로 보여주는 사례다. → [[Research/2026-07-24 Fable Credit 실험 영상 유튜브 업로드 자료 (한국어) by Claude Code|한국어 업로드 자료]] · [[Research/2026-07-24 Fable Credit Experiment Video - YouTube Upload Assets (English) by Claude Code|English 업로드 자료]]

> 🎙️ **멘트**: "이 영상들, 제가 어떻게 만드는지 궁금하지 않으세요? 그 만드는 과정을 오늘 4부 '오늘의 실험'에서 실제로 보여드리겠습니다." — 지난 주 완성한 결과물(1부)에서 그 결과물이 나오는 과정(4부)으로 자연스럽게 넘어가는 연결 멘트.

## 2부: 오늘의 인사이트 (시간 미정)

> **이번 방송 커버리지**: ①재미있는 일과 재미없는 일 분리하기 ②VibeLearn AI + AI4PKM 자동화 구조 ③Codex Win — 화면 읽기에서 데이터 흐름 찾기로 ④로드맵 우선 설계 — 시작은 신중하게, 재개는 간편하게

### ① 재미있는 일과 재미없는 일 분리하기

이번 방송의 핵심 인사이트는 "모든 일을 AI로 한다"가 아니라, 사람이 계속 해야 할 일과 AI에게 넘길 일을 분리하는 것이다. 사람에게 남겨야 할 일은 무엇을 공부할지 정하고, 실제로 해 보고, 그 과정에서 느낀 의미를 판단하는 부분이다. 반대로 AI에게 넘기고 싶은 일은 공부 중 나온 기록을 정리하고, 흩어진 자료를 연결하고, 영상 제작에 필요한 스크립트·슬라이드·자막·업로드 자료로 바꾸는 반복 작업이다.

이 구분이 중요한 이유는 자동화의 목적이 생산량 자체가 아니기 때문이다. 자동화의 목적은 사람이 재미있고 배움이 있는 일에 더 오래 머물 수 있게 하는 것이다. 그래서 이번 방송에서는 "나는 공부만 하면 되고, 기록과 영상화는 AI가 맡는다"는 방향을 메인 메시지로 둔다.

### ② VibeLearn AI + AI4PKM 자동화 구조

VibeLearn AI는 학습 Topic을 잡고, 공부 과정과 실험 로그를 남기며, 그 흐름을 다음 학습 단계로 이어 주는 역할을 한다. AI4PKM은 그 기록이 단순한 메모로 흩어지지 않도록 볼트 안에서 관리하고, Skill·템플릿·오케스트레이션을 통해 필요한 작업으로 연결한다. 두 시스템을 함께 쓰면 "공부했다"에서 끝나는 것이 아니라, 공부 기록이 Rundown, 영상 스크립트, Remotion 구성, 자막 작업, SNS 홍보 자료로 이어지는 파이프라인이 된다.

방송에서는 이 구조를 추상 설명으로만 다루지 않고, 이번 주 실제 사례로 보여준다. Seattle Tech Week 일정 관리는 VibeLearn AI 방식으로 조사·선정·캘린더 반영까지 진행했고, 그 기록을 바탕으로 AI에게 동영상 제작을 맡겨 볼 수 있다. Spark + AI / Databricks Bellevue 녹화 영상은 Remotion 자막 작업으로 이어가며, 기존 녹화 콘텐츠를 다시 공개 가능한 영상 자산으로 바꾸는 실험으로 다룬다.

### ③ Codex Win — 화면 읽기에서 데이터 흐름 찾기로

7/19의 핵심 인사이트는 Seattle Tech Week 조사에서 나왔다. Claude Code는 Luma 허브 페이지를 찾았지만, 동적 웹앱에 렌더링되는 이벤트별 세부 시간·장소·링크를 안정적으로 수집하지 못했다. 처음에는 사용자가 화면 캡처를 제공해 사람이 데이터 접근 병목을 메웠다.

Codex는 같은 문제를 "화면에 보이는 정보를 읽기"가 아니라 "Luma가 이벤트 데이터를 가져오는 원천 찾기"로 바꾸었다. 그 결과 Luma 공개 JSON API를 찾아 7/19 당시 전체 237개 이벤트와 AI 태그 74개를 자동 수집했고, 7/24 재확인에서는 현재 예정 행사 242개와 AI 태그 77개까지 확인했다. 이 사례는 AI Agent의 성패가 모델 능력만이 아니라 문제 정의와 데이터 접근 방식에 달려 있음을 보여준다. 결론 문장: **이번 건은 Codex Win**. → [[Ingest/CatchUpAI_VL/Topics/Seattle-Tech-Week-2026/04-Process-Notes/claude-code-to-codex-automation|Codex 자동화 프로세스 노트]]

### ④ 로드맵 우선 설계 — 시작은 신중하게, 재개는 간편하게

4부 "오늘의 실험" 슬라이드를 준비하면서 실제로 확인된 인사이트다. VibeLearn AI는 Topic을 시작할 때 먼저 전체 로드맵을 세우고, 이후 모듈(M1, M2...)마다 산출물과 WorkLog를 남기며 진행한다. 이 구조 덕분에, 몇 주씩 손을 놓았던 Topic도 다시 시작할 때 긴 설명이 필요 없다.

오늘 방송 준비 중 실제로 이 방식을 검증했다. Bila-AI-Agent(마지막 세션 7/5), Peter-Thiel-Vision(7/12), VibeCoding-Onboarding-Program(7/21), Obsidian-Omnisearch-Google-CMDS(6/28), Vibe-Guiding-VSCode(5/10) — 짧게는 5일, 길게는 12주 가까이 비어 있던 Topic들 모두 "OOO 학습 작업을 진행해줘" 한 줄만으로 AI가 Roadmap과 최신 WorkLog를 읽고 다음 단계를 스스로 파악해 이어갈 수 있는 상태였다. (예외적으로 Bila-AI-Agent는 대화로만 공유되고 아직 파일에 기록되지 않은 최신 상태(Google Drive 버그 fix)가 있어, 그 한 줄만 프롬프트에 보탰다 — 이것도 "파일에 없는 정보는 AI가 모른다"는 같은 원칙을 반대로 보여주는 사례다.)

**단, 대가가 있다.** 이 간편함은 처음 로드맵을 세울 때 얼마나 신중했는지에 달려 있다. 시작 단계에서 프롬프트를 자세히 쓰고 필요한 자료를 충분히 모아 둘수록, 로드맵과 WorkLog가 정확해지고, 나중에 재개할 때 AI가 헤매지 않는다. 반대로 GOBI-Guiding처럼 초기 로드맵만 세우고 M1에서 멈춘 Topic은 재개 기준 자체가 모호해질 수 있다(이 경우는 실패가 아니라 GOBI Desktop 플랫폼 성숙도에 막힌 외부 요인이지만, 원칙은 동일하다). **결론: 시작은 신중하게, 재개는 간편하게 — 이 둘은 로드맵 하나로 연결된다.**

### 추가 후보 (미확정) — BigHug AI/Bila AI: 흩어진 커뮤니티 문서를 요약·보고하는 운영 보조자

7/22의 핵심 인사이트는 BigHug 행사 준비 과정에서 나왔다. 현재 BigHug는 K-pop 추석행사 준비 문서와 자료를 메신저로 주고받고 있는데, 이런 방식은 나중에 찾기 어렵고 그때그때 읽어야 하는 부담도 크다. GobiSpace에서 개발 중인 Bila AI 기능을 BigHug 준비 공간에 적용하면, 자료를 한곳에 올려 두고 BigHug AI가 필요한 내용을 요약·보고하는 구조를 만들 수 있다. 이 구상은 BigHug 자체 시스템 구축, GOBI와의 협업, grant project 후보로 확장될 수 있다. → [[Roundup/2026-07-22 - Daily Roundup#Interpretation|7/22 BigHug AI 인사이트]]

## 3부: 내 주변 AI News (시간 미정)

> **이번 방송 커버리지**: ①Seattle Tech Week 2026 ②Spark + AI ③이번 주 캘린더 고정 일정 ④페더럴웨이 한인회 광복절 기념식 AI 접목 논의

### ① Seattle Tech Week 2026

Seattle Tech Week는 2026-07-27(월)~2026-07-31(금)에 진행된다. 7/19 기준으로 전체 237개 이벤트와 AI 태그 74개를 수집했고, 7/24에는 Luma 공개 캘린더 기준 현재 예정 행사 242개와 AI 태그 77개를 다시 확인했다. 7/23에는 M3를 완료해 실제 참가 계획과 Google Calendar 등록까지 마쳤으며, 승인 이메일을 받은 행사들은 Calendar에서도 `[Approved]`와 busy 상태로 보정했고, Ai2 행사는 `How AI Gets Built at Ai2 | AI Research Talk`로 제목 변경까지 반영했다. → [[Ingest/CatchUpAI_VL/Topics/Seattle-Tech-Week-2026/03-Schedule/final|최종 참가 계획]]

### ② Spark + AI

2026-07-22(수) 5:00 PM-8:00 PM, Databricks Bellevue에서 열린 Spark + AI: Ignite the Future 행사에는 참석 완료했다. Spark + AI와 Databricks Bellevue는 같은 일정으로 통합 관리하고, 행사 녹화본 편집은 7/23 task로 넘겼다. → [[Roundup/2026-07-22 - Daily Roundup#Spark + AI / Databricks Bellevue 참석|7/22 Spark + AI 기록]]

### ③ 이번 주 캘린더 고정 일정

7/23 Lee & Park 미팅, BigHug 주간 미팅에 이어 7/24에는 Fable Credit 실험 영상 제작(한국어·영어 업로드까지 완료), Live20 썸네일 제작·라이브 방송 세팅, 밤 8시 페더럴 한인회 화상 미팅 참가를 모두 마쳤다. 7/25에는 Bite of Seattle 참석을 불참으로 정리하고, 대신 7/26(일) 오후 4시 페더럴웨이 5 Mile Lake Park에서 열리는 피크닉(주관: 늘푸른연대) 참가를 확정했다 — 오후 9시 Live20 방송 전에 여유 있게 끝나는 일정이다. 7/26 방송 중에는 Seattle Tech Week 일정 관리 기록을 영상 제작 재료로 바꾸는 실험, Spark + AI / Databricks Bellevue 녹화 영상 자막 작업, 그리고 새로 추가된 광복절 기념식 AI 접목 라이브 기획을 이어간다.

### ④ 페더럴웨이 한인회 광복절 기념식 AI 접목 논의

7/24 밤 8시 페더럴웨이 한인회 화상 미팅에 참가했다. 페더럴웨이 한인회는 올해 시애틀 총영사관에서 열리는 광복절 기념식을 주관하는데, 이번 행사 주제가 **"8·15 광복 AI 시대 독립을 외치다"**로 정해졌다. 한인회 측도 광복절 기념식에 AI를 구체적으로 어떻게 접목할지 아직 고민 중인 단계다. 이 논의를 이어서 4부에서 VibeLearn AI로 Research를 진행한다. → [[Roundup/2026-07-24 - Daily Roundup|7/24 Daily Roundup]]

> ✅ **7/26 방송 결과**: 한인회 자료는 끝내 도착하지 않았지만, 방송 중 자료를 기다리지 않고 VibeLearn AI 새 Topic(`FedWay-Liberation-Day-2026`)으로 자체 리서치를 진행해 M1~M4 전 모듈을 완주했다. 최종 기획서(`final-proposal.md`)는 7/27~28 중 한인회에 전달 예정이다. → [[Ingest/CatchUpAI_VL/Topics/FedWay-Liberation-Day-2026/04-Final-Proposal/final-proposal|final-proposal.md]]

## 4부: 오늘의 실험 (시간 미정)

> **이번 방송 커버리지**: ①Seattle Tech Week 일정 관리 기록으로 영상 만들기 ②Databricks 녹화 영상에 Remotion으로 자막 입히기 ③광복절 기념식 AI 섹션 준비 — VibeLearn AI로 Research ④Bila AI Agent M2 진행 상황

> ✅ **7/26 방송 결과**: ①~④는 실제로 방송에서 진행했다. ⑤AI와 글쓰기(피터틸 vs 내 관점), ⑥Slack 채널 자동 수집은 이번 방송에서 다루지 못해 다음 기회로 이월한다.

### ① Seattle Tech Week 일정 관리 기록으로 영상 만들기

방송 중 첫 번째 실험은 VibeLearn AI로 진행한 Seattle Tech Week 일정 관리 과정을 콘텐츠 제작 재료로 바꾸는 것이다. 이미 조사, 후보 수집, AI 태그 필터링, 관심 행사 선정, Google Calendar 반영까지 기록이 남아 있으므로, 방송에서는 그 기록을 AI에게 넘겨 영상의 핵심 메시지와 구성안을 만들게 한다. 목표는 "공부하고 실행한 기록이 있으면, 사람이 다시 처음부터 대본을 쓰지 않아도 영상 제작으로 이어질 수 있는가"를 보여주는 것이다. → [[Ingest/CatchUpAI_VL/Topics/Seattle-Tech-Week-2026/03-Schedule/final|Seattle Tech Week 최종 참가 계획]]

이 실험에서 보여줄 장면은 세 가지다. 첫째, VibeLearn AI가 학습·조사 과정을 단계별 기록으로 남긴다. 둘째, AI4PKM이 그 기록을 볼트 안에서 찾고 연결 가능한 자료로 관리한다. 셋째, AI가 그 기록을 바탕으로 Remotion 영상의 제목, 메시지, 장면 구성, 나레이션 초안을 만든다. 여기까지 되면 "나는 공부만 하면 된다"는 말이 단순 구호가 아니라 실제 워크플로우가 된다.

> ✅ **7/26 방송 결과**: 12장 슬라이드 플랜이 승인됐고, Remotion 컴포넌트(`SeattleTechWeek0726.tsx`)와 12개 슬라이드용 edge-tts 오디오까지 초벌 제작을 마쳤다. 최종 렌더링은 다음 세션으로 이월. → [[AI/RemotionStudio/public/seattle-tech-week-0726/video-slide-plan|슬라이드 플랜]]

### ② Databricks 녹화 영상에 Remotion으로 자막 입히기

두 번째 실험은 Spark + AI / Databricks Bellevue 녹화 영상을 공개 가능한 콘텐츠로 바꾸기 위한 자막 작업이다. 이 작업은 기존 녹화 영상을 가져와 전사·번역·자막 타이밍을 만들고, Remotion으로 읽기 좋은 자막을 입히는 흐름으로 진행한다. 방송에서는 전체 완성보다 파이프라인을 확인하는 데 초점을 둔다: 원본 영상 확인, 자막 작업 단위 결정, Remotion 프로젝트에서 자막 표시 구조 확인, 다음 렌더링 단계 정리. → [[Roundup/2026-07-22 - Daily Roundup#Spark + AI / Databricks Bellevue 참석|7/22 Spark + AI 기록]]

이 실험은 이번 방송 주제와 직접 연결된다. 행사에 참석하고 녹화까지 해 두는 것은 비교적 재미있고 의미 있는 일인데, 전사·번역·자막·렌더링은 반복적이고 시간이 오래 걸리는 작업이다. 그래서 이 부분을 AI와 Remotion 파이프라인으로 넘길 수 있으면, 현장 활동이 자연스럽게 영상 콘텐츠로 이어진다.

> ✅ **7/26 방송 결과**: IMG_5033(96MB, 1:28) 전체를 Whisper 전사 → 번역 → ffmpeg+libass 렌더링까지 완료해 `out/databricks-0722-entoko.mp4`(87.9초)로 확정했다. 나머지 7개 영상은 다음 세션으로 이월.

### ③ 광복절 기념식 AI 섹션 준비 — VibeLearn AI로 Research

세 번째 실험은 3부에서 소개한 페더럴웨이 한인회 광복절 기념식 건을, 이번 주 다른 두 실험과 같은 방식으로 다룬다 — 즉흥 브레인스토밍이 아니라 **VibeLearn AI로 Research를 진행**하는 것이다. 시애틀 총영사관에서 열리는 이번 광복절 기념식 주제는 "8·15 광복 AI 시대 독립을 외치다"이고, 한인회도 구체적인 AI 접목 방법은 아직 정하지 못한 상태다. 방송에서는 이 주제를 VibeLearn AI의 새 Topic으로 잡아, 조사·아이디어 정리 과정을 시청자와 함께 실시간으로 진행한다 — 전시·체험 부스, 발표 자료, 인터랙티브 콘텐츠 등 실제로 제안할 수 있는 구체적인 안을 몇 가지 뽑아 보는 것이 목표다.

이 실험에는 방송 밖으로 이어지는 두 단계 후속 구상이 있다. 첫째, Research 결과물이 쓸 만하면 페더럴웨이 한인회 쪽에 실제로 전달한다. 둘째, 더 나아가 그 시민단체 실무자들에게 VibeLearn AI를 직접 써 보게 할 수도 있다 — 즉 이번 실험이 잘 되면 "AI를 잘 모르는 시민단체 실무자도 VibeLearn AI로 행사 기획 리서치를 할 수 있다"는 별도 사례가 되고, 그 자체를 다시 영상으로 만들어 홍보할 수 있는 후보가 된다. → 아래 `주간 영상` 코너의 "시민단체 실무자용 VibeLearn AI 확산" 후보 참고

> ✅ **7/26 방송 결과**: `FedWay-Liberation-Day-2026` Topic으로 M1(리서치·스토리라인)~M4(통합 기획서·전달 준비) 전 모듈을 하루 안에 완주했다. 국가보훈부 AR 교재·독립기념관×SKT AI 복원 영상·재외동포청 스터디코리안 등 실존 자료와 페더럴웨이 통합한국학교라는 로컬 자원을 발견해 "어린이 주도형 15분 세그먼트 + 그림 전시 연계 AI 이벤트 3개"로 구체화했다. 1단계(한인회 전달, 7/27~28 목표)는 계획대로 진행 중이며, 2단계(시민단체 실무자 확산)는 전달 후 반응을 보고 판단한다. → [[Ingest/CatchUpAI_VL/Topics/FedWay-Liberation-Day-2026/04-Final-Proposal/final-proposal|final-proposal.md]] · [[Ingest/CatchUpAI_VL/Topics/FedWay-Liberation-Day-2026/vl_worklog/20260726_FedWay-Liberation-Day-2026_Final_Retrospective|Topic Retrospective]]

### ④ Bila AI Agent M2 진행 상황

Builders Lounge의 AI Agent인 Bila AI Agent 개발이 M2 단계로 진행 중이다. Google Drive 연결 관련 버그가 fix됐고, 테스트 후 이후 과정으로 넘어간다. 방송에서는 라이브 개발보다 현재 상태 공유 위주로 다룰 가능성이 높다 — 구체적인 진행 방식은 추후 확정. → [[Ingest/CatchUpAI_VL/Topics/Bila-AI-Agent/topic_starter|Bila-AI-Agent Topic]]

> ✅ **7/26 방송 결과**: Drive 재검증 가이드, Drive 포함 시스템 프롬프트 v2.2, Phase 1 최종 10문항 테스트 시트까지 준비했으나, Slack 연동에서 `invalid_team_for_non_distributed_app` 인증 오류라는 새 블로커를 만났다. Changbal 스페이스 어드민 권한 범위를 넘어서는 문제로 판단, GOBI 개발자 확인이 필요한 상태로 정리했다. → [[Ingest/CatchUpAI_VL/Topics/Bila-AI-Agent/vl_worklog/20260726_M2_Bila-AI-Agent|M2 WorkLog]]

### ⑤ AI와 글쓰기 — 피터틸 vs 내 관점 대결

피터 틸의 독점(monopoly) 정당화 주장에 대한 반박·내 관점을 담은 에세이 초안을 AI와 함께 써 보는 실험이다. VibeLearn AI로 진행 중인 `Peter-Thiel-Vision` Topic의 최신 단계이며, 방송에서는 AI와 함께 관점이 다른 글을 어떻게 써 나가는지 과정을 보여줄 수 있다. → [[Ingest/CatchUpAI_VL/Topics/Peter-Thiel-Vision/topic_info|Peter-Thiel-Vision Topic]]

> ⏭️ **7/26 방송 결과**: 시간 관계상 다루지 못함 — 다음 방송으로 이월

### ⑥ Slack 채널 자동 수집 — Builders Lounge Automation M1

Builders Lounge Slack 채널(`#club-sg-ai`) 내용을 자동으로 가져오는 실험이다. M1에서 API vs export vs no-code 방식을 검토해 접근 방식을 확정했다. 아직 별도 WorkLog 파일로는 기록되지 않은 최신 진행 상황으로, 방송 전 정리가 필요하다. → [[Ingest/CatchUpAI_VL/Topics/Slack-Builders-Lounge-Automation/topic_info|Slack-Builders-Lounge-Automation Topic]]

> ⏭️ **7/26 방송 결과**: 시간 관계상 다루지 못함 — 다음 방송으로 이월

### 참고 — 기타 VibeLearn AI로 진행 중인 Topic (오늘 커버리지 아님)

`GOBI-Guiding`, `VibeCoding-Onboarding-Program`, `Vibe-Guiding-VSCode`도 VibeLearn AI로 계속 진행 중인 Topic이다. 오늘 방송에서 다룰 확정 항목은 아니고, 참고용 목록으로만 슬라이드에 표시한다.

## 주간 영상 (시간 미정)

> **이번 방송 커버리지**: ①공부 기록을 영상으로 바꾸는 자동화 ②Seattle Tech Week 일정 수립 과정 영상

### ① 공부 기록을 영상으로 바꾸는 자동화

이번 주 주간 영상의 중심 후보는 "공부하면서 기록하기, 기록을 영상으로 만들기"다. 예전에는 공부와 실험 이후에 사람이 다시 내용을 정리하고, 영상 주제를 잡고, 대본을 쓰고, 슬라이드를 만들고, 렌더링과 업로드 자료까지 준비해야 했다. 이번에는 그 흐름을 뒤집어, 공부와 실험 중에 남긴 기록이 그대로 영상 제작의 입력이 되도록 만든다.

영상의 핵심 메시지는 명확하다. 재미있는 일은 공부와 실험이고, 재미없는 일은 기록 정리와 영상 제작이다. VibeLearn AI가 공부 과정을 기록하고 AI4PKM이 그 기록을 관리·오케스트레이션하면, AI가 그 자료를 바탕으로 영상 구성과 제작 자료를 만들 수 있다. Seattle Tech Week 일정 관리 사례는 이 메시지를 보여주기 좋은 실제 소재다.

### ② Seattle Tech Week 일정 수립 과정 영상

Seattle Tech Week 영상은 방송 중 실험이자 주간 영상 후보로 둔다. 이 영상은 "AI가 이벤트를 찾아 줬다"에서 끝나지 않고, 일정 조사, 후보 필터링, 실제 캘린더 커밋, 그리고 그 과정을 다시 영상으로 만드는 흐름까지 보여준다. 이 구조가 성공하면 앞으로 다른 학습 Topic과 현장 활동에도 같은 방식을 반복 적용할 수 있다.

### Fable 사용 관련 영상 — 7/24 완성, 한국어·영어 유튜브 업로드 완료

이번 주 주간 영상 전략은 변경됐다. 한 주간 실험한 내용을 한 영상에 여러 개 넣는 대신, 영상 하나당 확실하게 하나의 실험과 하나의 인사이트를 담기로 했다. Fable 사용 관련 영상은 별도 후보로 분리했고, 7/24에 실제로 완성해 한국어·영어 두 버전 모두 유튜브에 업로드했다(챕터·SNS 홍보 글까지 완료). 이번 방송에서는 이 완성된 영상을 소개하고, Seattle Tech Week 일정 관리 기록을 영상 제작 재료로 바꾸는 흐름을 이어서 다룬다. → [[Roundup/2026-07-23 - Daily Roundup#Interpretation|7/23 영상 전략 변경]] · [[Roundup/2026-07-24 - Daily Roundup|7/24 완성 기록]]

Fable 영상의 핵심은 "크레딧을 많이 썼다"가 아니라, 창의적 설계가 필요한 작업은 Fable로, 정해진 절차를 따르는 기계적 작업은 Sonnet으로 나눠 쓰기로 한 실제 운영 판단이다. Google Form 제작은 Sonnet으로 처리해 추가 Fable 소모가 없었고, 신청 안내 슬라이드처럼 카피·구성·톤을 새로 잡아야 하는 작업은 Fable을 써서 비용이 발생했다. 이 대비가 영상의 중심 메시지다.

### 추가 후보 (미확정) — Seattle Tech Week 일정 수립 과정 영상 상세 구조

Seattle Tech Week 영상은 이번 방송의 메인 실험이자 주간 영상 후보로 둔다. 이 영상에서 다룰 수 있는 구조는 다음과 같다.

| 구성 | 내용 |
|---|---|
| 문제 | Claude Code가 Luma 페이지는 찾았지만 이벤트 세부 정보 수집에서 막힘 |
| 우회 | 사용자가 7/27 화면 캡처를 제공해 사람이 데이터 접근 병목을 메움 |
| 해결 | Codex가 Luma 공개 JSON API를 찾아 전체 행사 자동 수집. 7/24 기준 현재 예정 행사 242개와 AI 태그 77개 확인 |
| 인사이트 | AI에게 결과물을 요구하는 것과 데이터 원천을 찾게 하는 것은 자동화 수준이 다름 |
| 결론 | AI와 함께 행사 계획을 끝내려면 조사 자동화뿐 아니라 캘린더 커밋까지 가야 함 |

이 후보는 다음 주 주간 영상에서 "AI Agent는 100마일짜리 4차선 고속도로 중 5마일만 10차선" 비유와 연결해 사용할 수 있다. Codex가 한 일은 첫 5마일을 더 빠르게 달린 것이 아니라, 막힌 구간의 데이터 도로를 새로 찾은 것이다. 242개 예정 행사 중 AI 태그 77개를 확인하고, 그 전체 후보를 AI와 함께 관심사·오프라인 가치·캘린더 충돌 기준으로 추려 실제 참가 계획으로 바꿨다는 점까지 보여줄 수 있다.

### 추가 후보 (미확정) — Fable Credit 소모 실험: 한도를 네 번 올리고, 결국 "작업 성격대로" 모델을 바꾸다 (7/20~21)

Fable 5 무료 프로모션이 7/7 종료되고 Pro 플랜은 Usage Credit 기반으로만 Fable을 쓸 수 있게 되면서, "Fable로 영상 하나를 실제로 완성하는 데 크레딧이 얼마나 드는가"를 실측하는 실험을 시작했다. 시작 잔액 $25.08, Monthly spend limit $20→$25 상향으로 출발했다. → [[Research/2026-07-20 Fable Credit 소모 실험 - Build-with-AI Remotion 영상 제작 by Claude Code|Fable Credit 소모 실험]]

**이 실험의 그림은 "한도를 네 번 올렸다"는 것이고, 결론은 "그래서 모델을 나눠 쓰기로 했다"는 것이다.**

| 시점 | Monthly spend limit | 결과 |
|---|---|---|
| 7/20 착수 | $20 → $25 | 넉넉하다고 생각하고 시작 |
| 7/20 저녁 | $25 | Build with AI 컴포넌트·나레이션 반복 작업 중 **118%(한도 초과)**로 작업 중단 — "You've hit your monthly spend limit" |
| (재상향) | $25 → $40 | 작업 재개 |
| 7/20 밤~21 새벽 | $40 | VibeCoding-Onboarding-Program Topic 로드맵 작성 중 **또다시 한도 도달**, 재중단 |
| 7/21 새벽 | $40 → $70 | 재상향 후 작업 재개, 66% 사용 |
| 7/21 새벽 | $70 | 로드맵 마무리 + M1(Google Form 문항·영상 CTA) 두 작업만으로 **$17.93 추가 소모**, 92%까지 재도달 |
| 7/21 새벽 | $70 → $100 | 3차 재상향. **단, 한도는 올렸지만 "당분간 Fable을 쓰지 말아야겠다"고 판단 — 다음 작업(Google Form 실제 제작)부터 Sonnet으로 전환 결정** |
| 7/21 (Google Form 제작·테스트, Sonnet) | $100 | Google Form 문항 구조·Section 분기 설정은 "창의력이 크게 필요 없는 기계적 작업"으로 판단해 Sonnet으로 진행 — 이 구간은 Fable 소모 없음 |
| 7/21 (Build with AI 영상에 CTA 슬라이드 추가, Fable 재전환) | $100 | 온보딩 신청 안내 슬라이드(S19.5) 추가는 "슬라이드 구성·카피·톤을 새로 설계하는 창의적 작업"으로 판단해 다시 Fable로 전환 → **이 작업 하나에 실제로 든 비용은 $8.16** (Current balance $56.89→$48.73, Promotional credit $50.10→$41.94, 두 값이 정확히 같은 폭으로 감소해 실제 지갑 소모액임을 뒷받침). 사용자 체감("9달러 정도")과 거의 일치. 화면 상단 "spent" 게이지는 $68.19→$75.11로 $6.92만 증가해 실제 잔액 감소분과 정확히 일치하지는 않음(원인 미확인, 사실만 기록) |

하루 반나절 사이 $25 → $40 → $70 → $100으로 네 번 한도를 올려야 했다는 사실이, 텍스트 슬라이드나 숫자보다 훨씬 직관적으로 "AI Agent 작업에는 실제 비용이 빠르게 붙는다"는 메시지를 전달한다. 하지만 이 실험의 진짜 포인트는 그다음이다 — 한도를 계속 올리는 대신, **"처음 설계·창의적 판단이 필요한 작업은 Fable로, 정해진 절차를 따르는 기계적 작업은 Sonnet으로" 작업 성격에 따라 모델을 나눠 쓰기로 한 것**이다. 이 원칙은 로드맵 작성 때 한 번(말로) 정해졌고, 이후 Google Form 제작(Sonnet, $0 추가 소모)과 CTA 슬라이드 추가(Fable, $6.92 소모) 두 작업으로 실제 숫자와 함께 검증됐다. "AI Agent는 공짜가 아니다"에서 한 걸음 더 나아가 "그래서 비용 대비 가치를 보고 작업마다 도구를 고른다"는 실전 결론까지, 이번엔 두 번째 사례로 다시 확인한 셈이다.

**영상 에셋 폴더**: `AI/Roundup/2026-07-19 - Weekly Video Assets/`

| 에셋 | 용도 |
|---|---|
| `Fable_Credit_Balance_2026-07-20.jpg` | Claude Code/Fable Credit Balance 화면 자료. AI Agent 사용량·크레딧·실험 비용 맥락을 보여주는 보조 이미지 |
| `WorkWithFable01~05.jpg` | Fable로 작업하는 과정 1~5. `04`·`05`는 주간 영상 제작 때 AI 작업에 실제로 credit/usage가 들어간다는 점을 보여주는 자료 |
| `WorkWithFable100Bul_06.jpg` | 첫 번째 Monthly spend limit 도달 메시지 ("You've hit your monthly spend limit") |
| `WorkWithFable100Bul_07.jpg` | $25 한도에서 118%(한도 초과) 소진된 Usage 화면 |
| `WorkWithFable100Bul_08.jpg` | 두 번째 Monthly spend limit 도달 메시지 ($40 한도에서 재도달) |
| `WorkWithFable100Bul_09.jpg` | $70로 재상향 후 66% 사용 중인 Usage 화면 |
| `WorkWithFable100Bul_10.jpg` | $70 한도에서 다시 92%(거의 소진)까지 도달한 Usage 화면 |
| `WorkWithFable100Bul_11.jpg` | $100로 3차 상향 후 68% 사용 중인 Usage 화면 — 이 시점에 사용자가 "다음 작업은 Sonnet으로" 결정 |
| `WorkWithFable100Bul_12.jpg` | Google Form(Sonnet) 작업 후, Build with AI 신규 슬라이드 추가 작업으로 다시 Fable 전환 — $75.11(75%) 사용 중인 Usage 화면 |

이 실험은 ①번 Codex Win의 "AI Agent는 공짜 마법이 아니다" 메시지와 바로 이어 붙일 수 있다 — 데이터 원천을 찾는 자동화든, 새 모델로 영상을 만드는 것이든, 실제 사용에는 크레딧이라는 예산이 붙는다는 점을, 이번엔 "한도를 네 번 올리다가 결국 작업 성격대로 모델을 나눠 쓰기로 한 사람"이라는 구체적이고 완결된 경험으로, 그리고 창의적 작업 하나($8.16)와 기계적 작업 하나($0)의 실제 비용 차이로 보여준다.

### 추가 후보 (미확정) — BigHug AI / Bila AI 적용: 메신저에 흩어진 행사 문서를 AI 운영 보조자로 바꾸기 (7/22)

7/22의 새 후보는 BigHug 행사 준비에서 나온 **커뮤니티 운영 AI** 아이디어다. BigHug K-pop 추석행사 준비 문서가 메신저로 오가면 나중에 찾아보기 어렵고, 준비자들이 그때그때 모든 내용을 읽어야 하는 부담도 크다. 이 문제는 GobiSpace의 Bila AI 기능을 적용하기 좋은 실제 사용 사례다. 자료를 특정 공간에 올려 두고 BigHug AI가 필요한 내용을 요약·보고해 주면, 행사의 준비 상황, 벤더 테이블 배치, 다음 회의 전 확인사항을 빠르게 파악할 수 있다. → [[Roundup/2026-07-22 - Daily Roundup#Interpretation|7/22 BigHug AI 인사이트]]

| 구성 | 내용 |
|---|---|
| 문제 | 행사 준비 문서와 메시지가 메신저에 흩어져 검색·공유·요약이 어려움 |
| 적용 | GobiSpace/Bila AI 기능을 BigHug 준비 공간에 적용해 자료를 한곳에 모으고 질문·요약·보고 흐름을 제공 |
| 확장 | BigHug 자체 시스템 구축을 grant project로 구조화하고, 그 예산으로 GOBI와 협업하는 모델 가능 |
| 주간 영상 메시지 | AI는 대형 제품보다 먼저 "커뮤니티 운영 자료를 제때 찾아 요약해 주는 보조자"로 실용화될 수 있음 |
| 다음 액션 | BigHug AI 요구사항, grant narrative, GOBI 협업 범위를 별도 기획 후보로 정리 |

이 후보는 Builders Lounge의 오프라인 확장 인사이트와도 연결된다. 빌더들이 만든 제품은 실제 소비자와 현장 피드백을 만나야 하고, 오프라인에서 만나는 일반 참여자들도 AI 기술에 관심이 높다. BigHug AI는 그런 현장 수요를 커뮤니티 운영 문제에서 시작해 실제 제품/계약/협업으로 이어 볼 수 있는 사례가 될 수 있다.

### 추가 후보 (미확정) — 시니어 도메인 전문가의 바이브 코딩 첫걸음: 코딩 교육보다 첫 진입로 동행 (7/21)

7/21의 가장 중요한 새 후보는 Build with AI 영상을 만들면서 나온 **시니어 도메인 전문가 온보딩** 인사이트다. 사용자는 AI를 일상에 잘 활용하는 방법을 계속 고민해 왔고, 그중 당장 잘할 수 있는 구체적 영역을 "오랜 경험과 자기 분야 전문 지식이 있고, 그것을 AI를 사용해 Product로 만들고 싶지만 바이브 코딩을 처음 시작하지 못하는 분들을 돕는 일"로 정리했다. → [[Roundup/2026-07-21 - Daily Roundup#Interpretation|7/21 Daily Roundup Interpretation]]

이 후보의 메시지는 "AI로 모두가 앱을 만들 수 있다"는 넓은 선언이 아니라, 더 작고 실행 가능한 약속이다. 자기 분야의 노하우는 이미 충분한데 컴퓨터·도구·세팅·첫 프롬프트 앞에서 멈추는 분들에게, 환경 세팅과 첫 성공 경험까지 같이 가면 시작할 수 있다는 것이다. 이 관점에서 7/21에 만든 Google Form과 VibeCoding-Onboarding-Program M1은 단순 신청서가 아니라, 영상에서 말한 메시지를 실제 행동으로 받을 수 있는 입구다. → [[Ingest/CatchUpAI_VL/Topics/VibeCoding-Onboarding-Program/vl_worklog/20260721_M1_VibeCoding-Onboarding-Program|VibeCoding-Onboarding M1 WorkLog]]

| 구성 | 내용 |
|---|---|
| 문제 | 오랜 경험과 노하우가 있어도 컴퓨터·바이브 코딩 첫 세팅 앞에서 시작하지 못하는 분들이 있음 |
| 관찰 | 이선생님 사례처럼 세팅과 첫 진입로만 도와도 본인의 도메인 지식으로 빠르게 앱을 만들 수 있음 |
| 실행 | VibeCoding-Onboarding-Program Topic, 5모듈 로드맵, 신청 Google Form, 영상 CTA 문구를 7/21에 구축 |
| 주간 영상 메시지 | AI 일상 활용의 한 출발점은 "시니어 도메인 전문가가 자기 노하우를 Product로 만드는 첫걸음을 돕는 것" |
| 다음 액션 | M2 온보딩 여정 커리큘럼 설계, 영상 설명란/홍보 글에서 신청 Form 연결 |

이 후보는 Build with AI 영상 자체와 자연스럽게 이어진다. 영상은 "도메인 지식이 있다면 AI로 제품을 만들 수 있다"는 설명이고, 온보딩 프로그램은 그 설명을 들은 사람이 바로 신청할 수 있는 실험이다. 방송에서는 주간 영상 후보로 남겨 두되, 실제 커버리지에 올릴지는 목/금 점검 때 확정한다.

### 추가 후보 (미확정) — AI 빌더의 범위는 생각보다 넓다 (7/24)

7/24 페더럴웨이 한인회 미팅을 계기로 나온 인사이트다. AI 빌더라고 하면 흔히 앱·서비스를 코딩하는 사람만 떠올리기 쉽지만, 실제로는 문인협회 소속 작가가 AI로 창작 작업을 하는 경우, 화가가 AI로 그림을 그리는 경우도 모두 AI 빌더라고 볼 수 있다는 관찰이다. 아직 구체적인 실행 계획은 없지만, Builders Lounge가 앞으로 다룰 수 있는 범위가 코딩·개발을 넘어 훨씬 넓다는 방향성 힌트로 남겨 둔다. → [[Roundup/2026-07-24 - Daily Roundup|7/24 Daily Roundup]]

### 추가 후보 (미확정) — 시민단체 실무자용 VibeLearn AI 확산 (7/26 방송에서 씨앗)

7/26 방송 4부에서 광복절 기념식 AI 섹션을 VibeLearn AI로 Research하는 실험이 잘 풀리면 나올 수 있는 다음 단계 후보다. 핵심 아이디어는 AI를 잘 모르는 시민단체(페더럴웨이 한인회 등) 실무자도 VibeLearn AI를 직접 써서 행사 기획 리서치를 할 수 있는지 확인하는 것이다. 이 실험이 성공하면 "코딩도, AI도 낯선 사람이 VibeLearn AI로 실제 행사를 준비하는 법"이라는 별도 영상으로 만들어 홍보할 수 있다. → [[Roundup/2026-07-19 - Live20 Weekly Rundown#④ 페더럴웨이 한인회 광복절 기념식 AI 접목 논의|3부 광복절 논의]] · [[Roundup/2026-07-19 - Live20 Weekly Rundown#③ 광복절 기념식 AI 섹션 준비 — VibeLearn AI로 Research|4부 실험]]

| 구성 | 내용 |
|---|---|
| 전제 | 7/26 방송에서 광복절 기념식 AI 섹션 Research가 실제로 쓸 만한 결과물로 나옴 |
| 1단계 | Research 결과물을 페더럴웨이 한인회에 실제 전달 |
| 2단계 | 한인회 실무자에게 VibeLearn AI 사용법을 직접 안내, 스스로 리서치해 보게 함 |
| 주간 영상 메시지 | Builders Lounge/VibeLearn AI가 개발자가 아닌 시민단체 실무자에게도 실제로 쓸모 있다는 확산 사례 |
| 다음 액션 | 7/26 방송 결과를 보고 실제 진행 여부·시점 결정 — 아직 확정 아님 |

## 아웃트로

- 다음 주 Seattle Tech Week 2026 예고
- 주간 영상 후보 중 실제 제작할 항목 안내
- 구독 & 좋아요 CTA

> ✅ **7/26 방송 결과 요약**: 4부 실험 6개 중 4개(①Seattle Tech Week 영상 슬라이드+오디오, ②Databricks 자막 완료, ③광복절 AI Research M1~M4 완주, ④Bila AI Agent Slack 블로커 발견)를 실제로 진행했다. 자료 미도착이었던 광복절 건을 VibeLearn AI 자체 리서치로 완결한 것이 이번 방송의 핵심 성과이며, ⑤피터틸 글쓰기·⑥Slack 자동화는 다음 방송으로 이월한다.

---

*2026-07-20 초안 작성. rundown-writer 스킬 기준으로 각 파트의 커버리지 줄을 포함했다. 2026-07-26 방송 종료 후 실제 결과를 반영해 최종 동기화했다.*
