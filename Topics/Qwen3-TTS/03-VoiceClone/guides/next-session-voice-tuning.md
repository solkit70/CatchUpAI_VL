---
title: "다음 세션 계획 — 목소리 품질 튜닝"
created: 2026-05-24
tags:
  - qwen3-tts
  - voice-clone
  - next-session
---

# 다음 세션 계획 — 창수님 목소리 품질 튜닝

**목표**: 클론된 목소리의 말하는 속도, 톤, 자연스러움을 개선해서  
실제 Remotion 영상에 바로 쓸 수 있는 수준(4점 이상)으로 끌어올린다.

---

## 현재 상태 (M3 완료 시점)

| 항목 | 상태 |
|------|------|
| 창수 클론 voice_id | `qwen-tts-vc-changsoo-voice-20260524223616404-9ed2` |
| 현재 품질 | 3/5 — 음색은 맞으나 속도·자연도 개선 필요 |
| 등록 모델 | `qwen3-tts-vc-2026-01-22` (instruct 불가) |
| 샘플 파일 | `samples/changsoo_sample.mp3` (12초, 95KB) |

---

## 실험 A — Instructions 파라미터 (재등록 방식)

**원리**: `qwen3-tts-instruct-flash-2026-01-26`에 같은 샘플을 재등록 →  
합성 시 `instructions`로 속도·톤·감정을 자연어로 제어

**Step 1**: 재등록 (스크립트 준비 완료 — 아래 명령만 실행)
```powershell
cd "C:\AI_study\2026\Changsoo_Vault\Ingest\CatchUpAI_VL\Topics\Qwen3-TTS\03-VoiceClone\examples"
python voice_clone_instruct.py --sample "samples\changsoo_sample.mp3"
```

**Step 2**: 아래 instructions 3종 비교 실험

| 버전 | instructions | 출력 파일 |
|------|-------------|---------|
| A-1 (느리고 차분) | "천천히, 또렷하게, 차분하고 신뢰감 있는 목소리로 말해주세요." | `tune_slow.wav` |
| A-2 (자연스러운 속도) | "자연스럽고 편안한 속도로, 강조할 부분에서 살짝 천천히 말해주세요." | `tune_natural.wav` |
| A-3 (방송 톤) | "방송 진행자처럼 명확하고 활기차게, 적당한 속도로 말해주세요." | `tune_broadcast.wav` |

---

## 실험 B — ffmpeg 후처리 (즉시 비교용)

기존 `clone_result.wav`를 속도만 조절해서 빠른 비교

```powershell
cd "C:\AI_study\2026\Changsoo_Vault\Ingest\CatchUpAI_VL\Topics\Qwen3-TTS\03-VoiceClone\examples"

# 10% 느리게
ffmpeg -i clone_result.wav -filter:a "atempo=0.9" tune_ffmpeg_90.wav -y

# 15% 느리게
ffmpeg -i clone_result.wav -filter:a "atempo=0.85" tune_ffmpeg_85.wav -y

# 20% 느리게 + 피치 약간 낮춤
ffmpeg -i clone_result.wav -filter:a "asetrate=44100*0.97,atempo=0.87,aresample=44100" tune_ffmpeg_low.wav -y
```

---

## 비교 평가표 (세션 중 채울 것)

| 파일 | 방식 | 속도 | 자연도 | 음색 | 종합 |
|------|------|------|--------|------|------|
| clone_result.wav (현재) | VC 원본 | /5 | /5 | 3/5 | 3/5 |
| tune_slow.wav | Instructions A-1 | /5 | /5 | /5 | /5 |
| tune_natural.wav | Instructions A-2 | /5 | /5 | /5 | /5 |
| tune_broadcast.wav | Instructions A-3 | /5 | /5 | /5 | /5 |
| tune_ffmpeg_90.wav | ffmpeg 0.9x | /5 | /5 | /5 | /5 |
| tune_ffmpeg_85.wav | ffmpeg 0.85x | /5 | /5 | /5 | /5 |

---

## DoD (완료 기준)

- [ ] Instructions 방식 3종 실험 완료
- [ ] ffmpeg 방식 2종 실험 완료
- [ ] 비교 평가표 완성
- [ ] 최종 채택 버전 결정 → `changsoo_final.wav` 저장
- [ ] Remotion 파이프라인에 사용할 voice_id 또는 처리 방식 확정

---

## 세션 시작 방법

```
"지난번에 목소리 튜닝 계획 세워뒀는데 오늘 그것 진행하겠습니다."
```

→ 이 파일 경로: `03-VoiceClone/guides/next-session-voice-tuning.md`
