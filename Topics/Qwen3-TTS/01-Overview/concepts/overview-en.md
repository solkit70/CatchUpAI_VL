# Qwen3-TTS Overview & Architecture Summary (M1)

## One-Line Definition
Qwen3-TTS is an open-source TTS family released under Apache-2.0 by Alibaba's Qwen team in January 2026, offering **3-second voice cloning, natural-language voice design, streaming synthesis, and support for 10 languages including Korean**.

## Why This Topic (Motivation)
The current video production pipeline relies on OpenAI TTS and Microsoft edge-tts. Qwen3-TTS offers significant value for video narration and live guidance because it is (1) open-source and commercially usable, (2) capable of building a consistent character voice from a short sample, and (3) able to design voice tone through natural language.

## 4 Core Features
1. **Voice Clone (Base model)** — Replicates speaker timbre using a 3-second reference audio + reference text. Input accepts file path / URL / base64 / numpy array.
2. **Natural-Language Voice Design (VoiceDesign model)** — Creates a voice from a text instruction (`instruct`) such as "a calm middle-aged male."
3. **Preset + Instruct Control (CustomVoice model)** — Modifies 9 preset voices using emotion and tone instructions.
4. **Streaming / Non-Streaming** — First packet output on single-character input; minimum latency ~97ms (potential for real-time guidance).

## Model Selection Guide (for this topic)
- **Consistent character voice / video narration** → `1.7B-Base` (clone) or `1.7B-VoiceDesign` (design)
- **Quick preset voice** → `1.7B-CustomVoice`
- **Lightweight / low-resource testing** → `0.6B-*`
- This topic's Capstone (Remotion integration) is **batch synthesis** focused → Streaming is an extension point for future live guidance work

## Architecture Notes
- All variants share a common **`Qwen3-TTS-Tokenizer-12Hz`** audio codec, with 1.7B / 0.6B LM backbones and task-specific heads (Base / CustomVoice / VoiceDesign).
- Example inference: PyTorch, `device_map="cuda:0"`, `dtype=torch.bfloat16`, optional FlashAttention2.

## Relationship to Existing Pipeline
- Current `gen_audio.py` (edge-tts) and OpenAI TTS are **simple with preset voices but cannot clone a custom speaker**.
- Qwen3-TTS excels at **cloning and voice design** but has the cost of **local installation and GPU dependency**. → Quality A/B in M3; adoption criteria documented in M5.

## Risks (to be verified in M2)
- Windows support not officially stated (examples assume CUDA / bfloat16 / flash-attn). NVIDIA GPU may be required; flash-attn installation is complex.
