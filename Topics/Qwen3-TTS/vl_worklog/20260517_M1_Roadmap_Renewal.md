---
title: "M1: 로드맵 v3.0 갱신 및 API 아키텍처 재설계"
created: 2026-05-17 10:00:00
author:
  - "[[Changsoo]]"
tags:
  - vibe-learn-ai
  - worklog
  - qwen3-tts
  - dashscope
  - harness-engineering
---

# 2026-05-17 WorkLog: Qwen3-TTS Roadmap Renewal (v3.0)

## 🎯 오늘 목표
- [x] Qwen3-TTS 로드맵을 v3.0으로 갱신 (API 및 하네스 엔지니어링 중심)
- [x] DashScope Intl API 최신 명세 및 엔드포인트 확인
- [x] '하네스 엔지니어링(Harness Engineering)' 개념을 학습 단계에 통합
- [x] VibeLearn AI 2.0 표준 템플릿(9개 항목) 준수

## 📝 진행 내용
### 1. DashScope API 최신 정보 분석
- 2026년 현재 DashScope Intl 엔드포인트: `https://dashscope-intl.aliyuncs.com/api/v1`
- 주요 모델 확인:
    - `qwen3-tts-instruct-flash`: 일반 합성용 (2026-01-26 스냅샷)
    - `qwen3-tts-vc`: 보이스 클론 전용
    - `qwen3-tts-vd`: 보이스 디자인(자연어 지시) 전용
- 환경 제어: CPU 기반 시스템(i7-1355U)임을 고려하여 로컬 실행을 배제하고 API 연동 품질 극대화 전략 수립.

### 2. 하네스 엔지니어링(Harness Engineering) 도입
- 단순 호출이 아닌, 품질과 안정성을 검증하는 **하네스(Harness)** 개념을 전 단계에 배치.
- **Connection Harness** (연결 안정성), **Quality Harness** (음질/유사도 검증), **Integration Harness** (실무 파이프라인 견고함)로 세분화.

### 3. 로드맵 v3.0 작성
- [[Ingest/CatchUpAI_VL/Topics/Qwen3-TTS/vl_roadmap/20260517_RoadMap_Qwen3-TTS|20260517_RoadMap_Qwen3-TTS.md]] 생성 완료.
- 모듈별로 VibeLearn AI 2.0의 9개 필수 항목을 반영하여 구조화.

## 🛠️ 문제 해결 로그
- **이슈**: 로컬 하드웨어(Intel i7-1355U)에서 Qwen3-TTS 실행 시 속도 저하 우려.
- **해결**: DashScope Intl API를 주력으로 설정하고, 대신 API 호출의 신뢰성을 높이는 'Harness'를 구축하여 성능 지연(Latency)을 정량적으로 관리하도록 계획 수정.

## ✅ Definition of Done (DoD)
- [x] DashScope Intl API 명세 반영: 완료
- [x] 하네스 엔지니어링 개념 통합: 완료
- [x] VibeLearn AI 2.0 템플릿 준수: 완료
- [x] 파일 생성 (`vl_roadmap/20260517_RoadMap_Qwen3-TTS.md`): 완료

## 🔍 Daily Retrospective
- **Well**: 하드웨어 제약 사항을 명확히 인지하고, 이를 극복하기 위한 API 및 품질 검증 프레임워크(Harness)를 로드맵에 잘 녹여냄.
- **Improve**: 하네스 엔지니어링의 구체적인 구현 도구(Python 라이브러리 등)에 대한 사전 조사를 M4 시작 전에 더 보강할 필요가 있음.
- **Insights**: API 기반 개발에서는 단순한 코드 작성이 아니라, 외부 의존성(API)의 품질을 상시 모니터링하는 '하네스'의 존재가 결과물의 신뢰도를 결정함.
- **Tomorrow**: M2 단계에 진입하여 DashScope Intl API 키 발급 및 기초 연결 하네스 구축 시작.

## 📂 참조 및 산출물
- **로드맵**: [[Ingest/CatchUpAI_VL/Topics/Qwen3-TTS/vl_roadmap/20260517_RoadMap_Qwen3-TTS|20260517_RoadMap_Qwen3-TTS]]
- **관련 토픽**: [[Ingest/CatchUpAI_VL/Topics/Qwen3-TTS/topic_info|Qwen3-TTS Topic Info]]

---
**Generated with [Claude Code](https://claude.com/claude-code)**
Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>
