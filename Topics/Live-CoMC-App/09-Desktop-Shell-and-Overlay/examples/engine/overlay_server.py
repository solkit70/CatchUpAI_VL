#!/usr/bin/env python3
"""M9 실습 3 — OBS Browser Source 오버레이.

## 무엇을 하는가

⑥ 단계가 쓰는 `output/overlay.json` 을 방송 화면에 띄운다.

    06_render_output.py  →  overlay.json  →  [이 서버]  →  OBS Browser Source

## 왜 폴링이 아니라 SSE 인가

OBS Browser Source 는 Chromium 이다. 세 가지 방법이 있는데:

| 방식 | 문제 |
|---|---|
| `<meta refresh>` | 화면이 깜빡인다. 방송에 그대로 나간다 |
| JS 폴링 (setInterval) | 갱신 주기만큼 늦는다. 1초로 잡으면 최대 1초 지연 |
| **SSE (Server-Sent Events)** | **파일이 바뀐 즉시 밀어 넣는다.** 깜빡임 없음 |

발화 지연을 4.5초까지 깎아 놓고 오버레이에서 1초를 더 쓸 이유가 없다.

## 왜 WebSocket 이 아닌가

방향이 한쪽뿐이다 — 서버가 화면에 밀어 넣기만 하고, 화면은 아무것도 안 보낸다.
**SSE 는 그 한 방향만 하는 도구**이고 표준 HTTP 위에서 돈다. WebSocket 은
양방향이 필요할 때 쓴다. 지금은 아니다.

## 모드가 화면에 보여야 한다

`mode.json` 이 `MUTE` 면 **화면에도 그렇게 표시한다.** 진행자가 방송 화면만 보고도
지금 AI 가 꺼져 있는지 알 수 있어야 한다. 상태를 숨기면 "왜 대답을 안 하지" 하고
같은 질문을 반복하게 된다.

실행:
    python overlay_server.py                 # http://127.0.0.1:8777/
    python overlay_server.py --port 9000
    python overlay_server.py --selftest      # 사람 없이 검증

OBS 설정:
    소스 추가 → 브라우저
    URL          http://127.0.0.1:8777/
    너비 1920 · 높이 1080
    ☑ 보이지 않을 때 소스 종료
    ☑ 장면이 활성화될 때 브라우저 새로고침
"""
from __future__ import annotations

import argparse
import json
import queue
import sys
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

HERE = Path(__file__).resolve().parent
M7_SRC = HERE.parents[2] / "07-CoMC-Engine-POC" / "src"
if str(M7_SRC) not in sys.path:
    sys.path.insert(0, str(M7_SRC))

from common import out  # noqa: E402

OVERLAY = out("overlay.json")
MODE = out("mode.json")
SESSION = out("session_state.json")

_clients: set[queue.Queue] = set()
_clients_lock = threading.Lock()

PAGE = """<!doctype html>
<meta charset="utf-8">
<title>Co-MC Overlay</title>
<style>
  /* OBS 는 투명 배경을 지원한다. 방송 화면 위에 얹히므로 배경을 깔지 않는다. */
  html,body{margin:0;height:100%;background:transparent;overflow:hidden}
  #wrap{
    position:absolute; left:0; right:0; bottom:0;
    padding:48px 64px 56px;
    font-family:"Pretendard","Noto Sans KR",system-ui,sans-serif;
    /* 아래쪽만 어둡게 깔아 글자를 띄운다. 영상 위 어디에 놓아도 읽힌다 */
    background:linear-gradient(to top, rgba(8,12,20,.88) 0%, rgba(8,12,20,.72) 62%, rgba(8,12,20,0) 100%);
    opacity:0; transition:opacity .28s ease;
  }
  #wrap.on{opacity:1}
  #meta{display:flex;align-items:center;gap:14px;margin-bottom:14px}
  .chip{
    font-size:22px;font-weight:800;letter-spacing:.4px;
    padding:6px 16px;border-radius:999px;
    background:rgba(255,255,255,.14);color:#EAF2FF;
  }
  .chip.mute{background:#B4232A;color:#fff}
  .chip.review{background:#B7791F;color:#fff}
  #text{
    font-size:44px;line-height:1.44;font-weight:600;color:#fff;
    text-shadow:0 2px 10px rgba(0,0,0,.55);
    /* 너무 길면 잘라낸다 — 방송 화면을 다 덮으면 안 된다 */
    display:-webkit-box;-webkit-line-clamp:4;-webkit-box-orient:vertical;overflow:hidden;
  }
</style>
<div id="wrap"><div id="meta"></div><div id="text"></div></div>
<script>
const wrap=document.getElementById('wrap'),meta=document.getElementById('meta'),text=document.getElementById('text');
function render(d){
  if(!d || !d.text){ wrap.classList.remove('on'); return; }
  const m=(d.mode||'LIVE').toUpperCase();
  let chips = `<span class="chip">PART ${d.part_id ?? '-'}</span>`;
  if(m!=='LIVE') chips += `<span class="chip ${m.toLowerCase()}">${m}</span>`;
  meta.innerHTML=chips;
  text.textContent=d.text;
  wrap.classList.add('on');
}
const es=new EventSource('/events');
es.onmessage=e=>{ try{ render(JSON.parse(e.data)); }catch(_){} };
es.onerror=()=>{ /* OBS 가 소스를 껐다 켤 때 자동 재연결된다 */ };
</script>
"""


def snapshot() -> dict:
    """overlay.json + mode.json + session_state.json 을 합친 한 덩어리.

    ⚠️ **`part_id` 는 `session_state.json` 에서 읽는다.**
       `overlay.json` 의 `part_id` 는 *마지막 발화를 렌더할 때의* 값이라
       핫키로 파트를 바꿔도 갱신되지 않는다. M7 이 정한 권위값은
       `session_state.current_part_id` 이고, 화면은 권위값을 보여야 한다.

       이 구분을 놓치면 진행자가 파트를 넘겼는데 **화면은 이전 파트를
       계속 표시**한다 — 2026-08-31 실사용 검증에서 잡힌 결함이다.
    """
    d: dict = {}
    try:
        d = json.loads(OVERLAY.read_text(encoding="utf-8"))
    except Exception:
        d = {}
    try:
        d["mode"] = json.loads(MODE.read_text(encoding="utf-8")).get("mode", "LIVE")
    except Exception:
        d["mode"] = "LIVE"
    try:
        st = json.loads(SESSION.read_text(encoding="utf-8"))
        if st.get("current_part_id") is not None:
            d["part_id"] = str(st["current_part_id"])       # 권위값이 이긴다
    except Exception:
        pass
    return d


def watcher(interval: float = 0.2):
    """파일 mtime 을 보고 바뀌면 모든 클라이언트에 밀어 넣는다.

    ⚠️ 폴링이지만 **서버 안에서만** 폴링한다. 화면은 SSE 로 즉시 받는다.
       0.2초 간격이면 파일 변경 감지 지연이 최대 200ms 이고, 이건
       발화 지연 4.5초에 비하면 무시할 수 있다. watchdog 같은 의존성을
       하나 더 들이는 것보다 낫다.
    """
    last = None
    while True:
        try:
            sig = tuple(p.stat().st_mtime_ns if p.exists() else 0
                        for p in (OVERLAY, MODE, SESSION))
        except OSError:
            sig = None
        if sig != last:
            last = sig
            data = json.dumps(snapshot(), ensure_ascii=False)
            with _clients_lock:
                dead = []
                for q in _clients:
                    try:
                        q.put_nowait(data)
                    except queue.Full:
                        dead.append(q)
                for q in dead:
                    _clients.discard(q)
        time.sleep(interval)


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass                                   # 방송 중 콘솔을 더럽히지 않는다

    def do_GET(self):
        if self.path.startswith("/events"):
            self.send_response(200)
            self.send_header("Content-Type", "text/event-stream; charset=utf-8")
            self.send_header("Cache-Control", "no-cache")
            self.send_header("Connection", "keep-alive")
            self.end_headers()
            q: queue.Queue = queue.Queue(maxsize=8)
            with _clients_lock:
                _clients.add(q)
            try:
                # 접속하자마자 현재 상태를 한 번 준다 — 새로고침해도 화면이 빈칸이 아니도록
                self._send_event(json.dumps(snapshot(), ensure_ascii=False))
                while True:
                    try:
                        self._send_event(q.get(timeout=15))
                    except queue.Empty:
                        self.wfile.write(b": keepalive\n\n")   # 프록시 타임아웃 방지
                        self.wfile.flush()
            except (BrokenPipeError, ConnectionResetError):
                pass
            finally:
                with _clients_lock:
                    _clients.discard(q)
            return

        if self.path.startswith("/state"):     # 디버깅·검증용
            body = json.dumps(snapshot(), ensure_ascii=False).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return

        body = PAGE.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _send_event(self, data: str):
        self.wfile.write(f"data: {data}\n\n".encode("utf-8"))
        self.wfile.flush()


def serve(port: int, host: str = "127.0.0.1"):
    threading.Thread(target=watcher, daemon=True).start()
    srv = ThreadingHTTPServer((host, port), Handler)
    print(f"\n  오버레이 서버  http://{host}:{port}/")
    print(f"  감시 대상      {OVERLAY.name} · {MODE.name} · {SESSION.name}")
    print("""
  OBS 설정
    소스 추가 → 브라우저
    URL      http://127.0.0.1:%d/
    너비 1920 · 높이 1080
    ☑ 보이지 않을 때 소스 종료
    ☑ 장면이 활성화될 때 브라우저 새로고침

  Ctrl+C 로 종료
""" % port)
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        print("\n서버 종료")


# ── 자기 검증 ──────────────────────────────────────────────────────────
def selftest(port: int) -> int:
    import urllib.request
    print("\n=== 오버레이 서버 자기 검증 ===\n")
    ok = True

    def check(label, passed, detail=""):
        nonlocal ok
        ok &= passed
        print(f"  {'✅' if passed else '❌'} {label}" + (f"   {detail}" if detail else ""))

    threading.Thread(target=watcher, args=(0.1,), daemon=True).start()
    srv = ThreadingHTTPServer(("127.0.0.1", port), Handler)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    time.sleep(0.4)
    base = f"http://127.0.0.1:{port}"

    # 1. 페이지
    try:
        html = urllib.request.urlopen(base + "/", timeout=3).read().decode()
        check("HTML 페이지 서빙", "EventSource" in html, f"{len(html)}바이트")
    except Exception as e:
        check("HTML 페이지 서빙", False, f"{type(e).__name__}")

    # 2. 상태 스냅샷
    try:
        st = json.loads(urllib.request.urlopen(base + "/state", timeout=3).read())
        check("현재 상태 반환", "text" in st, f"part={st.get('part_id')} mode={st.get('mode')}")
    except Exception as e:
        check("현재 상태 반환", False, f"{type(e).__name__}")

    # 3. SSE 로 초기값이 오는가
    got: list[str] = []
    def reader():
        try:
            r = urllib.request.urlopen(base + "/events", timeout=8)
            for raw in r:
                line = raw.decode("utf-8").strip()
                if line.startswith("data: "):
                    got.append(line[6:])
                    if len(got) >= 2:
                        break
        except Exception:
            pass
    th = threading.Thread(target=reader, daemon=True); th.start()
    time.sleep(0.6)
    check("SSE 접속 시 초기 상태 수신", len(got) >= 1)

    # 4. 파일을 바꾸면 밀려 오는가
    original = OVERLAY.read_text(encoding="utf-8") if OVERLAY.exists() else None
    probe = "가드 검증용 문장 " + str(int(time.time()))
    try:
        OVERLAY.write_text(json.dumps(
            {"text": probe, "part_id": "9",
             "updated_at": time.strftime("%Y-%m-%dT%H:%M:%S")},
            ensure_ascii=False), encoding="utf-8")
        th.join(timeout=3)
        pushed = any(probe in g for g in got)
        check("파일 변경이 SSE 로 전달", pushed,
              f"수신 {len(got)}건" + ("" if pushed else " — 변경분 없음"))
    finally:
        if original is not None:
            OVERLAY.write_text(original, encoding="utf-8")
        else:
            OVERLAY.unlink(missing_ok=True)

    srv.shutdown()
    print("\n  " + ("✅ 전부 통과" if ok else "❌ 실패 항목 있음"))
    print("\n  ⚠️ OBS 에서 실제로 보이는지는 사람이 확인해야 한다 — "
          "브라우저 소스를 추가하고 화면을 봐야 한다")
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--port", type=int, default=8777)
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()
    if args.selftest:
        raise SystemExit(selftest(args.port))
    serve(args.port)


if __name__ == "__main__":
    main()
