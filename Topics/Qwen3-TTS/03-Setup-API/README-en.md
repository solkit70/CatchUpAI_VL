# M2 — DashScope API Setup

**Status**: ✅ Complete (2026-05-24) · **Estimated Time**: 3h · **Difficulty**: ⭐⭐

This module covers setting up the **Alibaba Cloud Model Studio / DashScope API (Intl, Singapore)** to use Qwen3-TTS without a GPU.

## 📚 Learning Order
1. [guides/api-setup-en.md](guides/api-setup-en.md) — Key issuance → env var → SDK → first Korean synthesis, each step with a completion signal
2. [troubleshooting/known-issues-en.md](troubleshooting/known-issues-en.md) — Auth / region / model name / billing / fallback issues
3. `examples/` — `hello_ko.mp3`, `hello_en.mp3`, `model_name.txt`

## ✅ Environment Decision (confirmed)
- **API adopted.** Rationale: No GPU + i7-1355U (15W) + 16 GB RAM → local unsuitable. Local research is preserved in [02-Setup-Windows](../02-Setup-Windows/README-en.md) (appendix).
- Key advantage: **OpenAI-compatible endpoint** → replaces `base_url` in existing Remotion OpenAI-TTS code to minimize M5 integration work.

## ⚠️ Key Warnings
- Must use an **Intl (International) key** — China keys are incompatible with the Intl endpoint
- Confirm the exact model name from the official Model Studio documentation
- If Intl key issuance is unavailable → **fallback to Replicate**
- The OpenAI-compatible mode (`/compatible-mode/v1`) is **LLM-only** and does not support TTS; use the native DashScope SDK instead

## 🔗 Navigation
- Previous: [M1 — Overview](../01-Overview/README-en.md)
- Next: M3 — API Voice Clone & Voice Design (`../04-VoiceClone/`)
- Roadmap: [20260516_RoadMap_Qwen3-TTS](../vl_roadmap/20260516_RoadMap_Qwen3-TTS.md) · WorkLog: [20260524_M2_Qwen3-TTS](../vl_worklog/20260524_M2_Qwen3-TTS.md)
