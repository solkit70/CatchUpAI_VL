---
title: "Muse First-Use and Public-Material Verification Results"
source: "https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/"
author:
  - "박창수"
  - "Codex"
created: "2026-10-11 06:47:40"
tags:
  - ai-agent-apps-compare
  - muse
  - hands-on
---

# Muse First-Use and Public-Material Verification Results

[한국어](first-task-results.md)

## Scope

After reaching Muse's initial web screen on 2026-10-11, we checked a first read-focused task, settings screens, and research into official materials. Connected-app permission screens were also inspected, but actual email, schedules, account-specific settings, and their screenshots are excluded from this public record.

## First Task: Read-Focused Schedule Summary

Muse was asked to summarize aggregates only, excluding event titles, attendees, descriptions, and links, and to change nothing. Its first answer confused the entire day with time from the present onward, counting elapsed periods as free time. When asked to recalculate from the current time, it separated the remaining portion of an ongoing event from later events and followed the requested side-by-side Seattle/Korea time format.

**Assessment**: Do not assume time accuracy from the first answer alone. We confirmed that follow-up questions identifying date boundaries, time zones, and already elapsed periods can improve the calculation. Personal schedule values are not retained in this record.

## Concepts Observed in Settings

Data controls separated model-improvement use of interactions from data-management items. Permissions distinguished default consent behavior for connectors/web access from per-action read/write/delete permissions. Thus, check the actual per-action permission screen rather than relying on the general phrase “sensitive actions always require approval.”

The images below have been edited to show only action names on Gmail and Google Calendar permission screens. Account-specific Allow/Ask choices are masked in this public record.

![Gmail per-action permissions. Account-specific Allow/Ask values are masked.](../assets/muse-screenshots/gmail-permissions.png)

![Google Calendar read and write permissions. Account-specific Allow/Ask values are masked.](../assets/muse-screenshots/calendar-permissions.png)

![Google Calendar write permissions. Account-specific Allow/Ask values are masked.](../assets/muse-screenshots/calendar-write-permissions.png)

## Public-Material Research and Source Verification

Muse's first research answer provided a Sources panel, but the initially visible entries were mainly third-party sources such as media and summary sites. After requesting official material for each claim, it provided Meta announcement and Meta Help URLs.

### Claims Checked

| Claim | What official sources confirmed |
|---|---|
| Secure VM / Sentinel | Meta's announcement describes a dedicated cloud VM and separate Sentinel. It says Sentinel approves internet access and requests user permission when necessary. |
| Background work | It describes continuing long-running tasks after the app closes and returning to request approval when necessary, such as for sending email or making purchases. |
| Memory-based suggestions | It says Muse can remember information mentioned only once and proactively suggest or act, and users can ask it to forget specific memories. |
| Free/subscription scope | Free usage has a limit; users can wait or subscribe after reaching it. Power is $20/month with 500M tokens/week; Maximum is $100/month with 3B tokens/week. Subscriptions renew automatically each month. |
| Free-tier limit | Official subscription help states that free usage is limited but does not provide an exact weekly token count. The figure of 100 million tokens/week is not treated as officially verified. |

> “Muse is available for free with a usage limit.”

**Source-quality assessment**: Third-party material in the first Sources panel can provide research leads, but cannot replace official evidence for Meta policy/pricing claims. Evidence improved after explicitly requesting official URLs and titles.

### Sources Panel Reference

The initial source list consisted mainly of third-party materials. The screen below shows how the panel exposes individual page titles and domains. Meta's official pages were separately located and checked when citing official claims.

![Muse Sources panel. The displayed third-party results were not used as official evidence.](../assets/muse-screenshots/source-panel.png)

## Verified Official Sources

- [Introducing Muse: The World's First Personal AI Agent Built for Everyone](https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/) — Meta's official announcement. Features, security, privacy, and free availability. Checked 2026-10-11.
- [About Muse subscriptions](https://www.meta.com/help/subscriptions/1021145227643680/) — Meta Help Center. Usage limits, Power/Maximum pricing and tokens, automatic renewal. Benefits and availability may vary by region/account. Checked 2026-10-11.

## Apply in the Next Exercise

- In the same public-material task, check claims, cited URLs, and source domains individually.
- Specify time zone and reference time for time calculations, then independently verify results.
- Check per-action Allow/Ask values for connected-app permissions, rather than relying on default-setting wording.
- Exclude personal account states and real schedule/email contents from public deliverables.
