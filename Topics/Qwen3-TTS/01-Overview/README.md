# M1 — 개요·아키텍처·자료 조사

**상태**: ✅ 완료 (2026-05-16) · **예상 학습 시간**: 3h · **난이도**: ⭐

Qwen3-TTS가 무엇이고 왜 도입하는지, 공식 1차 출처를 검증해 정리한 모듈입니다.

## 📚 학습 순서
1. [concepts/overview.md](concepts/overview.md) — Qwen3-TTS 개요·핵심 기능 4가지·모델 선택 가이드·아키텍처 요약
2. [concepts/sources.md](concepts/sources.md) — 공식 1차 출처(GitHub·블로그·HF/ModelScope)와 검증된 핵심 사실, 모델 변형 5종
3. [concepts/comparison.md](concepts/comparison.md) — Qwen3-TTS vs edge-tts vs OpenAI TTS 7개 항목 비교 매트릭스

## ✅ 이 모듈에서 확정된 것
- 공식 저장소 `github.com/QwenLM/Qwen3-TTS`, Apache-2.0, 2026-01 공개
- 모델 변형 5종(Base=클론 / CustomVoice=프리셋+instruct / VoiceDesign=자연어 설계, 각 1.7B·0.6B)
- 보이스 클론: 3초 샘플 + `ref_text` 필수 / 10개 언어(한국어 포함) / 스트리밍 ~97ms

## ⚠️ 다음 모듈로 넘기는 리스크
- **Windows 지원 공식 미명시** → M2에서 conda(py3.12)·`pip install -U qwen-tts`·GPU/CUDA 판별로 실증. flash-attn 없이 동작 가능 여부 우선 확인.

## 🔗 이동
- 다음: **M2 — Windows 로컬 환경 구축** (`../02-Setup-Windows/`)
- 로드맵: [20260516_RoadMap_Qwen3-TTS](../vl_roadmap/20260516_RoadMap_Qwen3-TTS.md)
- WorkLog: [20260516_M1_Qwen3-TTS](../vl_worklog/20260516_M1_Qwen3-TTS.md)
