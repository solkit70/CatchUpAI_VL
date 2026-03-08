# Case Study: Clearly-BRD-PRD
> **[<- Korean Version](clearly-case.md)**


> **"A real example of learning with VibeLearn AI — Writing BRD/PRD with the Clearly App"**

**Created**: 2026-02-26
**Topic**: Clearly-BRD-PRD
**Learning period**: 2026-02-01 ~ 2026-02-15 (5 actual working days)
**Total learning hours**: approximately 9.5 hours
**Final output**: YouTube intro videos KR + EN

---

## 1. State Before Starting

### Learner Background

- Catch Up AI channel operator
- Interested in Vibe Coding (AI-collaborative development)
- Had heard of the Clearly app but never used it directly
- **Learning goal**: Fully understand the Clearly app and produce an intro video

### Questions to Resolve

1. Didn't know exactly what BRD and PRD were
2. Unclear what problem the Clearly app solves
3. Never experienced what "AI creates BRD/PRD" actually means in practice

---

## 2. Learning Process (3 Modules)

### M1: Clearly Overview & Core Concepts (2026-02-01, 3 hours)

**What was done**:
- Analyzed Clearly app official site and documentation
- Clarified BRD vs PRD concepts
- Understood the role of requirements documents in Vibe Coding

**What was created** (`01-Clearly-Overview/`):
```
concepts/
├── what-is-clearly.md     ← What Clearly is (AI tool for auto BRD/PRD generation)
├── brd-vs-prd.md          ← BRD (Why&What) vs PRD (What&How) comparison
└── vibe-coding-role.md    ← The connection: idea → requirements → code
guides/
└── clearly-quick-start.md ← Guide to creating your first BRD
```

**Key discovery**: Clearly's core value is not simple document generation but
an automated pipeline: "BRD → PRD → Output Tool (AI coding tool config files)"

---

### M2: Hands-on BRD/PRD Writing (2026-02-08~15, 5.5 hours, 3 sessions)

**What was done**:
- Wrote BRD 3 times and PRD 2 times using a real project (Catch Up AI 2026 homepage)
- Auto-generated Claude Code config file with Choose Output Tool
- Found and reported bugs to developer (4 cases)

**What was created** (`02-CatchUpAI-BRD-PRD/`):
```
brd/
├── catchupai-2026-brd-v1.md   ← First attempt
├── catchupai-2026-brd-v2.md   ← Improved from experience
└── catchupai-2026-brd-v3.md   ← Final (best quality)
prd/
├── catchupai-2026-prd-v1.md
└── catchupai-2026-prd-v2.md   ← Detailed PRD with 12 sections
claude-code-output/             ← AI coding tool config files (auto-generated)
├── CLAUDE.md
├── PRD.md
└── REFERENCE_DOCUMENT.md
notes/
└── clearly-bug-report.md       ← 4 bug reports
```

**The power of repetition discovered**:
- v1: "So this is how it's done" — getting familiar
- v2: Faster and better quality from previous experience
- v3: Filled the gaps from v1 and v2 for the best quality

> "Doing the same task 3 times made it 2× faster and 3× better in quality" — Daily Retrospective record

---

### M3: Documentation & Usage Guide (2026-02-15, 1 hour)

**What was done**:
- Wrote "guide for first-time users" based on M1~M2 experience
- With M2 experience, completed in half the planned time (1h instead of 2-3h)

**What was created**:
```
guides/
└── clearly-usage-guide.md    ← Detailed guide for the full workflow (key output)
```

---

### M4 (Added): Introduction Video Production (Capstone, 2026-02-22~25, approx. 8 hours)

**What was done**:
- Wrote KR+EN scripts with markdown-video pipeline
- Generated slide images with Gemini API (27 images)
- Generated audio with OpenAI TTS (27 MP3s)
- Synthesized MP4 with FFmpeg
- Additionally produced animated version with Remotion
- Uploaded to YouTube

**What was created** (`03-Clearly-Intro-Video/`):
- `clearly-intro-kr.mp4` (16:28, Korean)
- `clearly-intro-en.mp4` (13:48, English)
- Remotion version KR/EN (high quality)
- YouTube upload metadata

---

## 3. Final Outputs

### Textbook-Quality Documents (Other Learners Can Use Immediately)

| Document | Location | Description |
|----------|----------|-------------|
| Clearly introduction | `concepts/what-is-clearly.md` | Quick overview of what Clearly is |
| BRD vs PRD | `concepts/brd-vs-prd.md` | Differences and when to use each |
| Usage guide | `guides/clearly-usage-guide.md` | Complete follow-along guide from start to finish |
| BRD v3 (final) | `brd/catchupai-2026-brd-v3.md` | Real completed BRD example |
| PRD v2 (final) | `prd/catchupai-2026-prd-v2.md` | Detailed PRD example with 12 sections |

### YouTube Intro Videos

| Version | Link | Running time |
|---------|------|-------------|
| 🇰🇷 Korean | [AI가 질문 몇 가지로 BRD/PRD를 만들어준다?](https://youtu.be/crK2aO_uXkQ) | 16:28 |
| 🇺🇸 English | [AI Writes Your BRD & PRD in Minutes?](https://youtu.be/KwQOpU__BKo) | 13:48 |

---

## 4. Results by the Numbers

| Metric | Number |
|--------|--------|
| Total learning hours | 9.5 hours (planned: 7–10h ✅) |
| Actual working days | 5 days (out of 15-day period) |
| Outputs generated | 22 files |
| BRD/PRD writing sessions | BRD 3× + PRD 2× |
| Bugs found | 4 (all reported to developer) |
| YouTube videos | 2 (KR + EN) |
| Self-Assessment | ⭐⭐⭐⭐⭐ (4.7/5) |

---

## 5. What If You Had Done It Without VibeLearn AI?

### Method A: Study with YouTube videos
- Watch 3–5 videos → "I understand" → Forget a week later
- Never actually wrote BRD/PRD
- Wouldn't have even attempted making an intro video

### Method B: Read official documentation
- Read English docs → understand concepts → no practice
- No reproducible outputs
- Can't pass on to the next person

### With VibeLearn AI
- **9.5 hours** → Complete understanding + 22 outputs + 2 YouTube videos
- The next learner can learn Clearly from this folder alone
- Knowledge can spread to thousands through the videos

> "Learning doesn't end with me alone — it continues to the next person"

---

## 6. Evaluating VibeLearn AI Methodology Effectiveness (in This Case)

| Element | Rating | Notes |
|---------|--------|-------|
| Roadmap DoD checklists | ⭐⭐⭐⭐⭐ | Clear completion criteria per session |
| Real-time WorkLog writing | ⭐⭐⭐⭐ | Could reproduce previous content even after 3 repetitions |
| Daily Retrospective | ⭐⭐⭐⭐⭐ | Insights like "the power of repetition" discovered |
| Output-centered learning | ⭐⭐⭐⭐⭐ | Tangible results maintained motivation |
| 70/30 practice/theory ratio | ⭐⭐⭐⭐⭐ | M1 (theory) → M2 (3× practice) flow felt natural |

---

## 7. What You Can Learn from This Case

### For those who want to learn Clearly
→ See `Topics/Clearly-BRD-PRD/01-Clearly-Overview/` folder

### For those who want to understand the VibeLearn AI methodology
→ This case shows the 4 phases of the methodology actually working:
1. Phase 1: Write topic_info.md → create folder structure
2. Phase 2: Plan 3 modules with Roadmap
3. Phase 3: 5 learning sessions, 22 outputs
4. Phase 4: Final Retrospective + YouTube video upload

---

**Case author**: Claude with VibeLearn AI
**Original learning records**: [Topics/Clearly-BRD-PRD/](../../Clearly-BRD-PRD/)
**YouTube 🇰🇷**: [https://youtu.be/crK2aO_uXkQ](https://youtu.be/crK2aO_uXkQ)
**YouTube 🇺🇸**: [https://youtu.be/KwQOpU__BKo](https://youtu.be/KwQOpU__BKo)
