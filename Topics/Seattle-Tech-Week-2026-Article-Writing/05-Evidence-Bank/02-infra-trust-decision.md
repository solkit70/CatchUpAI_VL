---
title: "Evidence Bank B — 기술·신뢰·의사결정 클러스터 채굴"
created: 2026-08-12 00:00:00
author:
  - "Claude Code"
tags:
  - seattle-tech-week
  - evidence-bank
  - trust
  - infrastructure
---

## Evidence Bank B — 기술·신뢰·의사결정 클러스터

**모듈**: M5 - 1차 자료 채굴 / **대상**: 10개 (Spark+AI 4 · ACM 2 · InformsCon 3 · Biuty 1)

> **이 클러스터의 역할**: 창업 클러스터(A)만으로 기사를 쓰면 "AI로 누구나 만들 수 있다"는 낙관 일변도가 된다.
> B는 **"그래서 그걸 믿고 쓸 수 있는가"**를 묻는다. 두 축이 맞물려야 분석 기사가 된다.

## B-01. Muazma Zahid — 믿을 수 있는 AI 시스템 만들기

| 항목 | 내용 |
|---|---|
| 화자 | Muazma Zahid |
| 소속 | Group Product Manager, Google (직전 Microsoft 8년) |
| 행사 | ACM Data Conclave, ACM Seattle KDD 주최 |
| 일시·장소 | 2026-07-30, Everest Reception Hall, Bellevue |
| 영상 | https://youtu.be/_VFLykjvBCs (약 35분, 기조연설) |

> **연재 2편의 척추가 될 자료.** 793줄로 30개 중 가장 길고, 인용 밀도가 가장 높다.

### 장면 — 손 든 사람이 한 명이었다 (기사에 그대로 쓸 수 있는 현장 순간)

AI를 만드는 사람들로 가득 찬 방에서, 자기가 만든 것을 믿느냐고 묻자 벌어진 일이다.

> **[2:19]** "I want to start with a quick poll. Who here has built an AI application? A single agent, multi-agent, some sort of agentic application?"
>
> "간단한 설문으로 시작하겠습니다. 여기서 AI 애플리케이션을 만들어 보신 분? 단일 에이전트든 멀티 에이전트든, 에이전트 형태의 무언가요."

> **[2:28]** *(거의 전원 거수)* "Almost everyone here has done something about it. Now, how many of you will actually trust it — that application — to approve a mortgage? Approve a refund of $50,000? Delete a row or a table? Or prescribe medicine?"
>
> "여기 계신 거의 모든 분이 뭔가 만들어 보셨네요. 그러면, 그 애플리케이션에 **주택담보대출 승인**을 맡기시겠습니까? **5만 달러 환불 승인**은요? **행이나 테이블 삭제**는요? **약 처방**은요?"

> **[2:45]** "Anyone?" ... **[2:47]** "One person. I want to talk to you about it."
>
> "아무도 없나요? ... **한 분이시네요.** 그분과 얘기를 좀 해 보고 싶습니다."

→ **연재 2편의 리드로 최우선 후보.** 시애틀에서 열린 데이터 학회에서, AI를 직접 만드는 전문가들이
자기 시스템을 믿지 못한다는 사실이 한 장면으로 드러난다. 통계 백 줄보다 강하다.

### 인용 — 똑똑한 것은 더 이상 차별점이 아니다

> **[4:37]** "In my opinion, being smart isn't differentiated anymore. What I mean by that is that having a smart model with a large context window is not enough. Models are commodity at this point. If not every day, every other week, there is a new model which can do a little bit better job than the previous one."
>
> "제 생각에 **똑똑한 것은 더 이상 차별점이 아닙니다.** 큰 컨텍스트 창을 가진 똑똑한 모델만으로는 충분하지 않다는 뜻입니다. 이 시점에 모델은 **범용품(commodity)**입니다. 매일은 아니어도 격주로, 이전 것보다 조금 더 나은 모델이 나옵니다."

> **[4:56]** "It is the system around that that makes it smarter, reliable, accurate, and scalable."
>
> "그것을 더 똑똑하고, 신뢰할 수 있고, 정확하고, 확장 가능하게 만드는 것은 **그 주위의 시스템**입니다."

### 인용 — 비행기 비유

> **[3:37]** "If you are going to sit in a plane 50,000 feet above the ground, would you believe, by just listening to a pilot, which a person thinks that they are the smartest? Or would you believe a pilot who is smart enough but has all the systems around it to really trust that those systems work?"
>
> "지상 5만 피트 상공의 비행기에 앉는다면, 자기가 제일 똑똑하다고 생각하는 조종사의 말만 믿으시겠습니까? 아니면 충분히 똑똑하면서 **주변 시스템이 제대로 작동한다는 것까지 갖춘** 조종사를 믿으시겠습니까?"

### 인용 — 에이전트를 신입사원처럼 다뤄라 (가장 옮기기 좋은 개념)

> **[30:18]** "Really think of your agent as a new hire. So if you have somebody who just joined your team, you won't give them production database keys from day one until you really trust them with that information."
>
> "**에이전트를 신입사원이라고 생각하십시오.** 팀에 막 합류한 사람에게 첫날부터 운영 데이터베이스 키를 주지는 않습니다. 그 정보를 믿고 맡길 만하다는 것이 확인되기 전까지는요."

> **[30:44]** "It's really about thinking about some probation period, some kind of testing period ... Shadowing first."
>
> "일종의 **수습 기간**, 시험 기간을 생각하는 겁니다. 먼저 따라다니게 하는 것이죠."

> **[31:27]** "Performance reviews — you actually give them feedback. So that's the feedback loop. And then the escalation path. So a manager, leader, whoever there is in the path."
>
> "인사평가 — 피드백을 주는 겁니다. 그게 피드백 루프죠. 그리고 에스컬레이션 경로가 있습니다. 관리자든 리더든, 그 경로에 있는 사람 말입니다."

### 인용 — 되돌릴 수 있는가 (베조스 프레임을 에이전트에 적용)

> **[28:58]** "This threshold is defined by the cost of being wrong. Jeff Bezos has this famous decision-making framework ... is this decision reversible or not? And if you really think about an agentic system, is the action reversible or not?"
>
> "이 임계값은 **틀렸을 때의 비용**으로 정해집니다. 제프 베조스의 유명한 의사결정 프레임이 있죠. 이 결정이 되돌릴 수 있는가? 에이전트 시스템도 똑같이 생각하면 됩니다. **그 행동은 되돌릴 수 있는가?**"

> **[29:24]** "A chatbot typo tolerates more risk than a refund approval."
>
> "챗봇의 오타는 환불 승인보다 훨씬 많은 위험을 허용합니다."

### 인용 — 조직을 바꾼 곳은 거의 없다

> **[33:17]** "Everyone talks about AI, runs AI pilots, built AI agents, scaling agents. Very few really redesigned the org to actually support those AI agents — which is more about culture plus processes."
>
> "다들 AI를 이야기하고, 파일럿을 돌리고, 에이전트를 만들고, 확장합니다. 그런데 **그 에이전트를 실제로 뒷받침하도록 조직을 재설계한 곳은 거의 없습니다.** 그건 문화와 프로세스의 문제거든요."

### 수치

| 수치 | 원문 근거 | 주의 |
|---|---|---|
| 기업 생성AI 앱의 **95%가 프로덕션에 못 감** | [5:16] "95% of enterprise GenAI apps do not make it to production" | ⚠️ **발표자의 자체 데이터가 아니라 인용한 외부 조사**다. "This was a survey done last year." 기사에 쓸 때 출처를 그의 발언으로 귀속하지 말 것 |
| 제조 고객 **25일 → 5일** | [7:22] "it was 25 days ... In order to solve that 25 days down to five days" | 발표자가 직접 수행한 프로젝트 |
| 섀도 에이전트 도입으로 정확도 **7% 향상** | [31:10] "That process itself increased the accuracy by 7% for us" | 발표자 1인칭 실측 |
| 본인 경력 | Microsoft 8년 → Google, 5개국 3개 대륙 근무 | [0:52], [2:08] |

### 발표자가 제시한 다섯 가지 질문 (기사 박스 기사감)

> **[32:25]** "These are the five things to take home today. Before you do your next sprint of any of these AI applications, these are the questions I want you to ask."

1. **[32:35]** "What is your data freshness SLA? What is the least you can live with?" — 데이터 신선도 기준은 무엇인가
2. **[32:40]** "What is the cost of your worst-case hallucination?" — 최악의 환각이 발생했을 때의 비용은 얼마인가
3. **[32:45]** "Which of your agents could take an irreversible action today with no human in the loop?" — **사람 개입 없이 되돌릴 수 없는 행동을 할 수 있는 에이전트가 지금 어느 것인가**
4. **[33:07]** "When did we last look at the LLMs as a judge versus a human in the loop?" — LLM 심판과 사람 개입을 마지막으로 점검한 것이 언제인가
5. **[33:17]** 조직 재설계 — 문화와 프로세스를 바꿨는가

→ 이 다섯 질문은 **한인 매체 독자 중 기업 실무자에게 그대로 쓸 수 있는 체크리스트**다.
서비스 저널리즘 요소로 박스 처리하기 좋다.

### 반론·한계 (발표자 본인이 밝힌 것)

> **[27:28]** "Don't just do it once and forget about that. Because over time, there's model drift, there's data drift. Even in the same situation, you have not changed a single line of code, they can drift."
>
> "한 번 하고 잊어버리면 안 됩니다. 시간이 지나면 모델 드리프트, 데이터 드리프트가 있습니다. **코드를 한 줄도 안 바꿔도** 같은 상황에서 결과가 달라질 수 있습니다."

> **[32:52]** "Many of the limited tasks these agents can do today — it's really probably you or your system or organizational issue that's not actually making it to production."
>
> "오늘 에이전트가 할 수 있는 일이 제한적인 것은, 사실 여러분 자신이나 시스템, 조직의 문제 때문에 프로덕션까지 못 가는 경우가 많습니다."

### 기사 활용 각도

- **연재 2편 리드 = 손 든 사람 한 명 장면.** 1편이 창업 낙관이라면, 2편은 이 장면으로 연다.
- **"모델은 범용품, 시스템이 차별점"**은 한국 독자가 흔히 접하는 "어느 모델이 더 똑똑한가" 담론을 정면으로 뒤집는다.
- **"에이전트를 신입사원처럼"**은 비전문가 독자도 즉시 이해하는 비유다. 기사 제목 후보로도 가능하다.
- A 클러스터의 Quiana Daniels(의료), Dias Gotama(고령자 재입원)가 **되돌릴 수 없는 영역**을 다룬다는 점과 직접 충돌시킬 수 있다. "8주 만에 만들었다"와 "그걸 믿고 약을 처방하겠는가"를 나란히 놓으면 기사가 깊어진다.
- v1은 신뢰·평가 축을 McKinsey·Gartner 조사로만 채웠다. 여기 시애틀 현장에서 구글 PM이 말한 1차 증언이 있다.

## B-10. Ziqi Wang — Biuty.ai: 소비자 AI에서 신뢰는 기능이다

| 항목 | 내용 |
|---|---|
| 화자 | Ziqi Wang |
| 소속 | Founder, Biuty.ai (피부 인텔리전스) |
| 행사 | AI & the Future of Consumer Experiences |
| 일시·장소 | 2026-07-31, Redmond Community Center |
| 영상 | https://youtu.be/JWGEwcthshI |

> **B-01(Muazma Zahid)과 짝을 이루는 자료.** Zahid가 기업 시스템에서 신뢰를 원칙으로 말했다면,
> 여기서는 그 원칙이 **소비자 앱의 실제 기능으로 구현된 모습**을 볼 수 있다. 서로 다른 행사·다른 날인데
> 같은 결론에 도달한다.

### 인용 — 추천이 아니라 "왜 추천하는지"

> **[3:12]** "So I can not only see the recommendation, but also I can know why she's recommending that. For example, I can click in and see, oh, why it's compatible with me, and which specific ingredients is good for my — which kind of skin needs."
>
> "추천만 보는 게 아니라 **왜 그걸 추천하는지**도 알 수 있습니다. 눌러 들어가면 왜 나한테 맞는지, 어떤 성분이 내 피부 필요에 좋은지 볼 수 있죠."

→ Zahid가 말한 **설명 가능성(explainability)**이 소비자 앱의 핵심 기능으로 나타난 지점.

### 인용 — 경고를 띄운다

> **[3:53]** "One feature I find really helpful personally is it can show the compatibility with my current routine product. I already have some products on my shelf, but sometimes I don't really know if those products used together, if there will be some side effect. ... And if you can see like this one, there is a little caution, so I should be aware of."
>
> "개인적으로 정말 유용한 기능은 **지금 쓰는 제품과의 호환성**을 보여주는 것입니다. 선반에 제품이 몇 개 있는데, 같이 쓰면 부작용이 있는지 잘 모를 때가 있거든요. ... 보시면 여기 **주의 표시**가 떠 있습니다. 알고 있어야 할 부분이죠."

### 인용 — 얼굴을 숨길 수 있다 (사용자 통제감)

> **[6:16]** "If I only want to show what has changed, rather than show my face, I can hide it as well and just share the information of my skin."
>
> "변화만 보여주고 싶고 얼굴은 보이기 싫으면, **얼굴을 가리고** 피부 정보만 공유할 수도 있습니다."

→ 민감한 개인 데이터를 다루는 제품에서 **사용자 통제감**이 기능으로 설계된 사례.

### 인용 — 사진 한 장으로 판단하지 않는다

> **[8:39]** "We combine three parts. Number one is the picture, like the CV model. Number two is the behavior factors — which kind of product you use, as well as what kind of med spa treatment you have recently. ... And the third part is the environmental factors. So I'm right now at Redmond. And what's the temperature right now? And also hydration, like UV. So we combine all of these factors into our recommendation. So it's not only based on one single picture."
>
> "세 가지를 결합합니다. 첫째는 사진, 컴퓨터 비전 모델입니다. 둘째는 **행동 요인** — 어떤 제품을 쓰는지, 최근 어떤 시술을 받았는지. ... 셋째는 **환경 요인**입니다. 제가 지금 레드먼드에 있는데, 현재 기온은 어떤지, 수분과 자외선은 어떤지. 이 모든 걸 결합해 추천합니다. **사진 한 장에만 근거하지 않습니다.**"

### 기사 활용 각도

- **v1이 가장 약했던 축이다.** v1은 소비자 AI를 "외부 자료에는 약하게 보임"으로 처리하고 넘어갔다. 여기 현장 데모의 1차 기록이 있다.
- Gartner 조사(소비자는 AI가 정보는 찾아주되 결정은 대신하지 않기를 원한다)를 **배경**으로 놓고, 이 제품의 세 가지 기능(설명·경고·얼굴 가리기)을 **전면**에 놓으면 v1과 정반대의 구조가 된다.
- 한인 독자에게 피부·화장품은 접근성이 매우 높은 소재다. 기업 AI 이야기보다 먼저 읽힐 가능성이 크다.

## B-09. 의사결정 과학의 미래 — 패널 토론

| 항목 | 내용 |
|---|---|
| 패널 | **Emmy Smith** (Candela, 전 AWS) · **Guvenc Degirmenci** (AWS 사이언스팀) · **Vivek Radhakrishnan** (OR·ML 인프라, 전 Amazon 9년) |
| 사회 | **Apoorv Mathur** (Product Manager, Siemens) |
| 행사 | InformsCon 2026, INFORMS 태평양북서지부 주최 |
| 일시·장소 | 2026-07-31, Everest Reception Hall, Bellevue |
| 영상 | https://youtu.be/b8Fdb1woOLk (약 53분) |

> **v1이 한 문장으로 처리하고 넘어간 축**이다. 실제로는 30개 자료 중 기업 현실을 가장 날카롭게
> 보여주는 자료다. 패널 4인 전원이 Amazon/AWS 출신이라는 점도 시애틀 기사에 맞다([5:15] 사회자가 직접 언급).

### 인용 — "최적화 말고 생성 AI 주세요" (이번 취재 최고의 아이러니)

> **[11:24]** "What we are seeing on the customer engagement side, when we talk to customers, especially at the executive level — when we hear a problem, and we know the problem could be solved with optimization tools, and we propose solving that problem with optimization tools, we get the reaction of: **no, no, no, we don't want optimization, we want generative AI.**"
>
> "고객을 만나 보면, 특히 임원급에서 이런 일이 있습니다. 문제를 들었고 그게 최적화 도구로 풀 수 있는 문제라는 걸 알아서 최적화로 풀자고 제안하면, 돌아오는 반응이 이겁니다. **'아니요 아니요, 최적화 말고 생성 AI로 해 주세요.'**"
>
> — Guvenc Degirmenci (AWS 사이언스팀)

→ **연재의 강력한 한 방.** AI 열풍이 오히려 더 나은 해법을 밀어내는 장면이다. 한인 독자 중 기업
실무자·의사결정자에게 직격한다. v1의 "AI가 현실 문제로 분화되었다"는 추상 서술과 비교가 안 된다.

### 인용 — 전력망: 데이터센터는 2년, 송전선은 10년

> **[9:04]** "The hyperscalers can maybe put a data center up in two years. And I come from the energy utilities industry — the data center wants **one gigawatt of power within two years.** And the transmission lines, the energy infrastructure to feed this data center, **takes 10 years to build.**"
>
> "하이퍼스케일러는 데이터센터를 2년이면 세웁니다. 저는 에너지 유틸리티 업계 출신인데, 그 데이터센터는 **2년 안에 1기가와트의 전력**을 원합니다. 그런데 그 데이터센터에 전기를 보낼 **송전선과 에너지 인프라는 짓는 데 10년**이 걸립니다."
>
> **[9:43]** "No infrastructure upgrade you can imagine can come in the timeframe that you guys can set up."
>
> "여러분이 세우는 속도에 맞출 수 있는 인프라 증설은 상상할 수 있는 어떤 방법으로도 불가능합니다."
>
> — Apoorv Mathur (Siemens)

→ **AI 인프라 병목을 가장 구체적으로 보여주는 수치.** v1은 인프라·전력 문제를 AI2Work 분석 인용으로만
처리했다. 여기 그 업계에서 실제로 소프트웨어를 만드는 사람의 1인칭 증언이 있다.
해법도 함께 제시된다 — [10:05] 데이터센터가 연중 최대 전력을 쓰지 않고 **그리드 피크 시간대를 피하도록** 하는 유연성.

### 인용 — 그래서 OR(운영 연구)이 사라졌는가

> **[7:44]** "In my opinion, right now, for solving the whole problem, **OR is everything.** We haven't had much luck with using an LLM model to solve that. These are — we spend tens of billions, hundreds of billions per year on infrastructure; give us a tiny amount of variance, this is a ton of money."
>
> "제 생각에 지금 이 문제 전체를 푸는 데는 **운영 연구가 전부입니다.** LLM으로 그걸 풀어보려 했지만 잘 되지 않았습니다. 우리는 인프라에 연간 수백억, 수천억 달러를 씁니다. 오차가 아주 조금만 생겨도 엄청난 돈입니다."
>
> — Vivek Radhakrishnan

> **[8:14]** "OR was at the top of science for a long time. It was very hard — for people who don't understand what it is, essentially a black box. ... In organizing models, in helping people understand models, especially when people are explaining **why did the black box do this** — that's seen an absolute, it's given us good success."
>
> "운영 연구는 오랫동안 과학의 정점이었습니다. 모르는 사람에게는 사실상 블랙박스였죠. ... 모델을 정리하고, 사람들이 모델을 이해하도록 돕는 일, 특히 **'왜 블랙박스가 이런 결정을 했는가'**를 설명하는 데서는 확실한 성과를 봤습니다."

→ **LLM의 진짜 쓸모가 "푸는 것"이 아니라 "설명하는 것"**이라는 현장 판단. 기사에 쓰기 좋은 반전이다.

### 인용 — 검토와 판단이 오히려 늘었다

> **[25:51]** "These tools are not taking the accountability of everything that they're doing. Even if you set up an agent as a product manager, the agent does all the research, it tells you what you should be doing, and **you need to apply the judgment there.**"
>
> "이 도구들은 자기가 하는 일에 대해 **책임을 지지 않습니다.** 프로덕트 매니저로 에이전트를 세팅해도, 에이전트가 조사를 다 하고 뭘 해야 하는지 알려주지만, **판단은 여러분이 해야 합니다.**"

> **[26:12]** "The hard part is **the things that require my review or judgment are increasing**, because things can be generated very quickly. But can you really get through that stack of ideas, how quickly they are coming your way?"
>
> "어려운 점은 **제 검토와 판단이 필요한 일이 오히려 늘어난다**는 겁니다. 생성은 아주 빠르니까요. 그런데 그렇게 쏟아지는 아이디어 더미를 정말 다 처리할 수 있습니까?"
>
> — Vivek Radhakrishnan

### 인용 — "많은 부분이 애 보기(babysitting)입니다"

> **[20:34]** "If we standardize it, we can automate this, and now you can redeploy headcount to do things that humans are really good at doing: **high judgment, evaluating the output.** I think the new terminology is **a lot of babysitting.** So we've gotta find people who are comfortable doing that too."
>
> "표준화하면 자동화할 수 있고, 그러면 인력을 사람이 정말 잘하는 일로 재배치할 수 있습니다. **높은 수준의 판단, 결과물 평가** 같은 것이죠. 요즘 쓰는 표현으로는 **'애 보기'가 많아진** 겁니다. 그걸 편안해하는 사람도 찾아야 합니다."
>
> — Emmy Smith

### 장면 — 2007년 금융위기와 설명할 수 없는 모델

> **[33:09]** "I was building mass media effectiveness modeling for **Bank of America's home equity division when the 2007 market crash happened**, and they were like, *what happened to your model?* And I was like, **the other banks collapsed.** I don't know what you want me to say — but how do I ever represent that in the data if I wasn't following what was happening in the macroeconomic environment?"
>
> "저는 **2007년 시장 붕괴 때 뱅크오브아메리카 주택담보 부문의 매스미디어 효과 모델**을 만들고 있었습니다. 그쪽에서 묻더군요. *당신 모델에 무슨 일이 일어난 겁니까?* 제가 말했죠. **다른 은행들이 무너졌잖아요.** 뭐라고 말씀드려야 할지 모르겠는데, 거시경제 환경에서 벌어지는 일을 따라가고 있지 않았다면 그걸 데이터로 어떻게 표현합니까?"
>
> — Emmy Smith

→ **AI 시대 "기본기"의 필요성을 보여주는 장면.** 데이터에 절대 나타나지 않는 맥락이 있다는 것.
[32:00] "손으로 표준편차를 한 번 계산해 봤기 때문에 그게 무슨 일을 하는지 이해하게 된" 경험을 강조한 대목과 이어진다.

### 인용 — LLM이 되는 척한다

> **[28:50]** "The LLMs are well-known to **make you believe that they can do certain things, even if they cannot.** So it's important to understand what they can do and what they cannot do — especially during the interviews."
>
> "LLM은 **할 수 없는 일도 할 수 있다고 믿게 만드는** 것으로 잘 알려져 있습니다. 그래서 무엇을 할 수 있고 무엇을 할 수 없는지 이해하는 것이 중요합니다. 특히 채용 면접에서요."

> **[30:03]** "We have seen a lot of applications out there — public applications as well — that seem to be working, but easily hacked, or easily producing different solutions."
>
> "겉보기엔 잘 돌아가는데 쉽게 뚫리거나 쉽게 다른 답을 내놓는 애플리케이션을 많이 봤습니다. 공개된 것들도요."

> **[31:03]** "**Vibe coding is happening everywhere**, and then we end up seeing that the systems that are built are not holding each other as planned. So as developers, or as scientists, now we are required to **keep testing things** to make sure that they are working as planned."
>
> "**바이브 코딩이 사방에서 벌어지고 있습니다.** 그런데 그렇게 만들어진 시스템들이 계획대로 서로 맞물리지 않는 걸 보게 됩니다. 그래서 개발자든 과학자든 이제는 **계속 테스트해야** 합니다."
>
> — Guvenc Degirmenci

→ **클러스터 A(바이브 코딩 낙관)와 정면으로 부딪히는 발언.** 같은 주에 벨뷰에서 열린 다른 행사다.
연재에서 A와 B를 충돌시킬 때 가장 직접적인 근거가 된다.

### 수치

| 수치 | 원문 근거 | 화자 |
|---|---|---|
| 교육 영상 번역 **4개월 → 4일** | [1:22] "went from four months to four days" | Emmy Smith |
| BI 전략이 없다는 걸 파악하는 데 **3개월** | [1:07] "It took me three months to figure out there was no BI strategy" | Emmy Smith |
| 팀 규모 **90명 → 3명** (조직 이동) | [19:18] "a team of 90 at Amazon" → [19:57] "a team of three" | Emmy Smith |
| 데이터센터 **1GW / 2년** vs 송전 인프라 **10년** | [9:14]~[9:35] | Apoorv Mathur |
| 인프라 연간 지출 **수백억~수천억 달러** | [7:51] "tens of billions, hundreds of billions per year" | Vivek Radhakrishnan |
| 계획 수립 주기 **약 3개월**에서 단축 | [8:44] "We take almost three months to plan ... it's down" | Vivek Radhakrishnan |

### 반론·한계

- [21:34] Emmy: "We're gonna let capitalism run it first, but let's see what we can do with it." — 자본주의가 먼저 굴릴 것이라는 냉정한 인정
- [26:36] Vivek: "We are kind of the governors with all of these agents ... how are you monitoring, how are you making sure that they are on track" — 거버넌스가 개인에게 떠넘겨진 상태
- [23:02] Guvenc: "That makes our job a little bit drier" — 과학자가 방법론 대신 모델 평가에 시간을 쓰게 된 것에 대한 회의

### 기사 활용 각도

- **"최적화 말고 생성 AI"** 발언은 연재 2편의 핵심 인용 후보. AI 열풍의 부작용을 한 문장으로 보여준다.
- **1GW/2년 vs 10년**은 인프라 섹션의 유일한 1차 수치. 표나 도식으로 뽑기 좋다.
- Emmy Smith의 2007년 일화는 **"기본기" 논의를 사람 이야기로 전환**한다. 한인 독자에게 특히 잘 읽힌다.
- Guvenc의 "바이브 코딩이 사방에서" 경고는 **A 클러스터와의 충돌 지점**. 연재 구성의 축.
- Zahid(B-01)의 "조직을 재설계한 곳은 거의 없다"와 Emmy의 "리더십은 '너무 강력해서 뭔가 망가질 것'이라고 말한다"[1:34]가 서로를 보강한다.

## B-03. Denny Lee — Omnigent: 에이전트를 위한 오픈소스 메타 하네스

| 항목 | 내용 |
|---|---|
| 화자 | Denny Lee |
| 소속 | Databricks |
| 행사 | Spark + AI: Ignite the Future (Seattle Spark + AI) |
| 일시 | 2026-08-04 업로드 (Seattle Tech Week 주간) |
| 영상 | https://youtu.be/uACNZTN6doU |

### 수치 — 에이전트 사용 규모 (한 플랫폼 기준)

> **[2:34]** "On the data platform, there are more than **100,000 custom agents** built, **a quadrillion tokens** to use per year, and about **a billion downloads for MLflow**."
>
> "데이터 플랫폼에서 **10만 개 이상의 커스텀 에이전트**가 만들어졌고, 연간 **1000조(quadrillion) 토큰**이 사용되며, MLflow는 약 **10억 다운로드**입니다."

> ⚠️ **M8 확인 필요**: "quadrillion"은 전사 오류 가능성이 있다(trillion과 혼동 가능). 기사에 이 수치를
> 쓸 경우 원 영상 음성으로 재확인하거나, 수치 없이 "천문학적 규모"로 처리한다.

### 인용 — 변화 속도

> **[3:11]** *(청중에게 샌드박스 도구 이름을 하나씩 물은 뒤)* "It's okay that you don't know the answer to what I just said. The point I'm trying to get at is that's how fast things are happening. **What I just said — all these things, they weren't around six months ago.**"
>
> "제가 방금 말한 걸 모르셔도 괜찮습니다. 제가 말하려는 요점은 **일이 그만큼 빠르게 벌어지고 있다**는 겁니다. 방금 언급한 것들, **6개월 전에는 없던 것들입니다.**"

### 인용 — 환각은 기능이자 결함이다

> **[4:16]** "There's these systems that hallucinate, **which we actually want because it's the creativity portion of a model.** The problem is when it hallucinates, **it's wrong.**"
>
> "환각을 일으키는 시스템들이 있습니다. **사실 우리가 원하는 것이기도 합니다. 모델의 창의성 부분이니까요.** 문제는 환각이 일어날 때 **그게 틀렸다**는 것입니다."

> **[4:07]** "It's just like when you look at any image generated from any large language models — three fingers, six fingers, extra arms."
>
> "대규모 언어 모델이 만든 이미지를 볼 때와 같습니다. 손가락이 세 개, 여섯 개, 팔이 하나 더 있고요."

### 인용 — 실무자의 진짜 고통: 창을 옮겨 다니는 일

> **[0:22]** "What happens when you have to copy and paste from one IDE to your Slack, to your email, to your other models? ... You have multiple browser windows open, multiple CLIs, multiple terminal windows, multiple IDEs, all trying to interact with each other."
>
> "IDE에서 슬랙으로, 이메일로, 다른 모델로 복사·붙여넣기를 해야 할 때 어떻게 됩니까? ... 브라우저 창 여러 개, CLI 여러 개, 터미널 여러 개, IDE 여러 개가 서로 상호작용하려고 열려 있습니다."

> **[0:50]** "Everything I just said is real ... we at Databricks and the engineering side of the house, we actually have been **suffering from this for about nine months.**"
>
> "방금 말한 건 다 실제입니다. 저희 Databricks 엔지니어링 쪽에서도 **약 9개월째 이 문제로 고생해 왔습니다.**"

> **[5:04]** "I've got all my skills, or my agent memory ... How do I get that information over to Codex? ... Except now you have Codex and Claude both hitting their own version of the skill, and now they've **bifurcated.**"
>
> "제 스킬과 에이전트 메모리가 다 있습니다 ... 그 정보를 어떻게 Codex로 넘기죠? ... 그러면 Codex와 Claude가 각자 자기 버전의 스킬을 갖게 되고, **갈라져 버립니다.**"

→ 해법: [5:35] "You're going to build a skill once. It's in the Omnigent folder. And Omnigent itself can send it to Codex, or send it to Claude." 오픈소스, `omnigent.ai`.

### 기사 활용 각도

- **"6개월 전에는 없던 것들"**은 변화 속도를 보여주는 가장 간결한 인용. Greechan(A-03)의 "첫 안식휴가" 고백과 짝지으면 강하다.
- **"환각은 우리가 원하는 창의성이지만, 일어나면 틀린 것"**은 한인 독자에게 AI의 본질적 딜레마를 한 문장으로 설명한다.
- 대형 데이터 플랫폼 엔지니어링 조직도 **9개월째 같은 문제로 고생**했다는 고백은 "대기업은 다 해결했겠지"라는 통념을 깬다.
- Zahid(B-01)의 "모델은 범용품, 시스템이 차별점"과 정확히 같은 방향. 서로 다른 회사(Google / Databricks), 다른 행사, 다른 날의 발언이다.

## B-04. Kunal Jain — "그럴듯한 출력"이 가장 위험하다

| 항목 | 내용 |
|---|---|
| 화자 | Kunal Jain (커머스 데이터 플랫폼 팀 엔지니어, 벨뷰 소재) |
| 행사 | Spark + AI: Ignite the Future |
| 영상 | https://youtu.be/TInzom7heAs |

> ⚠️ **M8 확인**: 전사본 [0:12]에 화자가 "Pradhan Jain"으로 표기돼 있으나 **전사 오류**로 보인다.
> 영상 제목과 frontmatter의 `speaker` 필드는 **Kunal Jain**이다. 기사에는 frontmatter 기준으로 표기한다.

> **개념적으로 이번 취재에서 가장 중요한 자료 중 하나.** LLM 환각과 **정확히 같은 구조의 문제**가
> 데이터 파이프라인에서는 오래전부터 있었다는 것을 보여준다. AI 이전부터 있던 문제라는 점이
> 기사에 깊이를 준다.

### 인용 — 성공했다는 것이 맞다는 뜻은 아니다

> **[1:47]** "Have you ever seen your data pipelines **succeed** but then you found a data issue?" *(청중 다수 반응)* "I see a lot of yeses."
>
> "데이터 파이프라인이 **성공**했는데 나중에 데이터 문제를 발견한 적 있으십니까?" *(다수 거수)* "네가 많이 보이네요."

> **[2:05]** "**A successful job definitely does not guarantee that the data is correct.** It only guarantees that Spark has completed all the stages, there were no exceptions, the files were written. **But what about the business meaning?**"
>
> "**작업이 성공했다고 해서 데이터가 맞다는 보장은 전혀 없습니다.** 스파크가 모든 단계를 마쳤고, 예외가 없었고, 파일이 쓰였다는 것만 보장할 뿐입니다. **그런데 업무상의 의미는요?**"

> **[2:32]** "**The business meaning often lives in a ticket, or in someone's memory, instead of in an assertion.**"
>
> "**업무상의 의미는 검증 코드가 아니라 티켓 안에, 또는 누군가의 기억 속에 있는 경우가 많습니다.**"

→ 이 한 문장이 기사에 그대로 쓸 값이 있다. **조직의 지식이 코드가 아니라 사람 머릿속에 있다**는
문제는 Muazma Zahid(B-01)의 "조직을 재설계한 곳이 거의 없다"와 같은 이야기다.

### 인용 — 가장 위험한 것은 실패가 아니라 "그럴듯함"

> **[2:56]** "The reason is **plausible output.** And it is, I believe, **the most dangerous type of output.** Because what is worse than failures? **Silent failures.**"
>
> "이유는 **그럴듯한 출력**입니다. 제 생각에 **가장 위험한 종류의 출력**입니다. 실패보다 나쁜 게 뭘까요? **조용한 실패입니다.**"

> **[4:02]** "There's a common feature in all of these three things. **And it's not the API that caused it. It is that the result can still look like proper data.** A dashboard can still render it. The downstream jobs can still pick it up. Your non-zero row count will still succeed. **And your smoke test will also pass.**"
>
> "이 세 가지에는 공통점이 있습니다. **API가 원인이 아닙니다. 결과물이 여전히 제대로 된 데이터처럼 보인다는 것이 문제입니다.** 대시보드에 그려지고, 후속 작업이 받아서 처리하고, 행 개수 검사도 통과하고, **스모크 테스트도 통과합니다.**"

> **[4:32]** "**Rows exist is not the same as rows being correct.** The defect is actually **in the meaning, not the structure.**"
>
> "**행이 있다는 것과 행이 맞다는 것은 다릅니다.** 결함은 **구조가 아니라 의미에** 있습니다."

### 조용한 실패 3유형 (기사 박스감)

| 유형 | 증상 | 원문 |
|---|---|---|
| 잘못된 조인 | 합계가 부풀려지는데 **일주일간 아무도 의심하지 않음** | [3:14] "a wrong join can inflate totals ... nobody questions it for a week" |
| 새 null 차원 | 오류 경로가 아니라 **기본 버킷으로 흘러들어 보이지 않게 됨** | [3:31] "records into a default bucket rather than an error path ... they become invisible" |
| 타입 문제 | **값이 없는 것과 값이 잘못된 것의 구분이 조용히 지워짐** | [3:46] "silently erase the distinction between if the value is missing or if the value is malformed" |

### 인용 — 기존 검사로는 안 잡힌다

> **[5:52]** *(1월 15일 주문 사례)* "An order placed on January 15th **should carry the gold tier, not both gold and silver tiers.** But surely our traditional checks will be able to catch this, right? **Nope.** A schema check, a row count check — **they won't catch it.**"
>
> "1월 15일에 들어온 주문은 **골드 등급을 달아야지, 골드와 실버를 둘 다 달면 안 됩니다.** 그런데 기존 검사들이 이걸 잡아 주겠죠? **아닙니다.** 스키마 검사, 행 개수 검사 — **못 잡습니다.**"

> **[6:14]** "I'm not here to say these checks are useless. **They are really useful when used for answering real operational questions** — how the cluster behaves, what the job status is, whether the schema is consistent."
>
> "이 검사들이 쓸모없다는 말이 아닙니다. **실제 운영상의 질문에 답할 때는 정말 유용합니다.** 클러스터가 어떻게 동작하는지, 작업 상태가 어떤지, 스키마가 일관된지 같은 것들이요."

### 기사 활용 각도

- **"그럴듯한 출력이 가장 위험하다"**는 LLM 환각의 정확한 데이터 버전이다. Denny Lee(B-03)의
  "환각은 우리가 원하는 창의성인데, 일어나면 틀린 것"과 **개념적으로 같은 지점**이다.
  서로 다른 세션·다른 회사인데 같은 문제를 말한다.
- **AI 이전에도 있던 문제**라는 사실이 기사에 균형을 준다. "AI 때문에 생긴 문제"가 아니라
  "AI가 규모를 키운 오래된 문제"라는 서술이 더 정확하다.
- Guvenc(B-09)의 "겉보기엔 잘 돌아가는데 쉽게 뚫리는 애플리케이션"과 3중 교차를 이룬다.

## B-07. Amit Dubey — 자가 치유를 넘어: 공급망이 스스로 최적화하게

| 항목 | 내용 |
|---|---|
| 화자 | Amit Dubey (Founder & CEO, DataFlux.ai) — 의료·항공우주·방산 컨설팅 20년 |
| 행사 | InformsCon 2026, 2026-07-31, Everest Reception Hall, Bellevue |
| 영상 | https://youtu.be/Dr1tT0fz6qU |

> ⚠️ **전사 품질 경고 (M8 필수)**: 이 트랜스크립트는 Whisper 전사 오류가 눈에 띄게 많다.
> 확인된 것만 해도 "Beyond Self-**Trading**"(→ Self-Healing), "3.3 million **partners**"(→ parts),
> "simple **leading** programming"(→ linear programming), "**non-polar** simulation"(→ Monte Carlo) 등이다.
> **이 자료에서 직접 인용을 쓸 경우 반드시 원 영상 음성으로 대조**해야 한다. 수치도 마찬가지다.
> 아래는 맥락상 명백한 것만 정리했고, 인용은 최소화했다.

### 장면 — 열병 비유 (기사에 옮기기 좋음)

> **[3:51]** "In 2021, the supply chain — as you know, our body, if it goes through a fever, the body temperature will rise because of the infection. Just like that, **supply chain went through a fever**, and everybody was overstocking, overordering, and that left a massive amount piling up in the warehouse. ... And then, as our body recovers after fever — **that fever is over, but the items are still lying on the floor, so the recovery wasn't there.**"
>
> "2021년 공급망은 — 우리 몸이 감염으로 열이 나면 체온이 오르잖습니까. 꼭 그렇게 **공급망이 열병을 앓았습니다.** 다들 과잉 재고를 쌓고 과잉 주문을 했고, 그게 창고에 산더미로 남았습니다. ... 그리고 몸은 열이 내리면 회복하는데, **열은 끝났는데 물건은 여전히 바닥에 쌓여 있었습니다. 회복이 없었던 겁니다.**"

> **[5:00]** "What should the warehouse planners, supply chain planners, and expeditors do? **Because the cost is already sunk.** The warehouse is overflowing with inventory **which nobody wants.**"
>
> "창고 계획자, 공급망 계획자, 독촉 담당자는 뭘 해야 합니까? **비용은 이미 매몰됐습니다.** 창고는 **아무도 원하지 않는** 재고로 넘칩니다."

### 수치 (전부 M8 음성 대조 대상)

| 수치 | 원문 | 비고 |
|---|---|---|
| 항공기 1대에 약 **330만 개** 부품 | [6:01] "One airplane requires around 3.3 million parts" | 전사본은 "partners"로 오기 |
| 2021~2022 공급망 교란 약 **35%** | [6:11] "around 35% supply chain disruptions have occurred" | 원인: 코로나, 전쟁, 봉쇄, 유럽 화산 폭발 |
| 서비스 수준 **97.3%** (신뢰도 95%) | [9:06] "97.3 percent service level with 95 percent confidence" | 하이브리드(LP+몬테카를로) 결과 |

### 인용 — 에이전트가 먼저가 아니었다

> **[8:28]** "**I did not start with agents, because back then agents were still on the paper.** So I started with this."
>
> "**저는 에이전트로 시작하지 않았습니다. 그때는 에이전트가 아직 논문 속에 있었으니까요.** 그래서 이것부터 시작했습니다."

→ 선형계획법 → 몬테카를로 → 하이브리드 순으로 쌓은 뒤 **마지막에 에이전트를 얹었다**는 순서가 중요하다.
Vivek Radhakrishnan(B-09)의 **"문제 전체를 푸는 데는 운영 연구가 전부"**[7:44]와 정확히 같은 입장이다.
서로 다른 발표자가 같은 행사에서 같은 결론에 도달했다.

### 기사 활용 각도

- **열병 비유**는 공급망을 모르는 한인 독자에게 문제를 즉시 이해시킨다. 비전문 매체에 적합하다.
- "에이전트를 나중에 얹었다"는 순서는 **AI를 먼저 놓고 문제를 찾는 방식에 대한 반례**다.
  Guvenc(B-09)의 "최적화 말고 생성 AI 달라"와 짝으로 배치하면 강하다.
- 다만 **전사 품질 문제로 직접 인용은 최소화**하고, 개념과 비유 위주로 쓰는 것이 안전하다.

## B-02. Miriam Alvarez-Pintor — 기술을 이해하고 가능성을 여는 법

| 항목 | 내용 |
|---|---|
| 화자 | Miriam Alvarez-Pintor |
| 소속 | **Senior Data Scientist, Boeing** (13년) · President, ASA Puget Sound 지부 |
| 이력 | 순수수학 학사·응용통계 석사 / 특허 출원 2건 · 영업비밀 3건 / Boeing 사내 엔지니어 대상 데이터사이언스 강의 연 2회 / 켄트시 공원위원회 위원 · K-1 축구 코치 |
| 행사 | ACM Data Conclave, 2026-07-30, Everest Reception Hall, Bellevue |
| 영상 | https://youtu.be/GjUneZn9AA0 |

> **시애틀 산업의 앵커인 보잉의 현직 시니어 데이터 사이언티스트.** 한인 매체 독자에게 보잉은
> 설명이 필요 없는 이름이라 인용의 무게가 다르다. 발표 자체가 비전문가 눈높이라 기사에 옮기기 쉽다.

### 인용 — 성숙도 단계를 건너뛰는 것이 문제다 (교차 주제 3 확증)

> **[11:48]** "A lot of times I see teams jumping already — they're so excited, it's like *oh, AI is out, I want to use it, I want to buy it* — and they start creating solutions that leverage the cognitive self-learning analytics component **without even really understanding the first elementary steps of what is happening.**"
>
> "팀들이 이미 건너뛰는 걸 자주 봅니다. 잔뜩 들떠서 *AI가 나왔대, 써야지, 사야지* 하면서 인지·자가학습 분석 기능을 활용하는 솔루션을 만들기 시작합니다. **정작 무슨 일이 일어나고 있는지 가장 기초적인 단계도 이해하지 못한 채로요.**"

> **[12:32]** "A lot of businesses **get rolled down because they jumped all the way to the AI without really understanding what is happening in their businesses.**"
>
> "많은 기업이 무너집니다. **자기 사업에서 무슨 일이 일어나고 있는지도 모른 채 AI로 곧장 건너뛰었기 때문입니다.**"

> **[13:05]** "If we don't take those steps to understand those key components, **we essentially end up in a loop where we never solve any type of problem. We're just in a loop of using these tools**, and we never get to: *hey, are we really solving what we are observing in the business?*"
>
> "핵심 요소를 이해하는 단계를 밟지 않으면, **결국 아무 문제도 풀지 못하는 순환에 갇힙니다. 그냥 도구를 쓰는 순환일 뿐입니다.** 그리고 끝내 이 질문에 도달하지 못합니다. *우리가 사업에서 관찰한 그 문제를 정말 풀고 있는가?*"

→ **Guvenc Degirmenci(B-09)의 "최적화 말고 생성 AI 달라"와 정확히 같은 현상**을 다른 각도에서 말한다.
Guvenc는 AWS, Miriam은 Boeing. 행사도 다르다(InformsCon 7/31 vs ACM 7/30).
**교차 주제 3이 이로써 4개 행사 4인의 증거를 갖는다.**

### 건너뛰면 안 되는 4단계 (기사 도식감)

발표에서 제시한 분석 성숙도 사다리다. 한인 독자에게 **AI 도입 자가진단 도구**로 쓸 수 있다.

| 단계 | 질문 | 영문 |
|---|---|---|
| 1. 기술적 분석 | **무슨 일이 일어났는가?** | descriptive |
| 2. 진단적 분석 | **왜 일어났는가?** | diagnostic |
| 3. 예측적 분석 | **무슨 일이 일어날 것인가?** | predictive |
| 4. 처방적 분석 | **그래서 무엇을 해야 하는가?** | prescriptive |
| → 그다음이 AI | 인지·자가학습 | cognitive |

> **[12:13]** "If you don't take these fundamental steps — descriptive, why did it happen with diagnostic, what will happen with predictive, and then **what should we do about it** with prescriptive — it's really hard to then create [the rest]."

### 인용 — AI는 도구상자에 하나 더 들어온 도구다

> **[11:11]** "AI hasn't changed any of that. We've been doing that over time — **from the time we used to calculate things with paper or pencil, to using a TI-89, to progressing to programming**, and so forth. **AI is just another tool in our toolbox** that we're adding, but we're processing all this data a lot faster than we even thought we could."
>
> "AI가 그걸 바꾼 건 아닙니다. 우리는 늘 해 왔습니다. **연필과 종이로 계산하던 시절부터, TI-89 계산기를 쓰다가, 프로그래밍으로 넘어가고**, 그렇게요. **AI는 우리 도구상자에 하나 더 들어온 도구일 뿐입니다.** 다만 우리가 상상했던 것보다 훨씬 빠르게 데이터를 처리하고 있는 거죠."

> ⭐ **주목할 일치**: Emmy Smith(B-09, Candela/전 AWS)도 하루 뒤 InformsCon에서 거의 같은 표현을 썼다.
> [2:24] "AI just gives us **another tool in our toolbox.**" **서로 다른 회사·행사·날짜에서 나온 사실상 동일한 문장**이다.
> 기사에서 두 인용을 나란히 배치하면 "현장의 합의"를 보여줄 수 있다.

### 인용 — AI가 사람처럼 하지는 못한다

> **[8:37]** "It's essentially doing that whole thing that our brain generally does every day — consuming data, creating meaning, and making a decision. So now we're teaching other things to do the same thing. **But it will never do it the way we do, because we've had experiences over generations, decades, thousands of years. We've evolved to do that, and our brain is very powerful.**"
>
> "결국 우리 뇌가 매일 하는 일을 하는 겁니다. 데이터를 받아들이고, 의미를 만들고, 결정을 내리는 것이요. 이제 우리가 다른 것에게 같은 일을 가르치고 있는 겁니다. **하지만 우리가 하는 방식으로는 절대 하지 못합니다. 우리는 세대와 수십 년, 수천 년에 걸친 경험이 있고, 그렇게 진화했으며, 우리 뇌는 매우 강력하니까요.**"

### 인용 — 기계학습을 한 문장으로

> **[7:34]** "In the past, **humans wrote rules, fed them data, and got answers.** Machine learning **takes that data, takes the answers, and generates the rules.**"
>
> "예전에는 **사람이 규칙을 쓰고, 데이터를 넣어서, 답을 얻었습니다.** 기계학습은 **데이터와 답을 받아서 규칙을 만들어 냅니다.**"

→ **비전문 독자에게 기계학습을 설명하는 가장 간결한 문장.** 한인 매체 기고문의 배경 설명 단락에
그대로 쓸 수 있다. 수학(결정론) → 통계(불확실성 정량화) → ML → AI의 계단 설명도 함께 쓸 수 있다.

### 장면 — 알람 스누즈로 설명한 데이터

> **[2:38]** "How many times do you snooze that alarm? You've determined, based on all the data you've collected on past experiences, that **if you snooze the alarm three times, you get those golden extra minutes** of sleep and still make it on time. **But if you snooze that extra fourth time, you've made it late.**"
>
> "알람을 몇 번 미루십니까? 과거 경험에서 모은 데이터를 근거로 이미 판단하셨을 겁니다. **세 번 미루면 그 황금 같은 몇 분을 더 자면서도** 제시간에 도착한다는 걸요. **그런데 네 번째로 한 번 더 미루면 지각입니다.**"

→ 한인 매체 독자에게 "데이터 기반 의사결정"을 설명하는 최적의 예시. **일상 언어라 번역 손실이 없다.**

### 기사 활용 각도

- **연재의 배경 설명 단락을 이 발표 하나로 해결할 수 있다.** 보잉 현직자가 일상 언어로 설명한 것이라
  기자가 직접 설명하는 것보다 신뢰도가 높다.
- **4단계 성숙도 사다리는 독자 자가진단 박스**로 뽑는다. "우리 회사는 1단계도 안 됐는데 AI부터 사려는 건 아닌가."
- "AI는 도구상자의 도구 하나" — Boeing과 Candela(전 AWS) 두 사람이 각기 다른 행사에서 같은 말을 했다는
  사실 자체를 기사에 쓴다. **현장의 합의**를 보여주는 가장 강한 방식이다.
- 보잉·ASA 지부장·켄트시 공원위원·유소년 축구 코치라는 이력 조합은 **"기술자도 지역 공동체 사람"**이라는
  시애틀 생태계의 결을 보여준다. 인물 소개 한 줄로 쓸 값이 있다.

## B-08. Karl Joseph Weaver — 저궤도 위성 생태계와 다중궤도 우주 경쟁

| 항목 | 내용 |
|---|---|
| 화자 | Karl Joseph Weaver (Founder, Newport Technologies) — 무선통신·IoT·위성 30년 |
| 이력 | 대만·중국·싱가포르·네덜란드 근무. 발표 중 **중국어로 인사**하는 장면 있음 [1:22] |
| 행사 | InformsCon 2026, 2026-07-31, Everest Reception Hall, Bellevue |
| 영상 | https://youtu.be/JWGEwcthshI |

> ⚠️ **전사 품질 경고**: 오전사 다수. "geosatellites have been up in **Norway**"(→ in orbit),
> "smartphone **DVD** services"(→ D2D), "**Dave and Kyle** situation"(→ David and Goliath),
> "Starship, which equals **Starbucks**"(농담). **직접 인용 시 원 음성 대조 필수.**

### 인용 — 시애틀이 위성·로켓의 "그라운드 제로"다 (지역성 근거)

> **[6:11]** "**We are sitting in ground zero for satellite R&D and rocket R&D in this country — and also assembly and manufacturing.** Do you guys know that?"
>
> "**우리는 이 나라 위성 연구개발과 로켓 연구개발의 그라운드 제로에 앉아 있습니다. 조립과 제조도요.** 여러분 이거 아셨습니까?"

> **[3:12]** "There actually is **a new space race** going on right now. **The guy's up in Redmond Ridge** — Elon Musk. He's got SpaceX, Starlink, Starship."
>
> "지금 실제로 **새로운 우주 경쟁**이 벌어지고 있습니다. **그 사람은 레드먼드 리지에 있습니다.** 일론 머스크죠. SpaceX, 스타링크, 스타십을 갖고 있습니다."

> **[5:37]** "Starlink has **36 airlines** using this technology now. ... We are an Amazon country. So let's call **Amazon Leo** — because it's competition. We need lots of competition. **36 to 1.**"

→ **시애틀 지역성 섹션의 강력한 보강.** v1은 이 대목을 GeekWire의 OpenAI·xAI 벨뷰 사무실 기사로만
채웠는데, 여기 **위성·로켓 축**이라는 완전히 다른 산업 근거가 현장 발언으로 있다.
스페이스X(레드먼드), 아마존 Leo(커클랜드 인근)로 **이스트사이드 회랑이 AI 사무실만의 이야기가 아님**을 보여준다.

### 반론 — 업계 종사자 본인의 과장 경계

> **[4:37]** "By the way, **there's a little bit of hype in the industry right now.** You can take your iPhone and demo a satellite text message, but **it's not very sexy and it's very simple.** And you will only get that service if you have a T-Mobile plan and if you go into a dead zone."
>
> "그런데 말이죠, **지금 업계에 과장이 좀 있습니다.** 아이폰으로 위성 문자 메시지를 시연할 수 있지만 **그렇게 대단한 것도 아니고 아주 단순합니다.** 게다가 T-Mobile 요금제가 있고 음영지역에 들어가야만 됩니다."

> **[5:14]** "**But streaming video, audio — we're not quite there. I'm sorry to say.** We will get there."
>
> "**하지만 영상이나 음성 스트리밍은 아직입니다. 유감스럽게도요.** 언젠간 되겠지만요."

→ **교차 주제 3(AI/기술 열풍이 실제를 가린다)의 위성 버전.** 업계 사람이 직접 "과장이 있다"고 말한
것이라 기사에서 균형추로 쓰기 좋다.

### 수치·사실

| 항목 | 원문 |
|---|---|
| Starlink 이용 항공사 **36개** | [5:31] "Starlink has 36 airlines using this technology now" |
| 정지궤도 위성 **60년 이상** 역사, 다수 기업 **투자수익 부진** | [3:51] "geosatellites have been up ... more than 60 years ... they've not been very successful. The return on investment is not very good" |
| 위성 수명 **5~7년** (Q&A 주제) | 챕터 [54:39] "the true cost of satellites lasting only 5-7 years" |

### 미채굴 구간 (기사에서 필요 시 추가 확인)

발표 후반에 **교차 주제 5(물리 제약)와 직결되는 대목**이 챕터 표시로 남아 있다. 이번 채굴에서는
전반부만 정독했으므로, M6·M7에서 해당 주제를 두껍게 해야 할 경우 아래 구간을 표적 확인한다.

| 타임스탬프 | 내용 |
|---|---|
| [45:15] | **AI가 들어가는 지점** — 자가치유 네트워크, 궤도 로봇 |
| [46:03] | **StarCloud, 우주 데이터센터** ← 주제 5(전력·물리 제약)와 직결 |
| [48:17] | 중국·인도의 NTS 위성 금지, 글로벌 사우스 백서 |

### 기사 활용 각도

- **"위성·로켓의 그라운드 제로"**는 시애틀 지역성을 AI 밖으로 확장한다. 한인 독자에게
  "이 동네에 이런 산업도 있다"는 정보 가치가 있다.
- 업계인의 **자체 과장 경계**는 기사 균형에 기여한다.
- 다만 전사 품질 문제로 **개념·수치 위주로 쓰고 직접 인용은 최소화**한다.

## B-05 · B-06. Spark 스트리밍 세션 2건 — 밀리초의 벽

| 항목 | 내용 |
|---|---|
| 화자 | **Sudhanva Huruli** (PM, Databricks — 스트리밍 플랫폼 및 오픈소스 Spark Declarative Pipelines) |
| 함께 | Structured Streaming 세션 (같은 행사, 앞 발표) |
| 행사 | Spark + AI: Ignite the Future |
| 영상 | https://youtu.be/v73ucqAIDEk · https://youtu.be/ZtlmOOHJdZ0 |

> **기사 기여도는 클러스터 B에서 가장 낮다.** 순수 기술 세션이라 한인 일반 독자 대상 연재에
> 직접 인용할 대목이 적다. 다만 **"기술 축이 실재했다"는 사실 증명**과 아래 한 가지 관찰을 위해 채굴했다.

### 관찰 — 인프라 개선은 여전히 "물리적 한계"와 싸운다

> **[1:17]** "More and more customers require that event time processing. **They need millisecond processing.** Micro-batch was really designed for **seconds to minutes**, and millisecond latency was a little bit out of reach. **The reason why it is out of reach is scheduling overheads.**"
>
> "점점 더 많은 고객이 이벤트 시간 처리를 요구합니다. **밀리초 단위 처리가 필요하다는 거죠.** 마이크로배치는 원래 **초에서 분 단위**로 설계됐고, 밀리초 지연은 손이 닿지 않는 영역이었습니다. **닿지 않는 이유는 스케줄링 오버헤드입니다.**"

> **[2:31]** "This introduced **platform fragmentation.** If you wanted to get to real-time mode, **you'd end up building different stacks entirely.**"
>
> "이것이 **플랫폼 파편화**를 낳았습니다. 실시간 모드가 필요하면 **결국 완전히 다른 스택을 따로 만들게 됩니다.**"

→ Denny Lee(B-03)의 **하네스 파편화**(Claude와 Codex가 각자 스킬을 갖게 되는 문제)와 같은 구조의 문제가
데이터 처리 계층에서도 나타난다. **"도구가 늘어날수록 스택이 갈라진다"**는 것이 이 행사의 반복 관찰이다.

### 수치

| 항목 | 원문 |
|---|---|
| 실시간 모드 목표 구간 **40밀리초~1초** | [2:56] "targeted for those use cases that are like 40 milliseconds to one second" |
| 기존 마이크로배치 설계 구간 **초~분** | [1:22] "designed for seconds to minutes" |
| 개선 방식 | **같은 엔진·같은 API·같은 코드**로 밀리초 도달 [2:43] |

### 장면 — 전날 밤 10시에 확정된 발표

> **[0:44]** "Before today, if you actually looked at the agenda, **I wasn't slated to speak here. I was a last-minute addition yesterday at like 10 p.m.**, but I'm super glad I showed up."
>
> "오늘 전까지 일정표를 보셨다면 **저는 발표자가 아니었습니다. 어제 밤 10시쯤 막판에 추가됐어요.** 그래도 오길 정말 잘했습니다."

→ Seattle Tech Week의 **분산·커뮤니티 주도 성격**을 보여주는 작은 장면. 250개 넘는 행사가
중앙 기획이 아니라 이런 식으로 굴러갔다는 것을 한 문장으로 보여준다. 기사에서 행사 성격을
설명할 때 쓸 수 있다.

### 기사 활용 각도

- **직접 인용은 권하지 않는다.** 대신 "같은 주에 벨뷰에서는 밀리초 단위 데이터 처리를 다루는
  기술 세션도 열렸다" 정도의 **행사 스펙트럼 서술**에 쓴다.
- **파편화 관찰**은 Denny Lee(B-03)와 묶어 교차 주제 6의 보조 근거로 쓸 수 있다.
- 전날 밤 10시 섭외 일화는 **행사의 성격 묘사**로 값이 있다.

## 클러스터 B 채굴 완료 (10 / 10)

| # | 화자 | 소속 | 행사 | 기사 기여도 |
|---|---|---|---|:--:|
| B-01 | Muazma Zahid | Google (Group PM) | ACM Data Conclave | ★★★ |
| B-02 | Miriam Alvarez-Pintor | **Boeing** (Senior Data Scientist) | ACM Data Conclave | ★★★ |
| B-03 | Denny Lee | Databricks | Spark + AI | ★★☆ |
| B-04 | Kunal Jain | 커머스 데이터 플랫폼 (벨뷰) | Spark + AI | ★★★ |
| B-05 | Sudhanva Huruli | Databricks | Spark + AI | ★☆☆ |
| B-06 | (Structured Streaming 세션) | — | Spark + AI | ★☆☆ |
| B-07 | Amit Dubey | DataFlux.ai | InformsCon | ★★☆ |
| B-08 | Karl Joseph Weaver | Newport Technologies | InformsCon | ★★☆ |
| B-09 | Emmy Smith · Guvenc Degirmenci · Vivek Radhakrishnan · Apoorv Mathur | Candela · AWS · OR/ML · Siemens | InformsCon | ★★★ |
| B-10 | Ziqi Wang | Biuty.ai | Consumer Experiences | ★★☆ |
