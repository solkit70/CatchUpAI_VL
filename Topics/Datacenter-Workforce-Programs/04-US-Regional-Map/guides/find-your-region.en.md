<!-- lang-switch -->
[🇰🇷 한국어](find-your-region.md) · 🇺🇸 **English**
<!-- lang-switch -->

# How to Find a Data-Center Workforce Program in Your Area

**Prepared**: 2026-08-30 (M4)  
**For**: Anyone in the United States—no major or prior experience required  
**Time**: 30–60 minutes

Follow this document and you will get an answer. “None” is also an answer, because it changes what you should do next.

## Before you begin—separate the two paths

**“Data-center jobs” mean different things in different regions.**

| | Construction skilled trades | Operations technical roles |
|---|---|---|
| Work | Electrical, plumbing, HVAC, welding—**build** the site | Server and network work—**run** the site |
| When needed | While a new site is under construction | After the site begins operation |
| Entry door | Union apprenticeship (4–5 years, **paid while training**) | Job posting or certificate program |
| Physical demand | High | Moderate (shift work; lift about 18 kg/40 lb) |

**There are no servers while a data center is being built.** News that a facility is coming to town does not tell you which jobs will appear. Ask first: **Is the data center being built, or is it already operating?**

## Step 1—Check whether you are in a cluster (10 minutes)

Use the [cluster list](../examples/us-dc-clusters.en.md) to see whether a location is within 50 miles of where you live. It is fine if it is not: the broad programs in Step 3 may still apply.

## Step 2—Check the two designated programs (15 minutes)

These exist only in particular cities or colleges. If one applies, it is the most direct path.

### 1. Meta America’s Workforce Academy—construction skilled trades

**Four pilot cities**: Houston, TX; Columbus, OH; Indianapolis, IN; and Baton Rouge, LA.

| | |
|---|---|
| Cost | **Free** |
| Support | Scholarship plus **transportation, housing, and living-expense support** |
| After completion | **Guaranteed employment at a Meta data-center construction site** |
| For | Veterans, career changers, and people entering skilled trades |

Search: `Meta America's Workforce Academy apply`.

### 2. Microsoft Datacenter Academy—operations technical roles

**Confirmed U.S. locations**

| College | Location |
|---|---|
| Big Bend Community College | Moses Lake, WA |
| Des Moines Area Community College (West) | Des Moines, IA |
| Estrella Mountain Community College | Phoenix (West Valley), AZ |
| Glendale Community College | Phoenix (West Valley), AZ |

> ⚠️ **This is not a complete list.** The program reportedly exists in twelve locations worldwide, but no official complete list is public. Ask a nearby community college directly: “Do you offer a Datacenter Academy or data-center technician program?”

Microsoft scholarships may cover tuition, books, and exam fees. Confirm this with the school.

## Step 3—Check the two broad networks (15 minutes)

These may apply in many states, but this is the trap.

### 3. TradesFutures (NABTU × Microsoft)—34 states

An MC3 pre-apprenticeship program for construction unions.

### 4. Google.org × electrical training ALLIANCE—20+ states

Funds IBEW/NECA electrical-apprenticeship training.

> ### ⚠️ What you must understand here
>
> Programs 3 and 4 are **networks and funding, not a single enrollment program.** The entity that actually takes applicants is the local union apprenticeship committee (JATC), and its door opens and closes separately.
>
> For example, Puget Sound Electrical JATC stopped accepting new applications on 2026-05-01, with no reopening date. Washington is “covered” at the state level, but the real local door was closed.

Search `IBEW local [your city] apprenticeship` and call the local directly. Enrollment status often is not shown on the website.

## Step 4—Check AWS postings (10 minutes)

The AWS **Work-Based Learning Program** is an uncommon route into data-center technical work without a degree or experience (twelve paid months followed by direct employment). It exists only when a posting is live.

As of 2026-08-30, there were **zero U.S. postings**; the three worldwide postings were in Tokyo, Sweden, and Germany.

### How to check—do not trust the rendered page

`amazon.jobs` is rendered with JavaScript, and Google often shows undated cached listings. Enter this directly in a browser address bar to retrieve the live JSON list:

```
https://www.amazon.jobs/search.json?base_query=work-based+learning&result_limit=50&sort=recent
```

> ### ⚠️ If you get `0`, check again
>
> This API intermittently returns zero for valid queries. Repeat the check 3–4 times with time between requests and trust it only when the result is consistent.

AWS Technical Apprenticeship also exists, but is for veterans and has no current data-center technician track.

## Step 5—If nothing is available (10 minutes)

This is common. Even Northern Virginia, Atlanta, and Dallas may not have either designated program.

1. **A nearby community college**—search `[your area] community college data center technician certificate`.
2. **A local IBEW office**—ask when apprenticeship intake will reopen and leave your contact information for an alert.
3. **Your state apprenticeship office**—search `[state] registered apprenticeship` (Washington: WSATC).
4. Earn credentials you can start remotely while waiting—[Start Remotely Now](../../06-Remote-Pathways/guides/start-now-remotely.en.md).

## Easy-to-miss decision points

**“Exists,” “has a cohort this year,” and “is accepting applications now” are three different things.**

Distance can work in the opposite direction from what you expect. In Washington, training was far away (180 miles) while employment was close (20–25 miles). Assess the training period and the post-training job separately.

**An apprenticeship is a job, not school.** Registered apprentices earn wages while training; that difference from an unpaid certificate program changes the entire financial plan.

## Summary checklist

- [ ] Is my area a cluster, and is it being built or operating?
- [ ] Do I want construction skilled trades or operations technical work?
- [ ] Am I in one of Meta AWA’s four pilot cities?
- [ ] Does a nearby community college offer a data-center course? (**Call directly.**)
- [ ] Is the local IBEW apprenticeship accepting applications **now**? (**Call directly.**)
- [ ] Is an AWS WBLP posting live? (**Check the API 3–4 times.**)
- [ ] If not: register for alerts and begin remote prerequisite credentials.

**Limit of this document**: This research is current as of 2026-08-30. Job postings and apprenticeship intake change weekly. Program existence may persist, but always recheck whether the door is open.
