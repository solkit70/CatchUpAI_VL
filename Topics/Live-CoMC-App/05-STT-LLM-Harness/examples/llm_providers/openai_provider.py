#!/usr/bin/env python3
"""OpenAI 어댑터 — response_format=json_schema(strict) 로 구조화 출력을 강제한다.

주의:
  - strict 모드는 additionalProperties:false 와 **전 필드 required** 를 요구한다.
    그래서 provider_schema(force_all_required=True) 로 만들어 보낸다.
    이 때문에 어댑터 주입 필드(provider/created_at)를 스키마에서 미리 빼는 것이
    선택이 아니라 필수다 — 남겨 두면 모델이 채울 수 없는 값을 required 로 요구받는다.
  - 결과는 message.content 에 JSON **문자열**로 온다 → 직접 파싱한다.
"""
from __future__ import annotations

import json

from openai import OpenAI

from .base import LLMProvider, native_effort, provider_schema


class OpenAIProvider(LLMProvider):
    name = "openai"

    def __init__(self, model: str, cost_per_1k_tokens=None, effort: str | None = None):
        super().__init__(model, cost_per_1k_tokens, effort=effort)
        self.client = OpenAI()                    # OPENAI_API_KEY

    def _schema_for_provider(self) -> dict:
        return provider_schema(force_all_required=True)

    def _call(self, system: str, user: str, schema: dict):
        extra = {}
        eff = native_effort(self.name, self.effort)
        if eff:
            extra["reasoning_effort"] = eff

        resp = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "system", "content": system},
                      {"role": "user", "content": user}],
            response_format={
                "type": "json_schema",
                "json_schema": {"name": "answer_draft", "strict": True, "schema": schema},
            },
            **extra,
        )
        choice = resp.choices[0]

        # content_filter 등으로 잘리면 content 가 비거나 부분 JSON 이 온다
        if choice.finish_reason not in ("stop", None):
            raise RuntimeError(f"openai finish_reason={choice.finish_reason}")

        text = choice.message.content or ""
        try:
            payload = json.loads(text)
        except json.JSONDecodeError as e:
            raise RuntimeError(f"JSON 파싱 실패: {e} / 앞부분={text[:120]!r}")

        u = resp.usage
        # OpenAI 는 추론 토큰을 따로 보고한다 → 지연 원인을 직접 볼 수 있는 곳이다.
        details = getattr(u, "completion_tokens_details", None)
        usage = {"input_tokens": getattr(u, "prompt_tokens", 0),
                 "output_tokens": getattr(u, "completion_tokens", 0),
                 "reasoning_tokens": getattr(details, "reasoning_tokens", None),
                 "effort_sent": eff}
        return payload, usage
