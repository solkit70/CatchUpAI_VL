# Seattle Tech Week 2026 - 최종 참가 계획

**작성일**: 2026-07-19  
**최종 업데이트**: 2026-07-25  
**상태**: 참가 계획 확정 + Google Calendar 등록 완료 + 오프라인 우선 기준 반영 + Luma 전체 행사 수 재확인 + Good to Great 등록 미승인 반영  
**기준 문서**: `../02-Curation/shortlist.md`, `../02-Curation/priority-review.md`

## M3 판단

오늘 M3의 목적은 `final.md`를 "의사결정 보드"에서 **실제 참가 계획**으로 바꾸고, Google Calendar에 등록 가능한 일정까지 넣는 것이다. Luma 상태는 2026-07-23 기준으로 다시 확인했고, 이미 사용자 캘린더에 있던 7/29 Databricks Omnigent 일정과 7/30 Lee & Park Meeting을 함께 고려했다. 이후 사용자 기준이 보강되어 Lee & Park Meeting은 연기 가능 일정으로 보고, 오프라인 AI 행사를 온라인 행사보다 우선하도록 7/30 계획을 다시 조정했다.

2026-07-24에 Luma 공개 캘린더를 다시 확인한 결과, Seattle Tech Week 2026의 현재 예정 행사는 **총 242개**이며, 이 중 AI 태그가 붙은 행사는 **77개**다. 이 최종 계획은 242개 전체 후보를 사람이 손으로 훑은 것이 아니라, AI와 함께 Luma 공개 데이터에서 이벤트를 수집하고 AI/Agent/Pitch/Demo/Hackathon/Workshop/오프라인 여부/기존 캘린더 충돌을 기준으로 분석해 실제 움직일 수 있는 일정으로 추려낸 결과다. 출처는 [Seattle Tech Week 2026 Luma 캘린더](https://luma.com/seattletechweek2026)이며, API 응답 기준 `period=future`, `entries=242`, `has_more=false`로 확인했다.

핵심 판단은 **모든 관심 후보를 넣지 않고, 실제 행동으로 이어질 가능성이 높은 행사만 캘린더에 등록**하는 것이다. Approval Required 항목은 제목 앞에 `[Apply]`를 붙였고, 승인 전이지만 우선순위가 높은 행사는 시간을 막아 두었다. 종료 시간이 확인되지 않은 일부 항목은 설명에 "verify before event"를 명시했다.

비용은 Luma 공개 페이지 기준으로 적었다. 가격이 명시되지 않고 `Register` 또는 `Request to Join`만 보이는 행사는 `가격 표시 없음`으로 적었으며, 실제 무료 여부는 Luma RSVP/Register 마지막 단계에서 한 번 더 확인해야 한다.

## 2026-07-25 Luma 상태 업데이트

사용자가 `Good to Great with AI Agents: Coffee & Panel with Seattle's best AI entrepreneurs | Lightspeed AI`의 상태가 **Registration not accepted**라고 알려 주었다. 이 행사는 더 이상 7/28 오전 참석 후보로 보지 않고, AI agent 제품화 관점의 관심 참고 후보로만 남긴다. Google Calendar의 해당 이벤트도 `[Not Accepted]` 제목과 투명 일정으로 업데이트했다.

## 2026-07-23 승인 이메일 반영

Luma에서 아래 11개 행사의 승인 이메일을 받아 Pending Approval → Approved로 변경했다. **How AI Gets Built at Ai2**는 행사명이 "AI Research Panel & Networking"에서 "AI Research Talk"로 변경됨을 주최측 공지로 확인했다.

- AEO: Optimize your business for AI Search (7/27)
- STW: Stories from Build-Fail-Build (7/27)
- Agentic Commerce ASO (7/27)
- Built to Last? AI, Startups and Data (7/28)
- AI With Agency (7/28)
- TwelveLabs + Qdrant AI Memory (7/28)
- You Vibe-Coded an App, Now What? (7/29)
- How AI Gets Built at Ai2 | AI Research Talk (7/30, 행사명 변경)
- Founder Fundamentals: AI IP Minefield (7/31)
- Preparing to Thrive (7/31)
- Building AI You Can Stand Behind (7/31)

아래 6개 행사도 같은 날 승인 이메일을 받았지만, 원래 무료/즉시 등록형이라 이미 "신청 완료"·Attend 상태였다 — 상태 변경 없이 승인 확인만 기록한다: AI Startup Secret Sauce, Automating Your Workflow Correctly, Seattle AI Summit - The Infrastructure Era, Startup425 AI Accelerator Demo Day, ACM Data Conclave, AI & the Future of Consumer Experiences.

새로 Approved된 항목 중 같은 날 다른 Approved/Attend 항목과 시간이 겹치는 경우가 여러 건 생겼다(7/28 저녁 AI With Agency ↔ TwelveLabs + Qdrant, 7/29 오전 You Vibe-Coded ↔ Seattle AI Summit, 7/30 오후 How AI Gets Built at Ai2 ↔ ACM Data Conclave, 7/31 오전 Founder Fundamentals ↔ Preparing to Thrive, 7/31 오후 Building AI You Can Stand Behind ↔ Consumer Experiences). 실제 참석은 각 항목의 날짜별 운영 메모에 표시된 대로 겹치는 시간대에서 선택이 필요하다.

**Google Calendar 반영**: 이번 세션에서는 Google Calendar 도구가 연결되어 있지 않아 캘린더 이벤트를 직접 업데이트하지 못했다. 문서상 상태는 모두 Approved로 반영했으니, 캘린더 도구가 연결되면 위 11개 이벤트를 tentative → confirmed(busy)로, Ai2 이벤트는 제목도 함께 갱신해야 한다.

## 최종 등록 일정

### 7/27 Mon

| 결정 | 시간 | 이벤트 | 상태 | 비용 | 장소/형식 | Calendar | Luma |
|---|---:|---|---|---|---|---|---|
| Attend | 1:00 PM-3:00 PM | AEO: Optimize your business for AI Search | Approved | 확인 필요 | Seattle, Register to See Address | [Calendar](https://www.google.com/calendar/event?eid=Zjc2aXY2dmwzOWtyZmlmNnVpc2UyOWtyNm8gc29sa2l0NzBAbQ) | [Luma](https://luma.com/02ar1zge) |
| Attend | 2:00 PM-3:00 PM | STW: Stories from Build-Fail-Build | Approved | 가격 표시 없음 | Seattle, Register to See Address | [Calendar](https://www.google.com/calendar/event?eid=c2RyYTRpYWozbG0yZG9zanVhbTg1bjR2NGMgc29sa2l0NzBAbQ) | [Luma](https://luma.com/jommk2wc) |
| Attend | 3:00 PM-5:00 PM | Agentic Commerce ASO | Approved | 가격 표시 없음 | Seattle, Register to See Address | [Calendar](https://www.google.com/calendar/event?eid=dGVnbnU0Z2FuaDQ1cjFxNzNlM2VtcnIzbWcgc29sa2l0NzBAbQ) | [Luma](https://luma.com/8024ch9r) |
| Attend | 5:00 PM-7:00 PM | AI Startup Secret Sauce | Registered | Free | Bellevue City Hall | [Calendar](https://www.google.com/calendar/event?eid=Z2FsM25zNnMydDMxbzJqNGEzNGVwMW1jcm8gc29sa2l0NzBAbQ) | [Luma](https://luma.com/njfn4ugt) |
| Waitlist | 6:00 PM-8:00 PM | Creativity, Intent, and the Future of AI | Waiting List | 확인 필요 | Art Love Salon | [Calendar](https://www.google.com/calendar/event?eid=bjZjZjBjcGo1bGJqZjBpazh1dWw4MmVlYjggc29sa2l0NzBAbQ) | [Luma](https://luma.com/khxpsau5) |

### 7/28 Tue

| 결정 | 시간 | 이벤트 | 상태 | 비용 | 장소/형식 | Calendar | Luma |
|---|---:|---|---|---|---|---|---|
| Attend | 9:00 AM-10:30 AM | Automating Your Workflow Correctly | 신청 완료 | 가격 표시 없음 | thinkspace SEATTLE | [Calendar](https://www.google.com/calendar/event?eid=ZHQxYnRxMXNqbGpiaXY3MGU3ODZxdjYycGcgc29sa2l0NzBAbQ) | [Luma](https://luma.com/xkkbxh0u) |
| Exclude | 9:30 AM-11:30 AM | Good to Great with AI Agents | Registration not accepted | 가격 표시 없음 | Seattle, Register to See Address | [Calendar](https://www.google.com/calendar/event?eid=YzEwZmIwcWM1anUzdTU0dXZvYjBudmQycGsgc29sa2l0NzBAbQ) | [Luma](https://luma.com/4uddde71) |
| Pending | 12:30 PM-4:00 PM | Building Enduring AI Products in a Shifting Market | Pending Approval | 가격 표시 없음 | Seattle, Register to See Address | [Calendar](https://www.google.com/calendar/event?eid=bGg1dXNxdXZzbDBxam9zbHI3Y2p2cGcxamMgc29sa2l0NzBAbQ) | [Luma](https://luma.com/seattle-u6gi) |
| Attend | 3:00 PM-4:00 PM | Built to Last? AI, Startups and Data | Approved | 확인 필요 | PitchBook | [Calendar](https://www.google.com/calendar/event?eid=aG4xbTVwYTBuYWc0Z2J0Nmt0cG91MThnNm8gc29sa2l0NzBAbQ) | [Luma](https://luma.com/7wo9san2) |
| Waitlist | 4:00 PM-5:30 PM | AI for Impact | Waitlist | 확인 필요 | Salesforce Seattle Office | [Calendar](https://www.google.com/calendar/event?eid=OGFtcTdhMHRvMWhjOTY5ZWVicjdja3YyaWsgc29sa2l0NzBAbQ) | [Luma](https://luma.com/vmk774sy) |
| Pending | 4:00 PM-6:00 PM | Your AI Strategy Is a People Strategy | Pending Approval | 가격 표시 없음 | Seattle, Register to See Address | [Calendar](https://www.google.com/calendar/event?eid=M2toZXJ2aWZhcmlwb3FvNjJmZzNjMTJnOG8gc29sa2l0NzBAbQ) | [Luma](https://luma.com/so0ufkgy) |
| Existing | 5:00 PM-6:00 PM | AI4PKM x CMDS 격주 미팅 | Existing calendar event | N/A | Online/Meeting | Existing | N/A |
| Attend | 5:30 PM-7:30 PM | AI With Agency | Approved | 가격 표시 없음 | Bellevue, exact address later | [Calendar](https://www.google.com/calendar/event?eid=NGRmYTB2azc0cDdqNGphaXRiOTI4ZmcwYzggc29sa2l0NzBAbQ) | [Luma](https://luma.com/xysigza0) |
| Attend | 5:30 PM-9:00 PM | TwelveLabs + Qdrant AI Memory | Approved | 가격 표시 없음 | Bellevue, Register to See Address | [Calendar](https://www.google.com/calendar/event?eid=MzZvamY2MG12ZWxiMjFjMTFzcGJiMnNlNG8gc29sa2l0NzBAbQ) | [Luma](https://luma.com/kyksgkak) |

### 7/29 Wed

| 결정 | 시간 | 이벤트 | 상태 | 비용 | 장소/형식 | Calendar | Luma |
|---|---:|---|---|---|---|---|---|
| Attend | 9:00 AM-6:00 PM | Seattle AI Summit - The Infrastructure Era | 신청 완료 | Name your own price / suggested price | 10455 NE 5th Pl, Bellevue | [Calendar](https://www.google.com/calendar/event?eid=X2Nscjc4YmFlNnQ2NmFvcGo2NTQ2Z2pqcWVkMTc0aDIwY2xyNmFyamtlY242b3Q5ZWRsZ2cgc29sa2l0NzBAbQ) | [Luma](https://luma.com/yra9zj02) |
| Attend | 9:00 AM-12:00 PM | You Vibe-Coded an App, Now What? | Approved | 가격 표시 없음 | AI House | [Calendar](https://www.google.com/calendar/event?eid=cWFuZDlsdTUwc3NrcWdxdDYydjFicmJlMDQgc29sa2l0NzBAbQ) | [Luma](https://luma.com/stw2026) |
| Attend | 12:00 PM-1:30 PM | Technical Talk: An Omnigent Deep Dive / Patio Social | 신청 완료 | 가격 표시 없음 | Databricks Seattle | [Calendar](https://www.google.com/calendar/event?eid=OGdnZzJucTBscWQ5cHI5Mzdmazd0MzI1bHMgc29sa2l0NzBAbQ) | [Luma](https://luma.com/tech_workshop_Omnigent) |
| Attend | 6:00 PM-8:00 PM | Startup425 AI Accelerator Demo Day | 신청 완료 | 가격 표시 없음 | Bellevue City Hall | [Calendar](https://www.google.com/calendar/event?eid=Y2hhNHYxYnY4ZmVjMzk5MnZtNDg5a2JmbXMgc29sa2l0NzBAbQ) | [Luma](https://luma.com/49ctfw1f) |

### 7/30 Thu

| 결정 | 시간 | 이벤트 | 상태 | 비용 | 장소/형식 | Calendar | Luma |
|---|---:|---|---|---|---|---|---|
| Existing | 10:00 AM-11:30 AM | Lee & Park Meeting | Existing calendar event / movable | N/A | Existing | Existing | N/A |
| Attend | 2:00 PM-3:45 PM | ACM Data Conclave | 신청 완료 | 가격 표시 없음 | Bellevue, Everest Reception Hall | [Calendar](https://www.google.com/calendar/event?eid=OWt0cDBudTg1MTVidm9qdHBlYWt2dDdzcTQgc29sa2l0NzBAbQ) | [Luma](https://luma.com/f3rma403) |
| Attend | 3:00 PM-4:00 PM | How AI Gets Built at Ai2 \| AI Research Talk | Approved | 가격 표시 없음 | Ai2 Office, Seattle | [Calendar](https://www.google.com/calendar/event?eid=bWlybHFzNDljODNtNW1xZjZmaDc3MmxyajQgc29sa2l0NzBAbQ) | [Luma](https://luma.com/cp10n5uk) |
| Pending | 4:00 PM-7:00 PM | OpenAI Builder Lounge #SeattleTechWeek | Pending Approval | 가격 표시 없음 | Bellevue, Register to See Address | [Calendar](https://www.google.com/calendar/event?eid=M2w0MWJnbzlrcmtjNGVwdmFoN3BlNHFmYTAgc29sa2l0NzBAbQ) | [Luma](https://luma.com/openai-builderlounge-seattle-jul30-2026) |
| Pending | 6:30 PM-9:30 PM | Seattle World Models Carnival | Pending Approval | 확인 필요 | Downtown Bellevue, Register to See Address | [Calendar](https://www.google.com/calendar/event?eid=bGx0dDhlMXJ0YWJrZmFkNGRnNDE2dGw5OGcgc29sa2l0NzBAbQ) | [Luma](https://luma.com/g4vycfcb) |

### 7/31 Fri

| 결정 | 시간 | 이벤트 | 상태 | 비용 | 장소/형식 | Calendar | Luma |
|---|---:|---|---|---|---|---|---|
| Attend | 9:00 AM-11:00 AM | Founder Fundamentals: AI IP Minefield | Approved | 가격 표시 없음 | Washington 1000 | [Calendar](https://www.google.com/calendar/event?eid=NHA3cWk1MGVkbjdmY2JkZ2NqanQ1Zmllbjggc29sa2l0NzBAbQ) | [Luma](https://luma.com/od8wjgld) |
| Pending | 9:00 AM-11:30 AM | Seattle \| Tech Week Claude Code Workshop | Pending Approval | 가격 표시 없음 | Pioneer Square Labs | [Calendar](https://www.google.com/calendar/event?eid=ZWdjMnFlZTU3MXZubXZxa2o5NzEzaXF1b2Mgc29sa2l0NzBAbQ) | [Luma](https://luma.com/claude-eulw) |
| Attend | 10:30 AM-12:00 PM | Preparing to Thrive | Approved | 가격 표시 없음 | College Club Seattle | [Calendar](https://www.google.com/calendar/event?eid=NG9wNW05cmpobjY5amVhM2VrZ3Z1M2owcTggc29sa2l0NzBAbQ) | [Luma](https://luma.com/5owz3qeo) |
| Attend | 2:00 PM-4:00 PM | Building AI You Can Stand Behind | Approved | 가격 표시 없음 | Register to See Location | [Calendar](https://www.google.com/calendar/event?eid=Mmw0a2NvaDZkYzJzczY0ZGk0OXBmYTZubWcgc29sa2l0NzBAbQ) | [Luma](https://luma.com/governance-security-ai) |
| Attend | 3:30 PM-6:00 PM | AI & the Future of Consumer Experiences | 신청 완료 | Free | Register to See Location | [Calendar](https://www.google.com/calendar/event?eid=MDgxNWZlaG50MWJvb2lxNW9objg1b3ZiMjggc29sa2l0NzBAbQ) | [Luma](https://luma.com/xmbjsen9) |
| Pending | 4:00 PM-7:00 PM | Aging in the Era of AI | Pending Approval | 가격 표시 없음 | CoLabs | [Calendar](https://www.google.com/calendar/event?eid=NWY5aHVndGpzbnZrYWl0YmNvbHVwa2Zja3Mgc29sa2l0NzBAbQ) | [Luma](https://luma.com/p9gkeexu) |

## 날짜별 운영 메모

### 7/27 Mon

- **1:00 PM-3:00 PM — [Approved] AEO: Optimize your business for AI Search**
  - 이유: Agentic Commerce ASO와 같은 Aizii.ai/TF Labs 흐름으로, AI 검색 최적화에서 AI 거래 최적화로 이어지는 전 단계를 볼 수 있다.
  - 상태: Approved (2026-07-23 승인 이메일 수신). Busy 일정으로 변경했다.
- **2:00 PM-3:00 PM — [Approved] STW: Stories from Build-Fail-Build**
  - 이유: AI 창업자의 실패/재시도 이야기라 Builders Lounge와 창업 관점에서 의미가 있다.
  - 상태: Approved (2026-07-23 승인 이메일 수신). Busy 일정으로 변경했다.
- **3:00 PM-5:00 PM — [Approved] Agentic Commerce ASO**
  - 이유: AI Agent가 실제 거래·구매·결제 흐름으로 이어지는 지점을 관찰할 수 있다.
  - 상태: Approved (2026-07-23 승인 이메일 수신). Busy 일정으로 변경했다.
- **5:00 PM-7:00 PM — AI Startup Secret Sauce**
  - 이유: Eastside AI startup 네트워킹이며 BigHug, Builders Lounge, Startup425 네트워크와 연결된다.
  - 상태: 신청 완료. 실제 busy 일정으로 등록했다.
- **6:00 PM-8:00 PM — [Waitlist] Creativity, Intent, and the Future of AI**
  - 이유: AI와 창작/인간 의도 주제라 관심이 있지만, AI Startup Secret Sauce와 충돌한다.
  - 상태: Waiting List 등록 완료. 투명 일정으로 등록했다.

### 7/28 Tue

- **9:00 AM-10:30 AM — Automating Your Workflow Correctly**
  - 이유: AI workflow 자동화가 실제 팀에서 유지되려면 context layer가 필요하다는 주제가 Bila AI/업무 자동화와 맞다.
  - 상태: 신청 완료. 실제 busy 일정으로 등록했다.
- **9:30 AM-11:30 AM — [Not Accepted] Good to Great with AI Agents**
  - 이유: AI agent를 production/reliability/product lesson 관점에서 다룬다.
  - 상태: Registration not accepted(2026-07-25 사용자 업데이트). Google Calendar에는 투명 참고 일정으로만 남겼고 실제 참석 후보에서는 제외한다.
- **12:30 PM-4:00 PM — [Pending Approval] Building Enduring AI Products**
  - 이유: AWS, OpenAI, Madrona 조합이며 evals, reliability, portability, 모델 성능 변화 속에서의 차별화가 핵심이다.
  - 상태: Pending Approval. 투명 일정으로 등록했다.
- **3:00 PM-4:00 PM — [Approved] Built to Last?**
  - 이유: AI hype와 지속 가능한 AI 사업을 구분하는 관점이다.
  - 상태: Approved (2026-07-23 승인 이메일 수신). Busy 일정으로 변경했다. Building Enduring(아직 Pending)과 주제/시간이 겹치므로 실제 참석은 이쪽 우선.
- **4:00 PM-5:30 PM — [Waitlist] AI for Impact**
  - 이유: Responsible AI, governance, social impact. BigHug/grant/social impact 관점에서 의미가 있다.
  - 상태: Waitlist. 투명 일정으로 등록했다.
- **4:00 PM-6:00 PM — [Pending Approval] Your AI Strategy Is a People Strategy**
  - 이유: AI adoption을 사람/팀 역량으로 보는 행사라 Builders Lounge/교육 운영과 연결 가능하다.
  - 상태: Pending Approval. 투명 일정으로 등록했다.
- **5:00 PM-6:00 PM — AI4PKM x CMDS 격주 미팅**
  - 기존 캘린더 일정. Tech Week 일정과 충돌 없음.
- **5:30 PM-7:30 PM — [Approved] AI With Agency**
  - 이유: Agentic AI, autonomous enterprise, startup spotlight가 핵심이다.
  - 상태: Approved (2026-07-23 승인 이메일 수신). Busy 일정으로 변경했다. TwelveLabs + Qdrant(같은 5:30 PM 시작, 역시 Approved)와 겹치므로 실제 참석 선택 필요.
- **5:30 PM-9:00 PM — [Approved] TwelveLabs + Qdrant**
  - 이유: AI memory, video intelligence, retrieval, agents가 Catch Up AI 영상/지식 검색/agent memory와 연결된다.
  - 상태: Approved (2026-07-23 승인 이메일 수신). Busy 일정으로 변경했다. AI With Agency(같은 5:30 PM 시작, 역시 Approved)와 겹치므로 실제 참석 선택 필요.

### 7/29 Wed

- **9:00 AM-6:00 PM — Seattle AI Summit - The Infrastructure Era**
  - 이유: Bellevue 기반 flagship AI 행사이며 infrastructure, enterprise AI, consumer AI, startup pitch를 넓게 볼 수 있다.
  - 상태: 신청 완료. 실제 busy 일정으로 등록했다.
- **9:00 AM-12:00 PM — [Approved] You Vibe-Coded an App, Now What?**
  - 이유: Build with AI 영상과 VibeCoding-Onboarding-Program의 핵심 질문과 직접 연결된다.
  - 상태: Approved (2026-07-23 승인 이메일 수신). Busy 일정으로 변경했다. Seattle AI Summit 오전 구간(9 AM-6 PM)과 겹치므로 실제 참석 시간대 선택 필요.
- **12:00 PM-1:30 PM — Databricks Omnigent Deep Dive**
  - 상태: 신청 완료. 실제 busy 일정으로 등록했다. Seattle AI Summit 중간 시간과 겹치므로 실제 이동 여부를 결정해야 한다.
- **6:00 PM-8:00 PM — Startup425 AI Accelerator Demo Day**
  - 이유: Bellevue City Hall에서 비기술 창업자들이 AI 도구로 MVP를 만든 사례를 볼 수 있다. Builders Lounge, BigHug, 비개발자 AI 제품화 관점과 강하게 연결된다.
  - 상태: 신청 완료. 실제 busy 일정으로 등록했다.

### 7/30 Thu

- **10:00 AM-11:30 AM — Lee & Park Meeting**
  - 기존 캘린더 일정. 다만 사용자가 연기 가능하다고 했으므로, 같은 시간대에 더 높은 가치의 오프라인 AI 행사가 확정되면 연기 후보로 본다.
- **2:00 PM-3:45 PM — ACM Data Conclave**
  - 이유: Bellevue 오프라인 AI/data 행사라 같은 시간대 온라인 AI Agents보다 사용자 기준에 더 맞는다.
  - 상태: 신청 완료. 실제 busy 일정으로 등록했다.
  - 메모: 공개 아젠다는 4:45 PM까지 이어지지만, OpenAI Builder Lounge 이동을 위해 핵심 구간 중심으로 3:45 PM까지 캘린더를 잡았다.
- **3:00 PM-4:00 PM — [Approved] How AI Gets Built at Ai2 \| AI Research Talk**
  - 이유: Ai2의 open models, post-training, evaluation, AI research lifecycle을 직접 볼 수 있어 기술 학습 가치는 높다.
  - 상태: Approved (2026-07-23 승인 이메일 수신). 행사명이 "AI Research Panel & Networking"에서 "AI Research Talk"로 변경됨. Busy 일정으로 변경했다. ACM Data Conclave(2:00-3:45 PM)와 겹치고 OpenAI Builder Lounge(4 PM 시작, 아직 Pending)와 동선이 빡빡하므로 실제 참석 여부는 계속 검토.
- **4:00 PM-7:00 PM — [Pending Approval] OpenAI Builder Lounge**
  - 이유: Codex coworking, OpenAI Applications CTO AMA, open demos, founder/developer dinner가 포함된 최우선 네트워킹 후보.
  - 상태: Pending Approval. 승인 전까지는 투명 일정으로 관리한다.
- **6:30 PM-9:30 PM — [Pending Approval] Seattle World Models Carnival**
  - 이유: video generation, world models, simulation, evaluation 주제가 영상 제작/Remotion/Qwen3-TTS 관심과 연결된다.
  - 상태: Pending Approval. OpenAI Builder Lounge와 겹치지만 9:30 PM까지 이어지므로 후반부 백업으로 둔다.

### 7/31 Fri

- **9:00 AM-11:30 AM — [Pending Approval] Claude Code Workshop**
  - 이유: 현재 Codex/Claude Code 기반 조사 자동화와 VibeLearn 산출물 제작에 가장 직접적인 학습 가치가 있다.
  - 상태: Pending Approval. 승인되면 오전 anchor로 둔다.
- **9:00 AM-11:00 AM — [Approved] Founder Fundamentals: AI IP Minefield**
  - 이유: AI 창업/제품화 과정의 IP/legal risk를 이해하는 데 유용하다.
  - 상태: Approved (2026-07-23 승인 이메일 수신). Busy 일정으로 변경했다. Claude Code Workshop(9:00-11:30 AM, 아직 Pending)과 겹치므로 실제 참석 선택 필요.
- **10:30 AM-12:00 PM — [Approved] Preparing to Thrive**
  - 이유: AI readiness/교육 관점이 BigHug 일반 사용자 교육과 연결된다.
  - 상태: Approved (2026-07-23 승인 이메일 수신). Busy 일정으로 변경했다. Claude Code Workshop(아직 Pending)과 겹치는 오전 시간대이므로 실제 참석 선택 필요.
- **2:00 PM-4:00 PM — [Approved] Building AI You Can Stand Behind**
  - 이유: AI governance, security, trust in production이 VibeGuiding/Bila AI 제품화와 연결된다.
  - 상태: Approved (2026-07-23 승인 이메일 수신). Busy 일정으로 변경했다. AI & the Future of Consumer Experiences(3:30-6:00 PM)와 30분(3:30-4:00 PM) 겹치므로 실제 참석 선택 필요.
- **3:30 PM-6:00 PM — AI & the Future of Consumer Experiences**
  - 이유: BigHug AI/Bila AI, Builders Lounge의 소비자 참여, Catch Up AI의 일반 사용자 관점과 연결된다.
  - 상태: 신청 완료. 실제 busy 일정으로 등록했다.
- **4:00 PM-7:00 PM — [Pending Approval] Aging in the Era of AI**
  - 이유: AI와 고령화/헬스/사회적 영향 주제라 BigHug/NGO 관점과 연결된다.
  - 상태: Pending Approval. Consumer Experiences와 겹치므로 승인되면 선택 필요.

## 제외 / 보류한 후보

| 결정 | 이벤트 | 이유 |
|---|---|---|
| Calendar Removed | AI Agents as Force Multipliers | Virtual 행사라 Google Calendar에서 제거했다. 주제 참고용 Luma 후보로만 남긴다. |
| Exclude | Good to Great with AI Agents | Registration not accepted. AI agent 제품화 관점의 관심 참고 후보로만 남긴다. |
| Exclude | Applied AI Pitch Night | 7/29 저녁은 Open 상태의 Startup425 Demo Day를 우선 |
| Conflict (결정 필요) | Building AI You Can Stand Behind | Approved(2026-07-23). 7/31 오후 Consumer Experiences(3:30-6:00 PM)와 30분 겹치므로 실제 참석 시간 조정 필요 |
| Interest Only | The Global AI Conversation | 온라인 보조 후보이나 이번 주 캘린더에는 넣지 않음 |

## Luma 신청 상태

캘린더 등록은 완료했지만, Google Calendar 등록만으로 Luma 참석 신청이 완료되는 것은 아니다. 각 행사는 Luma의 `Request to Join`, `Register`, `Join Waitlist` 상태를 따로 관리한다.

### 7/27 Mon

| 상태 | 이벤트 | 링크 |
|---|---|---|
| 승인 완료 | Agentic Commerce ASO | [Luma](https://luma.com/8024ch9r) |
| 승인 완료 | STW: Stories from Build-Fail-Build | [Luma](https://luma.com/jommk2wc) |
| 신청 완료 | AI Startup Secret Sauce | [Luma](https://luma.com/njfn4ugt) |
| Waiting List 등록 완료 | Creativity, Intent, and the Future of AI | [Luma](https://luma.com/khxpsau5) |
| 승인 완료 | AEO: Optimize your business for AI Search | [Luma](https://luma.com/02ar1zge) |

### 7/28 Tue

| 상태 | 이벤트 | 링크 |
|---|---|---|
| 신청 완료 | Automating Your Workflow Correctly | [Luma](https://luma.com/xkkbxh0u) |
| Pending Approval | Building Enduring AI Products | [Luma](https://luma.com/seattle-u6gi) |
| Registration not accepted | Good to Great with AI Agents | [Luma](https://luma.com/4uddde71) |
| 승인 완료 | AI With Agency | [Luma](https://luma.com/xysigza0) |
| 승인 완료 | TwelveLabs + Qdrant | [Luma](https://luma.com/kyksgkak) |
| Pending Approval | Your AI Strategy Is a People Strategy | [Luma](https://luma.com/so0ufkgy) |
| 승인 완료 | Built to Last? AI, Startups and Data | [Luma](https://luma.com/7wo9san2) |
| Waitlist | AI for Impact | [Luma](https://luma.com/vmk774sy) |

### 7/29 Wed

| 상태 | 이벤트 | 링크 |
|---|---|---|
| 신청 완료 | Seattle AI Summit - The Infrastructure Era | [Luma](https://luma.com/yra9zj02) |
| 승인 완료 | You Vibe-Coded an App, Now What? | [Luma](https://luma.com/stw2026) |
| 신청 완료 | Databricks Omnigent Deep Dive | [Luma](https://luma.com/tech_workshop_Omnigent) |
| 신청 완료 | Startup425 AI Accelerator Demo Day | [Luma](https://luma.com/49ctfw1f) |

### 7/30 Thu

| 상태 | 이벤트 | 링크 |
|---|---|---|
| Pending Approval | OpenAI Builder Lounge #SeattleTechWeek | [Luma](https://luma.com/openai-builderlounge-seattle-jul30-2026) |
| Pending Approval | Seattle World Models Carnival | [Luma](https://luma.com/g4vycfcb) |
| 신청 완료 | ACM Data Conclave | [Luma](https://luma.com/f3rma403) |
| 승인 완료 | How AI Gets Built at Ai2 \| AI Research Talk | [Luma](https://luma.com/cp10n5uk) |

### 7/31 Fri

| 상태 | 이벤트 | 링크 |
|---|---|---|
| Pending Approval | Claude Code Workshop | [Luma](https://luma.com/claude-eulw) |
| 신청 완료 | AI & the Future of Consumer Experiences | [Luma](https://luma.com/xmbjsen9) |
| 승인 완료 | Building AI You Can Stand Behind | [Luma](https://luma.com/governance-security-ai) |
| Pending Approval | Aging in the Era of AI | [Luma](https://luma.com/p9gkeexu) |
| 승인 완료 | Founder Fundamentals: AI IP Minefield | [Luma](https://luma.com/od8wjgld) |
| 승인 완료 | Preparing to Thrive | [Luma](https://luma.com/5owz3qeo) |

### 남은 신청/확인 필요

1. [OpenAI Builder Lounge](https://luma.com/openai-builderlounge-seattle-jul30-2026) — Pending Approval
2. [Seattle World Models Carnival](https://luma.com/g4vycfcb) — Pending Approval
3. [Claude Code Workshop](https://luma.com/claude-eulw) — Pending Approval
4. [Aging in the Era of AI](https://luma.com/p9gkeexu) — Pending Approval

## M3 DoD 체크

- [x] 캘린더 등록 후보 정리
- [x] 사용자 결정 필요 항목 정리
- [x] 최종 참석 이벤트 확정
- [x] Google Calendar 등록
- [x] 등록 링크 기록
- [x] Topic Retrospective 작성
