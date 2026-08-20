"""M5 실습 3 — LLM 프로바이더 어댑터 계층.

build(name, ...) 로 어댑터를 만들고, router.call_with_fallback() 로 호출한다.
바깥에서는 프로바이더 이름 말고는 3사 차이를 알 필요가 없다.
"""
from .base import (ANSWER_DRAFT_SCHEMA, LLMProvider, LLMResult, SchemaViolation,
                   normalize, provider_schema, validate)

__all__ = ["LLMProvider", "LLMResult", "SchemaViolation", "ANSWER_DRAFT_SCHEMA",
           "normalize", "validate", "provider_schema", "build"]


def build(name: str, model: str, cost_per_1k_tokens=None) -> LLMProvider:
    """이름으로 어댑터를 만든다. SDK import 는 실제로 쓸 때만 일어나게 지연시킨다."""
    if name == "claude":
        from .claude_provider import ClaudeProvider
        return ClaudeProvider(model, cost_per_1k_tokens)
    if name == "openai":
        from .openai_provider import OpenAIProvider
        return OpenAIProvider(model, cost_per_1k_tokens)
    if name == "gemini":
        from .gemini_provider import GeminiProvider
        return GeminiProvider(model, cost_per_1k_tokens)
    raise ValueError(f"알 수 없는 프로바이더: {name}")
