---
title: Slack Connection Guide - Bila AI Agent
created: 2026-07-26 07:15:04
tags:
  - bila-ai-agent
  - slack
  - m2
---

## Purpose

This guide records the Slack connection flow for Bila AI Agent. Slack is a required Builders Lounge data source because most online Builders Lounge conversation happens in Slack. In GobiSpace, Slack is read-only: the agent can read messages from public channels where the Gobi Slack app has been invited, but the agent cannot post to Slack.

Source context: [[Ingest/CatchUpAI_VL/Topics/Material_For_Topics/Bila_AI_Agent/gobi_space_settings#3-5. Slack 연동|Changbal Space settings - Slack]] and the user-provided screenshots from 2026-07-26.

## Target Environment

| Item | Value |
|------|-------|
| GobiSpace | Changbal |
| Agent | Bila AI |
| Settings location | `Settings -> Agents -> Slack` |
| Slack workspace | `changbal.slack.com` |
| Slack plan shown | Pro Plan |
| Login email shown | `douggy.park@yahoo.com` |
| Permission model | Read-only |

## Observed Flow

### Step 1. Start From GobiSpace Agents

In `Settings -> Agents`, the Slack section currently shows `No Slack workspace connected`. The screen explains that the Gobi Slack app must be installed into the Slack workspace and that the Gobi bot must then be invited to channels the agent should read.

Observed text:

> Connect a Slack workspace so the agent can read messages from public channels it has been invited to. Read-only - the agent cannot post to Slack.

Action: click `Connect Slack`.

### Step 2. Slack Asks For Workspace URL

Slack opens a sign-in screen with the prompt `Sign in to your workspace` and asks for the workspace Slack URL. The correct workspace from the Slack app screenshot is `changbal.slack.com`.

Important input note: do not submit a duplicated URL such as `changbal.slack.com.slack.com`. If Slack or the browser appends a suffix unexpectedly, clear the field and enter only the canonical workspace URL shown in Slack: `changbal.slack.com`.

Action: enter `changbal.slack.com`, then click `Continue`.

### Step 3. Confirm Workspace URL From Slack App If Needed

The Slack desktop app workspace menu shows:

| Field | Value |
|------|-------|
| Workspace name | Changbal |
| Workspace URL | `changbal.slack.com` |
| Plan | Slack Pro Plan |

Use this screen as the source of truth when the Slack sign-in page asks for the workspace URL.

### Step 4. Slack Sends Email Code

After continuing, Slack shows `We emailed you a code` and says the code was sent to `douggy.park@yahoo.com`. The page contains six code boxes and options to open Gmail or Outlook. It also offers `Request a new code` if the code does not arrive.

Action pending: enter the emailed code to continue Slack authorization.

## Current Status

| Check | Status | Notes |
|------|--------|-------|
| GobiSpace Slack section found | Done | Shows no Slack workspace connected. |
| `Connect Slack` clicked | Done | Redirected to Slack sign-in. |
| Workspace URL identified | Done | `changbal.slack.com`. |
| Email verification code requested | Done | Sent to `douggy.park@yahoo.com`. |
| PIN/code entered | Blocked | User reports the email code is not arriving. |
| Gobi Slack app installed | Pending | Expected after code verification and authorization. |
| Bot invited to target public channels | Pending | Required before Bila can read messages. |
| Bila Slack retrieval test | Pending | Run after app install and bot invitation. |

## Authorization Error - invalid_team_for_non_distributed_app

After the email code was entered, Slack showed:

```text
Something went wrong when authorizing this app.

Error details
invalid_team_for_non_distributed_app
```

Slack's OAuth documentation defines `invalid_team_for_non_distributed_app` as the case where someone attempts to install or authorize an undistributed Slack API app on a team where the app was not created. In this context, the most likely interpretation is that the Gobi Slack app is still a non-distributed/development Slack app, or it is only installable in the Gobi team's own Slack workspace, not in the Builders Lounge `Changbal` workspace.

This is not caused by the user entering the wrong PIN. The PIN succeeded enough to reach the app authorization step, then Slack rejected the app/workspace combination.

### Likely Owner

This needs action from the GOBI/Slack app developer, not from the Changbal workspace admin alone. The developer likely needs to either:

- enable Slack app distribution for the Gobi Slack app,
- add/install the app specifically for the `Changbal` workspace through the correct development flow,
- or provide a workspace-specific install link/app configuration that targets `changbal.slack.com`.

### Developer Report Draft

```text
GobiSpace Connect Slack fails for Changbal workspace.

Flow:
1. GobiSpace Changbal -> Settings -> Agents -> Slack -> Connect Slack
2. Slack asks for workspace URL
3. Entered changbal.slack.com
4. Slack sent email code to douggy.park@yahoo.com
5. After entering the code, Slack showed:
   "Something went wrong when authorizing this app."
   Error details: invalid_team_for_non_distributed_app

Interpretation from Slack OAuth docs:
This error occurs when an undistributed Slack API app is authorized/installed on a workspace where the app was not created.

Could you check whether the Gobi Slack app is configured for distribution or otherwise installable on the Changbal Slack workspace?
```

## Email Code Not Arriving - Triage

If the Slack email code does not arrive, treat this as an authentication blocker before debugging Gobi itself.

1. Wait 2-5 minutes and check `Spam`, `Junk`, `Promotions`, and `All Mail` for `Slack`, `code`, `sign in`, or `douggy.park@yahoo.com`.
2. On the Slack code screen, click `Request a new code` once. Avoid repeated rapid requests because older codes may become invalid.
3. Confirm the workspace URL is exactly `changbal.slack.com`. If the page contains `changbal.slack.com.slack.com`, go back to `Try entering a workspace URL` and re-enter only `changbal.slack.com`.
4. Try signing in to `changbal.slack.com` directly in the browser first. If direct Slack login also fails to send the code, the problem is Slack account/email delivery rather than Gobi.
5. In the Slack desktop app, confirm the current signed-in account is the same account that receives email at `douggy.park@yahoo.com`. If the workspace is actually tied to another email, use that email/session for authorization.
6. Try an incognito/private browser window to avoid stale Slack sessions or browser autofill state.
7. If the email still does not arrive, use Slack's `Find your workspaces` flow to confirm which email address Slack associates with the `Changbal` workspace.

Escalation condition: if direct Slack login works but the Gobi Connect Slack flow still cannot deliver a code, record this as a Gobi Slack OAuth onboarding issue and share the exact timestamp, workspace URL, target email, and screenshot sequence with the GOBI developer.

## Post-Authorization Checklist

- [ ] Enter Slack email code.
- [ ] Approve/install the Gobi Slack app for the `Changbal` workspace.
- [ ] Return to GobiSpace `Settings -> Agents -> Slack`.
- [ ] Confirm the Slack section no longer shows `No Slack workspace connected`.
- [ ] Invite the Gobi bot to the public Builders Lounge Slack channels Bila should read.
- [ ] Ask Bila a question whose answer exists only in Slack and record whether it uses Slack context.

## Verification Question Template

Use a question with an answer known to exist in a Slack public channel and not in GitHub, Drive, or GobiSpace posts.

```text
Slack의 #[채널명] 채널에서 최근 논의된 [주제]에 대해 Bila가 확인할 수 있는 내용을 요약해 주세요. 근거가 되는 Slack 메시지나 채널명을 함께 말해 주세요.
```

Pass condition: Bila identifies Slack channel context and does not fabricate content when it cannot access a channel.
