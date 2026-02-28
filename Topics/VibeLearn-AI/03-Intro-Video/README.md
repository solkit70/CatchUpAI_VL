# M3: 소개 영상 제작 (Capstone)

**Topic**: VibeLearn-AI
**모듈**: M3
**작성일**: 2026-02-27
**상태**: ✅ 완료

---

## 이 모듈에서 만든 것

M1·M2에서 만든 모든 개념과 가이드를 토대로 **VibeLearn AI 소개 영상 KR+EN**을 제작했습니다.

---

## 영상 결과물

| 언어 | 파일 | 슬라이드 | 재생 시간 | 파일 크기 |
|------|------|---------|---------|---------|
| 한국어 | `vibelearn-intro-kr.mp4` | 24개 | 8분 15초 | 18.6 MB |
| 영어 | `vibelearn-intro-en.mp4` | 24개 | 7분 00초 | 16.4 MB |

> YouTube 업로드 후 링크 추가 예정

---

## 영상 구성 (6개 섹션, 24개 슬라이드)

| 섹션 | 내용 | 슬라이드 수 |
|------|------|----------|
| 섹션 1: 인트로 | 타이틀, 오늘 배울 내용, 이런 분께 | 3 |
| 섹션 2: 문제 제기 | 기존 학습의 악순환, AI 학습의 새 문제, 해결책 | 3 |
| 섹션 3: VibeLearn AI 소개 | 한 줄 소개, 핵심 설계 원칙, 4단계, 적용 분야 | 4 |
| 섹션 4: 사용법 | 준비물, Step 1~3 | 4 |
| 섹션 5: 케이스 스터디 | Clearly 케이스, 타임라인, 비교, 산출물 | 4 |
| 섹션 6: 아웃트로 | 반복성, 고급 팁, 시작, 요약, 공유, 마무리 | 6 |

---

## 폴더 구조

```
03-Intro-Video/
├── README.md                                  ← 이 파일
├── vibelearn-intro-script-kr.md               ← KR 스크립트 (슬라이드 + 나레이션)
├── vibelearn-intro-script-en.md               ← EN 스크립트
├── vibelearn-intro-script-kr - slides.md      ← KR Deckset 슬라이드 파일
├── vibelearn-intro-script-en - slides.md      ← EN Deckset 슬라이드 파일
├── audio-kr/                                  ← KR TTS 오디오 (24개 MP3)
├── audio-en/                                  ← EN TTS 오디오 (24개 MP3)
├── slides-gemini-kr/                          ← KR Gemini 슬라이드 JPEG (24개)
├── slides-gemini-en/                          ← EN Gemini 슬라이드 JPEG (24개)
├── vibelearn-intro-kr.mp4                     ← 최종 KR 영상 (8:15, 18.6MB)
└── vibelearn-intro-en.mp4                     ← 최종 EN 영상 (7:00, 16.4MB)
```

---

## M3 학습 목표 달성 현황

- [x] VibeLearn AI 소개 영상 KR 스크립트 완성 (24개 슬라이드)
- [x] EN 스크립트 완성 (자연스러운 번역)
- [x] markdown-video 파이프라인으로 KR 슬라이드+오디오+MP4 생성
- [x] markdown-video 파이프라인으로 EN 슬라이드+오디오+MP4 생성
- [x] WorkLog 작성 + Daily Retrospective 완료

**달성률**: 100% ✅

---

## 영상 제작 파이프라인

```
스크립트 (.md)
  → Deckset 형식 슬라이드 파일 (- slides.md)
  → TTS 오디오 생성 (gpt-4o-mini-tts, 24개 MP3)
  → Gemini 슬라이드 이미지 생성 (gemini-3-pro-image-preview, 24개 JPEG)
  → FFmpeg MP4 합성 (1920×1080, slides_to_video.py)
```

---

**작성자**: Claude with VibeLearn AI
**방법론**: VibeLearn AI v2.0
**WorkLog 참조**: [20260227_M3_VibeLearn-AI.md](../vl_worklog/20260227_M3_VibeLearn-AI.md)
