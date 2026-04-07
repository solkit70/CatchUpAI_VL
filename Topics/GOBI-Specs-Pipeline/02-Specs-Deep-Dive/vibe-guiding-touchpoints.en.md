# Vibe Guiding Touchpoint Integrated Analysis

**Created**: 2026-04-07
**Based on**: Analysis results of Specs 05, 06, 07, 19

---

## Core Conclusion

> **Vibe Guiding is not a new product.**
> It can be implemented by **combining** GOBI's existing infrastructure (agent + voice + capture + orchestrator).
> The only additions needed are **context (spec-based guides) and prompts**.

---

## Full Touchpoint Map

```
┌──────────────────────────────────────────────────────────────┐
│                      GOBI Desktop App                         │
│                                                              │
│  [Capture Tab]      [Agent Tab]         [Orchestrator]        │
│   ↓ New capture      ↓ Voice/text         ↓ File change      │
│   File saved         Input received        Reflex trigger     │
│      └──────────────────┴────────────────────┘               │
│                          ↓                                   │
│              Vibe Guiding Agent                              │
│         (System Prompt + spec-based context)                 │
│                          ↓                                   │
│         Guidance delivered via voice (TTS) or text           │
└──────────────────────────────────────────────────────────────┘
```

---

## Touchpoint Feasibility Matrix

| # | Touchpoint | Related Spec | Implementation Difficulty | GOBI Team Collaboration | Phase |
|---|-----------|-------------|--------------------------|------------------------|-------|
| 1 | System Prompt injection | 05 Agent | ⭐ Very low | ❌ Not required | 1 |
| 2 | Dedicated Vibe Guiding Vault / Brain | 05 Agent | ⭐ Very low | ❌ Not required | 1 |
| 3 | Post-capture Reflex trigger | 07+19 | ⭐ Low | ❌ Not required | 1 |
| 4 | Ambient Mode + Vibe context | 06+05 | ⭐⭐ Medium | △ Config level | 2 |
| 5 | Vibe Guiding Skill packaging | 19 | ⭐⭐ Medium | △ Skill distribution | 2 |
| 6 | Real-time guidance during ACB session | 07+06 | ⭐⭐⭐ High | ✅ Required | 3 |
| 7 | Wake Word → Vibe Guiding routing | 06 | ⭐⭐⭐ High | ✅ Required | 3 |
| 8 | Schedule-based automatic guide | 19 | ⭐⭐⭐ High | ✅ Required | 3 |

---

## Phase-by-Phase Implementation Roadmap

### Phase 1 — Immediate Proof (1-2 weeks, no GOBI team collaboration required)

**Goal**: Prove that a Vibe Guiding prototype can be built right now

**Implementation**:
1. Add a dedicated Vibe Guiding prompt file to Changsoo Vault
   ```
   Changsoo_Vault/.gobi/prompts/vibe-guiding.md
   ```
2. Prompt content: Core Concepts extracted from specs + guiding instructions
3. Set Watch Pattern: trigger Reflex when new Capture/Note files are detected
4. Reflex output → saved to `.gobi/outputs/` or spoken via TTS

**VibeLearn AI's role**:
- Read gobi-monorepo/specs
- Extract Core Concepts for each feature
- Auto-generate Vibe Guiding prompts (`SPECS_TO_GUIDE`)

**Validation metrics**:
- Does related Brain knowledge get auto-connected after a new capture?
- Does asking "how do I capture?" via voice produce a correct answer?

---

### Phase 2 — Skill Packaging (2-4 weeks, minimal GOBI team collaboration)

**Goal**: Distribute a Vibe Guiding Skill that all GOBI users can use

**Implementation**:
1. Create the `vibe-guiding` Skill package
   ```
   vibe-guiding-skill/
   ├── SKILL.md              # Behavior definition
   ├── prompts/
   │   ├── desktop-guide.md  # Desktop feature guide
   │   ├── space-guide.md    # Space feature guide
   │   └── cli-guide.md      # CLI feature guide
   └── watch-patterns.yaml   # Automation trigger config
   ```
2. Use VibeLearn AI to auto-generate specs → per-feature guide prompts (CVL)
3. Align with GOBI team on Skill distribution method

**CVL (Continuous Vibe Learning)**:
- Detect updates to gobi-monorepo/specs
- Changed spec → auto-regenerate corresponding guide prompt
- Vibe Guiding Skill auto-updates

---

### Phase 3 — Native In-App Integration (1-3 months, GOBI team collaboration required)

**Goal**: GOBI Desktop/Space users experience Vibe Guiding with zero manual setup

**Implementation**:
1. Add Vibe Guiding routing to Ambient Mode
   - Specific Wake Word → connect to Vibe Guiding Agent
   - Auto-detect current screen/feature context
2. Show related knowledge in side panel during ACB sessions in real time
3. After schedule trigger is implemented → auto-generate daily/weekly Vibe Guides
4. Operate a public Vibe Guiding Brain on Gobi Space

---

## "In-App Real-Time Vibe Guiding" Feasibility Assessment

**GOBI team expectation**: "A way to run Vibe Guiding actually inside the app, rather than through the docs pipeline"

**Assessment**:
- Phase 1 (immediate): ✅ **Possible right now** — prove in Changsoo Vault using Orchestrator + prompt only
- Phase 2 (short-term): ✅ **Possible within 2-4 weeks** — package as Skill and distribute to other users
- Phase 3 (long-term): 🔄 **Requires GOBI team collaboration** — native UX integration requires app code changes

> **Key message**: Running Vibe Guiding in the app is possible from Phase 1.
> A fully native experience requires Phase 3, but proof of value can start today.

---

## VibeLearn AI's Role (Position in the Pipeline)

```
gobi-monorepo/specs (26 feature definitions)
        ↓
VibeLearn AI (SPECS_TO_GUIDE)
  - Extract Core Concepts
  - Generate guides per user persona
  - Write Vibe Guiding prompts
        ↓
Vibe Guiding Skill / Vault prompts
        ↓
GOBI Orchestrator (Reflex / Ambient Mode)
        ↓
Real-time personalized guidance for users
```

**CVL (Continuous Vibe Learning)**:
```
Detect changes in specs files
        ↓
VibeLearn AI auto re-runs
        ↓
Updated Vibe Guiding prompts
        ↓
Auto-deployed → user experience automatically improves
```
