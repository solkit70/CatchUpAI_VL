# ESP-ME3 Program Separation Strategy (A/B/C/D)

**Created**: 2026-03-11
**Application**: Tehaleh WA — My Lawn

---

## Why Separate Programs?

Lawn and flower beds have different water requirements. Putting everything in one program causes:
- Lawn may be underwatered while flower beds are overwatered
- When using Seasonal Adjust, all zones change by the same percentage

→ **Separate programs by plant type** = optimal watering per zone

---

## My Lawn Program Assignment Strategy

### Program A — Front Yard Lawn

| Item | Setting |
|------|---------|
| Start Time | 5:00 AM (one only) |
| Water Days | Mon/Wed/Fri (spring basis) |
| Run Time | 10–15 min per station |
| Seasonal Adjust | Spring 70% → Summer 140% |

**Feature**: Early morning watering → minimizes evaporation, prevents fungal disease

---

### Program B — Back Yard Lawn

| Item | Setting |
|------|---------|
| Start Time | 5:30 AM (one only) |
| Water Days | Mon/Wed/Fri (spring basis) |
| Run Time | 10–15 min per station |
| Seasonal Adjust | Spring 70% → Summer 130% |

**Feature**: Starts immediately after A completes → distributes water pressure

> ⚠️ Running front and back simultaneously reduces water pressure and decreases coverage

---

### Program C — Mulch Beds / Flower Bed Drip

| Item | Setting |
|------|---------|
| Start Time | 7:00 AM (one only) |
| Water Days | Tue/Thu (less than lawn) |
| Run Time | 20–30 min for drip zones |
| Seasonal Adjust | Adjusted separately from lawn |

**Feature**: Drip irrigation needs slow, extended watering → must be separated from lawn

---

### Program D — Spare / Manual Testing

| Item | Setting |
|------|---------|
| Purpose | Temporary zones, testing |
| Normally | OFF |

---

## Start Time Spacing Design

```
5:00 AM  → Program A (Front Yard Lawn) starts
           ↓ (auto after A completes)
5:30 AM  → Program B (Back Yard Lawn) starts
           ↓
7:00 AM  → Program C (Flower Bed/Drip) starts
           ↓ complete
All watering complete before sunrise ✅
```

---

## Program A/B Detail — Spring Schedule Design

### Spring (March–April) Water Requirements
- Goal: 0.5 inches per week (March, PNW rain supplement)
- Sprinkler precipitation rate: approx. 0.5 in/hour (rotary heads)
- → **2–3x/week, 6–10 min per zone** (adjust after confirming precipitation rate)

### Current Recommended Spring Settings

| Setting | Value |
|---------|-------|
| Water Days | Mon/Wed/Fri (3x/week) |
| Run Time | 10 min per zone (spring basis) |
| Seasonal Adjust | 70% |
| Start Time | 5:00 AM |

> Adjust after confirming actual station count and locations (after outdoor practice)

---

## Common Mistakes & Solutions

| Mistake | Cause | Solution |
|---------|-------|----------|
| Water runs multiple times a day | Multiple Start Times set | Leave only one, turn rest OFF |
| Specific zone doesn't water | Run Time = 0 min | Reset time for that station |
| Front and back running simultaneously | A/B set to same Start Time | Stagger A→B in sequence |
| Flower bed waters too frequently | In same program as A | Separate to Program C |

---

## Program Verification Based on Measured Area (2026-03-15)

| Program | Zone | Measured Area | Estimated Station Count | Estimated Total Run Time |
|---------|------|--------------|------------------------|--------------------------|
| A | Front Yard | **2,265 sq ft** | 2–3 stations | 20–30 min |
| B | Back Yard | **6,448 sq ft** | 4–6 stations | 40–60 min |
| C | Mulch Beds | Need separate measurement | 1–2 stations | 20–40 min |

### Start Time Spacing Verification

```
5:00 AM → Program A starts (Front Yard 2,265 sq ft)
           ↓ max 30 min (3 stations × 10 min)
5:30 AM → Program B can start ✅ (immediately after A ends)
           ↓ max 60 min (6 stations × 10 min)
6:30 AM → Program B completes (around sunrise)
7:00 AM → Program C starts (Mulch Beds)
```

> Back yard is **2.8x** the front yard area → likely proportionally more stations
> Confirm actual station count during outdoor practice, then adjust B's start time if needed

**Reference**: esp-me3-complete-guide.md
**Next Step**: Fill in this table after confirming actual stations outdoors
