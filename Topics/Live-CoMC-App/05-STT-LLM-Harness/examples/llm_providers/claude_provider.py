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

from .base import LLMProvider, native_effort, provider_schema

TOOL_NAME = "emit_answer_draft"

# Claude 네이티브 structured outputs 가 받지 않는 키워드 (M3 조사 결과)
DROP = ("minimum", "maximum", "minLength", "maxLength", "minItems", "maxItems")


class ClaudeProvider(LLMProvider):
    name = "claude"

    def __init__(self, model: str, cost_per_1k_tokens=None, max_tokens: int = 4096,
                 effort: str | None = None):
        super().__init__(model, cost_per_1k_tokens, effort=effort)
        self.max_tokens = max_tokens
        self.client = anthropic.Anthropic()      # ANTHROPIC_API_KEY 를 알아서 읽는다

    def _schema_for_provider(self) -> dict:
        return provider_schema(drop=DROP)

    def _call(self, system: str, user: str, schema: dict):
        # Opus 5 는 thinking 이 기본 ON(adaptive)이다. 지연 제어는 effort 로 한다.
        # thinking={"type": "disabled"} 는 쓰지 않는다 — strict tool use 와 함께 쓰면
        # 도구 호출이 tool_use 블록 대신 본문 텍스트로 새는 실패 모드가 있다.
        # output_config 는 설치된 anthropic 0.75.0 이 아직 모르는 파라미터라
        # 명시 인자로 넣으면 TypeError 가 난다. extra_body 로 요청 본문에
        # 그대로 실어 보낸다 — 서버가 받는 JSON 은 동일하다.
        # SDK 1.x 로 올리면 output_config=... 로 바꿀 수 있다(백로그).
        extra = {}
        eff = native_effort(self.name, self.effort)
        if eff:
            extra["extra_body"] = {"output_config": {"effort": eff}}

        resp = self.client.messages.create(
            model=self.model,
            max_tokens=self.max_tokens,
            system=system,
            **extra,
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

        # Anthropic 은 thinking 토큰을 따로 보고하지 않는다 — output_tokens 에 포함된다.
        # 추론 비중은 effort 를 낮췄을 때 output_tokens 가 얼마나 줄어드는지로 읽는다.
        usage = {"input_tokens": resp.usage.input_tokens,
                 "output_tokens": resp.usage.output_tokens,
                 "reasoning_tokens": None,
                 "effort_sent": eff}
        # tool_use.input 은 이미 파싱된 객체다 (JSON 문자열 아님)
        return dict(block.input), usage
