#!/usr/bin/env python3
"""OpenAI TTS 어댑터 — 진짜 스트리밍 경로를 쓴다.

with_streaming_response 를 쓰지 않으면 SDK 가 응답을 다 받은 뒤에야 바이트를 돌려주므로
first_chunk_ms 가 latency_ms 와 같아진다. 그러면 "일찍 재생 시작"이라는 이 어댑터의
유일한 장점이 측정에서 사라진다.
"""
from __future__ import annotations

import os
from typing import Iterator

from .base import TTSProvider, TTSUnavailable


class OpenAITTSProvider(TTSProvider):
    name = "openai"
    audio_ext = "mp3"

    def __init__(self, model, voice, cost_per_1k_chars=None, replacements=None):
        super().__init__(model, voice, cost_per_1k_chars, replacements)
        if not os.environ.get("OPENAI_API_KEY"):
            raise TTSUnavailable("OPENAI_API_KEY 없음")
        try:
            from openai import OpenAI
        except ImportError as e:
            raise TTSUnavailable(f"openai 패키지 없음: {e}")
        self.client = OpenAI()

    @property
    def supports_streaming(self) -> bool:
        return True

    def _synth_bytes(self, text: str) -> Iterator[bytes]:
        with self.client.audio.speech.with_streaming_response.create(
            model=self.model,
            voice=self.voice,
            input=text,
            response_format="mp3",
        ) as resp:
            for chunk in resp.iter_bytes(4096):
                yield chunk
