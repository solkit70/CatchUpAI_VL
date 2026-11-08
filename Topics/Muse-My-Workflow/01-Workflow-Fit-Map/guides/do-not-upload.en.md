# What Not to Upload to Muse — One-Page Summary
[한국어](do-not-upload.md)

> Muse is a cloud service run by Meta. Anything that must not leave the vault is not uploaded to Muse either. It falls under "internal" in judgment criterion ① data grade — [../concepts/fit-criteria.en.md](../concepts/fit-criteria.en.md). The v2.0 revision (2026-10-25) added the "connection rule" and the "naming rule."

## What Not to Upload

| Type | Examples | Why |
|---|---|---|
| **Documents marked internal** | Documents and folders with frontmatter `visibility: internal` · a 🔒 mark in the body | Under vault rules, they are not sent outside |
| **An organization's internal material** | Company IR · internal meeting summaries · settlements · amounts | Non-public information of the organization and participating companies |
| **Client information** | Consultation content · client names · materials a client gave | The client has not agreed |
| **Other people's contacts** | Mailing lists · email addresses · phone numbers | Personal information |
| **Accounts · passwords** | Login information · verification codes · API keys | Security |
| **Original photos · receipts** | Photos of personal documents · ID cards · receipts | Personal information · amounts |

## When It Can Be Split Off and Delegated

Even work mixed with internal material can be delegated if **only the public part** is split off. Example: while preparing an organization's event, "organize the public event schedule · venue · public speaker information" can be delegated, while analysis of participating companies is done at home. Client work can also be delegated if it is a general topic that does not reveal the client, like "research AI tools for video editing."

## Connection Rule — Decision: ③ Mail · Calendar (v2.0)

If you connect mail · calendar · storage to Muse, Muse reaches their contents regardless of the "don't upload" rule. According to the help pages, Muse pulls only as much as it needs while working, but information it already used may remain in memory even after you disconnect. There is no explicit statement that turning off training use also blocks connector data, and the Dropbox help page states that connected data may be used for training — [feature table](../examples/muse-feature-check.en.md).

| Option | What becomes possible | Cost |
|---|---|---|
| ① No connection | I handle mail and schedule work myself | Safest, but I can't use Muse's big strengths (mail · schedule · reminders) |
| ② Calendar only | Checking and adding events · recurring reminders (#20) | Event titles · locations · attendee names go into Muse |
| ③ Mail · calendar | ② + checking and organizing mail · reply drafts (#19), moving and handing off by mail (M2) | Muse reaches an organization's internal mail and other people's contacts in the inbox |
| ④ Up to storage (Dropbox · GitHub) | Reading a vault copy · inbox (M4) | Only after approving the copy rules and the first upload in M4 |

**Whichever you choose, keep these**
- Turning off training use: the help page says it can be turned off in Settings → Data controls, but **on 2026-10-25 the Data controls screen of web Muse did not have that switch** (only Import memory · Download your agent data · Reset Muse). The phone app and other menus have not been checked yet. Until it is confirmed, assume it cannot be turned off, and use this page's "What Not to Upload" as the line of defense
- Keep Settings → Permissions → Connectors at "Ask for some actions" (default) or stricter — do not use "Always allow"
- By default, do not connect work accounts — if one becomes necessary, show the account and scope at that time and Changsoo Park approves it (2026-10-25 Changsoo Park: "If needed, I can connect a work account too")
- Know how to disconnect (Settings → Connectors) and how to erase memory (forget)

**Decision (2026-10-25, Live #33)**: **③ Mail · calendar** — I decided to keep Gmail and Google Calendar connected and in use. No other new connections (including storage) will be made. **I keep this even knowing there is no switch to turn off training** (Changsoo Park decision A, same day). I decided that Muse may be asked to handle an organization's internal content and contacts inside mail — but this permission applies **only to inbox mail**, and vault documents (`visibility: internal` · 🔒) and the "What Not to Upload" list above stay as they are. When moving mail content into the vault or a public document, follow the vault rules. ④ will be decided separately in M4 after the copy rules and first upload are approved. Any of the 4 common settings above that are not yet verified will be checked at the start of M2.

## Naming Rule — Decision: ② Names and Relationships Only (v2.0)

According to a TIME report (2026-10-06), Muse updates records about the user and the people the user mentions — including people who don't use Muse — every hour. The more you put in other people's names, the more records about those people pile up.

| Option | Example | Fits / cost |
|---|---|---|
| ① Leave out (v1 rule) | "Follow-up meeting next week with someone" | Safest. Post-event follow-up notes (#21) and reply drafts (#14) become less useful |
| ② Names and relationships only | "Follow-up meeting next week with CEO ○○" — leave out contacts, amounts, and an organization's internal decisions | Organizing memories right after an event and reply drafts become useful. Records about that person pile up in Muse |
| ③ As is | No limits | Not recommended — it conflicts with the internal material rule |

**Decision (2026-10-25, Live #33)**: **② Names and relationships only** — write it like "Follow-up meeting next week with CEO ○○." Contacts, amounts, an organization's internal decisions, and client consultation content are still left out. I chose this knowing that records about that person pile up in Muse. Files with many names in them, such as photos and roster files, follow "What Not to Upload" above rather than this rule.

## If You're Unsure

- "Would it be okay if this content appeared on the broadcast screen?" — If not, don't upload it.
- Notes of my own thoughts and to-dos (personal grade) can be uploaded, but other people's names follow the **naming rule** above, and contacts are always left out.
- Connecting mail · calendar · storage follows the **connection rule** above.
- The rules on this page apply unchanged to the vault copy (M4) as well.
