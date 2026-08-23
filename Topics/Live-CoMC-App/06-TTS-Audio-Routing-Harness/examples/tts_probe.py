#!/usr/bin/env python3
"""M6 실습 1 — TTS 프리플라이트.

키가 있는지, 패키지가 깔렸는지만 보지 않는다. **짧은 한국어 문장을 실제로 합성**해서
파일이 나오는지까지 확인한다.

M5에서 LLM 프리플라이트를 models.list() 로만 만들었더니 3사 모두 "정상"이라고 했는데
실제 호출은 두 곳이 실패했다(잔액 부족, 모델 접근 권한 없음). 목록 조회는 인증만
검증하고 사용 권한은 검증하지 못한다. TTS 도 같은 함정이 있다 — 키가 유효해도
그 모델·그 보이스를 쓸 권한이 없을 수 있다.

모델 폴백도 여기서 해소한다. model 이 실패하면 model_fallbacks 를 순서대로 시도하고,
성공한 것을 runtime 레지스트리에 적는다. 추측한 모델 ID를 코드에 남기지 않기 위해서다.

실행:
    python tts_probe.py
    python tts_probe.py --provider openai
    python tts_probe.py --keep          # 프리플라이트 오디오를 지우지 않는다

산출:
    voice_registry.runtime.json   — 실제로 쓸 수 있는 것만 남은 레지스트리
    tts_log.jsonl                 — tts_preflight 이벤트

⚠️ 오디오를 재생하지 않는다. 파일만 쓴다.
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from tts_providers import TTSUnavailable, build  # noqa: E402

REGISTRY = HERE / "voice_registry.json"
RUNTIME = HERE / "voice_registry.runtime.json"
TTS_LOG = HERE / "tts_log.jsonl"
TMP = HERE / "audio" / "_preflight"


def log(event: dict):
    event["ts"] = datetime.now(timezone.utc).isoformat()
    with TTS_LOG.open("a", encoding="utf-8") as f:
        f.write(json.dumps(event, ensure_ascii=False) + "\n")


def probe_one(name: str, cfg: dict, shared_repl: dict) -> dict:
    """모델 후보를 순서대로 시도해 실제로 합성되는 첫 모델을 찾는다."""
    candidates = [cfg["model"]] + list(cfg.get("model_fallbacks") or [])
    tried = []

    for model in candidates:
        trial = dict(cfg)
        trial["model"] = model
        trial["replacements"] = {**shared_repl, **(cfg.get("replacements") or {})}
        trial["replacements"].pop("_note", None)
        try:
            p = build(name, trial)
        except TTSUnavailable as e:
            return {"usable": False, "reason": "unavailable", "detail": str(e),
                    "tried": tried}
        except Exception as e:
            return {"usable": False, "reason": "build", "detail": f"{type(e).__name__}: {e}"[:200],
                    "tried": tried}

        try:
            r = p.preflight(TMP)
        except Exception as e:
            tried.append({"model": model, "error": f"{type(e).__name__}: {e}"[:200]})
            continue

        return {
            "usable": True, "model": model, "voice": r.voice,
            "latency_ms": r.latency_ms, "first_chunk_ms": r.first_chunk_ms,
            "streamed": r.streamed, "bytes": r.bytes, "duration_s": r.duration_s,
            "ext": p.audio_ext, "tried": tried,
        }

    return {"usable": False, "reason": "all_models_failed", "tried": tried}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--provider")
    ap.add_argument("--keep", action="store_true")
    args = ap.parse_args()

    reg = json.loads(REGISTRY.read_text(encoding="utf-8"))
    shared = {k: v for k, v in (reg.get("shared_replacements") or {}).items()
              if not k.startswith("_")}
    targets = [args.provider] if args.provider else list(reg["providers"])

    TMP.mkdir(parents=True, exist_ok=True)
    results, usable = {}, {}

    for name in targets:
        cfg = reg["providers"][name]
        if not cfg.get("enabled", True):
            print(f"  - {name:<12} 레지스트리에서 비활성")
            continue

        print(f"  · {name:<12} 합성 시도...", end=" ", flush=True)
        r = probe_one(name, cfg, shared)
        results[name] = r

        if r["usable"]:
            fc = f"첫청크 {r['first_chunk_ms']}ms · " if r.get("first_chunk_ms") is not None else ""
            dur = f"{r['duration_s']}s" if r.get("duration_s") else "길이 미측정"
            print(f"OK  ({r['model']}/{r['voice']}) {fc}완료 {r['latency_ms']}ms · "
                  f"{r['bytes']:,}B · {dur}")
            usable[name] = {**{k: v for k, v in cfg.items() if not k.startswith("_")},
                            "model": r["model"], "ext": r["ext"],
                            "streaming_verified": bool(
                                r.get("first_chunk_ms") is not None
                                and r["first_chunk_ms"] < r["latency_ms"] * 0.9)}
        else:
            print(f"제외  ({r['reason']}) {r.get('detail','')}")
            for t in r.get("tried", []):
                print(f"       └ {t['model']}: {t['error'][:110]}")

    runtime = {
        "_comment": "tts_probe.py 가 생성한다. 직접 수정하지 말 것.",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "default_provider": reg["default_provider"] if reg["default_provider"] in usable
                            else (next(iter(usable), None)),
        "degrade_to": reg["degrade_to"] if reg["degrade_to"] in usable else None,
        "voice_policy": reg["voice_policy"],
        "shared_replacements": shared,
        "excluded": [n for n, r in results.items() if not r["usable"]],
        "providers": usable,
    }
    RUNTIME.write_text(json.dumps(runtime, ensure_ascii=False, indent=2), encoding="utf-8")
    log({"event": "tts_preflight", "results": results})

    print()
    print(f"사용 가능: {len(usable)}/{len(results)}개 — {', '.join(usable) or '없음'}")
    if runtime["excluded"]:
        print(f"제외: {', '.join(runtime['excluded'])}")
    if runtime["degrade_to"] is None:
        print("⚠ 강등 목적지(무료 프로바이더)가 없습니다 — 서킷 브레이커가 성립하지 않습니다")

    if not args.keep:
        for f in TMP.glob("_preflight_*"):
            f.unlink(missing_ok=True)

    return 0 if usable else 1


if __name__ == "__main__":
    sys.exit(main())
