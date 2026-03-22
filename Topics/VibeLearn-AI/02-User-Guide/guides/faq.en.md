# VibeLearn AI — FAQ & Troubleshooting
> **[<- Korean Version](faq.md)**


**Created**: 2026-02-26
**Audience**: People who are new to VibeLearn AI or stuck on something

---

## Frequently Asked Questions (FAQ)

---

### Q1. Can't it be used without AI?

**A**: Correct. AI is an essential component of VibeLearn AI.

Why:
- Roadmap generation: AI analyzes Topic information to create a customized plan
- Daily Learning: AI reads Roadmap+WorkLog and creates today's plan
- Real-time learning support: Instant answers when you get stuck

**Recommended AI tools** (ones that can read and write files directly):
- **VS Code + GitHub Copilot** — most common, install Copilot extension in VS Code
- **VS Code + Claude Code** (Extension) — Claude-based, powerful file manipulation
- **Cursor** — AI-integrated editor (VS Code-based)

> Web-based AI (ChatGPT web, Claude.ai) can't read and write files directly, requiring copy/paste which is inefficient. Using editor-integrated AI tools is strongly recommended.

---

### Q2. Can it be used without GitHub?

**A**: Yes. GitHub is optional.

Without GitHub:
- All work can proceed in a local folder
- WorkLog, outputs all saved locally
- No backup or sharing features

With GitHub:
- Version control (can revert mistakes)
- Share outputs and contribute to community
- Access from other devices

**Recommendation**: If you've never used GitHub, try learning GitHub basics alongside this Topic.

---

### Q3. Can it be used for any topic?

**A**: Yes. Applicable to any field, not just technical topics.

Topics it works well for:
- Programming languages (Python, JavaScript, etc.)
- Frameworks & tools (React, Docker, Git, etc.)
- AI/ML tools (Claude API, LangChain, etc.)
- Non-technical fields (English writing, financial planning, cooking skills, etc.)

Key: Applicable to anything you want to learn and approach systematically

---

### Q4. How do I determine the learning period?

**A**: You don't have to. AI identifies it automatically through conversation.

Process:
1. "I want to learn Python basics." → AI asks about your learning background
2. AI suggests an appropriate period and asks for confirmation
3. Provide feedback: "too short / appropriate / too long"
4. User makes final decision

Reference guidelines:
- Simple tool usage: 3–7 days
- Framework/library: 2–4 weeks
- Complex system: 1–3 months

---

### Q5. Can I modify files in the templates/ folder?

**A**: Strongly recommended not to modify.

Why:
- templates/ is the "universal original" — reusable for any Topic
- If modified, you'll start your next Topic with a broken template

Alternative:
- If modification is needed, modify a copy in the `vl_prompts/` folder
- Always keep templates/ in its original state

---

### Q6. Do I really need to write the WorkLog every day?

**A**: Writing it every day you study is strongly recommended.

Without it:
- AI can't identify previous progress in the next session
- High likelihood of re-learning the same content
- Without Daily Retrospective, learning method doesn't improve

How to write it:
- AI automatically creates and fills the WorkLog file
- If you want to edit it directly, open the file and add to it

---

### Q7. Can multiple Topics be studied simultaneously?

**A**: Technically possible, but not recommended.

Why:
- Focusing on one Topic allows for deeper learning
- Running multiple Topics in parallel makes it harder to achieve DoD for each
- AI also struggles to manage context across multiple Topics simultaneously

Exception:
- Two complementary Topics (e.g., Python + Docker) can run in parallel
- However, each Topic should be handled in separate chat sessions

---

### Q8. Isn't sharing the output folder with others not allowed?

**A**: Sharing is the core purpose of VibeLearn AI!

How to share:
1. Upload to GitHub as a public repository
2. Share documents on a blog/Notion
3. Share the learning process as a YouTube video (like the Clearly case)

Caution:
- Review WorkLogs containing personal information before sharing
- Confirm no sensitive information like API keys or passwords

---

### Q9. The AI-generated Roadmap is too hard or too easy. What do I do?

**A**: The Roadmap can be modified.

How:
1. Open the Roadmap file and edit it directly
2. Ask AI: "M2 is too hard, can you adjust it to be easier?"
3. Split or merge modules

Important:
- The Roadmap is a starting point, not an absolute plan
- It's natural to adjust as you learn

---

### Q10. Can I skip the Daily Retrospective?

**A**: Skipping reduces the core value of learning.

Why:
- Retrospective is meta-learning that improves the learning method itself
- "Why did today go well?", "Why did I get stuck?" → makes the next session more efficient
- "The power of repetition" insight in the Clearly case was also thanks to Retrospective

Invest at least 5 minutes:
```markdown
## Daily Retrospective
- What went well? (one line)
- What could be improved? (one line)
- Tomorrow's focus (one line)
```

---

### Q11. I want to proceed in English.

**A**: Fully supported.

How:
1. Use `templates/*.en.md` files (English version templates)
2. Tell AI "I'll proceed in English"
3. Write WorkLog and outputs in English

English versions of all templates:
- `templates/roadmap_prompt_template.en.md`
- `templates/daily_learning_prompt.en.md`
- `templates/topic_starter.en.md`

---

### Q12. What do I do when the original technology/software gets updated during learning?

**A**: Follow the CVL (Continuous Vibe Learning) process.

How:
1. Run `git fetch` check at the start of every learning session
2. Analyze changes (ask AI)
3. Reflect immediately or conduct a separate update session based on scale
4. Record sync content in WorkLog

Detailed guide: Refer to the CVL section in [key-concepts.en.md](../../01-System-Overview/concepts/key-concepts.en.md)

---

### Q13. What do I need to do after cloning from GitHub?

**A**: You need a 3-step initial setup.

```bash
# 1. Install git hooks (activate automation pipeline)
powershell -ExecutionPolicy Bypass -File scripts/install-hooks.ps1

# 2. Install Python packages
pip install -r requirements.txt

# 3. (Optional) Set ANTHROPIC_API_KEY - for auto-translation feature
$env:ANTHROPIC_API_KEY = "sk-ant-..."
```

Basic learning features work without this setup. However, the automation pipeline (translation/sync/validation) won't run on git commit.

---

### Q14. Is translation automatic?

**A**: Yes, it translates automatically on git commit — provided `ANTHROPIC_API_KEY` is set.

How it works:
1. `git commit` runs → pre-commit hook starts automatically
2. If `CLAUDE.md` was changed → `translate-claude.py` calls Claude API to translate
3. Translation result saved to `CLAUDE.en.md`
4. Commit completes

**If translation fails**: Only a warning message is shown and commit continues (non-blocking design).
Commit is not blocked even if you have no API key or no credits.

---

### Q15. What happens if I don't have ANTHROPIC_API_KEY?

**A**: Only translation is skipped — commit completes normally.

| Situation | Result |
|-----------|--------|
| API key present, translation succeeds | `CLAUDE.en.md` auto-updated + commit complete |
| No API key or failure | ⚠️ Warning message → commit continues |
| sync/validate fails | ❌ Commit aborted (unrelated to API key) |

Translation is a convenience feature and doesn't affect learning progress.
If you need English docs, translate manually or set up the API key later.

---

## Troubleshooting

---

### Problem 1: AI won't create folders

**Cause**: AI tool doesn't have file system access permissions

**Solution**:
```bash
# Windows PowerShell
$topic = "Python-Basics"
mkdir "Topics/$topic/vl_prompts", "Topics/$topic/vl_roadmap", "Topics/$topic/vl_worklog", "Topics/$topic/vl_materials" -Force

# macOS/Linux Bash
topic="Python-Basics"
mkdir -p "Topics/$topic"/{vl_prompts,vl_roadmap,vl_worklog,vl_materials}
```

---

### Problem 2: The Roadmap file is too long

**Cause**: Normal. The Roadmap is a full learning plan so it can be long.

**Solution**:
- Keep only the current module section open
- Ask AI: "Summarize just the M1 section"
- Use VS Code's code folding feature

---

### Problem 3: WorkLog keeps disappearing (AI keeps creating new ones)

**Cause**: Designed to create new files per day — normal behavior

**Solution**:
- Same day, same module → append to existing file
- Tell AI: "Add to the existing WorkLog"

---

### Problem 4: "This methodology doesn't seem to fit my learning"

**Cause**: No methodology is perfect for everyone

**Solution**:
- Record "What part of this method felt uncomfortable?" in Daily Retrospective
- Evolve into your own approach by modifying the uncomfortable parts
- VibeLearn AI is a guideline, not a rule

---

### Problem 5: "AI isn't handling steps it should handle automatically"

**Cause**: Not operating as designed

**Solution**:
- VibeLearn AI is designed so that saying "I want to learn" starts everything automatically
- If a specific step isn't happening automatically, it's not working as intended
- Please report to [GitHub Issues](https://github.com/solkit70/VibeLearn-AI/issues) → will be reviewed and fixed

Include in report:
1. AI tool being used (VS Code + Copilot, Claude Code, Cursor, etc.)
2. Which step you got stuck on
3. What you entered and AI's response

---

**Author**: Claude with VibeLearn AI
**Last updated**: 2026-02-27
