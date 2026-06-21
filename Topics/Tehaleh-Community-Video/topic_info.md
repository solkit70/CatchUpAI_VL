---
title: Tehaleh-Community-Video
created: 2026-06-21 07:30:00
methodology: VibeLearn AI
methodology_version: "2.0"
tags:
  - cua-vl
  - vibelearn-ai
  - remotion
  - tehaleh
  - community-video
  - presentation-demo
---

# Tehaleh-Community-Video Topic Info

## Topic 기본 정보

**Topic 이름**: Tehaleh-Community-Video

**설명**: 창발 Product Group 발표(2026-06-26) 오프닝 데모 영상 제작 Topic이다.
"AI로 이렇게 뚝딱 만들 수 있습니다"를 실증하기 위해, 사용자가 실제 거주 중인
Tehaleh 커뮤니티 소개 영상(2~3분)을 Remotion으로 제작하는 전 과정을 기록한다.
Phase 1(리서치) → Phase 2(슬라이드 플랜) → Phase 3(Remotion 영상) 3단계로 진행한다.

**학습 목적**:
- VibeLearn AI 방법론을 사용해 영상 제작 A to Z 과정을 체계적으로 기록한다.
- Tehaleh에 대한 정보를 AI 웹 검색으로 수집·구조화하는 리서치 역량을 쌓는다.
- video-slide-plan.md 작성 → Remotion 컴포넌트 개발 → MP4 렌더링 파이프라인을 완성한다.
- 발표 데모 녹화를 통해 "기록 + AI → 즉석 콘텐츠" 공식을 실제로 증명한다.

**예상 기간**: 3~5시간 (1~2 세션)

## 학습 목표

- [ ] Tehaleh 기본 정보, 위치, IT 종사자·은퇴자 관점 리서치 문서 완성
- [ ] video-slide-plan.md (15~18슬라이드) 확정
- [ ] image-prompts.md 작성 → gpt-image-2 이미지 생성
- [ ] Remotion 컴포넌트 개발 완료 (TehalehIntro0619.tsx)
- [ ] edge-tts 오디오 생성 완료
- [ ] Qwen3-TTS 리뷰 후 교체 여부 결정
- [ ] MP4 렌더링 완료 (tehaleh-intro-0619.mp4)
- [ ] 발표 데모 녹화 완료

## 학습 환경

**OS**: Windows 11

**주요 도구**:
- Claude Code (AI 에이전트)
- Remotion (`Ingest/CatchUpAI_VL/Topics/Remotion-VideoCreation/my-first-video/`)
- edge-tts / Qwen3-TTS (gen_audio.py)
- gpt-image-2 (이미지 생성)
- OBS 또는 Windows 게임바 (스크린 녹화)

**사전 지식**:
- Remotion 영상 제작 파이프라인 경험 (membership-promo-0614 등)
- Tehaleh 실제 거주 경험 (정보 제공자 = 사용자 본인)

## 참조 자료

**내부 자료**:
- `vl_prompts/tehaleh-video-prompt.md` — 메인 실행 프롬프트 (Phase 1~3 전체)
- `vl_roadmap/20260621_RoadMap_Tehaleh-Community-Video.md` — 전체 로드맵
- `Ingest/CatchUpAI_VL/Topics/Remotion-VideoCreation/` — Remotion 프로젝트
- `Ingest/CatchUpAI_VL/Topics/The-AI-Powered-Creator/` — 부모 발표 Topic

**Remotion 산출물 경로**:
- Video ID: `tehaleh-intro-0619`
- Composition ID: `TehalehIntro0619`
- 슬라이드 플랜: `public/tehaleh-intro-0619/video-slide-plan.md`
- 오디오: `public/tehaleh-intro-0619/audio/`
- 이미지: `public/tehaleh-intro-0619/images/`

## 최종 산출물

- `vl_materials/tehaleh-research.md` — Phase 1 리서치 결과
- `public/tehaleh-intro-0619/video-slide-plan.md` — Phase 2 슬라이드 플랜
- `public/tehaleh-intro-0619/image-prompts.md` — 이미지 프롬프트
- `public/tehaleh-intro-0619/audio/` — TTS 오디오 파일
- `src/tehaleh-intro-0619/TehalehIntro0619.tsx` — Remotion 컴포넌트
- `out/tehaleh-intro-0619.mp4` — 최종 MP4
