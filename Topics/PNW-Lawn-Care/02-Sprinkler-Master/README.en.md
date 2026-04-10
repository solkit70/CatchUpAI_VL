# M2: Rain Bird ESP-ME3 Master

**Module**: M2 / 4
**Status**: 🔄 In Progress (started 2026-03-11)
**Location**: Tehaleh, WA
**Total Study Time**: ~8h estimated (includes outdoor practice)

---

## What You'll Learn in This Module

Fully understand the ESP-ME3 controller and set the optimal spring schedule for your lawn.

### Lesson 1: Programs A and B must NOT run at the same time
Running front and back yard simultaneously drops water pressure and reduces coverage. Run A → B → C sequentially with time offsets.

### Lesson 2: One Start Time per program only
The most common mistake: setting multiple Start Times → water runs multiple times per day.
Each program must have exactly one Start Time.

### Lesson 3: Seasonal Adjust handles the whole season
No need to change each station's Run Time individually.
Use a single Seasonal Adjust % to scale the entire system up or down.

---

## 📚 Learning Order (Read in this sequence)

### ⚠️ Step 0. First Startup — Do This First (required for new systems)

> **When this applies**: First time using the system after move-in, or spring restart after leaving it OFF all winter.
> This home was moved into in October 2025 and the sprinkler stayed OFF all winter → **March 2026 is the first startup**.

0. [concepts/first-startup-guide.md](concepts/first-startup-guide.md) ⭐⭐
   - Finding the main valve from orientation video, how to open it slowly
   - Backflow preventer check, controller power ON, first manual test sequence
   - **Complete this guide before proceeding to Step 1**

> Also use [outdoor-tasks-20260311.md](outdoor-tasks-20260311.md) **Task 0** checklist alongside this guide.

---

### Step 1. Background — Full Controller Overview

> Quickly go through all ESP-ME3 functions first.

1. [../vl_materials/esp-me3-quick-reference.md](../vl_materials/esp-me3-quick-reference.md)
   - Basic 5-step programming flow, manual watering, ALERT meanings
   - **⭐ Start here** — one-page summary cheat sheet

2. [../vl_materials/esp-me3-complete-guide.md](../vl_materials/esp-me3-complete-guide.md)
   - Full basic and advanced programming, Seasonal Adjust, troubleshooting
   - Full reference — use as needed

---

### Step 2. Strategy — Custom Schedule for My Lawn

> Use background knowledge to plan a schedule tailored to your yard.

3. [concepts/program-strategy.md](concepts/program-strategy.md)
   - Programs A/B/C/D role separation, spring schedule design (start time/days/run time)
   - Common mistakes & fixes

4. [concepts/seasonal-adjust-guide.md](concepts/seasonal-adjust-guide.md)
   - Monthly recommended Seasonal Adjust % table (Tehaleh WA)
   - Current (March) recommended: **70%**, with adjustment instructions

5. [concepts/advanced-cycles-guide.md](concepts/advanced-cycles-guide.md)
   - Cycle+Soak principle, how to apply it to sloped front yard zones
   - Settings: 10 min × 3 cycles + 15 min soak

---

### Step 3. Outdoor Practice — Audit + Schedule Setup

> Practice at the actual controller and walk your yard.

6. [outdoor-tasks-20260311.md](outdoor-tasks-20260311.md) ⭐
   - **Full to-do list for daylight hours** (Tasks 1–5)
   - Task 1: Measure lawn area by pacing
   - Task 2: Read current controller settings + take photos
   - Task 3: Manual test all stations
   - Task 4: Document unusual findings with photos
   - Task 5: Send results to AI → calculate spring schedule

7. [current-settings-audit.md](current-settings-audit.md)
   - Template to record current settings read during outdoor practice
   - ⏳ **Fill in after outdoor practice**

---

### Step 4. Final Settings (to be completed after outdoor practice)

> Document practice results and finalize the optimal spring schedule.

8. [spring-schedule-2026.md](spring-schedule-2026.md)
   - Spring schedule draft based on measured area (8,713 sq ft)
   - Program A/B/C settings, timeline, seasonal adjustment plan
   - ⏳ Actual station numbers to be filled in after outdoor practice

9. station-test-log.md *(to be created)*
   - Per-station test results and any issues found

---

### Reference: Alexa Voice Control Integration

10. [../vl_materials/alexa-smart-home-guide.md](../vl_materials/alexa-smart-home-guide.md)
    - LNK WiFi module setup, Alexa skill configuration, voice command examples
    - Recommended to do after basic schedule setup is complete

---

## 📊 Progress Status

| Step | Content | Status |
|------|---------|--------|
| **Step 0** | **First startup** (orientation video → valve open → first test) | ⏳ Not done |
| Step 1 | Background reading (quick-reference, complete-guide) | ✅ Done |
| Step 2 | Strategy documents (program, seasonal, cycles) | ✅ Done |
| Step 3 | Outdoor practice | ⏳ After Step 0 |
| Step 3 | current-settings-audit completed | ⏳ After outdoor |
| Step 4 | spring-schedule-2026 **draft done** (measured area basis) | ✅ Draft done, finalize after outdoor |
| Step 4 | station-test-log created | ⏳ After outdoor |

---

## Spring Target Settings (apply after outdoor practice)

| Item | Setting |
|------|---------|
| Seasonal Adjust | **70%** |
| Program A Start Time | **5:00 AM** (one only) |
| Program A Water Days | **Mon / Wed / Fri** |
| Program B Start Time | **5:30 AM** |
| Program C Start Time | **7:00 AM** |
| Front yard slope zone | **Multiple Start Times** 10 min×3 (controller only) or **Cycle+Soak** (with App+LNK2) |

---

**Previous Module**: [M1: PNW Lawn Basics + Spring Prep](../01-Spring-Basics/README.en.md)
**Next Module**: M3: Summer Care + Troubleshooting *(starts after outdoor practice)*
**Methodology**: VibeLearn AI
