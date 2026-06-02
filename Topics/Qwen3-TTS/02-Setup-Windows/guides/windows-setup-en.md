# Qwen3-TTS Windows Local Installation Guide (M2)

> Environment: Windows 11 · PowerShell · conda
> Based on verified key facts (M1/M2 web research). **Branch to GPU path or CPU path based on Step 0 GPU detection result.**
> Each step has a "completion signal." When that signal appears, the step succeeded — do not guess.

## ⚠️ Key Windows Issue (Understand This First)
- The official `qwen-tts` package uses **FlashAttention 2** in its examples, but **flash-attn is Linux-only** and is difficult to install on Windows.
- **Workaround**: Use PyTorch's built-in **SDPA** (Scaled Dot-Product Attention) → specify `attn_implementation="sdpa"` when loading the model. **Skip flash-attn installation entirely.**
- References: official repo (`--no-flash-attn` flag), community Windows guide at `github.com/andimarafioti/faster-qwen3-tts/blob/main/WINDOWS_SETUP_GUIDE.md`, SDPA fork `Qwen3-TTS-JP`.
- Performance: NVIDIA GPU recommended. CPU works; 30-sec voice takes ~40–90 sec (1.5–2.5× real-time depending on model and options). **Use the lightweight `0.6B` model on CPU.**

## Step 0 — Detect GPU/CUDA (Branch Decision, 1 min)
In PowerShell:
```powershell
nvidia-smi
```
- **NVIDIA GPU info is printed** → take **GPU path** (Step 1-A)
- `'nvidia-smi' is not recognized` or no GPU → take **CPU path** (Step 1-B), use `0.6B` model

> Completion signal: Confirm which branch (GPU or CPU) and follow only that branch below.

## Step 1 — Create conda Environment (Both Paths)
```powershell
conda create -n qwen3-tts python=3.12 -y
conda activate qwen3-tts
```
> Completion signal: Prompt changes to `(qwen3-tts)`.

## Step 2 — Install PyTorch (Branch)

### 1-A. GPU Path (NVIDIA + CUDA)
```powershell
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu128
```

### 1-B. CPU Path
```powershell
pip install torch torchvision
```
> Completion signal:
> ```powershell
> python -c "import torch; print(torch.__version__, torch.cuda.is_available())"
> ```
> GPU path outputs `... True`, CPU path outputs `... False`.

## Step 3 — Install Qwen3-TTS (Both Paths, without flash-attn)
```powershell
pip install -U qwen-tts
```
- **Do NOT install flash-attn** (incompatible with Windows). Use SDPA instead.
> Completion signal:
> ```powershell
> python -c "import qwen_tts; print('qwen_tts OK')"
> ```
> Output: `qwen_tts OK`.

## Step 4 — Download Model Weights & First Speech (Hello World)
- Model selection: GPU = `Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice`, CPU = `Qwen/Qwen3-TTS-12Hz-0.6B-CustomVoice`
- Auto-downloaded from HuggingFace (several GB). First run takes a while.
- Apply **SDPA** option (no flash-attn) when running. Confirm exact arguments from the official Windows guide linked in the warning above — general form:

```python
# examples/hello.py (conceptual skeleton — confirm device/attn options from official Windows guide)
import torch, time
from qwen_tts import Qwen3TTSModel

MODEL = "Qwen/Qwen3-TTS-12Hz-0.6B-CustomVoice"   # Replace with 1.7B for GPU
DEVICE = "cuda:0" if torch.cuda.is_available() else "cpu"
DTYPE  = torch.bfloat16 if torch.cuda.is_available() else torch.float32

model = Qwen3TTSModel.from_pretrained(
    MODEL, device_map=DEVICE, dtype=DTYPE,
    attn_implementation="sdpa",   # Replaces flash-attn (Windows)
)

for lang, txt, out in [
    ("Korean",  "안녕하세요. 큐원 삼 티티에스 윈도우 첫 음성 테스트입니다.", "examples/hello_ko.wav"),
    ("English", "Hello. This is the first Qwen3-TTS test on Windows.",      "examples/hello_en.wav"),
]:
    t = time.time()
    wavs, sr = model.generate_custom_voice(text=txt, language=lang, speaker="Vivian")
    # Save wavs (use library save utility or soundfile)
    print(lang, "elapsed", round(time.time()-t, 1), "s")
```
> Completion signal: `examples/hello_ko.wav` and `examples/hello_en.wav` both created and play correctly. Record synthesis time (seconds) in WorkLog.

## Step 5 — Confirm Reproducibility
- Record the full procedure + Step 0 branch result + actual synthesis time in WorkLog.
- Log any errors in `../troubleshooting/known-issues-en.md` using the symptom → cause → fix format.

---

### Verification Checklist (DoD)
- [ ] Step 0 GPU/CPU branch confirmed
- [ ] `(qwen3-tts)` environment + `torch.cuda.is_available()` result recorded
- [ ] `qwen_tts OK`
- [ ] `hello_ko.wav` / `hello_en.wav` created and playback verified
- [ ] Synthesis time recorded (for CPU: verify ratio vs. 30-sec audio)
- [ ] At least one troubleshooting entry recorded
