---
title: "Topic Retrospective: Qwen3-TTS"
created: 2026-05-29
author:
  - "[[Changsoo]]"
tags:
  - vibe-learn-ai
  - retrospective
  - qwen3-tts
---

# Topic Retrospective: Qwen3-TTS

**작성일**: 2026-05-29
**Topic**: Qwen3-TTS
**학습 기간**: 2026-05-16 ~ 2026-05-29 (약 2주)
**방법론**: VibeLearn AI v2.0

---

## 1. 전체 학습 여정 통계

### 모듈별 진행

| 모듈 | 예상 시간 | 실제 시간 | 날짜 | 핵심 산출물 |
|------|----------|----------|------|-----------|
| M1 개요 & 아키텍처 | 3h | ~2h | 05/16 | 개념 정리, API 구조 분석 |
| M2 DashScope API 환경 | 3h | ~2h | 05/16~05/24 | hello_qwen.py, API 연결 성공 |
| M3 Voice Clone & Quality | 5h | ~4h | 05/24 | changsoo 클론 3/5, VD 튜터 4/5 |
| M3 연장 Voice Tuning | (추가) | ~3h | 05/25~05/26 | changsoo_final.wav 4/5, 여성 VD 4종 |
| M4 Harness Skill 개발 | 6h | ~3h | 05/26 | gen_audio_qwen.py (Live #11용) |
| M5 Remotion 통합 | 5h | ~4h | 05/24~05/27 | Live #11 YouTube 업로드 완료 |
| **합계** | **22h** | **~18h** | **14일** | **YouTube 영상 2편 + 클론 voice_id** |

### 효율성 분석
- **예상 대비 실제**: 22시간 → 약 18시간 (82% 소요)
- **가장 효율적**: M4·M5 (실제 영상 제작으로 병합 처리)
- **가장 시간이 걸린 부분**: 클론 품질 튜닝 (M3 연장) — 샘플 v1~v4, ffmpeg 조합 반복

---

## 2. 핵심 학습 내용

### 기술 역량

| 항목 | 학습 전 | 학습 후 |
|------|--------|--------|
| Qwen3-TTS API | 모름 | DashScope Intl API 호출, VC·VD 모델 완전 이해 |
| Voice Clone | 개념만 앎 | 3초 샘플로 실제 목소리 클론 완료 (changsoo_final.wav) |
| Voice Design | 모름 | 한국어 프롬프트 기반 음색 설계, 영어 프롬프트 억양 이슈 파악 |
| TTS 파이프라인 | edge-tts만 앎 | Qwen3-TTS 배치 처리 harness 직접 구현 |
| Remotion 통합 | 기존 edge-tts만 사용 | Qwen3-TTS VC 전면 교체 + 멀티보이스 적용 |

### 핵심 개념 정리

1. **VC vs VD 트레이드오프**: VC는 정체성(실제 목소리), VD는 용도 맞춤(스타일 설계). 채널 아이덴티티엔 VC, 특정 캐릭터나 톤엔 VD.

2. **한국어 프롬프트 필수 원칙**: VD 모델에 영어 프롬프트 입력 시 일본어/영어 억양 패턴 적용 — 한국어 콘텐츠에는 반드시 한국어 프롬프트.

3. **샘플 품질 > 텍스트 > 속도**: 클론 품질 향상 순서. v4 샘플(단어를 이어 흐르게 읽기)이 끊김을 가장 크게 개선.

4. **AUDIO_HEAD_PAD + atempo 패턴**: 오디오 앞 1.0s + 뒤 0.4s 패딩 + 1.08배속 조합이 자연스러운 나레이션 흐름.

5. **Harness = VOICE_MAP + 건너뛰기 로직**: 슬라이드별 음성 전략을 딕셔너리로 관리 + 이미 생성된 파일 건너뛰기 → 반복 수정 시 빠른 피드백 루프.

---

## 3. 산출물 현황

### 코드 산출물

| 파일 | 위치 | 설명 |
|------|------|------|
| `voice_clone.py` | `03-VoiceClone/examples/` | Voice Enrollment + 합성 |
| `voice_design.py` | `03-VoiceClone/examples/` | Voice Design 합성 |
| `register_female_vd.py` | `03-VoiceClone/examples/` | 여성 VD 4종 등록 |
| `gen_audio_qwen.py` | `live11-0524/` (Remotion) | 실전 Harness Skill |
| `changsoo_final.wav` | `03-VoiceClone/examples/` | 최종 클론 결과물 |

### 핵심 voice_id 목록

| 종류 | voice_id | 품질 | 용도 |
|------|---------|------|------|
| 창수 VC 최종 | `qwen-tts-vc-changsoo-voice-20260526021509918-daf1` | 4/5 | 메인 나레이터 |
| VD 튜터 | `qwen-tts-vd-tutor-voice-20260524223907309-beb8` | 4/5 | 활기찬 설명 |
| VD 뉴스 | `qwen-tts-vd-news-voice-20260524223858597-f0cf` | 1/5 | ❌ 일본 억양 |
| 여성 VC #1~4 | (5/26 등록) | 미평가 | 멀티보이스용 |

### 최종 영상 산출물

- **Live #11 한국어**: https://youtu.be/ApWkZu0RcWE (Qwen3-TTS 전면 적용)
- **Live #11 영어**: https://youtu.be/VL-S43gnhe0

---

## 4. 발생한 문제와 해결

| # | 문제 | 원인 | 해결 |
|---|------|------|------|
| 1 | Voice Design 400 에러 | `MultiModalConversation.call()`로 VD 호출 — 잘못된 방식 | `customization` REST 엔드포인트 + `requests.post()`로 교체 |
| 2 | vd_news.wav 일본 억양 | 영어 프롬프트 → 모델이 영어/일본어 패턴 적용 | 한국어 프롬프트 사용 원칙 확립 |
| 3 | Instructions 방식 미지원 | `qwen3-tts-instruct-flash`는 VC voice_id 재사용 불가 | VC 모델에서 샘플 품질 향상으로 대체 |
| 4 | 클론 끊김 현상 (v1~v3) | 샘플에서 단어 사이 멈춤, 기본 텍스트 | 샘플 v4 (이어 흐르게 읽기) + 쉼표 강화 텍스트 |

---

## 5. Self-Assessment

### 개념 이해 ⭐⭐⭐⭐
- [x] VC와 VD의 차이, 적합한 사용 시점 설명 가능
- [x] DashScope Intl API 구조 (enrollment → synthesis 2단계) 이해
- [x] 한국어 콘텐츠에 한국어 프롬프트를 써야 하는 이유 설명 가능
- [x] 클론 품질 향상 3대 원칙 (샘플 > 텍스트 > 속도) 이해

### 실무 활용 ⭐⭐⭐⭐⭐
- [x] changsoo_final.wav — 실제 YouTube 영상에 나레이션으로 적용 완료
- [x] gen_audio_qwen.py — 재사용 가능한 배치 처리 harness 완성
- [x] 멀티보이스 패턴 — 슬라이드별 다른 목소리로 영상 생동감 향상
- [x] 전체 파이프라인 (TTS → Remotion → YouTube) 실전 가동

### AI 협업 ⭐⭐⭐⭐
- [x] 오류 발생 시 원인 분석 + 수정 방향 제시 가능
- [x] API 문서 읽고 적합한 엔드포인트/파라미터 직접 선택
- [x] 품질 평가를 수치화(1~5점)하여 객관적 비교

### 종합 평가: ⭐⭐⭐⭐½

---

## 6. CUA_VL 방법론 효과성 평가

### 효과적이었던 점
1. **로드맵의 유연성**: M4·M5를 독립 모듈로 진행하지 않고 실제 Live #11 제작으로 통합 — 계획보다 실질 산출물이 훨씬 가치 있었음
2. **M3 연장의 가치**: DoD에 없던 품질 개선을 자발적으로 추가 — changsoo_final.wav의 4/5 품질이 M3 종료 시의 3/5보다 훨씬 좋은 영상을 만들었음
3. **워크로그 실시간 기록**: 클론 튜닝 과정(v1~v4)이 기록되어 어떤 방식이 효과적인지 추적 가능

### 개선할 점
1. **VC Instructions 실험 계획 재조정**: 실제로 불가능한 기능을 로드맵에 포함했다가 시간 낭비. API 가능 여부를 M2에서 먼저 확인하는 패턴 필요.
2. **harness 단위 테스트 부재**: `test_harness.py`는 구현하지 않음. 실전 테스트(영상 제작)로 대체했으나 재사용 시 유닛 테스트가 있으면 더 안전.

---

## 7. 향후 활용 방향

### 즉시 활용 가능
- Live #12, #13 등 모든 방송 영상 나레이션에 changsoo_final.wav 적용
- 멀티보이스 패턴으로 각 섹션 특성에 맞는 목소리 선택

### 추가 탐구 권장
- 더 긴 샘플(30초+)로 클론 품질 향상 실험
- 여성 VC 4종 품질 비교 평가 → 최적 버전 채택
- `qwen3-tts-max` (고품질 모델) vs `qwen3-tts` 품질 비교

---

## 8. 통계 요약

| 항목 | 수치 |
|------|------|
| 총 학습 기간 | 14일 (05/16 ~ 05/29) |
| 실제 학습 시간 | 약 18시간 |
| 모듈 수 | 5개 (M1~M5) + M3 연장 |
| 등록 voice_id 수 | 7개 (창수 VC 2 + VD 3 + 여성 VC 4) |
| 최종 클론 품질 | 4/5 (changsoo_final.wav) |
| 실제 영상 제작 | 2편 (Live #11 한·영, YouTube 업로드) |
| WorkLog 수 | 6개 |

---

**방법론**: VibeLearn AI v2.0
**Retrospective 버전**: 1.0
**작성자**: Changsoo (Claude Code 활용)
