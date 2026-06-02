"""
connection_probe.py — DashScope Intl API 연결 상태 점검 하네스 (M2)

목적: API 호출 성공 여부와 응답 시간(Latency)을 측정·기록한다.
     M3 이후 품질 하네스의 기반이 되는 Connection Harness.

실행:
    python connection_probe.py              # 기본 1회 점검
    python connection_probe.py --repeat 3  # 3회 반복 측정
"""

import argparse
import json
import os
import sys
import time
from datetime import datetime
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

import dashscope

# ── 설정 ──────────────────────────────────────────────────────────────────
dashscope.base_http_api_url = "https://dashscope-intl.aliyuncs.com/api/v1"
MODEL      = "qwen3-tts-flash"
PROBE_TEXT = "Connection probe."          # 짧은 텍스트로 비용 최소화
LOG_FILE   = Path(__file__).parent / "probe_log.jsonl"


def probe_once() -> dict:
    """API를 1회 호출하고 결과를 dict로 반환."""
    ts = datetime.now().isoformat(timespec="seconds")
    t_start = time.time()
    try:
        response = dashscope.MultiModalConversation.call(
            model=MODEL,
            api_key=os.environ["DASHSCOPE_API_KEY"],
            text=PROBE_TEXT,
            voice="Cherry",
            language_type="English",
            stream=False,
        )
        elapsed = round(time.time() - t_start, 3)
        if response.status_code == 200:
            return {"ts": ts, "ok": True,  "latency_s": elapsed, "model": MODEL}
        else:
            return {"ts": ts, "ok": False, "latency_s": elapsed,
                    "error": f"{response.status_code}: {response.message}"}
    except Exception as exc:
        elapsed = round(time.time() - t_start, 3)
        return {"ts": ts, "ok": False, "latency_s": elapsed, "error": str(exc)}


def print_result(r: dict, idx: int = 1, total: int = 1) -> None:
    status = "✅ OK" if r["ok"] else "❌ FAIL"
    print(f"  [{idx}/{total}] {status}  latency={r['latency_s']}s  ({r['ts']})")
    if not r["ok"]:
        print(f"         error: {r['error']}")


def main():
    parser = argparse.ArgumentParser(description="DashScope TTS 연결 상태 점검")
    parser.add_argument("--repeat", type=int, default=1, help="점검 반복 횟수")
    args = parser.parse_args()

    if not os.environ.get("DASHSCOPE_API_KEY"):
        raise EnvironmentError("DASHSCOPE_API_KEY 환경변수가 설정되지 않았습니다.")

    print(f"Connection Probe — 모델: {MODEL}  반복: {args.repeat}회\n")

    results = []
    for i in range(1, args.repeat + 1):
        r = probe_once()
        results.append(r)
        print_result(r, i, args.repeat)
        # 결과를 JSONL 로그에 누적
        with LOG_FILE.open("a", encoding="utf-8") as f:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
        if i < args.repeat:
            time.sleep(1)

    # 요약
    ok_count  = sum(1 for r in results if r["ok"])
    avg_lat   = round(sum(r["latency_s"] for r in results) / len(results), 3)
    print(f"\n─── 요약 ───────────────────────────────")
    print(f"  성공: {ok_count}/{args.repeat}  평균 응답시간: {avg_lat}s")
    print(f"  로그: {LOG_FILE}")


if __name__ == "__main__":
    main()
