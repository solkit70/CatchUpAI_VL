# 2026 Spring Sprinkler Schedule

**Created**: 2026-03-15
**Status**: 🔄 Draft — actual station numbers to be filled in after outdoor practice
**System**: Rain Bird ESP-ME3 (Tehaleh, WA)

---

## Measured Area Summary

| Zone | Area | Program |
|------|------|---------|
| Front Yard | 2,265 sq ft | Program A |
| Back Yard | 6,448 sq ft | Program B |
| Mulch Beds/Flower Beds | Not measured | Program C |
| **Total Lawn** | **8,713 sq ft** | — |

---

## Spring Run Time Calculation Basis

### Basic Assumptions
- Sprinkler head type: Rotary heads (Rotor) — precipitation rate approx. **0.5 in/hour**
- Spring watering goal: **0.5 inches per week** (supplementing PNW spring rain in March–April)
- Seasonal Adjust: **70%** (early spring March basis)

### Run Time Calculation

```
Goal: 3x/week × 1 watering = 0.5 inches/week
→ Amount needed per watering = 0.5 ÷ 3 ≈ 0.17 inches

Precipitation rate 0.5 in/hour → time for 0.17 inches = approx. 20 min

Base Run Time before applying Seasonal Adjust 70%:
20 min ÷ 0.70 = approx. 28 min → round to 30 min

But actual application:
- First startup, so start conservatively: base Run Time = 10 min
- With Seasonal Adjust 70% → actual 7 min/station
- Increase Run Time after observing lawn condition in 2–3 weeks
```

> **First startup recommendation**: 10 min/station × 70% = actual 7 min. Adjust after checking lawn condition.

---

## Spring Schedule Settings (Draft)

### Program A — Front Yard Lawn (2,265 sq ft)

| Item | Setting | Notes |
|------|---------|-------|
| Start Time 1 | **5:00 AM** | Set only 1 |
| Start Times 2–6 | **OFF** | |
| Water Days | **Mon/Wed/Fri** | 3x/week |
| Seasonal Adjust | **70%** | March basis |

| Station | Run Time | Coverage Zone | Confirmed? |
|---------|---------|---------------|-----------|
| ___ | 10 min | Front Yard 1 (35.6×34 ft) | ☐ Fill in after outdoor check |
| ___ | 10 min | Front Yard 2 (37×28.5 ft) | ☐ Fill in after outdoor check |
| ___ | 10 min | (if additional station exists) | ☐ |

**Estimated Program A Total Run Time**: 2–3 stations × 10 min = **20–30 min**
→ Starts 5:00 AM → completes by 5:20–5:30 AM ✅

---

### Program B — Back Yard Lawn (6,448 sq ft)

| Item | Setting | Notes |
|------|---------|-------|
| Start Time 1 | **5:30 AM** | Starts after A completes |
| Start Times 2–6 | **OFF** | |
| Water Days | **Mon/Wed/Fri** | 3x/week |
| Seasonal Adjust | **70%** | Shared with Program A |

| Station | Run Time | Coverage Zone | Confirmed? |
|---------|---------|---------------|-----------|
| ___ | 10 min | Back Yard Zone 1 | ☐ Fill in after outdoor check |
| ___ | 10 min | Back Yard Zone 2 | ☐ |
| ___ | 10 min | Back Yard Zone 3 | ☐ |
| ___ | 10 min | Back Yard Zone 4 | ☐ |
| ___ | 10 min | (additional station) | ☐ |
| ___ | 10 min | (additional station) | ☐ |

**Estimated Program B Total Run Time**: 4–6 stations × 10 min = **40–60 min**
→ Starts 5:30 AM → completes by 6:10–6:30 AM ✅

---

### Program C — Mulch Beds/Flower Bed Drip

| Item | Setting | Notes |
|------|---------|-------|
| Start Time 1 | **7:00 AM** | |
| Water Days | **Tue/Thu** | Less than lawn |

| Station | Run Time | Coverage Zone | Confirmed? |
|---------|---------|---------------|-----------|
| ___ | 20–30 min | Drip zone | ☐ Fill in after outdoor check |

---

## Daily Watering Timeline (Spring, Mon/Wed/Fri)

```
5:00 AM ┌─────────────────────────────────────────
        │ Program A (Front Yard) starts
        │ Sequential station operation (10 min each)
        │ Estimated 2–3 stations
5:30 AM ├─────────────────────────────────────────
        │ Program A complete ✅
        │ Program B (Back Yard) starts
        │ Sequential station operation (10 min each)
        │ Estimated 4–6 stations
6:30 AM ├─────────────────────────────────────────
        │ Program B complete ✅
        │ (Sunrise 6:00–6:30 AM, March basis)
7:00 AM ├─────────────────────────────────────────
        │ Program C (Flower Beds/Drip) starts ← Tue/Thu only
        │ Drip 20–30 min
7:30 AM └─────────────────────────────────────────
          All watering complete ✅
```

---

## Seasonal Adjustment Plan

| Month | Seasonal Adjust | Water Days | Notes |
|-------|----------------|------------|-------|
| **March** | **70%** | Mon/Wed/Fri | Current |
| April | 80–90% | Mon/Wed/Fri | |
| May | 90–100% | Mon/Wed/Fri | |
| June | 100–120% | Mon–Sat | Dry season begins |
| July | 130–150% | Every other day | Peak |
| August | 140–160% | Every other day–daily | Maximum |
| September | 100–120% | Mon/Wed/Fri | |
| October | 60–80% | Tue/Thu | |
| November | OFF | — | Winter prep |

---

## Post-Outdoor-Practice Update Checklist

- [ ] Confirm actual station count → fill in numbers in tables above
- [ ] Confirm each station's coverage zone (during manual test)
- [ ] Confirm sloped front yard station → decide whether to apply Cycle+Soak
- [ ] Confirm Program A total run time → re-verify 5:30 AM Program B start buffer
- [ ] Take photo of settings after changes → `photos/spring-settings-2026.jpg`
- [ ] Confirm Seasonal Adjust 70%

---

**Related Documents**:
- [program-strategy.en.md](concepts/program-strategy.en.md) — A/B/C/D strategy
- [seasonal-adjust-guide.en.md](concepts/seasonal-adjust-guide.en.md) — Monthly Seasonal Adjust
- [current-settings-audit.en.md](current-settings-audit.en.md) — Current settings audit
- [outdoor-tasks-20260311.en.md](outdoor-tasks-20260311.en.md) — Outdoor practice checklist

**Methodology**: VibeLearn AI
**Next Update**: After outdoor practice is complete
