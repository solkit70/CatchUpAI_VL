#!/usr/bin/env python3
"""M7 공통 유틸 — 파일 기반 6단계가 공유하는 것들.

## 왜 파일 기반인가

각 단계가 JSON 을 읽고 JSON 을 쓴다. 함수 호출로 이어 붙이면 빠르지만,
방송 사고가 났을 때 **어느 단계가 잘못됐는지 알 수 없다.**
파일로 남기면 `output/` 폴더만 열어 보고 원인 단계를 좁힐 수 있다.

  01 → rundown_index.json
  02 → broadcast_context.json
  03 → intent.json
  04 → answer_draft.json
  05 → verdict.json
  06 → output.json  (+ overlay.json / spoken.json)

그리고 전 단계가 `session_trace.jsonl` 에 append 한다. 파일이 남지 않는 사고는
재현할 수 없고, 재현할 수 없는 사고는 고칠 수 없다.

## 스키마는 M3 원본을 직접 읽는다

복사본을 두지 않는다. M6에서 `voice_registry.runtime.json` 이 원본보다 오래돼
비용 표가 조용히 틀렸던 일이 있었다(M6 문제 3). 파생 사본은 원본이 바뀐 것을
스스로 알지 못한다. 스키마는 하나만 둔다.

`safety_policy.json` 만 예외로 `data/` 에 복사한다(로드맵 산출물 명세).
대신 원본 해시를 함께 확인해 드리프트를 즉시 드러낸다.
"""
from __future__ import annotations

import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

try:
    # stderr 도 반드시 함께 바꾼다. 오류 메시지는 stderr 로 나가는데
    # 여기서 cp1252 로 두면 정작 사고가 났을 때 한글이 파트 처럼 깨져
    # 원인을 읽을 수 없다.
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

ROOT = Path(__file__).resolve().parents[1]          # 07-CoMC-Engine-POC/
TOPIC = ROOT.parent                                  # Topics/Live-CoMC-App/
DATA = ROOT / "data"
OUTPUT = ROOT / "output"
TRACE = OUTPUT / "session_trace.jsonl"

SCHEMA_DIR = TOPIC / "03-Data-Contracts-and-Safety" / "examples" / "schemas"
SAFETY_SRC = TOPIC / "03-Data-Contracts-and-Safety" / "examples" / "safety_policy.json"
SAFETY_COPY = DATA / "safety_policy.json"

# Topics -> CatchUpAI_VL -> Ingest -> Changsoo_Vault  (parents[3])
# parents[2] 로 두면 Ingest 를 볼트 루트로 잡아 'Roundup/...' 링크가 전부
# missing_file 로 떨어진다 — 문서가 없는 것과 경로가 틀린 것을 구분 못 하게 된다.
VAULT = TOPIC.parents[3]


# ── 입출력 ────────────────────────────────────────────────────────────

def read_json(path: Path) -> Any:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def write_json(path: Path, data: Any) -> Path:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n",
                    encoding="utf-8")
    return path


def read_text(path: Path) -> str:
    return Path(path).read_text(encoding="utf-8")


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


# ── 추적 ──────────────────────────────────────────────────────────────

def trace(stage: str, **fields) -> None:
    """session_trace.jsonl 에 한 줄 append.

    각 단계는 성공/실패와 무관하게 반드시 한 줄을 남긴다.
    실패한 단계가 아무것도 남기지 않으면 "여기까지는 됐다"를 판정할 수 없다.
    """
    TRACE.parent.mkdir(parents=True, exist_ok=True)
    rec = {"ts": now_iso(), "stage": stage, **fields}
    with TRACE.open("a", encoding="utf-8") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")


# ── 스키마 검증 ───────────────────────────────────────────────────────

_validators: dict[str, Any] = {}


def validator(schema_name: str):
    from jsonschema import Draft202012Validator
    if schema_name not in _validators:
        schema = read_json(SCHEMA_DIR / f"{schema_name}.schema.json")
        _validators[schema_name] = Draft202012Validator(schema)
    return _validators[schema_name]


def validate(schema_name: str, instance: Any) -> list[str]:
    """M3 계약 위반 목록을 돌려준다. 빈 리스트면 통과."""
    v = validator(schema_name)
    return [f"{'/'.join(map(str, e.path)) or '(root)'}: {e.message}"
            for e in sorted(v.iter_errors(instance), key=lambda e: list(e.path))]


def validate_or_die(schema_name: str, instance: Any, stage: str) -> None:
    """검증 실패를 조용히 넘기지 않는다.

    파이프라인 중간 산출물이 계약을 어긴 채 다음 단계로 흘러가면
    사고는 훨씬 뒤에서 터지고 원인은 훨씬 찾기 어려워진다.
    """
    errs = validate(schema_name, instance)
    if errs:
        trace(stage, ok=False, schema=schema_name, errors=errs[:5])
        print(f"\n[{stage}] {schema_name} 계약 위반 {len(errs)}건:", file=sys.stderr)
        for e in errs[:8]:
            print(f"   - {e}", file=sys.stderr)
        sys.exit(1)


# ── 안전 정책 ─────────────────────────────────────────────────────────

def _sha(path: Path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()[:16]


def load_safety_policy(warn: bool = True) -> dict:
    """data/ 사본을 읽되 M3 원본과 다르면 경고한다.

    사본은 원본이 바뀐 것을 스스로 알지 못한다. 안전 정책이 낡은 채로
    게이트가 도는 것은 게이트가 없는 것보다 나쁘다 — 있다고 믿게 만들기 때문이다.
    """
    if warn and SAFETY_SRC.exists():
        a, b = _sha(SAFETY_COPY), _sha(SAFETY_SRC)
        if a != b:
            print(f"⚠ safety_policy.json 이 M3 원본과 다릅니다 "
                  f"(사본 {a} / 원본 {b}). 원본을 다시 복사하세요.", file=sys.stderr)
            trace("safety_policy", ok=False, reason="drift", copy=a, source=b)
    return read_json(SAFETY_COPY)


# ── 경로 도우미 ───────────────────────────────────────────────────────

def out(name: str) -> Path:
    return OUTPUT / name


def vault_path(rel: str) -> Path:
    """볼트 상대 경로를 실제 경로로. 'AI/' 접두사 생략 규칙을 흡수한다."""
    p = VAULT / rel
    if p.exists():
        return p
    alt = VAULT / "AI" / rel
    return alt if alt.exists() else p


def rel_to_vault(path: Path) -> str:
    try:
        return str(Path(path).resolve().relative_to(VAULT)).replace("\\", "/")
    except ValueError:
        return str(path)
