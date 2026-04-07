# GOBI-Specs-Pipeline

**Methodology**: CUA_VL (VibeLearn AI) | **Status**: ✅ Complete | **Duration**: 2026-04-06 ~ 2026-04-07 (2 days, ~9 hours)

---

## Topic Overview

This learning topic analyzes the documentation pipeline operated by the GOBI development team (`gobi-monorepo/specs` → `gobi-ai/docs` → `docs.gobihq.com`) and **determines how Vibe Guiding can be integrated into it**.

Beyond a technical study, the goal is to produce a **Vibe Guiding strategy proposal shareable with the GOBI team**.

---

## Key Findings (3-Line Summary)

1. **Pipeline Gap**: The conversion from `gobi-monorepo/specs` → `gobi-ai/docs` is manual — this is VibeLearn AI's (SPECS_TO_GUIDE) core opportunity
2. **Phase 1 is possible right now**: With only `.gobi/settings.yaml` + a Vibe Guiding prompt file, Vibe Guiding can run inside the app without any GOBI team code changes
3. **CVL is the key to sustainability**: specs update → VibeLearn AI auto re-runs → Vibe Guiding auto-improves

---

## Pipeline Structure

```
gobi-monorepo/specs (26 feature specs)
        ↓ ⚠️ Manual conversion (no automation)
gobi-ai/docs (Mintlify MDX)
        ↓ ✅ Auto deployment
docs.gobihq.com
```

**After Vibe Guiding integration**:

```
gobi-monorepo/specs
        ↓ VibeLearn AI (SPECS_TO_GUIDE) ← CVL automation
Vibe Guiding prompts + gobi-ai/docs
        ↓
In-app real-time Vibe Guiding (Reflex) + docs.gobihq.com
```

---

## Module Structure

| Module | Status | Study Time | Folder |
|--------|--------|------------|--------|
| M1: gobi-monorepo + gobi-ai/docs Full Structure Analysis | ✅ Complete | 3h | [01-Monorepo-Overview/](01-Monorepo-Overview/README.en.md) |
| M2: Deep Dive into Key Vibe Guiding Spec Files | ✅ Complete | 3h | [02-Specs-Deep-Dive/](02-Specs-Deep-Dive/README.en.md) |
| M3: Capstone — Vibe Guiding Strategy Proposal | ✅ Complete | 3h | [03-Capstone/](03-Capstone/README.en.md) |

---

## Output Files

### M1 — Structure Analysis
- [repo-structure.en.md](01-Monorepo-Overview/repo-structure.en.md) — 7 projects + 26 spec analysis table
- [pipeline-diagram.en.md](01-Monorepo-Overview/pipeline-diagram.en.md) — Current pipeline + Vibe Guiding integration diagram

### M2 — Spec Deep Dive
- [spec-analysis-second-brain-agent.en.md](02-Specs-Deep-Dive/spec-analysis-second-brain-agent.en.md) — Immediate Vibe Guiding via System Prompt injection
- [spec-analysis-voice-interaction.en.md](02-Specs-Deep-Dive/spec-analysis-voice-interaction.en.md) — Ambient Mode = optimal voice channel for Vibe Guiding
- [spec-analysis-capture.en.md](02-Specs-Deep-Dive/spec-analysis-capture.en.md) — Post-capture Reflex = golden timing
- [spec-analysis-orchestration.en.md](02-Specs-Deep-Dive/spec-analysis-orchestration.en.md) — Phase 1 implementation via `.gobi/settings.yaml` Watch Pattern
- [vibe-guiding-touchpoints.en.md](02-Specs-Deep-Dive/vibe-guiding-touchpoints.en.md) — 8-touchpoint matrix + phase-by-phase roadmap

### M3 — Strategy Proposal
- [integration-options.en.md](03-Capstone/integration-options.en.md) — Comparison of 4 integration options
- [**vibe-guiding-strategy-proposal.en.md**](03-Capstone/vibe-guiding-strategy-proposal.en.md) — Strategy proposal for sharing with the GOBI team ⭐
- [topic-retrospective.en.md](03-Capstone/topic-retrospective.en.md) — Full topic retrospective

---

## Strategy Summary (Phase 1/2/3)

| Phase | Timeline | Goal | GOBI Team Collaboration |
|-------|----------|------|------------------------|
| Phase 1 | Immediate (1-2 weeks) | Reflex-based Vibe Guiding prototype in Changsoo Vault | Not required |
| Phase 2 | 2-4 weeks | Vibe Guiding Skill packaging + docs automation contribution | PR review |
| Phase 3 | 1-3 months | Native Ambient Mode integration | Collaboration required |

---

## Learning Environment

| Item | Details |
|------|---------|
| Local repo | `C:\AI_study\2026\GOBI_VibeGuiding\gobi-monorepo\` (Private) |
| Local repo | `C:\AI_study\2026\GOBI_VibeGuiding\docs\` (Public) |
| GitHub | https://github.com/gobi-ai/gobi-monorepo |
| GitHub | https://github.com/gobi-ai/docs |
| Official docs | https://docs.gobihq.com |

---

## WorkLog

| Date | Module | Link |
|------|--------|------|
| 2026-04-06 | M1 | [20260406_M1_GOBI-Specs-Pipeline.md](vl_worklog/20260406_M1_GOBI-Specs-Pipeline.md) |
| 2026-04-07 | M2 | [20260407_M2_GOBI-Specs-Pipeline.md](vl_worklog/20260407_M2_GOBI-Specs-Pipeline.md) |
| 2026-04-07 | M3 | [20260407_M3_GOBI-Specs-Pipeline.md](vl_worklog/20260407_M3_GOBI-Specs-Pipeline.md) |

---

*Methodology: CUA_VL (VibeLearn AI) — Author: Changsoo (with Claude Code)*
