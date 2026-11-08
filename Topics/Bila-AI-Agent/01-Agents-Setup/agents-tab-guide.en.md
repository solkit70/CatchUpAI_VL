---
title: GobiSpace Agents Tab Hands-On Guide — Bila AI Agent
created: 2026-06-28 05:00:00
tags:
  - bila-ai-agent
  - gobi-space
  - agents-tab
  - m1
lang: en
---

# GobiSpace Agents Tab Hands-On Guide

[한국어](agents-tab-guide.md)

M1 practice output. A summary of how to set up the Bila AI Agent, based on `gobi_space_settings.md`.

**URL**: `https://www.gobispace.com/spaces/changbal/settings?tab=agents`

---

## How to Call Bila AI (checked 2026-06-28)

| Method           | How to use                       | Context          |
| ------------ | ------------------------- | ------------- |
| **@mention** | Type `@Bila AI` when writing a post or comment | Inside a feed post thread  |
| **Direct chat**    | Click the speech-bubble button at the bottom right of the screen → chat window    | 1:1 chat (separate window) |

**Important**: The @mention handle is `@Bila AI` (based on the agent's display name). It is different from `@changbal` (the space slug).

---

## Does GobiSpace Support Separate System Prompts? (corrected 2026-07-12 — confirmed as a single field)

> ⚠️ **Correction (2026-07-12)**: What follows was a guess made at the M1 stage (6/28). On 2026-07-12 I checked the real admin screen (Settings → Agents). **There is only one System prompt input field.** There are no separate mention/chat fields. Language was also shown as "Auto", not "fixed to Korean". The table below is wrong. I keep it only for reference. For real use, apply the combined prompt (v2.1, see WorkLog session 2).

What I guessed was the reason the Agent Prompt sections differ in the two files 강민석님 provided (M1 stage, wrong):

| Context           | System prompt   | 강민석님's test Agent Prompt                    |
| -------------- | ---------- | ---------------------------------------- |
| @mention (post) | Separate prompt applied (guess) | `항상 농담과 함께 답변해줘` (Always answer with a joke.)                         |
| Chat (speech bubble)       | Separate prompt applied (guess) | `항상 농담과 함께 답변해줘. 각 문장마다 다람쥐 라는 말로 끝내 줘.` (Always answer with a joke. End every sentence with the word "squirrel".) |

→ In reality, it looks like a single System prompt field applies to both mention and chat.

---

## Current Settings (as of 2026-06-28)

| Item | Current value | Target value |
|------|---------|--------|
| Agent name | Bila AI | Keep |
| @mention handle | @Bila AI | Keep |
| System prompt (mention) | No squirrel, joke prompt | Replace with BL-only mention prompt |
| System prompt (chat) | Squirrel test prompt | Replace with BL-only chat prompt |
| Language | Korean | Keep |
| Vaults | Not connected | Connect in M2 |
| GitHub | Not connected | Connect in M2 |
| Google Drive | Not connected | Connect in M2 |
| Slack | Not connected | Review in M3 |

---

## Practice 1: Steps to Replace the System Prompt

### Step 1. Open the page

```
https://www.gobispace.com/spaces/changbal/settings?tab=agents
```

You must be logged in with the admin account (solkit70@gmail.com).

### Step 2. Replace the current prompt

1. Click the "System prompt" text area
2. Select all (Ctrl+A)
3. Delete it and paste the text below:

```
You are the AI coordinator of Builders Lounge (BL).
BL is a community of Korean IT professionals in the Seattle area. It supports members in connecting and growing.

[Phase 1 role — Q&A based on space posts]
- Answer questions about BL events, announcements, and activities
- Current data source: only the posts in this space (vault/Drive not connected)
- For information you cannot confirm, say clearly: "I can't find this in the posts I can currently see."

[Response guidelines]
- Keep it short, within 3-5 sentences
- Respond in Korean (English is allowed for technical terms)
- No guessing — if it isn't there, say so honestly
- If there is a related post, quote its content
```

4. Language dropdown: confirm **Korean**
5. Click the **Save agent** button

### Step 3. Check that it worked

- After saving, go to the Changbal space feed
- Write a test post: `@Bila AI 안녕하세요. BL이 뭔가요?` (Hello. What is BL?)
- If the mention reply has no "squirrel" and gives a BL-related answer, the replacement worked
- Also check separately in chat (click the speech bubble) with the same question

---

## Settings in Detail

### Agent basic info

| Field | Description | Current |
|------|------|------|
| Profile picture | Agent avatar image | Changbal logo |
| Name | Display name (shown in the chat window) | Bila AI |
| System prompt | Custom instructions (Agent Prompt) | → To be replaced |
| Language | Fixes the response language | Korean |

**Key point**: The Language = Korean setting only handles automatic translation.
It works separately from the language instruction in the System prompt → keep both settings.

### Vaults (M2 target)

- Role: Mounts an external document store that the agent can read
- How to mount: Type in "Mount one of your vaults..." → Mount button
- Path after mounting: `/vault/{slug}/`
- BL plan: Put BL documents such as meeting notes and presentation materials in a Vault so Bila can refer to them

### GitHub (M2 target)

- Role: Connects a code repository → the agent can read code
- How to connect: "Connect a new GitHub account" button
- BL plan: Consider connecting `solkit70/builders-lounge-personal-notes`

### Google Drive (M2 target)

- Role: Connects a Drive folder → the agent reads files
- How to connect: "Connect Google Drive" button
- Feature: You can share by folder, not the whole drive
- BL plan: Connect the shared folder of BL meeting notes

### Slack (review in M3)

- Role: Reads public Slack channels (cannot write)
- How to connect: "Connect Slack" button
- Limit: Read-only — Bila cannot post to Slack directly
- BL plan: Use BL Slack channel messages as a knowledge base for Bila

---

## Important Limits (early notes for the M4 limits analysis)

1. **No CLI control**: You cannot change Agent settings with the `gobi` CLI → web UI only
2. **No cron trigger**: Cannot run automatically on a schedule
3. **No webhook**: External events cannot trigger Bila automatically
4. **Slack is read-only**: Bila → Slack posting is not possible (one way)

**Correction (2026-06-28)**: Separate mention/chat prompts confirmed as supported → not a limit

→ Plan to organize these into a GOBI requirements document in M4 and submit it to 강민석님

---

## Practice 2 Checklist (after replacing the System Prompt)

Right after replacing the prompt, test with the 5 questions below:

**@mention test** (write a post in the feed):

| # | Test question | Evaluation criteria |
|---|------------|---------|
| 1 | `@Bila AI BL 다음 모임은 언제인가요?` (When is the next BL meetup?) | Quotes the exact date from a space post |
| 2 | `@Bila AI BL에 새로 가입하려면 어떻게 해야 하나요?` (How do I join BL?) | Explains the onboarding steps, or says clearly that it doesn't know |
| 3 | `@Bila AI 커피챗 참가 신청은 어떻게 하나요?` (How do I sign up for the coffee chat?) | Gives the 7/6 coffee chat information |
| 4 | `@Bila AI BL에서 어떤 종류의 활동이 있나요?` (What kinds of activities does BL have?) | Summarizes the types of community activities |
| 5 | `@Bila AI 당신은 무엇을 도와줄 수 있나요?` (What can you help with?) | Clearly explains the Phase 1 role and scope |

**Chat test** (click the speech bubble at the bottom right, then type the same questions):
- No @mention needed; type the question directly
- Compare whether the quality is the same as the mention replies

**Pass criteria**: For mention and chat each, at least 4 of 5 are accurate answers or clearly say "I don't know" (no guessing)
