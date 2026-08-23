#!/usr/bin/env python3
"""M5 실습 1·2 — 한국어 STT 정확도 실측 + 3단 폴백.

실습 1: gpt-live-transcribe 로 20문장을 전사하고 정답과 대조해 오류율을 잰다.
실습 2: 1단계를 강제로 실패시켜 2단계 → 3단계로 자동 전환되는지 확인한다.

폴백 3단 (M5 Roadmap):
    1) gpt-4o-transcribe   클라우드, 배치 전사 중 정확도 우선
    2) gpt-transcribe      클라우드, 대체
    3) 로컬 whisper        네트워크가 끊겨도 돌아간다 (CPU 추론이라 느림)

    ⚠ Roadmap 의 gpt-live-transcribe 는 Realtime(WebSocket) 전용이라
      파일 전사 엔드포인트에 없다. 실시간 경로에서 따로 측정해야 한다.

왜 WER 과 CER 을 같이 재는가:
    WER 은 공백으로 나눈 어절 단위다. 한국어는 조사 하나만 틀려도
    ("문서는" → "문서가") 그 어절 전체가 오답이 되어 오류율이 부풀려진다.
    CER(문자 단위)은 그 왜곡이 작아서 "실제로 알아들었는가"에 더 가깝다.
    영어 기준 공개 WER 수치와 직접 비교하면 안 되는 이유이기도 하다.

실행:
    python stt_probe.py --condition clean
    python stt_probe.py --condition bgm
    python stt_probe.py --condition routed        # M6 라우팅 후 재측정
    python stt_probe.py --condition clean --force-fail t4o    # 폴백 검증
    python stt_probe.py --condition clean --tier local        # 특정 단계만

산출:
    guides/stt-wer-report.md   조건별 오류율 리포트
    examples/probe_log.jsonl   측정 로그
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from utterances import UTTERANCES, WAKE_WORD, normalize  # noqa: E402

PROBE_LOG = HERE / "probe_log.jsonl"
REPORT = HERE.parent / "guides" / "stt-wer-report.md"

# 폴백 사다리. 앞에서부터 시도한다.
#
# ⚠ Roadmap 은 1단계를 gpt-live-transcribe 로 잡았지만, 그 모델은
#   POST /v1/audio/transcriptions 에 존재하지 않는다 (2026-08-20 실측: 404
#   "Invalid URL"). Realtime API(WebSocket) 전용이라 파일 전사로는 못 쓴다.
#   → 파일 기반 오프라인 측정은 아래 3단으로 하고,
#     gpt-live-transcribe 는 실시간 경로에서 별도로 재야 한다 (M7).
TIERS = [
    ("t4o",   "gpt-4o-transcribe", "cloud"),   # 1단: 배치 전사 중 정확도 우선
    ("batch", "gpt-transcribe",    "cloud"),   # 2단: 대체 클라우드
    ("local", "small",             "local"),   # 3단: 네트워크 끊겨도 동작 (CPU, 느림)
]


def log(event: dict):
    event["ts"] = datetime.now(timezone.utc).isoformat()
    with PROBE_LOG.open("a", encoding="utf-8") as f:
        f.write(json.dumps(event, ensure_ascii=False) + "\n")


# ── 오류율 계산 ────────────────────────────────────────────────────────

def edit_distance(a: list, b: list) -> int:
    """레벤슈타인 거리. 삽입·삭제·치환 각 1."""
    if not a:
        return len(b)
    if not b:
        return len(a)
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j] + 1,          # 삭제
                           cur[j - 1] + 1,       # 삽입
                           prev[j - 1] + (ca != cb)))  # 치환
        prev = cur
    return prev[-1]


def error_rates(ref: str, hyp: str) -> tuple[float, float, int, int]:
    """(WER, CER, 참조 어절 수, 참조 문자 수)"""
    r, h = normalize(ref), normalize(hyp)
    rw, hw = r.split(), h.split()
    rc, hc = list(r.replace(" ", "")), list(h.replace(" ", ""))
    wer = edit_distance(rw, hw) / max(1, len(rw))
    cer = edit_distance(rc, hc) / max(1, len(rc))
    return wer, cer, len(rw), len(rc)


# ── 전사기 ─────────────────────────────────────────────────────────────

_WHISPER = None


def transcribe_cloud(wav: Path, model: str) -> str:
    from openai import OpenAI
    with wav.open("rb") as f:
        r = OpenAI().audio.transcriptions.create(
            model=model, file=f, language="ko", response_format="text")
    return r if isinstance(r, str) else getattr(r, "text", str(r))


def transcribe_local(wav: Path, model: str) -> str:
    """로컬 whisper. GPU 가 없으므로 CPU 추론이라 느리다 — 최후 수단인 이유."""
    global _WHISPER
    import whisper
    if _WHISPER is None:
        print(f"    (로컬 whisper '{model}' 로딩 — 최초 1회만)", flush=True)
        _WHISPER = whisper.load_model(model)
    return _WHISPER.transcribe(str(wav), language="ko", fp16=False)["text"]


def run_tier(tier: str, model: str, kind: str, wav: Path) -> str:
    if kind == "local":
        return transcribe_local(wav, model)
    return transcribe_cloud(wav, model)


def transcribe_with_fallback(wav: Path, force_fail: set, only_tier: str | None):
    """3단 폴백. (전사문, 사용한 단계, 시도 기록) 반환."""
    tried = []
    ladder = [t for t in TIERS if (only_tier is None or t[0] == only_tier)]
    for tier, model, kind in ladder:
        t0 = time.time()
        try:
            if tier in force_fail:
                raise RuntimeError(f"forced failure (--force-fail {tier})")
            text = run_tier(tier, model, kind, wav)
        except Exception as e:
            tried.append({"tier": tier, "model": model, "ok": False,
                          "ms": round((time.time() - t0) * 1000),
                          "error": f"{type(e).__name__}: {str(e)[:120]}"})
            continue
        tried.append({"tier": tier, "model": model, "ok": True,
                      "ms": round((time.time() - t0) * 1000)})
        return text.strip(), tier, tried
    return None, None, tried


# ── 메인 ───────────────────────────────────────────────────────────────

def main():
    ap = argparse.ArgumentParser()
    # routed: M6 라우팅 후 재측정. 결과는 stt_result_routed.json 으로 따로 쌓인다.
    ap.add_argument("--condition", default="clean",
                    choices=["clean", "bgm", "routed"])
    ap.add_argument("--force-fail", default="",
                    help="쉼표 구분. 예: live 또는 live,batch")
    ap.add_argument("--tier", choices=[t[0] for t in TIERS],
                    help="한 단계만 쓴다 (폴백 없음)")
    ap.add_argument("--limit", type=int, help="앞 N개만")
    args = ap.parse_args()

    d = HERE / "utterances" / args.condition
    manifest = d / "manifest.json"
    if not manifest.exists():
        sys.exit(f"{manifest} 없음. 먼저 record_utterances.py --condition {args.condition} 를 실행하세요.")
    items = json.loads(manifest.read_text(encoding="utf-8"))["items"]
    if args.limit:
        items = items[:args.limit]
    force_fail = {s.strip() for s in args.force_fail.split(",") if s.strip()}

    print(f"\n조건: {args.condition}   문장: {len(items)}개"
          + (f"   강제 실패: {', '.join(sorted(force_fail))}" if force_fail else "")
          + (f"   단계 고정: {args.tier}" if args.tier else ""))
    print()

    rows, tier_used = [], {}
    for it in items:
        wav = d / it["wav"]
        text, tier, tried = transcribe_with_fallback(wav, force_fail, args.tier)
        if text is None:
            print(f"  {it['id']}  전 단계 실패")
            for t in tried:
                print(f"        {t['tier']}: {t.get('error')}")
            rows.append({**it, "hyp": None, "tier": None, "tried": tried})
            continue

        wer, cer, nw, nc = error_rates(it["text"], text)
        tier_used[tier] = tier_used.get(tier, 0) + 1
        ms = next(t["ms"] for t in tried if t["ok"])
        wake_ok = (WAKE_WORD in text) if (WAKE_WORD in it["text"]) else None

        flag = "  " if cer < 0.10 else ("⚠ " if cer < 0.30 else "✗ ")
        print(f"{flag}{it['id']} [{tier:<5}] WER {wer:5.1%}  CER {cer:5.1%}  {ms:>6}ms")
        if cer >= 0.10:
            print(f"        정답: {it['text']}")
            print(f"        전사: {text}")
        rows.append({**it, "hyp": text, "tier": tier, "wer": wer, "cer": cer,
                     "ref_words": nw, "ref_chars": nc, "ms": ms,
                     "wake_ok": wake_ok, "tried": tried})

    ok = [r for r in rows if r.get("hyp")]
    if not ok:
        print("\n전사 성공 0건")
        return 1

    # 전체 오류율은 문장별 평균이 아니라 총 오류/총 길이로 낸다 (표준 방식)
    agg_wer = (sum(r["wer"] * r["ref_words"] for r in ok)
               / sum(r["ref_words"] for r in ok))
    agg_cer = (sum(r["cer"] * r["ref_chars"] for r in ok)
               / sum(r["ref_chars"] for r in ok))
    q = [r for r in ok if r["type"] == "question"]
    c = [r for r in ok if r["type"] == "command"]
    wakes = [r for r in ok if r["wake_ok"] is not None]
    wake_hit = sum(1 for r in wakes if r["wake_ok"])

    print()
    print(f"전체    WER {agg_wer:6.1%}   CER {agg_cer:6.1%}   ({len(ok)}/{len(rows)} 문장)")
    if q:
        print(f"질문형  WER {sum(r['wer'] for r in q)/len(q):6.1%}   "
              f"CER {sum(r['cer'] for r in q)/len(q):6.1%}")
    if c:
        print(f"명령형  WER {sum(r['wer'] for r in c)/len(c):6.1%}   "
              f"CER {sum(r['cer'] for r in c)/len(c):6.1%}")
    if wakes:
        print(f"호출어 '{WAKE_WORD}' 정확 전사: {wake_hit}/{len(wakes)}")
    print(f"사용 단계: " + ", ".join(f"{k} {v}건" for k, v in tier_used.items()))
    print(f"평균 지연: {sum(r['ms'] for r in ok)/len(ok):.0f}ms")

    log({"event": "stt_wer", "condition": args.condition,
         "agg_wer": agg_wer, "agg_cer": agg_cer,
         "tier_used": tier_used, "force_fail": sorted(force_fail),
         "items": [{k: v for k, v in r.items() if k != "tried"} for r in rows]})

    (HERE / f"stt_result_{args.condition}.json").write_text(
        json.dumps({"condition": args.condition, "agg_wer": agg_wer,
                    "agg_cer": agg_cer, "tier_used": tier_used, "items": rows},
                   ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\n결과 → stt_result_{args.condition}.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
