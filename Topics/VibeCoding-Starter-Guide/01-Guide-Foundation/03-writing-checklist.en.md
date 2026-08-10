---
title: "Writing & Review Checklist"
created: 2026-08-10 10:05:00
author:
  - "Claude Code"
tags:
  - vibecoding
  - guide-foundation
  - checklist
---

> 🌐 [한국어](03-writing-checklist.md) · **English**

## What this document is for

After writing any document for M2–M7, review it with this checklist. Keeping the first principles in mind and confirming them with checkboxes give different results. **Run through this list from the top every time you finish a document.**

## 1. Plain language

- [ ] No technical term appears without an explanation unless it's in `02-glossary.en.md`
- [ ] Not a single word from the **banned list** in the glossary's substitute-expression table (repository, directory, run/execute, install-as-jargon, error, etc.)
- [ ] If a new term was used, it was added to `02-glossary.en.md` first
- [ ] No sentence runs longer than three lines
- [ ] When an abbreviation is used, its **full form and a plain explanation are given together** the first time
      (e.g. "DoD (Definition of Done)") — after that, use the abbreviation only

## 2. One action = one step

- [ ] No place where **two actions are bundled into one step** ("download and install it")
- [ ] Each step is numbered and holds a single action
- [ ] Buttons to click are written with both **color and name** (e.g. "the blue Download button")
- [ ] Where Windows and macOS diverge is marked

## 3. Checkpoints

- [ ] Each step ends with a confirmation line, a "you'll see this screen when it works"
- [ ] The confirmation names **something visible** (a screen or result, not internal state)
- [ ] Each section closes with a "if this worked, on to the next" signal

## 4. Encouragement + reality

- [ ] Problem situations are phrased as **"a common thing that happens," not "an error"**
- [ ] It's not all success stories — the sticking points are stated honestly
- [ ] Conversely, no paragraph ends on an intimidating note ("this is hard," "if you're not careful")
- [ ] Costs (the Claude subscription) aren't hidden; what you get is stated alongside

## 5. Cite the source (required for M5·M6)

- [ ] Every claim is tagged with its source file or document
- [ ] When quoting a number, **what's included and what's excluded** is stated exactly
      (e.g. Clearly "22 outputs in 9.5 hours" — the ~8 hours of video production is separate)
- [ ] No sentence written from guessing or memory
- [ ] Self-Assessment scores from vault retrospectives are used only for motivation (not cited as evidence)

## 6. Video links inline

- [ ] Every place a Park Changsoo video is mentioned has the YouTube link **right there**
- [ ] The link was taken from the `vl_materials/video-references.md` table (zero links not in the table)
- [ ] No English video link in the Korean body (and vice versa for this English version — Korean links stay in the Korean body)
- [ ] Runtime is noted when known
- [ ] **Videos that don't exist yet** aren't presented as if they do
      (the setup-process video, the teacher's Voice Legacy video — neither exists)

## 7. Dual purpose

- [ ] A participant reading alone doesn't get stuck
- [ ] The order also flows naturally for a facilitator guiding alongside
- [ ] Anything only the facilitator needs is pulled out of the body into the facilitator manual

## 8. Document format

- [ ] **The filename starts with a `NN-` number** (see the rule below)
- [ ] Frontmatter (`title`, `created`, `tags`) is present
- [ ] The first line is a heading (H2 or higher) — no loose text after frontmatter
- [ ] There's a blank line before tables
- [ ] No horizontal rules (`---`) between sections
- [ ] No lone single-sentence paragraph (bundled into 2–3 sentences)
- [ ] Wiki/relative links point to files that actually exist

## Filename rule — sort order = learning order

**Every output filename starts with a `NN-` number.** GitHub and Obsidian show files in **alphabetical order**, so without numbers the learning order in the README diverges from the order shown on screen. The reader clicks in screen order and ends up opening the wrong document first.

| | Without numbers (alphabetical) | With numbers |
|---|---|---|
| Actual learning order | concept → cases → collaboration | concept → cases → collaboration |
| Order shown on screen | ai-as-partner (3rd shows first) → beyond-coding → what-is… | 01-what-is… → 02-beyond… → 03-ai-as-partner |

**Rules**

- Use **two digits** (`01-`, `02-` …). One digit breaks the order from the 10th file on
- **Match the README's "learning order" section exactly.** If you change the order, rename the files too
- **`README.md` gets no number.** GitHub auto-renders it below the folder contents, so its list position doesn't matter, and numbering it breaks that auto-display
- When renaming a file, **update every link pointing to it** (README, other bodies' next/previous links, output paths in WorkLogs and the Roadmap)

## Final read-through (on module completion)

- [ ] Read start to finish from a first-timer's point of view
- [ ] **Zero sentences where understanding stalls**
- [ ] No point where the reader is left asking "so what do I do right now?"

## Result of reviewing the Roadmap with this checklist (2026-08-10)

Following the verification method for M1's Exercise 3, this checklist was used to review `vl_roadmap/20260810_RoadMap_VibeCoding-Starter-Guide.md`.

| Item | Result |
|---|---|
| 1. Plain language | ⚠️ Pass — but the Roadmap is an **author-facing internal document**, so terms like DoD/Capstone/Self-Assessment are used as-is. This does not apply to participant-facing outputs |
| 2. One action = one step | ✅ Exercise steps are all broken into numbers |
| 3. Checkpoints | ✅ Every exercise has a "verification method" |
| 4. Encouragement + reality | ✅ M6 enforces both encouragement and reality via DoD |
| 5. Cite the source | ✅ M5·M6 reference materials tag file path and line number |
| 6. Video links inline | ✅ Reflected in 4 places: first-principles table + M2·M6 DoD + M7 final review + success criteria |
| 7. Dual purpose | ✅ M7 splits participant vs. facilitator |
| 8. Document format | ✅ No horizontal rules, blank line before tables confirmed |

**Conclusion**: Pass. Item 1 differs in standard between the Roadmap and participant-facing outputs, noted as above.
