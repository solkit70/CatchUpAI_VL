# M2 Troubleshooting — Windows Local (Symptom → Cause → Fix)

## 1. flash-attn Installation Fails (Windows)
- **Symptom**: `pip install flash-attn` build error / no wheel / CUDA compile failure
- **Cause**: FlashAttention 2 is **Linux-only**. Not supported on Windows.
- **Fix**: **Do not install flash-attn.** Use `attn_implementation="sdpa"` (PyTorch built-in) when loading the model. Confirm exact flags from the official Windows guide (`andimarafioti/faster-qwen3-tts/WINDOWS_SETUP_GUIDE.md`) or the official repo `--no-flash-attn` flag.

## 2. `torch.cuda.is_available()` Returns False (Even with GPU)
- **Symptom**: GPU is installed but returns False
- **Cause**: CPU-build torch was installed / CUDA build mismatch
- **Fix**: Reinstall with the GPU wheel — `pip install torch torchvision --index-url https://download.pytorch.org/whl/cu128` (use the index matching your driver/CUDA version)

## 3. Too Slow on CPU
- **Symptom**: 30-second audio takes 90+ seconds
- **Cause**: 1.7B model + complex voice prompt + CPU
- **Fix**: Use the lightweight `0.6B` model, simplify the prompt. 40–90 sec for 30-sec audio is normal range on CPU. Run large batches overnight or as scheduled jobs.

## 4. Model Download Slow / Interrupted
- **Symptom**: HuggingFace download is very slow or keeps interrupting
- **Cause**: Network / mainland mirror needed
- **Fix**: Retry, or use ModelScope mirror `modelscope download --model Qwen/<model>`. Ensure sufficient disk space (several GB) at the cache path.

## 5. bfloat16 Error (CPU)
- **Symptom**: bfloat16 operation error on CPU
- **Cause**: Some CPU paths do not efficiently support bf16
- **Fix**: Use `dtype=torch.float32` for the CPU path.

> Add new issues in the same format (symptom → cause → fix).
