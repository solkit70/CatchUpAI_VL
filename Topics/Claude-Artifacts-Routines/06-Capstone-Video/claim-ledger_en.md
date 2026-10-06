---
title: "Claude Artifacts and Routines — Scene-by-Scene Claims and Evidence Ledger v2"
created: "2026-10-04 07:30:16"
author:
  - "Codex"
tags:
  - remotion
  - claim-ledger
  - claude-artifacts-routines
status: "review-pending"
---

## Scope

This ledger maps every slide-plan scene S01–S28 to claims C01–C28. Public candidates are verified experiences, minimal exercises, and explanatory diagrams. Internal materials and original private-account information are not moved into production assets. Even public-safe material requires personal-information masking and a boundary review. User-spoken quotations were checked against their original vault entries; exact lines intended for the public video are preserved below.

## Scene mapping in v2

The scenes were reorganized for the 2026-10-04 slide plan v2 (23 scenes). The “Scene” rows below use v1 numbering; this table maps them to v2. The evidence and verification scope did not change; two new claims, C29 and C30, were added.

| v2 scene | Evidence | v2 scene | Evidence |
|---|---|---|---|
| S01 | C17 · C18 | S13 | C16 |
| S02 | C04 | S14 | C17 · **C35** |
| S03 | C01 · C02 · C05 | S15 | C17 · C18 |
| S04 | C03 · **C38** | S16 | C19 |
| S05 | C05 · C03 | S17 | C20 · C29 |
| S06 | C04 · **C33** · C09 | S18 | C30 |
| S07 | C09 · C04 | S19 | C21 · C22 · C28 · **C36** |
| S08 | C09 · C08 | S20 | C31 · C32 |
| S09 | C11 · **C34** · **C37** | S21 | C24 · C25 · C23 |
| S10 | C12 | S22 | C26 · C06 |
| S11 | C13 · C14 · **C36** | **S23 (new in v4)** | C36 · C09 · C16 · C34 · C37 · C18 · C13 |
| S12 | C15 | S24 | C27 · **C36** |
|  |  | S25 | C28 |

**v3 (2026-10-06):** A new S20 was added; v2 scenes S20–S23 shifted to S21–S24. Claims C31 and C32 were added.

**v4 (2026-10-06 narration review):** S23 (“Five things I use for other work”) was added, moving the conclusion to S24 and the outro to S25. The table shows v4 numbering. New claims C33–C36 are descriptions and insights from the user’s review that day, preserved in the [[Journal/2026-10-06#Artifacts · Routines 영상 나레이션 리뷰 — 일을 시키는 사람도 배워야 한다 (구술 원문)|original spoken entry of Oct 6]].

C10 (the different conditions in the Sep 13 and Sep 27 sharing records) was removed from the v2 narration because its cause was not established and it offered beginners no action rule. The S08 screen label “May vary by account and date” and the upload description communicate its scope.

The S07 statement “an instruction appeared in the logged-out window” comes from A1’s Sep 13 incognito observation (“Sign in to view this page”) in the [inventory](../01-Inventory-and-Questions/guides/inventory_en.md#six-artifacts), and the “empty shell for anonymous visitors” explanation in the [sharing experiment](../02-Artifacts-Sharing-and-Versions/guides/sharing-matrix_en.md#answer-to-question-1). The test date was Sep 13; it checked the Sep 3 meeting-day report that link sharing “did not work.”

## Verified original user quotations

> I had always thought that you needed to know enough to tell AI what to do in order to give it good instructions.... In this case, AI simply found and applied features I knew nothing about on its own.

Source: [[Journal/2026-09-01#AI가 스스로 찾아낸 기능 — 지시자의 사전 지식에 대해 (구술 원문)|user’s original spoken entry, Sep 1]]. S03 narrates the meaning; on-screen direct quotations should be short excerpts from this original.

> During the meeting, an idea came to me, so I made it on the spot and used it in the meeting......
> Something like that would have been unimaginable before.

Source: [[Journal/2026-09-03#9/3 하루 정리 (구술 원문)|user’s original spoken entry, Sep 3]]. Candidate direct quote for S04; narration paraphrases the experience.

## Corrections and unverified details found while reviewing records

- M2’s conclusion that comments were unavailable was corrected by the M3 test in which the author posted a comment. There is no test record for public-link visitors.
- M2’s observation of a public DB page with anonymous data blocked and M3’s rule for organization-only sharing may not represent the same conditions. The current general conclusion about sharing scope is withheld; retain the date with historical claims.
- M1/M2’s watch limit of five and M3’s watch limit of ten were recorded at different times. Do not present either as the current limit.
- Topic README says M2 took 45 minutes; M2 WorkLog says 55 minutes. Do not use total time spent or time-saved figures in the video.
- Do not misrepresent WBLP failure pushes as “no notifications.” Say that it took time to recognize them as an operational problem.
- Historical screenshots of environment settings, current run state, and email bodies are not in this folder. Follow the [capture request](capture-request_en.md).

## Official documents and public sources checked

On 2026-10-04, the [Claude Code Artifact documentation](https://code.claude.com/docs/en/artifacts) and [Routines documentation](https://code.claude.com/docs/en/routines) were accessed. They were used to check product scope, definitions, and comment-access conditions; the current public docs did not resolve differences in the local runtime contract’s DB-sharing rules. Past observations are not generalized into current account availability.

The public GitHub remote is `solkit70/CatchUpAI_VL`, branch `main`. Raw GET requests for the Topic README, sharing experiment, DB round trip, routine audit, local-vs-cloud guide, and playbook all returned HTTP 200. The [playbook page](https://github.com/solkit70/CatchUpAI_VL/blob/main/Topics/Claude-Artifacts-Routines/05-Usage-Patterns/guides/artifacts-routines-playbook.md) was also read. This confirms that the links are publicly accessible; it does **not** mean that conflicting claims in those documents were newly tested.

## Scene-by-scene evidence

### C01

**Scene:** S01. **Claim:** During work, a person encountered features they had not known through working with AI.

**Evidence type/date:** `[observed · user reflection]` 2026-09-01 and 09-03. **Sources:** [[Journal/2026-09-01#AI가 스스로 찾아낸 기능 — 지시자의 사전 지식에 대해 (구술 원문)|Sep 1 original user entry]] · [[Journal/2026-09-03#9/3 하루 정리 (구술 원문)|Sep 3 original user entry]].

**Scope and public conditions:** This is one person’s experience. It does not promise that every task will be reproduced successfully or that productivity will improve.

### C02

**Scene:** S02. **Claim:** The video explains decision criteria for requesting and checking the two features.

**Evidence type/date:** `[planning]` 2026-10-04. **Source:** [The playbook’s three questions](../05-Usage-Patterns/guides/artifacts-routines-playbook_en.md#1-what-should-you-build-ask-three-questions).

**Scope and public conditions:** The effect on viewers has not been measured. Present this as the video’s promise.

### C03

**Scene:** S03. **Claim:** The user recorded an experience in which AI found and used a tool while doing job-related work.

**Evidence type/date:** `[user-spoken reflection]` 2026-09-01. **Source:** [[Journal/2026-09-01#AI가 스스로 찾아낸 기능 — 지시자의 사전 지식에 대해 (구술 원문)|Sep 1 original user entry]].

**Scope and public conditions:** Do not generalize this into a claim that any task succeeds even if the user does not know the tools.

### C04

**Scene:** S04. **Claim:** A booth-status page was built during a meeting and used in that meeting.

**Evidence type/date:** `[user-spoken reflection · artifact record]` 2026-09-03 and 09-13. **Sources:** [[Journal/2026-09-03#9/3 하루 정리 (구술 원문)|Sep 3 original user entry]] · [inventory](../01-Inventory-and-Questions/guides/inventory_en.md#six-artifacts) · [candidate not yet a pattern](../05-Usage-Patterns/guides/patterns_en.md#candidates--not-yet-established-patterns).

**Scope and public conditions:** Actual use is recorded; comparative evidence that it worked better is not measured. Use a public-safe capture or anonymous diagram, not original internal event materials.

### C05

**Scene:** S05. **Claim:** A Claude Code Artifact is a result page; a Routine is an automatically executed task.

**Evidence type/date:** `[docs · exercise]` 2026-09-13, 09-27, and 10-04. **Sources:** [inventory](../01-Inventory-and-Questions/guides/inventory_en.md#six-artifacts) · [second-routine configuration](../04-Routines-Lab/guides/second-routine_en.md#configuration).

**Scope and public conditions:** Do not describe these as all features of ordinary Claude chat. Official documentation definitions were cross-checked on Oct 4.

### C06

**Scene:** S06. **Claim:** Frame a request using the goal, audience, and result to verify.

**Evidence type/date:** `[inference · suggestion]` 2026-10-04. **Sources:** [the playbook’s three questions](../05-Usage-Patterns/guides/artifacts-routines-playbook_en.md#1-what-should-you-build-ask-three-questions) · [candidates not yet patterns](../05-Usage-Patterns/guides/patterns_en.md#candidates--not-yet-established-patterns).

**Scope and public conditions:** This is a sample request, not a prompt proven superior by comparative testing.

### C07

**Scene:** S07. **Claim:** Published/edited version and sharing state should be checked separately.

**Evidence type/date:** `[observed · documentation]` 2026-09-13 and 09-25. **Sources:** [inventory](../01-Inventory-and-Questions/guides/inventory_en.md#six-artifacts) · [latest shared-version pattern](../05-Usage-Patterns/guides/patterns_en.md#6-set-shared-links-to-the-latest-version-and-verify-in-incognito).

**Scope and public conditions:** Capture the current UI before describing its exact details. This work did not create or change public links.

### C08

**Scene:** S08. **Claim:** The user learned a criterion for separating a static page for sharing from a tool for editing data.

**Evidence type/date:** `[observed · pattern]` 2026-09-13 and 09-27. **Sources:** [inventory](../01-Inventory-and-Questions/guides/inventory_en.md#six-artifacts) · [sharing experiment answer](../02-Artifacts-Sharing-and-Versions/guides/sharing-matrix_en.md#answer-to-question-1) · [the playbook’s three questions](../05-Usage-Patterns/guides/artifacts-routines-playbook_en.md#1-what-should-you-build-ask-three-questions).

**Scope and public conditions:** This is a historical case and design criterion. Do not treat all database sharing rules as if they had one condition.

### C09

**Scene:** S09. **Claim:** On Sep 13, an anonymous window could open the HTML of a public DB page but could not access its data.

**Evidence type/date:** `[observed]` 2026-09-13. **Source:** [sharing experiment result](../02-Artifacts-Sharing-and-Versions/guides/sharing-matrix_en.md#answer-to-question-1).

**Scope and public conditions:** Based on the platform dialog and user capture at that time. Data access from another signed-in account was not tested.

### C10

**Scene:** S10. **Claim:** Documentation and publish records from Sep 27 stated organization-only sharing constraints for `db`, `user`, and `assets`.

**Evidence type/date:** `[documentation · publish record]` 2026-09-27. **Sources:** [capability selection table](../03-Artifacts-Capabilities-Lab/concepts/capability-selection-table_en.md#sharing-limits) · [minimal examples](../03-Artifacts-Capabilities-Lab/guides/lab-log_en.md#published-examples) · [sharing experiment](../02-Artifacts-Sharing-and-Versions/guides/sharing-matrix_en.md#answer-to-question-1).

**Scope and public conditions:** The conditions differ from M2. The cause—account, version, or contract change—was not established. Do not generalize as a rule for every current account.

### C11

**Scene:** S11. **Claim:** There is a record of changing the shared version of the event guide to Latest on Sep 25.

**Evidence type/date:** `[observed record]` 2026-09-07 and 09-25. **Source:** [latest shared-version pattern](../05-Usage-Patterns/guides/patterns_en.md#6-set-shared-links-to-the-latest-version-and-verify-in-incognito).

**Scope and public conditions:** Use the later confirmation rather than the Sep 13 “toggle not visible” note. A new capture is needed to verify what recipients currently see.

### C12

**Scene:** S12. **Claim:** A person incremented the value 11 written by AI twice to 13, and AI read it.

**Evidence type/date:** `[observed]` 2026-09-27. **Source:** [round trip complete](../03-Artifacts-Capabilities-Lab/guides/db-roundtrip_en.md#round-trip-complete).

**Scope and public conditions:** `counter/main`, v2→v4. Do not present the page’s current state as the historical moment.

### C13

**Scene:** S13. **Claim:** After the person’s edit, the AI’s stale v2 write was rejected and nothing was written.

**Evidence type/date:** `[observed]` 2026-09-27. **Sources:** [round trip complete](../03-Artifacts-Capabilities-Lab/guides/db-roundtrip_en.md#round-trip-complete) · [what was learned](../03-Artifacts-Capabilities-Lab/guides/db-roundtrip_en.md#what-this-shows).

**Scope and public conditions:** A real person/AI conflict; server was at v4. Specific to the session `ArtifactData` path.

### C14

**Scene:** S14. **Claim:** After rereading v4 and writing against that version, value 14 was saved at v5.

**Evidence type/date:** `[observed]` 2026-09-27. **Sources:** [round trip complete](../03-Artifacts-Capabilities-Lab/guides/db-roundtrip_en.md#round-trip-complete) · [what was learned](../03-Artifacts-Capabilities-Lab/guides/db-roundtrip_en.md#what-this-shows).

**Scope and public conditions:** The record notes that page-side writes do not use the same guard. Loss of increments under multi-user simultaneous clicks is a documentation warning, not a multi-user experiment.

### C15

**Scene:** S15. **Claim:** Examples for user info, images, comments, and multiple files were published and checked in the author’s view.

**Evidence type/date:** `[observed]` 2026-09-27. **Source:** [minimal-example lab](../03-Artifacts-Capabilities-Lab/guides/lab-log_en.md#published-examples).

**Scope and public conditions:** Checks from another account/incognito were skipped. Multiple files are not a capability name.

### C16

**Scene:** S16. **Claim:** The “comments unavailable” conclusion was corrected after an author comment and Send to Claude were tested.

**Evidence type/date:** `[observed · correction]` 2026-09-13 → 09-27. **Sources:** [minimal-example lab](../03-Artifacts-Capabilities-Lab/guides/lab-log_en.md#published-examples) · [M5 retrospective](../vl_worklog/20260927_M5_Claude-Artifacts-Routines.md#daily-retrospective).

**Scope and public conditions:** Distinguish success by the author from behavior for public-link visitors or users in another organization. Current official documentation also says that a visitor with only a public link cannot comment.

### C17

**Scene:** S17. **Claim:** The WBLP job routine was configured for recurring checks and conditional email.

**Evidence type/date:** `[configuration · observation]` 2026-09-02 and 09-21. **Sources:** [routine summary](../04-Routines-Lab/guides/wblp-routine-audit_en.md#in-one-sentence) · [run history](../04-Routines-Lab/guides/wblp-routine-audit_en.md#run-history-observed-in-session-logs).

**Scope and public conditions:** This is a work-based learning job-search case, not current employment or application advice.

### C18

**Scene:** S18. **Claim:** Runs on Sep 7, 14, and 21 all failed; “unable to check” pushes were sent, but no job-alert email was sent.

**Evidence type/date:** `[observed logs]` 2026-09-07, 09-14, and 09-21. **Source:** [run history](../04-Routines-Lab/guides/wblp-routine-audit_en.md#run-history-observed-in-session-logs).

**Scope and public conditions:** Do not say there were no pushes. The observation is that looking only at email made an empty result indistinguishable from a failure.

### C19

**Scene:** S19. **Claim:** The same request worked locally and was blocked by policy in the cloud.

**Evidence type/date:** `[observed]` 2026-09-21. **Source:** [diagnosis](../04-Routines-Lab/guides/wblp-routine-audit_en.md#diagnosis--how-the-cause-was-isolated).

**Scope and public conditions:** Determined from `EGRESS_BLOCKED`/CONNECT rejection and local HTTP 200 at that time. This does not mean every failure is an allowlist issue.

### C20

**Scene:** S20. **Claim:** After changing the environment, the manual recovery and Sep 28 scheduled result email were confirmed.

**Evidence type/date:** `[observed · user receipt confirmation]` 2026-09-21, 09-28, and 09-29. **Sources:** [run history](../04-Routines-Lab/guides/wblp-routine-audit_en.md#run-history-observed-in-session-logs) · [first scheduled run after recovery](../04-Routines-Lab/guides/wblp-routine-audit_en.md#first-scheduled-run-after-recovery--monday-2026-09-28).

**Scope and public conditions:** Distinguish manual success from the first scheduled success. Do not predict run or job status after Oct 5.

### C21

**Scene:** S21. **Claim:** The one-time routine checked four calendars, found zero events, and sent a result email.

**Evidence type/date:** `[observed · user receipt confirmation]` 2026-09-27. **Sources:** [lessons from the second routine](../04-Routines-Lab/guides/second-routine_en.md#what-we-learned) · [configuration](../04-Routines-Lab/guides/second-routine_en.md#configuration).

**Scope and public conditions:** The record says it took 25 seconds, started about one minute late, and ran once. Do not claim guaranteed speed or exact-on-the-minute timing.

### C22

**Scene:** S22. **Claim:** Choose conditional notifications or always-report based on purpose, and make failures visible/check logs.

**Evidence type/date:** `[experience-based pattern]` 2026-09-21 and 09-27. **Sources:** [notification pattern](../05-Usage-Patterns/guides/patterns_en.md#3-choose-conditional-or-always-on-notifications-based-on-the-purpose) · [lessons from second routine](../04-Routines-Lab/guides/second-routine_en.md#what-we-learned) · [run history](../04-Routines-Lab/guides/wblp-routine-audit_en.md#run-history-observed-in-session-logs).

**Scope and public conditions:** Lessons from two cases. Do not claim an improved monitoring system has already been implemented.

### C23

**Scene:** S23. **Claim:** Choose local rather than cloud for this vault, which the cloud routine cannot reach, and separate external-source work.

**Evidence type/date:** `[documentation · environment decision]` 2026-09-27. **Source:** [where it should run](../04-Routines-Lab/concepts/local-vs-cloud_en.md#the-30-second-rule).

**Scope and public conditions:** The public CatchUpAI_VL repository can be connected; distinguish it from the full local vault. Do not make the absolute claim that no cloud routine can ever access local files.

### C24

**Scene:** S24. **Claim:** Prepare a routine by specifying its goal, schedule, access scope, success/failure reporting, and first-run verification.

**Evidence type/date:** `[pattern · docs]` 2026-09-27 and 10-04. **Sources:** [Routine checklist](../05-Usage-Patterns/guides/artifacts-routines-playbook_en.md#3-when-creating-a-routine) · [second-routine configuration](../04-Routines-Lab/guides/second-routine_en.md#configuration).

**Scope and public conditions:** The exact current click path has not been rechecked; omit detailed button instructions until then. Note that connected services may have write permission.

### C25

**Scene:** S25. **Claim:** Choose a feature based on whether automation is needed, where the data lives, and who needs to share it.

**Evidence type/date:** `[pattern · proposal]` 2026-09-27. **Sources:** [the playbook’s three questions](../05-Usage-Patterns/guides/artifacts-routines-playbook_en.md#1-what-should-you-build-ask-three-questions) · [where it should run](../04-Routines-Lab/concepts/local-vs-cloud_en.md#the-30-second-rule).

**Scope and public conditions:** This is a decision criterion, not a promise of automatic correct classification.

### C26

**Scene:** S26. **Claim:** The example prompt states the goal, audience, constraints, and verification method.

**Evidence type/date:** `[inference · proposal]` 2026-10-04. **Sources:** [the playbook’s three questions](../05-Usage-Patterns/guides/artifacts-routines-playbook_en.md#1-what-should-you-build-ask-three-questions) · [candidates not yet patterns](../05-Usage-Patterns/guides/patterns_en.md#candidates--not-yet-established-patterns).

**Scope and public conditions:** Reproduction with the new example is unverified. Do not present it as a verbatim request that the user entered at the time.

### C27

**Scene:** S27. **Claim:** The learning records were gathered into patterns, corrections, and a playbook.

**Evidence type/date:** `[artifact · retrospective]` 2026-09-27. **Sources:** [M5 retrospective](../vl_worklog/20260927_M5_Claude-Artifacts-Routines.md#daily-retrospective) · [playbook’s three questions](../05-Usage-Patterns/guides/artifacts-routines-playbook_en.md#1-what-should-you-build-ask-three-questions).

**Scope and public conditions:** No generalized learning result or quantitative productivity metric is available.

### C28

**Scene:** S28. **Claim:** It was confirmed that relevant learning materials open from public GitHub.

**Evidence type/date:** `[direct unauthenticated GET check]` 2026-10-04. **Source:** [the playbook’s three questions](../05-Usage-Patterns/guides/artifacts-routines-playbook_en.md#1-what-should-you-build-ask-three-questions).

**Scope and public conditions:** QR images have not been generated or scanned. Recheck links immediately before rendering.

### C29

**Scene:** v2 S17. **Claim:** Immediately after recovery, a manual run sent the first alert email with four U.S. technical jobs that had not been reported during the outage.

**Evidence type/date:** `[observed logs]` 2026-09-21. **Sources:** [routine summary](../04-Routines-Lab/guides/wblp-routine-audit_en.md#in-one-sentence) · [results](../04-Routines-Lab/guides/wblp-routine-audit_en.md#results).

**Scope and public conditions:** The four postings were Berwick, PA ×2 (posted Sep 10), Canton, MS (Sep 8), and Boardman, OR (Jun 5). Boardman was posted before the first failure on Sep 7, so say **four postings that had not been received during that period**, not “four jobs newly posted during the three weeks.” Do not claim the user missed application opportunities. Location names may appear; avoid making this look like detailed job or application advice.

### C30

**Scene:** v2 S18. **Claim:** During the Sep 21 recovery, the routine itself found that the Amazon Jobs search filters for Washington and the U.S. were being ignored. The user checked working parameters on the PC and corrected them.

**Evidence type/date:** `[observed log · local validation]` 2026-09-21; correct application confirmed in scheduled run Sep 28. **Sources:** [additional prompt defect](../04-Routines-Lab/guides/wblp-routine-audit_en.md#an-additional-prompt-defect-found-during-recovery) · [first scheduled run after recovery](../04-Routines-Lab/guides/wblp-routine-audit_en.md#first-scheduled-run-after-recovery--monday-2026-09-28).

**Scope and public conditions:** The response showed search condition `location: null`. The Washington query returned the same seven results as the general query; “fiber USA” returned a job in Spain. With corrected filters, U.S.-only search went from 7 to 5 (Spain and Japan removed), while Washington returned zero. The point that “no results for three weeks concealed the problem” comes from the audit note “there had been no results for three weeks, so it did not show.” Do not generalize to all Amazon APIs or current behavior.

### C31

**Scene:** v3 S20. **Claim:** After recovery, the WBLP routine continued its weekly Monday checks. On 2026-10-05 it found a new technical job in Canton, Mississippi (posted Oct 4) and sent an alert email. The email ended, “There were no Washington State postings this week either.” The user said the actual emails and Claude notifications were helpful.

**Evidence type/date:** `[email received]` 2026-10-05 10:14 CDT; subject “AWS WBLP Job Alert — Canton, Mississippi” (Gmail checked 2026-10-06) · `[user-spoken reflection]` 2026-10-06. **Sources:** [[Journal/2026-10-06#AWS 루틴 알림과 워싱턴주 공고 (구술 원문)|Oct 6 original user entry]] · [first scheduled run after recovery](../04-Routines-Lab/guides/wblp-routine-audit_en.md#first-scheduled-run-after-recovery--monday-2026-09-28), which records the following run as scheduled for Oct 5.

**Scope and public conditions:** The Claude notification is based on the user’s statement; the user will capture screen R6. Show the email as R5, hiding application links and job ID. Do not say “an email arrives every week”—the routine emails only when a new posting matches. Narration should say “it checks every week.”

### C32

**Scene:** v3 S20. **Claim:** The user intends to apply if a WBLP posting appears in Washington State, where they live.

**Evidence type/date:** `[user-spoken reflection]` 2026-10-06. **Source:** [[Journal/2026-10-06#AWS 루틴 알림과 워싱턴주 공고 (구술 원문)|Oct 6 original user entry]]—“I would apply if a posting came up in Washington State, where I live.”

**Scope and public conditions:** This is a future intention. Do not say the user applied or is likely to be accepted. Washington-only search returned zero with the corrected parameters on Sep 21 (C30).

### C33

**Scene:** v4 S06. **Claim:** The Sep 3 meeting was an event-planning meeting for a nonprofit where the user volunteers, discussing booth placement for participating businesses. The user spoke to Claude to organize their own work, not intending to create something for the meeting; a page appeared there and the group viewed and used it together.

**Evidence type/date:** `[user-spoken reflection]` 2026-10-06 · `[user-spoken reflection]` 2026-09-03 (“During the meeting, an idea came to me, so I made it on the spot and used it in the meeting.”). **Sources:** [[Journal/2026-10-06#Artifacts · Routines 영상 나레이션 리뷰 — 일을 시키는 사람도 배워야 한다 (구술 원문)|Oct 6 original user entry]] · [[Journal/2026-09-03#9/3 하루 정리 (구술 원문)|Sep 3 original user entry]].

**Scope and public conditions:** 🔒 Organization, event, and business names and settlement information are internal. Say only “a nonprofit” and “participating businesses” in the video, and use an anonymized booth-layout board on screen.

### C34

**Scene:** v4 S09 and S23. **Claim:** The user edited a shared page, but recipients saw an old version. The artifact sharing settings had an “Always share latest version” option, which the user did not know about and Claude had not suggested. The user found and enabled it, resolving the confusion.

**Evidence type/date:** `[user-spoken reflection]` 2026-10-06 · `[official-doc screenshot · symptom record]` 2026-09-07 and 09-13. **Sources:** [[Journal/2026-10-06#Artifacts · Routines 영상 나레이션 리뷰 — 일을 시키는 사람도 배워야 한다 (구술 원문)|Oct 6 original user entry]] · [shared link showing an old version](../02-Artifacts-Sharing-and-Versions/troubleshooting/shared-link-shows-old-version_en.md) · [official-doc clipping](../vl_materials/2026-09-13%20Claude%20Code%20Artifacts%20공식%20문서%20발췌%20(code.claude.com).md).

**Scope and public conditions:** There is no record of the date the toggle was enabled or a screenshot. It could not be found in the menu on Oct 6 either (C37), so S09 is set as a “reconstruction for explanation” diagram. “Claude did not suggest it” is this user’s experience, not a universal claim about Claude.

### C35

**Scene:** v4 S14. **Claim:** The user did not know about Routines. While using AI to explore data-center jobs, they noted that Amazon WBLP had no Washington postings and said they would need to check again if one appeared. Claude recognized the need and created a routine on its own (check postings every Monday and email). This experience impressed the user and led to making the video.

**Evidence type/date:** `[user-spoken reflection]` 2026-10-06 · `[routine configuration record]` created 2026-09-02. **Sources:** [[Journal/2026-10-06#Artifacts · Routines 영상 나레이션 리뷰 — 일을 시키는 사람도 배워야 한다 (구술 원문)|Oct 6 original user entry]] · [routine case — what it does](../04-Routines-Lab/guides/wblp-routine-audit_en.md#what-this-routine-does) · [[Journal/2026-09-01#AI가 스스로 찾아낸 기능 — 지시자의 사전 지식에 대해 (구술 원문)|Sep 1 original user entry]].

**Scope and public conditions:** Narration should say “early September” without emphasizing an exact date because the Sep 1 note and Sep 2 creation record differ by one day.

### C36

**Scene:** v4 S11, S19, S23, and S24. **Claim:** The user’s conclusion changed. They had thought that explaining the goal well was enough, but learning is needed both to explain goals well and to check whether work is moving toward them: “The person giving the work also has to learn.” AI sometimes demonstrates surprising capabilities, but it still needs to be used carefully. The three-week failure showed the user that AI was not yet reliable enough to take over everything.

**Evidence type/date:** `[user-spoken reflection]` 2026-10-06. **Source:** [[Journal/2026-10-06#Artifacts · Routines 영상 나레이션 리뷰 — 일을 시키는 사람도 배워야 한다 (구술 원문)|Oct 6 original user entry]].

**Scope and public conditions:** Present this as a perspective from personal experience (“In my experience”). Do not generalize it into an evaluation or prediction about all AI.

### C37

**Scene:** v4 S09 and S23. **Claim:** While working in September 2026, the user saw a version list dropdown whenever an artifact was edited, and there was an “Always share latest version” toggle. As of 2026-10-06, the user could no longer find that menu. The user sees this as an example of “features change frequently → human verification matters even more.”

**Evidence type/date:** `[user confirmation · spoken reflection]` 2026-10-06 · `[official documentation screenshot]` clipping from 2026-09-13. **Sources:** [[Journal/2026-10-06#「항상 최신 버전 공유」 설정이 사라졌다 (구술 원문)|Oct 6 original user entry]] · [shared link showing an old version — menu no longer visible as of Oct 6](../02-Artifacts-Sharing-and-Versions/troubleshooting/shared-link-shows-old-version_en.md#oct-6-2026--menu-no-longer-visible).

**Scope and public conditions:** It is unknown whether the feature was removed, moved, renamed, or changed to a default behavior. Narration should say “I don’t see that menu now,” not assert that “the feature is gone.”

### C38

**Scene:** v4 S04. **Claim:** In late August and early September 2026, the user researched data-center jobs and caregiver work with AI and published YouTube videos based on the results. They first encountered Artifacts and Routines during that research.

**Evidence type/date:** `[public videos · Topic records]` 2026-09. **Sources:** [Datacenter-Workforce-Programs video](../../Datacenter-Workforce-Programs/README.md#-영상)—Korean video https://youtu.be/DotegI2Q8fw · [WA-Caregiver-Pathways video](../../WA-Caregiver-Pathways/README.md)—Korean video https://youtu.be/ma59E0ij1_w · [[Journal/2026-09-01#AI가 스스로 찾아낸 기능 — 지시자의 사전 지식에 대해 (구술 원문)|Sep 1 original user entry]] (“I learned about these two features while working on Datacenter and Caregiver.”).

**Scope and public conditions:** The thumbnail is an original image from the user’s public channel (1280×720, under `assets/`). The research is in the past, so narration uses past tense (Oct 6 review). The routine and intent to apply in Washington (S20) are ongoing, so those use present tense.

[Korean original](claim-ledger.md) · [M6 overview](README_en.md) · [Slide plan](video-slide-plan_en.md)
