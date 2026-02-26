# VibeLearn AI Roadmap Generation Prompt

**Version**: 2.0
**Created**: 2025-12-28
**Methodology**: VibeLearn AI

---

## 📌 How to Use

This prompt automatically generates a learning roadmap based on the Topic information entered in `topic_starter.md`.

**Procedure**:
1.  Once the Topic folder is created, this file is copied to `[TopicName]/vl_prompts/`.
2.  The Topic information is already injected.
3.  Provide this entire file to the AI.
4.  The AI generates a standard VibeLearn AI roadmap.
5.  Save the generated roadmap to `vl_roadmap/YYYYMMDD_RoadMap_{Topic}.md`.

---

## [Step 1] Topic Information (Automatically Injected)

> **Note**: This section is automatically filled with information from `topic_starter.md`.
> If modifications are needed, edit the `topic_info.md` file.

### Basic Information

**Topic Name**: `{TOPIC_NAME}`

**Topic Description**:
```
{TOPIC_DESCRIPTION}
```

**Learning Purpose**:
```
{LEARNING_GOALS}
```

**Estimated Learning Period**: `{DURATION}`

---

### Environment and Prerequisites

**Operating System**: `{OS}`

**Main Tools and Tech Stack**:
```
{TECH_STACK}
```

**Prerequisites**:
```
Required:
{PREREQUISITES_REQUIRED}

Recommended:
{PREREQUISITES_RECOMMENDED}
```

---

### Outputs and References

**Learning Objectives** (What you want to achieve):
```
{LEARNING_OBJECTIVES}
```

**Reference Materials**:
```
{REFERENCE_MATERIALS}
```

**vl_materials/ Folder**:
```
{MATERIALS_FOLDER_INFO}
```

---

## [Step 2] Task to Request from the AI

Based on the injected Topic information above, please generate a learning roadmap that follows the **VibeLearn AI methodology**.

---

### 🔍 STEP 1: Review Appropriateness of Learning Period (Required)

**Must be performed before generating the roadmap:**

Analyze whether the user-entered learning period `{DURATION}` is appropriate for the Topic and provide feedback.

#### Analysis Criteria:
1.  **Assess Topic Complexity**
    -   Simple (e.g., CLI tool, basic concepts): 3-7 days is appropriate.
    -   Intermediate (e.g., framework, library): 2-4 weeks is appropriate.
    -   Complex (e.g., large-scale system, multiple technologies): 1-3 months is appropriate.

2.  **Consider Prior Knowledge**
    -   Sufficient prior knowledge: The period can be shortened.
    -   Lack of prior knowledge: The period needs to be extended.

3.  **Scope of Learning Objectives**
    -   Basic understanding: Short period.
    -   Practical application level: Intermediate period.
    -   Expert level: Long period.

#### Feedback Format:

```markdown
## 📊 Analysis of Learning Period Appropriateness

**User-entered Period**: {DURATION}
**Topic Complexity**: [Simple/Intermediate/Complex]
**Recommended Period**: [X weeks or Y days]

**Analysis Result**:
- ✅ **Appropriate**: The period you entered is suitable for learning this Topic.
- ⚠️ **Too Short**: This Topic generally requires [Recommended Period]. With the current period, you will only learn the core concepts quickly.
- ⚠️ **Too Long**: [Recommended Period] is usually sufficient for this Topic. You can learn at a relaxed pace or cover advanced content.

**Suggested Action**:
- [If appropriate] Proceed as planned.
- [If too short] 1) Recommend extending the period or 2) Reduce the learning scope (basics only).
- [If too long] 1) Shorten the period or 2) Add advanced content.

**User Confirmation Needed**:
Please review the analysis above and choose one of the following:
1.  "Proceed as is" - Continue with the entered period.
2.  "Adjust period" - Change to the recommended period.
3.  "Adjust scope" - Keep the period but adjust the learning scope.
```

**Important**: Pause roadmap generation and wait until the user confirms and makes a final decision.

---

### 🗺️ STEP 2: Roadmap Generation Requirements

After the user finalizes the period, generate the roadmap according to the requirements below.

#### Overall Structure

**Learning Period**: Adjust to match `{Final Confirmed Period}`.
-   3 days or less: 3-5 modules
-   1-2 weeks: 5-7 modules
-   1 month or more: 7-10 modules

**Module Composition Principles**:
-   Each module is an independently completable unit.
-   Difficulty increases gradually (Basics → Intermediate → Advanced).
-   The final module is a Capstone project (integrated practice).

**Naming Conventions**:
-   Modules: `M1`, `M2`, `M3`, ...
-   Output folders: `01-{TopicName}/`, `02-{TopicName}/`, ...

---

#### Required Items for Each Module

Each module must include the following 9 items:

##### 1. Basic Module Information
```markdown
### MX - {Module Name}

**Difficulty**: ⭐/⭐⭐/⭐⭐⭐ (1-3)
**Estimated Time**: X hours
**Output Folder**: `0X-{ModuleName}/`
```

##### 2. Learning Objectives (3-5)
-   Write them to be verifiable ("understand ~" X, "be able to implement ~" O).
-   Use checklist format `- [ ]`.
-   Specific and measurable objectives.

##### 3. Key Concepts
-   Definitions of 3-5 key terms.
-   1-2 sentence explanation for each concept.
-   Mention common points of misunderstanding.

##### 4. Practical Exercises (2-3)
For each exercise:
-   **Exercise Name**: A clear name.
-   **Purpose**: Why this exercise is being done.
-   **Steps**: Specific execution steps (1, 2, 3, ...).
-   **Estimated Time**: X minutes.
-   **Difficulty**: ⭐/⭐⭐/⭐⭐⭐.
-   **Verification Method**: How to confirm success.

##### 5. Outputs
-   Folder structure to be created.
-   List of required files (README.md, code, documents, etc.).
-   Recommended subfolders (`concepts/`, `examples/`, `guides/`, `troubleshooting/`).

##### 6. Definition of Done
5-8 items in a checklist format:
```markdown
- [ ] Achieved all learning objectives.
- [ ] Completed X practical exercises.
- [ ] Successfully executed Y key commands/APIs.
- [ ] Created output folder and wrote README.
- [ ] Completed WorkLog.
- [ ] Completed Daily Retrospective.
```

##### 7. Self-Assessment
Evaluation criteria suitable for the AI era (3-5 questions):
```markdown
**Conceptual Understanding** (5 min):
- [ ] Can explain what this technology/feature is in 1-2 sentences.
- [ ] Can explain why it's needed with examples.

**Practical Application** (5 min):
- [ ] Can request tasks using this technology from an AI.
- [ ] Can judge the quality of code generated by an AI.

**Problem Solving** (5 min):
- [ ] Can suggest debugging directions to an AI when a problem occurs.
```

##### 8. Estimated Time Allocation
```markdown
-   Concept Learning: X min (20-30%)
-   Practice 1: X min
-   Practice 2: X min
-   Documentation: X min
-   **Total**: X hours (including 20% buffer)
```

##### 9. Reference Materials
-   Official documentation link (required).
-   Tutorials/examples (recommended).
-   1-line description for each link.

---

#### Practice Design Principles (Important!)

When designing practical exercises, you **must** adhere to the following principles:

##### 1. Practice First
-   Theory explanation: 20-30%
-   Practice time: 70-80%
-   Repeat the "Explain concept → Immediate practice" pattern.

##### 2. Gradual Complexity
-   Practice 1: Simple (⭐) - "Hello World" level.
-   Practice 2: Intermediate (⭐⭐) - Practical function.
-   Practice 3: Advanced (⭐⭐⭐) - Optional, in-depth.

##### 3. Verifiability
-   Success of all practice can be confirmed by the execution result.
-   e.g., "Log output," "File creation," "Successful API response."
-   Provide clear success criteria.

##### 4. AI-Era Learning Scope
**What humans should know**:
-   Conceptual understanding (what, why, when).
-   Architecture and structure.
-   How to effectively instruct an AI.
-   Basic usage patterns (3-5 core features).

**Memorization not required**:
-   Detailed API parameter lists.
-   All options and flags.
-   Internal implementation details.

##### 5. Output-centric
-   Create a folder for each module (`01-xxx/`, `02-xxx/`).
-   **"Textbook quality"**: At a level that another learner can learn from this alone.
-   README.md must be included (overview, usage, examples).

##### 6. Consider the Environment
-   Use commands appropriate for the OS/tools entered by the user.
-   Windows: PowerShell commands.
-   macOS/Linux: Bash commands.
-   Adjust path notation to match the OS.

---

#### VibeLearn AI Methodology Integration

Integrate the following VibeLearn AI elements into the roadmap:

##### 1. WorkLog Guide
```markdown
## WorkLog Writing Guide

Track your progress by writing a WorkLog for each learning session.

**Filename Convention**: `vl_worklog/YYYYMMDD_MX_{Topic}.md`
- e.g., `vl_worklog/20251228_M1_MCP-Basics.md`

**Required WorkLog Sections**:
1.  Today's Learning Objectives (checklist)
2.  Progress Details (detailed record per exercise)
3.  Problem Solving Log
4.  DoD Checklist (module completion criteria)
5.  Daily Retrospective
6.  References and Outputs
```

##### 2. Retrospective Guide
```markdown
## Retrospective Guide

### Daily Retrospective (Daily, 5-10 min)
Write within the WorkLog:
- What went well?
- What could be improved?
- Insights
- Tomorrow's focus

### Module Retrospective (On module completion, 15-20 min)
`vl_worklog/YYYYMMDD_MX_Retrospective.md`:
- Plan vs. Actual comparison
- Key learnings
- Problems encountered and solutions
- Roadmap accuracy assessment
- Preparation for the next module

### Topic Retrospective (On total completion, 30-60 min)
`vl_worklog/YYYYMMDD_{Topic}_Final_Retrospective.md`:
- Overall learning journey statistics
- Evaluation of VibeLearn AI methodology effectiveness
- Output quality assessment
- Future learning improvements
```

##### 3. Folder Structure
```
{Topic}/
├── topic_info.md              # Topic information (reference)
├── vl_prompts/
│   ├── roadmap_prompt.md      # This file
│   └── daily_learning_prompt.md
├── vl_roadmap/
│   └── YYYYMMDD_RoadMap_{Topic}.md  # Roadmap to be created
├── vl_worklog/
│   ├── YYYYMMDD_M1_{Topic}.md
│   ├── YYYYMMDD_M2_{Topic}.md
│   └── ...
├── vl_materials/              # Optional: Reference materials
│   └── (PDF, documents, code, etc.)
├── 01-{Module1}/
│   ├── README.md
│   ├── concepts/
│   ├── examples/
│   ├── guides/
│   └── troubleshooting/
├── 02-{Module2}/
└── ...
```

---

#### Module Composition Example (for reference)

Below is an example of module composition for a typical learning Topic (adjust according to the Topic):

**M1 - Overview and Core Concepts**
-   What the Topic is and why it's needed.
-   Understanding key terms and architecture.
-   First practice at a "Hello World" level.

**M2 - Environment Setup**
-   Build the development environment.
-   Install and verify required tools.
-   Project scaffolding.

**M3 - Basic Functions**
-   Learn 3-5 core features.
-   Basic usage patterns.
-   Implement simple examples.

**M4 - Intermediate Functions**
-   Utilize advanced features.
-   Apply to real scenarios.
-   Error handling and debugging.

**M5 - Integration and Application**
-   Integrate into an existing project.
-   Apply practical patterns.
-   Performance optimization (optional).

**M6 - Deployment and Documentation** (Optional)
-   Deploy to production.
-   Write documentation.
-   Prepare for team sharing.

**MX (Final) - Capstone Project**
-   Integrate all learned content.
-   Implement a complete project.
-   Finalize the ultimate output.

---

## [Step 3] Output Format

Generate the roadmap in the following Markdown format and save it to `vl_roadmap/YYYYMMDD_RoadMap_{Topic}.md`.

### Roadmap Template Structure

```markdown
# {Topic} Learning Roadmap

**Created**: YYYY-MM-DD
**Methodology**: VibeLearn AI
**Version**: 1.0

---

## 📚 Learning Overview

### Topic Introduction
{Topic Description}

### Learning Objectives
{Learning objectives from topic_starter.md}

### Estimated Learning Period
{Entered period}

### Learning Environment
-   OS: {OS}
-   Tools: {Tech Stack}
-   Prerequisites: {Prerequisites}

---

## 🗺️ Overall Roadmap Structure

| Module | Module Name | Difficulty | Est. Time | Output Folder |
|---|---|---|---|---|
| M1 | {Module Name} | ⭐ | Xh | 01-{Name}/ |
| M2 | {Module Name} | ⭐⭐ | Xh | 02-{Name}/ |
| ... | ... | ... | ... | ... |

**Total Estimated Time**: X hours

---

## 📖 Detailed Module Plan

### M1 - {Module Name}

**Difficulty**: ⭐
**Estimated Time**: Xh
**Output Folder**: `01-{ModuleName}/`

#### Learning Objectives
- [ ] Objective 1
- [ ] Objective 2
- [ ] Objective 3

#### Key Concepts
1.  **Concept1**: Description
2.  **Concept2**: Description
3.  **Concept3**: Description

#### Practical Exercises

**Practice 1: {Exercise Name}** ⭐
-   **Purpose**: {Purpose}
-   **Steps**:
    1.  Step 1
    2.  Step 2
    3.  Step 3
-   **Estimated Time**: X min
-   **Verification**: {Verification method}

**Practice 2: {Exercise Name}** ⭐⭐
{Same format}

#### Outputs
```
01-{ModuleName}/
├── README.md
├── concepts/
│   └── concept1.md
├── examples/
│   └── example1.py
└── guides/
    └── guide1.md
```

#### Definition of Done
- [ ] Item 1
- [ ] Item 2
- [ ] Item 3
- [ ] Item 4
- [ ] Item 5

#### Self-Assessment
**Conceptual Understanding**:
- [ ] Question 1
- [ ] Question 2

**Practical Application**:
- [ ] Question 3
- [ ] Question 4

#### Estimated Time Allocation
-   Concept Learning: X min
-   Practice 1: X min
-   Practice 2: X min
-   Documentation: X min
-   **Total**: Xh

#### Reference Materials
-   [Official Docs](URL): Description
-   [Tutorial](URL): Description

---

{Repeat in the same format for M2, M3, ...}

---

## 📝 WorkLog Writing Guide

{Content of the WorkLog guide from above}

---

## 🔍 Retrospective Guide

{Content of the Retrospective guide from above}

---

## 📂 Overall Folder Structure

{Content of the folder structure from above}

---

## 📊 Learning Progress Tracker

| Module | Start Date | End Date | Status | DoD Rate | Notes |
|---|---|---|---|---|---|
| M1 | | | ⏳ | 0% | |
| M2 | | | ⏳ | 0% | |
| ... | | | | | |

**Legend**:
-   ⏳ Pending
-   🔄 In Progress
-   ✅ Completed

---

## 🎯 Success Criteria

Criteria for completing the entire Topic:
- [ ] All modules completed (100% DoD)
- [ ] At least {N} output folders created
- [ ] Topic Retrospective written
- [ ] Self-Assessment average ⭐⭐⭐⭐ or higher
- [ ] Capstone project completed

---

**Generated by**: Claude with VibeLearn AI
**Roadmap Version**: 1.0
**Methodology Version**: VibeLearn AI 2.0
```

---

## ✅ Roadmap Quality Checklist

Check if the generated roadmap meets the following criteria:

### Structure
- [ ] Appropriate number of modules for the learning period.
- [ ] Gradual increase in difficulty (Basics → Advanced).
- [ ] Includes a final Capstone module.
- [ ] Each module is independent.

### Each Module
- [ ] 3-5 verifiable learning objectives.
- [ ] 3-5 key concepts (with clear definitions).
- [ ] 2-3 practical exercises (with specific steps).
- [ ] Output structure is specified.
- [ ] 5-8 DoD checklist items.
- [ ] 3-5 Self-Assessment questions.
- [ ] Time allocation is specified (including buffer).
- [ ] Links to reference materials.
- [ ] All 9 required items are included.

### VibeLearn AI Integration
- [ ] WorkLog guide.
- [ ] Retrospective guide (3 stages).
- [ ] Folder structure is specified.
- [ ] Progress tracking table.

### Practice Design
- [ ] Practice-first (70-80% practice, 20-30% theory).
- [ ] Verifiable results.
- [ ] Environment is considered (OS-specific commands).
- [ ] AI-era learning scope is applied.
- [ ] Outputs = Textbook quality.

---

## 🎯 Final Check

After roadmap generation is complete:

1.  [ ] Save to `vl_roadmap/YYYYMMDD_RoadMap_{Topic}.md` file.
2.  [ ] Check the total number of modules (is it right for the period?).
3.  [ ] Verify with the quality checklist.
4.  [ ] Request user to review the roadmap.
5.  [ ] Reflect feedback and make adjustments.
6.  [ ] Prepare to start the first module (M1).

---

**Generated by**: Claude with VibeLearn AI
**Template Version**: 2.0
**Created**: 2025-12-28
**Methodology**: VibeLearn AI
