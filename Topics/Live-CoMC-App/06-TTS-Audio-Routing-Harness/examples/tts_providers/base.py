#!/usr/bin/env python3
"""M6 실습 1 — TTSProvider 공통 인터페이스.

M5의 LLMProvider와 같은 구조다. 바깥(⑧ 오디오 라우팅)은 프로바이더를 몰라야 하고,
런타임에 갈아 끼울 수 있어야 한다. 비용 상한을 넘으면 무료 프로바이더로 강등하는
서킷 브레이커(실습 4)가 성립하려면 이 계층이 먼저 있어야 한다.

M5에서 얻은 규율을 그대로 가져온다.
  · 모델·보이스 ID는 voice_registry.json 에서 주입한다. 코드에 박지 않는다
  · 프리플라이트는 키 존재 확인이 아니라 **실제 합성 1회**로 한다
    (M5 문제 1: models.list() 에 있다고 호출 가능한 게 아니다)
  · 확인되지 않은 단가는 추측하지 않고 None 으로 둔다

두 가지 지연을 구분해서 잰다.
  first_chunk_ms — 첫 오디오 바이트가 도착한 시각. 재생을 시작할 수 있는 시점이다
  latency_ms     — 합성이 끝난 시각

LLM 단계에서는 첫 토큰 지연이 무의미했다. ⑦ 안전 검증 게이트가 JSON 전체를 받아
검증해야 발화가 허용되므로 부분 응답으로 할 수 있는 일이 없었다.
TTS는 반대다. 이 단계에 들어온 텍스트는 이미 게이트를 통과했으므로,
첫 청크가 도착하는 순간 스피커로 내보낼 수 있다. 그래서 여기서는 첫 청크가 실질 지표다.

⚠️ 이 계층은 오디오를 **재생하지 않는다**. 파일로만 쓴다.
   라이브 방송 중 검증을 돌리면 스피커 출력이 방송에 섞이고,
   M4에서 만든 에코 게이트 측정 조건까지 오염된다. 재생은 ⑧ 라우팅의 몫이다.
"""
from __future__ import annotations

import json
import shutil
import subprocess
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterator

FFPROBE = shutil.which("ffprobe")


class TTSUnavailable(Exception):
    """이 프로바이더는 지금 쓸 수 없다 (키 없음 / 패키지 없음 / 권한 없음).

    호출 실패와 구분한다. 프리플라이트는 이 예외를 잡아 레지스트리에서 제외하고,
    서킷 브레이커는 강등 대상 후보에서 뺀다.
    """


@dataclass
class TTSResult:
    """어댑터 출력. 실측표(실습 2)의 한 행이 된다."""
    provider: str
    model: str
    voice: str
    path: Path
    chars: int
    latency_ms: int
    first_chunk_ms: int | None = None      # 스트리밍 불가면 None
    streamed: bool = False
    bytes: int = 0
    duration_s: float | None = None
    est_cost_usd: float | None = None
    meta: dict = field(default_factory=dict)

    @property
    def rtf(self) -> float | None:
        """실시간 계수 = 합성 시간 / 오디오 길이.

        1.0 미만이면 말하는 속도보다 빨리 만든다는 뜻이고, 그래야 실시간 발화가 가능하다.
        """
        if not self.duration_s:
            return None
        return round(self.latency_ms / 1000 / self.duration_s, 3)


def audio_duration(path: Path) -> float | None:
    """ffprobe 로 오디오 길이를 잰다. 없으면 None (추측하지 않는다)."""
    if not FFPROBE or not path.exists():
        return None
    try:
        out = subprocess.run(
            [FFPROBE, "-v", "error", "-show_entries", "format=duration",
             "-of", "json", str(path)],
            capture_output=True, text=True, timeout=30)
        if out.returncode != 0:
            return None
        return round(float(json.loads(out.stdout)["format"]["duration"]), 3)
    except Exception:
        return None


class TTSProvider(ABC):
    """4종 공통 인터페이스.

    구현체는 요청 빌드와 바이트 수신만 책임진다. 길이 측정·비용 계산·결과 조립은
    여기서 한 번만 한다.
    """

    name: str = "base"
    audio_ext: str = "mp3"

    def __init__(self, model: str, voice: str,
                 cost_per_1k_chars: float | None = None,
                 replacements: dict | None = None):
        self.model = model
        self.voice = voice
        # 확인된 공개 단가만 넣는다. 모르면 None — 추측 단가는 비용 리포트를 조용히 망친다.
        self.cost_per_1k_chars = cost_per_1k_chars
        # 발음 보정 표. RemotionStudio 의 기존 자산에서 검증된 방식이다
        # (예: "GOBI" → "고비"). 프로바이더마다 오독 지점이 달라 레지스트리로 주입한다.
        self.replacements = replacements or {}

    # ── 하위 구현 ─────────────────────────────────────────────────────

    @abstractmethod
    def _synth_bytes(self, text: str) -> Iterator[bytes]:
        """오디오 바이트를 청크로 내놓는다.

        스트리밍이 가능하면 도착하는 대로 yield 하고, 불가능하면 통짜로 한 번 yield 한다.
        첫 yield 시각이 first_chunk_ms 가 되므로, 통짜 프로바이더는 자연히
        first_chunk == latency 가 되어 "재생을 일찍 시작할 수 없다"는 사실이 수치로 드러난다.
        """

    @property
    def supports_streaming(self) -> bool:
        return False

    # ── 공통 ─────────────────────────────────────────────────────────

    def prepare_text(self, text: str) -> str:
        """발음 보정을 적용한다. 합성에 실제로 들어간 문자열이 비용 산정 기준이다."""
        for a, b in self.replacements.items():
            text = text.replace(a, b)
        return text

    def estimate_cost(self, chars: int) -> float | None:
        if self.cost_per_1k_chars is None:
            return None
        return round(chars / 1000 * self.cost_per_1k_chars, 6)

    def synth(self, text: str, out_path: Path) -> TTSResult:
        """텍스트 → 오디오 파일. 재생하지 않는다."""
        import time

        spoken = self.prepare_text(text)
        out_path = Path(out_path).with_suffix("." + self.audio_ext)
        out_path.parent.mkdir(parents=True, exist_ok=True)

        t0 = time.time()
        first = None
        total = 0
        with out_path.open("wb") as f:
            for chunk in self._synth_bytes(spoken):
                if not chunk:
                    continue
                if first is None:
                    first = round((time.time() - t0) * 1000)
                f.write(chunk)
                total += len(chunk)
        latency = round((time.time() - t0) * 1000)

        if total == 0:
            raise RuntimeError(f"{self.name}: 오디오 바이트가 하나도 오지 않았습니다")

        return TTSResult(
            provider=self.name, model=self.model, voice=self.voice,
            path=out_path, chars=len(spoken),
            latency_ms=latency, first_chunk_ms=first,
            streamed=self.supports_streaming,
            bytes=total, duration_s=audio_duration(out_path),
            est_cost_usd=self.estimate_cost(len(spoken)),
        )

    def preflight(self, tmp_dir: Path) -> TTSResult:
        """실제로 합성이 되는지 확인한다.

        키 존재나 패키지 import 만으로는 부족하다 — M5에서 그렇게 만든 프리플라이트가
        3사 모두 '정상'이라고 했지만 두 곳이 실제 호출에서 실패했다.
        짧은 한국어 한 문장을 진짜로 합성해 본다.
        """
        return self.synth("연결 확인용 짧은 문장입니다.",
                          Path(tmp_dir) / f"_preflight_{self.name}")
