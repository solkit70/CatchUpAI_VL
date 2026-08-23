#!/usr/bin/env python3
"""M5 실습 3 — LLMProvider 공통 인터페이스와 스키마 정규화.

M3 llm-schema-normalization.md 의 설계를 코드로 옮긴 것이다. 핵심 구조는 이중 검증:

  프로바이더 구조화 출력 = "대략 맞게 유도"
  어댑터 뒤단 재검증     = "합격/불합격 판정"

3사가 받는 JSON Schema 서브셋이 서로 달라서, 계약 스키마를 그대로 보내면
어떤 곳은 400을 내고 어떤 곳은 제약을 조용히 무시한다. 그래서 프로바이더에는
각 사가 받는 형태로 **다운그레이드**해 보내고, 진짜 계약 강제는 돌아온 결과를
answer_draft.schema.json 으로 재검증하는 데서 한다.

⑦ 안전 검증 게이트는 프로바이더를 몰라야 한다(M2). 그래서 이 계층 밖으로는
표준 answer_draft dict 하나만 나간다.
"""
from __future__ import annotations

import copy
import json
import sys
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator

# M3 산출물을 그대로 재사용한다 (별도 구현 금지 — M3 설계 명시)
M3_SCHEMAS = (Path(__file__).resolve().parents[3]
              / "03-Data-Contracts-and-Safety" / "examples" / "schemas")

ANSWER_DRAFT_SCHEMA = json.loads(
    (M3_SCHEMAS / "answer_draft.schema.json").read_text(encoding="utf-8"))

_VALIDATOR = Draft202012Validator(ANSWER_DRAFT_SCHEMA)

# 어댑터가 주입하는 필드 — 프로바이더에게 요구하지 않는다.
# provider: 어느 어댑터가 만들었는지 어댑터 자신이 안다
# created_at: 수신 시각이므로 모델이 알 수 없다
# 이 둘을 프로바이더 스키마에 남기면 OpenAI strict(전 필드 required)에서 걸린다.
ADAPTER_INJECTED = ("provider", "created_at")

# ── 추론 강도 정규화 ───────────────────────────────────────────────────
# 3사가 같은 이름을 쓰지 않는다. 공통 척도를 하나 정하고 각 사 파라미터로 번역한다.
# None = 그 프로바이더에는 해당 수준이 없음 → 스윕에서 건너뛴다.
#
# claude : output_config.effort  (low/medium/high/xhigh/max, 기본 high)
#          thinking 을 끄는 선택지는 두지 않는다 — strict tool use 와 함께 쓰면
#          도구 호출이 tool_use 블록 대신 본문 텍스트로 나오는 실패 모드가 있다.
# openai : reasoning_effort      (minimal/low/medium/high)
# gemini : thinking_level        (low/high)
EFFORT_LEVELS = ("minimal", "low", "medium", "high")

EFFORT_MAP = {
    "claude": {"minimal": None, "low": "low", "medium": "medium", "high": "high"},
    "openai": {"minimal": "minimal", "low": "low", "medium": "medium", "high": "high"},
    "gemini": {"minimal": None, "low": "low", "medium": None, "high": "high"},
}


def native_effort(provider: str, effort: str | None) -> str | None:
    """공통 척도를 프로바이더 고유 값으로 번역한다. 미지원이면 None."""
    if effort is None:
        return None
    return EFFORT_MAP.get(provider, {}).get(effort)


class SchemaViolation(Exception):
    """재검증 실패. 같은 프로바이더 재시도 → 실패 시 폴백의 트리거."""

    def __init__(self, errors: list[str], raw: Any = None):
        self.errors = errors
        self.raw = raw
        super().__init__("; ".join(errors[:3]))


@dataclass
class LLMResult:
    """어댑터 출력. 게이트가 보는 것은 draft 하나뿐이고 나머지는 관측용이다."""
    draft: dict
    provider: str
    model: str
    latency_ms: int
    attempts: int = 1
    usage: dict = field(default_factory=dict)
    est_cost_usd: float | None = None


# ── 스키마 다운그레이드 ────────────────────────────────────────────────

def strip_keywords(schema: dict, drop: tuple[str, ...] | list[str]) -> dict:
    """스키마 트리에서 지정한 키워드를 재귀적으로 제거한다.

    프로바이더별로 받지 못하는 제약이 다르다. 제거해도 안전한 이유는
    최종 판정을 어댑터 뒤단 재검증이 하기 때문이다.
    """
    if not drop:
        return schema
    drop = set(drop)

    def walk(node):
        if isinstance(node, dict):
            return {k: walk(v) for k, v in node.items() if k not in drop}
        if isinstance(node, list):
            return [walk(v) for v in node]
        return node

    return walk(copy.deepcopy(schema))


def provider_schema(drop: tuple[str, ...] | list[str] = (),
                    force_all_required: bool = False) -> dict:
    """프로바이더에게 보낼 스키마를 만든다.

    1) 어댑터 주입 필드를 제거한다
    2) 각 사가 못 받는 키워드를 제거한다
    3) OpenAI strict 처럼 전 필드 required 를 요구하면 채워 넣는다
    """
    s = copy.deepcopy(ANSWER_DRAFT_SCHEMA)
    for k in ADAPTER_INJECTED:
        s["properties"].pop(k, None)
    s["required"] = [r for r in s.get("required", []) if r not in ADAPTER_INJECTED]
    s.pop("$schema", None)
    s.pop("$id", None)

    s = strip_keywords(s, drop)

    if force_all_required:
        def fix(node):
            if isinstance(node, dict):
                if node.get("type") == "object" and "properties" in node:
                    node["required"] = list(node["properties"].keys())
                    node.setdefault("additionalProperties", False)
                for v in node.values():
                    fix(v)
            elif isinstance(node, list):
                for v in node:
                    fix(v)
        fix(s)
    return s


# ── 정규화 + 재검증 ────────────────────────────────────────────────────

def normalize(payload: dict, provider: str) -> dict:
    """프로바이더 응답 본문을 내부 계약으로 맞춘다. (M3 매핑 규칙 표)"""
    d = dict(payload or {})
    d["provider"] = provider                        # 어댑터가 주입
    d.setdefault("created_at", datetime.now(timezone.utc).isoformat())
    # length_sentences 는 모델이 빠뜨리거나 실제 문장 수와 어긋나는 일이 잦다.
    # 계약상 이 값은 safety_policy 길이 하드컷의 입력이므로 실제 배열 길이를 신뢰한다.
    sentences = d.get("sentences")
    if isinstance(sentences, list):
        d["length_sentences"] = len(sentences)
    return d


def validate(draft: dict) -> None:
    """answer_draft.schema.json 재검증 + 스키마로 표현 못 하는 계약 검사."""
    errs = [f"{'/'.join(map(str, e.path)) or '(root)'}: {e.message}"
            for e in sorted(_VALIDATOR.iter_errors(draft), key=lambda e: list(e.path))]

    # claim_map 이 sentences 를 전부 덮는가.
    # JSON Schema로는 표현할 수 없지만 M3 계약의 핵심이다 —
    # 근거 없는 문장이 하나라도 있으면 ⑦ 게이트가 통과시켜선 안 된다.
    sents = draft.get("sentences")
    cmap = draft.get("claim_map")
    if isinstance(sents, list) and isinstance(cmap, list):
        covered = {c.get("sentence_idx") for c in cmap if isinstance(c, dict)}
        missing = [i for i in range(len(sents)) if i not in covered]
        if missing:
            errs.append(f"claim_map: 근거 없는 문장 인덱스 {missing}")
        out_of_range = sorted(i for i in covered
                              if isinstance(i, int) and not 0 <= i < len(sents))
        if out_of_range:
            errs.append(f"claim_map: 범위 밖 sentence_idx {out_of_range}")

    if errs:
        raise SchemaViolation(errs, raw=draft)


# ── 추상 클래스 ────────────────────────────────────────────────────────

class LLMProvider(ABC):
    """3사 공통 인터페이스.

    구현체는 요청 빌드와 응답 파싱만 책임진다. 정규화·검증·재시도·폴백은
    이 베이스와 router 가 처리하므로 프로바이더별로 중복 구현하지 않는다.
    """

    name: str = "base"

    def __init__(self, model: str, cost_per_1k_tokens: dict | None = None,
                 effort: str | None = None):
        self.model = model
        # {"input": 0.005, "output": 0.025} 형식. 확인되지 않은 값은 None 으로 둔다 —
        # 추측한 단가를 넣으면 비용 리포트가 조용히 틀린다.
        self.cost_per_1k_tokens = cost_per_1k_tokens or {}
        # 추론 강도. None 이면 프로바이더 기본값(=M5 측정 조건)을 그대로 쓴다.
        # 정규화된 값은 EFFORT_MAP 으로 각 사 파라미터에 번역한다.
        self.effort = effort

    @abstractmethod
    def _call(self, system: str, user: str, schema: dict) -> tuple[dict, dict]:
        """(파싱된 본문, usage dict) 를 반환한다. 예외는 그대로 올린다."""

    @abstractmethod
    def _schema_for_provider(self) -> dict:
        """이 프로바이더가 받아들이는 형태로 다운그레이드한 스키마."""

    def estimate_cost(self, usage: dict) -> float | None:
        c = self.cost_per_1k_tokens
        if not c or c.get("input") is None or c.get("output") is None:
            return None      # 미확인 단가를 추측하지 않는다
        return round(usage.get("input_tokens", 0) / 1000 * c["input"]
                     + usage.get("output_tokens", 0) / 1000 * c["output"], 6)

    def complete(self, system: str, user: str, max_retries: int = 1) -> LLMResult:
        """호출 → 정규화 → 재검증. 실패하면 오류를 붙여 같은 프로바이더로 재시도한다.

        재시도까지 실패하면 SchemaViolation 을 올린다. 폴백 판단은 router 몫이다.
        """
        import time
        schema = self._schema_for_provider()
        attempt, last = 0, None
        prompt = user
        while attempt <= max_retries:
            attempt += 1
            t0 = time.time()
            payload, usage = self._call(system, prompt, schema)
            latency = round((time.time() - t0) * 1000)
            draft = normalize(payload, self.name)
            try:
                validate(draft)
            except SchemaViolation as e:
                last = e
                if attempt > max_retries:
                    break
                # 오류를 프롬프트에 첨부해 같은 프로바이더로 한 번 더 (M3 흐름도)
                prompt = (f"{user}\n\n[이전 응답이 계약을 위반했습니다. "
                          f"아래를 고쳐 같은 스키마로 다시 출력하세요]\n- "
                          + "\n- ".join(e.errors[:5]))
                continue
            return LLMResult(draft=draft, provider=self.name, model=self.model,
                             latency_ms=latency, attempts=attempt, usage=usage,
                             est_cost_usd=self.estimate_cost(usage))
        raise last

    def stream(self, system: str, user: str):
        """스트리밍은 M6(TTS 라우팅)에서 문장 단위 발화와 함께 다룬다.

        지금 구현하면 검증 없는 문장이 스피커로 나갈 수 있다 —
        M1 "커버리지 없으면 침묵" 원칙과 충돌하므로 의도적으로 미구현으로 둔다.
        """
        raise NotImplementedError(
            "stream() 은 M6에서 구현한다. ⑦ 게이트 통과 전 발화를 막기 위해 의도적으로 비워 둔다.")
