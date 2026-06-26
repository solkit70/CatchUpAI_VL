---
title: "AI 콘텐츠 제작 사례 인벤토리 — The AI Powered Creator"
created: 2026-06-19 17:30:00
tags:
  - the-ai-powered-creator
  - m5-content-workflow
---

# AI 콘텐츠 제작 사례 인벤토리 (M5)

**목적**: 발표 3부 "기록이 콘텐츠가 되는 실제 사례" 파트의 원천 자료.
각 사례를 `기록 원천 → Context → AI 협업 → 산출물 → 배포` 구조로 정리.

---

## Case 1: 라이브 방송 → Remotion 요약 영상

**슬라이드 핵심 한 줄**: "기록이 없었다면 이 영상은 만들 수 없었다"

| 단계 | 내용 |
|------|------|
| **기록 원천** | GOBI Desktop Capture (방송 중 실시간 캡처) + Rundown 문서 |
| **Context** | 방송 핵심 포인트, 인용 발언, 실험 결과가 구조화된 텍스트로 저장 |
| **AI 협업** | Claude Code → 슬라이드 플랜(video-slide-plan.md) 작성 → Remotion 컴포넌트 생성 |
| **산출물** | MP4 요약 영상 (1~2분) — live13-0607-summary, membership-promo-0614 등 |
| **배포** | YouTube (Members Only 선공개 → Public 전환), SNS 7개 플랫폼 |

**발표 포인트**:
- 오프닝에서 재생한 바로 그 영상이 이 파이프라인의 결과물
- "기록(Capture) → 구조화(Rundown) → AI(슬라이드 플랜) → 영상(Remotion) → 배포(YouTube)" 루프 시각화

---

## Case 2: 미팅 기록 → 리서치 문서 + GitHub 공개

**슬라이드 핵심 한 줄**: "대화도 기록하면 자산이 된다"

| 단계 | 내용 |
|------|------|
| **기록 원천** | Zoom/온라인 미팅 녹화 → Whisper 전사 → Transcript 파일 |
| **Context** | 김성진님(James Kim) 미팅 Transcript — Loop Engineering, GOBI 피드백, Builders Lounge 전략 |
| **AI 협업** | Claude Code → 인사이트 추출 → 섹션별 분석 문서 작성 |
| **산출물** | `builders-lounge-personal-notes` GitHub 레포 공개 문서 |
| **배포** | GitHub 오픈소스 공개, Builders Lounge Slack 공유 |

**발표 포인트**:
- "미팅 하나가 다섯 개의 기록이 된다" — Transcript → 분석 → 문서 → 공유 → 피드백
- 강민석님 공식 답변 수령 사례: 피드백이 GOBI 로드맵에 반영됨

---

## Case 3: VibeLearn AI WorkLog → 학습 연속성

**슬라이드 핵심 한 줄**: "기록이 AI의 장기 기억이 된다"

| 단계 | 내용 |
|------|------|
| **기록 원천** | 매 학습 세션마다 작성하는 WorkLog (`vl_worklog/YYYYMMDD_MX_*.md`) |
| **Context** | 오늘의 목표, 진행 내용, 문제 해결 로그, Daily Retrospective가 구조화된 형태로 저장 |
| **AI 협업** | 다음 세션에서 Claude Code가 WorkLog를 읽고 → 미완료 작업 파악 → 학습 계획 즉시 수립 |
| **산출물** | 세션 간 끊김 없는 연속성 — "어디까지 했더라?" 제로 |
| **배포** | 학습 결과물이 발표 자료로 직접 변환 (M1~M6 산출물 → 슬라이드) |

**발표 포인트**:
- 지금 이 발표 준비 과정 자체가 이 케이스의 실시간 증거
- "기록이 AI의 장기 기억이 된다" — 사람이 기억 못해도 AI가 WorkLog로 맥락 복원

---

## Case 4: BeYouLifeUpWithUs — Vibe Guiding 사례

**슬라이드 핵심 한 줄**: "세션 자체가 콘텐츠가 된다"

| 단계 | 내용 |
|------|------|
| **기록 원천** | 매주 온라인 세션 녹화 → Transcript 전사 → Obsidian 저장 |
| **Context** | 이선생님의 학습 과정, 질문, 진행 상황이 누적 기록으로 저장 |
| **AI 협업** | 다음 세션에서 이전 기록 기반으로 맞춤 학습 계획 즉시 수립 |
| **산출물** | 세션 영상 YouTube 공개 (1:1 가이드 과정이 콘텐츠화) |
| **배포** | YouTube 채널 콘텐츠 — "배우는 과정도 콘텐츠다" |

**발표 포인트**:
- 가르치는 것도, 배우는 것도, 함께 하는 과정도 — 기록하면 전부 콘텐츠
- AI4PKM + VibeLearn AI 소개 이벤트의 실제 모델 사례

---

## Case 5: Tehaleh 소개 영상 — KR/EN 이중 언어 + YouTube

**슬라이드 핵심 한 줄**: "36분 만에 부동산 영상을 만든다 — 기록이 없었다면 불가능했다"

| 단계 | 내용 |
|------|------|
| **기록 원천** | VibeLearn AI WorkLog (Tehaleh Topic) + Rundown + 개인 사진 (Mt. Rainier, Post & Pour) |
| **Context** | tehaleh-research.md (지역 정보 6개 섹션) + video-slide-plan.md (15장 슬라이드 기획) |
| **AI 협업** | Claude Code → Remotion 컴포넌트 생성 → Qwen3-TTS 음성 합성 (창수 클론 + 여성 3종) → 렌더링 |
| **산출물** | `tehaleh-intro-0619.mp4` (한국어 81MB) + `tehaleh-intro-0619-en.mp4` (영어 71MB) |
| **배포** | YouTube 한국어·영어 동시 업로드 (2026-06-22) |

**발표 포인트**:
- 오프닝에서 직접 재생하는 바로 그 영상 — "이게 36분 만에 만들어진 영상입니다"
- 리서치 → 기획 → 코딩 → 음성 → 렌더링 → YouTube: 전 과정이 기록 기반
- 한국어·영어 이중 언어 영상: 기록 구조가 있어서 영어 버전 추가가 2시간 내 완료됨

---

## 5개 사례 비교 매트릭스

| 사례 | 기록 도구 | AI 도구 | 최종 산출물 | 배포 채널 |
|------|----------|---------|-----------|---------|
| Case 1: 방송 → 영상 | GOBI Capture + Rundown | Claude Code + Remotion | MP4 요약 영상 | YouTube + SNS |
| Case 2: 미팅 → 문서 | Zoom 녹화 + Whisper | Claude Code | GitHub 문서 | GitHub + Slack |
| Case 3: WorkLog → 연속성 | VibeLearn AI WorkLog | Claude Code | 발표 자료 | 창발 발표 |
| Case 4: 세션 → 콘텐츠 | 세션 녹화 + Transcript | Claude Code | YouTube 영상 | YouTube |
| Case 5: Tehaleh 영상 | WorkLog + 개인 사진 | Claude Code + Remotion + Qwen3-TTS | KR/EN MP4 | YouTube (이중 언어) |

---

## 공통 패턴 (발표 핵심 구조)

```
[기록] 경험, 대화, 학습, 방송
  ↓ (구조화)
[Context] Rundown, WorkLog, Transcript, Capture
  ↓ (AI 협업)
[산출물] 영상, 문서, 슬라이드, 분석
  ↓ (배포)
[배포] YouTube, GitHub, SNS, 발표
  ↓ (새 경험 → 새 기록)
[기록으로 돌아옴]
```

**핵심**: 기록이 없으면 루프가 시작되지 않는다.

---

## 발표 사용 위치 메모

| 사례 | 발표 파트 | 슬라이드 | 소요 시간 |
|------|---------|---------|---------|
| Case 1 | 3부 (S10) | 1장 | 3~4분 |
| Case 2 | 3부 (S11) | 1장 | 3분 |
| Case 3 | 3부 (S12) | 1장 | 3분 |
| Case 4 | 3부 (S13) | 1장 (간략) | 2분 |

*M5 착수 — 2026-06-19, VibeLearn AI*
