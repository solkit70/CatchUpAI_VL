---
title: "M5 — 슬라이드 덱과 발표 노트"
created: 2026-09-13 15:45:00
status: 진행 중
tags:
  - vibelearn-ai
  - m5
---

# M5 — 슬라이드 덱과 발표 노트

**상태**: ✅ **9/16 사용자 리뷰 반영 완료 — 14장** (5·7 장을 둘로 나누고 8·9·11·12·13 장 내용 재작성) · 발표 당일
**묻는 것**: *"10분 안에 그래프로 바닥을 보여 주고, 틀린 판정을 전환점으로 쓰고, 한 문장으로 닫을 수 있는가."*

## 📚 읽는 순서

1. [slides/presentation-0916.md](slides/presentation-0916.md) — **Marp 덱 14장** (6/26 덱과 같은 테마 — "2편") · 렌더: [presentation-0916.html](slides/presentation-0916.html) · [presentation-0916.pdf](slides/presentation-0916.pdf)
2. [slides/speaker-notes.md](slides/speaker-notes.md) — 장별 발표 노트 + 계획 시간 (합계 약 11:40 — 리허설에서 조정)
3. [images/](images/) — 그래프 3장: [chart-1-subscribers.png](images/chart-1-subscribers.png) 횡보→돌파 · [chart-2-weekly-net.png](images/chart-2-weekly-net.png) 주별 순증 · [chart-3-retention.png](images/chart-3-retention.png) 지속률 16→27%
4. [scripts/make_charts.py](scripts/make_charts.py) — 그래프 재생성 (`daily.json` → 9/7=4,320 역산, 지속률은 M3 표 그대로)
5. [rehearsal-log.md](rehearsal-log.md) — 장별 계획 시간 · 실측 칸 · 뺄 순서

## 덱 구조 (9/16 리뷰 후)

| 장 | 슬라이드 | 시간 |
|---|---|---|
| 훅 | 1 표지(6/26 썸네일·QR) · 2 지난 발표의 마지막 표 + 발표 이후·최근 6주 | 0:55 |
| 바닥 | 3 그래프(9/15 4,330) · 4 두 가지를 바꿨다 (작전 1 자막 7/14 · 작전 2 퀄리티 7/19) | 1:40 |
| 무엇을 했나 | 5 채널 영상 세 부류 · 6 87편 부류·언어별 성적 · 7 가설이 틀렸다 1.71→0.86 · 8 사람의 개입은 퀄리티의 조건(기술 영상 QR) · 9 작전 2 효과·검색 0.76배·앱 계획 | 4:35 |
| 숫자 | 10 시차 그래프 · 11 시청 지속률 18→16→27% | 2:00 |
| 배운 것 | 12 퀄리티 제고 사례 3건(팩트체크·이해하기 쉽게·자막 STT) · 13 이번 조사를 통해 배운 것 · 14 GitHub QR | 2:25 |

## 렌더 / 수정

```powershell
cd slides
# 본문(_body.md)을 고친 뒤:
# ⚠️ PowerShell 5.1 의 Get-Content 는 ANSI 로 읽어 한글이 깨진다 (9/15 실제 발생) — Python 으로 합친다
python -c "open('presentation-0916.md','w',encoding='utf-8').write(open('_style-header.md',encoding='utf-8').read()+open('_body.md',encoding='utf-8').read())"
npx -y @marp-team/marp-cli@latest presentation-0916.md --html --allow-local-files -o presentation-0916.html
npx -y @marp-team/marp-cli@latest presentation-0916.md --pdf  --allow-local-files -o presentation-0916.pdf
# GitHub htmlpreview 용 (차트·썸네일·QR 을 base64 로 인라인) — 05-Slide-Deck 에서
python -c "import base64,re,os;t=open('slides/presentation-0916.html',encoding='utf-8').read();f=lambda m:'src=\"data:image/'+('jpeg' if m.group(1).endswith('.jpg') else 'png')+';base64,'+base64.b64encode(open(os.path.join('slides',m.group(1)),'rb').read()).decode();open('slides/presentation-0916-preview.html','w',encoding='utf-8').write(re.sub(r'src=\"(\.\./images/[^\"]+\.(?:png|jpg))',f,t))"
```

## 이전 / 다음

- 이전: [../04-Core-Message/](../04-Core-Message/) · 다음: `06-Distribution/` (발표 후 — Substack)
