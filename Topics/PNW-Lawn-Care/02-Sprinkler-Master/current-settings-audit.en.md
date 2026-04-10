# ESP-ME3 Current Settings Audit

**Created**: 2026-03-11
**Last Updated**: 2026-03-15 (reflecting measured area)
**Status**: 🔄 To be filled in after outdoor practice (after completing outdoor-tasks-20260311.en.md)
**Controller Location**: _________

---

## 📏 Irrigation Plan Reference Based on Measured Area

| Zone | Area | Program | Recommended Run Time (Spring, 70%) |
|------|------|---------|-------------------------------------|
| Back Yard | **6,448 sq ft** | Program A | 10 min/station × number of stations |
| Front Yard 1 | **1,210 sq ft** | Program B | 10 min/station |
| Front Yard 2 | **1,055 sq ft** | Program B | 10 min/station |
| **Front Yard Total** | **2,265 sq ft** | — | — |
| **Total Lawn** | **8,713 sq ft** | — | — |

> **Back yard (74% of area)** is overwhelmingly larger → prioritize when distributing station count and Run Time
> Fill in the table above after confirming which zones each station covers during outdoor practice

---

## Basic Information

| Item | Current Value |
|------|--------------|
| Date/Time Accuracy | Needs verification |
| Total Station Count | Needs verification |
| Seasonal Adjust | Needs verification |
| Rain Sensor Connected | Needs verification |
| LNK WiFi Module Connected | Needs verification |

---

## Program A Current Settings (Front Yard Lawn — St. 2, 4)

| Item | Current Value | Recommended (Spring) | Change Needed? |
|------|--------------|---------------------|----------------|
| Start Time 1 | 6:00 AM | 6:00 AM | ✅ Done |
| Start Time 2 | OFF | OFF | ✅ Done |
| Water Days | 3-day cycle | Mon/Wed/Fri | 🔶 Adjustment recommended |
| Seasonal Adjust | 70% | 70% | ✅ Done |

### Program A Station Run Times

| Station | Run Time | Coverage Zone | Notes |
|---------|---------|---------------|-------|
| 1 | 10 min | Front yard right slope (Bark) | ⚠️ Needs to move to Program C |
| 2 | 10 min | Front yard right lawn | ✅ Lawn zone |
| 3 | 10 min | Front entrance (Bark/flower bed) | ⚠️ Needs to move to Program C |
| 4 | 10 min | Front yard left lawn | ✅ Lawn zone |
| 5 | 10 min | Front yard left slope (Bark) | ⚠️ Needs to move to Program C |
| 6 | 10 min | Back yard left | ⚠️ Needs to move to Program B |
| 7 | 10 min | Back yard right | ⚠️ Needs to move to Program B |
| 8 | 10 min | Back yard center | ⚠️ Needs to move to Program B |

---

## Program B Recommended Settings (Back Yard Lawn — St. 6, 7, 8)

| Item | Current Value | Recommended (Spring) | Change Needed? |
|------|--------------|---------------------|----------------|
| Start Time 1 | OFF | 6:40 AM | ⏳ Needs setup |
| Water Days | — | Mon/Wed/Fri | ⏳ Needs setup |

### Program B Station Run Times (to be set)

| Station | Run Time | Coverage Zone |
|---------|---------|---------------|
| 6 | 10 min | Back yard left |
| 7 | 10 min | Back yard right |
| 8 | 10 min | Back yard center |

---

## Program C Recommended Settings (Bark/Flower Beds — St. 1, 3, 5)

| Item | Current Value | Recommended |
|------|--------------|-------------|
| Start Time 1 | OFF | 7:30 AM |
| Water Days | — | Tue/Thu (less than lawn) |

### Program C Station Run Times (to be set)

| Station | Run Time | Coverage Zone |
|---------|---------|---------------|
| 1 | 20 min | Front yard right slope (Bark) |
| 3 | 20 min | Front entrance (Bark/flower bed) |
| 5 | 20 min | Front yard left slope (Bark) |

---

## Manual Test Results Summary (Confirmed 2026-03-30)

**Total Stations**: 8 (stations 9–22 not connected)
**Test Results**: All normal ✅

| Station | Normal? | Coverage Zone | Zone Type | Recommended Program |
|---------|---------|---------------|-----------|---------------------|
| 1 | ✅ | Front yard right slope (Bark) | Flower bed/Bark | **Program C** |
| 2 | ✅ | Front yard right lawn | Lawn | **Program A** |
| 3 | ✅ | Front entrance (Bark/flower bed) | Flower bed/Bark | **Program C** |
| 4 | ✅ | Front yard left lawn | Lawn | **Program A** |
| 5 | ✅ | Front yard left slope (Bark) | Flower bed/Bark | **Program C** |
| 6 | ✅ | Back yard left | Lawn | **Program B** |
| 7 | ✅ | Back yard right | Lawn | **Program B** |
| 8 | ✅ | Back yard center | Lawn | **Program B** |
| 9–22 | — | Not connected (NoMod) | — | — |

**Problem Stations**: None ✅

---

## Changes Needed

| Item | Current Value | Change To | Priority |
|------|--------------|-----------|----------|
| Seasonal Adjust | | 70% | High |
| Program A Start Time | | 5:00 AM | High |
| | | | |

---

## Spring Schedule Setup Completion Check

- [ ] Verify date/time accuracy
- [ ] Seasonal Adjust → set to 70%
- [ ] Program A Start Time → 5:00 AM (rest OFF)
- [ ] Program A Water Days → Mon/Wed/Fri
- [ ] Program B Start Time → 5:30 AM
- [ ] Repair/adjust problem stations
- [ ] Save settings (hold ◄▶ simultaneously for 3 seconds)
- [ ] Take photo of settings screen

---

**Next Update**: After outdoor practice is complete
**Reference**: outdoor-tasks-20260311.en.md
