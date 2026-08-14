# -*- coding: utf-8 -*-
"""8·15 광복절 기념식 박창수 5분 발표 슬라이드 HTML 생성.

재생성 방법:
    python build-slides.py     # slides.html 생성
    python build-pdf.py        # out/20260815-박창수-발표.pdf 생성

의존 자산:
  - _files_/qr-honorees.png              (이 폴더에 포함)
  - AI/RemotionStudio/public/fedway-honorees-0803/images/ThumbNail_Final.png
    ↳ RemotionStudio는 이 저장소에 포함되지 않는다. 볼트 로컬 경로에 있어야 실행된다.

QR 대상: https://youtu.be/K8IYVPLrYZA (독립유공자 소개 영상)
"""
import base64
import os

VAULT = r'C:\AI_study\2026\Changsoo_Vault'
OUT_DIR = os.path.join(
    VAULT, 'Ingest', 'CatchUpAI_VL', 'Topics',
    'FedWay-Liberation-Day-2026', '05-Presentation')

QR = os.path.join(OUT_DIR, '_files_', 'qr-honorees.png')
THUMB = os.path.join(
    VAULT, 'AI', 'RemotionStudio', 'public',
    'fedway-honorees-0803', 'images', 'ThumbNail_Final.png')


def b64(path):
    with open(path, 'rb') as fh:
        return base64.b64encode(fh.read()).decode('ascii')


qr_b64 = b64(QR)
thumb_b64 = b64(THUMB)

CSS = """
:root {
  --bg: #1F1A15;
  --bg2: #2A231C;
  --gold: #B8935B;
  --gold-soft: #D4B584;
  --ink: #F3EDE3;
  --muted: #B5A794;
  --line: rgba(184,147,91,0.32);
}
* { box-sizing: border-box; margin: 0; padding: 0; }
html, body {
  width: 100%; height: 100%;
  background: var(--bg);
  color: var(--ink);
  font-family: "Malgun Gothic", "Apple SD Gothic Neo", "Noto Sans KR",
               "Segoe UI", sans-serif;
  -webkit-font-smoothing: antialiased;
}
.slide {
  position: relative;
  width: 1920px; height: 1080px;
  padding: 96px 128px 88px;
  display: flex; flex-direction: column;
  background:
    radial-gradient(ellipse at 50% 0%, rgba(184,147,91,0.09), transparent 62%),
    linear-gradient(160deg, #241E18 0%, #1F1A15 55%, #191411 100%);
  overflow: hidden;
  page-break-after: always;
  break-after: page;
}
.slide::after {  /* vignette */
  content: ""; position: absolute; inset: 0; pointer-events: none;
  background: radial-gradient(ellipse at 50% 45%,
              transparent 52%, rgba(0,0,0,0.42) 100%);
}
.topbar {
  display: flex; justify-content: space-between; align-items: center;
  font-size: 26px; color: var(--muted); letter-spacing: .04em;
  padding-bottom: 22px; border-bottom: 1px solid var(--line);
  margin-bottom: 56px;
}
.topbar .brand { color: var(--gold); font-weight: 700; }
h1 { font-size: 108px; line-height: 1.16; letter-spacing: -.02em; font-weight: 800; }
h2 {
  font-size: 76px; line-height: 1.2; font-weight: 800;
  letter-spacing: -.015em; margin-bottom: 12px;
}
h2 .accent { color: var(--gold-soft); }
.rule { width: 132px; height: 5px; background: var(--gold); margin: 30px 0 46px; }
.body { flex: 1; display: flex; flex-direction: column; justify-content: center; }
.lead { font-size: 50px; line-height: 1.48; font-weight: 600; }
p.big { font-size: 46px; line-height: 1.6; margin-bottom: 26px; }
p.sub { font-size: 38px; line-height: 1.6; color: var(--muted); margin-bottom: 20px; }
strong { color: var(--gold-soft); font-weight: 800; }
ul { list-style: none; }
li {
  font-size: 44px; line-height: 1.55; margin-bottom: 26px;
  padding-left: 46px; position: relative;
}
li::before {
  content: ""; position: absolute; left: 0; top: 26px;
  width: 16px; height: 16px; border-radius: 50%;
  background: var(--gold);
}
.split {
  display: grid; grid-template-columns: 1.12fr .88fr; gap: 64px;
  align-items: center; flex: 1; min-height: 0;
}
.qr-card {
  background: #fff; border-radius: 16px; padding: 18px;
  box-shadow: 0 22px 56px rgba(0,0,0,.5);
  width: 268px; display: block;
}
.qr-card img { width: 100%; display: block; }
.qr-wrap {
  display: flex; flex-direction: column; align-items: center;
  gap: 16px; justify-content: center; min-height: 0;
}
.qr-label { font-size: 28px; color: var(--gold-soft); font-weight: 700; }
.thumb {
  width: 100%; max-width: 620px; border-radius: 14px; display: block;
  border: 3px solid var(--line);
  box-shadow: 0 26px 64px rgba(0,0,0,.55);
}
/* 슬라이드 7 왼쪽 열 밀도 조정 */
.tight li { font-size: 40px; margin-bottom: 20px; }
.tight li::before { top: 22px; }
.tight p.big { font-size: 42px; margin-bottom: 22px; }
.tight p.sub { font-size: 34px; }
.compare { display: grid; grid-template-columns: 1fr 1fr; gap: 52px; margin-bottom: 34px; }
.card {
  border: 2px solid var(--line); border-radius: 16px; padding: 34px 40px;
  background: rgba(255,255,255,.035);
}
/* 슬라이드 4 하단 비유 블록 — 4줄이 들어가도록 밀도 조정 */
p.big.meta { font-size: 41px; line-height: 1.5; margin-bottom: 26px; }
.punch.meta { font-size: 44px; line-height: 1.42; }
.card.hi { border-color: var(--gold); background: rgba(184,147,91,.13); }
.card .tag {
  font-size: 30px; color: var(--muted); font-weight: 700;
  letter-spacing: .06em; margin-bottom: 18px;
}
.card.hi .tag { color: var(--gold); }
.card .txt { font-size: 42px; line-height: 1.45; font-weight: 600; }
.punch {
  font-size: 52px; line-height: 1.45; font-weight: 800;
  border-left: 6px solid var(--gold); padding-left: 36px;
}
.footer {
  display: flex; justify-content: space-between; align-items: center;
  font-size: 24px; color: var(--muted);
  border-top: 1px solid var(--line); padding-top: 22px; margin-top: 48px;
}
.center { text-align: center; align-items: center; }
.center h1, .center .lead { text-align: center; }
.motto {
  font-size: 54px; color: var(--gold-soft); font-weight: 800;
  line-height: 1.4; margin: 18px 0 40px;
}
.q { font-size: 40px; color: var(--muted); margin-top: 34px; }
@page { size: 1920px 1080px; margin: 0; }
@media print {
  html, body { width: 1920px; height: auto; }
  .slide { margin: 0; }
}
"""


def slide(n, title, body_html, brand='제81주년 광복절 기념식'):
    return f"""
<section class="slide">
  <div class="topbar">
    <div class="brand">{brand}</div>
    <div>2026. 8. 15.</div>
  </div>
  {body_html}
  <div class="footer">
    <div>박창수 · Catch Up AI</div>
    <div>{n} / 7</div>
  </div>
</section>"""


slides = []

# 1 — 타이틀 겸 QR
slides.append(slide(1, 'title', f"""
  <div class="body">
    <div class="split">
      <div>
        <h2>다시 <span class="accent">보실 수 있습니다</span></h2>
        <div class="rule"></div>
        <p class="big"><strong>다시 만나는 열두 분</strong></p>
        <p class="sub">시애틀 지역에 유가족이 계신<br>독립유공자 열두 분의 이야기</p>
        <p class="sub" style="margin-top:34px;">휴대폰 카메라로 QR 코드를 비춰 주세요</p>
      </div>
      <div class="qr-wrap">
        <img class="thumb" src="data:image/png;base64,{thumb_b64}" alt="영상 썸네일">
        <div class="qr-card"><img src="data:image/png;base64,{qr_b64}" alt="영상 QR 코드"></div>
        <div class="qr-label">지금 찍으셔도 됩니다</div>
      </div>
    </div>
  </div>"""))

# 2 — 자기소개
slides.append(slide(2, 'intro', """
  <div class="body">
    <h2>저는 이런 <span class="accent">사람입니다</span></h2>
    <div class="rule"></div>
    <ul>
      <li>한국 15년 · 미국 15년 — <strong>IT 엔지니어 30년</strong></li>
      <li>은퇴 후 2년째, <strong>AI를 일상에서 어떻게 쓸까</strong> 연구</li>
      <li>Catch Up AI 창업 — 아직은 <strong>AI를 열심히 써 보는 사용자</strong></li>
    </ul>
  </div>"""))

# 3 — 시작 경위
slides.append(slide(3, 'origin', """
  <div class="body">
    <h2>이 영상은 <span class="accent">이렇게 시작됐습니다</span></h2>
    <div class="rule"></div>
    <p class="motto">"광복정신, AI 시대의 새로운 독립을 말하다"</p>
    <ul>
      <li><strong>페더럴웨이 한인회</strong>에서 전해 주신 올해의 모토</li>
      <li>마침 <strong>AI로 영상 만드는 방법</strong>을 연구하던 참이었습니다</li>
      <li>그래서 시애틀과 인연이 있는 <strong>열두 분</strong>을 그 방법으로</li>
    </ul>
  </div>"""))

# 4 — 핵심
slides.append(slide(4, 'core', """
  <div class="body">
    <h2>찾아가는 것, <span class="accent">집으로 부르는 것</span></h2>
    <div class="rule"></div>
    <div class="compare">
      <div class="card">
        <div class="tag">Chatbot AI · 챗봇</div>
        <div class="txt">내가 AI에게<br><strong>찾아가서</strong> 부탁하는 것</div>
      </div>
      <div class="card hi">
        <div class="tag">Local Agentic AI · 내 컴퓨터에서</div>
        <div class="txt">AI를 <strong>내 집으로<br>데려와서</strong> 일을 시키는 것</div>
      </div>
    </div>
    <p class="big meta">내 집에는 평소에 내가 쓰는 물건이 다 있습니다.<br>
      도와주는 분을 부르면 <strong>더 정확하게 진단하고</strong>, 나에게 딱 맞게 도와주십니다.</p>
    <div class="punch meta"><strong>카메라를 설치해 두면</strong> 그 과정이 다 기록됩니다.<br>
      다음에 비슷한 문제가 생기면 <strong>훨씬 빨리 해결됩니다.</strong></div>
  </div>"""))

# 5 — 학생
slides.append(slide(5, 'student', """
  <div class="body">
    <h2>같은 방법을 <span class="accent">학생에게</span></h2>
    <div class="rule"></div>
    <p class="big meta">제가 공부하고 <strong>그 과정과 결과를 기록하기 위해</strong> 만든
      <strong>VibeLearn AI</strong><br>
      미국에서 자란 우리 한인 학생들은 <strong>광복을 접할 기회가 많지 않습니다.</strong></p>
    <p class="sub" style="margin-bottom:30px;">페더럴웨이 통합한국학교 ·
      이재은 교장선생님의 도움으로 <strong>이지은 학생</strong>과 함께 했습니다.</p>
    <div class="punch meta">이 방법은 한 번 공부하고 <strong>잊히는 것이 아닙니다.</strong><br>
      그 과정과 결과가 <strong>기록으로 남아</strong>, 앞으로도 계속 참고하며 이어 갈 수 있습니다.</div>
    <p class="q" style="margin-top:28px;">그 학생이 무엇을 느꼈는지는, 잠시 후 본인이 직접 말씀드립니다.</p>
  </div>"""))

# 6 — AI 시대의 독립
slides.append(slide(6, 'independence', """
  <div class="body center">
    <h2 style="text-align:center;">AI 시대의 <span class="accent">독립</span></h2>
    <div class="rule" style="margin:14px auto 26px;"></div>
    <p class="big meta" style="text-align:center;margin-bottom:22px;">기리는 일도 중요합니다. 오늘 이 자리가 그 자리입니다.</p>
    <p style="font-size:44px;line-height:1.45;font-weight:600;text-align:center;margin-bottom:24px;">
      그러나 그 뜻을 진정으로 이어받는 것은<br>
      그분들이 되찾아 주신 이 나라를 <strong>더 좋은 나라로 만드는 것</strong>일 겁니다.</p>
    <p style="font-size:40px;line-height:1.5;text-align:center;color:var(--muted);margin-bottom:26px;">
      그 일에는 여러 갈래가 있습니다.<br>
      그중 하나가 <strong style="color:var(--ink);">이 시대에 우리가 할 수 있는 몫</strong>입니다.</p>
    <p class="motto" style="text-align:center;font-size:46px;line-height:1.4;margin:0;">
      급변하는 AI 시대를 우리 한민족이 더 잘 맞이하고,<br>
      다른 이들에게도 선한 영향을 끼치는 것.<br>
      그것이 AI 시대의 독립에 이바지하는 길이 아닐까 합니다.</p>
  </div>"""))

# 7 — CTA + QR
slides.append(slide(7, 'cta', f"""
  <div class="body">
    <div class="split tight">
      <div>
        <h2>함께하고 <span class="accent">싶습니다</span></h2>
        <div class="rule"></div>
        <p class="big">Catch Up AI는 그 일에 <strong>작은 보탬</strong>이 되고 싶습니다.</p>
        <ul style="margin-top:24px;">
          <li>AI 시대에는 <strong>배우는 방법 자체</strong>가 달라집니다</li>
          <li>학생만이 아닙니다. <strong>어른들도 준비해야 합니다</strong></li>
        </ul>
        <p class="sub" style="margin-top:24px;">함께 가고 싶은 단체나 개인이 계시면<br>언제든지 연락 주십시오.</p>
        <p style="margin-top:20px;font-size:36px;font-weight:800;color:var(--gold-soft);
                  line-height:1.5;letter-spacing:.01em;">solkit70@gmail.com</p>
        <p class="qr-label" style="margin-top:4px;font-size:30px;">youtube.com/@catchupai</p>
      </div>
      <div class="qr-wrap">
        <div class="qr-card"><img src="data:image/png;base64,{qr_b64}" alt="영상 QR 코드"></div>
        <div class="qr-label">오늘 영상 다시 보기</div>
      </div>
    </div>
  </div>"""))

html = f"""<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<title>광복 81주년 — AI 시대의 새로운 독립을 말하다 | 박창수</title>
<style>{CSS}</style>
</head>
<body>
{''.join(slides)}
</body>
</html>"""

out = os.path.join(OUT_DIR, 'slides.html')
with open(out, 'w', encoding='utf-8') as fh:
    fh.write(html)
print('생성:', out, f'{len(html)/1024:.0f} KB', f'· 슬라이드 {len(slides)}장')
