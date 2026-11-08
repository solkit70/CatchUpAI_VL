# Steps and Prompt to Fit Inbox Documents to the Vault Rules

[한국어](vault-cleanup-prompt.md)

> This is the cleanup done at home after a document made in Muse while away arrives in the inbox. Changsoo Park chose the inbox as **A — straight into `_Inbox_/` at the vault root** (2026-10-25). For the comparison and candidates, see [transfer-comparison.en.md](transfer-comparison.en.md). For the test result, see [../examples/sample-transfer.en.md](../examples/sample-transfer.en.md).

## Cleanup Steps (6 Steps)

| # | Step | Reason |
|---|---|---|
| 1 | **First check that there is no internal or secret content** — contacts · amounts · accounts · 🔒 marks | Even from the vault, it can become a document that goes outside |
| 2 | Rename the file to `YYYY-MM-DD Title by Muse.md` and put it in `_Inbox_/` | The vault's output naming rule (`YYYY-MM-DD [Name] by [Agent]`) |
| 3 | Add frontmatter with **lowercase English keys** — `title` · `created` · `author` · `tags` + source marking (`origin` · `reviewed`) | Vault rule. Muse has made Korean keys before |
| 4 | Lower the first line `# Title` to `## Title` (after the frontmatter, start with a section heading) | Vault structure rule ("Don't duplicate the title as H1") |
| 5 | **Don't edit** the body. Only check whether links, tables, or lists are broken, and if so, fix only that spot | Keeps the original wording Muse wrote |
| 6 | Change `reviewed` to `true` only after a person has read it | If "reviewed or not" becomes false information, the source marking is useless |

## Frontmatter Rules

```yaml
---
title: "Document title"
created: 2026-10-25 07:00:00
author:
  - "Muse"
tags:
  - muse-inbox
origin: muse
reviewed: false
---
```

- `origin: muse` and `reviewed` are this Topic's source marking (made in Muse · reviewed or not). `created` takes care of the date.
- `created` is **the time it was created in the vault**. The time Muse made it is often unknown, so it is not used.
- Write `tags` as a list without `#`. When cleanup is finished and you move it to its proper place, remove the `muse-inbox` tag.

## Claude Code / Codex Prompt

```text
Please clean up the Muse document that arrived in the inbox so it fits the vault rules.
Target file: {file path}

1. First check whether it has contacts, amounts, accounts, passwords, or 🔒 marks. If it does, don't clean it up — tell me.
2. Rename the file to `YYYY-MM-DD Title by Muse.md` and put it in `_Inbox_/`.
3. Add frontmatter in the format below. Keys are lowercase English. Don't use Korean keys.
   title · created (current time YYYY-MM-DD HH:MM:SS) · author (- "Muse") · tags (- muse-inbox) · origin: muse · reviewed: false
4. Lower the `# Title` on the first line to `## Title`.
5. Don't change a single character of the body text. Only tell me where links, tables, or lists are broken, and if you fixed something, write down where you fixed it.
6. Leave `reviewed` as false. I'll change it after I read it.

When you're done, report what you changed in 5 lines or fewer.
```

## One Line to Put in the Packet When Sending Work Away

The home → away packet also needs to tell Muse this rule, so Muse makes it right from the start.

```text
Vault frontmatter uses lowercase English keys (title · created · author · tags), and a document's first heading starts with H2 (##).
```
