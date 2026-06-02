# Qwen3-TTS Official Primary Sources

> Collected 2026-05-16 · Only primary sources directly verified via WebSearch + WebFetch (no speculation)

## Official Sources
- **GitHub (code, README, examples)**: https://github.com/QwenLM/Qwen3-TTS — Primary source for installation (`pip install -U qwen-tts`), inference examples, model variants, and license
- **Official Blog (announcement)**: https://qwen.ai/blog?id=qwen3tts-0115 — Qwen3-TTS family open-source announcement (voice design, cloning, multilingual)
- **HuggingFace Models**: `Qwen/Qwen3-TTS-*` — Weight downloads and model cards
- **ModelScope**: `modelscope download --model Qwen/[model_name]` — China mainland mirror

## Verified Key Facts
- **Released**: January 2026, Alibaba Cloud Qwen team
- **License**: Apache-2.0 (research + commercial use permitted)
- **Supported Languages (10)**: Chinese, English, Japanese, **Korean**, German, French, Russian, Portuguese, Spanish, Italian (+ dialects such as Beijing and Sichuan)
- **Voice Clone**: 3-second sample + **reference text (`ref_text`) required**. Input accepts local path / URL / base64 / `(numpy_array, sample_rate)`
- **Streaming**: Supported, minimum end-to-end synthesis latency ~97ms
- **Distribution**: HuggingFace + ModelScope

## Model Variants (5 total, all share `Qwen3-TTS-Tokenizer-12Hz` codec)
| Model ID (HuggingFace) | Purpose |
|---|---|
| `Qwen/Qwen3-TTS-12Hz-1.7B-VoiceDesign` | Design voice style via natural-language description |
| `Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice` | 9 preset voices + instruct control |
| `Qwen/Qwen3-TTS-12Hz-1.7B-Base` | 3-second sample voice clone |
| `Qwen/Qwen3-TTS-12Hz-0.6B-CustomVoice` | Lightweight preset voice |
| `Qwen/Qwen3-TTS-12Hz-0.6B-Base` | Lightweight clone |
| `Qwen/Qwen3-TTS-Tokenizer-12Hz` | Shared codec (tokenizer) |

## Unconfirmed / Needs Verification in M2
- **No official Windows support statement**: Examples are based on `device_map="cuda:0"`, `torch.bfloat16`, FlashAttention2 (GPU). Whether it works on Windows + NVIDIA GPU, and whether it works without flash-attn → verified in M2 Practice 1.
