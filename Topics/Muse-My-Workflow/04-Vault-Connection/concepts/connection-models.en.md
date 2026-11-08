# Two Models for Connecting the Vault and Muse

[한국어](connection-models.md)

These are concepts to know before comparing the 8 candidates in M4. They are organized from the M4 "key concepts" in roadmap v2.0 and from facts checked in M4 Labs 1 · 2 (expanded by Claude Code on 2026-11-07).

## 1. Cloud-Agent Model and Remote-Console Model

| | Cloud-agent model | Remote-console model |
|---|---|---|
| Where the work happens | Muse's computer (cloud) | Home PC (Claude Code, etc.) |
| Role of the phone | Where you give instructions and get results | A remote control that operates the home PC |
| If the home PC is off | Still works | Does not work |
| Vault rules | It is outside the vault, so the rules must be given separately | Uses the vault and its rules as they are |
| Material | **Leaves the vault** through a mirror copy · connector | Stays inside the vault |
| Candidates in this Topic | A Dropbox · B GitHub · C Drive · Box · G desktop · H custom connector | E Remote Control · F Claude Code web · mobile |

The conclusion of the earlier Topic [Claude-Code-Mobile-Remote-Execution](../../../Claude-Code-Mobile-Remote-Execution/README.md) was "mobile is the control console, execution is local." Manual transfer (D) belongs to neither model; it is the baseline — a person downloads and uploads by hand.

## 2. Connection, Not Sync

I could not find, in the official documentation, a "sync" feature that keeps Muse's computer and my folder matched. Files go in by upload (System Files) or through a connector, and a connector brings in only as much as is needed for the work. So the picture is not "a synced vault mirror copy inside Muse" but **"Muse looking into my storage each time it needs to."** This is also why no candidate yet meets "the work I did away is already at the home PC by itself" (scenario S5), which was the starting point of this Topic. → [Scenario comparison table](../guides/seamless-scenarios.en.md#scenario-comparison)

## 3. A Selected Mirror Copy and the Inbox

- **The original is always the vault.** The mirror copy is copied in **one direction** only, from the vault to the mirror copy folder.
- **Only what is marked public goes in.** By default only Markdown with `visibility: public` is included. Internal markers · personal · unclassified · paths not allowed · large files · non-Markdown are left out. → [Mirror policy draft](../guides/mirror-policy.en.md)
- **Muse only reads the mirror copy and writes its results to the inbox.** This is because the mirror copy is overwritten at the next copy. Keeping the reading place and the writing place separate prevents conflicts.
- **The preview comes first.** The result of running a preview on the real vault (11/5) was 3 candidates to include · 55,975 excluded · 0 copied, and all documents with internal markers were left out. A real copy is made only after Changsoo Park approves the preview report.

## 4. Connecting Is the Same as Having Uploaded

Once you connect a connector, the material in that storage becomes material Muse can see. So connecting is judged with the same weight as "uploading files" (the connection rule from the M1 expansion). There are three things to check before connecting.

1. **Permissions** — read only, or also write · delete · share? (Drive showed settings per action)
2. **Scope** — can it be narrowed to one folder · one repo? (Could not be judged from the screen alone — needs testing)
3. **Training use** — is my material used for model training? (Could not find a switch to turn it off in Data controls on the web)

## Common Misunderstandings

- **A private repo and cloud storage are also outside the vault.** Uploading the whole vault breaks the internal material rule. Not "everything" but "only as much as needed."
- **One tool does not do it all.** The result is not one right answer but a "route table by type of work" — for example, voice memos in Muse, viewing vault material through the mirror copy, and work that needs vault rules in Claude Code at home.
