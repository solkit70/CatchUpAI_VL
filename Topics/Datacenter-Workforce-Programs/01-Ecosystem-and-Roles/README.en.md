<!-- lang-switch -->
[🇰🇷 한국어](README.md) · 🇺🇸 **English**
<!-- lang-switch -->

# M1 — Data Center Workforce Ecosystem and Role Map

**Status**: Complete · DoD 7/7
**Estimated time**: 3h
**Difficulty**: ⭐

This module builds the **coordinate system** that every later investigation sits on.
Once you can ask "which cell does this belong in?" for any program, it becomes clear
where the six programs cluster and where the gaps are.

---

## Reading order

1. [concepts/role-map.md](concepts/role-map.md)
   — **Read this first.** A 2×2 map of Construction/Operations × Trades/Technician,
   with per-role detail including pay and entry requirements
2. [concepts/employment-structure.md](concepts/employment-structure.md)
   — Who actually employs you. Four common misconceptions
3. [examples/program-to-role-matrix.md](examples/program-to-role-matrix.md)
   — The six programs placed on the map, with interpretation

---

## What this module found

| # | Finding | Impact |
|---|---|---|
| 1 | **"Completing a Big Tech program" ≠ "becoming a Big Tech employee"** | 4 of 6 programs target construction-phase trades, and the employer there is a partner construction company |
| 2 | **The lowest-barrier door is on the technician side** — Data Center Technician entry is a high school diploma + on-the-job training, $60–90k | The opposite of the common assumption that "technician = degree required." Could be decisive in M7 |
| 3 | **The two tracks are not walled off from each other** — Critical Facilities Engineer can be entered via apprenticeship too | Treating M7 as "pick one or the other" misses this bridge |
| 4 | **Pay ranges overlap** — skilled construction trades reach "six figures," while Operations CFE runs $93–155k | Track choice is not simply an income ranking |
| 5 | **Construction × Technician is empty** (0 of 6 programs) | There are no servers while the building is under construction — appears to be a structural gap |
| 6 | **Larger data centers need fewer workers per MW** — 8–12/MW for small facilities vs. 1–2/MW for hyperscale campuses | A baseline for reading regional economic-impact claims |
| 7 | **⑤ Amazon TWD straddles two cells** | Likely a family of separate sub-tracks under one umbrella brand → needs to be broken apart in M2 |

---

## Definition of Done

- [x] 2×2 role map complete (all four cells — one deliberately left empty, with reasoning, as a "structural gap")
- [x] Employer noted for each role (construction: GC/subcontractor/staffing agency; operations: badged direct employment)
- [x] All 6 programs placed on the map (⑤ recorded as straddling two cells)
- [x] Documented why "completing a program" ≠ "getting hired by Big Tech"
- [x] README written (reading order + links + one-line summary)
- [x] WorkLog completed
- [x] Daily retrospective written

---

## Self-Assessment

**Concept understanding**

- [x] Can explain in 1–2 sentences why construction-phase and operations-phase roles differ
  → During construction you need people who *install* electrical, plumbing, and cooling
    infrastructure; after go-live you need people who *maintain* it and handle servers.
    Servers arrive only after the building is finished.

- [x] Can answer "who employs you after completing the Meta program?"
  → Not Meta — a **partner construction company**. Meta provides the training;
    a GC or subcontractor does the hiring.

**Practical application**

- [x] Can immediately place a newly found program on the role map
  → Look at the target roles and ask ① the time axis (building vs. maintaining) and
    ② the role axis (license/apprenticeship vs. certification/experience) — the cell follows.
    A program that straddles cells, like ⑤, is a signal to break it into sub-tracks.

---

## Handing off to the next module

Open items are listed at the end of each document. In summary:

- Break ⑤ Amazon TWD into its sub-tracks
- Confirm the **post-completion employer** for each of the 6 programs from official pages
- ④ Google.org's actual application channel (Google itself, or a training provider?)
- Primary source for the Uptime Institute per-MW staffing figures
- Once more programs are gathered, re-check whether the "Construction × Technician" gap still holds
- The share of welders/ironworkers (trade lists differ across sources)

---

## References

- [Tradesmen International — The Skilled Trades Behind Data Center Construction](https://www.tradesmeninternational.com/news-events/the-skilled-trades-behind-data-center-construction-and-how-to-staff-them/)
  — The 5 construction trades and their roles (source of direct quotes)
- [Built In — Data Center Jobs: Pay, Roles and What to Expect](https://builtin.com/articles/data-center-jobs)
  — Pay and entry requirements for the 3 operations roles
- [[Roundup/2026-08-19 - Daily Roundup#새로 생긴 학습 주제 두 가지]] — the baseline table of 6 programs
- [../vl_materials/00-baseline-programs.md](../vl_materials/00-baseline-programs.md) — copy of baseline material and context

---

← Previous: (none — first module)
→ Next: M2 — Anatomy of the 6 programs + early intake-cycle scan (`02-Program-Anatomy/`)
