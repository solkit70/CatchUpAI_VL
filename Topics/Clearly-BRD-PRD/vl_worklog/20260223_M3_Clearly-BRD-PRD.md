# WorkLog - M3: Clearly 앱 소개 영상 제작 (2일차)

**날짜**: 2026-02-23
**Topic**: Clearly-BRD-PRD
**모듈**: M3 - Clearly App 소개 영상 제작
**학습 시간**: 약 1시간
**이전 세션**: [20260222_M3_Clearly-BRD-PRD.md](20260222_M3_Clearly-BRD-PRD.md)

---

## 오늘의 학습 목표

- [x] 스크립트 수정 — 이름 제거 + AI 팁 슬라이드 추가
- [x] 스크린샷 8장 수집 → `_files_/` 폴더에 저장
- [x] 슬라이드 파일에 스크린샷 이미지 경로 삽입
- [x] Output Tool 슬라이드 텍스트 업데이트 (실제 스크린샷 기준)
- [x] GitHub 커밋 & 푸시
- [ ] `/markdown-video` 스킬로 MP4 영상 생성 (다음 세션)

---

## 작업 컨텍스트

**2022-02-22 세션에서 이어지는 작업입니다.**

| 전 세션 완료 | 이번 세션 목표 |
|------------|-------------|
| 영상 스크립트 27장 작성 | 스크립트 수정 + 스크린샷 삽입 |
| Deckset 슬라이드 변환 | 슬라이드 파일 완성 (이미지 포함) |
| README.md, WorkLog 작성 | GitHub 푸시 |
| GitHub 커밋 & 푸시 | **다음 세션: MP4 영상 생성** |

**현재 상태**: 슬라이드 파일 완성 ✅ — 영상 생성만 남음

---

## 진행 내용

### Phase 2-A: 스크립트 수정 ✅

**변경 사항:**

1. **이름 제거**
   - 수정 전: `"여러분, 안녕하세요! Catch Up AI 채널의 창수입니다."`
   - 수정 후: `"여러분, 안녕하세요! Catch Up AI 입니다."`
   - 슬라이드 파일 첫 번째 스피커노트도 동일하게 수정

2. **AI 팁 슬라이드 추가 (슬라이드 15-B)**
   - 위치: BRD Wizard 답변 팁 슬라이드 다음
   - 제목: `🤖 프로 팁: AI로 BRD/PRD 답변 미리 준비하기`
   - 내용: Clearly Wizard 질문이 AI 생성이라 매번 달라짐 → 사전에 AI 도구(Claude Code, ChatGPT 등)와 프로젝트를 충분히 논의해두면 어떤 질문이 나와도 바로 고품질 답변 생성 가능
   - **핵심 메시지**: AI 도구가 핵심, 특정 도구에 국한하지 않음

3. **메타데이터 업데이트**:
   - 슬라이드 수: 27장 → 28장
   - 예상 영상 길이: 17-20분 → 18-22분

> **수정 과정 인사이트**: 처음에 "Claude Code로 답변 준비하기"로 제목을 작성했으나 사용자가 "AI 도구가 핵심, Claude Code만 국한하지 말 것"을 요청해 수정. 특정 도구 홍보가 아닌 방법론(AI 활용)에 집중하는 것이 올바른 방향.

---

### Phase 3: 스크린샷 수집 ✅

사용자가 직접 캡처한 8개 스크린샷을 `_files_/` 폴더에 저장:

| # | 파일명 | 내용 | 비고 |
|---|--------|------|------|
| 1 | `clearly-main_before_login.png` | 랜딩 페이지 ("Requirements Made Clear") | 계획에 없던 추가 화면 |
| 2 | `clearly-main.png` | 로그인 후 대시보드 | "Welcome back, Changsoo Park!" |
| 3 | `project-create.png` | 새 프로젝트 생성 화면 | Title + Initial Idea 입력 필드 |
| 4 | `brd-wizard.png` | BRD Wizard 질문 화면 | "Questions answered: 1/5+", 20% 진행 |
| 5 | `brd-result.png` | 생성된 BRD 문서 | Approve/Edit/Regenerate 버튼 |
| 6 | `prd-result.png` | 생성된 PRD 문서 | — |
| 7 | `output-tool.png` | Output Tool 선택 화면 | Vibe Coding + AI Coding 두 카테고리 |
| 8 | `homepage.png` | 완성된 Catch Up AI 홈페이지 | "Catching Up with AI Innovation" |

**발견**: `output-tool.png` 스크린샷에 스크립트에 없던 도구들이 포함됨
- Vibe Coding Tools: v0, Lovable, Bolt.new, **Replit**, **Firebase Studio**
- AI Coding Tools: Claude Code, Cursor, **OpenAI Codex**, **Google Antigravity**
→ 슬라이드 텍스트를 실제 스크린샷과 일치하도록 즉시 업데이트

---

### Phase 3-B: 슬라이드 파일에 이미지 경로 삽입 ✅

**산출물**: `03-Clearly-Intro-Video/clearly-intro-script - slides.md` (완성본)

Deckset `![right fit](_files_/파일명.png)` 형식으로 8개 슬라이드에 이미지 삽입:

| 슬라이드 | 삽입된 이미지 |
|---------|-------------|
| ✨ Clearly, 한 줄 소개 | `clearly-main_before_login.png` |
| 🚀 Clearly 앱: 핵심 기능 | `clearly-main.png` |
| 🆕 Step 1: 프로젝트 생성 | `project-create.png` |
| 🤖 Step 2: BRD Wizard | `brd-wizard.png` |
| 📄 Step 3: BRD 생성 및 검토 | `brd-result.png` |
| 🔧 Step 4: PRD Wizard | `prd-result.png` |
| 🔗 Step 5: Output Tool 선택 | `output-tool.png` |
| 🎉 완성된 홈페이지 | `homepage.png` |

**적용 규칙 (SKILL.md 기준)**:
- 이미지는 `^` 스피커노트 바로 직전에 배치
- 콘텐츠 슬라이드에는 `![right fit]()` 형식 사용 (PRIMARY FORMAT)
- 존재하지 않는 이미지는 절대 참조 금지 — 8개 모두 실제 파일 확인 후 삽입

---

### Phase 3-C: GitHub 커밋 & 푸시 ✅

**커밋**: `d646aff`
```
docs: Add screenshots and update slides for M3 Clearly intro video - 2026-02-23
```

**변경 파일 (10개)**:
- `clearly-intro-script - slides.md` — 이미지 삽입 + Output Tool 텍스트 업데이트
- `clearly-intro-script.md` — 스크립트 수정 (이름 제거, 팁 슬라이드, 메타데이터)
- `_files_/` 폴더의 스크린샷 8개 (신규)

---

## DoD 체크리스트

| 항목 | 상태 |
|------|------|
| `03-Clearly-Intro-Video/` 폴더 생성 | ✅ (2/22) |
| 영상 스크립트 (clearly-intro-script.md) 작성 | ✅ (2/22) |
| Deckset 슬라이드 (clearly-intro-script - slides.md) 변환 | ✅ (2/22) |
| README.md 작성 | ✅ (2/22) |
| 스크립트 수정 (이름 제거 + AI 팁 슬라이드) | ✅ (2/23) |
| 스크린샷 8장 수집 → `_files_/` 저장 | ✅ (2/23) |
| 슬라이드 파일에 이미지 경로 삽입 | ✅ (2/23) |
| GitHub 커밋 & 푸시 | ✅ (2/23) |
| 오디오 생성 (OpenAI TTS) | ⏳ 다음 세션 |
| AI 슬라이드 이미지 생성 (Gemini) | ⏳ 다음 세션 |
| MP4 합성 (FFmpeg) | ⏳ 다음 세션 |

**완료율**: 8/11 (73%) — MP4 영상 생성만 남음

---

## Daily Retrospective

### What went well (잘된 점)
- **스크린샷 → 슬라이드 삽입 완성**: 8개 스크린샷을 정확한 슬라이드에 배치하여 시각적으로 완성된 슬라이드 파일 완성
- **실제 스크린샷 기반 업데이트**: output-tool.png를 보고 스크립트에 빠진 도구들(Replit, Firebase Studio, OpenAI Codex, Google Antigravity)을 즉시 발견하고 수정 — 정확성 향상
- **AI 팁 슬라이드**: Clearly Wizard 질문이 AI 생성이라 변동성이 있다는 실제 경험을 영상 콘텐츠로 전환한 유용한 팁

### What could be improved (개선할 점)
- 스크린샷 준비를 M3 시작 전에 했다면 2/22 한 세션에 전체 완료 가능했음
- AI 도구 이름 표현: 특정 도구명(Claude Code)이 아닌 카테고리(AI 도구)로 먼저 생각하는 습관 필요

### Insights (인사이트)
- **스크린샷이 슬라이드 내용을 검증한다**: output-tool.png에서 스크립트에 없던 도구들을 발견. 스크린샷 수집이 단순한 시각 자료 추가가 아니라 내용 정확성 검증 역할도 함
- **Deckset `![right fit]()` 패턴**: 텍스트(왼쪽) + 이미지(오른쪽) 레이아웃이 데모 슬라이드에 매우 적합. 텍스트로 설명하고 오른쪽에 실제 화면을 보여주는 구성이 교육 영상에 효과적
- **markdown-video 스킬 준비 완료**: 슬라이드 파일이 완성됐으므로 다음 세션에서 바로 영상 생성 가능

### Tomorrow's focus (다음 세션에서 할 일)

#### Step 1: markdown-video 스킬 SKILL.md 읽기
```
Topics/Claude-Skills/temp-claude-obsidian-skills/markdown-video/SKILL.md
```

#### Step 2: 오디오 생성
```bash
python generate_audio.py "clearly-intro-script - slides.md" --output-dir "audio"
```
- 모델: OpenAI TTS (`gpt-4o-mini-tts` 또는 `tts-1`)
- 음성: nova (한국어 자연스러운 발음)
- 소스: 슬라이드의 `^` 스피커노트 텍스트

#### Step 3: AI 슬라이드 이미지 생성
```bash
python create_slides_gemini.py "clearly-intro-script - slides.md" \
  --output-dir "slides-gemini" --style "professional" --auto-approve
```
- 이미지 있는 슬라이드: 실제 스크린샷 사용 (생성 불필요)
- 이미지 없는 슬라이드: Gemini로 professional 스타일 이미지 생성

#### Step 4: MP4 합성
```bash
python slides_to_video.py \
  --slides-dir "slides-gemini" --audio-dir "audio" --output "clearly-intro.mp4"
```

**API 요구사항**: `OPENAI_API_KEY`, `GEMINI_API_KEY` 환경변수 확인 필요
**예상 비용**: ~$1.30 (Gemini 이미지 ~20장 + OpenAI TTS ~18-22분)
**스킬 경로**: `Topics/Claude-Skills/temp-claude-obsidian-skills/markdown-video/`

---

## 산출물 요약

### 오늘 변경/추가된 파일

| 파일 | 상태 | 설명 |
|------|------|------|
| `clearly-intro-script.md` | ✏️ 수정 | 28장, 18-22분, 이름 제거, AI 팁 슬라이드 추가 |
| `clearly-intro-script - slides.md` | ✏️ 수정 | 이미지 8개 삽입, Output Tool 텍스트 업데이트 |
| `_files_/clearly-main_before_login.png` | 🆕 추가 | 랜딩 페이지 스크린샷 |
| `_files_/clearly-main.png` | 🆕 추가 | 로그인 후 대시보드 |
| `_files_/project-create.png` | 🆕 추가 | 프로젝트 생성 화면 |
| `_files_/brd-wizard.png` | 🆕 추가 | BRD Wizard 질문 화면 |
| `_files_/brd-result.png` | 🆕 추가 | 생성된 BRD 문서 |
| `_files_/prd-result.png` | 🆕 추가 | 생성된 PRD 문서 |
| `_files_/output-tool.png` | 🆕 추가 | Output Tool 선택 화면 |
| `_files_/homepage.png` | 🆕 추가 | 완성된 홈페이지 |

### 현재 03-Clearly-Intro-Video 폴더 구조

```
03-Clearly-Intro-Video/
├── README.md                                    ✅
├── clearly-intro-script.md                      ✅ (28슬라이드, 18-22분)
├── clearly-intro-script - slides.md             ✅ (이미지 삽입 완료)
├── _files_/                                     ✅ (스크린샷 8개)
│   ├── clearly-main_before_login.png
│   ├── clearly-main.png
│   ├── project-create.png
│   ├── brd-wizard.png
│   ├── brd-result.png
│   ├── prd-result.png
│   ├── output-tool.png
│   └── homepage.png
├── audio/                                       ⏳ (다음 세션 자동 생성)
├── slides-gemini/                               ⏳ (다음 세션 자동 생성)
└── clearly-intro.mp4                            ⏳ (다음 세션 완성)
```

---

**작성자**: CUA_VL 학습자
**방법론**: CUA_VL (VibeLearn AI)
