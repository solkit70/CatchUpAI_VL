slidenumbers: true

---

# VibeLearn AI
## A New Way to Learn Systematically with AI

**Catch Up AI | 2026**

^ Hey everyone, welcome to Catch Up AI! Today I'm excited to share a learning methodology I've been using that's been incredibly effective. It's called VibeLearn AI. The idea is simple — just say "I want to learn Python" to your AI tool, and it takes care of everything: creating a learning plan, guiding you through daily sessions, and turning what you've learned into reusable documentation that others can use too. In this video, I'll show you what it is, how it works, and the real results I got from using it.

---

## 📋 What We'll Cover Today

- 🤔 Why does learning with AI still feel scattered?
- 💡 What is VibeLearn AI?
- 🔄 The 4-Phase workflow: how it works
- 🛠️ Live demo: step-by-step walkthrough
- 📊 Case Study: 9.5 hours → YouTube videos
- 🚀 How to get started right now

^ Here's what we'll cover today. We'll start by looking at why learning — even with AI — often doesn't stick. Then I'll show you how VibeLearn AI solves that problem, walk through the workflow step by step, and share a real case study showing the actual results. By the end, you'll have everything you need to start today.

---

## 🙋 This Video Is For You If...

- You watch tutorials and **forget everything a week later**
- You use ChatGPT to study but **lose all context when you close the window**
- You learn things but **can't explain them to others**
- You want to **learn systematically with AI as your partner**

^ Does any of this sound familiar? You watch a tutorial, think "I've got it!" — and then a week later you're searching for the same video again. Or you're in the middle of a great study session with ChatGPT, close the tab, and when you come back... it's like starting from zero. I've been there too. VibeLearn AI was built to solve exactly these problems.

---

# The Problem

---

## 😩 The Typical Learning Pattern

```
Watch tutorial → "I got it!" → 1 week later → "How did I do that?"
                                               ↓
                               Search again (infinite loop)
```

**Result**: Time spent, but knowledge doesn't accumulate

^ Why does this happen? The biggest reason is that what you learn never gets accumulated anywhere. While you're watching, it makes sense. But if the understanding doesn't get organized into structured knowledge, it fades. And the algorithm keeps recommending more videos, which actually reinforces this loop.

---

## 🤖 New Challenges When Learning With AI

| Problem | What Happens |
|:--::--::--:|:--::--::--::--:--|
| **Context loss** | Close the chat window → AI forgets everything |
| **Inconsistent guidance** | Different AI sessions give different directions |
| **Can't share** | What you learned stays locked in your head |
| **No progress tracking** | Hard to know "where was I again?" |

^ AI tools didn't automatically fix these problems — they actually introduced new ones. When you close an AI chat, all the context is gone. Every new session, you have to re-explain everything. That's why using AI as a learning partner requires a different approach. That's where VibeLearn AI comes in.

---

## 🎯 Solving All Four Problems Together

| Problem | Solution |
|:--::--::--:|:--::--::--:-|
| Knowledge fades | **WorkLog** records every learning session |
| No structure | **Standard folder structure** organizes everything |
| Context lost | **File-based persistence** — files hold the context |
| Can't share | **Textbook-quality outputs** — reusable by others |

^ What if there was a system that solved all four of these at once? That's exactly what VibeLearn AI does. Let me show you how.

---

# What Is VibeLearn AI

---

## ✨ VibeLearn AI, In One Sentence

> **"A repeatable system that uses AI as a learning partner to turn your personal learning journey into structured, reusable documentation."**

🌐 **github.com/solkit70/VibeLearn-AI** (Free & Open Source)

^ VibeLearn AI is a learning methodology that treats AI not as a search engine, but as a true learning partner. And crucially, what you learn doesn't disappear — it becomes textbook-quality documentation that others can use too. It's free and open source on GitHub, so anyone can start right now.

---

## 🎨 The Most Important Design Principle

> **"You don't need to learn this methodology."**
>
> "I want to learn Python basics."
> → AI handles everything else.

**What gets automated**:
- ✅ Collecting your learning info (AI asks via conversation)
- ✅ Creating folder structure
- ✅ Generating your learning Roadmap
- ✅ Planning each daily session
- ✅ Writing WorkLogs

^ This is the principle I care most about in VibeLearn AI. You shouldn't need to study the methodology before you can use it. Just say "I want to learn Python basics" and the AI will ask what it needs to know, set up your folders, generate a roadmap, and guide you through daily sessions. You just need to want to learn something.

---

## 🔄 The 4-Phase Workflow

```
Phase 1: Topic Setup (once per topic)
  "I want to learn Python" → AI collects info → Auto-creates folders & files

Phase 2: Roadmap Generation (once per topic)
  AI auto-generates personalized learning plan → Defines modules, goals, deliverables

Phase 3: Daily Learning (repeating cycle)
  "Start today's learning" → AI checks progress → Today's plan → Practice → Log

Phase 4: Completion & Retrospective (once per topic)
  Module complete → Textbook-quality output → Topic retrospective
```

^ The whole process has four phases. You set up your Topic once, and then AI generates a roadmap for that specific topic. After that, every day you just say "start today's learning," and AI figures out where you left off and what to do today. When you finish, you have a polished set of documentation.

---

## 🌐 Works for Any Topic

| Field | Examples |
|:--::--:-|:--::--::--:|
| Programming | Python, JavaScript, Rust |
| AI/ML Tools | Claude API, LangChain |
| Frameworks | React, FastAPI, Docker |
| **Non-technical** | English writing, financial planning |
| Creative | Video editing, Figma design |

**The only requirement**: You want to learn + You have access to an AI tool

^ VibeLearn AI isn't limited to technical topics. English writing, financial planning, cooking techniques — it works for anything. The only requirements are that you want to learn something and you have access to an AI tool.

---

# How to Use It

---

## 🛠️ What You Need

**Required**:
- One AI tool (that can read/write files):
  - **VS Code + GitHub Copilot** (most common)
  - **VS Code + Claude Code** (Extension)
  - **Cursor** (AI-native editor)
- Something you want to learn

**Optional**:
- GitHub account (for version control & sharing)

> 💡 Web-based AI can't create files directly — use an editor-integrated AI tool

^ The setup is minimal. An AI tool and something to learn — that's all. The key is using an AI tool that can access your file system, so it can actually create folders, read files, and write WorkLogs. Editor-integrated tools like VS Code with Copilot or Cursor work great.

---

## 📥 Step 1: Get VibeLearn AI (5 minutes)

```bash
git clone https://github.com/solkit70/VibeLearn-AI.git
cd VibeLearn-AI
```

**Verify these files exist**:
```
VibeLearn-AI/
├── README.md
├── GETTING_STARTED.md
└── templates/
    ├── topic_starter.md
    ├── roadmap_prompt_template.md
    └── daily_learning_prompt.md
```

^ Clone or download the VibeLearn AI repository from GitHub. Five minutes is all it takes. You'll see a templates folder — those are the standard templates the AI uses internally. You don't need to open or edit those files. The AI handles them automatically.

---

## 💻 Step 2: Open in Your AI Tool (2 minutes)

**VS Code + GitHub Copilot**:
1. Open `VibeLearn-AI/` folder in VS Code
2. Open Copilot Chat (`Ctrl+Alt+I`)

**VS Code + Claude Code**:
1. Open folder in VS Code
2. Activate Claude Code Extension panel

**Cursor**:
1. Open `VibeLearn-AI/` folder in Cursor

^ Open the VibeLearn-AI folder in your AI tool. The important thing is that the AI tool can see and read the files inside this folder — that's how it accesses the template system and maintains context across sessions.

---

## 🗣️ Step 3: That's All There Is to It

```
"I want to learn Python basics."
```

**What AI automatically does**:
1. Asks about your goals, timeline, and background
2. Creates `Topics/Python-Basics/` folder structure
3. Auto-generates a personalized learning Roadmap
4. Guides you to start your first module

**Every day after that**:
```
"Start today's learning."
```
→ AI checks your progress and picks up where you left off

^ This is the moment where it all comes together. Just say "I want to learn Python basics" and the AI takes it from there. It asks a few questions, sets up your folders, and generates your roadmap. From that point on, every morning you just say "start today's learning" and the AI knows exactly where you left off.

---

# Case Study

---

## 📊 Real Case: Learning the Clearly App for BRD/PRD

**Starting Point**:
- "I want to learn Clearly (an AI-powered BRD/PRD tool)"
- Prior knowledge: Knew it existed, but never used it

**Results**:
- **Total time**: 9.5 hours (over 5 days)
- **Outputs**: 22 documentation files
- **Final**: 2 YouTube intro videos (Korean + English)

^ Let me show you a real example. I used VibeLearn AI to learn the Clearly app — an AI tool that helps you write product requirement documents. Starting from knowing almost nothing about it, in 9.5 hours I produced 22 documentation files and two YouTube videos.

---

## 🗓️ Learning Timeline

| Module | Content | Time | Output |
|:--::--:--|:--::--::--:|:--::--:|:--::--:--|
| M1 | Understand Clearly concepts | 2h | 5 concept docs |
| M2 | Use it & write BRD/PRD | 3h | 4 practice examples |
| M3 | Create intro video | 4.5h | KR+EN MP4 videos |
| **Total** | | **9.5h** | **22 outputs** |

**Bonus**: Found and reported 4 bugs to the developers

^ Here's how the learning broke down. M1 was understanding the concept and documenting it. M2 was hands-on practice. M3 was creating the intro videos you might have already seen on the channel. And while learning, I found 4 bugs in the product and reported them — learning led to contribution.

---

## ❓ Without VibeLearn AI?

| Item | With VibeLearn AI | Without |
|:--::--:|:--::--::--::--::--::--:|:--::--::--:|
| Learning structure | AI auto-designs | Manual (1-2 days) |
| Progress tracking | Automated WorkLog | Irregular notes |
| Outputs | 22 textbook-quality docs | A few scattered notes |
| Reusability | Anyone can use immediately | Only you understand |
| Time | 9.5 hours | 3x+ for same quality |

^ The difference is stark. Without VibeLearn AI, achieving the same quality of output would have taken at least three times longer. And the textbook-quality documentation that others can actually use? That just doesn't happen without structure.

---

## 📁 What the Output Looks Like

```
Topics/Clearly-BRD-PRD/
├── 01-Product-Overview/       ← M1 outputs
│   ├── concepts/              ← 5 concept docs
│   └── guides/                ← usage guide
├── 02-BRD-PRD-Practice/       ← M2 outputs
│   └── examples/              ← 4 practice examples
└── 03-Clearly-Intro-Video/    ← M3 outputs
    ├── clearly-intro-kr.mp4   ← Korean video
    └── clearly-intro-en.mp4   ← English video
```

^ Here's the actual folder structure that came out of that learning journey. If I hand this folder to someone, they can start learning Clearly from scratch using the documentation I created. This is the core value of VibeLearn AI — your learning becomes the next person's starting point.

---

# Outro

---

## 🔁 Once You Learn It, Use It for Anything

```
Topic 1: Clearly App ✅ Complete
Topic 2: Remotion Video Creation ✅ Complete
Topic 3: VibeLearn AI itself 🔄 In Progress
Topic 4: (what you'll learn next) ...
```

**What accumulates**:
- Your knowledge base (Topics/ folder)
- Your AI collaboration skills
- A growing collection of textbook-quality outputs

^ One of the best things about VibeLearn AI is that it compounds. Once you're comfortable with the workflow, you apply it to every new topic you want to learn. Over time, you build a library of documentation that represents everything you've learned — organized, searchable, and shareable.

---

## 💡 As You Get More Comfortable: Higher Quality

**Basic (first time users)**:
```
"I want to learn Python basics."
```

**Advanced (once comfortable)**:
```
"I want to learn Python basics.
Background: 2 years JavaScript experience, data analysis goal,
3 weeks available, 2 hours/day."
```

More context → AI generates a more precise Roadmap + personalized plan

^ Starting with a simple sentence is the best approach for beginners. As you get comfortable with VibeLearn AI, you can provide richer context upfront, and the AI will create even more precise roadmaps and learning plans. But there's no need to figure this out before you start — just get going.

---

## 🚀 Start in 30 Minutes

**3 steps to your first learning session**:

1. **Get the repo** (5 min)
   ```
   git clone https://github.com/solkit70/VibeLearn-AI.git
   ```

2. **Open in your AI tool** (2 min)
   - VS Code + Copilot, Claude Code, or Cursor

3. **Say it** (the rest of the time)
   ```
   "I want to learn ___."
   ```

^ You can start in 30 minutes. Clone the repo, open it in your AI tool, and say what you want to learn. That's it. The link is in the description below.

---

## 📝 Today's Summary

| Item | Details |
|:--::--:|:--::--::--:|
| **What is it?** | A learning methodology with AI as partner |
| **Core design** | Say what you want → AI automates everything |
| **4 Phases** | Setup → Roadmap → Daily learning → Complete |
| **Output** | Textbook-quality docs (reusable by others) |
| **Case** | 9.5h → 22 outputs + 2 YouTube videos |
| **Get started** | github.com/solkit70/VibeLearn-AI |

^ Here's a quick recap. VibeLearn AI is a learning methodology that uses AI as your partner. The design is intentionally simple — say what you want to learn, AI handles the rest. The output is structured documentation that anyone can use. And the case study shows it works.

---

## 🤝 Building VibeLearn AI Together

**Share your case with the community**:
- Learned something with VibeLearn AI? → Share on GitHub Issues
- Feedback and improvement ideas welcome
- Something not working automatically? → Report on Issues — we'll fix it

**GitHub**: github.com/solkit70/VibeLearn-AI
**Email**: solkit70@gmail.com

^ VibeLearn AI is a collaborative project. If you use this methodology and get results, please share your case on GitHub Issues — it becomes a learning resource for others working on the same topic. And if something isn't automating the way it should, let us know — the whole point is that it should "just work."

---

## 👋 Wrapping Up

**One thing to do today**:

> Pick one topic you've been wanting to learn.
> Open your AI tool.
> And say:
>
> **"I want to learn ___."**

That one sentence is the beginning of your first VibeLearn AI learning session.

^ Thanks for watching! If this was helpful, please like and subscribe — it really helps the channel. Drop any questions in the comments, and I'll see you in the next video!
