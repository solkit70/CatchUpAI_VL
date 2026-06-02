---
title: "Qwen3-TTS — 내 목소리를 AI로 만들기"
created: 2026-05-16 12:00:00
updated: 2026-06-01 00:00:00
author:
  - "[[Changsoo]]"
tags:
  - vibe-learn-ai
  - tts
  - alibaba-qwen
  - open-source-ai
  - voice-clone
---

# Qwen3-TTS — 내 목소리를 AI로 만들기

**기간**: 2026-05-16 ~ 2026-05-27 (캘린더 12일 · 실제 집중 18시간)
**방법론**: VibeLearn AI 2.0 · **모듈**: 5개 (M1~M5)
**상태**: ✅ 완료 · **최종 산출물**: YouTube 영상 (한국어 + 영어)

## 📌 Topic 소개

Qwen3-TTS는 알리바바 Qwen 팀이 2026년 1월 Apache-2.0으로 공개한 오픈소스 텍스트-음성 변환(TTS) 모델입니다. **3초짜리 음성 샘플 하나**로 실제 목소리를 복제하는 Voice Clone과, 자연어 프롬프트로 원하는 음색을 설계하는 Voice Design, 두 가지 핵심 기능을 제공합니다.

이 Topic은 VibeLearn AI 방법론으로 Qwen3-TTS를 학습하고, 최종적으로 **Remotion AI 영상 제작 파이프라인에 클론 목소리를 연동**하는 것을 목표로 진행했습니다.

### 핵심 결정 사항

- **실행 환경**: DashScope Intl API (싱가포르 서버, OpenAI 호환) — 로컬 설치 부적합으로 전환
  - 이유: GPU 없음 + Intel i7-1355U(15W) + RAM 16GB → CPU 미지원
  - 로컬 검토 기록은 [02-Setup-Windows](02-Setup-Windows/README.md)(부록)에 보존
- **비용**: 슬라이드 15개 기준 약 $0.30 (1,000자당 $0.014)
- **클론 품질**: changsoo_final.wav — 5점 만점 4점 달성 (샘플 v4 + ffmpeg atempo=1.08)

## 🎯 학습 결과 요약

| 항목 | 결과 |
|------|------|
| Voice Clone 품질 | ★★★★☆ (4/5) |
| Voice Design 품질 | ★★★★☆ (4/5) |
| 클론 voice_id | `qwen-tts-vc-changsoo-voice-20260526021509918-daf1` |
| Remotion 연동 | ✅ gen_audio_qwen.py 파이프라인 완성 |
| YouTube 업로드 | ✅ 한국어 + 영어 버전 (2026-05-27) |

## 📁 폴더 구조 & 학습 경로

아래 순서대로 학습하면 처음부터 따라올 수 있습니다.

---

### 📂 01-Overview — M1: 개요·아키텍처·자료 조사

**상태**: ✅ 완료 (2026-05-16) · **예상 시간**: 3h · **난이도**: ⭐

Qwen3-TTS가 무엇이고, 왜 도입하는지 공식 1차 출처를 검증해 정리한 모듈입니다.

| 순서 | 파일 | 내용 |
|------|------|------|
| 1 | [01-Overview/concepts/overview.md](01-Overview/concepts/overview.md) | Qwen3-TTS 개요·핵심 기능 4가지·모델 선택 가이드·아키텍처 요약 |
| 2 | [01-Overview/concepts/sources.md](01-Overview/concepts/sources.md) | 공식 1차 출처(GitHub·블로그·HF/ModelScope)와 검증된 핵심 사실, 모델 변형 5종 |
| 3 | [01-Overview/concepts/comparison.md](01-Overview/concepts/comparison.md) | Qwen3-TTS vs edge-tts vs OpenAI TTS 7개 항목 비교 매트릭스 |

→ [01-Overview/README.md](01-Overview/README.md)

---

### 📂 02-Setup-Windows — (부록) 로컬 설치 검토 기록

**상태**: 📌 부록 — 채택 안 함 · **난이도**: ⭐⭐

> ⛔ 이 폴더는 **정식 학습 경로가 아닙니다.** 로컬 구동 가능성을 검토했으나 GPU 부재로 부적합 판정 후 API로 전환한 기록을 보존합니다. 실제 M2는 → [03-Setup-API](03-Setup-API/README.md)

| 순서 | 파일 | 내용 |
|------|------|------|
| 참고 | [02-Setup-Windows/guides/windows-setup.md](02-Setup-Windows/guides/windows-setup.md) | GPU 판별 → conda → torch → qwen-tts 단계별 설치 (참고용) |
| 참고 | [02-Setup-Windows/troubleshooting/known-issues.md](02-Setup-Windows/troubleshooting/known-issues.md) | flash-attn·CUDA·CPU 속도·다운로드 등 알려진 이슈 |

→ [02-Setup-Windows/README.md](02-Setup-Windows/README.md)

---

### 📂 03-Setup-API — M2: DashScope API 환경 구축

**상태**: ✅ 완료 (2026-05-24) · **예상 시간**: 3h · **난이도**: ⭐⭐

GPU 없이 클라우드 API로 Qwen3-TTS를 사용하기 위한 DashScope 환경 구축 모듈입니다.

| 순서 | 파일 | 내용 |
|------|------|------|
| 1 | [03-Setup-API/guides/api-setup.md](03-Setup-API/guides/api-setup.md) | Intl 키 발급 → 환경변수 → SDK 설치 → 첫 한국어 합성 단계별 가이드 |
| 2 | [03-Setup-API/troubleshooting/known-issues.md](03-Setup-API/troubleshooting/known-issues.md) | 인증·리전·모델명·과금·폴백 관련 알려진 이슈 |
| 3 | [03-Setup-API/harness/connection_probe.py](03-Setup-API/harness/connection_probe.py) | API 연결 확인용 프로브 스크립트 |
| 산출물 | [03-Setup-API/examples/hello_qwen.py](03-Setup-API/examples/hello_qwen.py) | 첫 합성 예제 코드 |
| 산출물 | [03-Setup-API/examples/hello_ko.wav](03-Setup-API/examples/hello_ko.wav) | 한국어 합성 결과 오디오 |
| 산출물 | [03-Setup-API/examples/hello_en.wav](03-Setup-API/examples/hello_en.wav) | 영어 합성 결과 오디오 |

→ [03-Setup-API/README.md](03-Setup-API/README.md)

---

### 📂 04-VoiceClone — M3~M5: 보이스 클론·Skill·Remotion 통합

**상태**: ✅ 완료 (2026-05-25~29) · **예상 시간**: 15h · **난이도**: ⭐⭐~⭐⭐⭐

Voice Clone과 Voice Design 실험, 샘플 품질 튜닝, Remotion 영상 파이프라인 연동까지 M3~M5를 아우르는 핵심 모듈입니다.

**Voice Clone 튜닝 과정**: 샘플 v1(3점) → v4(4점) + ffmpeg atempo=1.08 후처리

| 순서 | 파일 | 내용 |
|------|------|------|
| 1 | [04-VoiceClone/guides/next-session-voice-tuning.md](04-VoiceClone/guides/next-session-voice-tuning.md) | 목소리 품질 튜닝 계획 — Instructions 실험 A·ffmpeg 후처리 실험 B 비교표 |
| 2 | [04-VoiceClone/examples/voice_clone.py](04-VoiceClone/examples/voice_clone.py) | Voice Clone 기본 스크립트 (등록 → 합성 2단계) |
| 3 | [04-VoiceClone/examples/voice_clone_instruct.py](04-VoiceClone/examples/voice_clone_instruct.py) | Instruct 모델 기반 Voice Clone (속도·톤 제어) |
| 4 | [04-VoiceClone/examples/voice_design.py](04-VoiceClone/examples/voice_design.py) | Voice Design — 자연어 프롬프트로 음색 설계 |
| 5 | [04-VoiceClone/examples/register_female_vd.py](04-VoiceClone/examples/register_female_vd.py) | 여성 목소리 VC 등록 스크립트 (멀티보이스용) |

**샘플 파일** (`examples/samples/`):

| 파일 | 설명 |
|------|------|
| [changsoo_sample.mp3](04-VoiceClone/examples/samples/changsoo_sample.mp3) | 창수 목소리 샘플 v1 |
| [changsoo_sample_v2.mp3](04-VoiceClone/examples/samples/changsoo_sample_v2.mp3) | 샘플 v2 |
| [changsoo_sample_v3.mp3](04-VoiceClone/examples/samples/changsoo_sample_v3.mp3) | 샘플 v3 |
| [changsoo_sample_v4.mp3](04-VoiceClone/examples/samples/changsoo_sample_v4.mp3) | 샘플 v4 ← 최종 채택 (4점) |

**클론 결과 오디오** (`examples/`):

| 파일 | 설명 |
|------|------|
| [changsoo_final.wav](04-VoiceClone/examples/changsoo_final.wav) | 최종 채택 클론 목소리 ★★★★☆ |
| [clone_result.wav](04-VoiceClone/examples/clone_result.wav) | M3 초기 클론 결과 (3점) |
| [tune_v4_final.wav](04-VoiceClone/examples/tune_v4_final.wav) | v4 샘플 + ffmpeg 튜닝 결과 |
| [vd_tutor.wav](04-VoiceClone/examples/vd_tutor.wav) | Voice Design — AI 튜터 스타일 |
| [vd_news.wav](04-VoiceClone/examples/vd_news.wav) | Voice Design — 뉴스 앵커 스타일 |
| [vd_lively.wav](04-VoiceClone/examples/vd_lively.wav) | Voice Design — 활기찬 스타일 |

---

## 📔 WorkLog (학습 일지)

총 9개 세션 기록. `vl_worklog/` 폴더에 있습니다.

| 날짜 | 파일 | 내용 |
|------|------|------|
| 2026-05-16 | [20260516_M1_Qwen3-TTS.md](vl_worklog/20260516_M1_Qwen3-TTS.md) | M1 — 개요·아키텍처 조사 |
| 2026-05-16 | [20260516_M2_Qwen3-TTS.md](vl_worklog/20260516_M2_Qwen3-TTS.md) | M2 초기 — Windows 로컬 시도 및 부적합 판정 |
| 2026-05-17 | [20260517_M1_Roadmap_Renewal.md](vl_worklog/20260517_M1_Roadmap_Renewal.md) | 로드맵 개정 — 로컬 → API 전환 확정 |
| 2026-05-24 | [20260524_M2_Qwen3-TTS.md](vl_worklog/20260524_M2_Qwen3-TTS.md) | M2 — DashScope API 연결 성공·첫 합성 |
| 2026-05-24 | [20260524_M3_Qwen3-TTS.md](vl_worklog/20260524_M3_Qwen3-TTS.md) | M3 — 첫 Voice Clone (3점) |
| 2026-05-25 | [20260525_M3ext_Qwen3-TTS.md](vl_worklog/20260525_M3ext_Qwen3-TTS.md) | M3 연장 — 샘플 v2→v4 튜닝, 4점 달성 |
| 2026-05-29 | [20260529_M4_Qwen3-TTS.md](vl_worklog/20260529_M4_Qwen3-TTS.md) | M4 — gen_audio_qwen.py Skill 완성 |
| 2026-05-29 | [20260529_M5_Qwen3-TTS.md](vl_worklog/20260529_M5_Qwen3-TTS.md) | M5 — Remotion 영상 파이프라인 연동 완료 |
| 2026-05-29 | [20260529_Final_Retrospective_Qwen3-TTS.md](vl_worklog/20260529_Final_Retrospective_Qwen3-TTS.md) | 최종 회고 — 전체 여정 정리 |

## 🗺️ 로드맵

| 파일 | 내용 |
|------|------|
| [vl_roadmap/20260516_RoadMap_Qwen3-TTS.md](vl_roadmap/20260516_RoadMap_Qwen3-TTS.md) | 초기 로드맵 (로컬 기반) |
| [vl_roadmap/20260517_RoadMap_Qwen3-TTS.md](vl_roadmap/20260517_RoadMap_Qwen3-TTS.md) | 개정 로드맵 (API 전환 확정) ← **현행** |

## 🎬 최종 산출물

이 Topic의 최종 산출물은 클론 목소리로 제작된 YouTube 영상입니다.

| 버전 | 링크 | 업로드 |
|------|------|--------|
| 한국어 | [youtu.be/ApWkZu0RcWE](https://youtu.be/ApWkZu0RcWE) | 2026-05-27 |
| 영어 | [youtu.be/VL-S43gnhe0](https://youtu.be/VL-S43gnhe0) | 2026-05-27 |

Remotion 영상 소스 코드:
- 한국어: `Remotion-VideoCreation/my-first-video/src/qwen3tts-0529/`
- 영어: `Remotion-VideoCreation/my-first-video/src/qwen3tts-0529-en/`

---

## 🔗 관련 자료

- 로드맵: [[Ingest/CatchUpAI_VL/Topics/Qwen3-TTS/vl_roadmap/20260517_RoadMap_Qwen3-TTS|Qwen3-TTS 로드맵 (API 기반)]]
- 관련 Topic: [[Topics/Daily Content Factory|Daily Content Factory]]
- GitHub (학습 자료 공개): [github.com/solkit70/CatchUpAI_VL/tree/main/Topics/Qwen3-TTS](https://github.com/solkit70/CatchUpAI_VL/tree/main/Topics/Qwen3-TTS)
- VibeLearn AI: [github.com/solkit70/VibeLearn-AI](https://github.com/solkit70/VibeLearn-AI)
