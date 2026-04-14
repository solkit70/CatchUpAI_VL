---
title: "Google Learn Your Way: 생성형 AI로 교과서를 재창조"
created: 2026-04-03
source: https://research.google/blog/learn-your-way-reimagining-textbooks-with-generative-ai/
tags:
  - google
  - generative-ai
  - personalized-learning
  - vibe-learning
  - reference
---

## 개요

Google Research가 **Learn Your Way**를 발표했다. 정적인 교과서를 생성형 AI로 개인화된 멀티모달 학습 경험으로 변환하는 플랫폼. Google Labs에서 현재 사용 가능.

Jin이 "you should be interested in this!"라며 공유 → Vibe Learning 및 Vibe Guiding과 직접 연결되는 콘셉트.

## 핵심 개념

두 가지 이론적 기반 위에 설계됨:

1. **Multiple Representations (다중 표현)**: 이중 코딩 이론(dual coding theory)에 기반. 같은 내용을 여러 형태(텍스트, 이미지, 오디오, 마인드맵 등)로 제공하여 학습자가 개념 간 연결을 강화.

2. **Personalization (개인화)**: 학생의 학년과 관심사에 맞게 콘텐츠 자동 조정. 퀴즈 결과를 실시간으로 반영해 추가 맞춤화.

## 기술 구조

- **AI 모델**: LearnLM — Google의 교육학 기반 AI 모델 (Gemini 2.5 Pro 통합)
- **Personalization Pipeline**: 원본 PDF를 학생 수준에 맞게 재조정, 일반적 예시를 관심사 기반 예시로 교체
- **Content Generation**: 전문화된 AI 에이전트와 파인튜닝 모델을 통해 다양한 표현 형식 자동 생성

## 제공하는 5가지 콘텐츠 형식

| 형식 | 설명 |
|------|------|
| Immersive Text | 생성된 이미지와 질문이 포함된 소화하기 쉬운 텍스트 섹션 |
| Section Quizzes | 지식 격차를 발견하는 인터랙티브 퀴즈 |
| Slides & Narration | 활동과 녹화 강의가 포함된 프레젠테이션 |
| Audio Lessons | 실제 수업 방식을 모델링한 교사-학생 대화 시뮬레이션 |
| Mind Maps | 확대/축소 기능이 있는 계층적 지식 구조도 |

## 연구 결과

시카고 지역 고등학생 60명 대상 무작위 대조 실험:

- **즉시 평가**: Learn Your Way 사용자가 일반 디지털 리더 대비 **평균 9% 높은 점수**
- **3~5일 후 보유율**: Learn Your Way 그룹 **78% vs 67%** (11 포인트 차이)
- **사용자 만족도**: 100%가 평가에 대한 자신감 향상, 93%가 향후 재사용 희망 (전통 리더는 67%)

## Vibe Learning / Vibe Guiding 과의 연결

| Google Learn Your Way | 나의 시스템 |
|-----------------------|------------|
| PDF 교과서 → 개인화 콘텐츠 | VL 문서 → Vibe Guiding |
| 학생 수준 + 관심사 기반 | User Info 기반 개인화 |
| AI가 콘텐츠를 읽고 제공 | AI가 매뉴얼을 읽고 가이드 |
| Multiple Representations | 다양한 가이드 경로 |
| Real-time 퀴즈 피드백 | 사용자 행동 기반 적응 |

**핵심 공통점**: 정적인 문서를 AI가 읽어서 개인에게 맞는 동적인 경험으로 전환한다는 철학이 동일하다.

**차별점**: Google은 교육(학습)에 집중, 나의 시스템은 소프트웨어 사용(가이딩/행동)에 집중. 접근 방식은 같지만 적용 도메인이 다르다.

## 참고

현재 사용 가능한 예제:
- 면역계 생물학
- 경제 조직
- 사회학 입문
