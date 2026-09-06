<!-- lang-switch -->
[🇰🇷 한국어](README.md) · 🇺🇸 **English**
<!-- lang-switch -->

# Big Tech Is Training Data Center Workers Directly

A record of **researching 6 US data center workforce programs over ten days — and actually applying to one of them.**

The whole process is documented: research, judgment, application, and failure. This isn't a cleaned-up summary — **the wrong calls and the things I couldn't confirm are still in here.**

> 📅 **Researched August–September 2026.** In this field, application windows **open and close within weeks.**
> One program's US postings vanished entirely within two days of being checked.
> **Always re-verify at the source before acting.**

---

## Why these programs exist

AI is driving a massive data center buildout — and **there aren't enough people to build them or run them.**
In the [Uptime Institute 2026 Global Data Center Survey](https://uptimeinstitute.com/about-ui/press-releases/16th-annual-2026-global-data-center-survey-deployment-of-high-density-racks-rising-fast-operators-face-continued-recruiting-and-retention-pressures), **more than half of respondents reported difficulty finding qualified candidates** (800+ operators; secondary coverage puts it at **53%**, up from 46% in 2025).

So Big Tech started **paying for the training themselves.**

| Company | Scale |
|---|---|
| **Meta** | **$115M** in year one |
| **Google.org** | AI Opportunity Fund **$50M** (~$20M of it for electrical training) |
| **Microsoft** | Curriculum, equipment, and scholarships to community colleges (since 2018) |
| **Amazon** | 12 months of paid training, then direct hire |

This isn't philanthropy. **Without people, the data centers don't run.**

---

## The 6 programs — at a glance

| # | Program | Backed by | Duration | Paid during training | Employer after | Where you apply |
|---|---|---|---|---|---|---|
| ① | **America's Workforce Academy** | Meta | 4 weeks | ✅ stipend + airfare + lodging | ⚠️ **Not Meta** — a partner construction company | Meta portal |
| ② | **Datacenter Academy** | Microsoft | 1–2 years | ❌ | Not stated | **Each community college** |
| ③ | **NABTU partnership** | Microsoft | Apprenticeship schedule | ❌ | Union construction company | TradesFutures |
| ④ | **Skilled Trades support** | Google.org | Years (apprenticeship) | ✅ | Union electrical contractor | **Local IBEW local** |
| ⑤ | **Work-Based Learning** | Amazon/AWS | 12 months | ✅ | ✅ **Direct AWS hire** | Amazon careers |
| ⑥ | **Technical Apprenticeship** | Amazon/AWS | Up to 18 months | ✅ | ✅ Direct Amazon hire | Amazon careers |

> ⚠️ **⑥ targets the military community** (veterans and spouses), and all current tracks
> are cloud roles. There is no hands-on data center track.

### 🔑 The mistake people make most often

**The company in the program's name is not the company that hires you.**

In **5 of the 6**, the operator, the funder, and the employer are three different parties.

- ④ Google.org — **there is nowhere to send Google an application.** Google funds it; a local IBEW local selects you
- ① Meta AWA — completing it makes you an employee of **a Meta partner construction company, not Meta**
- ② Microsoft — you're not applying to Microsoft, you're **enrolling at a college**

→ Detail: [Operator ≠ funder ≠ employer](02-Program-Anatomy/guides/who-actually-hires-you.en.md)

---

## 🔑 One question that sorts all six

If the program descriptions blur together, this settles it.

> ### Do you get paid while you train?

| | Yes | No |
|---|---|---|
| Which ones | ① Meta · ④ Google · ⑤⑥ Amazon | ② Microsoft · ③ NABTU |
| What it means | **An employer is training you to hire you** | **You're a student; employment is a separate problem** |
| Risk | Low — worst case, you spend time | High — **you spend money and time with no guarantee** |

**Two things both called "data center workforce programs" can be opposites.**
Meta AWA (free, paid, 4 weeks, conditional offer) and BBCC (student, self-funded, 1 year, no guarantee)
should not be compared side by side.

> 📌 **Even at $0 cost, a year with no income is, in real terms, a year of living expenses.**

---

## Five things I learned along the way

### 1. The bottleneck was **geography**, not qualifications

With 20 years in IT, I met most requirements. But **there were no postings in Washington State.**
Checked three times, zero every time.

Meta's application form made it literal — **"preferred work location" was a fixed dropdown, and Washington wasn't in it.**

### 2. The deadline had already passed the day I started

The community college fall deadline was **August 10.** I began researching on **August 23.**
These programs close **two to three months before classes start.** Check the **deadline**, not the start date.

### 3. The job title doesn't tell you the job

I mistook `Inside Wireman` for a software role — the entrance exam covers algebra and reading comprehension.
It's actually a **building electrician (SOC 47-2111)**. The algebra is for Ohm's law and voltage drop;
the reading is for the National Electrical Code.

→ **Checking the SOC code settles it.**

### 4. A posting can disappear in two days

| Checked | AWS WBLP postings |
|---|---|
| August 28 | 4 worldwide · 1 in the US (Ohio) |
| **August 30** | 3 worldwide · **0 in the US** |

The path I'd rated the strongest candidate **vanished from the US within two days.**

### 5. The search API lies

`amazon.jobs` search **intermittently returns `0` even for a perfectly valid query.**

```
technician   first try: 0 results  →  repeated: 2,352
```

**Look once, conclude "nothing there," and you miss a door that's open.**
Repeat 3–4 times with a delay, and only trust a value that stays consistent.

---

## So what happened

**Six narrowed to one.** Each for a different reason.

| # | Outcome | Why |
|---|---|---|
| ① Meta AWA | ✅ **Applied 2026-09-01** | The only path left. One document required: a resume |
| ② BBCC | 🔻 Dropped to 4th | A year without income — **not a path to near-term earnings** |
| ③ NABTU | Closed | Once ④'s structure was clear, there was no reason to examine the same category twice |
| ④ SW WA JATC | Switched to information-gathering | 8,000 hours · 5 years · starts at 40% wage |
| ⑤ AWS WBLP | 🤖 Weekly automated monitoring | Zero WA postings, three checks running |
| ⑥ Amazon Apprenticeship | ❌ Ineligible | Military community only |

> ⭐ **The ranking flipped once.** Not because I re-researched anything.
> **Writing my actual goal down in one sentence** turned the same conditions
> from advantages into disqualifiers.
> **Write down what you're actually after before comparing programs.**

**I don't know the outcome yet.** This repository is not a success story — it's **a record of looking into it and applying.**

---

## Where to start

### If this is new to you

**→ [Getting into Data Center Work](09-Public-Guide/public-guide.en.md)**
The research rebuilt in the order a first-time reader needs it. This one document may be enough.

### If you want to know what's near you

**→ [How to find out if there's a program in your region](04-US-Regional-Map/guides/find-your-region.en.md)**
A procedure that produces an answer if you follow it. 30–60 minutes.

### If you need per-program detail

**→ [Program anatomy table — 6 programs × 8 fields](02-Program-Anatomy/examples/program-anatomy.en.md)**
Operator, funder, duration, cost, employer, and application channel measured against the same yardstick.

### If you want to see the actual application materials

**→ [AWA submission sheet](08-Application-Execution/guides/awa-submission-sheet.en.md)** · **[Resume draft](08-Application-Execution/examples/awa-resume-draft.en.md)**
The real form inputs and the resume strategy behind them.

### If you want one person's actual run

**→ [My case — ten days from six programs to one](09-Public-Guide/examples/my-case.en.md)**

---

## All modules

| # | Module | Content |
|---|---|---|
| M1 | [Ecosystem and Role Map](01-Ecosystem-and-Roles/README.en.md) | Construction/operations × trades/technician 2×2. **There are four doors** |
| M2 | [Program Anatomy](02-Program-Anatomy/README.en.md) | 6 × 8 fields. Early intake-cycle scan |
| M3 | [Credentials and Apprenticeship](03-Credentials-and-Apprenticeship/README.en.md) | Registered apprenticeship / pre-apprenticeship / certificate / degree |
| M4 | [US Regional Map](04-US-Regional-Map/README.en.md) | Cluster × program matrix |
| M5 | [Washington State Deep Dive](05-WA-Deep-Dive/README.en.md) | Which doors are actually open · commute feasibility |
| M6 | [Remote and Online Pathways](06-Remote-Pathways/README.en.md) | What you can start without relocating |
| M7 | [Fit and Shortlist](07-Fit-and-Shortlist/README.en.md) | Screening criteria · narrowing candidates |
| M8 | [Application Execution](08-Application-Execution/README.en.md) | Checklist · resume · submission record |
| M9 | [Public Guide](09-Public-Guide/README.en.md) | A guide for others (KR/EN) |

---

## ⚠️ What I couldn't confirm

Recorded honestly. **Never written down as zero.**

| Item | Status |
|---|---|
| Microsoft NABTU partnership | **Not researched.** Judged to be a building-trades apprenticeship structure and deprioritized |
| Microsoft DCA's full partner college list | Claims 12 sites worldwide, but **no official full list is published** |
| TradesFutures' 34 states · etA's 20 states | Only the counts are public; no state-by-state lists |
| BBCC total tuition · remote/part-time availability | **Inquiry pending** |
| AWS WBLP's DOL registration status | Unconfirmed — determines whether the credential carries nationally |
| Starting apprentice wage percentage · physical requirements | Set individually in each program's standards. No single value exists |

---

## What this repository actually is

**The output of researching alongside AI, and documenting the process as it happened.**

This isn't the result of solo searching — **the reasoning behind each judgment was written down as it was made**,
which means **the record also shows how wrong calls got corrected.**

- An AI-inferred residency date that turned out to be an error
- A live web page carrying a dead email address, which bounced two inquiries
- An unverified "7 days left" deadline claim that did *not* get to shake the roadmap, because it was checked first

I kept those in, because they may be more useful than the research itself.

---

## 🎬 Video

This research process was also made into a video.

- 🇰🇷 Korean — https://youtu.be/DotegI2Q8fw
- 🇺🇸 English — https://youtu.be/749dpzOq09Y

**The video covers only what's needed to make a decision. The detail lives here.**

---

*Catch Up AI · Researched 2026-08-23 – 09-02*
