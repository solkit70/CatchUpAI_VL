---
title: "WorkLog 2026-06-21 — The-AI-Powered-Creator M4~M6"
created: 2026-06-21 21:00:00
tags:
  - the-ai-powered-creator
  - worklog
  - m4-core-message
  - m5-content-workflow
  - m6-slide-deck
---

# WorkLog 2026-06-21 — M4~M6 발표 준비 작업

**Topic**: The-AI-Powered-Creator
**D-day**: D-5 (2026-06-26 창발 Product Group)
**작업 시간**: 2026-06-21 오후 세션
**모듈 범위**: M4 (Core Message), M5 (Content Workflow), M6 (Slide Deck)

---

## 세션 요약

이전 세션(2026-06-19 M4 착수)에서 작성된 핵심 참조 파일들을 바탕으로, 오늘 사용자가 제공한 새로운 발표 구조 아이디어를 반영하여 v2.0으로 전면 재편 후 슬라이드 초안 완성.

**핵심 변경**: 오프닝을 Tehaleh 영상 36분 제작 과정 데모로 전면 교체 + 사전 준비/후작업 섹션 신규 추가 + Tehaleh→기록 브릿지 추가

---

## 완료 작업

### M4: Core Message 업데이트

**`04-Core-Message/presentation-structure.md`** → **v2.0으로 개편**
- v1.0 (15장, 40분) → v2.0 (19장, ~39분)
- 전체 흐름 재설계: 오프닝 데모(7장) + 전환(3장) + 브릿지(2장) + 본론(7장)
- v1.0 오프닝(뚝딱 순간 데모, 2장) → v2.0 오프닝(Tehaleh 5단계 클립, 7장)
- v2.0 변경 이유 주석 포함

### M5: Content Workflow 착수

**`05-Content-Workflow/ai-creator-workflow.md`** — **신규 작성** ✅
- 발표 S15용 핵심 Mermaid 다이어그램: 기록→Context→AI협업→콘텐츠→배포→새경험 순환
- PNW 컬러 테마 적용 (#22C55E forest green, #F59E0B mountain gold, #8B5CF6 purple)
- 4개 사례와 워크플로우 매핑 테이블
- "기록 없이 vs 기록 있을 때" 대비 예시

### M6: Slide Deck 착수 및 전체 완성

**`06-Slide-Deck/slide-draft.md`** — **신규 작성** ✅
- 19장 전체 슬라이드 초안 (제목 + bullet 3개 + 발표자 노트 + 시각 자료 명세)
- 슬라이드별 예상 시간, 파트 구분
- 발표 당일 체크리스트 포함 (클립 편집, YouTube 업로드, 프로젝터 테스트)

**`06-Slide-Deck/demo-assets.md`** — **신규 작성** ✅
- 5단계 영상 클립 목록 (`clip_01_roadmap.mp4` ~ `clip_05_audio.mp4`)
- Tehaleh 완성본 YouTube 업로드 일정 (D-3까지)
- 발표 도구 비교 (Google Slides vs Marp vs Slidev)
- D-3 / D-2 / D-1 / D-Day 체크리스트

**`06-Slide-Deck/presentation-0626.md`** — **Marp 슬라이드 파일 작성** ✅
- Marp for VS Code 확장 설치 완료 (v3.5.1)
- 19장 완전한 Marp 형식 슬라이드
- PNW 컬러 CSS 커스텀 테마 적용 (#0f172a 배경, #22C55E 강조색)
- S3~S7 동영상 클립: `<video src="clips/clip_0N_xxx.mp4" controls>` 태그 삽입
- S15 Mermaid 다이어그램 인라인 포함
- HTML / PDF / PPTX 내보내기 모두 지원

---

## 산출물 목록

| 파일 | 상태 | 비고 |
|------|------|------|
| `04-Core-Message/presentation-structure.md` | ✅ v2.0 | v1.0 → v2.0 개편 완료 |
| `05-Content-Workflow/ai-creator-workflow.md` | ✅ 완성 | Mermaid 다이어그램 + 4개 사례 |
| `06-Slide-Deck/slide-draft.md` | ✅ 완성 | 19장, 발표자 노트 포함 |
| `06-Slide-Deck/demo-assets.md` | ✅ 완성 | 클립 목록 + 일정 체크리스트 |
| `06-Slide-Deck/presentation-0626.md` | ✅ 완성 | Marp 형식, 즉시 미리보기 가능 |

---

## 발표 구조 v2.0 최종 확정

| 파트 | 슬라이드 | 시간 |
|------|---------|------|
| 오프닝: Tehaleh 36분 데모 | S1~S7 (7장) | ~10분 |
| 전환: 뚝딱이 아님 | S8~S10 (3장) | ~5분 |
| 브릿지: 기록 연결 | S11~S12 (2장) | ~3분 |
| 1부: 자기소개 | S13~S14 (2장) | ~5분 |
| 2부: 기록 논리 | S15~S16 (2장) | ~5분 |
| 3부: 사례 (압축) | S17 (1장) | ~5분 |
| 4부: 실행 제안 | S18 (1장) | ~4분 |
| 마무리 | S19 (1장) | ~2분 |
| **합계** | **19장** | **~39분** |

---

## 다음 세션 작업 (D-5 → D-3)

### 사용자 작업 필요 (외부)
- [ ] 5개 영상 클립 편집 (각 20~30초) → `06-Slide-Deck/clips/` 폴더에 저장
- [x] Tehaleh 영상 Qwen3-TTS 한국어·영어 버전 제작 + 렌더링
- [x] YouTube 제목·설명·챕터·태그·썸네일 문구 준비 → [[20260621_M1-M4_Tehaleh-Community-Video#YouTube 업로드 메타데이터|Tehaleh 영상 YouTube 업로드 메타데이터]]
- [ ] 한국어·영어 영상 YouTube 업로드 + 공개 URL 상호 연결

### Claude Code 후속 작업
- [ ] `05-Content-Workflow/README.md` 작성 (M5 완료 처리용)
- [ ] `04-Core-Message/README.md` 작성
- [ ] `03-Channel-Topic-Evolution/presentation-use-snippets.md` (60초 자기소개 문장)
- [ ] `vl_materials/experience-inventory.md` Case 5 추가 (Tehaleh 영상 + 오늘 데모)
- [ ] Roadmap M5/M6 진행률 업데이트
- [ ] S1 YouTube 썸네일 이미지 교체 (placeholder → 실제 이미지)
- [ ] VS Code settings.json `"markdown.marp.enableHtml": true` 추가 확인

### 발표 리허설 계획 (D-2, 2026-06-24)
- 전체 39분 타이밍 리허설
- 클립 재생 테스트 (HTML 모드)
- Q&A 예상 질문 준비

---

## 세션 인사이트

1. **발표 구조 재편 결정**: 오프닝을 "이론 데모"에서 "실제 작업 과정 데모"로 전환 → 청중 체험형 오프닝이 더 임팩트
2. **Marp 도입**: Google Slides보다 Marp HTML이 Claude Code와의 협업에 유리 (마크다운 직접 수정, 버전 관리 가능)
3. **동영상 클립 전략**: 각 20~30초 클립이 핵심 — 실제 작업 시간의 증거이자 청중의 이해를 돕는 시각적 증거

---

*M4~M6 WorkLog — 2026-06-21, VibeLearn AI*
