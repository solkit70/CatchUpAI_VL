---
marp: true
theme: gaia
class: invert
paginate: true
lang: ko
style: |
  :root {
    --color-foreground: #e8f0fe;
    --color-background: #1a2744;
    --color-highlight: #22C55E;
  }
  section {
    background-color: #1d3a6e;
    background-image:
      radial-gradient(ellipse at 5% 5%, rgba(34,197,94,0.18) 0%, transparent 45%),
      radial-gradient(ellipse at 95% 95%, rgba(56,189,248,0.14) 0%, transparent 45%),
      radial-gradient(ellipse at 90% 5%, rgba(245,158,11,0.10) 0%, transparent 35%),
      radial-gradient(circle at 1.5px 1.5px, rgba(255,255,255,0.06) 1.5px, transparent 0);
    background-size: 100% 100%, 100% 100%, 100% 100%, 32px 32px;
    color: #e8f0fe;
    font-family: 'Noto Sans KR', 'Malgun Gothic', sans-serif;
  }
  h1 {
    color: #22C55E;
    font-size: 1.6em;
    border-bottom: 2px solid rgba(34,197,94,0.35);
    padding-bottom: 0.15em;
    margin-bottom: 0.4em;
  }
  h2 {
    color: #F59E0B;
    font-size: 1.3em;
    letter-spacing: -0.01em;
  }
  h3 { color: #60A5FA; }
  strong { color: #F59E0B; }
  a { color: #60A5FA; }
  blockquote {
    border-left: 4px solid #22C55E;
    background: rgba(34, 197, 94, 0.10);
    padding: 0.5em 1em;
    font-size: 0.95em;
    color: #bbf7d0;
    border-radius: 0 8px 8px 0;
    margin: 0.6em 0;
  }
  table {
    font-size: 0.82em;
    width: 100%;
    border-collapse: collapse;
  }
  th {
    background: rgba(34,197,94,0.22);
    color: #22C55E;
    padding: 6px 10px;
  }
  td { padding: 5px 10px; }
  tr:nth-child(even) { background: rgba(255,255,255,0.06); }
  tr:nth-child(odd) { background: rgba(255,255,255,0.02); }
  code {
    background: rgba(34,197,94,0.14);
    color: #a7f3d0;
    padding: 0.15em 0.4em;
    border-radius: 4px;
    font-size: 0.88em;
  }
  pre {
    background: rgba(10,16,38,0.75);
    border: 1px solid rgba(34,197,94,0.3);
    border-radius: 10px;
    padding: 0.8em 1em;
    font-size: 0.82em;
  }
  pre code { background: transparent; color: #a7f3d0; padding: 0; }
  .lead h1 { font-size: 2em; text-align: center; }
  .lead p { text-align: center; font-size: 1.1em; }
  section.lead {
    background-image:
      radial-gradient(ellipse at 50% 35%, rgba(34,197,94,0.25) 0%, transparent 60%),
      radial-gradient(ellipse at 5% 100%, rgba(56,189,248,0.18) 0%, transparent 50%),
      radial-gradient(circle at 1.5px 1.5px, rgba(255,255,255,0.06) 1.5px, transparent 0);
    background-size: 100% 100%, 100% 100%, 32px 32px;
  }
  video {
    width: 100%;
    max-height: 38vh;
    border-radius: 10px;
    border: 2px solid rgba(34,197,94,0.5);
    box-shadow: 0 4px 20px rgba(34,197,94,0.18);
    margin-bottom: 0.6em;
  }
  .clip-label {
    font-size: 0.75em;
    color: #64748b;
    text-align: right;
    margin-top: 4px;
  }
---

<!-- _class: lead invert -->

# 기록이 AI를 강하게 만든다

**AI 크리에이터의 경쟁력은 기록에서 시작된다**

---

<div style="display:flex;flex-direction:column;align-items:center;justify-content:center;height:85%;">
  <div style="display:flex;gap:80px;margin-bottom:28px;">
    <div style="text-align:center;">
      <div style="background:#fff;padding:12px;border-radius:12px;display:inline-block;">
        <img src="qr_youtube.png" style="width:180px;height:180px;display:block;">
      </div>
      <p style="font-size:0.85em;margin-top:12px;"><a href="https://www.youtube.com/@catchupai" target="_blank" rel="noopener" style="color:#60A5FA;text-decoration:none;">📺 youtube.com/@catchupai</a></p>
    </div>
    <div style="text-align:center;">
      <div style="background:#fff;padding:12px;border-radius:12px;display:inline-block;">
        <img src="qr_website.png" style="width:180px;height:180px;display:block;">
      </div>
      <p style="font-size:0.85em;margin-top:12px;"><a href="https://catchupai.net/" target="_blank" rel="noopener" style="color:#60A5FA;text-decoration:none;">🌐 catchupai.net</a></p>
    </div>
  </div>
  <div style="border-top:1px solid rgba(34,197,94,0.35);width:50%;margin:0 auto 20px;"></div>
  <p style="text-align:center;margin:0;color:#e8f0fe;font-size:1.05em;">
    <strong style="color:#F59E0B;">박창수</strong> · Catch Up AI<br>
    <span style="color:#94a3b8;font-size:0.85em;">창발 Product Group · 2026-06-26</span>
  </p>
</div>

<!-- 인사 + "오늘 36분 영상 데모로 시작하겠습니다" -->

---

<!-- _paginate: false -->

<img src="https://img.youtube.com/vi/Cucvcz9bVPU/maxresdefault.jpg" style="position:absolute;right:0;top:0;width:46%;height:100%;object-fit:cover;object-position:left center;border-left:3px solid rgba(34,197,94,0.45);">

<div style="max-width:52%;display:flex;flex-direction:column;gap:56px;padding-top:10px;margin-left:-10px;">

<h2 style="color:#F59E0B;font-size:1.6em;margin:0;">🎬 Tehaleh 소개 영상</h2>

<blockquote style="border-left:4px solid #22C55E;background:rgba(34,197,94,0.10);padding:0.5em 1em;color:#bbf7d0;border-radius:0 8px 8px 0;margin:0;">발표 전에 링크를 공유드렸습니다. 보셨나요?</blockquote>

<div>
<strong style="color:#F59E0B;">Tehaleh — Pierce County, WA</strong><br>
AI가 만든 동네 소개 영상
</div>

<div><a href="https://youtu.be/Cucvcz9bVPU" style="color:#60A5FA;" target="_blank" rel="noopener">한국어 영상</a> · <a href="https://youtu.be/YygPvJbKPvU" style="color:#60A5FA;" target="_blank" rel="noopener">English Version</a></div>

</div>

---

## 36분만에 영상 초본 완성 — 5단계 과정

| 단계 | 작업 | 시간 |
|------|------|------|
| 1 | <a href="https://github.com/solkit70/VibeLearn-AI" target="_blank" rel="noopener">VibeLearn AI</a> — Roadmap 작성 | **8분** |
| 2 | M1 Research | **2분** |
| 3 | M2 슬라이드 플랜 (15장) | **4분** |
| 4 | M3 Remotion 컴포넌트 개발 | **13분** |
| 5 | M4 오디오 생성 + Draft 렌더링 | **9분** |
| | **합계** | **36분** |

지금부터 각 단계를 직접 보여드리겠습니다.

<!-- "화면에 보이는 영상은 각 단계에서 실제 작업한 20~30초 클립입니다" -->

---

<!-- _header: "오프닝 데모 — Step 1/5" -->

## 🗺️ VibeLearn AI — Roadmap 8분

<video src="clips/clip_01_roadmap.mp4" controls></video>

- **VibeLearn AI**: 목표 → 로드맵 → 단계별 학습 시스템
- **4개 모듈**: Research / 슬라이드 플랜 / Remotion 개발 / 오디오·렌더링
- 로드맵이 있어야 AI에게 정확하게 지시할 수 있습니다

---

<!-- _header: "오프닝 데모 — Step 2/5" -->

## 🔍 M1 Research — 2분

<video src="clips/clip_02_research.mp4" controls></video>

- `tehaleh-research.md` — 6개 섹션 자동 구조화
- 위치 / 커뮤니티 / IT 종사자 / 은퇴자 / 한인 관점
- 리서치 결과 → 다음 슬라이드 플랜의 소재

---

<!-- _header: "오프닝 데모 — Step 3/5" -->

## 📋 M2 슬라이드 플랜 — 4분

<video src="clips/clip_03_slideplan.mp4" controls></video>

- `video-slide-plan.md` — 15장 슬라이드 기획 + 한국어 나레이션 스크립트
- 슬라이드 타입, 내용, 예상 시간 자동 작성
- 이 계획 문서가 코딩 단계의 청사진

---

<!-- _header: "오프닝 데모 — Step 4/5" -->

## ⚛️ M3 Remotion 개발 — 13분

<video src="clips/clip_04_remotion.mp4" controls></video>

- React 기반 영상 프레임워크 + Claude Code
- 6가지 슬라이드 타입 컴포넌트 + 별빛 배경 애니메이션
- `video-slide-plan.md` → 코드 자동 생성 → Remotion Studio 미리보기

---

<!-- _header: "오프닝 데모 — Step 5/5" -->

## 🎤 M4 오디오 + 렌더링 — 9분

<video src="clips/clip_05_audio.mp4" controls></video>

- `gen_audio.py` — 15개 슬라이드 한국어 TTS 동시 생성
- 오디오 길이 측정 → `data.ts` 타이밍 자동 업데이트
- **Draft MP4 렌더링 완료** — 총 36분

---

<!-- _class: lead -->

<div style="display:flex;flex-direction:column;align-items:center;justify-content:center;gap:12px;">
  <img src="images/dokkaebi.png" style="height:40vh;border-radius:12px;">
  <p style="color:#F59E0B;font-weight:bold;font-size:0.85em;margin:0;">사실 이게 도깨비 방망이 처럼 뚝딱 만들어진 것은 아닙니다.</p>
</div>

---

## 사전 준비 — 시스템과 스킬

- ✅ **tehaleh-video-prompt.md** — 영상 제작 워크플로우 프롬프트
- ✅ <a href="https://github.com/solkit70/VibeLearn-AI" target="_blank" rel="noopener" style="font-weight:bold;">VibeLearn AI 학습 시스템</a> — 1년간 실험으로 구축
- ✅ <a href="https://github.com/jykim/ai4pkm-vault" target="_blank" rel="noopener" style="font-weight:bold;">AI4PKM Vault</a> — 김진영님의 기록 저장 기반 시스템
- ✅ **Remotion 프레임워크** — React 기반 코드형 영상 제작 도구
- ✅ **VS Code + Claude Code** — AI 코딩 환경 세팅 완료
- ✅ <a href="https://www.gobispace.com/" target="_blank" rel="noopener" style="font-weight:bold;">GOBI Desktop</a> — 방송 중 실시간 Capture

---

## 사전 준비 — API와 도구

- ✅ **Node.js 18+ + Remotion** — `npm install` 완료
- ✅ **Remotion 스킬 라이브러리** — 10개+ 영상 제작으로 축적된 패턴
- ✅ **openai-image-skill / gemini-image-skill** — API 이미지 생성
- ✅ **ChatGPT/Gemini 웹** — API 없이 이미지 생성
- ✅ **edge-tts** — 무료 초안용 TTS (`pip install edge-tts`)
- ✅ **Qwen3-TTS API** — 내 목소리 복제 모델 + `DASHSCOPE_API_KEY`
- ✅ **ffmpeg** — 오디오 후처리 (속도·음량)

이것들이 없었다면 36분이 아니라 며칠이 걸렸을 것입니다

---

## Draft 이후 — 후작업 플로우

<div style="display:flex;gap:24px;margin-top:12px;font-size:0.82em;">
  <div style="flex:1;border:1px solid rgba(34,197,94,0.28);border-radius:10px;padding:14px 16px;">
    <div style="color:#60A5FA;font-weight:bold;margin-bottom:10px;font-size:1.05em;">🎬 영상 제작</div>
    <div style="display:flex;flex-direction:column;gap:4px;">
      <div style="display:flex;align-items:center;gap:8px;"><span style="color:#22C55E;font-weight:bold;min-width:18px;">1.</span><span>Edge-TTS 생성</span></div>
      <div style="color:#22C55E;padding-left:26px;line-height:1;">↓</div>
      <div style="display:flex;align-items:center;gap:8px;"><span style="color:#22C55E;font-weight:bold;min-width:18px;">2.</span><span>나레이션 수정 (내 말투로)</span></div>
      <div style="color:#22C55E;padding-left:26px;line-height:1;">↓</div>
      <div style="display:flex;align-items:center;gap:8px;"><span style="color:#22C55E;font-weight:bold;min-width:18px;">3.</span><span>슬라이드 세부 수정</span></div>
      <div style="color:#22C55E;padding-left:26px;line-height:1;">↓</div>
      <div style="display:flex;align-items:center;gap:8px;"><span style="color:#22C55E;font-weight:bold;min-width:18px;">4.</span><span>Qwen3-TTS로 음성 교체</span></div>
      <div style="color:#22C55E;padding-left:26px;line-height:1;">↓</div>
      <div style="display:flex;align-items:center;gap:8px;background:rgba(34,197,94,0.12);border-radius:6px;padding:5px 8px;"><span style="color:#22C55E;font-weight:bold;min-width:18px;">5.</span><span style="color:#22C55E;font-weight:bold;">렌더링 완료 🎬</span></div>
      <div style="color:#22C55E;padding-left:26px;line-height:1;">↓</div>
      <div style="display:flex;align-items:center;gap:8px;"><span style="color:#22C55E;font-weight:bold;min-width:18px;">6.</span><span>영어 영상 제작</span></div>
    </div>
  </div>
  <div style="flex:1;border:1px solid rgba(245,158,11,0.28);border-radius:10px;padding:14px 16px;">
    <div style="color:#F59E0B;font-weight:bold;margin-bottom:10px;font-size:1.05em;">📺 YouTube 업로드</div>
    <div style="display:flex;flex-direction:column;gap:4px;">
      <div style="display:flex;align-items:center;gap:8px;"><span style="color:#F59E0B;font-weight:bold;min-width:18px;">1.</span><span>유튜브 업로드</span></div>
      <div style="color:#F59E0B;padding-left:26px;line-height:1;">↓</div>
      <div style="display:flex;align-items:center;gap:8px;"><span style="color:#F59E0B;font-weight:bold;min-width:18px;">2.</span><span>썸네일 작업</span></div>
      <div style="color:#F59E0B;padding-left:26px;line-height:1;">↓</div>
      <div style="display:flex;align-items:center;gap:8px;"><span style="color:#F59E0B;font-weight:bold;min-width:18px;">3.</span><span>제목 · Description · Tags 작성</span></div>
      <div style="color:#F59E0B;padding-left:26px;line-height:1;">↓</div>
      <div style="display:flex;align-items:center;gap:8px;"><span style="color:#F59E0B;font-weight:bold;min-width:18px;">4.</span><span>Publish</span></div>
      <div style="color:#F59E0B;padding-left:26px;line-height:1;">↓</div>
      <div style="display:flex;align-items:center;gap:8px;background:rgba(245,158,11,0.12);border-radius:6px;padding:5px 8px;"><span style="color:#F59E0B;font-weight:bold;min-width:18px;">5.</span><span style="color:#F59E0B;font-weight:bold;">SNS 홍보 📢</span></div>
    </div>
  </div>
</div>

---

## End to End 완전 자동화 예

<div style="display:flex;justify-content:center;margin-top:12px;">
  <img src="images/RimahDailyMeditation.jpg" style="max-height:62vh;max-width:88%;object-fit:contain;border-radius:10px;border:2px solid rgba(34,197,94,0.35);">
</div>

---

<!-- _class: lead -->
<!-- _paginate: false -->

<div style="display:flex;justify-content:center;align-items:center;height:90%;">
  <img src="images/dokkaebi_content.png" style="max-height:78vh;max-width:88%;object-fit:contain;border-radius:12px;">
</div>

---

## Catch Up AI — 채널 변화 타임라인

<table style="width:100%; font-size:0.72em; border-collapse:collapse; margin-top:0.4em; line-height:1.3">
<thead>
<tr style="background:rgba(255,255,255,0.15)">
<th style="padding:0.4em 0.7em; text-align:left; width:6%">Phase</th>
<th style="padding:0.4em 0.7em; text-align:left; width:22%; white-space:nowrap">기간</th>
<th style="padding:0.4em 0.7em; text-align:left; width:32%">주제</th>
<th style="padding:0.4em 0.7em; text-align:left">특성</th>
</tr>
</thead>
<tbody>
<tr style="border-top:1px solid rgba(255,255,255,0.1)">
<td style="padding:0.4em 0.7em; font-weight:bold; color:#60A5FA; vertical-align:middle">P1</td>
<td style="padding:0.4em 0.7em; color:#94a3b8; white-space:nowrap; vertical-align:middle">24-02-13 ~ 24-03-19</td>
<td style="padding:0.4em 0.7em; vertical-align:middle">Deep Learning 기초</td>
<td style="padding:0.4em 0.7em; color:#94a3b8; vertical-align:middle">기술 설명</td>
</tr>
<tr style="border-top:1px solid rgba(255,255,255,0.1)">
<td style="padding:0.4em 0.7em; font-weight:bold; color:#22C55E; vertical-align:middle" rowspan="2">P2</td>
<td style="padding:0.4em 0.7em; color:#94a3b8; white-space:nowrap; vertical-align:middle" rowspan="2">24-03-20 ~ 25-03-31</td>
<td style="padding:0.4em 0.7em; vertical-align:middle">LangChain / LangGraph</td>
<td style="padding:0.4em 0.7em; color:#94a3b8; vertical-align:middle">AI 앱 개발</td>
</tr>
<tr>
<td style="padding:0.4em 0.7em; vertical-align:middle">AI Agent / 추론</td>
<td style="padding:0.4em 0.7em; color:#94a3b8; vertical-align:middle">방법론 탐구</td>
</tr>
<tr style="border-top:1px solid rgba(255,255,255,0.1)">
<td style="padding:0.4em 0.7em; font-weight:bold; color:#F59E0B; vertical-align:middle" rowspan="3">P3</td>
<td style="padding:0.4em 0.7em; color:#94a3b8; white-space:nowrap; vertical-align:middle" rowspan="3">25-04-01 ~ 26-02-23</td>
<td style="padding:0.4em 0.7em; vertical-align:middle"><strong style="color:#22C55E">Vibe Coding</strong> <span style="color:#94a3b8; font-size:0.85em">(라방)</span></td>
<td style="padding:0.4em 0.7em; color:#94a3b8; vertical-align:middle">재미로 하는 Vibe Coding</td>
</tr>
<tr>
<td style="padding:0.4em 0.7em; vertical-align:middle">PKM / AI4PKM</td>
<td style="padding:0.4em 0.7em; color:#94a3b8; vertical-align:middle">기록 시스템</td>
</tr>
<tr>
<td style="padding:0.4em 0.7em; vertical-align:middle">AI 일상 실험 <span style="color:#94a3b8; font-size:0.85em">(라방)</span></td>
<td style="padding:0.4em 0.7em; color:#94a3b8; vertical-align:middle">AI를 일상에 적용</td>
</tr>
<tr style="border-top:1px solid rgba(255,255,255,0.1)">
<td style="padding:0.4em 0.7em; font-weight:bold; color:#a78bfa; vertical-align:middle">P4</td>
<td style="padding:0.4em 0.7em; color:#94a3b8; white-space:nowrap; vertical-align:middle">26-02-24 ~ 현재</td>
<td style="padding:0.4em 0.7em; vertical-align:middle"><strong>AI 영상 제작</strong> <span style="color:#94a3b8; font-size:0.85em">(라방 요약 등)</span></td>
<td style="padding:0.4em 0.7em; color:#94a3b8; vertical-align:middle">Remotion·AI로 영상 자동 제작</td>
</tr>
</tbody>
</table>

<div style="display:flex; align-items:center; justify-content:center; gap:1.5em; margin-top:0.7em; font-size:0.65em">
  <div style="white-space:nowrap; color:#94a3b8">채널의 변화 = 관심의 변화</div>
  <div style="display:flex; align-items:center; gap:0.6em">
    <span style="background:rgba(96,165,250,0.15); border-radius:6px; padding:0.25em 0.8em; color:#60A5FA; white-space:nowrap">AI 배우기</span>
    <span style="color:#94a3b8">→→→</span>
    <span style="background:rgba(34,197,94,0.15); border-radius:6px; padding:0.25em 0.8em; color:#22C55E; white-space:nowrap">AI 사용하기</span>
    <span style="color:#94a3b8; font-size:0.9em; padding-left:0.3em">학습 중심에서 실전·창작 중심으로</span>
  </div>
</div>

---

## 기록이 없으면 AI를 활용 할 수 없다

| | Tehaleh/묵상 영상 | 내 실험·방송·학습 |
|--|------------|---------------|
| 정보 원천 | 인터넷 | **내 컴퓨터에 과정과 결과 기록** |
| AI 활용 | 누구나 가능 | **기록한 사람만 가능** |
| 타 영상과 비교 | 차별화 제한적 | **나만의 콘텐츠** |

> "AI 크리에이터의 경쟁력은 기록에서 시작된다"

> "기록하지 않은 경험은 AI 에게는 존재하지 않는 대상이다"

---

<div style="display:flex; justify-content:center; align-items:center; height:100%">
  <img src="images/dokkaebi_AI.png" style="width:85%; border-radius:12px; box-shadow:0 8px 32px rgba(0,0,0,0.5)">
</div>

---

## Phase별 성과 비교

<table style="width:100%; font-size:0.78em; border-collapse:collapse; margin-top:0.6em; line-height:1.4">
<thead>
<tr style="background:rgba(255,255,255,0.15)">
<th style="padding:0.45em 0.8em; text-align:left; width:18%">Phase</th>
<th style="padding:0.45em 0.8em; text-align:center; width:10%">기간(월)</th>
<th style="padding:0.45em 0.8em; text-align:right; width:18%">일반 영상 조회수</th>
<th style="padding:0.45em 0.8em; text-align:right; width:16%">월평균 조회수</th>
<th style="padding:0.45em 0.8em; text-align:right; width:16%">월평균 신규구독</th>
<th style="padding:0.45em 0.8em; text-align:left">비고</th>
</tr>
</thead>
<tbody>
<tr style="border-top:1px solid rgba(255,255,255,0.1)">
<td style="padding:0.45em 0.8em; font-weight:bold; color:#60A5FA">P1 DL 입문</td>
<td style="padding:0.45em 0.8em; text-align:center; color:#94a3b8">1.2</td>
<td style="padding:0.45em 0.8em; text-align:right; color:#94a3b8">~1,200</td>
<td style="padding:0.45em 0.8em; text-align:right; color:#94a3b8">~1,000</td>
<td style="padding:0.45em 0.8em; text-align:right; color:#94a3b8">~12명</td>
<td style="padding:0.45em 0.8em; color:#94a3b8">소규모, 채널 시작</td>
</tr>
<tr style="border-top:1px solid rgba(255,255,255,0.1); background:rgba(34,197,94,0.08)">
<td style="padding:0.45em 0.8em; font-weight:bold; color:#22C55E">P2 외부 기술 전달</td>
<td style="padding:0.45em 0.8em; text-align:center; color:#22C55E">12.4</td>
<td style="padding:0.45em 0.8em; text-align:right; color:#e8f0fe">~71,307</td>
<td style="padding:0.45em 0.8em; text-align:right; font-weight:bold; color:#22C55E">~5,750</td>
<td style="padding:0.45em 0.8em; text-align:right; font-weight:bold; color:#22C55E">~231명</td>
<td style="padding:0.45em 0.8em; color:#22C55E">채널 핵심 성장기</td>
</tr>
<tr style="border-top:1px solid rgba(255,255,255,0.1)">
<td style="padding:0.45em 0.8em; font-weight:bold; color:#F59E0B">P3 라이브 방송</td>
<td style="padding:0.45em 0.8em; text-align:center; color:#94a3b8">10.8</td>
<td style="padding:0.45em 0.8em; text-align:right; color:#94a3b8">~52,175</td>
<td style="padding:0.45em 0.8em; text-align:right; color:#94a3b8">~4,831</td>
<td style="padding:0.45em 0.8em; text-align:right; color:#94a3b8">~125명</td>
<td style="padding:0.45em 0.8em; color:#94a3b8">전환 후 하락</td>
</tr>
<tr style="border-top:1px solid rgba(255,255,255,0.1)">
<td style="padding:0.45em 0.8em; font-weight:bold; color:#a78bfa">P4 AI 영상 제작</td>
<td style="padding:0.45em 0.8em; text-align:center; color:#94a3b8">3.9</td>
<td style="padding:0.45em 0.8em; text-align:right; color:#94a3b8">~10,326</td>
<td style="padding:0.45em 0.8em; text-align:right; color:#94a3b8">~2,648</td>
<td style="padding:0.45em 0.8em; text-align:right; color:#94a3b8">~18명</td>
<td style="padding:0.45em 0.8em; color:#94a3b8">진행 중</td>
</tr>
</tbody>
</table>

---

## 월별 조회수 · 구독자 추이

<div style="display:grid; grid-template-columns:1fr 1fr; gap:1em; margin-top:0.2em; font-size:0.57em">

<div>
<table style="width:100%; border-collapse:collapse; line-height:1.2">
<thead>
<tr style="background:rgba(255,255,255,0.15)">
<th style="padding:0.22em 0.45em; text-align:left">월</th>
<th style="padding:0.22em 0.45em; text-align:right">조회수</th>
<th style="padding:0.22em 0.45em; text-align:right">구독</th>
<th style="padding:0.22em 0.45em; text-align:left">비고</th>
</tr>
</thead>
<tbody>
<tr style="border-top:1px solid rgba(255,255,255,0.08)"><td style="padding:0.18em 0.45em; color:#60A5FA">2024-02</td><td style="padding:0.18em 0.45em; text-align:right; color:#94a3b8">~800</td><td style="padding:0.18em 0.45em; text-align:right; color:#94a3b8">~4</td><td style="padding:0.18em 0.45em; color:#94a3b8">채널 시작 2/13</td></tr>
<tr style="border-top:1px solid rgba(255,255,255,0.08)"><td style="padding:0.18em 0.45em; color:#60A5FA">2024-03 (1~19)</td><td style="padding:0.18em 0.45em; text-align:right; color:#94a3b8">~169</td><td style="padding:0.18em 0.45em; text-align:right; color:#94a3b8">~10</td><td style="padding:0.18em 0.45em; color:#94a3b8">DL Basic 07 마지막</td></tr>
<tr style="border-top:1px solid rgba(255,255,255,0.08); background:rgba(34,197,94,0.05)"><td style="padding:0.18em 0.45em; color:#22C55E">2024-03 (20~31)</td><td style="padding:0.18em 0.45em; text-align:right">~106</td><td style="padding:0.18em 0.45em; text-align:right">~4</td><td style="padding:0.18em 0.45em; color:#22C55E">P2 시작</td></tr>
<tr style="border-top:1px solid rgba(255,255,255,0.08); background:rgba(34,197,94,0.05)"><td style="padding:0.18em 0.45em; color:#22C55E">2024-04</td><td style="padding:0.18em 0.45em; text-align:right">2,918</td><td style="padding:0.18em 0.45em; text-align:right">58</td><td style="padding:0.18em 0.45em"></td></tr>
<tr style="border-top:1px solid rgba(255,255,255,0.08); background:rgba(34,197,94,0.05)"><td style="padding:0.18em 0.45em; color:#22C55E">2024-05</td><td style="padding:0.18em 0.45em; text-align:right">3,378</td><td style="padding:0.18em 0.45em; text-align:right">202</td><td style="padding:0.18em 0.45em"></td></tr>
<tr style="border-top:1px solid rgba(255,255,255,0.08); background:rgba(34,197,94,0.05)"><td style="padding:0.18em 0.45em; color:#22C55E">2024-06</td><td style="padding:0.18em 0.45em; text-align:right">1,078</td><td style="padding:0.18em 0.45em; text-align:right">66</td><td style="padding:0.18em 0.45em"></td></tr>
<tr style="border-top:1px solid rgba(255,255,255,0.08); background:rgba(34,197,94,0.05)"><td style="padding:0.18em 0.45em; color:#22C55E">2024-07</td><td style="padding:0.18em 0.45em; text-align:right">4,154</td><td style="padding:0.18em 0.45em; text-align:right">150</td><td style="padding:0.18em 0.45em"></td></tr>
<tr style="border-top:1px solid rgba(255,255,255,0.08); background:rgba(34,197,94,0.05)"><td style="padding:0.18em 0.45em; color:#22C55E">2024-08</td><td style="padding:0.18em 0.45em; text-align:right">4,350</td><td style="padding:0.18em 0.45em; text-align:right">194</td><td style="padding:0.18em 0.45em"></td></tr>
<tr style="border-top:1px solid rgba(255,255,255,0.08); background:rgba(34,197,94,0.05)"><td style="padding:0.18em 0.45em; color:#22C55E">2024-09</td><td style="padding:0.18em 0.45em; text-align:right">3,100</td><td style="padding:0.18em 0.45em; text-align:right">104</td><td style="padding:0.18em 0.45em"></td></tr>
<tr style="border-top:1px solid rgba(255,255,255,0.08); background:rgba(34,197,94,0.05)"><td style="padding:0.18em 0.45em; color:#22C55E">2024-10</td><td style="padding:0.18em 0.45em; text-align:right; font-weight:bold; color:#22C55E">11,914</td><td style="padding:0.18em 0.45em; text-align:right">411</td><td style="padding:0.18em 0.45em; color:#F59E0B">IONQ 바이럴</td></tr>
<tr style="border-top:1px solid rgba(255,255,255,0.08); background:rgba(34,197,94,0.05)"><td style="padding:0.18em 0.45em; color:#22C55E">2024-11</td><td style="padding:0.18em 0.45em; text-align:right">~5,518</td><td style="padding:0.18em 0.45em; text-align:right">126</td><td style="padding:0.18em 0.45em"></td></tr>
<tr style="border-top:1px solid rgba(255,255,255,0.08); background:rgba(34,197,94,0.05)"><td style="padding:0.18em 0.45em; color:#22C55E">2024-12</td><td style="padding:0.18em 0.45em; text-align:right">~7,433</td><td style="padding:0.18em 0.45em; text-align:right">384</td><td style="padding:0.18em 0.45em"></td></tr>
<tr style="border-top:1px solid rgba(255,255,255,0.08); background:rgba(34,197,94,0.05)"><td style="padding:0.18em 0.45em; color:#22C55E">2025-01</td><td style="padding:0.18em 0.45em; text-align:right">9,343</td><td style="padding:0.18em 0.45em; text-align:right">415</td><td style="padding:0.18em 0.45em"></td></tr>
<tr style="border-top:1px solid rgba(255,255,255,0.08); background:rgba(34,197,94,0.05)"><td style="padding:0.18em 0.45em; color:#22C55E">2025-02</td><td style="padding:0.18em 0.45em; text-align:right">12,218</td><td style="padding:0.18em 0.45em; text-align:right; font-weight:bold; color:#22C55E">427</td><td style="padding:0.18em 0.45em; color:#F59E0B">구독자 월 최고</td></tr>
<tr style="border-top:1px solid rgba(255,255,255,0.08); background:rgba(34,197,94,0.05)"><td style="padding:0.18em 0.45em; color:#22C55E">2025-03</td><td style="padding:0.18em 0.45em; text-align:right">~10,479</td><td style="padding:0.18em 0.45em; text-align:right">319</td><td style="padding:0.18em 0.45em"></td></tr>
</tbody>
</table>
</div>

<div>
<table style="width:100%; border-collapse:collapse; line-height:1.2">
<thead>
<tr style="background:rgba(255,255,255,0.15)">
<th style="padding:0.22em 0.45em; text-align:left">월</th>
<th style="padding:0.22em 0.45em; text-align:right">조회수</th>
<th style="padding:0.22em 0.45em; text-align:right">구독</th>
<th style="padding:0.22em 0.45em; text-align:left">비고</th>
</tr>
</thead>
<tbody>
<tr style="border-top:1px solid rgba(255,255,255,0.08); background:rgba(245,158,11,0.05)"><td style="padding:0.18em 0.45em; color:#F59E0B">2025-04</td><td style="padding:0.18em 0.45em; text-align:right">9,998</td><td style="padding:0.18em 0.45em; text-align:right">386</td><td style="padding:0.18em 0.45em; color:#F59E0B">라이브 방송 시작</td></tr>
<tr style="border-top:1px solid rgba(255,255,255,0.08); background:rgba(245,158,11,0.05)"><td style="padding:0.18em 0.45em; color:#F59E0B">2025-05</td><td style="padding:0.18em 0.45em; text-align:right">8,399</td><td style="padding:0.18em 0.45em; text-align:right">235</td><td style="padding:0.18em 0.45em"></td></tr>
<tr style="border-top:1px solid rgba(255,255,255,0.08); background:rgba(245,158,11,0.05)"><td style="padding:0.18em 0.45em; color:#F59E0B">2025-06</td><td style="padding:0.18em 0.45em; text-align:right">4,471</td><td style="padding:0.18em 0.45em; text-align:right">107</td><td style="padding:0.18em 0.45em; color:#94a3b8">성장세 꺾임</td></tr>
<tr style="border-top:1px solid rgba(255,255,255,0.08); background:rgba(245,158,11,0.05)"><td style="padding:0.18em 0.45em; color:#F59E0B">2025-07</td><td style="padding:0.18em 0.45em; text-align:right">4,023</td><td style="padding:0.18em 0.45em; text-align:right">126</td><td style="padding:0.18em 0.45em"></td></tr>
<tr style="border-top:1px solid rgba(255,255,255,0.08); background:rgba(245,158,11,0.05)"><td style="padding:0.18em 0.45em; color:#F59E0B">2025-08</td><td style="padding:0.18em 0.45em; text-align:right">5,040</td><td style="padding:0.18em 0.45em; text-align:right">84</td><td style="padding:0.18em 0.45em"></td></tr>
<tr style="border-top:1px solid rgba(255,255,255,0.08); background:rgba(245,158,11,0.05)"><td style="padding:0.18em 0.45em; color:#F59E0B">2025-09</td><td style="padding:0.18em 0.45em; text-align:right">3,838</td><td style="padding:0.18em 0.45em; text-align:right">58</td><td style="padding:0.18em 0.45em"></td></tr>
<tr style="border-top:1px solid rgba(255,255,255,0.08); background:rgba(245,158,11,0.05)"><td style="padding:0.18em 0.45em; color:#F59E0B">2025-10</td><td style="padding:0.18em 0.45em; text-align:right">2,362</td><td style="padding:0.18em 0.45em; text-align:right">51</td><td style="padding:0.18em 0.45em"></td></tr>
<tr style="border-top:1px solid rgba(255,255,255,0.08); background:rgba(245,158,11,0.05)"><td style="padding:0.18em 0.45em; color:#F59E0B">2025-11</td><td style="padding:0.18em 0.45em; text-align:right">2,635</td><td style="padding:0.18em 0.45em; text-align:right">51</td><td style="padding:0.18em 0.45em; color:#94a3b8">저점</td></tr>
<tr style="border-top:1px solid rgba(255,255,255,0.08); background:rgba(245,158,11,0.05)"><td style="padding:0.18em 0.45em; color:#F59E0B">2025-12</td><td style="padding:0.18em 0.45em; text-align:right">3,455</td><td style="padding:0.18em 0.45em; text-align:right">74</td><td style="padding:0.18em 0.45em"></td></tr>
<tr style="border-top:1px solid rgba(255,255,255,0.08); background:rgba(245,158,11,0.05)"><td style="padding:0.18em 0.45em; color:#F59E0B">2026-01</td><td style="padding:0.18em 0.45em; text-align:right; font-weight:bold">3,990</td><td style="padding:0.18em 0.45em; text-align:right">101</td><td style="padding:0.18em 0.45em"></td></tr>
<tr style="border-top:1px solid rgba(255,255,255,0.08); background:rgba(245,158,11,0.05)"><td style="padding:0.18em 0.45em; color:#F59E0B">2026-02 (1~23)</td><td style="padding:0.18em 0.45em; text-align:right">~3,964</td><td style="padding:0.18em 0.45em; text-align:right; color:#94a3b8">—</td><td style="padding:0.18em 0.45em"></td></tr>
<tr style="border-top:1px solid rgba(255,255,255,0.08); background:rgba(167,139,250,0.05)"><td style="padding:0.18em 0.45em; color:#a78bfa">2026-02 (24~28)</td><td style="padding:0.18em 0.45em; text-align:right">~862</td><td style="padding:0.18em 0.45em; text-align:right; color:#94a3b8">—</td><td style="padding:0.18em 0.45em; color:#a78bfa">AI 영상 제작 시작</td></tr>
<tr style="border-top:1px solid rgba(255,255,255,0.08); background:rgba(167,139,250,0.05)"><td style="padding:0.18em 0.45em; color:#a78bfa">2026-03</td><td style="padding:0.18em 0.45em; text-align:right">3,302</td><td style="padding:0.18em 0.45em; text-align:right">35</td><td style="padding:0.18em 0.45em"></td></tr>
<tr style="border-top:1px solid rgba(255,255,255,0.08); background:rgba(167,139,250,0.05)"><td style="padding:0.18em 0.45em; color:#a78bfa">2026-04</td><td style="padding:0.18em 0.45em; text-align:right">2,321</td><td style="padding:0.18em 0.45em; text-align:right; color:#94a3b8">—</td><td style="padding:0.18em 0.45em"></td></tr>
<tr style="border-top:1px solid rgba(255,255,255,0.08); background:rgba(167,139,250,0.05)"><td style="padding:0.18em 0.45em; color:#a78bfa">2026-05</td><td style="padding:0.18em 0.45em; text-align:right">2,331</td><td style="padding:0.18em 0.45em; text-align:right">10</td><td style="padding:0.18em 0.45em"></td></tr>
<tr style="border-top:1px solid rgba(255,255,255,0.08); background:rgba(167,139,250,0.05)"><td style="padding:0.18em 0.45em; color:#a78bfa">2026-06 (1~23)</td><td style="padding:0.18em 0.45em; text-align:right">1,510</td><td style="padding:0.18em 0.45em; text-align:right">14</td><td style="padding:0.18em 0.45em"></td></tr>
</tbody>
</table>
</div>

</div>

---

## 구독자 최고 성장기 (2024-12 ~ 2025-03)

<div style="margin:0.4em 0 0.25em">
<div style="display:flex; gap:0.6em; align-items:center">
  <div style="white-space:nowrap; background:rgba(34,197,94,0.10); border-radius:6px; padding:0.22em 0.7em; font-size:0.82em"><span style="color:#94a3b8">2024-12 &nbsp;</span><strong style="color:#22C55E">384명</strong></div>
  <div style="white-space:nowrap; background:rgba(34,197,94,0.10); border-radius:6px; padding:0.22em 0.7em; font-size:0.82em"><span style="color:#94a3b8">2025-01 &nbsp;</span><strong style="color:#22C55E">415명</strong></div>
  <div style="white-space:nowrap; background:rgba(34,197,94,0.20); border-radius:6px; padding:0.22em 0.7em; font-size:0.88em; border:1px solid rgba(34,197,94,0.5)"><span style="color:#94a3b8">2025-02 ★ &nbsp;</span><strong style="color:#22C55E">427명</strong></div>
  <div style="white-space:nowrap; background:rgba(34,197,94,0.10); border-radius:6px; padding:0.22em 0.7em; font-size:0.82em"><span style="color:#94a3b8">2025-03 &nbsp;</span><strong style="color:#22C55E">319명</strong></div>
</div>
</div>

<table style="width:100%; font-size:0.68em; border-collapse:collapse; line-height:1.2">
<thead>
<tr style="background:rgba(255,255,255,0.12)">
<th style="padding:0.28em 0.6em; text-align:left; width:58%">영상 제목</th>
<th style="padding:0.28em 0.6em; text-align:center; white-space:nowrap; width:10%">업로드</th>
<th style="padding:0.28em 0.6em; text-align:left; width:20%">주제</th>
<th style="padding:0.28em 0.6em; text-align:right; white-space:nowrap; width:12%">조회수</th>
</tr>
</thead>
<tbody>
<tr style="border-top:1px solid rgba(255,255,255,0.08)">
<td style="padding:0.22em 0.6em">Multi-Agent Architectures — 직장 그만두고 시작한 공부</td>
<td style="padding:0.22em 0.6em; text-align:center; color:#94a3b8; white-space:nowrap">24-12-01</td>
<td style="padding:0.22em 0.6em; color:#60A5FA">Multi-Agent</td>
<td style="padding:0.22em 0.6em; text-align:right; color:#22C55E">2,834</td>
</tr>
<tr style="border-top:1px solid rgba(255,255,255,0.08)">
<td style="padding:0.22em 0.6em">Hierarchical Agent Teams Architecture 최종회</td>
<td style="padding:0.22em 0.6em; text-align:center; color:#94a3b8; white-space:nowrap">25-01-06</td>
<td style="padding:0.22em 0.6em; color:#60A5FA">Multi-Agent</td>
<td style="padding:0.22em 0.6em; text-align:right; color:#22C55E">2,561</td>
</tr>
<tr style="border-top:1px solid rgba(255,255,255,0.08)">
<td style="padding:0.22em 0.6em">AI Agent 시대 한국이 선도할 수 있습니다</td>
<td style="padding:0.22em 0.6em; text-align:center; color:#94a3b8; white-space:nowrap">25-01-19</td>
<td style="padding:0.22em 0.6em; color:#60A5FA">Multi-Agent</td>
<td style="padding:0.22em 0.6em; text-align:right; color:#22C55E">1,448</td>
</tr>
<tr style="border-top:1px solid rgba(255,255,255,0.08)">
<td style="padding:0.22em 0.6em">Plan & Execute — AI 추론·추론 방법론</td>
<td style="padding:0.22em 0.6em; text-align:center; color:#94a3b8; white-space:nowrap">25-02-04</td>
<td style="padding:0.22em 0.6em; color:#60A5FA">추론 방법론</td>
<td style="padding:0.22em 0.6em; text-align:right; color:#22C55E">2,708</td>
</tr>
<tr style="border-top:1px solid rgba(255,255,255,0.08); background:rgba(34,197,94,0.06)">
<td style="padding:0.22em 0.6em; font-weight:bold">코딩의 판이 바뀐다 — Prompt를 지배하는 자</td>
<td style="padding:0.22em 0.6em; text-align:center; color:#94a3b8; white-space:nowrap">25-02-07</td>
<td style="padding:0.22em 0.6em; color:#60A5FA">추론 방법론</td>
<td style="padding:0.22em 0.6em; text-align:right; font-weight:bold; color:#F59E0B">3,876</td>
</tr>
<tr style="border-top:1px solid rgba(255,255,255,0.08)">
<td style="padding:0.22em 0.6em">AI로 AI 웹앱 만들기 — 코딩 몰라도 5분에 무료</td>
<td style="padding:0.22em 0.6em; text-align:center; color:#94a3b8; white-space:nowrap">25-03-16</td>
<td style="padding:0.22em 0.6em; color:#60A5FA">실용 튜토리얼</td>
<td style="padding:0.22em 0.6em; text-align:right; color:#22C55E">1,855</td>
</tr>
<tr style="border-top:1px solid rgba(255,255,255,0.08)">
<td style="padding:0.22em 0.6em">AI 해커톤 1등 — 인도 미녀와 6시간에 앱 완성</td>
<td style="padding:0.22em 0.6em; text-align:center; color:#94a3b8; white-space:nowrap">25-03-21</td>
<td style="padding:0.22em 0.6em; color:#60A5FA">해커톤 참가기</td>
<td style="padding:0.22em 0.6em; text-align:right; color:#22C55E">1,673</td>
</tr>
<tr style="border-top:1px solid rgba(255,255,255,0.08); background:rgba(34,197,94,0.06)">
<td style="padding:0.22em 0.6em; font-weight:bold">LLMCompiler — 한국인이 만든 추론 방법론</td>
<td style="padding:0.22em 0.6em; text-align:center; color:#94a3b8; white-space:nowrap">25-03-26</td>
<td style="padding:0.22em 0.6em; color:#60A5FA">추론 방법론</td>
<td style="padding:0.22em 0.6em; text-align:right; font-weight:bold; color:#F59E0B">4,085</td>
</tr>
</tbody>
</table>
<p style="font-size:0.7em; color:#94a3b8; margin-top:0.2em; margin-bottom:0">공통 키워드: <strong style="color:#60A5FA">Multi-Agent 아키텍처 · 추론 방법론</strong></p>

---

## AI YouTube 채널의 유형

<div style="display:grid; grid-template-columns:repeat(3,1fr); grid-template-rows:1fr 1fr; gap:1em; margin-top:0.8em; font-size:0.8em; height:78%">

<div style="background:rgba(34,197,94,0.18); border:1px solid rgba(34,197,94,0.5); border-radius:10px; padding:1.3em 1.2em">
<div style="font-weight:bold; color:#22C55E; margin-bottom:0.5em; white-space:nowrap">✓ 튜토리얼 / 기술 전달형</div>
<div style="font-size:0.85em; color:#94a3b8">도구·라이브러리 사용법 설명<br>검색 유입 강점 · P2 주력</div>
</div>

<div style="background:rgba(255,255,255,0.04); border-radius:10px; padding:1.3em 1.2em; opacity:0.5">
<div style="font-weight:bold; color:#e8f0fe; margin-bottom:0.5em; white-space:nowrap">뉴스 / 트렌드 해설형</div>
<div style="font-size:0.85em; color:#94a3b8">최신 AI 발표·업계 소식<br>발행 속도가 경쟁력</div>
</div>

<div style="background:rgba(245,158,11,0.15); border:1px solid rgba(245,158,11,0.4); border-radius:10px; padding:1.3em 1.2em">
<div style="font-weight:bold; color:#F59E0B; margin-bottom:0.5em; white-space:nowrap">✓ 프로젝트 / 빌드 로그형</div>
<div style="font-size:0.85em; color:#94a3b8">AI 프로젝트 제작 과정 공유<br>개발자 구독자 집중 · P4</div>
</div>

<div style="background:rgba(168,85,247,0.15); border:1px solid rgba(168,85,247,0.4); border-radius:10px; padding:1.3em 1.2em">
<div style="font-weight:bold; color:#a855f7; margin-bottom:0.5em; white-space:nowrap">✓ 개념 / 교육형</div>
<div style="font-size:0.85em; color:#94a3b8">AI 원리·아키텍처·논문 해설<br>깊이 있는 시청자 확보 · P1</div>
</div>

<div style="background:rgba(96,165,250,0.15); border:1px solid rgba(96,165,250,0.4); border-radius:10px; padding:1.3em 1.2em">
<div style="font-weight:bold; color:#60A5FA; margin-bottom:0.5em; white-space:nowrap">✓ 라이브 / 커뮤니티형</div>
<div style="font-size:0.85em; color:#94a3b8">실시간 방송·Q&A 참여<br>팬덤 구축에 강함 · P3</div>
</div>

<div style="background:rgba(255,255,255,0.04); border-radius:10px; padding:1.3em 1.2em; opacity:0.5">
<div style="font-weight:bold; color:#e8f0fe; margin-bottom:0.5em; white-space:nowrap">개인 스토리 / 브이로그형</div>
<div style="font-size:0.85em; color:#94a3b8">공부 일지·커리어 전환기<br>감성적 연결로 구독 전환</div>
</div>

</div>

<div style="font-size:0.65em; text-align:center; color:#94a3b8; margin-top:0.6em">
  현재 Catch Up AI &nbsp;→&nbsp; 🔬 <span style="color:#F59E0B">AI 실험 과정 공유</span> &nbsp;·&nbsp; 📡 <span style="color:#60A5FA">라이브 방송</span> &nbsp;·&nbsp; 🎙️ 시애틀 AI 세미나 소식
</div>

---

<!-- _class: lead -->
<!-- _paginate: false -->

![w:1100](images/dokkaebi_thinking.png)

---

## 선택의 기로 — 그리고 나의 선택

<div style="display:grid;grid-template-columns:1fr 1fr;gap:18px;margin-top:0.4em;">

<div style="background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.15);border-radius:12px;padding:16px 18px;">
<div style="color:#94a3b8;font-size:0.72em;font-weight:bold;letter-spacing:0.08em;margin-bottom:10px;">📌 현재 상황</div>
<ul style="margin:0;padding-left:1.2em;font-size:0.88em;line-height:1.75;color:#e8f0fe;">
  <li>AI 활용 실험을 컨텐츠로 제작 중</li>
  <li>조회수·시청 시간 등 아직 부진</li>
  <li>기술 전달형 채널 복귀 의사 없음</li>
</ul>
</div>

<div style="background:rgba(34,197,94,0.08);border:1px solid rgba(34,197,94,0.35);border-radius:12px;padding:16px 18px;">
<div style="color:#22C55E;font-size:0.72em;font-weight:bold;letter-spacing:0.08em;margin-bottom:10px;">✅ 나의 선택</div>
<ul style="margin:0;padding-left:1.2em;font-size:0.88em;line-height:1.75;color:#e8f0fe;">
  <li>관심 가는 AI 실험 지속 추진</li>
  <li>컨텐츠 제작까지 AI 활용 실험</li>
  <li>구독자 관심 확대 방법 병행 탐색</li>
</ul>
</div>

</div>

<div style="margin-top:16px;background:rgba(245,158,11,0.10);border-left:4px solid #F59E0B;border-radius:0 8px 8px 0;padding:12px 16px;font-size:0.9em;color:#fde68a;line-height:1.6;">
  나만의 컨텐츠를 만들려면 <strong style="color:#F59E0B;">나만의 기록</strong>이 필요하다.<br>
  그것이 내가 생각하는 <strong style="color:#F59E0B;">AI 경쟁력의 핵심</strong>이다.
</div>

---

<!-- _class: lead invert -->

# 기록이 AI를 강하게 만든다

AI 크리에이터의 경쟁력은 기록에서 시작된다

---

## 기록 → Context → AI → 배포 순환

<div style="display:grid;grid-template-columns:auto 36px auto 36px auto;grid-template-rows:auto 28px auto;align-items:center;justify-items:center;margin:70px auto 62px;width:fit-content;gap:0;">
  <div style="background:#22C55E;color:#fff;padding:10px 20px;border-radius:10px;font-weight:bold;font-size:0.9em;text-align:center;min-width:80px;">📝<br>기록</div>
  <div style="color:#94a3b8;font-size:1.5em;">→</div>
  <div style="background:#38BDF8;color:#0f172a;padding:10px 20px;border-radius:10px;font-weight:bold;font-size:0.9em;text-align:center;min-width:80px;">🧠<br>Context</div>
  <div style="color:#94a3b8;font-size:1.5em;">→</div>
  <div style="background:#8B5CF6;color:#fff;padding:10px 20px;border-radius:10px;font-weight:bold;font-size:0.9em;text-align:center;min-width:80px;">🤖<br>AI 협업</div>
  <div style="color:#94a3b8;font-size:1.5em;line-height:1;">↑</div>
  <div></div><div></div><div></div>
  <div style="color:#94a3b8;font-size:1.5em;line-height:1;">↓</div>
  <div style="background:#22C55E;color:#fff;padding:10px 20px;border-radius:10px;font-weight:bold;font-size:0.9em;text-align:center;min-width:80px;">✨<br>새 경험</div>
  <div style="color:#94a3b8;font-size:1.5em;">←</div>
  <div style="background:#F87171;color:#fff;padding:10px 20px;border-radius:10px;font-weight:bold;font-size:0.9em;text-align:center;min-width:80px;">📢<br>배포</div>
  <div style="color:#94a3b8;font-size:1.5em;">←</div>
  <div style="background:#F59E0B;color:#0f172a;padding:10px 20px;border-radius:10px;font-weight:bold;font-size:0.9em;text-align:center;min-width:80px;">🎬<br>콘텐츠</div>
</div>

- 기록 없이: AI → Generic 결과 (내 경험 반영 안 됨)
- **기록 있을 때: AI + Context → 나만의 결과, 내 언어, 내 스타일**

---

<!-- _class: lead -->
<!-- _paginate: false -->

![w:880](images/dokkaebi_Live_Recap.png)

---

## 이 기록들이 AI를 위한 Context가 된다

<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:7px;margin-top:12px;margin-bottom:7px;">
  <div style="background:rgba(56,189,248,0.15);border:1px solid #38BDF8;border-radius:8px;padding:7px 10px;">
    <div style="font-size:0.95em;">🎙️</div>
    <div style="color:#38BDF8;font-weight:bold;font-size:0.78em;margin:3px 0 1px;">GOBI 캡처</div>
    <div style="color:#94a3b8;font-size:0.64em;">2026-06-21 Capture.md · 현장 음성 맥락</div>
  </div>
  <div style="background:rgba(139,92,246,0.15);border:1px solid #8B5CF6;border-radius:8px;padding:7px 10px;">
    <div style="font-size:0.95em;">💬</div>
    <div style="color:#8B5CF6;font-weight:bold;font-size:0.78em;margin:3px 0 1px;">AI ChatHistory</div>
    <div style="color:#94a3b8;font-size:0.64em;">Weekly Planning.md · 실제 작업 내역</div>
  </div>
  <div style="background:rgba(245,158,11,0.15);border:1px solid #F59E0B;border-radius:8px;padding:7px 10px;">
    <div style="font-size:0.95em;">📺</div>
    <div style="color:#F59E0B;font-weight:bold;font-size:0.78em;margin:3px 0 1px;">YouTube 자막</div>
    <div style="color:#94a3b8;font-size:0.64em;">captions.sbv · 방송 전체 흐름 기준</div>
  </div>
  <div style="background:rgba(248,113,113,0.15);border:1px solid #F87171;border-radius:8px;padding:7px 10px;">
    <div style="font-size:0.95em;">📅</div>
    <div style="color:#F87171;font-weight:bold;font-size:0.78em;margin:3px 0 1px;">Weekly Planning</div>
    <div style="color:#94a3b8;font-size:0.64em;">2026-06-22 Planning.md · 주간 맥락</div>
  </div>
  <div style="background:rgba(34,197,94,0.10);border:1px solid #22C55E;border-radius:8px;padding:7px 10px;">
    <div style="font-size:0.95em;">📓</div>
    <div style="color:#22C55E;font-weight:bold;font-size:0.78em;margin:3px 0 1px;">Daily Roundup</div>
    <div style="color:#94a3b8;font-size:0.64em;">2026-06-21 Claude Code.md · 당일 정리</div>
  </div>
  <div style="background:rgba(34,197,94,0.15);border:1px solid #22C55E;border-radius:8px;padding:7px 10px;">
    <div style="font-size:0.95em;">📋</div>
    <div style="color:#22C55E;font-weight:bold;font-size:0.78em;margin:3px 0 1px;">Live Rundown</div>
    <div style="color:#94a3b8;font-size:0.64em;">Live15 Weekly Rundown.md · 방송 계획</div>
  </div>
</div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:7px;margin-bottom:7px;">
  <div style="background:rgba(148,163,184,0.12);border:1px solid #64748b;border-radius:8px;padding:7px 10px;">
    <div style="font-size:0.95em;">🔧</div>
    <div style="color:#94a3b8;font-weight:bold;font-size:0.78em;margin:3px 0 1px;">시스템 변경 기록</div>
    <div style="color:#64748b;font-size:0.64em;">CLAUDE.md · AGENTS.md · .claude/skills/* · 기술 변화 추적</div>
  </div>
  <div style="background:rgba(34,197,94,0.08);border:2px solid #22C55E;border-radius:8px;padding:7px 14px;display:flex;flex-direction:column;justify-content:center;">
    <div style="color:#22C55E;font-weight:bold;font-size:0.84em;">🎬 → Live #15 요약 영상</div>
    <div style="color:#94a3b8;font-size:0.68em;margin-top:3px;">video-slide-plan.md · 16장 슬라이드 플랜 완성</div>
  </div>
</div>
<div style="text-align:center;color:#64748b;font-size:0.75em;">
  하나의 자막만으로는 부족했다 — 7가지 기록이 맥락을 완성했다
</div>

---

<!-- _class: lead -->
<!-- _paginate: false -->

<div style="margin-top:-80px;">

![w:540](images/CatchUpAI.jpg)

</div>

---

## 기록, AI 시대의 경쟁력

<div style="font-size:0.83em;margin-top:22px;">

<div style="color:#cbd5e1;margin-bottom:20px;line-height:1.8;">굳이 컨텐츠를 만들기 위해서만 기록이 필요한 것은 아닙니다.<br><strong style="color:#F59E0B;">AI를 잘 사용하려면 기록이 필요합니다.</strong></div>

<div style="background:rgba(245,158,11,0.12);border:2px solid #F59E0B;border-radius:12px;padding:12px 20px;text-align:center;margin-bottom:20px;">
  <span style="color:#F59E0B;font-weight:bold;font-size:1.05em;">✨ Gold in, Gold out &nbsp;·&nbsp; Garbage in, Garbage out</span><br>
  <span style="color:#94a3b8;font-size:0.85em;">AI에게 좋은 Context를 주어야 좋은 답을 얻을 수 있습니다</span>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-bottom:20px;">
  <div style="background:rgba(56,189,248,0.10);border:1px solid rgba(56,189,248,0.35);border-radius:10px;padding:12px 14px;">
    <div style="color:#38BDF8;font-weight:bold;font-size:0.88em;margin-bottom:6px;">🎯 나에게 딱 맞는 AI</div>
    <div style="color:#cbd5e1;font-size:0.82em;line-height:1.7;">AI가 나를 알려면 내 정보가 필요합니다.<br>내 기록이 곧 나만의 Context입니다.</div>
  </div>
  <div style="background:rgba(34,197,94,0.10);border:1px solid rgba(34,197,94,0.35);border-radius:10px;padding:12px 14px;">
    <div style="color:#22C55E;font-weight:bold;font-size:0.88em;margin-bottom:6px;">🚀 AI 시대 경쟁력</div>
    <div style="color:#cbd5e1;font-size:0.82em;line-height:1.7;">기록하는 사람이 AI를 더 잘 씁니다.<br>오늘 메모 하나가 경쟁력의 시작입니다.</div>
  </div>
</div>

<div style="background:rgba(139,92,246,0.12);border-left:4px solid #8B5CF6;border-radius:0 8px 8px 0;padding:10px 16px;color:#e2e8f0;font-size:0.85em;">
  AI 시대 경쟁력을 갖기 위해 <strong style="color:#8B5CF6;">지금 바로 기록을 시작하세요</strong>
</div>

</div>

---

<!-- _class: lead invert -->

## 기록이 AI를 강하게 만듭니다

오늘 집에 가서 **메모 하나** 쓰세요.
그게 AI와의 협업의 시작입니다.

---

<div style="display:flex;gap:60px;justify-content:center;margin-bottom:20px;">
  <div style="text-align:center;">
    <div style="background:#fff;padding:10px;border-radius:10px;display:inline-block;">
      <img src="qr_youtube.png" style="width:140px;height:140px;display:block;">
    </div>
    <p style="font-size:0.78em;margin-top:8px;"><a href="https://www.youtube.com/@catchupai" target="_blank" rel="noopener" style="color:#60A5FA;text-decoration:none;">📺 youtube.com/@catchupai</a></p>
  </div>
  <div style="text-align:center;">
    <div style="background:#fff;padding:10px;border-radius:10px;display:inline-block;">
      <img src="qr_website.png" style="width:140px;height:140px;display:block;">
    </div>
    <p style="font-size:0.78em;margin-top:8px;"><a href="https://catchupai.net/" target="_blank" rel="noopener" style="color:#60A5FA;text-decoration:none;">🌐 catchupai.net</a></p>
  </div>
</div>

<div style="font-size:0.78em;line-height:1.9;color:#e2e8f0;">

📺 **Catch Up AI** — AI를 일상에 적용해 보는 다양한 실험
💬 **Builders Lounge** — Builder들의 모임 #club-sg-ai · gobispace.com
🛠️ **Utah Project** — 비개발자 Vibe Coding 앱 개발 Guide
🏠 **Channel Membership** — Members Only 선공개 콘텐츠 (시애틀 AI 생태계)
📧 **1:1 세션** — AI4PKM / VibeLearn AI 상담

</div>

**감사합니다** 🌿

<!-- 질문 있으신 분? -->
