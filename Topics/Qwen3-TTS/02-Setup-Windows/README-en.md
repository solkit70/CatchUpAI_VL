# (Appendix) Windows Local Review — Not Adopted (Superseded)

> ⛔ **This module is not the official learning path.** It is preserved as a research record of evaluating local execution, which was deemed unsuitable.
> The actual M2 is **API path** → [03-Setup-API](../03-Setup-API/README-en.md)
>
> **Local unsuitable conclusion**: This PC has no GPU + Intel i7-1355U (15W low-power) + 16 GB RAM. The official `qwen-tts` package requires CUDA (no CPU support), and flash-attn is Linux-only. The only CPU path via the unofficial Rust/Q4 build barely runs in real-time on a powerful i9, making it inefficient on this low-power chip. **Confirmed switch to API-based approach.**

**Status**: 📌 Appendix (research record) · **Difficulty**: ⭐⭐

The documents below are reference materials for anyone who wishes to attempt local execution. The key insight was **avoiding FlashAttention2 (Linux-only) by using SDPA** and branching on GPU vs CPU.

## 📚 Learning Order
1. [guides/windows-setup-en.md](guides/windows-setup-en.md) — Step 0 (GPU detection) → conda → torch (branch) → `qwen-tts` → first wav. Completion signals at each step.
2. [troubleshooting/known-issues-en.md](troubleshooting/known-issues-en.md) — Known issues: flash-attn / CUDA / CPU speed / downloads
3. `examples/` — `hello_ko.wav`, `hello_en.wav` (output of Step 4)

## ✅ Environment Decision (confirmed)
- **Windows local not adopted** (API switch considered and then finalized). Rationale: CPU achieves ~40–90 sec for a 30-sec voice which is technically usable, but GPU would be needed for comfortable use.

## ⚠️ Key Warnings
- Do NOT install flash-attn (incompatible with Windows) → use `attn_implementation="sdpa"`
- Without GPU, use the lightweight `0.6B` model
- Confirm exact Windows run flags from the official Windows guide before Step 0

## 🔗 Navigation
- Previous: [M1 — Overview](../01-Overview/README-en.md)
- Next (main path): [M2 — DashScope API Setup](../03-Setup-API/README-en.md)
- Roadmap: [20260516_RoadMap_Qwen3-TTS](../vl_roadmap/20260516_RoadMap_Qwen3-TTS.md) · WorkLog: [20260516_M2_Qwen3-TTS](../vl_worklog/20260516_M2_Qwen3-TTS.md)
