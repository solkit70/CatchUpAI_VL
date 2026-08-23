#!/usr/bin/env python3
"""Qwen3-TTS 어댑터 — RemotionStudio 의 검증된 호출 형태를 그대로 옮겼다.

기존 자산: AI/RemotionStudio/public/*/gen_audio_qwen.py
  · 국제 엔드포인트를 반드시 지정해야 한다 (기본값은 중국 리전)
  · 응답이 오디오 바이트가 아니라 **다운로드 URL** 로 온다

URL 반환이라는 점이 방송용으로는 중요한 제약이다. 합성이 끝나야 URL 이 나오고
그때부터 다운로드를 시작하므로, 이 경로로는 첫 오디오 바이트를 일찍 받아 재생을
앞당길 수 없다. first_chunk_ms 가 latency_ms 와 거의 같게 찍히는 것이 그 표현이다.

⚠️ 이것은 **이 경로의 한계이지 Qwen 의 한계가 아니다.** DashScope 는 WebSocket 기반
스트리밍 경로를 따로 제공하고, Flash 티어는 첫 패킷 300ms 수준으로 알려져 있다.
여기서 HTTP 경로를 쓴 것은 RemotionStudio 에서 운영 검증된 형태를 그대로 옮겼기 때문이고,
스트리밍 경로는 아직 검증하지 않았다. 실측표에서 Qwen 의 첫 청크 지연을 읽을 때는
"Qwen 이 느리다"가 아니라 "이 경로가 스트리밍이 아니다"로 읽어야 한다. → 별도 과제.
"""
from __future__ import annotations

import os
import urllib.request
from typing import Iterator

from .base import TTSProvider, TTSUnavailable

INTL_ENDPOINT = "https://dashscope-intl.aliyuncs.com/api/v1"


class QwenTTSProvider(TTSProvider):
    name = "qwen"
    audio_ext = "wav"

    def __init__(self, model, voice, cost_per_1k_chars=None, replacements=None,
                 language_type: str = "Korean"):
        super().__init__(model, voice, cost_per_1k_chars, replacements)
        if not os.environ.get("DASHSCOPE_API_KEY"):
            raise TTSUnavailable("DASHSCOPE_API_KEY 없음")
        try:
            import dashscope
        except ImportError as e:
            raise TTSUnavailable(f"dashscope 패키지 없음: {e}")
        dashscope.base_http_api_url = INTL_ENDPOINT
        self._dashscope = dashscope
        self.language_type = language_type

    @property
    def supports_streaming(self) -> bool:
        return False

    def _synth_bytes(self, text: str) -> Iterator[bytes]:
        resp = self._dashscope.MultiModalConversation.call(
            model=self.model,
            api_key=os.environ["DASHSCOPE_API_KEY"],
            text=text,
            voice=self.voice,
            language_type=self.language_type,
            stream=False,
        )
        if resp.status_code != 200:
            raise RuntimeError(f"Qwen3-TTS {resp.status_code}: {resp.message}")

        url = resp.output.audio.url
        with urllib.request.urlopen(url, timeout=60) as r:
            yield r.read()
