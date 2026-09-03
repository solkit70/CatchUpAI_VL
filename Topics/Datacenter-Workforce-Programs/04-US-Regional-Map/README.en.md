<!-- lang-switch -->
[🇰🇷 한국어](README.md) · 🇺🇸 **English**
<!-- lang-switch -->

# M4 — US Regional Map

**Duration**: 2026-08-30 (1 day)
**Prerequisites**: [M2 Program Anatomy](../02-Program-Anatomy/README.en.md) · [M5 WA Deep Dive](../05-WA-Deep-Dive/README.en.md)
**Purpose**: **For community reference.** Looks at the whole US regardless of my own
eligibility (a roadmap-defined side thread)

## What this module did

Cataloged US data center clusters and built a matrix of where each of the 6
programs is actually open. The deliverable is **a procedure anyone else can use
to find their own region** ([find-your-region.en.md](guides/find-your-region.en.md)).

If M1–M3·M5 asked "where can I go," M4 asks **"what do I tell someone else who asks?"**

## Deliverables

| File | Content |
|---|---|
| [examples/us-dc-clusters.en.md](examples/us-dc-clusters.en.md) | Cluster list — operators, construction/operations phase |
| [examples/cluster-program-matrix.en.md](examples/cluster-program-matrix.en.md) | Cluster × 6-program matrix + interpretation of gaps |
| [guides/find-your-region.en.md](guides/find-your-region.en.md) | **The key deliverable.** A procedure anyone can follow to an answer |

## 4 things confirmed

### ① Programs are location-bound in different ways

The six don't tie to geography the same way. Without separating these, a "✓" in
the matrix means something different in every cell.

| Type | Program | What a "✓" means |
|---|---|---|
| **Named city** | ① Meta AWA | Eligible if you live in that city |
| **Named college** | ② MS Datacenter Academy | Eligible if you can attend that school |
| **Regional network** | ③ NABTU · ④ Google/etA | **"Ask your local"** — not the same as "open" |
| **Job posting** | ⑤-a AWS WBLP | Exists only while a posting is live |
| **National online** | ⑥ AWS Apprenticeship | Apply from anywhere (military-focused) |

### ② ① and ② share no overlapping locations at all

| ① Meta AWA (construction trades) | ② MS DCA (operations technician) |
|---|---|
| Houston · Columbus · Indianapolis · Baton Rouge | Phoenix · Des Moines · central Washington |

This looks like more than coincidence — it's a **difference in character.**
M1's 2×2 (construction/operations × trades/technician) **reappears as a
geographic pattern.**

### ③ The 3 largest US markets have no dedicated program

**Northern Virginia, Atlanta, Dallas** — neither ① nor ② is present. Three
hypotheses:

- **A. The labor market is already established, so a new pipeline is less
  urgent** — programs appear where labor is scarce
- **B. Mature markets are operations-focused, so the needed roles differ** —
  operations technicians are hired through job postings, not training programs
- **C. A measurement problem — it exists but wasn't found** — ②'s full partner
  college list isn't public

**C couldn't be ruled out, so the matrix marks those cells `❓` rather than `❌`.**
"It doesn't exist" and "I couldn't find it" are different claims.

### ④ ⑤-a AWS WBLP **disappeared from the US in two days**

This was the path M2 flagged as "the best-fit candidate for this topic."

| Research date | Result |
|---|---|
| M5 (2026-08-28) | 4 worldwide · **1 in the US** (Ohio) |
| **M4 (2026-08-30)** | **3 worldwide · 0 in the US** (Tokyo, Sweden, Germany) |

→ [Correction reflected in M5's deliverable](../05-WA-Deep-Dive/examples/wa-institutions.en.md)

## Methodology — the most important finding of this module

The `amazon.jobs` search API **intermittently returns `hits=0` even for a
perfectly valid query.**

```
learning     first try: 0 results  →  shortly after: 7,023
technician   first try: 0 results  →  repeated: 2,352
```

Query once, get 0, and it reads as **"no postings exist."** In reality it's
"couldn't be read."

**Attaching a control query in the same batch wasn't enough** — the target query
returned 0 even while the control returned 10,000 results in the same batch.
Each request fails independently.

**The right approach is to repeat 4 times with a delay between attempts and
judge by consistency.**

| Query | Result across 4 tries | Verdict |
|---|---|---|
| `technician` | 2,352 ×4 | Stable |
| `data center technician` | 1,334 ×4 | Stable |
| `work-based learning` | **3 ×4** | **A stable 3** |

The state-by-state distribution for `data center technician` **never returned a
response even after 6 retries, so it's recorded as `unconfirmed`,** not as 0.

> **M5's check was also a single query.** The "4 results" it got was correct only
> by chance — the same trap could have been triggered there too.

## DoD

- [x] Catalog 5+ clusters (with operator, construction/operations phase) — **top 5 by
      colocation + top 5 by state-level capacity + 6 by program relevance**
- [x] Complete the cluster × program matrix — 11 clusters × 6 programs
- [x] Interpret at least 1 region with a program gap — Northern Virginia, 3 hypotheses
- [x] `find-your-region.en.md` — a procedure anyone else can follow directly
- [x] README written
- [x] WorkLog written

## What was left as "unconfirmed"

Not recorded as zero.

- ② MS DCA's **full partner list** — claims 12 sites worldwide, no official list
  published. 4 confirmed in the US
- ③ TradesFutures' **specific list of 34 states** — only the count is published
- ④ etA's **list of 20 states** — same reason
- AWS `data center technician` **state-by-state US distribution** — API never
  responded
- ① Meta AWA's **expansion plan beyond the 4 pilot cities** — the phrase "first
  launch" suggests expansion is planned, but no timeline is public

## Next

- **M6 Remote/Online Pathways** — directly targets the only obstacle
  (relocation/no income) blocking the one door that's actually open right now (BBCC)
- 🔴 **Contact BBCC** — user to do this directly. M6 adds "is it possible remotely"
  to the question list
- 2 alerts to set — PSEJATC reopening · Amazon WBLP US postings reopening
