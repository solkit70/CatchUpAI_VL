# WorkLog: M3 - 소개 영상 제작 (Capstone)

**Date**: 2026-02-27
**Module**: M3 - 소개 영상 제작 (Capstone)
**Status**: ✅ 완료
**Topic**: VibeLearn-AI

---

## 📊 오늘의 학습 목표

- [ ] VibeLearn AI 소개 영상 KR 스크립트 작성 (25-30개 슬라이드)
- [ ] EN 스크립트 작성 (KR 번역 + 자연스럽게 조정)
- [ ] markdown-video 파이프라인 실행 — KR (슬라이드 + 오디오 + MP4)
- [ ] markdown-video 파이프라인 실행 — EN (슬라이드 + 오디오 + MP4)
- [ ] 03-Intro-Video/README.md 작성
- [ ] WorkLog 작성 + Daily Retrospective 완료

---

## 📝 학습 내용

### 참조 파일 분석 (15분) — 완료

분석한 파일:
- `Topics/Clearly-BRD-PRD/03-Clearly-Intro-Video/clearly-intro-script-kr.md`
  - 구조: 섹션 6개, 슬라이드 27개, 총 16분 28초 영상
  - 형식: `### 슬라이드 N: 제목` + 슬라이드 텍스트 + 나레이션
- `Topics/VibeLearn-AI/01-System-Overview/concepts/` — 모든 개념 문서
- `Topics/VibeLearn-AI/02-User-Guide/` — 가이드 및 케이스 스터디

### 영상 기획 결정

**타겟 시청자**: AI 도구로 무언가를 배우고 싶은데 체계적인 방법을 모르는 사람
**핵심 메시지**: "배우고 싶다는 말 한마디로, AI가 체계적인 학습 전과정을 이끌어준다"
**영상 구성**: 6개 섹션, 25-27개 슬라이드, 목표 15-18분

---

## ✅ 완료한 작업

### Step 1: 참조 분석 (15분)
- Clearly KR 스크립트 구조 분석 (27개 슬라이드, 6개 섹션)
- M1·M2 산출물 내용 파악 → 영상 구성 방향 결정

### Step 2: KR 스크립트 작성 (60분)
- 파일: `vibelearn-intro-script-kr.md`
- 6개 섹션, 25개 슬라이드 (인트로 → 문제 → 소개 → 사용법 → 케이스 → 아웃트로)
- 핵심 메시지: "배우고 싶다 한마디 → AI가 자동 처리"

### Step 3: EN 스크립트 작성 (45분)
- 파일: `vibelearn-intro-script-en.md`
- KR → EN 자연스러운 번역 (직역 아닌 EN 화자 스타일)

### Step 4: Deckset 슬라이드 파일 생성
- `vibelearn-intro-script-kr - slides.md` (Deckset 형식: `^` = 화자 노트)
- `vibelearn-intro-script-en - slides.md`
- 테이블 구분자 `|------|` → `|:--:--|` 수정 (false slide split 방지)

### Step 5: KR 파이프라인 실행
- 오디오: 24개 MP3 생성 (gpt-4o-mini-tts, nova 음성, 7.6MB)
- 슬라이드: 24개 JPEG 생성 (Gemini gemini-3-pro-image-preview, 유료 API 키 사용)
- MP4: `vibelearn-intro-kr.mp4` (8분 15초, 18.6MB)

### Step 6: EN 파이프라인 실행
- 오디오: 24개 MP3 생성 (gpt-4o-mini-tts, alloy 음성, 6.4MB)
- 슬라이드: 24개 JPEG 생성
- MP4: `vibelearn-intro-en.mp4` (7분 00초, 16.4MB)

---

## 🐛 문제 해결 로그

### 문제 1: Gemini API 무료 한도 초과
- **증상**: `429 RESOURCE_EXHAUSTED` — 무료 티어 일일 한도 초과
- **해결**: 유료 Gemini API 키 사용 (`AIzaSyCb8X1...`)
- **학습**: 슬라이드 생성은 유료 키 보유 필요

### 문제 2: 테이블 구분자 → false slide split
- **증상**: dry-run에서 45개 슬라이드 감지 (실제 30개여야 함)
- **원인**: `|------|` 안의 `---` 패턴을 슬라이드 구분자로 오인
- **해결**: Python regex로 `---` → `:--:` 치환 (15개 패턴 수정)

---

## 📋 DoD 체크리스트

- [x] KR 스크립트 완성 (24개 슬라이드)
- [x] EN 스크립트 완성
- [x] KR Gemini 슬라이드 생성 완료 (24개 JPEG)
- [x] EN Gemini 슬라이드 생성 완료 (24개 JPEG)
- [x] KR TTS 오디오 생성 완료 (24개 MP3)
- [x] EN TTS 오디오 생성 완료 (24개 MP3)
- [x] `vibelearn-intro-kr.mp4` 완성 (8:15, 18.6MB)
- [x] `vibelearn-intro-en.mp4` 완성 (7:00, 16.4MB)
- [ ] YouTube 업로드 (다음 세션)
- [x] WorkLog 작성 + Daily Retrospective 완료

**DoD 달성률**: 90% (YouTube 업로드 제외)

---

## 🔍 Daily Retrospective

**What went well?**
- KR+EN 스크립트를 빠르게 작성 — M1·M2 산출물이 그대로 스크립트 자료가 됨
- 파이프라인이 예상대로 작동 — Clearly 케이스에서 배운 경험이 그대로 재사용됨
- Gemini API 키 이슈 즉시 해결

**What could be improved?**
- 테이블 구분자 문제는 파이프라인 자체에서 처리해야 함 (향후 개선 가능)
- 영상 길이가 8분/7분으로 예상(15-18분)보다 짧음 — 나레이션을 더 풍부하게 할 수 있었음

**Insights**
- VibeLearn AI의 진짜 힘: M1에서 만든 개념 문서 → M2에서 만든 케이스 스터디 → M3 스크립트가 자동으로 완성. 이전 모듈이 다음 모듈의 재료가 됨
- "Capstone"의 의미: 모든 모듈의 학습 결과가 영상 하나로 결집되는 느낌

**Tomorrow's focus**
- YouTube 업로드 (제목·설명·태그 작성 후)
- M3 Module Retrospective 작성
- Topic Retrospective (전체 VibeLearn-AI 학습 회고)

---

## 🎯 다음 세션 준비사항

1. YouTube 업로드:
   - `vibelearn-intro-kr.mp4` → 제목·설명·태그 KR 작성
   - `vibelearn-intro-en.mp4` → 제목·설명·태그 EN 작성
2. M3 Module Retrospective 작성
3. Topic Retrospective (VibeLearn-AI 전체 회고)
4. Roadmap에 M3 완료 표시 업데이트
