---
title: Bila AI Agent M2 - Data Source & Phase 1
created: 2026-07-26 07:15:04
tags:
  - bila-ai-agent
  - m2
  - vibelearn-ai
---

## Module Overview

M2 connects Bila AI Agent to external knowledge sources and verifies whether Phase 1 Q&A can answer real Builders Lounge questions from evidence. The current priority is external source connection validation after the Google Drive persistence bug fix. Slack is also required because most Builders Lounge online conversation happens in Slack.

Source context: [[Ingest/CatchUpAI_VL/Topics/Bila-AI-Agent/vl_worklog/20260705_M2_Bila-AI-Agent|M2 previous WorkLog]] and [[Ingest/CatchUpAI_VL/Topics/Bila-AI-Agent/vl_roadmap/20260628_RoadMap_Bila-AI-Agent|Bila AI Agent Roadmap]].

## Learning Order

1. [guides/google-drive-connection-guide.md](guides/google-drive-connection-guide.md) - Reconnect Google Drive after the Gobi fix and verify persistence.
2. [guides/slack-connection-guide.md](guides/slack-connection-guide.md) - Connect the Changbal Slack workspace and invite Gobi bot to the required public channels.
3. [prompt-iterations/prompt_v2_2_after_drive_fix.md](prompt-iterations/prompt_v2_2_after_drive_fix.md) - Apply the production prompt that explicitly names GitHub and Google Drive as data sources.
4. [test-results/qa-test-phase1-final.md](test-results/qa-test-phase1-final.md) - Run the final 10-question Phase 1 validation and record exact outputs.

## Previous And Next Modules

Previous module: [../01-Agents-Setup](../01-Agents-Setup)

Next module: [../03-Channel-Admin](../03-Channel-Admin)

## Completion Criteria

- [x] GitHub repository attached and verified.
- [x] System prompt updated to mention the GitHub repository.
- [ ] Google Drive folder attached and persisted after leaving/re-entering Agents settings.
- [ ] Drive marker test returns `DRIVE-TEST-7749`.
- [ ] Slack workspace connected.
- [ ] Gobi Slack app invited to required public Builders Lounge channels.
- [ ] Phase 1 final test passes at least 7 of 10 questions.
- [ ] Data connection before/after comparison is documented.
