#!/usr/bin/env python3
"""ElevenLabs 어댑터 — ⚠️ 미검증.

2026-08-23 현재 이 환경에 ELEVENLABS_API_KEY 가 없고 elevenlabs 패키지도 설치돼 있지 않다.
그래서 이 어댑터는 **작성만 하고 실제 호출로 검증하지 못했다.** 프리플라이트가
TTSUnavailable 로 걸러내므로 실측표와 서킷 브레이커 후보에서 자동으로 빠진다.

M5 문제 1의 교훈을 여기에 그대로 적용한다 — 검증하지 않은 것을 검증했다고 적지 않는다.
키가 생기면 `python tts_probe.py` 한 번으로 이 어댑터가 실제로 도는지 판정된다.
그때까지 아래 요청 형태는 **가설**이다.

패키지 의존 없이 REST 로 직접 호출한다. elevenlabs SDK 를 새로 깔지 않아도
키만 생기면 바로 시험할 수 있게 하기 위해서다.
"""
from __future__ import annotations

import json
import os
import urllib.request
from typing import Iterator

from .base import TTSProvider, TTSUnavailable

API_BASE = "https://api.elevenlabs.io/v1/text-to-speech"


class ElevenLabsTTSProvider(TTSProvider):
    name = "elevenlabs"
    audio_ext = "mp3"

    def __init__(self, model, voice, cost_per_1k_chars=None, replacements=None):
        super().__init__(model, voice, cost_per_1k_chars, replacements)
        self.api_key = (os.environ.get("ELEVENLABS_API_KEY")
                        or os.environ.get("ELEVEN_API_KEY"))
        if not self.api_key:
            raise TTSUnavailable("ELEVENLABS_API_KEY 없음 (어댑터는 작성됨, 미검증)")

    @property
    def supports_streaming(self) -> bool:
        return True

    def _synth_bytes(self, text: str) -> Iterator[bytes]:
        # voice 는 사람이 읽는 이름이 아니라 voice_id 다 (레지스트리에 id 를 적는다)
        req = urllib.request.Request(
            f"{API_BASE}/{self.voice}/stream",
            data=json.dumps({"text": text, "model_id": self.model}).encode("utf-8"),
            headers={"xi-api-key": self.api_key,
                     "Content-Type": "application/json",
                     "Accept": "audio/mpeg"},
            method="POST")
        with urllib.request.urlopen(req, timeout=120) as r:
            while True:
                chunk = r.read(4096)
                if not chunk:
                    break
                yield chunk
