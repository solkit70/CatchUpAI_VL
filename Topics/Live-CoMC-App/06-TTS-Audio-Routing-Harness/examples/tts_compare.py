#!/usr/bin/env python3
"""M6 실습 2 — 지연·비용·안정성 실측표.

기본 프로바이더를 취향이 아니라 데이터로 정하기 위한 측정이다.

문장 세트는 세 종류다. 방송에서 실제로 나올 발화의 성질이 서로 다르기 때문이다.

  plain    평범한 한국어 발화       — 기준선
  mixed    숫자·영어 약어 혼합       — 이 파이프라인의 실제 발화가 이렇게 생겼다
  long     긴 문장                  — RTF 가 길이에 따라 무너지는지

`mixed` 를 따로 둔 이유는 M5에서 나온 발견 때문이다. LLM 단계에서 Gemini 는 숫자를
"마흔두 개"로 풀어 썼고 Claude·OpenAI 는 "42개"로 남겼다. 그 차이가 TTS 로 넘어오면
읽는 방식과 길이가 달라진다. 여기서는 **합성 길이와 그 편차**로 그 영향을 본다.

⚠️ 주관 청취 품질은 이 스크립트가 판정하지 않는다. 오디오를 재생하지 않기 때문이다
   (라이브 방송 중이면 스피커 출력이 방송에 섞이고 M4 에코 게이트 조건까지 오염된다).
   품질 평가는 생성된 파일을 나중에 따로 들어서 채운다.

실행:
    python tts_compare.py
    python tts_compare.py --repeats 3
    python tts_compare.py --provider edge

산출:
    audio/compare/{provider}_{case}_{n}.{ext}
    tts_comparison.json
    tts_log.jsonl 에 tts_compare 이벤트
"""
from __future__ import annotations

import argparse
import json
import statistics
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

RUNTIME = HERE / "voice_registry.runtime.json"
OUT_DIR = HERE / "audio" / "compare"
RESULT = HERE / "tts_comparison.json"
TTS_LOG = HERE / "tts_log.jsonl"

# 실제 방송 발화를 축소한 문장들. M5 llm_compare 의 답변 초안에서 가져왔다 —
# 파이프라인이 진짜로 TTS 에 넘길 문장이 이렇게 생겼다.
CASES = {
    "plain": "오늘 3번 파트는 FDE 영상 제작 과정을 다룹니다.",
    "mixed": "한국어 28분 1초, 영어 27분 11초 두 편을 공개했고요, "
             "조사 문서 42개가 GitHub에 전부 공개돼 있습니다.",
    "long": "네, 확인해 볼게요. 오늘 3번 파트는 FDE 영상 제작 과정을 다루고, "
            "한국어 28분 1초와 영어 27분 11초 두 편을 공개했습니다. "
            "관련 조사 문서 42개도 GitHub에 전부 올려 두었으니 방송 후에 "
            "링크를 통해 직접 확인하실 수 있습니다.",
}


def log(event: dict):
    event["ts"] = datetime.now(timezone.utc).isoformat()
    with TTS_LOG.open("a", encoding="utf-8") as f:
        f.write(json.dumps(event, ensure_ascii=False) + "\n")


def fmt(v, unit="", nd=0):
    if v is None:
        return "—"
    return f"{v:.{nd}f}{unit}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--provider")
    ap.add_argument("--repeats", type=int, default=2)
    args = ap.parse_args()

    if not RUNTIME.exists():
        sys.exit("voice_registry.runtime.json 이 없습니다. 먼저 python tts_probe.py 를 실행하세요.")
    rt = json.loads(RUNTIME.read_text(encoding="utf-8"))
    shared = rt["shared_replacements"]
    targets = [args.provider] if args.provider else list(rt["providers"])

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    results = {}

    for name in targets:
        cfg = dict(rt["providers"][name])
        cfg["replacements"] = {**shared, **(cfg.get("replacements") or {})}
        try:
            p = build(name, cfg)
        except TTSUnavailable as e:
            print(f"  ! {name}: {e}")
            continue

        print(f"\n═══ {name} ({cfg['model']} / {cfg['voice']}) ═══")
        results[name] = {"model": cfg["model"], "voice": cfg["voice"],
                         "cost_per_1k_chars": cfg.get("cost_per_1k_chars"),
                         "cost_confirmed": cfg.get("cost_confirmed", False),
                         "cost_incomplete": cfg.get("cost_incomplete", False),
                         "cases": {}}

        for case, text in CASES.items():
            runs = []
            for i in range(args.repeats):
                out = OUT_DIR / f"{name}_{case}_{i+1}"
                try:
                    r = p.synth(text, out)
                except Exception as e:
                    print(f"  {case:<6} #{i+1} ✗ {type(e).__name__}: {str(e)[:80]}")
                    runs.append({"ok": False, "error": f"{type(e).__name__}: {e}"[:200]})
                    continue
                runs.append({
                    "ok": True, "latency_ms": r.latency_ms,
                    "first_chunk_ms": r.first_chunk_ms, "duration_s": r.duration_s,
                    "rtf": r.rtf, "bytes": r.bytes, "chars": r.chars,
                    "est_cost_usd": r.est_cost_usd, "path": r.path.name,
                })
                fc = f"첫청크 {r.first_chunk_ms}ms" if r.first_chunk_ms is not None else "첫청크 —"
                print(f"  {case:<6} #{i+1} ✓ {fc} · 완료 {r.latency_ms}ms · "
                      f"오디오 {r.duration_s}s · RTF {r.rtf}")

            good = [x for x in runs if x.get("ok")]
            results[name]["cases"][case] = {
                "runs": runs,
                "chars": len(p.prepare_text(text)),
                "latency_med_ms": round(statistics.median([x["latency_ms"] for x in good])) if good else None,
                "first_chunk_med_ms": (round(statistics.median(
                    [x["first_chunk_ms"] for x in good if x["first_chunk_ms"] is not None]))
                    if any(x["first_chunk_ms"] is not None for x in good) else None),
                "duration_med_s": round(statistics.median([x["duration_s"] for x in good]), 3)
                    if good and all(x["duration_s"] for x in good) else None,
                "rtf_med": round(statistics.median([x["rtf"] for x in good]), 3)
                    if good and all(x["rtf"] for x in good) else None,
                # 방송에서는 중앙값이 아니라 최악값이 사고를 만든다.
                # 한 번의 긴 침묵이 스무 번의 빠른 응답을 지운다.
                "first_chunk_max_ms": (max(
                    [x["first_chunk_ms"] for x in good if x["first_chunk_ms"] is not None])
                    if any(x["first_chunk_ms"] is not None for x in good) else None),
                "latency_max_ms": max([x["latency_ms"] for x in good]) if good else None,
                "n_ok": len(good),
            }

    # ── 표 1: 지연 ────────────────────────────────────────────────────
    print()
    print("【지연】 첫 청크 = 재생을 시작할 수 있는 시점 · 완료 = 합성이 끝난 시점")
    print("        방송에서 사고를 만드는 것은 중앙값이 아니라 최악값이다.")
    print(f"{'프로바이더':<11} {'문장':<7} {'첫청크(중앙)':>12} {'첫청크(최악)':>12} "
          f"{'완료(중앙)':>10} {'RTF':>6} {'조기시작':>9}")
    print("-" * 74)
    for name, r in results.items():
        for case, c in r["cases"].items():
            if c["latency_med_ms"] is None:
                continue
            fc, lat = c["first_chunk_med_ms"], c["latency_med_ms"]
            gain = f"{lat - fc:,}ms" if fc is not None and lat - fc > lat * 0.1 else "없음"
            print(f"{name:<11} {case:<7} {fmt(fc,'ms'):>12} {fmt(c['first_chunk_max_ms'],'ms'):>12} "
                  f"{fmt(lat,'ms'):>10} {fmt(c['rtf_med'],'',3):>6} {gain:>9}")

    # ── 표 2: 비용 ────────────────────────────────────────────────────
    print()
    print("【비용】 1시간 방송에서 AI 발화 100회 × 평균 80자 = 8,000자 가정")
    print(f"{'프로바이더':<11} {'$/1k자':>10} {'8,000자':>10}  근거")
    print("-" * 64)
    for name, r in results.items():
        c = r["cost_per_1k_chars"]
        if c is None:
            note = "미확인 — 공식 가격 확인 필요"
            print(f"{name:<11} {'—':>10} {'—':>10}  {note}")
        else:
            note = "확인됨" if r["cost_confirmed"] else "미확인"
            if r["cost_incomplete"]:
                note = "⚠ 하한값 — 오디오 출력 토큰 요금 별도"
            print(f"{name:<11} {'$'+format(c,'.4f'):>10} {'$'+format(c*8,'.3f'):>10}  {note}")

    RESULT.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    log({"event": "tts_compare", "repeats": args.repeats,
         "summary": {n: {c: {k: v for k, v in d.items() if k != "runs"}
                         for c, d in r["cases"].items()} for n, r in results.items()}})
    print(f"\n오디오: {OUT_DIR.relative_to(HERE)}/  ·  원자료: {RESULT.name}")
    print("주관 청취 평가는 방송 종료 후 위 파일들을 들어서 채운다 (여기서는 재생하지 않는다).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
