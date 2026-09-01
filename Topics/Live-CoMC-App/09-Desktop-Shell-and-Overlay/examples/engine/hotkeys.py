#!/usr/bin/env python3
"""M9 실습 2 — 글로벌 핫키.

## 왜 핫키인가

방송 중 진행자의 손은 키보드에 있다. 마우스로 창을 찾아 클릭하는 동작은
**말하면서 할 수 없다.** 파트 전환·모드 전환·패닉 스톱은 전부 한 손으로,
화면을 안 보고 눌러야 한다.

## 왜 라이브러리를 안 쓰는가

`keyboard` 나 `pynput` 을 흔히 쓰는데 이 환경에는 없다. 그런데 설치할 필요가 없다 —
**Win32 `RegisterHotKey` 가 더 맞는 도구다.**

| | `keyboard` 류 | `RegisterHotKey` |
|---|---|---|
| 동작 방식 | 전역 키보드 훅. **모든 키 입력을 가로챈다** | OS 에 조합을 등록. **그 조합만** 받는다 |
| 권한 | 관리자 권한이 필요할 때가 있다 | 불필요 |
| 부작용 | 훅이 죽으면 키 입력 전체가 영향받을 수 있다 | 없음 |
| 설치 | pip | **표준 라이브러리(ctypes)** |

방송 중에 도는 프로그램이 **모든 키 입력을 훔쳐보게** 만들 이유가 없다.
필요한 조합만 등록하는 쪽이 안전하다.

## 무엇을 지키는가 — M7 원칙

> `current_part_id` 는 **권위값**이다. 핫키·음성 명령·클릭으로만 바뀐다.
> 시간 추정치(`suggested_part_id`)가 여기에 대입되는 일은 없다.

이 파일은 파트 전환 시 반드시 `session_state.set_current_part(..., by="hotkey")`
를 거친다. **`current_part_id` 에 직접 대입하는 줄은 존재하지 않는다.**

## 핫키 배치

| 조합 | 동작 |
|---|---|
| `Ctrl+Alt+←` / `→` | 이전 / 다음 파트 |
| `Ctrl+Alt+1`~`9` | 해당 번호 파트로 직접 이동 |
| `Ctrl+Alt+L` / `R` / `M` | LIVE / REVIEW / MUTE 모드 |
| **`Ctrl+Alt+Space`** | **패닉 스톱** — 재생 중단 + MUTE |

`Ctrl+Alt` 조합만 쓴다. 방송 중 잘못 눌러도 다른 프로그램과 충돌하지 않는 조합이다.

실행:
    python hotkeys.py --live 21              # 대기
    python hotkeys.py --live 21 --selftest   # 키를 스스로 눌러 검증
"""
from __future__ import annotations

import argparse
import ctypes
import ctypes.wintypes as wt
import json
import sys
import threading
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
M7_SRC = HERE.parents[2] / "07-CoMC-Engine-POC" / "src"
if str(M7_SRC) not in sys.path:
    sys.path.insert(0, str(M7_SRC))

user32 = ctypes.windll.user32

MOD_ALT, MOD_CONTROL, MOD_NOREPEAT = 0x0001, 0x0002, 0x4000
WM_HOTKEY = 0x0312
VK = {"LEFT": 0x25, "RIGHT": 0x27, "SPACE": 0x20,
      "L": 0x4C, "R": 0x52, "M": 0x4D,
      **{str(i): 0x30 + i for i in range(1, 10)}}

MODES = ("LIVE", "REVIEW", "MUTE")

# ── 핫키 정의: id → (수식키, 가상키, 동작이름, 인자) ────────────────────
BINDINGS: dict[int, tuple[int, int, str, object]] = {}


def _register_all() -> list[str]:
    mod = MOD_CONTROL | MOD_ALT | MOD_NOREPEAT
    plan = [("part_prev", VK["LEFT"], None), ("part_next", VK["RIGHT"], None),
            ("panic", VK["SPACE"], None),
            ("mode", VK["L"], "LIVE"), ("mode", VK["R"], "REVIEW"),
            ("mode", VK["M"], "MUTE")]
    plan += [("part_set", VK[str(i)], str(i)) for i in range(1, 10)]

    failed = []
    for i, (action, vk, arg) in enumerate(plan, start=1):
        if user32.RegisterHotKey(None, i, mod, vk):
            BINDINGS[i] = (mod, vk, action, arg)
        else:
            failed.append(f"{action}({arg or ''}) vk=0x{vk:02X}")
    return failed


def _unregister_all():
    for i in list(BINDINGS):
        user32.UnregisterHotKey(None, i)


# ── 동작 ──────────────────────────────────────────────────────────────
class Actions:
    """핫키가 실제로 하는 일. 상태 파일만 만지고 오디오는 콜백으로 위임한다."""

    def __init__(self, live: str, on_panic=None):
        import session_state as ss
        self.ss = ss
        self.live = live
        self.on_panic = on_panic          # 재생 중단 콜백 (없으면 상태만 바꾼다)
        self.log: list[dict] = []
        try:
            self.state = ss.load()
        except Exception:
            self.state = ss.init_state(live, "1")
            ss.save(self.state)

    # ── 파트 ──
    def _parts(self) -> list[str]:
        """rundown_index 에서 파트 목록을 읽는다. 없으면 1~9 로 가정."""
        from common import out, read_json
        try:
            idx = read_json(out(f"rundown_index.{self.live}.json"))
            return [str(p["part_id"]) for p in idx.get("parts", [])] or \
                   [str(i) for i in range(1, 10)]
        except Exception:
            return [str(i) for i in range(1, 10)]

    def part_set(self, part_id: str):
        # ⚠️ 반드시 set_current_part 를 거친다 (M7 권위값 원칙)
        self.state = self.ss.set_current_part(self.state, part_id, by="hotkey")
        self.ss.save(self.state)
        self._note("part_set", part_id)

    def part_next(self, _=None):
        self._step(+1)

    def part_prev(self, _=None):
        self._step(-1)

    def _step(self, d: int):
        parts = self._parts()
        cur = str(self.state.get("current_part_id") or parts[0])
        i = parts.index(cur) if cur in parts else 0
        self.part_set(parts[max(0, min(len(parts) - 1, i + d))])

    # ── 모드 ──
    def mode(self, name: str, reason: str | None = None):
        import importlib.util
        if "stage06" in sys.modules:
            m = sys.modules["stage06"]
        else:
            spec = importlib.util.spec_from_file_location(
                "stage06", M7_SRC / "06_render_output.py")
            m = importlib.util.module_from_spec(spec)
            sys.modules["stage06"] = m
            spec.loader.exec_module(m)
        # ⚠️ 사유는 감사 기록이다. 패닉으로 들어온 MUTE 와 손으로 누른 MUTE 를
        #    구분할 수 없으면, 나중에 로그를 봐도 왜 꺼졌는지 알 수 없다.
        m.set_mode(name, reason=reason or f"핫키 (Ctrl+Alt+{name[0]})")
        self._note("mode", name)

    # ── 패닉 ──
    def panic(self, _=None):
        """재생 중단 + MUTE. **오디오를 먼저 끊는다.**"""
        t0 = time.perf_counter()
        if self.on_panic:
            try:
                self.on_panic()               # 스트림 abort — 가장 급한 것
            except Exception as e:
                self._note("panic_audio_error", str(e))
        self.mode("MUTE", reason="패닉 스톱 (Ctrl+Alt+Space)")   # 그다음 상태 전환
        self._note("panic", round((time.perf_counter() - t0) * 1000))

    def _note(self, action: str, arg):
        rec = {"t": time.time(), "action": action, "arg": arg}
        self.log.append(rec)
        print(f"  [{time.strftime('%H:%M:%S')}] {action} {arg}", flush=True)

    def dispatch(self, action: str, arg):
        getattr(self, action)(arg)


# ── 메시지 루프 ────────────────────────────────────────────────────────
def listen(actions: Actions, stop_after: float | None = None):
    msg = wt.MSG()
    t_end = time.time() + stop_after if stop_after else None
    while True:
        if t_end and time.time() > t_end:
            break
        # PeekMessage 로 논블로킹 — 타임아웃을 걸 수 있다
        if user32.PeekMessageW(ctypes.byref(msg), None, 0, 0, 1):
            if msg.message == WM_HOTKEY:
                hk = msg.wParam
                if hk in BINDINGS:
                    _, _, action, arg = BINDINGS[hk]
                    try:
                        actions.dispatch(action, arg)
                    except Exception as e:
                        print(f"  ⚠️ {action} 실패: {type(e).__name__}: {e}")
        else:
            time.sleep(0.005)


# ── 자기 검증 ──────────────────────────────────────────────────────────
def send_combo(vk: int):
    """Ctrl+Alt+<vk> 를 실제로 눌렀다 뗀다. 등록이 진짜 먹는지 확인용."""
    KEYUP = 0x0002
    for k in (0x11, 0x12, vk):                 # Ctrl, Alt, key
        user32.keybd_event(k, 0, 0, 0)
        time.sleep(0.01)
    for k in (vk, 0x12, 0x11):
        user32.keybd_event(k, 0, KEYUP, 0)
        time.sleep(0.01)


def selftest(live: str) -> int:
    from common import out, read_json
    print("\n=== 핫키 자기 검증 ===\n")
    failed = _register_all()
    print(f"  등록 {len(BINDINGS)}개" + (f" · 실패 {len(failed)}개: {failed}" if failed else ""))
    if not BINDINGS:
        print("  ⛔ 하나도 등록되지 않았습니다"); return 1

    acts = Actions(live)
    before_part = str(acts.state.get("current_part_id"))
    print(f"  시작 current_part_id = {before_part}\n")

    seq = [("Ctrl+Alt+2", VK["2"]), ("Ctrl+Alt+→", VK["RIGHT"]),
           ("Ctrl+Alt+←", VK["LEFT"]), ("Ctrl+Alt+R", VK["R"]),
           ("Ctrl+Alt+Space", VK["SPACE"])]

    def sender():
        time.sleep(0.4)
        for label, vk in seq:
            print(f"  ↳ 보냄 {label}")
            send_combo(vk)
            time.sleep(0.35)

    threading.Thread(target=sender, daemon=True).start()
    listen(acts, stop_after=0.4 + len(seq) * 0.35 + 0.8)
    _unregister_all()

    # ── 판정 ──
    print()
    ok = True
    got = [r["action"] for r in acts.log]
    expect = ["part_set", "part_set", "part_set", "mode", "panic"]
    hit = sum(1 for e in expect if e in got)
    print(f"  수신한 동작 {len(acts.log)}건: {got}")
    if hit < 3:
        print("  ❌ 핫키가 거의 전달되지 않았습니다"); ok = False

    st = read_json(out("session_state.json"))
    print(f"  session_state.current_part_id = {st.get('current_part_id')}")
    if st.get("current_part_id") == before_part and "part_set" in got:
        print("  ⚠️ 파트가 원래 값으로 돌아왔습니다 (→ 다음 → 이전 이면 정상)")

    try:
        md = read_json(out("mode.json"))
        print(f"  mode.json = {md.get('mode')}  (사유: {md.get('reason')})")
        if md.get("mode") != "MUTE":
            print("  ❌ 패닉 스톱 뒤 MUTE 가 아닙니다"); ok = False
    except Exception as e:
        print(f"  ❌ mode.json 을 읽을 수 없습니다: {e}"); ok = False

    # 권위값 원칙 확인 — set_current_part 를 거쳤는지
    changed_by = st.get("current_part_changed_by") or st.get("last_change_by")
    if changed_by:
        print(f"  변경 주체 = {changed_by}"
              + ("  ✅" if changed_by == "hotkey" else "  ⚠️ hotkey 가 아님"))

    print("\n  " + ("✅ 자기 검증 통과" if ok else "❌ 자기 검증 실패"))
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--live", default="21")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()

    if args.selftest:
        raise SystemExit(selftest(args.live))

    failed = _register_all()
    print(f"\n핫키 {len(BINDINGS)}개 등록"
          + (f" (실패 {len(failed)}: {failed})" if failed else ""))
    print("""
  Ctrl+Alt+← / →      이전 / 다음 파트
  Ctrl+Alt+1~9        해당 파트로 이동
  Ctrl+Alt+L / R / M  LIVE / REVIEW / MUTE
  Ctrl+Alt+Space      패닉 스톱

  Ctrl+C 로 종료
""")
    acts = Actions(args.live)
    try:
        listen(acts)
    except KeyboardInterrupt:
        pass
    finally:
        _unregister_all()
        print("\n핫키 해제됨")


if __name__ == "__main__":
    main()
