# VibeLearn AI Workflow Guide

**Version**: 1.0
**Created**: 2026-01-25
**Methodology**: VibeLearn AI

---

## 📌 Overview

This guide explains how to use prompts for each workflow so that the VibeLearn AI learning methodology can be used with **any AI tool**.

**Supported AI Tools**:
- ChatGPT (OpenAI)
- Claude (Anthropic)
- Gemini (Google)
- Copilot (Microsoft)
- Other LLM-based AI tools

---

## 🚀 Overall Workflow

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  1. Start Topic  │ ──▶ │  2. Gen Roadmap  │ ──▶ │  3. Daily Learn  │
│  topic_starter  │     │  roadmap_prompt │     │  daily_learning │
└─────────────────┘     └─────────────────┘     └─────────────────┘
        │                       │                       │
        ▼                       ▼                       ▼
   topic_info.md         RoadMap_{Topic}.md      WorkLog_{Date}.md
```

---

## 📋 Step-by-Step Guide

---

### Step 1: Start a New Topic

**When to use**: When starting to learn a new technology/framework/concept.

#### 1.1 Prompt to Send to the AI

```
I want to start a new learning Topic using the VibeLearn AI methodology.

Based on the information below:
1. Please create the Topic folder structure.
2. Help me create the topic_info.md file.

## Topic Information
- Topic Name: [e.g., Docker-Fundamentals]
- Description: [e.g., From basic concepts of Docker container technology to practical application]
- Learning Purpose: [e.g., Improve productivity by containerizing the development environment]
- Estimated Period: [e.g., 2 weeks (5 hours per week)]
- Learning Objectives:
  - [e.g., Understand the concepts of Docker images and containers]
  - [e.g., Be able to create custom images by writing a Dockerfile]
  - [e.g., Be able to configure a multi-container environment with docker-compose]

## Folder Structure to Create
Topics/{TopicName}/
├── topic_info.md           # Basic Topic Information
├── vl_prompts/             # Prompt Templates
├── vl_roadmap/             # Learning Roadmap
├── vl_worklog/             # Learning Log
└── vl_materials/           # Reference Materials
```

#### 1.2 Create Folders Manually (Optional)

If the AI cannot create folders directly:

**Windows (PowerShell)**:
```powershell
$topic = "Docker-Fundamentals"
mkdir "Topics/$topic/vl_prompts", "Topics/$topic/vl_roadmap", "Topics/$topic/vl_worklog", "Topics/$topic/vl_materials" -Force
```

**macOS/Linux (Bash)**:
```bash
topic="Docker-Fundamentals"
mkdir -p "Topics/$topic"/{vl_prompts,vl_roadmap,vl_worklog,vl_materials}
```

#### 1.3 Next Steps

- [ ] Complete writing `topic_info.md`.
- [ ] Proceed to Step 2: Roadmap Generation.

---

### Step 2: Generate Roadmap

**When to use**: After `topic_info.md` is complete.

#### 2.1 Prompt to Send to the AI

```
Please generate a learning Roadmap according to the VibeLearn AI methodology.

## Topic Information
[Paste the content of topic_info.md here]

## Roadmap Generation Request
Please generate the Roadmap according to the VibeLearn AI standards below:

### Required Items (per module)
1. Basic module info (number, title, estimated time)
2. Learning objectives (3-5)
3. Core concepts (20-30% theory)
4. Practical exercises (70-80% practice)
5. Expected outputs
6. Definition of Done
7. Self-assessment checklist
8. Time allocation
9. Reference materials

### Module Composition Principles
- The first module should be environment setup + a quick success experience.
- Each module should be completable in 1-2 days.
- The final module should be a comprehensive project.

### Output Format
Please output in Markdown format.
Filename: YYYYMMDD_RoadMap_{TopicName}.md
```

#### 2.2 Use Detailed Prompt (Recommended)

For a more refined Roadmap, use the entire `templates/roadmap_prompt_template.md` file.

#### 2.3 Save the Roadmap

Save the generated Roadmap to the following location:
```
Topics/{TopicName}/vl_roadmap/YYYYMMDD_RoadMap_{TopicName}.md
```

#### 2.4 Next Steps

- [ ] Review and save the Roadmap.
- [ ] Proceed to Step 3: Daily Learning.

---

### Step 3: Start Daily Learning

**When to use**: At the start of each daily learning session.

#### 3.1 Prompt to Send to the AI

```
I am starting today's learning according to the VibeLearn AI methodology.

## Current Status
- Topic: [e.g., Docker-Fundamentals]
- Current Module: [e.g., M2 - Writing a Dockerfile]
- Available Time: [e.g., 3 hours]

## Roadmap
[Paste the content of the Roadmap file or just the current module part here]

## Previous WorkLog (if any)
[Paste the content of the most recent WorkLog here]

## Request
1. Please create a learning plan for today.
2. Tell me where to start in the current module.
3. Guide me to handle any unfinished tasks first.
```

#### 3.2 Use Detailed Prompt (Recommended)

For a more structured learning session, use the entire `templates/daily_learning_prompt.md` file.

#### 3.3 Write WorkLog While Learning

Write the WorkLog in real-time as you learn:
```
Topics/{TopicName}/vl_worklog/YYYYMMDD_M{X}_{TopicName}.md
```

**Required WorkLog Items**:
- Tasks completed today
- Problems encountered and their solutions
- Learning insights
- Tomorrow's focus

---

## 📁 Folder Structure Reference

### Overall Structure

```
VibeLearn-AI/
├── README.md                        # Methodology description
├── GETTING_STARTED.md               # Quick start guide
├── templates/                       # Prompt templates
│   ├── topic_starter.md             # Topic start template
│   ├── roadmap_prompt_template.md   # Roadmap generation prompt
│   ├── daily_learning_prompt.md     # Daily learning prompt
│   └── workflow_guide.md            # This file
└── Topics/                          # Learning Topics
    └── {TopicName}/
        ├── topic_info.md
        ├── vl_prompts/
        ├── vl_roadmap/
        │   └── YYYYMMDD_RoadMap_{TopicName}.md
        ├── vl_worklog/
        │   └── YYYYMMDD_M{X}_{TopicName}.md
        └── vl_materials/
```

### vl_ Prefix Rule

| Folder          | Purpose                |
|-----------------|------------------------|
| `vl_prompts/`   | Topic-specific prompts |
| `vl_roadmap/`   | Learning roadmaps      |
| `vl_worklog/`   | Learning logs (WorkLogs) |
| `vl_materials/` | Reference materials    |

---

## 🔄 Retrospective

### Daily Retrospective (Daily, 5-10 min)

Add to the WorkLog at the end of the learning session:

```markdown
## Daily Retrospective

### What I Learned Today
- [Key takeaway 1]
- [Key takeaway 2]

### What Went Well
- [Success experience]

### What Could Be Better
- [Point for improvement]

### Tomorrow's Focus
- [Task 1 for tomorrow]
- [Task 2 for tomorrow]
```

### Module Retrospective (On module completion, 15-20 min)

```markdown
## Module Retrospective - M{X}

### Achievement of Learning Objectives
- [ ] Objective 1: [Achieved/Not Achieved]
- [ ] Objective 2: [Achieved/Not Achieved]

### Key Insights
1. [Insight 1]
2. [Insight 2]

### Preparation for Next Module
- [Things to prepare]
```

### Topic Retrospective (On Topic completion, 30-60 min)

```markdown
## Topic Retrospective - {TopicName}

### Overall Achievement of Learning Objectives
- [ ] Objective 1: [Achieved/Not Achieved]

### Most Valuable Learning
- [Content]

### Plan for Practical Application
- [Plan]

### Suggestions for Methodology Improvement
- [Suggestion]
```

---

## 💡 Tips & Best Practices

### Tip 1: Naming a Topic

**Good Examples**:
- `Docker-Fundamentals` (Technology-Difficulty)
- `React-Hooks` (Technology-Specific Subject)
- `ML-Basics` (Acronym-Difficulty)

**Examples to Avoid**:
- `Docker` (Too broad)
- `docker advanced` (Uses a space)

### Tip 2: Writing Learning Objectives

**Good Examples**:
- "Be able to create a custom image by writing a Dockerfile."
- "Be able to link 3 or more services with docker-compose.yml."

**Examples to Avoid**:
- "Understand Docker" (Not verifiable)
- "Become a Docker expert" (Not measurable)

### Tip 3: Write WorkLog in Real-time

- Record immediately **during** learning.
- "Studied" (X) → "Completed 5 examples of Pandas DataFrame practice" (O)
- Detail the problem-solving process.

### Tip 4: Maintain Practice Ratio

- **Theory 20-30%**: Understanding concepts, reading docs.
- **Practice 70-80%**: Writing code, working on projects.

---

## 📞 Help

### More Information

- **Full Methodology Description**: `README.md`
- **Quick Start Guide**: `GETTING_STARTED.md`
- **Detailed Templates**: `templates/` folder

### Contact

- Email: solkit70@gmail.com
- GitHub: [VibeLearn-AI Repository]

---

**Template Version**: 1.0
**Created by**: VibeLearn AI Methodology
**Last Updated**: 2026-01-25
