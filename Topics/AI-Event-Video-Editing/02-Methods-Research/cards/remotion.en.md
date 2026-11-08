---
title: "Research Card — Remotion: Intros, Captions, Repeatable Templates"
author:
  - "Codex"
created: 2026-10-24 22:52:50
source: "https://www.remotion.dev/docs"
tags:
  - ai-event-video-editing
  - research-card
lang: en
---

## Summary
[한국어](remotion.md)

**Group E · checked 2026-10-24 · documents only / not practiced in this Topic.** A candidate that assembles video and graphics with code, kept separate from a model that understands scenes and selects them on its own. It is the researcher's judgment that it may suit templates where the intro, captions and logo repeat for each event.

## Features, language, limits

The [video embedding documentation](https://www.remotion.dev/docs/videos/) describes start segment, frame length and placement, and the [parameters documentation](https://www.remotion.dev/docs/parameterized-rendering) describes a structure where content changes with input values such as event name and date. The [captions documentation](https://www.remotion.dev/docs/captions/) describes importing SRT/VTT and caption output paths. Which scenes to use has to be decided by a person or by connecting a separate analysis.

Korean text, fonts, line breaks and render results need actual checking. It is not a candidate with a fixed SaaS upload limit, and local rendering and cloud rendering are kept separate in terms of resources, cost and where the media is. Importing the output video into Premiere is different from the text and effects in the source code carrying over as Premiere elements.

## Cost and license

> “free to use for individuals and companies up to three people”
> — [Remotion official license page](https://www.remotion.pro/license), checked 2026-10-24

The official page separates the Free License for individuals and companies of 3 people or fewer from the Company License conditions for collaboration and companies of 4 or more. The Company License lists Creators at $25/month per seat, and Automators at $0.01 per render with a minimum of $100/month. **The client's organization and form of collaboration are unverified, so I do not conclude it can be used for free.** External rendering, AI, font and music costs are also separate.

## Judgment for this Topic

Keep it as a comparison candidate for short intros and repeatable templates, and combine it with other tools for scene selection from long videos. The [official getting started guide](https://www.remotion.dev/docs) introduces a coding agent path and a ChatGPT desktop plugin path, but this time I did not install the plugin or check whether it can be used.

In follow-up practice, build a 5–10 second template that only changes the event name, date and logo, and check Korean rendering and Premiere import. This belongs to M5, and this document research does not mark a demo video as completed.
