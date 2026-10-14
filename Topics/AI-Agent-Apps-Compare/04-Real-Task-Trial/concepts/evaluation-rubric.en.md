---
title: "Evaluation Criteria for Agents on Synthetic Work Tasks"
source: "[[README.md]]"
author:
  - "박창수"
  - "Codex"
created: "2026-10-11 07:23:37"
tags:
  - ai-agent-apps-compare
  - evaluation
---

# Evaluation Criteria for Agents on Synthetic Work Tasks

[한국어](evaluation-rubric.md)

## Task Design

Fix the input materials, desired output format, and success criteria before comparing. Fact-extraction tasks include verifiable answers and calculations; writing tasks define length, structure, and evidence boundaries. Changing criteria after execution undermines comparison, so record the reason for any change.

## Synthetic Data

Test with fictional names and content resembling only the structure needed for the purpose, instead of real customer, schedule, email, or account materials. Minimize materials provided to the agent; when no external-app action is needed, limit the task to pasting text into chat.

## Quality and Human Review

Inspect correctness, format compliance, unsupported additions, and required edits separately. Include missing information and wrong values in human correction time. Do not assert numerical time savings before agent response time, human review time, and a manual-work baseline have all been actually measured.

## Decisions

- **Usable**: Meets every success criterion and can be used after fact-checking alone.
- **Usable with edits**: Achieves the basic purpose but requires specific human corrections or verification.
- **Unusable**: Misses core requirements or contains major errors, making it better to recreate the result.

M4's specific tasks and results are recorded in the [task cards](../examples/task-cards.en.md) and [execution evaluation](../guides/trial-results.en.md).
