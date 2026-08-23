#!/usr/bin/env python3
"""Edge-TTS 어댑터 — 무료. 서킷 브레이커의 강등 목적지다.

edge_tts.Communicate.stream() 은 async generator 라서 동기 인터페이스와 맞지 않는다.
바이트를 다 모은 뒤 한 번에 내놓으면 first_chunk_ms 가 실제보다 늦게 찍혀
"스트리밍이 되는데 안 되는 것처럼" 보인다. 그래서 별도 스레드에서 async 루프를 돌리고
큐로 넘겨 도착 순서와 시각을 보존한다.
"""
from __future__ import annotations

import asyncio
import queue
import threading
from typing import Iterator

from .base import TTSProvider, TTSUnavailable

_SENTINEL = object()


class EdgeTTSProvider(TTSProvider):
    name = "edge"
    audio_ext = "mp3"

    def __init__(self, model, voice, cost_per_1k_chars=None, replacements=None):
        super().__init__(model, voice, cost_per_1k_chars, replacements)
        try:
            import edge_tts  # noqa: F401
        except ImportError as e:
            raise TTSUnavailable(f"edge-tts 패키지 없음: {e}")

    @property
    def supports_streaming(self) -> bool:
        return True

    def _synth_bytes(self, text: str) -> Iterator[bytes]:
        import edge_tts

        q: queue.Queue = queue.Queue()

        async def pump():
            try:
                comm = edge_tts.Communicate(text, self.voice)
                async for chunk in comm.stream():
                    if chunk.get("type") == "audio" and chunk.get("data"):
                        q.put(chunk["data"])
            except Exception as e:                  # 스레드 예외를 본체로 넘긴다
                q.put(e)
            finally:
                q.put(_SENTINEL)

        t = threading.Thread(target=lambda: asyncio.run(pump()), daemon=True)
        t.start()
        while True:
            item = q.get()
            if item is _SENTINEL:
                break
            if isinstance(item, Exception):
                raise item
            yield item
        t.join(timeout=5)
