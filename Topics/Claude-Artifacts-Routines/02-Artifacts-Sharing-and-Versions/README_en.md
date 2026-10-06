# M2 — Artifact Official Documentation · Sharing Scope · Versions

**Status:** ✅ Complete (2026-09-13 during Live #27; 45 minutes actual / 2.5 hours estimated). Comments and watch were marked “not applicable” due to account limitations as then understood.

This module answered the original question: **“Why can’t a page connected to `db` be shared by link?”** The answer: **the page and its data have different sharing scopes.** With a public link, anyone can view the HTML, but only signed-in Claude users see DB data—anonymous viewers see an empty shell. This cannot be fixed with a setting; it is structural. A related finding was that this account is Pro/Max, so it did not show editor or organization-sharing options and was initially believed unable to use comments.

## Learning sequence

1. [Excerpt from official Claude Code Artifacts documentation](../vl_materials/2026-09-13%20Claude%20Code%20Artifacts%20공식%20문서%20발췌%20(code.claude.com).md) — quotations about sharing, versions, comments, and restrictions.
2. [Excerpt from artifact-capabilities skill](../vl_materials/2026-09-13%20artifact-capabilities%20스킬%20발췌%20(contract%200.2.46).md) — eight capabilities served to this account and sharing-related statements.
3. [Sharing scopes](concepts/sharing-scopes_en.md) — three scopes, page layer vs. data layer, and checks before sending a link.
4. [Capability roster](concepts/capabilities-roster_en.md) — eight capabilities at a glance, use cases, public-share availability.
5. [Sharing matrix](guides/sharing-matrix_en.md) — **observed 2×2 experiment and answer to question 1**.
6. [Minimal static](examples/minimal-static.html) and [minimal DB](examples/minimal-db.html) experiment source; published artifacts: [static](https://claude.ai/code/artifact/3f864d29-c5c5-4d6c-b696-37fcc798ee62) · [DB](https://claude.ai/code/artifact/a3bb593a-c879-42c2-b996-e11cc167ec1d).
7. [Shared link shows an old version](troubleshooting/shared-link-shows-old-version_en.md) — reanalysis of the Sep 7 issue.

## Left open

- Whether a **different signed-in account** can actually read DB data (the dialog says it can) → M3.
- Whether the Share menu has an “Always share latest version” toggle after public sharing → user to check in a later session.
- Comment and editor exercises → deferred until a Team/Enterprise account becomes available.

## Previous / next

Previous: [M1 — Inventory and Questions](../01-Inventory-and-Questions/README_en.md). Next: `03-Artifacts-Capabilities-Lab/` (to be created at the start of M3).

[Korean original](README.md)
