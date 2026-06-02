# M2 (API) Troubleshooting (Symptom → Cause → Fix)

## 1. 401 / Authentication Failure
- **Symptom**: `invalid api key` / 401
- **Cause**: Using a China key against the Intl endpoint, or key not set
- **Fix**: Confirm the key is an **Intl key**; confirm `base_url` is `dashscope-intl...api/v1`; confirm `$env:DASHSCOPE_API_KEY` is recognized (open a new terminal)

## 2. Cannot Issue Intl Key (Residence / Billing)
- **Symptom**: Unable to get an international account / payment method not accepted
- **Cause**: Regional or billing restrictions
- **Fix**: **Fallback → Replicate** `replicate.com/qwen/qwen3-tts` (simple token issuance). Design the Skill backend to accept a `replicate` argument.

## 3. Model Name Error (model not found)
- **Symptom**: 404 / model not found for the specified model name
- **Cause**: Using a guessed model name (date-versioned names change)
- **Fix**: Re-confirm the currently valid `qwen3-tts-*` model name from the official Model Studio documentation and update `model_name.txt`

## 4. Korean Pronunciation / Quality Issues
- **Symptom**: Unnatural Korean or mispronunciation
- **Cause**: Missing `language` parameter, or wrong voice/model
- **Fix**: Use language specification and recommended voices from official docs; test the Voice Design model as an alternative (explored further in M3)

## 5. Billing / Quota
- **Symptom**: Free quota exhausted / unexpected charges
- **Cause**: Accumulated test calls (synthesis ≈ $0.013/1k chars, clone $0.01/enrollment)
- **Fix**: Use short sentences for testing; log call count and character count; monitor 90-day free quota balance

## 6. OpenAI-Compatible Mode 404 (TTS Not Supported)
- **Symptom**: `openai.NotFoundError: Error code: 404` when calling `/compatible-mode/v1/audio/speech`
- **Cause**: DashScope's OpenAI-compatible endpoint (`/compatible-mode/v1`) is **LLM (chat) only** — it does not support the TTS API
- **Fix**: Install `dashscope` and use `dashscope.MultiModalConversation.call()`. Use endpoint `https://dashscope-intl.aliyuncs.com/api/v1`

> Add new issues in the same format (symptom → cause → fix).
