# Claude Artifacts and Routines — Using Them Well

> A topic that relearned two features encountered during work, starting from real artifacts already built and checking them against official documentation and experiments. Artifacts are webpages/apps published by Claude, including runtime features such as databases, viewer identity, files, and comments. Routines are Claude Code tasks that run in the cloud on a schedule, even when the local PC is off. The capstone is a Remotion video: “AI found a feature I didn’t know.”

| | |
|---|---|
| Period | Roadmap began 2026-09-13; in progress (M1–M5 completed 2026-09-27) |
| Status | ✅ M1–M5 complete · 🔄 M6 video — slide plan awaiting review |
| Actual time | M1 50 min · M2 45 min · M3 about 1 hour · M4 about 1h 35m (Sep 21 + 27) · M5 about 25 min. About 4h 40m of the roadmap’s estimated 15h. |
| Starting point | Existing work: event booth-layout editor, booth status board, event entry page, and weekly job-posting check routine. On review there were **seven** real artifacts, not four. |
| One-line result | **When a person and AI edit the same data, `if_version` protects the person’s change, while a quiet automation can hide its own failure.** Both were directly observed. |

## What we found

- **A public link does not expose data from a DB-backed page.** Page and data have different visibility. Anyone can see public HTML, but only signed-in Claude users can see DB data. This is structural, not a setting. See the [M2 sharing matrix](02-Artifacts-Sharing-and-Versions/guides/sharing-matrix_en.md).
- **`if_version` protects writes from an AI session.** After a person changed the page from v2 to v4, the session’s write based on v2 was rejected with `version_mismatch`; a write based on reread v4 succeeded. Page-side writes use last-write-wins. See [M3 DB round trip](03-Artifacts-Capabilities-Lab/guides/db-roundtrip_en.md).
- **A “notify only when conditions match” routine failed silently for three weeks.** The cause was cloud environment network mode (`Trusted` = allowlist only), not the routine itself. A failed week and a week with no postings both looked like “no news.” See [M4 WBLP audit](04-Routines-Lab/guides/wblp-routine-audit_en.md).
- **Connectors (Gmail/Calendar) do not depend on the network allowlist.** The second routine succeeded in 25 seconds without changing the environment. Green in the run list means “no infrastructure error,” not that the task succeeded. See [M4 second routine](04-Routines-Lab/guides/second-routine_en.md).
- **If the task uses the vault, run locally; if it only uses external services, cloud may fit.** A cloud routine clones only the selected GitHub repository and cannot read this local vault. See [M4 decision table](04-Routines-Lab/concepts/local-vs-cloud_en.md).
- **Verify “it cannot” claims through direct testing too.** M2 concluded from one sentence in documentation that comments were unavailable on this account; M3 observed comments and Send to Claude working. See [M5 anti-pattern 10](05-Usage-Patterns/guides/anti-patterns_en.md).

## Modules (learning order)

| # | Module | Status | Key outputs |
|---|---|---|---|
| 1 | [Review of existing work and questions](01-Inventory-and-Questions/README_en.md) | ✅ Sep 13 | [Inventory](01-Inventory-and-Questions/guides/inventory_en.md) (6/6 incognito checks matched) · [nine questions](01-Inventory-and-Questions/guides/questions_en.md) |
| 2 | [Artifact sharing and versions](02-Artifacts-Sharing-and-Versions/README_en.md) | ✅ Sep 13 | [Sharing scopes](02-Artifacts-Sharing-and-Versions/concepts/sharing-scopes_en.md) · [2×2 test results](02-Artifacts-Sharing-and-Versions/guides/sharing-matrix_en.md) · [Old version appears](02-Artifacts-Sharing-and-Versions/troubleshooting/shared-link-shows-old-version_en.md) |
| 3 | [Artifact runtime capability lab](03-Artifacts-Capabilities-Lab/README_en.md) | ✅ Sep 27 | Five examples (db, user, assets, comments, multiple files) · [DB round trip](03-Artifacts-Capabilities-Lab/guides/db-roundtrip_en.md) · [capability selection table](03-Artifacts-Capabilities-Lab/concepts/capability-selection-table_en.md) |
| 4 | [Routines](04-Routines-Lab/README_en.md) | ✅ Sep 27 | [Three-week failure diagnosis](04-Routines-Lab/guides/wblp-routine-audit_en.md) · [basics](04-Routines-Lab/concepts/routines-basics_en.md) · [second routine](04-Routines-Lab/guides/second-routine_en.md) · [local vs. cloud](04-Routines-Lab/concepts/local-vs-cloud_en.md) |
| 5 | [Usage pattern guide](05-Usage-Patterns/README_en.md) | ✅ Sep 27 | [Playbook](05-Usage-Patterns/guides/artifacts-routines-playbook_en.md) · [six patterns](05-Usage-Patterns/guides/patterns_en.md) · [ten anti-patterns](05-Usage-Patterns/guides/anti-patterns_en.md) |
| 6 | [Capstone — Remotion video](06-Capstone-Video/README_en.md) | 🔄 Plan review pending since Oct 4 | Korean video “AI found a feature I didn’t know” (duration follows content) · [25-scene plan](06-Capstone-Video/video-slide-plan_en.md) · [claim ledger](06-Capstone-Video/claim-ledger_en.md) |

New here? Start with the one-page [playbook](05-Usage-Patterns/guides/artifacts-routines-playbook_en.md). It collects what to choose and check before building.

## Where the order changed

M4 exercise 1 (routine audit) was moved earlier to Sep 21. It became incident response after discovering the only real routine had failed three weeks in a row. M3 was attempted with another tool (Codex) on the morning of Sep 27, got stuck, and was restarted from scratch that afternoon in the Claude Code extension for VS Code. That extension had direct tools to publish Artifacts and read/write DB data, so the exercise did not require browser automation.

## What remains unverified

- Can people outside the organization or public-link visitors comment? Only author-side comments were tested.
- Can a page-side +1 be lost when several people click at the same time? Confirmed in documentation only.
- The M3 examples were all private; checks from another account and incognito were skipped.

## Folders

| Folder | Contents |
|---|---|
| [vl_roadmap/](vl_roadmap/20260913_RoadMap_Claude-Artifacts-Routines.md) | Roadmap and progress table |
| [vl_worklog/](vl_worklog/) | Session WorkLogs — M1, M2, M4a, M3, M4b, M5 |
| [vl_materials/](vl_materials/) | Official-document excerpts (Artifacts, Routines, capability skill) |
| [vl_prompts/](vl_prompts/) | Roadmap and daily-learning prompts |
| [topic_starter.md](topic_starter.md) | Topic starting information |

[Korean original](README.md)
