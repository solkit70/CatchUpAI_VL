# Requirements Card — Turning Event Footage into a 3-Minute Highlight with AI
[한국어](requirements-card.md)

> This card organizes the request from the client (a reporter who shoots event photos and videos). **Parts that are not confirmed are marked as "assumption,"** and we confirm them with the client through [client-questions.en.md](client-questions.en.md).

## 1. The Request in One Sentence

**The client needs a way to tell AI "use these kinds of scenes" for event video shot over several hours, and have it pick only the matching parts, edit them into a short video of about 3 minutes, and add an intro and effects in the middle.**

## 2. The 6-Cell Summary

| Cell | Content | To confirm |
|---|---|---|
| **Input** | Video of a group event shot over several hours (possibly several clips) | Camera gear · resolution · file format · total length → **confirm** |
| **Instruction** | Describe what you want in words (spoken or written) — e.g. "3 minutes with the key points of the congratulatory speech, the award scenes, and participants having fun" | Whether they want to give instructions in Korean → **confirm** |
| **Output** | A short video of about 3 minutes | Aspect ratio (landscape 16:9 / vertical 9:16 for social media) · resolution · where it is delivered → **confirm** |
| **Finishing** | An intro effect at the start, various effects in the middle (transitions · captions · logo · music) | Event name · logo captions, whether music is used → **confirm** |
| **Budget** | It is for business, so **paid tools are fine** — willing to pay if it helps the work | Monthly budget range → **confirm** |
| **Current tools** | Manual editing with **Adobe Premiere Pro** (main tool, confirmed 10/17) · After Effects · CapCut | PC (Windows/Mac) · Adobe subscription plan → **confirm** |

## 3. Features Split into Three Parts

| Part | What needs to be done | Where manual work takes time (assumption) |
|---|---|---|
| **① Selecting scenes** | Find the sections that match the instruction in hours of video | Re-watching everything to find usable scenes — **the biggest time-saving point** |
| **② Assembling** | Adjust the order and length of the chosen sections to fit 3 minutes | Trimming cut lengths, matching the music beat |
| **③ Finishing** | Intro · transitions · captions · logo · music | Making a similar intro from scratch for every event |

## 4. An Example of a "Good 3-Minute Event Video" (for evaluation criteria)

This is one example of an event highlight (assumption — to be replaced with the client's actual delivery format).

| Order | Length | Content |
|---|---|---|
| Intro | 5–10 sec | Event name · date · host logo |
| Opening scene | 20 sec | Wide shot of the venue · arrivals · atmosphere |
| Congratulatory speech · key remarks | 30–40 sec | One or two key sentences from the speech (captioned) |
| Event montage | 60–80 sec | Program scenes · smiling faces · applause · performances |
| Awards · highlight | 30–40 sec | Awards · group photo · climax |
| Closing | 10–15 sec | Group photo · thank-you message · logo |

## 5. Must-Haves / Nice-to-Haves

**Must-haves**
- Can **upload or read** hours-long video (or several clips)
- **Selects scenes from spoken/written instructions** (scenes with speech + scenes without speech)
- Can **give revised instructions** on the result ("make the speech shorter and the awards longer")
- Can **pass the result to Premiere for finishing** (XML · project · plugin) — because the client is a Premiere user
- Can export at deliverable quality **without a watermark** (including paid plans)

**Nice-to-haves**
- Korean instructions · Korean captions
- Automatically adding intro · transition effects, and an intro template reused for every event
- Making a vertical (9:16) social media version at the same time
- Local processing (when uploading event video to outside servers is a concern)

## 6. Comparison and Evaluation Criteria (used in M2 · M4)

| Criterion | Question |
|---|---|
| Following instructions | Did it pick scenes as instructed? |
| Scene accuracy | Does it also find scenes without speech (awards · performances)? |
| Time taken | Upload · processing · up to revised instructions |
| Amount of touch-up | How much rework is needed in Premiere? |
| Premiere connection | Can it be passed over via XML · plugin? |
| Cost | Free trial scope · monthly fee · extra cost for long videos |
| Korean | Instructions · captions · interface |
| Data | Whether the video is uploaded to outside servers (whether the event host's consent is needed) |

## 7. What Changsoo Park Can and Cannot Do for the Client

**Changsoo Park cannot practice with or try paid services himself (decided 2026-10-17).** A free trial that only starts after registering a card (e.g. the Adobe trial) also counts as a paid service. So the manual **marks "what I tried myself" separately from "what I organized from official documentation."**

| Area | What I can do | What I cannot do |
|---|---|---|
| **Research** | Organize each method's features · pricing · limits · Premiere connection from official documentation · price tables · tutorials, and write down the date checked | Check real quality not in official documentation (whether it picks scenes well) in paid tools |
| **Hands-on trial** | Use tools with **free plans · free trials without a card** myself and record captures · where I got stuck · free limits | Practice with **paid plans · card-required trials** — demos inside Premiere Pro · After Effects also fall here |
| **Test video** | Test the same instructions with long videos that can be made public (recordings of Changsoo Park's public seminars · meetups) | Testing with the client's actual event video — only with the client's · event host's consent, and never uploaded to the public repo |
| **Code approach** | Demonstrate cutting scenes · an intro template myself with Claude Code + FFmpeg · Remotion (tools Changsoo Park uses) | Hard to guarantee the client can use it without coding |
| **Manual** | For tools I tried: a step-by-step manual with captures. For paid tools: steps based on official documentation and reference links, marked "not tried myself" | Guaranteeing that screens · steps in paid-tool manuals match the real thing |
| **Working together** | When the client uses paid tools, guide them **in person, sitting next to them** (possible because we live close) or through screen sharing, and add the results to the manual (with the client's consent) — options B · C in section 8 below | Signing up for · paying for paid tools on the client's behalf |
| **Equipment** | Try mainly cloud services | Changsoo Park's PC has no GPU (i7-1355U · 16GB), so trying local AI processing is slow or impossible |

## 8. Working Style — Three Options (decided with the client)

We live close to the client, so **we can meet in person** (Changsoo Park, night of 2026-10-17). How to proceed after M1 will be decided after getting the client's answer, and options can be mixed (e.g. start with B and move to C).

| Option | How | Good points | Things to consider |
|---|---|---|---|
| **A. Changsoo Park researches → delivers a manual** | Do M2–M6 on Changsoo Park's PC as in the roadmap and hand over the results and manual | Takes the least of the client's time | Paid tools are organized "from documentation only" |
| **B. Meet and work together on Changsoo Park's PC** | Do the process from M2 onward together in person on Changsoo Park's PC. For paid tools, the client logs in with their own account and tests | The client learns by watching the process, and paid tools are actually checked | Scheduling · the client logs out of their account after testing · if Changsoo Park's PC has no Premiere, check the Premiere connection on the client's PC |
| **C. Install VibeLearn AI on the client's PC + guidance** | Changsoo Park installs VibeLearn AI (VS Code · Claude Code and learning templates) on the client's PC and shows how to use it. After that, the client **researches · tries things themselves in the direction they want**, and Changsoo Park helps when they get stuck | Try things directly on the client's PC · Premiere · paid accounts. The client learns how to research itself and can use it for the next topic | The client needs a paid Claude subscription · installation and first guidance take time · the client needs time to study on their own |
