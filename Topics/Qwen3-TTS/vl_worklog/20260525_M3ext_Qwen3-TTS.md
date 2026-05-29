---
title: "M3 연장: 목소리 튜닝 & 여성 VD 등록"
created: 2026-05-25
author:
  - "[[Changsoo]]"
tags:
  - vibe-learn-ai
  - worklog
  - qwen3-tts
  - voice-tune
  - voice-design
  - m3-ext
---

# WorkLog — M3 연장: 목소리 튜닝 & 여성 VD 등록

**날짜**: 2026-05-25
**Topic**: Qwen3-TTS
**모듈**: M3 연장 (Voice Tuning & Female VD) → M4 진입 준비
**학습 시간**: 시작 -- : -- - 종료 -- : --

**배경**: M3 완료 시점에서 창수 클론 품질 3/5로 목표 미달. 오늘 Instructions 튜닝 + 여성 VD 신규 등록으로 Remotion 영상 파이프라인 음성을 완성한다.

---

## 🎯 오늘의 학습 목표

- [ ] 실험 A: Instructions 3종 (`tune_slow`, `tune_natural`, `tune_broadcast`) 생성 완료
- [ ] 실험 B: ffmpeg 후처리 2~3종 생성 완료
- [ ] 비교 평가표 완성 → 최종 버전 결정 (`changsoo_final.wav`)
- [ ] VD 여성 음성 등록 (한국어 프롬프트, `language: "ko"`) → voice_id 발급
- [ ] VD 여성 합성 테스트 → 품질 3/5 이상 확인
- [ ] VOICE_MAP `VD_FEMALE` 값 확정

---

## 📚 진행 내용

### 1. 실험 A — Instructions 튜닝 (`voice_clone_instruct.py`)

**시간**: 진행 불가 — API 호환성 문제

**결과**: ❌ 미진행

| 원인 | 내용 |
|------|------|
| PipelineNotFound | `qwen3-tts-instruct-flash-2026-01-26`은 enrollment `target_model`로 미지원 |
| Voice 미지원 | VC voice_id를 instruct 모델에 전달 시 "Voice not supported" 오류 |

**메모/인사이트**: instruct 모델은 독립적인 내장 음성만 지원. VC voice_id 재사용 불가. Instructions 기능은 현재 창수 클론에 적용 불가.

---

### 2. 실험 B — 샘플 재녹음 + 텍스트 튜닝 + ffmpeg

**시간**: 2026-05-26

**시도 과정**:

| 버전 | 샘플 | 텍스트 | 속도 | 문제점 |
|------|------|--------|------|--------|
| clone_result (M3) | Recording (8) v1 | 기본 | 1.0x | 끊김, 유사도 3/5 |
| tune_text_v1_108 | Recording (11) v2 | 쉼표 강화 | 1.08x | 끊김 잔존, 말투 자연스러움 |
| tune_v3_final | Recording (13) v3 | 쉼표 강화 | 1.08x | 끊김 개선, 말투 느끼함 |
| **tune_v4_final** ✅ | Recording (14) v4 | 쉼표 강화 | 1.08x | **최종 채택** |

**최종 채택**:
- 파일: `tune_v4_final.wav` → `changsoo_final.wav`로 복사 완료
- 샘플: `samples/changsoo_sample_v4.mp3` (Recording 14, 16초)
- 방식: 쉼표 강화 텍스트 합성 + `atempo=1.08` 후처리
- voice_id: `qwen-tts-vc-changsoo-voice-20260526021509918-daf1`

**메모/인사이트**:
- 샘플의 발화 방식이 합성 말투에 직결 — 단어를 이어 흐르게 읽은 v4가 끊김 최소화
- 끊김 개선의 핵심은 샘플 품질 > 텍스트 구성 > ffmpeg 순서
- 쉼표 강화 텍스트 + 1.08x 조합이 현재 최적

---

### 3. VD 여성 음성 신규 등록 (`register_female_vd.py`)

**시간**: -- : -- - -- : --

**핵심 변경사항**: `language: "ko"` + 한국어 프롬프트 (M3에서 영어 프롬프트 → 일본 억양 교훈 반영)

**실행 명령**:
```powershell
cd "C:\AI_study\2026\Changsoo_Vault\Ingest\CatchUpAI_VL\Topics\Qwen3-TTS\03-VoiceClone\examples"
python register_female_vd.py
```

**결과**:

| 버전 | 프롬프트 요약 | voice_id | 파일 | 품질 |
|------|-------------|---------|------|------|
| female_v1 (차분·따뜻) | 30대 여성, 차분하고 따뜻한 목소리 | | vd_female_v1.wav | /5 |
| female_v2 (활기·전문) | 30대 여성, 밝고 활기찬 목소리 | | vd_female_v2.wav | /5 |

**채택 버전**: (결정 후 기입)
**최종 VD_FEMALE voice_id**: (결정 후 기입)

**메모/인사이트**:

---

## 🐛 문제 해결 로그

| # | 증상 | 원인 | 해결 |
|---|------|------|------|

---

## 📊 DoD 체크리스트

- [x] Instructions 실험 — API 미지원으로 불가, 원인 기록 완료
- [x] 샘플 재녹음 4회 + 텍스트/속도 실험 완료 + 평가 기록
- [x] `changsoo_final.wav` 결정 및 저장 (v4 샘플 + 쉼표 텍스트 + 1.08x)
- [x] 여성 음성 4종 VC 등록 완료 (외부 샘플 + 1.15x 속도 조정)
- [x] `VOICE_MAP` 7종 확정 → Slide Plan 반영 완료
- [x] `next-session-voice-tuning.md` 비교 평가표 완성 (실험 과정으로 대체)

**완료율**: 6/6 (100%) ✅

---

## 💡 Daily Retrospective

### What went well (잘된 점)

### What could be improved (개선할 점)

### Insights (인사이트)

### Tomorrow's focus (내일 집중할 것)
- M4 Harness Skill 개발 시작 (`qwen3_harness.py` 기반)
- 또는 Remotion 영상 제작 Phase 2 진입 (이미지 생성 후)

---

**작성자**: Changsoo · **방법론**: VibeLearn AI 2.0
