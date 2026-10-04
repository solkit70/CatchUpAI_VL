#!/usr/bin/env python3
"""CoMC 콘솔 — 창 하나로 다 한다 (CVL 3, 2026-09-17).

창 4개(오버레이 서버 · 재생기 · 핫키 · 엔진)를 **프로세스 하나** 안에 스레드로 넣고,
브라우저 탭 하나(http://127.0.0.1:8778/)에서 상태 · 파트 · 모드 · 패닉 · 질문 · 결과 · 로그를 본다.
기존 모듈을 그대로 import 한다 — 새 로직은 없다. 검증된 코드 경로는 한 줄도 바꾸지 않는다(M9 원칙).

    ┌ comc_console.py ─────────────────────────────────────────────┐
    │  overlay_server  (8777, OBS Browser Source 가 보는 것)        │
    │  spoken_player   (spoken.json → CABLE Input)                  │
    │  hotkeys         (Ctrl+Alt+… 그대로 살아 있다)                │
    │  engine_daemon.Engine (①~⑥ 인프로세스)                        │
    │  콘솔 HTTP       (8778, 진행자가 보는 것)   ← 이 파일이 더한 것 │
    └───────────────────────────────────────────────────────────────┘

실행:
    python comc_console.py --live 28                 # 브라우저가 자동으로 열린다
    python comc_console.py --live 28 --no-browser

끝내기: 이 창에서 Ctrl+C. 전부 같이 꺼진다.
"""
from __future__ import annotations

import argparse
import io
import json
import subprocess
import sys
import threading
import time
import webbrowser
from contextlib import redirect_stderr
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse

HERE = Path(__file__).resolve().parent
TOPIC = HERE.parents[2]
M7_SRC = TOPIC / "07-CoMC-Engine-POC" / "src"
M10_EX = TOPIC / "10-Live-Rehearsal-Capstone" / "examples"
for p in (HERE, M7_SRC):
    if str(p) not in sys.path:
        sys.path.insert(0, str(p))

from common import clear_overlay, now_iso, out, read_json, write_json   # noqa: E402
import overlay_server                                     # noqa: E402
import spoken_player                                      # noqa: E402
import hotkeys                                            # noqa: E402
import engine_daemon                                      # noqa: E402
from viewer_store import ViewerStore                       # noqa: E402
from persona_store import PersonaStore                      # noqa: E402

LOG_MAX = 200


class _Router:
    """스레드별 stdout 라우터.

    `contextlib.redirect_stdout` 은 **프로세스 전체**의 sys.stdout 을 바꾼다. 재생기가 합성하는 3초 동안
    핫키·콘솔 스레드가 찍는 줄이 재생기 버퍼로 새어 들어가 「player  hotkey part_set 1」 같은 가짜 로그가
    났다 (CVL 3 실측). 그래서 sys.stdout 을 한 번만 이 라우터로 바꾸고, 스레드마다 `capture()` 로 자기
    버퍼를 켠다. 버퍼가 없는 스레드의 출력은 진짜 stdout 으로 간다.
    """
    def __init__(self, real):
        self.real = real
        self.tls = threading.local()

    def capture(self, buf):
        self.tls.buf = buf

    def release(self):
        self.tls.buf = None

    def write(self, s):
        buf = getattr(self.tls, "buf", None)
        return (buf if buf is not None else self.real).write(s)

    def flush(self):
        buf = getattr(self.tls, "buf", None)
        (buf if buf is not None else self.real).flush()

    def __getattr__(self, name):                 # encoding, isatty …
        return getattr(self.real, name)


class QuietServer(ThreadingHTTPServer):
    """브라우저가 자기 쪽에서 끊은 연결(탭 새로고침 · keep-alive 교체)을 트레이스백으로 찍지 않는다.

    9/17 실사용에서 `ConnectionAbortedError [WinError 10053]` 스택이 콘솔 창에 40줄 튀어 진행자가
    고장으로 읽었다. 앱과 무관한 소음이다. 그 밖의 예외는 그대로 찍는다 — 진짜 고장은 보여야 한다.
    """
    daemon_threads = True

    def handle_error(self, request, client_address):
        exc = sys.exc_info()[1]
        if isinstance(exc, (ConnectionAbortedError, ConnectionResetError, BrokenPipeError)):
            return
        super().handle_error(request, client_address)


ROUTER = _Router(sys.stdout)
sys.stdout = ROUTER


class _capture:
    """with _capture() as buf: … — 이 스레드의 print 만 buf 로 보낸다."""
    def __init__(self, buf=None):
        self.buf = buf if buf is not None else io.StringIO()

    def __enter__(self):
        ROUTER.capture(self.buf)
        return self.buf

    def __exit__(self, *a):
        ROUTER.release()
        return False


class Console:
    def __init__(self, live: str, device: str, tts: str | None, overlay_port: int = 8777):
        self.live = live
        self.overlay_port = overlay_port
        self.device_pat = device
        self.tts = tts
        self.log: list[dict] = []
        self.results: list[dict] = []
        self.busy = False
        self.playing = False
        self.lock = threading.Lock()
        self.request_lock = threading.Lock()
        self.preflight: dict | None = None
        self.viewers = ViewerStore()
        self.personas = PersonaStore()
        self.started = time.strftime("%H:%M:%S")          # 화면 표시용 — 현지 시각

    # ── 로그 ──
    def note(self, kind: str, text: str, **extra):
        from deny_terms import redact
        text, extra = redact(text), redact(extra)
        rec = {"ts": time.strftime("%H:%M:%S"), "kind": kind, "text": text, **extra}
        self.log.append(rec)
        del self.log[:-LOG_MAX]
        ROUTER.real.write(f"  [{rec['ts']}] {kind:<8} {text}" + chr(10)); ROUTER.real.flush()

    # ── 기동 ──
    def start(self):
        # 1) ①② — 오늘 Rundown · 현재 파트
        with _capture(), redirect_stderr(io.StringIO()):
            self.engine = engine_daemon.Engine()
            pre = self.engine.prewarm(self.live)
        if pre.get("ok"):
            msg = "prewarm ok"
        elif pre.get("failed_at") == "②":
            # 현재 파트의 커버리지가 미정이면 ② 가 설계대로 거절한다 — 고장이 아니라 「이 파트에서는 침묵」이다.
            # 「실패」라고 찍으니 진행자가 고장으로 읽었다 (9/17 실사용). 파트를 확정된 것으로 바꾸면 다음 질문 전에 다시 만든다.
            msg = f"현재 파트 커버리지 미정 → 이 파트에서는 침묵 (정상). 확정된 파트 버튼을 누르세요"
        else:
            msg = f"prewarm 실패 {pre}"
        self.note("engine", f"기동 {self.engine.warmup_ms}ms · {msg}")
        # 2) 오버레이 서버 (8777)
        threading.Thread(target=overlay_server.watcher, daemon=True).start()
        self.overlay_srv = QuietServer(("127.0.0.1", self.overlay_port), overlay_server.Handler)
        threading.Thread(target=self.overlay_srv.serve_forever, daemon=True).start()
        self.note("overlay", f"http://127.0.0.1:{self.overlay_port}/ (OBS Browser Source)")
        # 3) 재생기
        self.device = spoken_player.pick_device(self.device_pat)
        self.tts_name, self.prov = spoken_player.load_provider(self.tts)
        threading.Thread(target=self._player_loop, daemon=True).start()
        dev = spoken_player.sd.query_devices(self.device)["name"] if self.device is not None else "기본 출력"
        self.note("player", f"{self.tts_name}/{self.prov.voice} → {dev}")
        # 3-b) 캐주얼 브리프 — start_comc 가 만들어 둔다. 없으면 여기서 만든다 (날씨 조회 포함, 수 초)
        st = self.brief_status()
        if st:
            self.note("brief", f"근거 {st['n']}건 ({st['generated_at']} 생성) · 날씨 " + " / ".join(f"{c} {v}" for c, v in st["weather"].items()))
        else:
            self.build_brief()
        # 4) 핫키 — RegisterHotKey 는 메시지 루프와 같은 스레드여야 한다
        self.actions = hotkeys.Actions(self.live)
        threading.Thread(target=self._hotkey_loop, daemon=True).start()

    def _hotkey_loop(self):
        failed = hotkeys._register_all()
        self.note("hotkeys", f"{len(hotkeys.BINDINGS)}개 등록" + (f" · 실패 {failed}" if failed else ""))
        orig = self.actions._note
        def mirrored(action, arg):
            orig(action, arg)
            self.note("hotkey", f"{action} {arg}")
        self.actions._note = mirrored
        try:
            hotkeys.listen(self.actions)
        finally:
            hotkeys._unregister_all()

    def _player_loop(self):
        while True:
            try:
                self.playing = spoken_player.SPOKEN.exists() or spoken_player.SIGNOFF_REQ.exists()
                with _capture() as buf:
                    did = spoken_player.consume_signoff(self.device) or                         spoken_player.consume_one(self.prov, self.tts_name, self.device)
                if did:
                    for line in buf.getvalue().strip().splitlines():
                        self.note("player", line.strip())
            except Exception as e:
                self.note("player", f"오류 {type(e).__name__}: {str(e)[:120]}")
            finally:
                self.playing = False
            time.sleep(spoken_player.POLL_S)

    # ── 상태 ──
    def parts(self) -> list[dict]:
        p = out(f"rundown_index.{self.live}.json")
        if not p.exists():
            return []
        return [{"id": x["id"], "title": x["title"], "coverage": x["coverage_state"],
                 "items": len(x["coverage_items"])} for x in read_json(p)["parts"]]

    def state(self) -> dict:
        from deny_terms import status
        review = {}
        pending_path = out('spoken_pending.json')
        review_path = out('private') / 'm11' / 'review_sources.json'
        try:
            if pending_path.exists() and review_path.exists():
                candidate = read_json(review_path)
                if candidate.get('spoken_at') == read_json(pending_path).get('spoken_at'):
                    review = candidate
        except (OSError, ValueError):
            pass
        ss = read_json(out("session_state.json")) if out("session_state.json").exists() else {}
        mode = spoken_player.current_mode()
        ov = read_json(out("overlay.json")) if out("overlay.json").exists() else {}
        return {"live": self.live, "part": ss.get("current_part_id"), "parts": self.parts(),
                "mode": mode, "overlay": ov.get("text") or "",
                "pending": out("spoken_pending.json").exists(),
                "busy": self.busy, "playing": self.playing, "results": self.results[-12:][::-1], "log": self.log[-40:][::-1],
                "preflight": self.preflight, "started": self.started, "brief": self.brief_status(),
                "viewers": self.viewers.snapshot(self.live), "persona": self.personas.snapshot(self.live),
                "deny_terms": status(), "review_sources": review}

    # ── 동작 ──
    SIGNOFF_KEYS = ("끝인사", "마무리 인사", "시그니처", "마지막 인사")
    INTRO_KEYS = ("15개 국어", "15개국어", "15개 언어", "다국어 소개", "다국어로 소개", "여러 나라 말로", "다국어 인사")

    def signoff(self, set_name: str = "signoff") -> dict:
        """다국어 고정 대본 — 15개 언어 mp3 를 재생기가 순서대로 튼다 (LLM·게이트 없음, 패닉으로 중단).
        set_name: signoff(끝인사) · intro(방송 중간 자기소개 샘플)"""
        label = spoken_player.MULTILANG_SETS.get(set_name, set_name)
        sj = out("private") / f"{set_name}.json"
        if not sj.exists():
            self.note("multilang", f"⛔ {label} 대본 없음 — signoff_build.py --set {set_name}")
            return {"ok": False, "error": f"{set_name}.json 없음"}
        d = read_json(sj)
        write_json(spoken_player.SIGNOFF_REQ, {"requested_at": now_iso(), "by": "console", "set": set_name})
        self.note("multilang", f"{label} 시작 · {len(d['lines'])}개 언어 · 약 {d.get('total_seconds', '?')}초 (패닉으로 중단)")
        return {"ok": True, "set": set_name, "languages": len(d["lines"]), "seconds": d.get("total_seconds")}

    def ask(self, text: str, lane: str = "auto", viewer_records: list | None = None,
            viewer_scope: str = "current") -> dict:
        text = text.strip()
        if not text:
            return {"ok": False, "error": "빈 질문"}
        if any(k in text for k in self.INTRO_KEYS):
            self.busy = False
            return self.signoff("intro")
        if any(k in text for k in self.SIGNOFF_KEYS):
            self.busy = False
            return self.signoff()
        if not self.lock.acquire(blocking=False):
            return {"ok": False, "error": "이전 질문을 처리 중입니다"}
        self.busy = True
        try:
            self.note("ask", text)
            for f in ("verdict.json", "intent.json", "answer_draft.json"):
                if out(f).exists():
                    out(f).unlink()
            with _capture(), redirect_stderr(io.StringIO()):
                if viewer_records is None:
                    r = self.engine.utter(self.live, text, lane=lane)
                else:
                    r = self.engine.utter(self.live, text, lane='auto', viewer_records=viewer_records,
                                          viewer_scope=viewer_scope)
            it = read_json(out("intent.json")) if out("intent.json").exists() else {}
            vd = read_json(out("verdict.json")) if out("verdict.json").exists() else {}
            import evidence_lanes as lanes
            lc = read_json(lanes.CONTEXT) if lanes.CONTEXT.exists() else {}
            if lc.get("intent_fingerprint") != lanes.fingerprint(it):
                lc = {}
            ov = read_json(out("overlay.json")) if out("overlay.json").exists() else {}
            reason = None
            if not r.get("ok"):
                from deny_terms import matches
                if matches(text):
                    reason = '그 내용은 방송에서 다루지 않는 정보예요'
                # ④ 거절 사유는 trace 마지막 줄에 있다
                try:
                    lines = out("session_trace.jsonl").read_text(encoding="utf-8").strip().splitlines()[-6:]
                    for l in reversed(lines):
                        d = json.loads(l)
                        if d.get("stage") in ("04_compose_answer", "02_resolve_context") and d.get("ok") is False:
                            reason = reason or d.get("reason"); break
                except Exception:
                    pass
            from deny_terms import redact
            res = {"ts": time.strftime("%H:%M:%S"), "q": redact(text), "ok": bool(r.get("ok")),
                   "ms": r.get("total_ms"), "failed_at": r.get("failed_at"), "reason": reason,
                   "intent": it.get("intent"), "mode": "REVIEW" if lc else spoken_player.current_mode(),
                   "persona": it.get('slots', {}).get('persona', {}).get('name', '기본 코엠씨'),
                   "lane": lanes.LANES.get(lc.get("lane"), "📋 Rundown / 캐주얼"),
                   "sources": list(dict.fromkeys(e["path"] for e in lc.get("evidence_pool", []))),
                   "answer": ov.get("text") or "", "pass": vd.get("pass"),
                   "dropped": [d["reason"] for d in vd.get("dropped_sentences", [])],
                   "violations": [v["rule_id"] for v in vd.get("violations", [])]}
            self.results.append(res)
            del self.results[:-50]
            self.note("result", ("✅ " if res["ok"] else f"⛔ {res['failed_at']} {reason or ''} ") + (res["answer"][:60] or "(침묵)"))
            return {"ok": True, "result": res}
        finally:
            self.busy = False
            self.lock.release()

    def greet_viewers(self, ids=None, scope='selected', batch=0):
        batches = self.viewers.greeting_batch(self.live, ids, scope)
        if not isinstance(batch, int) or not 0 <= batch < len(batches):
            self.busy = False
            return {'ok': False, 'error': '인사할 이름을 선택해 주세요'}
        rows = batches[batch]
        # Historical names are never represented as current viewers or new comments.
        text = '기록에 있는 시청자분들께 감사 인사 해 주세요'
        result = self.ask(text, viewer_records=rows, viewer_scope='all' if scope == 'all' else 'current')
        result.update({'batch_count': len(batches), 'batch_index': batch})
        return result

    def set_part(self, pid: str):
        self.actions.part_set(pid)
        self.note("part", pid)

    def set_mode(self, mode: str):
        self.actions.mode(mode, reason=f"콘솔 버튼 ({mode})")

    def panic(self):
        self.actions.panic()

    def clear(self):
        """오버레이만 비운다 — 소리·모드는 건드리지 않는다. 진행자가 「자막 이제 치워」 할 때 (9/17 실사용 요청)."""
        clear_overlay("comc_console", "operator_clear")
        self.note("overlay", "화면 지움 (진행자)")

    def approve(self) -> dict:
        if self.busy:
            return {"ok": False, "message": "질문 처리 중입니다. 새 답변이 나온 뒤 승인해 주세요."}
        m = sys.modules.get("stage06") or engine_daemon.load_stage("06_render_output.py")
        with _capture() as buf:
            rc = m.approve_pending()
        msg = buf.getvalue().strip().splitlines()[0] if buf.getvalue().strip() else ""
        self.note("approve", msg)
        return {"ok": rc == 0, "message": msg}

    # ── CVL 4 캐주얼 브리프 (②-b) ──
    def brief_status(self) -> dict | None:
        bp = out("private") / f"casual_brief.{self.live}.json"
        if not bp.exists():
            return None
        b = read_json(bp)
        w = {c: (f"{x['sky']} {x['temp_c']}도" if x.get("ok") else "조회 실패") for c, x in (b.get("weather") or {}).items()}
        try:                                                     # ISO(UTC) → 현지 HH:MM
            import datetime as _dt
            gen = _dt.datetime.fromisoformat(b["generated_at"]).astimezone().strftime("%H:%M")
        except Exception:
            gen = ""
        return {"generated_at": gen, "n": len(b.get("evidence_pool", [])),
                "kinds": b.get("kinds", {}), "weather": w, "window": b.get("window", {})}

    def build_brief(self) -> dict:
        """②-b 를 서브프로세스로 돌린다 — 날씨를 새로 받고 오늘 기록을 다시 읽는다."""
        try:
            r = subprocess.run([sys.executable, str(M7_SRC / "02b_build_casual_brief.py"), "--live", self.live],
                               capture_output=True, text=True, encoding="utf-8", timeout=60,
                               env={**__import__("os").environ, "PYTHONUTF8": "1"})
            ok = r.returncode == 0
            tail = (r.stdout or r.stderr).strip().splitlines()[-2:]
        except Exception as e:
            ok, tail = False, [f"{type(e).__name__}: {str(e)[:120]}"]
        st = self.brief_status()
        self.note("brief", (f"근거 {st['n']}건 · 날씨 " + " / ".join(f"{c} {v}" for c, v in st["weather"].items()))
                  if ok and st else "⛔ 브리프 생성 실패: " + " ".join(tail))
        return {"ok": ok, "brief": st}

    def run_preflight(self) -> dict:
        try:
            r = subprocess.run([sys.executable, str(M10_EX / "preflight_check.py"), "--probe-live", "--json"],
                               capture_output=True, text=True, encoding="utf-8", timeout=120,
                               env={**__import__("os").environ, "PYTHONUTF8": "1"})
            txt = r.stdout.strip()
            data = json.loads(txt[txt.index("{"):]) if "{" in txt else {"raw": txt[-800:]}
        except Exception as e:
            data = {"error": f"{type(e).__name__}: {str(e)[:200]}"}
        checks = data.get("checks") or []
        cnt = {}
        for c in checks:
            cnt[c.get("status")] = cnt.get(c.get("status"), 0) + 1
        summary = " · ".join(f"{k} {v}" for k, v in cnt.items()) if checks else (data.get("error") or str(data)[:120])
        self.preflight = {"ts": time.strftime("%H:%M:%S"), "summary": summary,
                          "checks": [{"num": c.get("num"), "status": c.get("status"), "name": c.get("name"),
                                      "detail": (c.get("detail") or "")[:120]} for c in checks]}
        self.note("preflight", summary)
        return self.preflight

    def build_vault_index(self):
        import evidence_lanes as lanes
        if not self.lock.acquire(blocking=False):
            return {"ok": False, "error": "질문 처리 중입니다"}
        try:
            self.busy = True
            result = lanes.VaultIndex().build()
            self.note("index", f"볼트 색인 완료 · {result['files']}개 문서 · {result['chunks']}개 근거")
            return {"ok": True, **result}
        except Exception as exc:
            self.note("index", "색인 실패: " + type(exc).__name__)
            return {"ok": False, "error": type(exc).__name__}
        finally:
            self.busy = False
            self.lock.release()


HTML = r"""<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>CoMC 콘솔</title>
<meta name="viewport" content="width=device-width,initial-scale=1">
<style>
:root{--bg:#0f1720;--card:#16222d;--ink:#e6edf3;--dim:#8b9bab;--line:#243342;--live:#e03131;--review:#e8a33b;--mute:#6b7280;--ok:#2fb344}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:15px/1.5 "Malgun Gothic",system-ui,sans-serif}
.wrap{max-width:1180px;margin:0 auto;padding:16px}
.top{display:flex;gap:12px;align-items:center;flex-wrap:wrap;margin-bottom:12px}
.badge{padding:6px 14px;border-radius:999px;font-weight:700;letter-spacing:.04em}
.m-LIVE{background:var(--live)}.m-REVIEW{background:var(--review);color:#000}.m-MUTE{background:var(--mute)}
.grid{display:grid;grid-template-columns:1.4fr 1fr;gap:14px}@media(max-width:900px){.grid{grid-template-columns:1fr}}
.card{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:14px}
h2{font-size:14px;color:var(--dim);margin:0 0 10px;text-transform:uppercase;letter-spacing:.08em}
button{font:inherit;border:1px solid var(--line);background:#1f2d3a;color:var(--ink);border-radius:10px;padding:10px 14px;cursor:pointer}
button:hover{background:#27394a}button.on{outline:2px solid #fff}
button.live{background:var(--live)}button.review{background:var(--review);color:#000}button.mute{background:var(--mute)}
button.panic{background:#b91c1c;font-size:18px;font-weight:800;padding:16px;width:100%;margin-top:8px}
.row{display:flex;gap:8px;flex-wrap:wrap}
textarea{width:100%;font:inherit;background:#0b1118;color:var(--ink);border:1px solid var(--line);border-radius:10px;padding:10px;min-height:64px}
.send{background:#1d4ed8;font-weight:700}
.overlay{background:#000;border-radius:10px;padding:12px 14px;min-height:56px;font-size:18px;font-weight:700;text-shadow:0 2px 8px #000}
.res{border-top:1px solid var(--line);padding:8px 0}.res .q{color:var(--dim);font-size:13px}.res .a{margin-top:2px}
.res.bad .a{color:#f59e0b}.meta{color:var(--dim);font-size:12px}
.log{font:12px/1.5 Consolas,monospace;color:var(--dim);max-height:260px;overflow:auto;white-space:pre-wrap}
.part{padding:10px 14px}.part small{display:block;color:var(--dim);font-size:11px}
.pf{font-size:13px;color:var(--dim)}
input,select{font:inherit;background:#0b1118;color:var(--ink);border:1px solid var(--line);border-radius:8px;padding:8px}
.viewer-row{display:flex;gap:6px;align-items:center;flex-wrap:wrap;margin-top:6px}.viewer-row button{padding:5px 8px;font-size:12px}
#viewer-list,#all-viewers{max-height:280px;overflow:auto}.greeted{color:var(--ok)}
</style></head><body><div class="wrap">
<div class="top"><b style="font-size:18px">CoMC 콘솔 · Live #<span id="live"></span></b>
 <span id="persona-current" class="badge" style="background:#334155"></span>
 <span id="mode" class="badge"></span><span class="meta">파트 <b id="part"></b> · 시작 <span id="started"></span></span>
 <span id="busy" class="meta"></span></div>
<div class="grid">
<div>
 <div class="card"><h2>오버레이 (시청자가 보는 것) <button id="clear" style="float:right;padding:4px 10px;font-size:13px" onclick="post('/api/clear')">화면 지우기</button></h2><div id="overlay" class="overlay"></div></div>
 <div class="card" style="margin-top:14px"><h2>질문 — Enter 로 보내기 (Shift+Enter 줄바꿈)</h2>
  <textarea id="q" placeholder="오늘 2부에서 뭘 다루나요?"></textarea>
  <div class="row"><label for="quick-mode">퀵 버튼:</label><select id="quick-mode"><option value="draft">질문란에 채우기 → 수정 후 Enter</option><option value="send">즉시 전송</option></select></div>
  <div id="question-message" class="meta" role="status" aria-live="polite"></div>
  <div class="row" style="margin-top:8px"><label for="lane">답변 근거:</label><select id="lane"><option value="auto">자동 · Rundown → 볼트 → 웹</option><option value="rundown">📋 Rundown</option><option value="vault">🗂️ 지난 볼트 기록</option><option value="web">🌐 공개 웹 검색</option><option value="creative">🎭 가상 이야기</option></select><button onclick="post('/api/vault-index')">볼트 색인 갱신</button></div>
  <div class="meta">볼트·웹·창작 답변은 화면에서 확인한 뒤 「대기 발화 승인」을 누르면 소리로 나갑니다.</div>
  <div class="row" style="margin-top:8px"><button class="send" onclick="ask()">보내기</button>
   <button onclick="quick('오늘 '+PART+'부에서 뭘 다루나요?')">이 파트 뭐 다뤄요?</button>
   <button onclick="quick(PART+'부 첫 항목이 뭐죠?')">첫 항목이 뭐죠?</button>
   <button id="approve" onclick="post('/api/approve')">대기 발화 승인 → 소리</button>
   <div id="review-warning" role="alert" style="display:none;color:#ffce58;font-weight:bold;border:2px solid #ffce58;padding:10px"></div></div>
  <div id="deny-status" class="meta"></div>
  <div class="row" style="margin-top:8px"><span class="meta" style="align-self:center">코엠씨 캐주얼:</span>
   <button onclick="quick('오늘 서울이랑 시애틀 날씨는 어때요?')">날씨</button>
   <button onclick="quick('이번 주에 뭘 했어요?')">이번 주 한 일</button>
   <button onclick="quick('이번 주 인사이트가 뭐예요?')">인사이트</button>
   <button onclick="quick('잠깐 물 마시고 올게요. 그동안 시청자분들께 재미있는 얘기 해 주세요')">잠깐 자리 비움 (≈50초)</button>
   <button onclick="quick('잠깐 볼일 보고 올게요. 시청자분들께 지금까지 한 일과 앞으로 남은 일을 설명해 주세요')">지금까지·남은 일 (≈50초)</button>
   <button onclick="$('viewer-name').focus();$('viewer-name').scrollIntoView({block:'center'})">시청자 명단에 추가</button>
   <button onclick="if(confirm('15개 국어 자기소개 샘플 — 약 2분. 시작할까요?'))post('/api/signoff',{set:'intro'})">🌏 15개 국어 자기소개 (샘플)</button>
   <button onclick="if(confirm('시그니처 끝인사 — 15개 언어, 약 2분 16초. 시작할까요?'))post('/api/signoff',{set:'signoff'})">🌏 시그니처 끝인사 (2:16)</button></div>
  <div class="meta" style="margin-top:6px">영어로 듣고 싶으면 질문 끝에 「영어로 답해 주세요」를 붙이면 영어 목소리로 나갑니다</div></div>
 <div class="card" style="margin-top:14px"><h2>결과</h2><div id="results"></div></div>
</div>
<div>
 <div class="card"><h2>모드</h2><div class="row">
  <button class="review" onclick="setMode('REVIEW')">REVIEW · 화면만</button>
  <button class="live" onclick="setMode('LIVE')">LIVE · 소리</button>
  <button class="mute" onclick="setMode('MUTE')">MUTE</button></div>
  <button class="panic" onclick="post('/api/panic')">■ 패닉 — 지금 말하는 것 끊기</button>
  <div class="meta" style="margin-top:6px">핫키: <b>Ctrl+Alt+Space = 패닉</b> · Ctrl+Alt+L/R/M = 모드 · Ctrl+Alt+1~9 = 파트 · <b>Space 만 누르면 안 됩니다</b> (마지막에 누른 버튼이 다시 눌려요)</div></div>
 <div class="card" style="margin-top:14px"><h2>AI 코엠씨 · Persona</h2>
  <select id="persona-select" aria-label="Persona 선택" onchange="selectPersona()"></select>
  <button style="margin-top:8px" onclick="personaIntro()">선택한 캐릭터 자기소개</button>
  <div id="persona-detail" class="meta" style="margin-top:8px"></div><div id="persona-message" class="meta" role="status"></div>
  <details style="margin-top:8px"><summary>이번 회차 사용 기록 · 반응 메모</summary><div id="persona-history" class="meta" style="white-space:pre-wrap;max-height:180px;overflow:auto"></div>
   <textarea id="persona-notes" aria-label="시청자 반응 메모" placeholder="진행자가 남기는 반응 메모 · 비공개 저장" maxlength="2000" oninput="PERSONA_NOTES_DIRTY=true"></textarea><button onclick="savePersonaNotes()">메모 저장</button></details>
 </div>
 <div class="card" style="margin-top:14px"><h2>파트</h2><div id="parts" class="row"></div></div>
 <div class="card" style="margin-top:14px"><h2>시청자 · 이번 회차 참여 기록</h2>
  <div class="row"><input id="viewer-date" type="date" aria-label="방송 날짜"><button onclick="viewerPost('/api/viewers/date',{date:$('viewer-date').value})">방송 날짜 저장</button></div>
  <div class="row" style="margin-top:8px"><input id="viewer-name" placeholder="표시 이름 · 여러 명은 쉼표" aria-label="시청자 표시 이름" style="flex:1;min-width:160px"><button onclick="addViewers()">추가</button></div>
  <div class="meta">진행자가 직접 등록합니다. 날짜를 확인해 주세요. ✓는 소리 재생 완료입니다.</div>
  <div id="viewer-list"></div>
  <div class="row" style="margin-top:8px"><button onclick="prepareGreetings('selected')">선택한 분께 인사</button><button onclick="prepareGreetings('ungreeted')">아직 인사 안 한 분 모두</button></div>
  <div id="greeting-batches" class="row" style="margin-top:8px"></div><div id="viewer-message" class="meta" role="status"></div>
  <details style="margin-top:10px"><summary>전체 참여자 · 연말 인사</summary><div id="all-viewers"></div><button onclick="prepareGreetings('all')">전체 감사 인사 준비</button></details>
 </div>
 <div class="card" style="margin-top:14px"><h2>캐주얼 브리프 (이번 주 기록 · 날씨) <button style="float:right;padding:4px 10px;font-size:13px" onclick="post('/api/brief')">다시 만들기</button></h2><div id="brief" class="pf">없음 — 「다시 만들기」</div></div>
 <div class="card" style="margin-top:14px"><h2>프리플라이트</h2><div class="row"><button onclick="post('/api/preflight')">지금 점검</button></div><div id="pf" class="pf"></div></div>
 <div class="card" style="margin-top:14px"><h2>로그</h2><div id="log" class="log"></div></div>
</div></div></div>
<script>
const $=id=>document.getElementById(id);let PART='1';
const plabel=id=>/^\d+$/.test(id)?id+'부':id;
const COV={defined:'확정',directive:'지시',undefined:'미정'};
async function post(u,b){const r=await fetch(u,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(b||{})});return r.json();}
function setMode(m){post('/api/mode',{mode:m});}
const QUICK_MODE_KEY='comc.quickMode';
try{if(localStorage.getItem(QUICK_MODE_KEY)==='send')$('quick-mode').value='send';}catch(e){}
$('quick-mode').addEventListener('change',()=>{try{localStorage.setItem(QUICK_MODE_KEY,$('quick-mode').value);}catch(e){}});
function quick(t){const q=$('q');q.value=t;if($('quick-mode').value==='send'){ask();}else{q.focus();q.setSelectionRange(q.value.length,q.value.length);$('question-message').textContent='질문을 확인·수정한 뒤 Enter 또는 「보내기」를 눌러 주세요.';}}
let VIEWERS=null, SELECTED=new Set(), VIEWER_SIGNATURE='';
let PERSONA_OPTIONS='',PERSONA_NOTES_DIRTY=false;
async function personaIntro(){const r=await post('/api/ask',{text:'코엠씨 자기소개 해 주세요',lane:'auto'});$('persona-message').textContent=r.error||(r.ok?'자기소개 생성 중 — REVIEW에서는 대기 발화를 승인해 주세요.':'생성하지 못했습니다');}
async function selectPersona(){try{const r=await post('/api/persona',{id:$('persona-select').value});$('persona-message').textContent=r.error||(r.ok?'다음 답변부터 적용됩니다.':'변경하지 못했습니다');await tick();}catch(e){$('persona-message').textContent='연결 오류 — 다시 시도해 주세요';}}
async function savePersonaNotes(){try{const r=await post('/api/persona/notes',{notes:$('persona-notes').value});$('persona-message').textContent=r.error||(r.ok?'반응 메모를 저장했습니다.':'저장하지 못했습니다');if(r.ok)PERSONA_NOTES_DIRTY=false;await tick();}catch(e){$('persona-message').textContent='연결 오류 — 다시 시도해 주세요';}}
function renderPersona(p){const sig=JSON.stringify(p.options);if(sig!==PERSONA_OPTIONS){PERSONA_OPTIONS=sig;$('persona-select').replaceChildren();for(const r of p.options){const o=document.createElement('option');o.value=r.id;o.textContent=r.name;$('persona-select').append(o);}}
 const r=p.current;$('persona-select').value=r.id;$('persona-current').textContent='AI · '+r.name;
 $('persona-detail').textContent=(r.speech==='casual'?'편한 반말':'존댓말')+' · '+(r.age?'가상 설정 '+r.age+'세 · ':'')+r.background+' · '+r.style;
 $('persona-history').textContent=p.history.map(e=>new Date(e.at).toLocaleTimeString()+' · '+({selected:'선택',rendered:'답변 생성',played:'재생 완료'}[e.event]||e.event)+' · '+(e.name||e.persona_id)+(e.mode?' · '+e.mode:'')).join('\n');
 if(!PERSONA_NOTES_DIRTY&&document.activeElement!==$('persona-notes'))$('persona-notes').value=p.notes||'';}
async function viewerPost(url,body){try{const r=await post(url,body);$('viewer-message').textContent=r.error||(r.ok?'저장했습니다':'처리하지 못했습니다');await tick();return r;}catch(e){$('viewer-message').textContent='연결 오류 — 다시 시도해 주세요';return {ok:false};}}
async function addViewers(){const names=$('viewer-name').value.trim();if(!names)return;const r=await viewerPost('/api/viewers/add',{names});if(r.ok)$('viewer-name').value='';}
$('viewer-name').addEventListener('keydown',e=>{if(e.key==='Enter'){e.preventDefault();addViewers();}});
function renderViewers(v){VIEWERS=v;const sig=JSON.stringify(v);if(sig===VIEWER_SIGNATURE)return;VIEWER_SIGNATURE=sig;
 if(document.activeElement!==$('viewer-date'))$('viewer-date').value=v.date;
 const valid=new Set(v.current.map(r=>r.id));SELECTED=new Set([...SELECTED].filter(i=>valid.has(i)));
 $('viewer-list').replaceChildren();
 for(const r of v.current){const row=document.createElement('div');row.className='viewer-row';
 const chip=document.createElement('button');chip.textContent=(r.greeted_at?'✓ ':'')+r.name;chip.className=(SELECTED.has(r.id)?'on ':'')+(r.greeted_at?'greeted':'');chip.setAttribute('aria-pressed',String(SELECTED.has(r.id)));chip.onclick=()=>{if(SELECTED.has(r.id))SELECTED.delete(r.id);else SELECTED.add(r.id);VIEWER_SIGNATURE='';renderViewers(VIEWERS);};row.append(chip);
 const meta=document.createElement('span');meta.className='meta';meta.textContent=`${r.count}회 참여`+(r.previous_count?' · 다시 온 분':'')+(r.pronunciation?' · 읽기: '+r.pronunciation:'');row.append(meta);
 for(const [label,action] of [['수정',()=>editViewer(r)],['이번 회차 삭제',()=>deleteViewer(r,false)],['전체 기록 삭제',()=>deleteViewer(r,true)]]){const b=document.createElement('button');b.textContent=label;b.onclick=action;row.append(b);}$('viewer-list').append(row);}
 if(!v.current.length)$('viewer-list').textContent='등록된 시청자가 없습니다.';
 $('all-viewers').textContent=v.all.map(r=>`${r.name} · ${r.count}회 · 처음 #${r.first_live} · 마지막 #${r.last_live}`).join('\n');$('all-viewers').style.whiteSpace='pre-wrap';}
async function editViewer(r){const name=prompt('표시 이름 수정 (모든 회차 기록에 반영)',r.name);if(name===null)return;const pronunciation=prompt('읽는 법 (비우면 표시 이름 그대로 읽기)',r.pronunciation||'');if(pronunciation===null)return;await viewerPost('/api/viewers/edit',{id:r.id,name,pronunciation});}
async function deleteViewer(r,everywhere){if(!confirm(r.name+(everywhere?'의 모든 회차 기록을 삭제할까요?':'을 이번 회차에서 삭제할까요?')))return;SELECTED.delete(r.id);await viewerPost('/api/viewers/delete',{id:r.id,everywhere});}
async function prepareGreetings(scope){const r=await post('/api/viewers/batches',{scope,ids:scope==='selected'?[...SELECTED]:null});$('greeting-batches').replaceChildren();if(!r.ok||!r.batches.length){$('viewer-message').textContent=r.error||'인사할 분이 없습니다.';return;}
 $('viewer-message').textContent='아래 묶음을 하나씩 눌러 인사하세요. REVIEW에서는 대기 발화를 승인해 주세요.';
 r.batches.forEach((batch,i)=>{const b=document.createElement('button');b.textContent=`${i+1}/${r.batches.length}: `+batch.map(x=>x.name).join(', ');b.onclick=async()=>{if(b.disabled)return;b.disabled=true;try{const res=await post('/api/viewers/greet',{scope:scope==='all'?'all':'selected',ids:batch.map(x=>x.id)});if(!res.ok){b.disabled=false;$('viewer-message').textContent=res.error;}else $('viewer-message').textContent='인사 생성 중 — 결과·승인 대기를 확인해 주세요';}catch(e){b.disabled=false;$('viewer-message').textContent='연결 오류 — 다시 시도해 주세요';}};$('greeting-batches').append(b);});}
let ASK_SENDING=false;
async function ask(){const q=$('q'),original=q.value,t=original.trim();if(!t||ASK_SENDING)return;ASK_SENDING=true;$('question-message').textContent='전송 중…';try{const r=await post('/api/ask',{text:t,lane:$('lane').value});if(r.ok){if(q.value===original)q.value='';$('busy').textContent='… 생각 중';$('question-message').textContent='질문을 전송했습니다.';}else{$('question-message').textContent=r.error||'전송하지 못했습니다. 질문을 확인한 뒤 다시 보내 주세요.';}}catch(e){$('question-message').textContent='연결 오류 — 질문을 유지했습니다. 다시 보내 주세요.';}finally{ASK_SENDING=false;}}
$('q').addEventListener('keydown',e=>{if(e.key==='Enter'&&!e.shiftKey&&!e.isComposing&&e.keyCode!==229){e.preventDefault();ask();}});
// 9/26 리허설 사고: 버튼을 누른 뒤 포커스가 남아 Space 한 번에 그 버튼이 다시 눌렸다(15개 국어 샘플 재시작 확인 창). 날씨 같은 확인 없는 버튼이면 바로 말을 시작한다.
// 버튼은 누르는 즉시 포커스를 놓고, 버튼 위의 Space·Enter 는 무시한다. 패닉은 Ctrl+Alt+Space(전역 핫키) 또는 빨간 버튼.
document.addEventListener('click',e=>{const b=e.target.closest('button');if(b)setTimeout(()=>b.blur(),0);},true);
document.addEventListener('keydown',e=>{if((e.key===' '||e.key==='Enter')&&e.target.tagName==='BUTTON'){e.preventDefault();e.stopPropagation();}},true);
function esc(s){return (s||'').replace(/[&<>]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;'}[c]));}
async function tick(){try{const s=await (await fetch('/api/state')).json();
 $('live').textContent=s.live;PART=s.part||'1';$('part').textContent=plabel(PART);$('started').textContent=s.started||'';
 const m=$('mode');m.textContent=s.mode;m.className='badge m-'+s.mode;
 $('busy').textContent=s.busy?'… 생각 중 (약 5초)':'';
 $('overlay').textContent=s.overlay||'(비어 있음 — 침묵)';$('clear').style.visibility=s.overlay?'visible':'hidden';
 $('approve').style.display=s.pending?'':'none';
 const dr=s.deny_terms||{};$('deny-status').textContent='금칙 목록 '+(dr.count||0)+'개 로드'+(dr.warning?' · ⚠ 목록을 읽을 수 없어 빈 목록으로 진행':'');
 const rw=s.review_sources||{};const warn=$('review-warning');warn.style.display=s.pending&&rw.personal_record?'':'none';
 warn.innerHTML=rw.personal_record?'⚠️ 개인 기록(Journal · Roundup)에서 온 답입니다 — 내용을 확인하고 승인하세요<br><span style="font-weight:normal">'+(rw.sources||[]).map(esc).join('<br>')+'</span>':'';
 if(s.viewers)renderViewers(s.viewers);
 if(s.persona)renderPersona(s.persona);
 $('parts').innerHTML=s.parts.map(p=>`<button class="part ${p.id==s.part?'on':''}" onclick="post('/api/part',{id:'${p.id}'})">${esc(plabel(p.id))}<small>${esc(p.title)} · ${COV[p.coverage]||p.coverage} ${p.items}</small></button>`).join('');
 $('results').innerHTML=s.results.map(r=>`<div class="res ${r.ok?'':'bad'}"><div class="q">${r.ts} · ${esc(r.q)} <span class="meta">${r.ok?r.ms+'ms':'⛔ '+(r.failed_at||'')+' '+(r.reason||'')} · ${r.mode||''} · ${esc(r.lane||'')} · ${esc(r.persona||'')}</span></div><div class="a">${r.ok?esc(r.answer):'(침묵 — '+(r.reason||r.failed_at||'')+')'}</div><div class="meta">${(r.sources||[]).map(esc).join('<br>')}</div>${r.violations&&r.violations.length?'<div class="meta">게이트: '+r.violations.join(', ')+'</div>':''}</div>`).join('');
 $('log').textContent=s.log.map(l=>`${l.ts} ${l.kind.padEnd(8)} ${l.text}`).join('\n');
 if(s.brief){const b=s.brief;$('brief').innerHTML='근거 <b>'+b.n+'</b>건 · '+esc(b.window.from+'~'+b.window.to)+' · '+esc(b.generated_at)+' 생성<br>'+Object.entries(b.weather).map(([c,v])=>esc(c+' '+v)).join(' · ')+'<br><span class="meta">'+esc(Object.entries(b.kinds).map(([k,v])=>k+' '+v).join(' · '))+'</span>';}
 if(s.preflight){const p=s.preflight;$('pf').innerHTML='<b>'+esc(p.ts+' · '+p.summary)+'</b>'+(p.checks||[]).map(c=>`<div>${esc(c.status)} ${c.num}. ${esc(c.name)} <span class="meta">${esc(c.detail)}</span></div>`).join('');}
}catch(e){}}
setInterval(tick,1000);tick();
</script></body></html>"""


def make_handler(con: Console):
    class H(BaseHTTPRequestHandler):
        def log_message(self, *a):
            pass

        def _json(self, data, code=200):
            b = json.dumps(data, ensure_ascii=False).encode("utf-8")
            self.send_response(code)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(b)))
            self.end_headers()
            self.wfile.write(b)

        def do_GET(self):
            path = urlparse(self.path).path
            if path == "/api/state":
                return self._json(con.state())
            b = HTML.encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(b)))
            self.end_headers()
            self.wfile.write(b)

        def do_POST(self):
            path = urlparse(self.path).path
            n = int(self.headers.get("Content-Length") or 0)
            body = json.loads(self.rfile.read(n) or b"{}") if n else {}
            try:
                if path == '/api/persona':
                    persona = con.personas.select(con.live, body.get('id'))
                    con.note('persona', persona['current']['name'] + ' · 다음 답변부터 적용')
                    return self._json({'ok': True, 'persona': persona})
                if path == '/api/persona/notes':
                    return self._json({'ok': True, 'persona': con.personas.note_episode(con.live, body.get('notes', ''))})
                if path == '/api/viewers/add':
                    return self._json({'ok': True, 'viewers': con.viewers.add(con.live, body.get('names', ''))})
                if path == '/api/viewers/date':
                    return self._json({'ok': True, 'viewers': con.viewers.set_date(con.live, body.get('date', ''))})
                if path == '/api/viewers/edit':
                    return self._json({'ok': True, 'viewers': con.viewers.edit(con.live, body.get('id'), body.get('name'), body.get('pronunciation', ''))})
                if path == '/api/viewers/delete':
                    return self._json({'ok': True, 'viewers': con.viewers.delete(con.live, body.get('id'), body.get('everywhere') is True)})
                if path == '/api/viewers/batches':
                    return self._json({'ok': True, 'batches': con.viewers.greeting_batch(con.live, body.get('ids'), body.get('scope', 'selected'))})
                if path == '/api/viewers/greet':
                    with con.request_lock:
                        if con.busy or con.playing or out('spoken_pending.json').exists() or out('spoken.json').exists():
                            return self._json({'ok': False, 'error': '이전 발화를 처리·승인한 뒤 다음 묶음을 눌러 주세요'}, 409)
                        batches = con.viewers.greeting_batch(con.live, body.get('ids'), body.get('scope', 'selected'))
                        if len(batches) != 1:
                            return self._json({'ok': False, 'error': '인사 준비에서 한 묶음을 선택해 주세요'}, 400)
                        con.busy = True
                        threading.Thread(target=con.greet_viewers, args=(body.get('ids'), body.get('scope', 'selected')), daemon=True).start()
                    return self._json({'ok': True, 'queued': True})
                if path == "/api/ask":
                    with con.request_lock:
                        if con.busy:
                            return self._json({'ok': False, 'error': '이전 질문을 처리 중입니다'}, 409)
                        if not str(body.get('text', '')).strip():
                            return self._json({'ok': False, 'error': '빈 질문'}, 400)
                        # ask owns its engine lock; the reservation closes the thread-start race.
                        con.busy = True
                        threading.Thread(target=con.ask, args=(body.get("text", ""), body.get("lane", "auto")), daemon=True).start()
                    return self._json({"ok": True, "queued": True})
                if path == "/api/part":
                    con.set_part(str(body.get("id"))); return self._json({"ok": True})
                if path == "/api/mode":
                    con.set_mode(str(body.get("mode", "REVIEW")).upper()); return self._json({"ok": True})
                if path == "/api/panic":
                    con.panic(); return self._json({"ok": True})
                if path == "/api/clear":
                    con.clear(); return self._json({"ok": True})
                if path == "/api/signoff":
                    return self._json(con.signoff(str(body.get("set") or "signoff")))
                if path == "/api/brief":
                    threading.Thread(target=con.build_brief, daemon=True).start()
                    return self._json({"ok": True, "queued": True})
                if path == "/api/vault-index":
                    threading.Thread(target=con.build_vault_index, daemon=True).start()
                    return self._json({"ok": True, "queued": True})
                if path == "/api/approve":
                    return self._json(con.approve())
                if path == "/api/preflight":
                    threading.Thread(target=con.run_preflight, daemon=True).start()
                    return self._json({"ok": True, "queued": True})
                return self._json({"ok": False, "error": "unknown"}, 404)
            except ValueError as e:
                return self._json({'ok': False, 'error': str(e)}, 400)
            except Exception as e:
                con.note("error", f"{path} {type(e).__name__}: {str(e)[:160]}")
                return self._json({"ok": False, "error": str(e)[:200]}, 500)
    return H


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--live", default="28")
    ap.add_argument("--port", type=int, default=8778)
    ap.add_argument("--device", default="CABLE Input", help="재생 출력 장치 (이름 일부)")
    ap.add_argument("--tts", help="TTS 프로바이더 (기본: 레지스트리)")
    ap.add_argument("--overlay-port", type=int, default=8777, help="OBS 가 보는 포트 — 방송에서는 바꾸지 않는다 (테스트용)")
    ap.add_argument("--no-browser", action="store_true")
    args = ap.parse_args()

    print(f"\n=== CoMC 콘솔 · Live #{args.live} ===")
    con = Console(args.live, args.device, args.tts, overlay_port=args.overlay_port)
    con.start()
    srv = QuietServer(("127.0.0.1", args.port), make_handler(con))
    url = f"http://127.0.0.1:{args.port}/"
    con.note("console", url)
    print(f"\n  콘솔  {url}\n  오버레이(OBS)  http://127.0.0.1:8777/\n  Ctrl+C 로 전부 종료\n")
    if not args.no_browser:
        threading.Timer(0.8, lambda: webbrowser.open(url)).start()
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        print("\n종료")
    return 0


if __name__ == "__main__":
    sys.exit(main())
