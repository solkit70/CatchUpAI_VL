---
title: "Next Session Plan — Voice Quality Tuning"
created: 2026-05-24
tags:
  - qwen3-tts
  - voice-clone
  - next-session
---

# Next Session Plan — Changsoo Voice Quality Tuning

**Goal**: Improve the speed, tone, and naturalness of the cloned voice so it reaches a level (4+ stars) that can be used directly in real Remotion videos.

---

## Current State (as of M3 completion)

| Item | Status |
|------|--------|
| Changsoo clone voice_id | `qwen-tts-vc-changsoo-voice-20260524223616404-9ed2` |
| Current quality | 3/5 — Timbre matches but speed and naturalness need improvement |
| Registered model | `qwen3-tts-vc-2026-01-22` (instruct not available) |
| Sample file | `samples/changsoo_sample.mp3` (12 sec, 95 KB) |

---

## Experiment A — Instructions Parameter (Re-enrollment Method)

**Principle**: Re-enroll the same sample in `qwen3-tts-instruct-flash-2026-01-26` →
control speed, tone, and emotion during synthesis via natural-language `instructions`

**Step 1**: Re-enroll (script is ready — just run the command below)
```powershell
cd "C:\AI_study\2026\Changsoo_Vault\Ingest\CatchUpAI_VL\Topics\Qwen3-TTS\04-VoiceClone\examples"
python voice_clone_instruct.py --sample "samples\changsoo_sample.mp3"
```

**Step 2**: Compare these 3 instruction variants

| Version | instructions | Output File |
|---------|-------------|-------------|
| A-1 (slow & calm) | "Please speak slowly, clearly, in a calm and trustworthy voice." | `tune_slow.wav` |
| A-2 (natural speed) | "Please speak at a natural, comfortable pace, slowing slightly for emphasis." | `tune_natural.wav` |
| A-3 (broadcast tone) | "Please speak clearly and energetically like a broadcast host, at a moderate pace." | `tune_broadcast.wav` |

---

## Experiment B — ffmpeg Post-Processing (Quick Comparison)

Apply speed adjustments to the existing `clone_result.wav` for fast comparison

```powershell
cd "C:\AI_study\2026\Changsoo_Vault\Ingest\CatchUpAI_VL\Topics\Qwen3-TTS\04-VoiceClone\examples"

# 10% slower
ffmpeg -i clone_result.wav -filter:a "atempo=0.9" tune_ffmpeg_90.wav -y

# 15% slower
ffmpeg -i clone_result.wav -filter:a "atempo=0.85" tune_ffmpeg_85.wav -y

# 20% slower + slightly lower pitch
ffmpeg -i clone_result.wav -filter:a "asetrate=44100*0.97,atempo=0.87,aresample=44100" tune_ffmpeg_low.wav -y
```

---

## Comparison Evaluation Table (fill in during session)

| File | Method | Speed | Naturalness | Timbre | Overall |
|------|--------|-------|-------------|--------|---------|
| clone_result.wav (current) | VC original | /5 | /5 | 3/5 | 3/5 |
| tune_slow.wav | Instructions A-1 | /5 | /5 | /5 | /5 |
| tune_natural.wav | Instructions A-2 | /5 | /5 | /5 | /5 |
| tune_broadcast.wav | Instructions A-3 | /5 | /5 | /5 | /5 |
| tune_ffmpeg_90.wav | ffmpeg 0.9× | /5 | /5 | /5 | /5 |
| tune_ffmpeg_85.wav | ffmpeg 0.85× | /5 | /5 | /5 | /5 |

---

## DoD (Definition of Done)

- [ ] 3 Instructions variants completed
- [ ] 2 ffmpeg variants completed
- [ ] Comparison evaluation table filled in
- [ ] Final adopted version decided → saved as `changsoo_final.wav`
- [ ] voice_id or processing method for the Remotion pipeline confirmed

---

## How to Start the Session

```
"I set up a voice tuning plan last time — let's work on that today."
```

→ This file path: `04-VoiceClone/guides/next-session-voice-tuning-en.md`
