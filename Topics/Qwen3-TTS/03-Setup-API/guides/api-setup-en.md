# Qwen3-TTS API Setup Guide (M2)

> Runtime: Alibaba Cloud Model Studio / DashScope **Intl (Singapore)**, OpenAI-compatible mode
> Each step has a "completion signal." When that signal appears, the step succeeded.
> Confirm the exact latest model name from the **official Model Studio documentation** in Step 3 (web search is supplementary only).

## Step 1 — Account & Intl API Key (45 min)
1. Sign up at https://www.alibabacloud.com → Activate **Model Studio (International)**
2. DashScope Console → **API-KEY Management** → Create Key
3. ⚠️ **Must be an Intl (International) key.** China keys are incompatible with the Intl endpoint.
> Completion signal: An active API key is visible in the console. (If issuance fails → see Replicate fallback in troubleshooting)

## Step 2 — Set Key as Environment Variable
PowerShell:
```powershell
setx DASHSCOPE_API_KEY "your_key_here"
```
- Open a new terminal for the variable to take effect.
> Completion signal:
> ```powershell
> $env:DASHSCOPE_API_KEY
> ```
> The key string is printed. (Do NOT store the key in plain text in code or notes.)

## Step 3 — Install SDK & Confirm Model Name
```powershell
pip install -U dashscope   # Native DashScope SDK (recommended for TTS)
# Alternative: pip install -U openai  (OpenAI-compatible mode — LLM only, NOT for TTS)
```
- Look up the **Qwen3-TTS model name** in the official Model Studio documentation and record it:
  - Voice Clone: `qwen3-tts-vc-*` (e.g., `qwen3-tts-vc-2026-01-22`)
  - Voice Design: `qwen3-tts-vd-*`
  - Real-time: `qwen3-tts-vc-realtime-*`
> Completion signal: The exact model name you will use is recorded in `examples/model_name.txt`.

## Step 4 — First Korean Synthesis (DashScope Native SDK)
`examples/hello_qwen.py` (conceptual skeleton — use model name confirmed in Step 3):
```python
import os, time
import dashscope

dashscope.base_http_api_url = "https://dashscope-intl.aliyuncs.com/api/v1"
dashscope.api_key = os.environ["DASHSCOPE_API_KEY"]

for txt, out in [
    ("안녕하세요. 큐원 삼 티티에스 에이피아이 첫 한국어 합성 테스트입니다.", "examples/hello_ko.wav"),
    ("Hello. First Qwen3-TTS API test in English.",                      "examples/hello_en.wav"),
]:
    t = time.time()
    response = dashscope.MultiModalConversation.call(
        model="<model name confirmed in Step 3>",
        text=txt,
        voice="<default voice from official docs>",
        stream=False,
    )
    # Download from response.output.audio.url and save
    print(out, "elapsed", round(time.time()-t, 1), "s")
```
> Completion signal: `examples/hello_ko.wav` and `hello_en.wav` created and play correctly. Record call latency (seconds) in WorkLog.

## Step 5 — Confirm Reproducibility
- Record Steps 1–4, actual latency (seconds), and confirmed model name in WorkLog.
- Log any errors in `../troubleshooting/known-issues-en.md` using the symptom → cause → fix format.

### Verification Checklist (DoD)
- [ ] Intl key issued + env var recognized
- [ ] SDK installed + exact model name recorded
- [ ] `hello_ko.wav` / `hello_en.wav` created and verified
- [ ] Call latency recorded
- [ ] At least one troubleshooting entry
