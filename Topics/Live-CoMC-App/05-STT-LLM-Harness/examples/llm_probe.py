#!/usr/bin/env python3
"""M5 실습 4 — LLM 프로바이더 프리플라이트.

방송 시작 전에 3사 API가 실제로 살아 있는지 확인하고, 죽은 프로바이더를
fallback_order 에서 자동으로 빼는 것이 목적이다.

왜 필요한가:
  M3 설계의 폴백 흐름은 "다음 프로바이더로 넘어간다"를 전제한다. 그런데 방송 중에
  키가 만료된 걸 알게 되면 이미 늦다. 폴백 대상이 애초에 비어 있으면 HITL 로 떨어지고,
  M1 의 "커버리지 없으면 침묵" 원칙 때문에 진행자가 그 공백을 떠안는다.
  프리플라이트는 그 상황을 방송 전으로 옮긴다.

무엇을 확인하는가 (토큰 비용 0):
  1. 환경 변수에 키가 있는가
  2. 그 키로 models 목록을 부를 수 있는가  ← 인증 검증
  3. 그 모델을 **실제로 호출**할 수 있는가  ← 스모크 콜
     목록에 있다고 호출 가능한 게 아니다. 2026-08-20 실측으로 두 가지가 잡혔다:
       · Claude: 키 유효 + models.list() 성공인데 크레딧 잔액 부족으로 생성만 400
         (M5 개념 3 "소비자 구독 ≠ API 접근권" 의 실제 사례)
       · Gemini: gemini-2.5 계열이 목록에는 있으나 신규 사용자에게 404
     둘 다 목록 조회만 했으면 방송 중에 만났을 문제다.

스모크 콜은 max_tokens 4 짜리 한 번이라 비용이 사실상 0이다.

실행:
    python llm_probe.py                  # 전체 점검
    python llm_probe.py --provider claude
    python llm_probe.py --simulate-fail claude   # 강제 실패 → 나머지로 동작하는지 확인

산출:
    guides/llm_registry.runtime.json     # 사용 가능한 프로바이더만 담은 런타임 레지스트리
    examples/probe_log.jsonl             # 측정 로그 (M4 와 같은 형식으로 누적)
"""
import argparse
import json
import os
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

HERE = Path(__file__).resolve().parent
REGISTRY = HERE.parent / "guides" / "llm_registry.json"
RUNTIME = HERE.parent / "guides" / "llm_registry.runtime.json"
PROBE_LOG = HERE / "probe_log.jsonl"


def now_iso():
    return datetime.now(timezone.utc).isoformat()


def log(event: dict):
    event["ts"] = now_iso()
    with PROBE_LOG.open("a", encoding="utf-8") as f:
        f.write(json.dumps(event, ensure_ascii=False) + "\n")


# ── 프로바이더별 모델 목록 조회 ────────────────────────────────────────
# 각 함수는 (모델 ID 리스트) 를 반환하거나 예외를 던진다.
# 여기서만 SDK 를 만지고, 아래 check() 는 SDK 를 모른다.

def _list_claude(_cfg):
    import anthropic
    client = anthropic.Anthropic()          # ANTHROPIC_API_KEY 를 알아서 읽는다
    return [m.id for m in client.models.list()]


def _list_openai(_cfg):
    from openai import OpenAI
    client = OpenAI()                       # OPENAI_API_KEY
    return [m.id for m in client.models.list()]


_GEMINI_CLIENT = None


def _gemini_client():
    """google-genai 클라이언트는 프로세스당 하나만 만든다.

    ⚠ 함수 안에서 매번 genai.Client() 를 만들면, 먼저 만든 클라이언트가 GC 될 때
      공유 전송 계층이 닫히면서 이후 호출이
      "Cannot send a request, as the client has been closed" 로 죽는다
      (2026-08-20 실측). 목록 조회와 스모크 콜이 같은 인스턴스를 써야 한다.
    """
    global _GEMINI_CLIENT
    if _GEMINI_CLIENT is None:
        from google import genai
        _GEMINI_CLIENT = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
    return _GEMINI_CLIENT


def _list_gemini(_cfg):
    # google-genai 는 "models/gemini-..." 형태로 반환한다 → 접두어를 벗긴다
    return [m.name.split("/", 1)[-1] for m in _gemini_client().models.list()]


LISTERS = {"claude": _list_claude, "openai": _list_openai, "gemini": _list_gemini}


# ── 실제 호출 가능 여부 (스모크 콜) ────────────────────────────────────
# 2026-08-20 발견: gemini-2.5-pro 는 models.list() 에 나오지만 실제 호출하면
# 404 "no longer available to new users" 가 난다. 목록 조회는 인증만 검증하고
# 모델 접근 권한은 검증하지 못한다. 방송 중에 이걸 만나면 늦으므로
# 최소 토큰으로 실제 한 번 불러 본다. (문장 하나, 비용 사실상 0)

def _smoke_claude(model):
    import anthropic
    anthropic.Anthropic().messages.create(
        model=model, max_tokens=4, messages=[{"role": "user", "content": "hi"}])


def _smoke_openai(model):
    from openai import OpenAI
    OpenAI().chat.completions.create(
        model=model, max_completion_tokens=4,
        messages=[{"role": "user", "content": "hi"}])


def _smoke_gemini(model):
    from google.genai import types
    _gemini_client().models.generate_content(
        model=model, contents="hi",
        config=types.GenerateContentConfig(max_output_tokens=4))


SMOKERS = {"claude": _smoke_claude, "openai": _smoke_openai, "gemini": _smoke_gemini}


def model_candidates(cfg, available):
    """시도할 모델 후보를 우선순위대로 만든다.

    model_preferred 를 맨 앞에 두고, 그 뒤에 model_prefix 매칭을 붙인다.
    첫 후보가 스모크 콜에서 죽어도 다음 후보로 넘어갈 수 있게 하기 위함이다.
    """
    out = []
    preferred = cfg.get("model_preferred")
    if preferred and preferred in available:
        out.append(preferred)
    prefix = cfg.get("model_prefix") or ""

    def ver_key(m):
        # 버전 번호가 큰 것을 먼저 시도한다. 구버전이 폐지되는 일이 잦기 때문이다
        # (2026-08-20: gemini-2.5 계열이 신규 사용자에게 404).
        nums = [int(x) for x in re.findall(r"\d+", m)[:3]]
        while len(nums) < 3:
            nums.append(0)
        return (-nums[0], -nums[1], -nums[2], len(m), m)

    rest = sorted([m for m in available if m.startswith(prefix) and m not in out],
                  key=ver_key)
    return out + rest


def check(name, cfg, simulate_fail=False):
    """한 프로바이더를 점검한다. 결과 dict 를 반환한다."""
    r = {"provider": name, "enabled": cfg.get("enabled", True),
         "key_present": False, "auth_ok": False,
         "model_preferred": cfg.get("model_preferred"),
         "resolved_model": None, "substituted": False,
         "latency_ms": None, "smoke_ok": False, "tried": [],
         "error": None, "usable": False}

    if simulate_fail:
        r["error"] = "simulated failure (--simulate-fail)"
        return r

    if not r["enabled"]:
        r["error"] = "registry 에서 enabled=false"
        return r

    env_key = cfg.get("env_key")
    if not os.environ.get(env_key):
        r["error"] = f"환경 변수 {env_key} 없음"
        return r
    r["key_present"] = True

    t0 = time.time()
    try:
        available = LISTERS[name](cfg)
    except Exception as e:
        r["latency_ms"] = round((time.time() - t0) * 1000)
        # 키가 있는데 실패 = 만료·권한·네트워크. 원인을 그대로 남긴다.
        r["error"] = f"{type(e).__name__}: {e}"[:300]
        return r
    r["latency_ms"] = round((time.time() - t0) * 1000)
    r["auth_ok"] = True

    cands = model_candidates(cfg, available)
    if not cands:
        r["error"] = (f"model_preferred={cfg.get('model_preferred')!r} 도 "
                      f"prefix={cfg.get('model_prefix')!r} 매칭도 없음 "
                      f"(사용 가능 {len(available)}개)")
        return r

    # 목록에 있다고 호출 가능한 게 아니다 → 실제로 불러 본다
    tried = []
    for m in cands[:8]:
        try:
            SMOKERS[name](m)
        except Exception as e:
            tried.append(f"{m}: {type(e).__name__}: {str(e)[:110]}")
            continue
        r["resolved_model"] = m
        r["substituted"] = (m != cfg.get("model_preferred"))
        r["smoke_ok"] = True
        r["usable"] = True
        r["tried"] = tried
        return r

    r["tried"] = tried
    r["error"] = "후보 모델이 모두 스모크 콜 실패 → " + " / ".join(tried[:3])
    return r


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--provider", help="한 곳만 점검")
    ap.add_argument("--simulate-fail", default="",
                    help="쉼표로 구분. 해당 프로바이더를 강제 실패시켜 폴백 축소를 확인한다")
    args = ap.parse_args()

    reg = json.loads(REGISTRY.read_text(encoding="utf-8"))
    providers = reg["providers"]
    order = reg["fallback_order"]
    fail = {s.strip() for s in args.simulate_fail.split(",") if s.strip()}

    targets = [args.provider] if args.provider else order
    results = []
    for name in targets:
        if name not in providers:
            print(f"  ! 알 수 없는 프로바이더: {name}")
            continue
        results.append(check(name, providers[name], simulate_fail=(name in fail)))

    # ── 리포트 ────────────────────────────────────────────────────────
    print()
    print(f"{'프로바이더':<10} {'키':<4} {'인증':<5} {'호출':<5} {'지연':>7}  모델")
    print("-" * 80)
    for r in results:
        key = "OK" if r["key_present"] else "--"
        auth = "OK" if r["auth_ok"] else "--"
        lat = f"{r['latency_ms']}ms" if r["latency_ms"] is not None else "-"
        model = r["resolved_model"] or "-"
        if r["substituted"]:
            model += f"  (대체: preferred={r['model_preferred']} 사용 불가)"
        smoke = "OK" if r.get("smoke_ok") else "--"
        print(f"{r['provider']:<10} {key:<4} {auth:<5} {smoke:<5} {lat:>7}  {model}")
        if r["error"]:
            print(f"{'':<10} └ {r['error']}")

    usable = [r["provider"] for r in results if r["usable"]]
    excluded = [r["provider"] for r in results if not r["usable"]]

    print()
    print(f"사용 가능: {', '.join(usable) if usable else '없음'}")
    if excluded:
        print(f"자동 제외: {', '.join(excluded)}")

    # ── 런타임 레지스트리 기록 ────────────────────────────────────────
    # 어댑터는 이 파일을 읽는다. 죽은 프로바이더는 애초에 목록에 없다.
    runtime = {
        "_comment": "llm_probe.py 가 생성한다. 직접 수정하지 말 것.",
        "generated_at": now_iso(),
        "fallback_order": [p for p in order if p in usable],
        "excluded": excluded,
        "providers": {
            r["provider"]: {
                "env_key": providers[r["provider"]]["env_key"],
                "sdk": providers[r["provider"]]["sdk"],
                "model": r["resolved_model"],
                "structured_output": providers[r["provider"]]["structured_output"],
                "schema_unsupported_keywords":
                    providers[r["provider"]].get("schema_unsupported_keywords", []),
            }
            for r in results if r["usable"]
        },
    }
    RUNTIME.write_text(json.dumps(runtime, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"런타임 레지스트리 → {RUNTIME.name}  (폴백 순서: {' → '.join(runtime['fallback_order']) or '비어 있음'})")

    log({"event": "llm_preflight", "results": results,
         "usable": usable, "excluded": excluded,
         "simulated_fail": sorted(fail)})

    if not usable:
        print()
        print("모든 프로바이더가 사용 불가하다. 이 상태로는 ⑥ LLM 응답 단계가 동작하지 않는다.")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
