# M3: Clearly App Introduction Video Production

> **[← Korean Version](README.md)**

**Topic**: Clearly-BRD-PRD
**Module**: M3 (Bonus Module)
**Date**: 2026-02-22
**Status**: 🔄 In Progress (script/slides complete, video generation pending)

---

## What You Learn in This Module

This module takes all the learning outputs from M1 (Clearly concepts) and M2 (BRD/PRD hands-on practice) and applies them to produce a **YouTube video introducing the Clearly app**. It serves as the capstone for the Clearly-BRD-PRD topic.

---

## Document List (Recommended Reading Order)

| # | Document | Description |
|---|----------|-------------|
| 1 | [clearly-intro-script-kr.md](clearly-intro-script-kr.md) | KR video script (narration included, 27 slides) |
| 2 | [clearly-intro-script-kr - slides.md](clearly-intro-script-kr%20-%20slides.md) | KR Deckset slide file (TTS source) |
| 3 | [clearly-intro-script-en.md](clearly-intro-script-en.md) | EN video script |
| 4 | [clearly-intro-script-en - slides.md](clearly-intro-script-en%20-%20slides.md) | EN Deckset slide file |
| 5 | [remotion-kr-plan.md](remotion-kr-plan.md) | KR video production plan using Remotion |
| Final | `clearly-intro-kr.mp4` / `clearly-intro-en.mp4` | Completed KR/EN intro videos |

**Previous Module**: [02-CatchUpAI-BRD-PRD](../02-CatchUpAI-BRD-PRD/) | **Next Module**: None (last module)

---

## Video Overview

**Video Purpose**: Clearly app introduction + step-by-step usage + live homepage demo
**Language**: Korean (KR) + English (EN)
**Estimated Length**: 17–20 minutes

### Video Structure (27 Slides)

| Section | Slides | Est. Time | Key Content |
|---------|--------|-----------|-------------|
| 1. Intro | 4 | 2 min | Channel intro, today's topic |
| 2. Vibe Coding & Problem Setup | 4 | 3 min | Why BRD/PRD is needed |
| 3. Clearly App Introduction | 5 | 3 min | Features, BRD vs PRD, two modes |
| 4. Step-by-Step Demo | 9 | 5 min | Project creation → BRD → PRD → Output |
| 5. Live Results Demo | 4 | 2 min | Catch Up AI homepage |
| 6. Insights & Outro | 3 | 1 min | Key takeaways, wrap-up |

---

## Folder Structure

```
03-Clearly-Intro-Video/
├── README.md / README.en.md                   ← This file
├── clearly-intro-script-kr.md                 # KR narration script
├── clearly-intro-script-kr - slides.md        # KR Deckset slides (TTS source)
├── clearly-intro-script-en.md                 # EN narration script
├── clearly-intro-script-en - slides.md        # EN Deckset slides (TTS source)
├── remotion-kr-plan.md                        # Remotion production plan
├── _files_/                                   # App screenshots (7 images)
├── audio/                                     # TTS audio files
├── slides-gemini/                             # AI-generated slide images
├── clearly-intro-kr.mp4                       # Final KR video
└── clearly-intro-en.mp4                       # Final EN video
```

---

## Video Production Workflow

```
clearly-intro-script.md          (original script)
        ↓ markdown-slides skill
clearly-intro-script - slides.md (Deckset slides)
        ↓ collect screenshots → _files_/ folder
        ↓ markdown-video skill
clearly-intro.mp4                (final video)
```

### Production Commands

```bash
# Step 1: Generate audio (OpenAI TTS)
python generate_audio.py "clearly-intro-script - slides.md" --output-dir "audio"

# Step 2: Generate slide images (Gemini)
python create_slides_gemini.py "clearly-intro-script - slides.md" \
  --output-dir "slides-gemini" --style "professional" --auto-approve

# Step 3: Synthesize MP4
python slides_to_video.py \
  --slides-dir "slides-gemini" --audio-dir "audio" --output "clearly-intro.mp4"
```

**API Requirements**: `OPENAI_API_KEY`, `GEMINI_API_KEY` environment variables required
**Estimated Cost**: ~$1.30 (30 Gemini images + OpenAI TTS)

---

## M3 Learning Objectives Status

- [x] KR video script written (27 slides, narration included)
- [x] EN video script written (bilingual parallel structure)
- [x] Deckset slide files generated (KR + EN)
- [ ] App screenshots collected (7 images) → `_files_/`
- [ ] Audio files generated (TTS)
- [ ] Slide images generated (Gemini)
- [ ] Final MP4 synthesized (KR + EN)

---

## Referenced M1/M2 Documents

| Document | How It Was Used |
|----------|----------------|
| `01-Clearly-Overview/concepts/what-is-clearly.md` | Clearly definition, workflow |
| `01-Clearly-Overview/concepts/brd-vs-prd.md` | BRD vs PRD comparison |
| `01-Clearly-Overview/concepts/vibe-coding-role.md` | Vibe Coding concept |
| `01-Clearly-Overview/guides/clearly-usage-guide.md` | Step-by-step usage, tips |
| `02-CatchUpAI-BRD-PRD/notes/wizard-experience.md` | Real Wizard experience |

---

## Key Insights (The "Aha!" Moments of This Module)

1. **Learning outputs become video content** — M1/M2 documents map directly to video slides
2. **Bilingual scripting doubles reach** — KR + EN with a shared structure
3. **Bug documentation adds authenticity** — showing real struggles builds trust with the audience
4. **The markdown-video pipeline** — TTS + Gemini + FFmpeg turns a script into a finished video

---

**Author**: Claude with VibeLearn AI
**Methodology**: VibeLearn AI v2.0
**WorkLog Reference**: `../vl_worklog/`
