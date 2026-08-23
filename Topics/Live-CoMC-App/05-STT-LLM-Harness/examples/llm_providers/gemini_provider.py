#!/usr/bin/env python3
"""Gemini 어댑터 — response_schema(OpenAPI 서브셋)로 구조화 출력을 유도한다.

주의:
  - Gemini 스키마는 OpenAPI 3.0 서브셋이라 additionalProperties 를 **무시**한다.
    보내도 되지만 400을 내는 경우가 있어 제거하고 보낸다.
    "추가 필드 금지"는 어댑터 뒤단 재검증이 잡는다 — 이중 검증 구조의 이유가 여기 있다.
  - 결과는 parts[0].text 에 JSON **문자열**로 온다.
  - finishReason 이 SAFETY/RECITATION 이면 본문이 비어 있다 → 먼저 확인한다.
"""
from __future__ import annotations

import json
import os

from google import genai
from google.genai import types

from .base import LLMProvider, native_effort, provider_schema

# Gemini 가 무시하거나 거부하는 키워드
DROP = ("additionalProperties", "$schema", "$id")


class GeminiProvider(LLMProvider):
    name = "gemini"

    def __init__(self, model: str, cost_per_1k_tokens=None, effort: str | None = None):
        super().__init__(model, cost_per_1k_tokens, effort=effort)
        self.client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

    def _schema_for_provider(self) -> dict:
        return provider_schema(drop=DROP)

    def _call(self, system: str, user: str, schema: dict):
        cfg = dict(system_instruction=system,
                   response_mime_type="application/json",
                   response_schema=schema)
        eff = native_effort(self.name, self.effort)
        if eff:
            cfg["thinking_config"] = types.ThinkingConfig(thinking_level=eff)

        resp = self.client.models.generate_content(
            model=self.model,
            contents=user,
            config=types.GenerateContentConfig(**cfg),
        )

        cands = getattr(resp, "candidates", None) or []
        if not cands:
            fb = getattr(resp, "prompt_feedback", None)
            raise RuntimeError(f"gemini 응답에 candidate 없음 (prompt_feedback={fb})")
        fr = str(getattr(cands[0], "finish_reason", "")).upper()
        if "SAFETY" in fr or "RECITATION" in fr:
            raise RuntimeError(f"gemini finish_reason={fr}")

        text = (resp.text or "").strip()
        if not text:
            raise RuntimeError(f"gemini 본문 비어 있음 (finish_reason={fr})")
        try:
            payload = json.loads(text)
        except json.JSONDecodeError as e:
            raise RuntimeError(f"JSON 파싱 실패: {e} / 앞부분={text[:120]!r}")

        um = getattr(resp, "usage_metadata", None)
        # Gemini 는 사고 토큰을 thoughts_token_count 로 따로 보고한다.
        # candidates_token_count 에 포함되지 않으므로 지연을 설명하려면 함께 봐야 한다.
        usage = {"input_tokens": getattr(um, "prompt_token_count", 0) or 0,
                 "output_tokens": getattr(um, "candidates_token_count", 0) or 0,
                 "reasoning_tokens": getattr(um, "thoughts_token_count", None),
                 "effort_sent": eff}
        return payload, usage
