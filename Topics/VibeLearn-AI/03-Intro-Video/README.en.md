# M3: Introduction Video Production (Capstone)
> **[<- Korean Version](README.md)**


**Topic**: VibeLearn-AI
**Module**: M3
**Created**: 2026-02-27
**Status**: ✅ Complete

---

## What Was Created in This Module

Based on all the concepts and guides created in M1 and M2, we produced **VibeLearn AI intro videos in KR+EN**.

---

## Video Outputs

| Language | File | Slides | Duration | File Size |
|----------|------|--------|----------|-----------|
| Korean | `vibelearn-intro-kr.mp4` | 24 | 8 min 15 sec | 18.6 MB |
| English | `vibelearn-intro-en.mp4` | 24 | 7 min 00 sec | 16.4 MB |

> YouTube link to be added after upload

---

## Video Structure (6 Sections, 24 Slides)

| Section | Content | Slides |
|---------|---------|--------|
| Section 1: Intro | Title, what you'll learn, who it's for | 3 |
| Section 2: Problem | The learning vicious cycle, new problem with AI learning, solution | 3 |
| Section 3: VibeLearn AI Introduction | One-line intro, core design principle, 4 phases, applicable fields | 4 |
| Section 4: How to Use | Prerequisites, Steps 1–3 | 4 |
| Section 5: Case Study | Clearly case, timeline, comparison, outputs | 4 |
| Section 6: Outro | Repeatability, advanced tips, start, summary, share, closing | 6 |

---

## Folder Structure

```
03-Intro-Video/
├── README.md / README.en.md             ← This file
├── vibelearn-intro-script-kr.md         ← KR script (slides + narration)
├── vibelearn-intro-script-en.md         ← EN script
├── vibelearn-intro-script-kr - slides.md ← KR Deckset slide file
├── vibelearn-intro-script-en - slides.md ← EN Deckset slide file
├── audio-kr/                            ← KR TTS audio (24 MP3s)
├── audio-en/                            ← EN TTS audio (24 MP3s)
├── slides-gemini-kr/                    ← KR Gemini slide JPEGs (24)
├── slides-gemini-en/                    ← EN Gemini slide JPEGs (24)
├── vibelearn-intro-kr.mp4               ← Final KR video (8:15, 18.6MB)
└── vibelearn-intro-en.mp4               ← Final EN video (7:00, 16.4MB)
```

---

## M3 Learning Objectives Status

- [x] VibeLearn AI intro video KR script complete (24 slides)
- [x] EN script complete (natural translation)
- [x] KR slides + audio + MP4 generated via markdown-video pipeline
- [x] EN slides + audio + MP4 generated via markdown-video pipeline
- [x] WorkLog written + Daily Retrospective complete

**Achievement Rate**: 100% ✅

---

## Video Production Pipeline

```
Script (.md)
  → Deckset-format slide file (- slides.md)
  → TTS audio generation (gpt-4o-mini-tts, 24 MP3s)
  → Gemini slide image generation (gemini-3-pro-image-preview, 24 JPEGs)
  → FFmpeg MP4 synthesis (1920×1080, slides_to_video.py)
```

---

**Author**: Claude with VibeLearn AI
**Methodology**: VibeLearn AI v2.0
**WorkLog Reference**: [20260227_M3_VibeLearn-AI.md](../vl_worklog/20260227_M3_VibeLearn-AI.md)
