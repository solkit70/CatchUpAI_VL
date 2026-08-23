"""M6 실습 1 — TTS 프로바이더 어댑터 계층.

build(name, cfg) 로 어댑터를 만든다. 바깥에서는 프로바이더 이름 말고 4종 차이를 모른다.
SDK import 는 실제로 쓸 때만 일어나게 지연시킨다 (설치되지 않은 프로바이더가
다른 프로바이더의 동작을 막지 않게 하려는 것 — M5 어댑터와 같은 이유).
"""
from .base import TTSProvider, TTSResult, TTSUnavailable, audio_duration

__all__ = ["TTSProvider", "TTSResult", "TTSUnavailable", "audio_duration",
           "build", "PROVIDERS"]

PROVIDERS = ("edge", "openai", "qwen", "elevenlabs")


def build(name: str, cfg: dict) -> TTSProvider:
    """레지스트리 항목 하나로 어댑터를 만든다.

    쓸 수 없는 프로바이더는 생성 시점에 TTSUnavailable 을 올린다 —
    호출 실패와 구분해야 프리플라이트가 "없음"과 "고장"을 갈라 볼 수 있다.
    """
    kw = dict(model=cfg["model"], voice=cfg["voice"],
              cost_per_1k_chars=cfg.get("cost_per_1k_chars"),
              replacements=cfg.get("replacements"))

    if name == "edge":
        from .edge_provider import EdgeTTSProvider
        return EdgeTTSProvider(**kw)
    if name == "openai":
        from .openai_provider import OpenAITTSProvider
        return OpenAITTSProvider(**kw)
    if name == "qwen":
        from .qwen_provider import QwenTTSProvider
        return QwenTTSProvider(language_type=cfg.get("language_type", "Korean"), **kw)
    if name == "elevenlabs":
        from .elevenlabs_provider import ElevenLabsTTSProvider
        return ElevenLabsTTSProvider(**kw)
    raise ValueError(f"알 수 없는 TTS 프로바이더: {name}")
