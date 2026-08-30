#!/usr/bin/env python3
"""M7 ⑥ verdict → output.json (+ overlay.json / spoken.json).

화면용과 음성용을 나눠 쓴다. M2 App Boundary 의 오디오판과 같은 이유다 —
하나가 잘못돼도 다른 하나로 방송을 이어갈 수 있어야 한다. OBS 에서 TTS 트랙만
뮤트할 수 있는 것과 같은 구조를, 데이터 층에서도 유지한다.

## verdict.pass=false 여도 발화할 수 있다

전부 아니면 전무가 아니다. 근거가 확인된 문장(`kept_sentences`)만 골라 말한다.
그래서 `source_verdict_pass` 를 함께 남긴다 — "이 발화는 부분 통과였다"를
사후에 알 수 있어야 한다. 남기지 않으면 완전 통과와 부분 통과가 구분되지 않는다.

**남은 문장이 하나도 없으면 파일을 쓰지 않는다.** 빈 텍스트로 overlay 를 갱신하면
화면이 깜빡이고, 빈 문자열을 TTS 에 넘기면 프로바이더마다 다르게 실패한다.
말할 것이 없을 때는 아무것도 하지 않는 것이 맞다 (M1 "커버리지 없으면 침묵").

## provider 는 명시한다

`spoken.provider` 는 2026-08-23 에 추가한 필수 필드다. M6 서킷 브레이커가 런타임에
프로바이더를 교체하므로 voice id 로 역추정하면 사후 분석 때 어느 발화가
강등/승격 이후였는지 가릴 수 없다. 값은 M6 런타임 레지스트리에서 읽는다.

⚠️ 이 단계는 **오디오를 합성하지 않는다.** 무엇을 어떤 목소리로 말할지 적을 뿐이다.
   실제 합성·재생은 M9 셸의 몫이고, 그래서 audio_path 는 null 로 둔다.

실행:
    python 06_render_output.py --live 21
    python 06_render_output.py --live 21 --provider openai

산출:
    output/output.json · output/overlay.json · output/spoken.json
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from common import (TOPIC, now_iso, out, read_json, trace,  # noqa: E402
                    validate_or_die, write_json)

M6_RUNTIME = (TOPIC / "06-TTS-Audio-Routing-Harness" / "examples"
              / "voice_registry.runtime.json")


def pick_voice(explicit: str | None) -> tuple[str, str]:
    """(provider, voice) — M6 실측으로 정한 기본값을 레지스트리에서 읽는다."""
    if not M6_RUNTIME.exists():
        # 레지스트리가 없으면 추측하지 않는다. M6 프리플라이트를 돌리라고 말한다.
        sys.exit(f"{M6_RUNTIME.name} 없음. 06-TTS-Audio-Routing-Harness/examples 에서 "
                 "python tts_probe.py 를 먼저 실행하세요.")
    rt = read_json(M6_RUNTIME)
    name = explicit or rt["default_provider"]
    cfg = rt["providers"].get(name)
    if cfg is None:
        avail = ", ".join(rt["providers"])
        sys.exit(f"TTS 프로바이더 '{name}' 은 사용 가능 목록에 없습니다: {avail}")
    return name, cfg["voice"]


def load_session_state(part_id: str) -> dict:
    """session_state.json 이 있으면 읽고, 없으면 최소값을 만든다.

    권위값/추정값 분리는 실습 5에서 다룬다. 여기서는 current_part_id 만 쓴다.
    """
    p = out("session_state.json")
    if p.exists():
        return read_json(p)
    return {"current_part_id": part_id}


MODES = ("LIVE", "REVIEW", "MUTE")

# 모드는 **파일**에 둔다. 프로세스 인자로 두면 방송 중에 모드를 바꾸려고
# 프로세스를 재시작해야 하는데, 사고가 난 순간에 재시작은 할 수 없는 일이다.
# 파일이면 다음 발화가 알아서 새 모드를 읽는다.
MODE_FILE = "mode.json"


def load_mode() -> tuple[str, str]:
    """(모드, 출처). 읽을 수 없으면 REVIEW 로 떨어진다.

    ## 왜 파일이 깨졌을 때 LIVE 가 아닌가

    파일이 없는 것과 깨진 것은 다르다.

      없다   아직 모드를 설정한 적이 없다 → LIVE (로드맵 기본값)
      깨졌다 무언가 잘못됐다 → REVIEW

    깨진 상태에서 LIVE 로 떨어지면 **모르는 상태로 말하기 시작한다.**
    REVIEW 는 화면에는 띄우되 사람의 승인을 받으므로 틀려도 방송으로 나가지 않는다.
    실패의 기본 방향은 침묵 쪽이어야 한다.
    """
    p = out(MODE_FILE)
    if not p.exists():
        return "LIVE", "기본값 (모드 파일 없음)"
    try:
        m = read_json(p)
        mode = str(m.get("mode", "")).upper()
        if mode not in MODES:
            raise ValueError(mode)
        return mode, f"{MODE_FILE} ({m.get('reason') or '사유 미기재'})"
    except Exception as e:
        print(f"⚠ {MODE_FILE} 을 읽을 수 없습니다 ({type(e).__name__}). "
              f"REVIEW 로 내려갑니다 — 모르는 상태로 말하지 않는다.", file=sys.stderr)
        trace("06_render_output", ok=False, reason="mode_unreadable", fallback="REVIEW")
        return "REVIEW", "폴백 (모드 파일 손상)"


def set_mode(mode: str, reason: str) -> None:
    write_json(out(MODE_FILE), {"mode": mode, "reason": reason,
                                "changed_at": now_iso()})
    print(f"모드 → {mode}   사유: {reason}")
    print("   다음 발화부터 적용됩니다 (진행 중인 발화는 건드리지 않는다).")
    trace("06_render_output", ok=True, action="set_mode", mode=mode, reason=reason)


def approve_pending() -> int:
    """REVIEW 에서 대기 중인 발화를 승인해 내보낸다."""
    pend = out("spoken_pending.json")
    if not pend.exists():
        print("승인 대기 중인 발화가 없습니다.")
        return 2
    spoken = read_json(pend)
    write_json(out("spoken.json"), spoken)
    pend.unlink()
    print("승인 → spoken.json 으로 내보냈습니다")
    print(f"   {spoken['text'][:88]}")
    trace("06_render_output", ok=True, action="approve", chars=len(spoken["text"]))
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--live", required=True)
    ap.add_argument("--provider", help="TTS 프로바이더 강제 지정 (기본: M6 실측 기본값)")
    ap.add_argument("--set-mode", choices=MODES, help="운영 모드 전환 (렌더하지 않는다)")
    ap.add_argument("--reason", default="", help="--set-mode 의 사유. 남기지 않으면 "
                                                 "나중에 왜 내렸는지 알 수 없다")
    ap.add_argument("--approve", action="store_true",
                    help="REVIEW 에서 대기 중인 발화를 승인해 내보낸다")
    args = ap.parse_args()

    if args.set_mode:
        set_mode(args.set_mode, args.reason)
        return 0
    if args.approve:
        return approve_pending()

    verdict = read_json(out("verdict.json"))
    ctx = read_json(out(f"broadcast_context.{args.live}.json"))

    if not verdict["kept_sentences"]:
        trace("06_render_output", ok=False, reason="nothing_to_say",
              dropped=len(verdict["dropped_sentences"]))
        print("\n⛔ 발화할 문장이 남지 않았습니다 — 파일을 쓰지 않습니다.")
        print("   빈 텍스트로 화면을 갱신하거나 빈 문자열을 TTS 에 넘기지 않는다.")
        print("   말할 것이 없을 때는 침묵이 정답이다.")
        return 2

    state = load_session_state(ctx["current_part_id"])
    provider, voice = pick_voice(args.provider)
    mode, mode_src = load_mode()
    ts = now_iso()

    output = {
        "overlay": {
            "text": verdict["final_text"],
            "part_id": state.get("current_part_id") or ctx["current_part_id"],
            "updated_at": ts,
        },
        "spoken": {
            "text": verdict["final_text"],
            "provider": provider,
            "voice": voice,
            "audio_path": None,      # 합성은 M9 셸의 몫
            "spoken_at": ts,
        },
        "mode": mode,
        # LIVE 가 아니면 spoken 은 '계획'이지 '나간 것'이 아니다.
        # 이 구분을 남기지 않으면 사후에 무엇이 실제로 방송됐는지 알 수 없다.
        "spoken_withheld": mode != "LIVE",
        "source_verdict_pass": verdict["pass"],
    }
    validate_or_die("output", output, "06_render_output")

    p_out = write_json(out("output.json"), output)
    # OBS Browser Source 와 TTS 는 서로 다른 프로세스가 폴링한다.
    # 한 파일을 둘이 읽게 하면 한쪽 오류가 다른 쪽을 멈춘다 → 파일도 분리한다.
    #
    # 화면은 세 모드 모두에서 갱신한다. 진행자가 무엇을 말하려 했는지는
    # 보여야 승인도 하고 판단도 한다. 모드가 가르는 것은 **소리**다.
    p_ov = write_json(out("overlay.json"), output["overlay"])

    written = [p_out.name, p_ov.name]
    stale = out("spoken.json")
    if mode == "LIVE":
        written.append(write_json(stale, output["spoken"]).name)
    else:
        # ⚠️ 지난 발화의 spoken.json 이 남아 있으면 TTS 폴러가 그것을 다시 읽어
        #    **모드를 내렸는데 옛 발화가 나가는** 사고가 난다. 반드시 지운다.
        if stale.exists():
            stale.unlink()
        if mode == "REVIEW":
            written.append(write_json(out("spoken_pending.json"),
                                      output["spoken"]).name)

    kept, total = len(verdict["kept_sentences"]), \
        len(verdict["kept_sentences"]) + len(verdict["dropped_sentences"])
    print(f"\n── 렌더 완료 · verdict.pass={verdict['pass']} · {kept}/{total} 문장")
    print(f"   overlay  part={output['overlay']['part_id']}")
    print(f"   모드     {mode}  ← {mode_src}")
    print(f"   spoken   {provider} / {voice}"
          + ("" if mode == "LIVE" else "   (보류됨)"))
    if mode == "REVIEW":
        print("   ⏸ 발화 보류 — spoken_pending.json · "
              f"승인: python 06_render_output.py --live {args.live} --approve")
    elif mode == "MUTE":
        print("   🔇 발화 없음 — 화면만 갱신했습니다")
    print(f"   text     {verdict['final_text'][:88]}")
    if not verdict["pass"]:
        print(f"   ⚠ 부분 통과 발화 — source_verdict_pass=false 로 기록됨")
    trace("06_render_output", ok=True, provider=provider, voice=voice,
          part_id=output["overlay"]["part_id"], kept=kept, mode=mode,
          spoken_withheld=output["spoken_withheld"],
          source_verdict_pass=verdict["pass"], outputs=written)
    print(f"   → {' · '.join(written)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
