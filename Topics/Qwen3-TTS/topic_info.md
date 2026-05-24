---
name: Qwen3-TTS
description: Alibaba Qwen 팀의 오픈소스, 피어리뷰 모델인 Qwen3-TTS 학습 및 로컬 환경 통합
type: project
author:
  - "[[Changsoo]]"
created: 2026-05-09 12:00:00
tags:
  - vibe-learn-ai
  - tts
  - alibaba-qwen
  - open-source-ai
---

# Qwen3-TTS 학습 및 도입 계획

## Overview
Changbal 멤버인 [[Sangho Yeo]]님의 `Daily Content Factory` 프로젝트 리뷰를 통해 발견한 최신 오픈소스 TTS 모델입니다. 15초의 짧은 음성 샘플만으로도 고품질의 음성 복제가 가능하며, Mac의 Neural Engine을 활용해 로컬에서 고속으로 작동하는 것이 특징입니다.

## Goals
- [ ] Qwen3-TTS의 기술적 구조 및 모델 성능 파악
- [ ] VibeLearn AI 방법론을 적용한 로컬 설치 및 환경 구축
- [ ] 음성 복제(Voice Cloning) 성능 테스트 및 품질 최적화
- [ ] 기존 영상 제작 스킬(Remotion/OpenAI TTS 기반)에 대체 또는 병행 도입
- [ ] 라이브 방송의 실시간 음성 가이딩 및 공동 호스팅(Gobi)에 적용

## Prerequisites
- [ ] Alibaba Qwen3-TTS GitHub 레포지토리 분석
- [ ] 로컬 실행 환경(Python/Conda) 준비
- [ ] 음성 샘플(15s) 확보

## Environment & Plan (2026-05-16 확정)
- **실행 환경**: **Cloud API — Alibaba Cloud Model Studio / DashScope (Intl, OpenAI 호환)** · 백업: Replicate
  - ※ 로컬 검토 결과 부적합으로 API 전환 확정: 현재 PC가 GPU 없음 + Intel i7-1355U(15W 저전력) + RAM 16GB, 공식 패키지 CPU 미지원. 근거는 [[Ingest/CatchUpAI_VL/Topics/Qwen3-TTS/02-Setup-Windows/README|02-Setup-Windows(로컬 부적합 부록)]]
  - ※ 위 Overview의 "Mac Neural Engine" 언급은 본 토픽 학습 범위에서 무효
- **학습 기간**: 1주 집중 · 5개 모듈 (VibeLearn AI)
- **최종 산출물**: Qwen3-TTS 음성 제작 Skill + Remotion AI 영상 제작 Skill 연동 (현행 OpenAI TTS / MS TTS와 병행·대체 가능)
- **로드맵**: [[Ingest/CatchUpAI_VL/Topics/Qwen3-TTS/vl_roadmap/20260516_RoadMap_Qwen3-TTS|20260516_RoadMap_Qwen3-TTS]]

## Related Documents
- [[Topics/Daily Content Factory|Daily Content Factory (리마목장) 토픽]]
- [[Ingest/Documents/Business/2026-05-05 Sangho Yeo - Overview|Service Overview]]
- [[AI/Research/2026-05-06 리마목장 Overview 피드백 정리 by Changsoo|피드백 정리 문서]]
