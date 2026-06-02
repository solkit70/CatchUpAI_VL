# TTS Comparison Matrix — Qwen3-TTS vs edge-tts (MS) vs OpenAI TTS (M1)

> Basis for adoption decision. Qwen3-TTS values are verified from official sources; other engines reflect generally known facts. Uncertain items are marked "needs verification."

| Item | Qwen3-TTS | edge-tts (MS, current) | OpenAI TTS (current) |
|------|-----------|------------------------|----------------------|
| Supported Languages | 10 (incl. Korean) + dialects | Multilingual (incl. Korean, many Neural voices) | Multilingual (Korean available) |
| Voice Clone | ✅ 3-sec sample + `ref_text` required | ❌ Not supported | ❌ Not supported in standard TTS |
| Voice Control Method | Natural-language `instruct` (VoiceDesign/CustomVoice) | SSML prosody (rate/pitch) level | Preset voices + limited instructions |
| Streaming | ✅ ~97ms latency | Limited (stream output) | ✅ Streaming supported |
| License / Cost | Apache-2.0, open-source (free) | Free (MS service) | Paid API (usage-based) |
| Runtime | Local (GPU recommended) / ModelScope | Cloud (network required) | Cloud API |
| Windows Support | Needs verification (no official statement, CUDA examples) | ✅ (Python package) | ✅ (API) |

## Runtime Update (2026-05-16): API Confirmed
- The "Local (GPU recommended)" entry above is unsuitable for this environment (no GPU, i7-1355U 15W, 16 GB RAM) → **Qwen3-TTS confirmed to use via DashScope API (Intl, OpenAI-compatible)**.
- Updated effective attributes for Qwen3-TTS: "Windows Support = ✅ (API)", "Cost = usage-based (synthesis ≈ $0.013/1k chars, clone $0.01/enrollment, 90-day free quota)" — the model itself is Apache-2.0 but the hosted API is billed.
- Details: [03-Setup-API](../../03-Setup-API/README-en.md) · Local research appendix: [02-Setup-Windows](../../02-Setup-Windows/README-en.md)

## One-Line Conclusion (provisional, confirmed with M3 quality evaluation)
- **Consistent character voice / voice cloning** needed → Qwen3-TTS (API) is superior.
- **Fast, lightweight multilingual narration at zero cost** → current edge-tts still has the advantage.
- Final adoption criteria will be confirmed numerically in **M3 (quality A/B) + M5 (adoption guide & cost estimate)**.
