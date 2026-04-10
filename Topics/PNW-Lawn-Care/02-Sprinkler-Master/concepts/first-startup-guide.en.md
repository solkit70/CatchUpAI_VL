# Sprinkler System First Startup Guide

> This document is a guide for **turning on the sprinkler system for the first time after winter**.
> Refer to this when using the system for the first time after moving in, or when restarting it in spring after keeping it OFF through winter.

**Background**: After moving into Tehaleh (WA) in October 2025, the sprinkler had not been used for 5–6 months.
This document records the procedure for operating the sprinkler for the first time in this home.

---

## Why Does the Order Matter?

The sprinkler system is connected in the order: **Water supply → Controller → Valve → Heads**.
Ignoring this order and turning on the controller first can cause:
- Potential overheating of solenoid valves without water supply
- Sudden water pressure upon restart can damage pipes and heads ("water hammer")
- Difficult to diagnose the cause when problems occur

**Always follow the order below.**

---

## Pre-Check — Review Orientation Video

First, check the orientation video received when purchasing the home.

**What to Confirm**:
- Where is the sprinkler main valve?
- How do you open and close it?
- Are there any special precautions?

> If hard to find in the video, search using keywords "irrigation," "sprinkler," or "valve"

---

## Step 1: Find the Main Water Supply Valve

### Typical Locations (for Tehaleh New Construction)

| Location | Description |
|----------|-------------|
| **Inside garage wall** | Near wall where pipes run, lever-type ball valve |
| **Utility room/laundry room** | At main water line branch point |
| **Lower exterior wall of house** | Next to or in front of backflow preventer |

### What Is a Backflow Preventer?

A metal device located low on the exterior wall of the house that prevents sprinkler water from flowing back into the household water supply.
Required by WA state law in most new home constructions.

```
[House exterior wall]
    |
[Backflow Preventer] ← Find this
    |
[Main Valve]
    |
[Underground pipes → Each station valve → Heads]
```

**Take a Photo**: Save the backflow preventer you find as `photos/backflow-preventer.jpg`

---

## Step 2: Open the Main Valve

### How to Open by Valve Type

**Lever-Type Ball Valve**:
- Lever **parallel** to pipe = Open
- Lever **perpendicular** to pipe = Closed
- Action: Turn lever in the direction of the pipe

**Handle-Type Gate Valve**:
- Turn **counterclockwise** (CCW) to open
- Turning 1/4 turn back after reaching the end is recommended (prevents sticking when fully open)

### ⚠️ Open Safely — Prevent Water Hammer

```
❌ Wrong method: Open all at once → pipe shock, connection damage risk
✅ Right method: Open 1/4 at a time slowly → if no noise, open a bit more
```

**Procedure**:
1. Confirm current valve position (if closed, identify the direction to open)
2. Turn 1/4 at a time slowly
3. Wait 10 seconds → listen for sounds (no banging, hissing, or dripping is normal)
4. Turn another 1/4 → repeat
5. Wait 1 minute after fully open
6. Visually inspect area around valve and pipe connections for leaks

---

## Step 3: Check Controller Status (Indoors)

### Power Check
1. Confirm ESP-ME3 plug is inserted
2. Check if LCD screen turns on
3. Confirm no `NO AC` message (if present, there is a power issue)

### Check and Correct Date/Time
```
Dial → SET Date/Time
▲▼ buttons to adjust → move to next item
```
- If power was disconnected during winter, date/time may have reset
- Built-in lithium battery maintains for ~10 years → should be correct if normal

### Check Existing Programs
Dial → RUN TIMES → Check Program A/B/C/D
→ If times are set incorrectly, correct them later

### Switch to AUTO Mode
- Dial → **AUTO** (or RUN) position
- ⚠️ If Start Times are programmed, water may start flowing → OK if early morning, be cautious if evening

---

## Step 4: First Manual Test (Outdoors)

Before running all stations at once, **test just one station first**.

```
Dial → MANUAL WATERING → Test By Station
Station 1 → Set 2 minutes → ▶ button
```

**What to Check Outdoors**:
- [ ] Does the head pop up?
- [ ] Is water spraying/rotating normally?
- [ ] No water leaking around the head?
- [ ] No ground heaving or pooling around pipe path?

**If first test is normal** → Proceed to Tasks 1–4 in `outdoor-tasks-20260311.en.md`

---

## Step 5: Troubleshooting If Issues Arise

### When No Water Comes Out
1. Is the main valve fully open? → Check again
2. Is there an error message on the controller LCD?
3. Is there a lock or closed lever on the backflow preventer?
4. Is the main water supply working normally? → Check indoor faucet

### When Water Leaks Around Heads
- Possible O-ring damage at head connection → Note that station, continue with the rest
- Rain Bird compatible replacement heads available at Home Depot/Lowe's

### When Pipes Sound Like Water Running But Head Won't Pop Up
- Head clogged (debris) → Clean or replace head

### When Controller LED Blinks Red
- Programming error or Flow Sensor alarm → Read scrolling LCD message
- If short circuit detected: Check wiring for that station

---

## Normal Operation Verification Checklist

```
□ Home orientation video reviewed
□ Main valve located + photo taken
□ Backflow preventer located + photo taken
□ Main valve slowly opened (no leaks)
□ Controller power ON + date/time confirmed correct
□ Station 1 manual test for 2 min → confirmed normal
□ Ready to begin full station manual test
```

---

## Reference: End of Season (Winter Preparation)

In fall, perform the reverse procedure:
1. Controller dial → OFF
2. Close main valve
3. Blow-out (use compressed air to remove water from pipes) → professional service recommended ($80–150)
4. Wrap insulation around backflow preventer (not mandatory for PNW but recommended)

> Tehaleh is at higher elevation and can have cold winters (below -4°C). Blow-out is recommended.

---

**Related Documents**:
- [outdoor-tasks-20260311.en.md](../outdoor-tasks-20260311.en.md) — Task 0 detailed checklist
- [esp-me3-complete-guide.md](../../vl_materials/esp-me3-complete-guide.md) — Full controller manual

**Created**: 2026-03-12
**Methodology**: VibeLearn AI
