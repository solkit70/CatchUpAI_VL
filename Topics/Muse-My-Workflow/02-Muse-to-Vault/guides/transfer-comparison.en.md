# Transfer Method Comparison and Default Methods

[한국어](transfer-comparison.md)

> These are results I tested hands-on in Live #33 Part 1 on 2026-10-25. The test material was one Markdown file (397 bytes) made with made-up content safe to make public (a heading · 3 list items · a 3-row table · 1 link · a last line). The test was done in **web Muse**, and the phone was marked "unverified" cell by cell. For the concepts, see [../concepts/transfer-paths.en.md](../concepts/transfer-paths.en.md).

## Away → Home (Muse Results to the Vault)

| Method | Result | Steps | Preservation | Phone | Watch out |
|---|---|---|---|---|---|
| ① Download one file at a time | ✅ | 3 (click card → ⋯ → Download) | Heading · list · table · link · last line all as-is | ✅ Open the file and tap ⋯ and a menu appears (2 steps). The menu names differ from the web — Pin · Search · Share · Copy text · Save to Files · Download as PDF · Delete. Save format unverified | The app had a feature that was not in the official help. The file name is the document title as-is (includes spaces · Korean) |
| ② Send to my own email | ✅ | One-line instruction to Muse + approve sending | The attachment is **byte-identical** (web 397B · phone 279B, both checked with a comparison tool) | ✅ Same result on the phone — a file made on the phone arrived as an attachment in Gmail on the home PC | Needs the Gmail connector. It gets mixed into the inbox of your mail. Sending is "Ask," so it needs approval |
| ③ Copy and paste | ✅ | 2 (⋯ → Copy → paste) | The **original Markdown** is copied as-is (not the rendered text). View source shows the same original | The phone menu has Copy text (no View source like the web) — the pasted result was not tested | To keep it as a file, there is one more step: save after pasting |
| ④ Download all data | ✅ | Settings → Data controls → Download your agent data | One zip (about 4MB · 103 items): conversation txt · inside `workspace/`, the Markdown Muse made with its folder structure as-is · uploaded files · manifest | ❓ | Received the same day I requested it. **It holds all your personal information at once** — it is for backup, not an everyday method |
| Share link | Not tested | — | — | — | It is not "a transfer" — if the account changes or the link expires, there is nothing in the vault |

## Home → Away (Let Muse Pick Up Ongoing Work)

| Method | Result | Preservation · continuing | Watch out |
|---|---|---|---|
| ① Upload a file (handoff packet) | ✅ | With a one-line instruction, it did both of the 2 "next steps." It said it "doesn't know" things not in the packet | It made Korean frontmatter keys → must be fixed at home. It filled in a date that was not in the packet on its own |
| ③ Public repo link | ✅ | It read the roadmap M2 that was online and summarized it accurately in three lines (nothing made up) | **Only what was pushed** is visible. Only public documents work |
| ② Send to my own email for Muse to read | ✅ (Changsoo Park's everyday-use report, 2026-10-25) | He says it works well on the home PC and in the phone and tablet apps. It was not separately tested under the same conditions in this session | Needs the Gmail connector. The content stays in your own mail inbox |

## Keeping the Original Wording of Voice

| Test | Result |
|---|---|
| A memo spoken by voice, with "Save it as a Markdown file without changing a single character" | ✅ One line was enough. The saved file is the same as the input text Muse transcribed — even filler words stayed, and no title or added words |
| Limits | What was compared is the transcribed text and the saved file. Only the speaker can judge whether the spoken sound and the transcribed text match (the brand name Muse was written as 「뮤즈」) |

## Recommended Default Methods

| Situation | Recommendation | Reason |
|---|---|---|
| Bring one Muse result while at the home PC | **① Download one file at a time** | Fewest steps, and the original is kept as-is |
| Send something made in Muse on the phone to home | **② Send to my own email** (tested on both web and phone) | Send with a one-line instruction in the app, and receive it in Gmail on the home PC. The attachment is the same as the original |
| Can't get the file, only move the text | ③ Copy and paste | The original is copied as-is |
| Home → away | ① Upload a handoff packet file; for public material, ③ repo link | Muse picks up the work from a one-line instruction |

**Recommendation table approval**: Changsoo Park approved it (2026-10-25, Live #33). After the phone test, ② was confirmed as the default phone method.

**One-line summary**: With any method, the original does not break. The differences between methods are **the number of steps, whether it works on a phone, and whether a connection is needed**. The really important work is the cleanup step that fits the file to the vault rules after the transfer.

## Inbox — Decision: A (Straight into `_Inbox_/`)

Changsoo Park chose **A**, as recommended (2026-10-25, Live #33). For the cleanup steps and prompt, see [vault-cleanup-prompt.en.md](vault-cleanup-prompt.en.md). Below is the candidate table used when choosing.

The vault already has an `_Inbox_/` folder ("notes waiting for right place" — it holds notes that haven't found their place, and has `_Inbox_.md`, which lists the notes in the same folder automatically).

| Candidate | Location | Pros | Cons |
|---|---|---|---|
| **A (recommended)** | Straight into `_Inbox_/` | Uses the existing purpose as-is, and the list is made automatically. No new folder rule | Things from Muse get mixed with other temporary notes → tell them apart by the source marking in the frontmatter |
| B | `_Inbox_/Muse/` subfolder | Only things from Muse are gathered separately | The automatic list in `_Inbox_.md` only picks up the same folder, so notes in subfolders don't show |
| C | `Ingest/Snippets/` | A storage place for short writing that came in from outside | It already holds cleaned-up writing, so mixing in "not yet reviewed" documents is awkward |

Muse also gave 3 candidates in the same direction (an Inbox inside the vault · an Inbox inside the Muse workspace · the Gmail inbox). But Muse said this without knowing the vault's real folders, so this table is the plan that fits the real structure.
