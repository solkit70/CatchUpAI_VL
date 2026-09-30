---
title: "Five Criteria for Choosing a Tool—Use the Same Standard Now and Later"
created: "2026-09-20 10:05:00"
module: M1
tags:
  - chrome-remote-desktop
  - guides
  - comparison
---

## Why set criteria first?

The reason I use Chrome Remote Desktop today is simple: **Google makes it, and it is free**. Those are good reasons, but **they are not enough to compare it with another tool**.

So I start with **five questions**. They still work when the tools change or new ones appear years from now. In M6, I will compare RustDesk, AnyDesk, TeamViewer, Windows Remote Desktop, Parsec, and Tailscale using the same questions.

## Five questions

| # | Question | Why ask it? |
|---|---|---|
| **Q1** | **What is free, and where does the free tier stop?** | Many tools say “free” but restrict use beyond a certain point. Some may even disconnect you if they decide your use looks commercial. |
| **Q2** | **Whose servers carry my screen?** | My home screen can show documents and email. Which company’s servers carry those images, and are they encrypted? |
| **Q3** | **What happens if my account is compromised?** | How bad is it if someone gets the key? Is two-step verification available, and can I review access history? |
| **Q4** | **Who made it, and which country’s laws apply?** | Whom do I contact if something goes wrong? In which country is the data stored? |
| **Q5** | **Does it actually work on my computer (Windows 11 Home)?** | Some tools do not work on the Home edition even when you expect them to (Windows Remote Desktop is one example). |

## Comparison table

> ✅ = checked · ⬜ = to be completed in M6

| Criterion | **Chrome Remote Desktop** ✅ | RustDesk ⬜ | AnyDesk ⬜ | TeamViewer ⬜ | Windows Remote Desktop ⬜ | Parsec ⬜ | Tailscale + VNC ⬜ |
|---|---|---|---|---|---|---|---|
| **Q1 Free tier** | Free. No separate plan or usage limit is listed. | | | | | | |
| **Q2 Servers / encryption** | Connection goes through Google servers. Google says **“all remote desktop sessions are fully encrypted.”** | | | | | | |
| **Q3 If account is compromised** | Serious: an authorized person can access **apps, files, email, documents, and browsing history** (official). Use Google Account two-step verification **and a PIN**. | | | | | | |
| **Q4 Provider / jurisdiction** | Google (United States) | | | | | | |
| **Q5 Windows 11 Home** | ✅ Works (supports Windows, Mac, and Linux) | | | | | | ⚠️ Key question: Home cannot host an RDP session |

### Chrome Remote Desktop: facts checked (2026-09-20)

- **Supported devices:** Mac, Windows, and Linux computers, plus mobile devices (dedicated app). Linux uses a 64-bit Debian package.
- **Setup:** In Chrome, open `remotedesktop.google.com/access` and select Download. You may be asked for your computer password during installation or asked to change a security setting.
- **Connection:** Enter a **PIN** to connect to another computer. (Google’s help does not specify PIN length or rules, so we choose at least six digits that are hard to guess ourselves. See M3.)
- **Encryption:** Google says, “All remote desktop sessions are fully encrypted.”
- **Access scope:** An authorized person can access **apps, files, email, documents, and browsing history**.
- **Share your screen with someone (Remote Support):** Create a code at `remotedesktop.google.com/support`; the other person enters it, and **their email address appears for your approval**. The **code works once**, and continued sharing prompts you every **30 minutes**.

Sources: [Chrome Remote Desktop Help](https://support.google.com/chrome/answer/1649523?hl=en) · [Access page](https://remotedesktop.google.com/access)

## How to read the table

**No tool has ✅ in every column.** The goal is not to pick “the best one,” but **the one that fits your situation**.

For my situation, the priorities are:

| Priority | Reason |
|---|---|
| 1. Q5—Does it work on my computer? | If it does not, the other criteria do not matter. |
| 2. Q1—Is it free? | I do not want to pay for another tool. |
| 3. Q3—How bad would an account compromise be? | The home computer has my vault and work files. |
| 4. Q2—Which servers carry the connection? | I already trust Google with email and calendar, so this does not add a new provider. |
| 5. Q4—Who made it? | Useful context. |

> 📌 **M6 result (scope changed 2026-09-27):** The six blank columns are filled in the [alternatives comparison](../../06-Alternatives-and-GrokBot/guides/comparison-table.en.md). The user chose not to install RustDesk because an additional app would use more CPU, memory, and storage on a modest laptop. There is no immediately available “second option” to switch to. If CRD fails, follow the [checks that do not require installation](../../06-Alternatives-and-GrokBot/troubleshooting/when-crd-fails.en.md).

## Rules for filling in the table

1. **Include only facts checked in official documentation.** Mark blog or YouTube claims “needs verification.”
2. **Add a source URL to each cell.** Policies may change, so recheck them later.
3. **Record the date checked.** Pricing and free tiers change often.
4. **Leave unknowns blank.** A guess can later be mistaken for a fact.

← Previous: [../examples/my-setup-diagram.en.md](../examples/my-setup-diagram.en.md)
→ Continue in M6: [comparison-table.en.md](../../06-Alternatives-and-GrokBot/guides/comparison-table.en.md)
