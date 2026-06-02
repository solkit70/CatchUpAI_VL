---
title: "Qwen3-TTS — Building My Voice with AI"
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

# Qwen3-TTS — Building My Voice with AI

**Duration**: 2026-05-16 ~ 2026-05-27 (12 calendar days · 18 focused hours)
**Methodology**: VibeLearn AI 2.0 · **Modules**: 5 (M1~M5)
**Status**: ✅ Complete · **Final Output**: YouTube video (Korean + English)

## 📌 Topic Overview

Qwen3-TTS is an open-source text-to-speech model family released under Apache-2.0 by Alibaba's Qwen team in January 2026. It offers two core capabilities: **Voice Clone**, which replicates a real voice from just a 3-second sample, and **Voice Design**, which designs a custom voice style using natural-language prompts.

This topic followed the VibeLearn AI methodology to learn Qwen3-TTS and ultimately **integrate a cloned voice into a Remotion AI video production pipeline**.

### Key Decisions

- **Runtime**: DashScope International API (Singapore server, OpenAI-compatible) — switched from local after finding it unsuitable
  - Reason: No GPU + Intel i7-1355U (15W TDP) + 16 GB RAM → CPU not supported
  - Local installation research is preserved in [02-Setup-Windows](02-Setup-Windows/README-en.md) (appendix)
- **Cost**: ~$0.30 for 15 slides ($0.014 per 1,000 characters)
- **Clone Quality**: changsoo_final.wav — 4/5 stars achieved (sample v4 + ffmpeg atempo=1.08)

## 🎯 Results Summary

| Item | Result |
|------|--------|
| Voice Clone Quality | ★★★★☆ (4/5) |
| Voice Design Quality | ★★★★☆ (4/5) |
| Clone voice_id | `qwen-tts-vc-changsoo-voice-20260526021509918-daf1` |
| Remotion Integration | ✅ gen_audio_qwen.py pipeline complete |
| YouTube Upload | ✅ Korean + English versions (2026-05-27) |

## 📁 Folder Structure & Learning Path

Follow the order below to go through the topic from start to finish.

---

### 📂 01-Overview — M1: Overview, Architecture & Research

**Status**: ✅ Complete (2026-05-16) · **Estimated Time**: 3h · **Difficulty**: ⭐

This module establishes what Qwen3-TTS is and why it was adopted, verified against official primary sources.

| Order | File | Description |
|-------|------|-------------|
| 1 | [01-Overview/concepts/overview-en.md](01-Overview/concepts/overview-en.md) | Overview, 4 core features, model selection guide, architecture summary |
| 2 | [01-Overview/concepts/sources-en.md](01-Overview/concepts/sources-en.md) | Official primary sources (GitHub, blog, HF/ModelScope), verified facts, 5 model variants |
| 3 | [01-Overview/concepts/comparison-en.md](01-Overview/concepts/comparison-en.md) | 7-item comparison matrix: Qwen3-TTS vs edge-tts vs OpenAI TTS |

→ [01-Overview/README-en.md](01-Overview/README-en.md)

---

### 📂 02-Setup-Windows — (Appendix) Local Installation Research

**Status**: 📌 Appendix — Not adopted · **Difficulty**: ⭐⭐

> ⛔ This folder is **not part of the main learning path.** It preserves the research log from evaluating local execution, which was deemed unsuitable due to lack of GPU. The actual M2 is → [03-Setup-API](03-Setup-API/README-en.md)

| Order | File | Description |
|-------|------|-------------|
| Ref | [02-Setup-Windows/guides/windows-setup-en.md](02-Setup-Windows/guides/windows-setup-en.md) | GPU detection → conda → torch → qwen-tts step-by-step install (reference only) |
| Ref | [02-Setup-Windows/troubleshooting/known-issues-en.md](02-Setup-Windows/troubleshooting/known-issues-en.md) | Known issues: flash-attn, CUDA, CPU speed, download |

→ [02-Setup-Windows/README-en.md](02-Setup-Windows/README-en.md)

---

### 📂 03-Setup-API — M2: DashScope API Setup

**Status**: ✅ Complete (2026-05-24) · **Estimated Time**: 3h · **Difficulty**: ⭐⭐

This module covers setting up the DashScope cloud API to run Qwen3-TTS without a GPU.

| Order | File | Description |
|-------|------|-------------|
| 1 | [03-Setup-API/guides/api-setup-en.md](03-Setup-API/guides/api-setup-en.md) | Intl key setup → env var → SDK → first Korean synthesis, step-by-step with completion signals |
| 2 | [03-Setup-API/troubleshooting/known-issues-en.md](03-Setup-API/troubleshooting/known-issues-en.md) | Known issues: auth, region, model name, billing, fallback |
| 3 | [03-Setup-API/harness/connection_probe.py](03-Setup-API/harness/connection_probe.py) | API connectivity probe script |
| Output | [03-Setup-API/examples/hello_qwen.py](03-Setup-API/examples/hello_qwen.py) | First synthesis example code |
| Output | [03-Setup-API/examples/hello_ko.wav](03-Setup-API/examples/hello_ko.wav) | Korean synthesis output audio |
| Output | [03-Setup-API/examples/hello_en.wav](03-Setup-API/examples/hello_en.wav) | English synthesis output audio |

→ [03-Setup-API/README-en.md](03-Setup-API/README-en.md)

---

### 📂 04-VoiceClone — M3~M5: Voice Clone, Skill & Remotion Integration

**Status**: ✅ Complete (2026-05-25~29) · **Estimated Time**: 15h · **Difficulty**: ⭐⭐~⭐⭐⭐

The core module covering Voice Clone and Voice Design experiments, sample quality tuning, and full integration into the Remotion video pipeline (M3–M5).

**Tuning journey**: Sample v1 (3/5) → v4 (4/5) + ffmpeg atempo=1.08 post-processing

| Order | File | Description |
|-------|------|-------------|
| 1 | [04-VoiceClone/guides/next-session-voice-tuning-en.md](04-VoiceClone/guides/next-session-voice-tuning-en.md) | Voice quality tuning plan — Instructions experiment A & ffmpeg post-processing experiment B |
| 2 | [04-VoiceClone/examples/voice_clone.py](04-VoiceClone/examples/voice_clone.py) | Voice Clone base script (enroll → synthesize 2-step) |
| 3 | [04-VoiceClone/examples/voice_clone_instruct.py](04-VoiceClone/examples/voice_clone_instruct.py) | Instruct-model Voice Clone (speed & tone control) |
| 4 | [04-VoiceClone/examples/voice_design.py](04-VoiceClone/examples/voice_design.py) | Voice Design — design voice style with natural-language prompt |
| 5 | [04-VoiceClone/examples/register_female_vd.py](04-VoiceClone/examples/register_female_vd.py) | Female voice VC enrollment script (for multi-voice) |

**Voice Samples** (`examples/samples/`):

| File | Description |
|------|-------------|
| [changsoo_sample.mp3](04-VoiceClone/examples/samples/changsoo_sample.mp3) | Changsoo voice sample v1 |
| [changsoo_sample_v2.mp3](04-VoiceClone/examples/samples/changsoo_sample_v2.mp3) | Sample v2 |
| [changsoo_sample_v3.mp3](04-VoiceClone/examples/samples/changsoo_sample_v3.mp3) | Sample v3 |
| [changsoo_sample_v4.mp3](04-VoiceClone/examples/samples/changsoo_sample_v4.mp3) | Sample v4 ← Final adopted (4/5 stars) |

**Clone Output Audio** (`examples/`):

| File | Description |
|------|-------------|
| [changsoo_final.wav](04-VoiceClone/examples/changsoo_final.wav) | Final adopted clone voice ★★★★☆ |
| [clone_result.wav](04-VoiceClone/examples/clone_result.wav) | M3 initial clone result (3/5) |
| [tune_v4_final.wav](04-VoiceClone/examples/tune_v4_final.wav) | v4 sample + ffmpeg tuning result |
| [vd_tutor.wav](04-VoiceClone/examples/vd_tutor.wav) | Voice Design — AI tutor style |
| [vd_news.wav](04-VoiceClone/examples/vd_news.wav) | Voice Design — news anchor style |
| [vd_lively.wav](04-VoiceClone/examples/vd_lively.wav) | Voice Design — lively energetic style |

---

## 📔 WorkLog (Session Logs)

9 sessions documented in the `vl_worklog/` folder.

| Date | File | Content |
|------|------|---------|
| 2026-05-16 | [20260516_M1_Qwen3-TTS.md](vl_worklog/20260516_M1_Qwen3-TTS.md) | M1 — Overview & architecture research |
| 2026-05-16 | [20260516_M2_Qwen3-TTS.md](vl_worklog/20260516_M2_Qwen3-TTS.md) | M2 initial — Windows local attempt & unsuitable verdict |
| 2026-05-17 | [20260517_M1_Roadmap_Renewal.md](vl_worklog/20260517_M1_Roadmap_Renewal.md) | Roadmap revision — local → API switch confirmed |
| 2026-05-24 | [20260524_M2_Qwen3-TTS.md](vl_worklog/20260524_M2_Qwen3-TTS.md) | M2 — DashScope API connected, first synthesis |
| 2026-05-24 | [20260524_M3_Qwen3-TTS.md](vl_worklog/20260524_M3_Qwen3-TTS.md) | M3 — First Voice Clone (3/5) |
| 2026-05-25 | [20260525_M3ext_Qwen3-TTS.md](vl_worklog/20260525_M3ext_Qwen3-TTS.md) | M3 extended — Sample v2→v4 tuning, 4/5 achieved |
| 2026-05-29 | [20260529_M4_Qwen3-TTS.md](vl_worklog/20260529_M4_Qwen3-TTS.md) | M4 — gen_audio_qwen.py Skill complete |
| 2026-05-29 | [20260529_M5_Qwen3-TTS.md](vl_worklog/20260529_M5_Qwen3-TTS.md) | M5 — Remotion video pipeline integration complete |
| 2026-05-29 | [20260529_Final_Retrospective_Qwen3-TTS.md](vl_worklog/20260529_Final_Retrospective_Qwen3-TTS.md) | Final retrospective — full journey summary |

## 🗺️ Roadmap

| File | Content |
|------|---------|
| [vl_roadmap/20260516_RoadMap_Qwen3-TTS.md](vl_roadmap/20260516_RoadMap_Qwen3-TTS.md) | Initial roadmap (local-based) |
| [vl_roadmap/20260517_RoadMap_Qwen3-TTS.md](vl_roadmap/20260517_RoadMap_Qwen3-TTS.md) | Revised roadmap (API switch confirmed) ← **Current** |

## 🎬 Final Output

The final deliverable is a YouTube video narrated entirely with the cloned voice.

| Version | Link | Uploaded |
|---------|------|----------|
| Korean | [youtu.be/ApWkZu0RcWE](https://youtu.be/ApWkZu0RcWE) | 2026-05-27 |
| English | [youtu.be/VL-S43gnhe0](https://youtu.be/VL-S43gnhe0) | 2026-05-27 |

Remotion source code:
- Korean: `Remotion-VideoCreation/my-first-video/src/qwen3tts-0529/`
- English: `Remotion-VideoCreation/my-first-video/src/qwen3tts-0529-en/`

---

## 🔗 Related Resources

- Roadmap: [[Ingest/CatchUpAI_VL/Topics/Qwen3-TTS/vl_roadmap/20260517_RoadMap_Qwen3-TTS|Qwen3-TTS Roadmap (API-based)]]
- Related Topic: [[Topics/Daily Content Factory|Daily Content Factory]]
- GitHub (public learning materials): [github.com/solkit70/CatchUpAI_VL/tree/main/Topics/Qwen3-TTS](https://github.com/solkit70/CatchUpAI_VL/tree/main/Topics/Qwen3-TTS)
- VibeLearn AI: [github.com/solkit70/VibeLearn-AI](https://github.com/solkit70/VibeLearn-AI)
