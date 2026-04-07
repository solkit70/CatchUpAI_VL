# M1 - gobi-monorepo + gobi-ai/docs Full Structure Analysis

**Module**: M1 | **Status**: ✅ Complete | **Study Time**: ~3h (2026-04-06)

---

## What You Learn in This Module

Directly clone and analyze the two core repositories in the GOBI ecosystem.

| # | Document | Description |
|---|----------|-------------|
| 1 | [repo-structure.en.md](repo-structure.en.md) | Full breakdown of 7 gobi-monorepo projects + 26 specs/ files + gobi-ai/docs structure |
| 2 | [pipeline-diagram.en.md](pipeline-diagram.en.md) | specs → docs.gobihq.com pipeline diagram + Vibe Guiding integration proposal |

---

## Key Summary

### 1. gobi-monorepo = 7 projects + specs + AI workflow
- Each project is managed as an independent repo (no build system at root)
- `specs/` = 26 cross-cutting feature specs (defines *what*, not *how*)
- `prompts/CODE_TO_SPECS.md` = AI prompt that generates specs from code (already exists!)
- `LINEAR.md` = Active Planner AI → Developer AI → PR Reviewer AI agent pipeline

### 2. gobi-ai/docs = Mintlify-based documentation site
- MDX format, navigation configured via docs.json
- git push → Mintlify auto build → docs.gobihq.com deployment (fully automated)
- Currently in early stage (4 Products + 2 Reference sections)

### 3. Key Finding: A manual step exists in the pipeline
```
specs (Markdown) → [Manual conversion ⚠️] → docs (MDX) → [Auto deploy ✅] → docs.gobihq.com
```
- specs are feature-centric; docs are product-centric → no direct 1:1 conversion
- **This manual conversion step = core opportunity for VibeLearn AI / Vibe Guiding**

### 4. CODE_TO_SPECS → SPECS_TO_GUIDE direction proposed
- Dev team: Code → AI → specs (already implemented)
- Vibe Guiding proposal: specs → VibeLearn AI → user guides + in-app Vibe Guiding context

---

## Next Module

→ **[M2: Deep Dive into Key Vibe Guiding Spec Files](../02-Specs-Deep-Dive/README.en.md)**
- Analysis targets: 05 (Second Brain Agent), 06 (Voice), 07 (Capture), 19 (Orchestration)
