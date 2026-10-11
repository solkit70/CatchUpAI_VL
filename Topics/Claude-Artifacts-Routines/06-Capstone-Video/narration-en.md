---
title: "Claude Artifacts and Routines — English narration"
created: "2026-10-06 16:16:06"
tags:
  - remotion
  - narration
status: review-pending
---

## English narration

Adapted from the approved Korean `narrations.json`, preserving facts and claim scope. Spoken quotations are translated from Korean. See [claim ledger](claim-ledger_en.md#scene-by-scene-evidence). The S22 request is an example, not a historical quote.

### S01 (Ethan)

> For three weeks, not a single job-alert email arrived. AI was supposed to check the job postings for me every Monday morning. So what was happening? Were there really no jobs to report?

### S02 (Ethan)

> And yet, this very same AI took an idea that came to me during a meeting and immediately built a page for it. We put that page on the screen and used it in that same meeting.

### S03 (Ethan)

> I did not even know the names of either feature. They are Claude Artifacts and Routines. In this video, I will show you what I was able to do with them, and exactly where I ran into trouble. Stay to the end, and you will have a checklist of what to tell AI, and what to verify, when you delegate a task.

### S04 (Jennifer)

> From late August into early September, I was researching data-center work and caregiver work. I did that research with AI, and I also turned the results into YouTube videos. Until then, I had always believed that if I wanted to give AI a task effectively, I needed to know at least something about that task myself. But during that research, something challenged that belief. AI found and used features whose names I had never even heard. This is what I wrote in my notes that day: In this case, AI simply found a feature I knew absolutely nothing about, and applied it on its own.

### S05 (Jennifer)

> Those two features were Artifacts and Routines. In very simple terms, an Artifact is a page AI builds for you, one you can look at and use. A Routine is a task AI runs when a scheduled time arrives. The important point is that I did not know these features and ask AI to use them. I only explained what I wanted. AI found the right tools for that goal and built something for me. That was where my belief, that you must know a task before you can delegate it, began to change.

### S06 (Jennifer)

> The first example was an Artifact. I volunteer with a nonprofit, and on September third we had a meeting about an event it was preparing. We were discussing where to place the booths for participating businesses. I thought it would be useful to have a page that showed the whole layout at a glance. Actually, I had not intended to make something for the meeting. I was talking to Claude to organize my own tasks. But Claude built a booth-layout page right there. I put it on the meeting screen, and we discussed it together while looking at it. In the past, I could hardly have imagined building and using a page like that in the middle of a meeting. But when I tried to send the page to other people as a link, the first trap was waiting.

### S07 (Aiden)

> When you send someone a link, will they see exactly what you see on your own screen? In my case, the answer was no. I could see the entire booth layout. But in a window where I was not signed in, all I got was a message saying I needed to sign in to view it. The page that had worked so well in the meeting was effectively blank outside it.

### S08 (Aiden)

> The reason was in the way the page had been built. To save the changes whenever I moved the booths, Claude had attached a small data store to the page. But with this kind of page, making the link public only makes the page itself visible to everyone. The saved contents can only be viewed by people signed in to Claude. Since the whole booth layout was in that data store, recipients saw an empty screen. I only understood this after testing two small pages that looked exactly alike. So I changed the approach. I kept the editing page, where we could make changes together. And I made a separate status board for other people to view, putting the contents directly into the page without a data store.

### S09 (Aiden)

> There was another trap. I edited the sharing page and sent it again, but a recipient told me it still had not changed. My own screen clearly showed the new version. It turned out that the Artifact sharing settings had a separate option to always show recipients the latest version. With that option turned off, they could keep seeing the version that had originally been shared. I did not know that setting existed, and Claude had not told me about it first. The confusion only cleared up after I found it in the settings and turned it on myself. But while preparing this video, I looked for that setting again, and I cannot see that menu now. Features in these tools change frequently. This taught me that even when AI seems to handle everything, it can skip an essential detail without explaining it. So now, after making a change, I open the recipient's view myself in a signed-out incognito window. In the next experiment, though, AI and I were both changing the same number.

### S10 (Cherry)

> Here is a small page that counts a number. First, AI saved the value as eleven. Then I pressed the plus button twice on the screen and made it thirteen. But AI still thinks the number is eleven. If AI now tries to change it to twelve, what do you think will happen?

### S11 (Cherry)

> The answer is: the change gets rejected. When AI tried to edit the value, it attached a condition: Only make this change if the value I last saw is still unchanged. I had changed it in the meantime, so the edit was refused and nothing was written. AI then read the number again, and changed it from thirteen to fourteen using the updated value. It did not overwrite the change I had made. But this was a safeguard checked on the AI side of the edit. If several people press buttons on the page at the same time, that needs its own design. Here is what I took from the experiment. To judge whether safeguards like this are needed, the person delegating the task must define the desired result clearly and understand the basics of the design.

### S12 (Ryan)

> I also tested several other features with small examples: greeting someone by name, uploading and displaying an image, leaving comments on individual paragraphs, and splitting the screen and its data across multiple files.

### S13 (Ryan)

> But I was wrong about comments. At first, after only reading the documentation, I concluded that comments were not available on this account. When I built a small example myself, I could leave a comment, send it to Claude, and receive a reply. After that, I adopted a rule: only conclude that something cannot be done after checking it with a small example. And the place where verification was needed most was those three quiet weeks I mentioned at the beginning.

### S14 (Maia)

> Now let me tell you the story that led me to make this video. It concerns the second feature, Routines. In early September, I was using AI to research Amazon's work-based learning program for data-center jobs. There were no postings in Washington State at the time. I said I would need to look again later if a posting appeared. Claude heard that and created a Routine on its own. Every Monday morning, it would check the postings and email me if it found a Washington posting or a technical job within the United States. I had no idea this feature existed, or even that something like this could be built. AI recognized what I needed before I did, and made a tool for it. That was what impressed me most, and it is why I made this video.

### S15 (Maia)

> But from here, the story takes a different turn. This Routine only sends an email when it finds a matching job posting, so silence would normally be expected. The problem was that failure looked just as quiet. September seventh, fourteenth, and twenty-first: on all three occasions, no email came. Instead, each time the Routine sent a short push notification saying it had been unable to check. There was a signal. But honestly, it took me three weeks to recognize that those notifications meant the same failure was happening every week.

### S16 (Maia)

> So I started checking the clues one by one. Was Amazon blocking the request? I opened the same address on my own computer, and it worked normally. Was the wording of the request wrong, then? The run history showed that the request was not even getting out. The cause was the cloud environment where the Routine ran. Its door was locked: it could only connect to sites on an allowlist.

### S17 (Maia)

> I added the Amazon jobs site to the allowlist in the environment settings. Rather than waiting another week, I ran the task manually right away. All four queries succeeded, and the first alert email arrived with four technical job postings I had not received during that period. A week later, the scheduled run found a new data-center technical job in Maryland and sent an email. Saying that I had fixed it was not the evidence. The result of the next automatic run was.

### S18 (Aiden)

> But on the day of the repair, the Routine itself discovered another problem. The search conditions I had added to filter for Washington State and the United States were being quietly ignored. The Washington search still returned jobs in other places, and the U.S. technical-job search included a posting in Spain. The filters had been wrong from the start. But because I had received no results at all, I had no way to see that problem. I checked which conditions actually filtered correctly on my own computer, and changed them. Having no results does not necessarily mean there really are none.

### S19 (Aiden)

> AI had created the Routine on its own, but noticing that it was broken and getting it fixed still fell to me. In my experience, there were still gaps that kept me from handing everything over to AI. I also learned that there are two kinds of silence: silence because there are no results, and silence because the task failed. So I made the second Routine work the other way around. It checked the next day's calendar and sent an email even when there were no events. Whether to notify only when needed or report every time depends on the purpose. But make sure failures are reported separately, and occasionally open the run history yourself. I documented this whole investigation on GitHub; an English translation is available there too.

### S20 (Aiden)

> Since the repair, this Routine has been checking the postings for me every Monday morning. On October fifth, it found a newly posted technical job in Mississippi and sent an email, along with a Claude notification. The emails and notifications I actually receive are really helpful in my job search now. At the end of the email was this sentence: There were no Washington State postings this week either. If a posting appears in Washington State, where I live, I intend to apply right away.

### S21 (Jennifer)

> So what should we tell AI the next time we delegate a task? After this experience, I realized I should have stated these four things from the beginning, before asking AI to build anything. First, what is the task for? What purpose should the result serve? Second, who will view it? Does that include people who are not signed in? Third, where should it run? Does it need files on my computer, or are internet sources enough? Fourth, how will we verify it? That means checking the recipient's screen and the actual run history.

### S22 (Jennifer)

> For example, I wish I had requested the booth-layout page like this from the start: Build a page that shows the booth layout to meeting participants. People who are not signed in must be able to view it, and the editing page and sharing page should be separate. When it is ready, tell me how to check it from the recipient's point of view. There is not a single feature name in that request. Let AI choose the tools, while the person focuses on the purpose and on verification.

### S23 (Jennifer)

> This is not limited to a booth page or job alerts. I put together five practices I can use when delegating other work to AI too. First, explain more than the deliverable: say who will use it and how. Second, whether AI says something can or cannot be done, check it yourself with a small example. Third, there may be settings AI does not tell you about. And those settings may change one day. Check the essential ones yourself, and revisit them from time to time. Fourth, when you delegate automation, decide how it will report failure before focusing on what happens when it succeeds. Fifth, the person delegating the work needs to learn the basic structure too. That is how we explain the goal properly and check whether the work is moving toward it.

### S24 (Ethan)

> When I planned this video, I meant to say: Even without knowing the features, explain your goal and AI will handle it. But the conclusion changed. To explain what we want properly, and check whether the work is going well, the person still has to learn. The person giving the task needs to learn too. AI's surprising abilities make the world feel ready to change quickly. But in my own experience, that world has not arrived yet. Occasional impressive features are not the whole picture. For now, I think we can trust AI, but must use it carefully and verify its work. Have you left anything to AI and never checked it? Tell me in the comments.

### S25 (Ethan)

> This story is what I personally checked in my environment in September twenty twenty-six. Results may differ by account or date. Find the detailed experiment records and a playbook for your next task through the on-screen QR codes and description links. Thank you for watching to the end.
