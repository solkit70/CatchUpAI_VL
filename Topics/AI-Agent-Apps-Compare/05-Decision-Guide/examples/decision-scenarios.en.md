---
title: "Agent Selection Examples"
source: "[[selection-criteria]]"
author:
  - "박창수"
  - "Codex"
created: "2026-10-11 07:38:08"
tags:
  - ai-agent-apps-compare
  - examples
---

# Agent Selection Examples

[한국어](decision-scenarios.md)

| Work example | Recommended approach | Evidence and limits |
|---|---|---|
| Research public materials and summarize facts | Delegate a research draft to an agent with search/source features; a person checks official originals | Muse's first Sources panel mainly contained third-party material; official material was verified after separately requesting official URLs. Source display alone does not complete verification. |
| Calculate conflicts and totals in a fictional timetable | Delegate analysis and compare against an independently calculated answer | Muse correctly found overlaps and totals in M4's fictional timetable. This does not guarantee the same quality on real schedules. |
| Convert notes into a post draft in a fixed format | Use draft generation; a person edits factual grounding and rhetoric | Muse met the format but left unsupported wording, requiring final review. Nothing was published. |
| Take real actions in connected email/calendar | Check necessary permissions per action; begin with reading/drafting where possible; human review before external changes | Muse permissions may vary by action. This M4 did not test connector-operation performance. |
| Manipulate local code/files | Compare the task scope with existing coding tools before choosing | Codex and Claude Code were not compared on identical tasks in this topic, so no performance judgment is made. |
| Service whose usage conditions are not met | Record only features/access from official materials and defer practical suitability judgments | Dots, Grok Bot, and Instinct were not hands-on targets in this run. |

## How to Use These Examples

Rather than treating each row as a universal rule, recheck data sensitivity, action impact, current access, and verification methods for the particular task. In particular, one or two successes do not guarantee a service's overall accuracy or safety.

## Observation Evidence

- Sources/permissions: [M3 source verification](../../03-Hands-On/guides/first-task-results.en.md#public-material-research-and-source-verification), [settings concepts](../../03-Hands-On/guides/first-task-results.en.md#concepts-observed-in-settings)
- Calculation/generation: [M4 decisions table](../../04-Real-Task-Trial/guides/trial-results.en.md#results-table)
- Access conditions: [M2 practice decisions](../../02-Comparison-Table/guides/comparison-table.en.md#practice-decisions-for-this-topic)

Local-tool selection is a work-environment consideration, not a conclusion from experimental comparison of tool performance.
