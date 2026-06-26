---
title: "M6 README — 슬라이드 초안과 발표 노트"
created: 2026-06-22 10:00:00
tags:
  - the-ai-powered-creator
  - m6-slide-deck
---

# M6 — 슬라이드 초안과 발표 노트

**상태**: ✅ 완료 (2026-06-21~22)
**예상 시간**: 3h | **실제 시간**: ~3h

---

## 문서 목록 (학습 순서)

| 순서 | 문서 | 설명 |
|------|------|------|
| 1 | [slide-draft.md](slide-draft.md) | 19장 슬라이드 전체 초안 — 제목 + bullet 3개 + 발표자 노트 + 시각 자료 명세 |
| 2 | [demo-assets.md](demo-assets.md) | 데모 자산 목록 — 완성본 MP4, 5단계 클립, 이미지, 다이어그램 + D-day 체크리스트 |
| 3 | [presentation-0626.md](presentation-0626.md) | Marp 형식 슬라이드 파일 — VS Code에서 바로 미리보기 가능 (PNW 다크 테마) |

---

## 발표용 영상 클립

`clips/` 폴더에 저장:

| 파일 | 슬라이드 | 내용 |
|------|---------|------|
| `clips/clip_01_roadmap.mp4` | S3 | VibeLearn AI Roadmap 작성 화면 |
| `clips/clip_02_research.mp4` | S4 | tehaleh-research.md 작성 화면 |
| `clips/clip_03_slideplan.mp4` | S5 | video-slide-plan.md 작성 화면 |
| `clips/clip_04_remotion.mp4` | S6 | VS Code + Remotion Studio 미리보기 |
| `clips/clip_05_audio.mp4` | S7 | gen_audio.py 실행 + 렌더링 화면 |

**상태**: ✅ 5개 클립 모두 저장 완료 (2026-06-22)

---

## Marp 슬라이드 사용법

1. VS Code에서 `presentation-0626.md` 열기
2. `Cmd/Ctrl+Shift+P` → "Marp: Open Preview"
3. 클립 재생: HTML 모드에서만 작동 (`Marp: Export as HTML`)
4. VS Code 설정 필요: `"markdown.marp.enableHtml": true`

---

## 이전/다음 모듈

- 이전: [M5 — AI 콘텐츠 제작 워크플로우](../05-Content-Workflow/README.md)
- 다음: [M7 — 리허설, 배포, 후속 콘텐츠 패키지](../07-Delivery-and-Distribution/README.md)
