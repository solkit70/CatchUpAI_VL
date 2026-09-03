<!-- lang-switch -->
[🇰🇷 한국어](cluster-program-matrix.md) · 🇺🇸 **English**
<!-- lang-switch -->

# Cluster × Program Matrix

**Researched**: 2026-08-30 (M4, exercise 2)
**Question**: *"What's available in my area?"*

## The 6 programs — different kinds of location-boundedness

Before drawing the matrix, one thing has to be understood: **the six don't tie
to geography the same way.**

| #   | Program                      | Type of location-boundedness              |
| --- | ----------------------------- | ------------------------------------ |
| ①   | Meta AWA                     | **Named cities only** — the 4 pilot cities             |
| ②   | MS Datacenter Academy        | **Named colleges** — where a partner community college is located |
| ③   | MS × NABTU                   | **Regional network** — TradesFutures, 34 states    |
| ④   | Google.org / etA             | **Regional network** — IBEW/NECA regional training centers, 20+ states |
| ⑤-a | AWS WBLP                     | **Wherever a posting exists** — it exists only while a posting is live |
| ⑥   | AWS Technical Apprenticeship | **National online application** (military-focused)              |

**Only ② is "a school you attend." ① names specific cities, ③④ are
organization-based, and ⑤ is a job posting.** Because of this, "✓" means
something different in every cell even inside the same table.

## The matrix

**Legend**: ✅ Confirmed open · ⭕ Falls within a regional network's footprint
(check the local) · ❌ Not applicable · ❓ Unconfirmed

| Cluster | ① Meta AWA | ② MS DCA | ③ NABTU | ④ Google/etA | ⑤-a AWS WBLP | ⑥ AWS Apprenticeship |
|---|---|---|---|---|---|---|
| **N. Virginia** | ❌ | ❓ | ⭕ | ⭕ | **❌ 0 postings** | ⭕ military |
| **Atlanta** (GA) | ❌ | ❓ | ⭕ | ⭕ | ❌ | ⭕ |
| **Dallas–Fort Worth** (TX) | ❌ | ❓ | ⭕ | ⭕ | ❌ | ⭕ |
| **Houston** (TX) | ✅ **pilot** | ❓ | ⭕ | ⭕ | ❌ | ⭕ |
| **Phoenix** (AZ) | ❌ | ✅ **Estrella Mountain CC · Glendale CC** | ⭕ | ⭕ | ❌ | ⭕ |
| **Chicago** (IL) | ❌ | ❓ | ⭕ | ⭕ | ❌ | ⭕ |
| **Columbus** (OH) | ✅ **pilot** | ❓ | ⭕ | ⭕ | ❌ | ⭕ |
| **Indianapolis** (IN) | ✅ **pilot** | ❓ | ⭕ | ⭕ | ❌ | ⭕ |
| **Baton Rouge** (LA) | ✅ **pilot** | ❓ | ⭕ | ⭕ | ❌ | ⭕ |
| **Des Moines** (IA) | ❌ | ✅ **DMACC West** | ⭕ | ⭕ | ❌ | ⭕ |
| **Central Washington** (Quincy, Moses Lake) | ❌ | ✅ **Big Bend CC** | ⭕ | ⭕ | ❌ | ⭕ |

## How to read this — what the table actually says

### 1. ⑤-a AWS WBLP is **0 for the entire US** as of today

M5 (8/28) found *"4 worldwide / 1 in the US, in Ohio."* **Checking again today
(8/30) finds 3, all overseas.**

| Posting | Location | Posted |
|---|---|---|
| Data Center Operations Trainee - WBLP | **Tokyo, Japan** | 2026-07-13 |
| Data Center Logistics Specialist Trainee | **Västerås, Sweden** | 2026-07-02 |
| Logistics Specialist Trainee, Data Center Communities | **Frankfurt, Germany** | 2026-01-15 |

**The US postings closed within two days.** This is the path M2 flagged as "the
best-fit candidate for this topic."

> ⚠️ Search-result pages still show Virginia (Sterling, Herndon, Manassas,
> Chantilly) WBLP postings. **Every one is an undated aggregator cache** and
> none appear in the live API's full results. **What's on screen and what you
> can actually apply to right now are different things.**

### 2. ① and ② don't overlap in location

There is **zero overlap** between Meta AWA's 4 pilot cities (Houston, Columbus,
Indianapolis, Baton Rouge) and MS DCA's sites (Phoenix, Des Moines, central
Washington).

This looks more like a difference in character than coincidence —
**① is construction trades** (guarantees Meta construction-site employment on
completion) and **② is operations technician** (IT networking, DC technician).
M1's 2×2 reproduces itself as a geographic pattern.

### 3. The top 3 markets by capacity have no "go and attend" program

**Northern Virginia, Atlanta, Dallas** — the three biggest US markets, and
neither ① nor ② is present. This cell is the most striking gap in the matrix.

## Interpreting the program gap — why nothing is in Northern Virginia

It's the largest US market and presumably has the highest labor demand, yet no
dedicated program exists there. Three hypotheses:

**Hypothesis A — the labor market is already established, so a new pipeline is
less urgent.** As a market that's been maturing for 20+ years, an experienced
labor pool, existing training institutions, and staffing pipelines are already
in place. Programs appear **where labor is scarce.** This is consistent with
Meta choosing new-entry sites like Baton Rouge and Indianapolis.

**Hypothesis B — mature markets are operations-focused, so different roles are
needed.** ① is a construction-trades program. Northern Virginia does have
expansion, but not at Atlanta's share of new construction. What's needed there
is operations technicians, and **those get hired through job postings (⑤), not
training programs.**

**Hypothesis C — a measurement problem; it exists but wasn't found.** ②'s
partner-college list isn't public (claims 12 sites worldwide, 40+ institutions).
Even if a Northern Virginia community college (e.g., NOVA) has a similar
program, it wouldn't show up in this research unless it carries the
"Datacenter Academy" brand.

> **C has to be ruled out before A or B can be claimed.** Since it hasn't been,
> the ② cell for Northern Virginia is marked **`❓`**, not `❌`.

## Why ③④ are almost entirely ⭕ across the table — and why that's a trap

TradesFutures covers **34 states**, and Google.org/etA covers **20+ states.**
Nearly every cluster falls within range.

**But that ⭕ does not mean "you can apply."**

- ③ TradesFutures is **apprenticeship-readiness** (MC3 training), not the
  apprenticeship itself. The actual game is **selection by the local union**,
  which opens and closes on its own separate schedule
- ④ Google.org **funds** things. The actual intake is run by IBEW/NECA regional
  training centers

M5 confirmed exactly this trap in the real world — **Washington's Puget Sound
Electrical JATC (PSEJATC) stopped accepting new applications as of May 1,
2026,** with no reopening date set. At the state level it reads "⭕, included
in the 34," but in practice the door was closed.

> **A ⭕ for a regional-network program means "ask your local," not "it's open."**

## What was left as "unconfirmed"

Recorded honestly. Not counted as zero.

- **② MS DCA's full partner list** — no full list on the official page. Beyond
  the 4 confirmed US sites (Big Bend, DMACC, Estrella Mountain, Glendale), more
  likely exist (claims 12 sites worldwide)
- **③ TradesFutures' specific list of 34 states** — only the count is public;
  no state-by-state list
- **④ etA's list of 20 states** — same reason
- **AWS `data center technician` state-by-state US distribution** — the API
  never responded even after 6 retries. **Unconfirmed, not zero**
- **① Meta AWA's expansion plan beyond the 4 pilot cities** — the phrase "first
  launch" suggests expansion is planned, but no timeline is public

## References

- [Meta launches program to train workers for data center jobs — CBS News](https://www.cbsnews.com/news/meta-data-center-workforce-academy-training/)
- [Columbus named one of four cities to host Meta workforce academy](https://www.10tv.com/article/news/local/columbus-chosen-to-host-meta-workforce-academy/530-5735cfe6-d875-4ffc-aa7a-4b2e62604e6f)
- [Microsoft Datacenter Academy — Big Bend CC](https://local.microsoft.com/blog/big-bend-community-college-cultivates-a-hometown-tech-workforce/)
- [Microsoft Datacenter Academy — West Valley Phoenix](https://local.microsoft.com/blog/microsoft-datacenter-academy-in-the-west-valley-phoenix-az/)
- [DMACC West Campus Microsoft Datacenter Academy](https://www.dmacc.edu/west/microsoft-data-center.html)
- [NABTU × Microsoft expansion announcement (2026-04-21)](https://nabtu.org/press_releases/nabtu-and-microsoft-expand-nationwide-initiative-to-strengthen-ai-training-and-career-pathways-across-the-skilled-trades/)
- [NECA / Google.org etA support (2026-06-12)](https://www.necanet.org/news-media/detail/press-releases/2026/06/12/neca-applauds-google.org-for-support-of-the-electrical-training-alliance-and-skilled-trades-growth)
- `amazon.jobs` search API full query (2026-08-30, confirmed consistent across 4 repeated tries)
