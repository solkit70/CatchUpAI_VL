# Advanced Cycles (Cycle+Soak) Guide

**Created**: 2026-03-11
**Application**: Tehaleh WA — sloped front yard zones

---

## What Are Advanced Cycles?

One long watering session → split into multiple short sessions.

```
Traditional:  [====30 min====]
Advanced:     [=10 min=] wait 15 min [=10 min=] wait 15 min [=10 min=]
              (Cycle 1)              (Cycle 2)              (Cycle 3)
```

---

## Why Is It Needed?

| Problem | When It Occurs | Solution |
|---------|---------------|----------|
| Runoff on slopes | Gently sloped front yards | Cycle+Soak |
| Clay soil absorbs slowly | Compacted soil of new developments | Cycle+Soak |
| Puddles form | Large volume watering in short time | Cycle+Soak |

**Tehaleh New Construction Characteristics**: Construction compacted soil + front yard slope → Cycle+Soak strongly recommended

---

## How to Set It Up

> ### ⚠️ Important: Cycle+Soak Cannot Be Set on the Controller Itself
>
> The ESP-ME3 controller dial does not have a Cycle+Soak option.
> You can only use it with **Rain Bird App (iOS/Android) + LNK2 WiFi Module**.

### Setup via App (After Connecting LNK2 Module)

```
1. Open Rain Bird App on iPhone/Android
2. Select your connected ESP-ME3 controller
3. Zones tab → Select the zone
4. Advanced Settings → Enable Cycle+Soak
5. Enter Cycle Time (minutes per watering session, e.g., 10 min)
6. Enter Soak Time (absorption wait time, e.g., 15 min)
7. Save → Automatically applied to controller
```

### What If You Don't Have the LNK2 WiFi Module? (Manual Alternative)

Set **2 Start Times** within the same program for a similar effect:
```
Program A Start Time 1: 5:00 AM (Run Time 10 min)
Program A Start Time 2: 5:30 AM (Run Time 10 min)
→ 2 waterings 30 minutes apart = manual Cycle+Soak effect
```
ESP-ME3 supports up to 6 Start Times per program — this method achieves the same result without LNK2.

---

## Recommended Settings for Tehaleh Front Yard

| Item | Value |
|------|-------|
| Cycle watering time | 10 min |
| Number of cycles | 3 |
| Soak (absorption wait) time | 15 min |
| Total time needed | 10×3 + 15×2 = **60 min** |

> ⏰ Allow for total time when setting Start Time
> Program A starts at 5:00 AM → completes by 6:00 AM

---

## Which Zones Should Use This?

| Zone | Advanced Cycles Needed? | Reason |
|------|------------------------|--------|
| Front yard grass (slope) | ✅ **Recommended** | Gentle slope → runoff risk |
| Back yard grass (flat) | Optional | Flat but new construction soil compaction |
| Mulch bed drip | ❌ Not needed | Drip already absorbs slowly |

---

## Before vs. After Comparison

**Before**:
- Water runs downhill on sloped front yard
- Runoff to road/sidewalk
- Grass receives water unevenly

**After**:
- 10 min watering → soil absorbs water
- 15 min wait → full absorption
- 10 min again → deeper penetration
- Result: Even and deep watering

---

## What to Check During Outdoor Practice

- [ ] Identify which station covers the sloped area of the front yard
- [ ] Observe if runoff problem currently exists (during manual test)
- [ ] If runoff confirmed, apply Cycle+Soak to that station

---

**Reference**: esp-me3-complete-guide.md
**Applies to**: Front yard sloped area station (enter number after outdoor confirmation)
