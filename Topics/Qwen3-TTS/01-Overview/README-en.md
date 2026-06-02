# M1 — Overview, Architecture & Research

**Status**: ✅ Complete (2026-05-16) · **Estimated Time**: 3h · **Difficulty**: ⭐

This module establishes what Qwen3-TTS is and why it is being adopted, based on verified official primary sources.

## 📚 Learning Order
1. [concepts/overview-en.md](concepts/overview-en.md) — Qwen3-TTS overview, 4 core features, model selection guide, architecture summary
2. [concepts/sources-en.md](concepts/sources-en.md) — Official primary sources (GitHub, blog, HF/ModelScope), verified key facts, 5 model variants
3. [concepts/comparison-en.md](concepts/comparison-en.md) — 7-item comparison matrix: Qwen3-TTS vs edge-tts vs OpenAI TTS

## ✅ Conclusions from This Module
- Official repo: `github.com/QwenLM/Qwen3-TTS`, Apache-2.0, released 2026-01
- 5 model variants (Base=clone / CustomVoice=preset+instruct / VoiceDesign=natural-language design, each 1.7B and 0.6B)
- Voice Clone: 3-second sample + `ref_text` required / 10 languages (including Korean) / streaming ~97ms

## ⚠️ Risk Passed to Next Module
- **Windows support not officially stated** → Verified in M2 via conda (py3.12), `pip install -U qwen-tts`, and GPU/CUDA checks. Confirmed whether it works without flash-attn.

## 🔗 Navigation
- Next: **M2 — Windows Local Environment** (`../02-Setup-Windows/`) — appendix only
- Next (main path): **M2 — DashScope API Setup** (`../03-Setup-API/`)
- Roadmap: [20260516_RoadMap_Qwen3-TTS](../vl_roadmap/20260516_RoadMap_Qwen3-TTS.md)
- WorkLog: [20260516_M1_Qwen3-TTS](../vl_worklog/20260516_M1_Qwen3-TTS.md)
