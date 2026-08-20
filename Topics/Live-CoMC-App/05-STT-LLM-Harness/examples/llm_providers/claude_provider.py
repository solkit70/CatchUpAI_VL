#!/usr/bin/env python3
"""Claude 어댑터 — strict tool use 로 구조화 출력을 강제한다.

M3 비교표의 ① 방식(Tool use + strict + tool_choice)을 쓴다. 도구를 하나만 두고
tool_choice 로 그 도구를 강제하면 모델이 텍스트로 빠져나갈 길이 없다.

주의 (claude-api 스킬 확인 사항):
  - strict 는 tool_choice 가 아니라 **도구 정의의 최상위 필드**다
  - Claude 구조화 출력은 minimum/maxLength 같은 수치·길이 제약을 미지원 →
    base.provider_schema(drop=...) 로 떨궈서 보낸다
  - budget_tokens 는 Opus 5에서 400. thinking 은 생략하면 adaptive 로 동작한다
"""
from __future__ import annotations

import anthropic

from .base import LLMProvider, provider_schema

TOOL_NAME = "emit_answer_draft"

# Claude 네이티브 structured outputs 가 받지 않는 키워드 (M3 조사 결과)
DROP = ("minimum", "maximum", "minLength", "maxLength", "minItems", "maxItems")


class ClaudeProvider(LLMProvider):
    name = "claude"

    def __init__(self, model: str, cost_per_1k_tokens=None, max_tokens: int = 4096):
        super().__init__(model, cost_per_1k_tokens)
        self.max_tokens = max_tokens
        self.client = anthropic.Anthropic()      # ANTHROPIC_API_KEY 를 알아서 읽는다

    def _schema_for_provider(self) -> dict:
        return provider_schema(drop=DROP)

    def _call(self, system: str, user: str, schema: dict):
        resp = self.client.messages.create(
            model=self.model,
            max_tokens=self.max_tokens,
            system=system,
            tools=[{
                "name": TOOL_NAME,
                "description": "검증된 근거만으로 만든 발화 초안을 제출한다.",
                "strict": True,                  # 도구 정의의 최상위 필드
                "input_schema": schema,
            }],
            tool_choice={"type": "tool", "name": TOOL_NAME},
            messages=[{"role": "user", "content": user}],
        )

        # 정책 거부는 예외가 아니라 stop_reason 으로 온다 → 먼저 확인한다
        if resp.stop_reason == "refusal":
            cat = getattr(getattr(resp, "stop_details", None), "category", None)
            raise RuntimeError(f"claude refusal (category={cat})")

        block = next((b for b in resp.content
                      if b.type == "tool_use" and b.name == TOOL_NAME), None)
        if block is None:
            kinds = [b.type for b in resp.content]
            raise RuntimeError(f"tool_use 블록 없음 (stop_reason={resp.stop_reason}, blocks={kinds})")

        usage = {"input_tokens": resp.usage.input_tokens,
                 "output_tokens": resp.usage.output_tokens}
        # tool_use.input 은 이미 파싱된 객체다 (JSON 문자열 아님)
        return dict(block.input), usage
