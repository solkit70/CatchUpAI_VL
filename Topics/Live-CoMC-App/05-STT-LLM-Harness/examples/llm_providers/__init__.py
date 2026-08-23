"""M5 실습 3 — LLM 프로바이더 어댑터 계층.

build(name, ...) 로 어댑터를 만들고, router.call_with_fallback() 로 호출한다.
바깥에서는 프로바이더 이름 말고는 3사 차이를 알 필요가 없다.
"""
from .base import (ANSWER_DRAFT_SCHEMA, EFFORT_LEVELS, EFFORT_MAP, LLMProvider,
                   LLMResult, SchemaViolation, native_effort, normalize,
                   provider_schema, validate)

__all__ = ["LLMProvider", "LLMResult", "SchemaViolation", "ANSWER_DRAFT_SCHEMA",
           "EFFORT_LEVELS", "EFFORT_MAP", "native_effort",
           "normalize", "validate", "provider_schema", "build"]


def build(name: str, model: str, cost_per_1k_tokens=None,
          effort: str | None = None) -> LLMProvider:
    """이름으로 어댑터를 만든다. SDK import 는 실제로 쓸 때만 일어나게 지연시킨다.

    effort 는 공통 척도(minimal/low/medium/high)다. None 이면 각 사 기본값을 쓴다 —
    M5 측정이 그 조건이었으므로 기존 호출의 동작은 바뀌지 않는다.
    """
    if name == "claude":
        from .claude_provider import ClaudeProvider
        return ClaudeProvider(model, cost_per_1k_tokens, effort=effort)
    if name == "openai":
        from .openai_provider import OpenAIProvider
        return OpenAIProvider(model, cost_per_1k_tokens, effort=effort)
    if name == "gemini":
        from .gemini_provider import GeminiProvider
        return GeminiProvider(model, cost_per_1k_tokens, effort=effort)
    raise ValueError(f"알 수 없는 프로바이더: {name}")
