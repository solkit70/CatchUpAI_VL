---
title: "2026-08-02 - Live22 Weekly Rundown"
created: 2026-08-02 22:30:00
status: "✅ 방송 완료 (2026-08-09) — 방송 후 실제 진행 일부 반영, 2부 최종 커버리지는 사용자 확인 대기"
tags:
  - roundup
  - rundown
  - live-broadcast
links:
  - "[[Roundup/2026-08-03 - Daily Roundup]]"
  - "[[Roundup/2026-08-04 - Daily Roundup]]"
  - "[[Roundup/2026-08-05 - Daily Roundup]]"
  - "[[Roundup/2026-08-06 - Daily Roundup]]"
  - "[[Roundup/2026-08-07 - Daily Roundup]]"
  - "[[Roundup/2026-08-02 - Weekly Progress and Planning]]"
  - "[[Roundup/2026-08-02 - Weekly Dashboard.canvas]]"
  - "[[Roundup/Weekly/2026-07-26~2026-08-02 - Claude Code]]"
---

# AI in Action Live #22

**방송일**: 2026-08-09 (일) — 정확한 시간은 미정 (Live21 기준 오전 5시 시애틀 / 오후 9시 KST 패턴 참고)
**제목**: AI를 일상에 적용해 보는 다양한 실험
**주제**: 내 일상에 AI 적용하기 그냥 보여주기

> **확정 상태**: 2026-08-08 최종 라이브 방송 준비 슬라이드 기준으로 정리했다. 이번 방송은 지난주 활동/AI 뉴스 섹션을 줄이고, 실제 일상 작업에 AI를 적용하는 실험 중심으로 진행한다.

> **방송 후 (2026-08-09)**: 방송 완료. 확인된 실제 진행은 ①Live-CoMC-App(M3 데이터 계약·안전 정책 완료 + M4 Wake Word/VAD 실습 1·2)과 ②Seattle Tech Week → 기사 작성 Topic 로드맵(Codex, VibeLearn AI 정합 수정)이었고, ③독립유공자 영상 마무리는 미완으로 이월됐다. 상세는 [[Roundup/2026-08-09 - Daily Roundup|8/9 Daily Roundup]]. 2부 12개 후보 중 실제로 다룬 나머지 항목은 사용자 확인 후 커버리지 확정 예정.

## 방송 순서

| 순서 | 파트 | 예상 시간 | 내용 |
|---|---|---|---|
| 0 | 방송 시작 전 | - | Capture 활성화, 지난 방송 결과 확인 |
| 1 | 1부: 지난 주 생성한 콘텐츠 | 미정 | Seattle Tech Week 2026 녹화 영상 편집/업로드 32개 완료 상황 공유 |
| 2 | 2부: 오늘의 실험 | 미정 | AI 보조 MC 앱, Seattle Tech Week 학습, FedWay 영상 마무리, DFS/Run-Hide-Fight 요약 영상, AI workload 회고, Bila/Peter/Slack/catchupai.net/실시간 번역/기타 VibeLearn Topic 후보 |
| 3 | 예비 실험 | 남는 시간 | 우선순위 낮은 VibeLearn Topic 또는 Builders Lounge 관련 자동화 |
| 4 | 아웃트로 | - | 다음 주 예고, 구독 & 좋아요 |

---

## 0. 방송 시작 전

- [ ] GOBI Desktop Capture 활성화
- [ ] Fable/agent 세션 사용량 확인
- [ ] VS Code + Claude Code / Codex Extension 준비
- [ ] 지난 주(8/2~8/8) 진행 상황 최종 점검

---

## 1부: 지난 주 생성한 콘텐츠 (시간 미정)

> **이번 방송 커버리지**: ①Seattle Tech Week 2026 녹화 영상 편집/업로드 32개 완료 ②편집 완료 자산을 VibeLearn AI 학습 재료로 전환

### Seattle Tech Week 녹화 영상 편집 결과와 Live22 학습 전환

8/4에는 공기질 악화로 외부 활동을 줄이고 집에서 유튜브 영상 편집에 집중했다. 그 결과 2026-07-22 Databricks Bellevue의 Seattle Spark + AI 영상 4편은 `whisper-1` 기반 전사, 챕터, 제목, 설명, 태그, YouTube URL까지 정리되었다. `gpt-transcribe`는 세그먼트 타임스탬프를 반환하지 않아 챕터 생성에 맞지 않았고, 타임스탬프가 필요한 편집 작업에는 `whisper-1`을 유지했다는 판단도 좋은 방송 소재다.

8/5에는 AI Startup Secret Sauce with Startup425 and Level UP 녹화본 5편이 추가로 업로드 가능한 자산이 되었다. Clara founder pitch, Eden Cohen의 ideation talk, Amit Gupta의 validation talk, Sunny Kotwal의 scaling with agents talk, 패널 Q&A까지 제목·설명·챕터·태그·YouTube 링크가 정리되었다. 특히 OpenAI API 크레딧 소진 상태에서 새 전사를 호출하지 않고, 기존 원본 클립 전사를 오디오 상호상관으로 편집본 타임라인에 맞춰 재배치한 점은 "이미 가진 자료를 재활용해 비용 없이 진행한 편집 파이프라인" 사례로 다룰 수 있다.

8/6에는 같은 방식으로 Startup425 Eastside Summit 3(5편)와 AI Demo Day(10편), 총 15편이 추가로 업로드 자산이 되어 플레이리스트 총합이 108편에서 123편으로 늘었다. Demo Day 작업에서는 사용자가 제공한 "Meet the Builders" 행사 명함 슬라이드를 근거로 발표자·회사명 오인식 8건(Winnovo→Wynovo, EverWatch→Everwatch, SeaStork→C-Stork, David Schenker→David Schainker, Sridhika→Shruthika Balasubramanian, Camellia.ai→Camillia.ai 등)을 바로잡았다. 화면 근거 없이는 놓쳤을 이름 오류였다는 점에서 "전사는 오디오만이 아니라 화면도 근거로 검증해야 한다"는 인사이트로 다룰 수 있다.

추가로 2026-07-31 Biuty AI 클립 2편은 한/영 자막을 재검수했다. `Biuty`, `skincare decisions`, `the B2B integrations`처럼 고유명사와 의미가 달라질 수 있는 표현을 화면 슬라이드와 재전사로 확인했고, 한글 자막 렌더링 산출물도 남았다.

8/7에는 ACM Data Conclave 2편과 InformsCon 3편이 YouTube 링크와 playlist까지 반영됐고, Biuty AI 2편도 후속 작업이 남지 않은 것으로 확인됐다. 이로써 Seattle Tech Week 편집 주간은 완료 상태로 정리됐고, Live22에서는 이 영상들을 단순 결과물이 아니라 VibeLearn AI 학습 재료로 다시 읽는 것이 좋다. 학습 질문은 ①신뢰할 수 있는 AI Agent 시스템(trust, grounding, evaluation, reversibility threshold), ②agentic AI와 operations research/optimization의 역할 분담, ③consumer AI의 onboarding과 trust를 Builders Lounge와 Vibe Guiding에 어떻게 연결할 것인가로 잡을 수 있다.

### Builders Lounge 4차 모임(8/6) 후기

4차 모임이 Bellevue City Hall에서 실제로 열렸다. 비개발자 출신 김성수님이 메인 스피커로, 이도규님이 퀀트 관련 프로덕트를, 김민수님이 서버 장애 대응 AI Agent 시스템 개발 상황을 발표했다. 사용자와 강민석님은 Bila AI와 Gobi Space 내 Builders Lounge 커뮤니티 기능을 소개했다.

사용자가 남긴 회고가 방송 소재로 강하다: 발표자마다 분야·관심사·접근 방식(기술적/인생철학적/사이드잡)이 달라 다양한 정보를 얻을 수 있는 건 장점이지만, 동시에 참가자마다 관심 없는 주제가 다뤄지는 순간이 생겨 만족도에는 구조적 한계가 있을 수 있다는 문제의식이다. 바이브코딩 시대에 Product를 만드는 사람의 배경 폭이 넓어질수록 커뮤니티가 피할 수 없는 "다양성 vs 만족도" 딜레마로 다룰 수 있다. 다음 모임은 김민수님의 서버관리 긴급상황 대처 AI Agent 후속 발표가 이미 확정됐고, AI Agent·5분 스피치 라인업 다양화와 모임 형식 재설계가 과제로 남았다.

8/7에는 이 고민이 한 단계 더 구체화됐다. 송재희님에게 비개발자 출신을 위한 AI Builder Guide 온라인 특강을 부탁해보는 아이디어가 생겼고, 김성진님·강민석님과 별도 미팅을 잡아 Builders Lounge가 참가자들에게 지속가능한 도움을 주는 시스템이 될 수 있는지 논의해야 한다. 다만 이 작업은 이번 Live22의 직접 실험이 아니라 주중 후속 기획으로 분리한다.

### FedWay 광복절 AI 특별기획 파일럿 제작

노백린·류동열·김동협 세 분의 3분 32초 파일럿 영상 제작 사례. 원본 사진 → AI 복원 사진 → Gemini 10초 말하는 영상 구조, 유족 동의 전 파일럿을 먼저 보여주며 판단받는 운영 방식, 그리고 "무료로 어디까지 가능한지 먼저 증명한 뒤 필요한 유료 항목만 분리한다"는 실무 패턴을 다룰 수 있다.

8/7 기준 다음 최우선 영상 작업은 FedWay 독립유공자 영상 마무리다. 이구님과 진행한 온라인 미팅 편집은 Live 준비 이후 주중 작업으로 따로 진행한다.

---

## 2부: 오늘의 실험 (시간 미정)

> **이번 방송 커버리지 (2026-08-09 방송 후 실제)**: ①라이브 방송 보조 MC 앱(Live-CoMC-App M3 완료 + M4 실습 1·2) ②Seattle Tech Week 2026 → 기사 작성 Topic 로드맵 ③VibeLearn AI를 Codex에 최적화
>
> ▷ 계획했던 나머지(FedWay 독립유공자 영상 마무리, ④DFS·⑤Run-Hide-Fight·⑥AI 회고글·⑦Bila M2·⑧피터틸 글쓰기·⑨Slack 자동수집·⑩catchupai.net·⑪실시간 번역 조사·⑫기타 Topic)는 이번 방송에서 **다루지 않음 → 이월**

### 후보 ① AI로 라이브 방송 보조 MC 앱 만들기

이번 방송의 중심 실험이다. 지난주 M1~M2를 완료한 Live-CoMC-App을 이어서 진행하고, 방송 중 진행 보조, 주제 전환, 실험 기록, 타임라인 관리에 필요한 다음 단계를 구체화한다.

→ **방송 후**: M3(데이터 계약·안전 정책 스펙) DoD 6/6 완료 + M4(Wake Word/VAD 하네스) 실습 1·2 진행(openWakeWord alexa 채택, Silero VAD context prepend 버그 수정). 실습 3·4는 다음 세션.

### 후보 ② Seattle Tech Week 2026 영상 VibeLearn AI 학습

Seattle Tech Week 2026에서 편집한 영상들을 재료로, 단순 요약이 아니라 현재 하고 있는 일과 연결되는 학습 세션을 진행한다. 우선 축은 ACM Data Conclave의 trust/evaluation/reversibility, InformsCon의 operations research와 agentic AI 역할 분담, Biuty AI의 consumer AI onboarding/trust다. 산출물 후보는 "내 일과 연결되는 Seattle Tech Week 인사이트 맵", "Builders Lounge 교육/운영 아이디어", "Vibe Guiding 또는 Live-CoMC-App 설계 메모"다.

→ **방송 후**: 학습을 넘어 `Seattle-Tech-Week-2026-Article-Writing` 정식 기사 작성 Topic의 로드맵으로 구체화됐다. Codex로 진행했고, Codex가 VibeLearn AI 설계대로 움직이도록 topic_starter→roadmap_prompt→Roadmap 순서를 수정했다.

### 실제 진행: VibeLearn AI를 Codex에 최적화

방송 중 예정에 없던 실제 작업으로, VibeLearn AI 학습 방법론을 Codex 환경에 최적화했다. Codex에서 VibeLearn AI가 원하는 대로 작동하지 않아, `AGENTS.md`·`CLAUDE.md`·`GEMINI.md`·`CODEX.md` 등 에이전트 지침을 수정해 topic_starter → roadmap_prompt → Roadmap → daily_learning 순서가 Codex에서도 지켜지도록 맞췄다. Seattle Tech Week 기사 Topic 로드맵을 Codex로 만든 것도 이 최적화의 결과다. "박창수의 VibeLearn AI 방법론이 Claude Code뿐 아니라 다른 에이전트(Codex)에서도 재현되게 만든다"는, 이번 방송 세 갈래 확장의 핵심 문제의식과 맞닿은 작업이다.

### 후보 ③ FedWay 독립유공자 영상 마무리

광복절 독립유공자 영상 작업을 마무리한다. Live에서는 온라인 미팅 녹화 편집이 아니라, FedWay 독립유공자 영상 자체의 마무리 작업을 다룬다.

→ **방송 후**: 미완료 — 이월. 다음 주 초 이구님과 통합한국학교 학생 대상 VibeLearn AI 시도(학생용 커리큘럼 신규 작성 필요)와 함께 우선 처리 대상.

### 후보 ④ DFS Crowd Manager Training 요약 영상 제작

BigHug 안전 운영 과정에서 실제로 수강한 DFS Crowd Manager Training을 요약 영상으로 재구성한다.

### 후보 ⑤ 총기난사 대처 요령 교육과정 요약 영상 제작

Run-Hide-Fight와 기존 안전 대비 문서를 바탕으로 행사 자원봉사자용 안전 교육 영상을 만들 수 있는지 실험한다.

### 후보 ⑥ AI는 일을 줄이는가, 더 만드는가 회고 글 작성

8/2 Titlow Park 경험과 이번 주 대량 영상 편집 주간을 바탕으로, AI가 일을 줄이는지 더 만드는지에 대한 회고와 철학 코멘트를 글로 정리한다.

### 후보 ⑦ Bila AI Agent 만들기 M2 진행

Slack 이슈는 개발자와 협의하고, GitHub 테스트 지속과 그 이후 진행 방향을 정리한다.

### 후보 ⑧ AI와 글쓰기 - 피터틸 vs 내 관점 대결

`Peter-Thiel-Vision` Topic에서 피터 틸의 관점과 사용자의 관점을 대결시키며 AI와 글쓰기 실험을 진행한다.

### 후보 ⑨ Slack 채널 내용 자동으로 가져오기

`Slack-Builders-Lounge-Automation` 후보. Builders Lounge 관련 Slack 채널 내용을 자동 수집해 후속 기록과 커뮤니티 운영에 활용할 수 있는지 본다.

### 후보 ⑩ catchupai.net Builders Lounge 내용 추가

catchupai.net 홈페이지에 Builders Lounge 관련 내용을 추가하는 작업 후보.

### 후보 ⑪ 실시간 번역 앱 feasibility 조사

내 일상에서 사용할 수 있는 실시간 번역 앱의 API 비용, 화자 구분, 개인정보 UX, 후처리 요약 가능성을 조사한다.

### 후보 ⑫ 기타 VibeLearn AI 진행 Topic

`GOBI-Guiding`, `VibeCoding-Onboarding-Program`, `Vibe-Guiding-VSCode` 등 진행 중인 Topic 중 시간이 맞는 것을 이어간다.

### 우선순위 낮은 대기 목록

| # | 항목 | 관련 Topic |
|---|---|---|
| 1 | 대기업 AI vs 스타트업 AI 인사이트 | Seattle Tech Week 학습 중 파생 인사이트 |
| 2 | Builders Lounge 지속가능 도움 시스템 설계 | 주중 후속 기획 |
| 3 | Builders Lounge 4차 모임 영상 편집 | 주중 영상 편집 |
| 4 | 김진영님 AI4PKM 사용 후기/advice 영상 편집 | 주중 영상 편집 |

---

## 아웃트로

- 다음 주 예고: 미정
- 구독 & 좋아요 CTA

---

## 보류된 인사이트 후보 (다음 방송 검토용)

- **AI는 일을 줄이는가, 더 만드는가** — 8/2 Titlow Park 새 관찰 모임에서 나온 "넓게 처리하는 시간과 좁게 몰입하는 시간을 의도적으로 번갈아 둔다"는 결론으로 구체화 가능
- **VibeLearn AI의 세 가지 용도** — 개인 학습(FedWay) → 협업(8/1 이구님) → 제품 개발(8/2 Live-CoMC-App)로 확장된 흐름

## 주간 영상 (시간 미정)

> **이번 방송 커버리지**: ①Seattle Tech Week 2026 녹화 영상 32개 편집/업로드 완료 ②Live22 준비 완료와 실험 중심 방송 전환

| 후보 | 상태 | 영상 메시지 |
|---|---|---|
| Seattle Tech Week 녹화 편집 | 완료 | 주중 한 작업으로 Seattle Tech Week 2026 녹화 영상 32개 편집/업로드 완료 |
| AI Startup Secret Sauce 5편 편집 파이프라인 | 후보 | API 크레딧 소진 상황에서 기존 원본 전사를 오디오 상호상관으로 편집본에 재배치해 비용 없이 5편 메타데이터를 완성한 사례 |
| Builders Lounge 4차 모임 — 다양성 vs 만족도 | 후보 | 발표자 배경·관심사가 다양할수록 정보 폭은 넓어지지만 개별 만족도는 흐려질 수 있다는 8/6 회고. 다음 모임 형식 재설계 과제로 이어짐 |
| 화면 슬라이드로 잡아낸 이름 오류 8건 | 후보 | Demo Day "Meet the Builders" 슬라이드 대조로 Winnovo→Wynovo 등 8건 교정 — 전사 검증은 오디오만이 아니라 화면도 근거로 삼아야 한다는 사례 |
| 산불 연기 속 실내 영상 편집 루틴 | 후보 | 공기질 악화로 레이니어산이 보이지 않을 정도였던 날, 외부 활동 대신 Seattle Spark + AI 4편과 Biuty AI 자막을 정리한 운영 사례 |
| FedWay 광복절 AI 특별기획 파일럿 | 완료(3인 샘플) | 지역 커뮤니티 행사의 AI 세그먼트를 말이 아니라 3분 32초 샘플 영상으로 증명 |
| FedWay 12인 영상 확장 | 진행 전환 | 8/5 이구님 답변 기준 현재 자료로 1차본을 만들고, fact check와 추가 사진을 후속 반영하는 제작 운영 사례 |
| BigHug Crowd Manager Training | 완료/후보 | Changsoo Park 수료증 저장, 공유용 수강 가이드 작성. 대규모 행사 안전 교육을 영상/가이드 자산으로 전환 가능 |
| 보조 MC 앱 만들기 (Live-CoMC-App) | 진행 중 (M3 완료 + M4 실습 1·2) | 12주 프로젝트 완성 과정 자체가 영상 소재. 8/9 Live22 Main Topic으로 진행 — M3(데이터 계약·안전 정책) 완료, M4(Wake Word/VAD) 실습 1·2. 호출어 감지/발화 종료 판정 실측이 방송 인프라 소재 |
| Seattle Tech Week 기사 작성 + Codex 정합 | 신규 후보 | Codex가 VibeLearn AI 설계대로 안 움직여 topic_starter→roadmap 순서를 수정한 사례 — "다른 에이전트에서도 방법론이 재현되게 만드는" 문제로 다룰 수 있음 |
| 실시간 번역 앱 | 조사 전 | feasibility 조사 결과에 따라 제작 여부 결정 |
| DFS Crowd Manager Training 요약 영상 | 백로그 추가 | 실제 수강·수료 과정을 바탕으로 커뮤니티 행사 안전 교육 영상을 Remotion AI로 제작 |
| Run-Hide-Fight 안전 교육 영상 | 백로그 추가 | DHS 총기 난사 대응요령과 기존 안전 대비 문서를 바탕으로 행사 자원봉사자용 영상 제작 |

---

*2026-08-08 최종 방송 준비 슬라이드 기준으로 업데이트. Live22 준비는 완료됐고, 다음 작업은 FedWay 독립유공자 영상 관련 이구님 온라인 미팅 편집 및 YouTube 업로드다.*
