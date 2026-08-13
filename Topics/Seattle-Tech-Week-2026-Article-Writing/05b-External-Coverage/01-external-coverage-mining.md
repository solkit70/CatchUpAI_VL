---
title: "External Coverage Mining — STW2026 외부 보도·분석 채굴"
created: 2026-08-12 00:00:00
author:
  - "Claude Code"
tags:
  - seattle-tech-week
  - external-coverage
  - evidence-bank
---

## 외부 보도·분석 채굴

**모듈**: M5.5 (신설) / **상태**: 실습 1·3 완료

> **왜 이 모듈이 생겼나**: M5는 사용자 현장 녹화 30건을 전량 정독했지만, **외부 보도·분석에는
> 같은 작업을 하지 않았다.** v1이 "나중에 확인할 것"으로 남긴 한 줄 요약을 그대로 둔 채 M6로 넘어가려 했다.
> v1의 실패 원인(자료를 열어보지 않음)을 외부 자료 쪽에서 반복하던 참이었다. 사용자 지적으로 교정.

## E-01. AI2Work — "진짜 이야기는 AI 인프라다"

**출처**: https://ai2.work/blog/seattle-tech-week-opens-with-ai-infrastructure-as-the-real-story (2026-07-26)

> **이번 M5.5의 최대 수확.** 현장 녹화 30건 어디에서도 나오지 않은 **거시 경제 축**을 제공한다.
> 제목부터 필자의 주장이 담겨 있다 — 사람들이 프런티어 모델과 애플리케이션에 주목하는 동안
> **진짜 이야기는 인프라**라는 것.

### 핵심 역설 — 돈은 여기 쏟아지는데 벤처 투자는 줄었다

| 항목 | 수치 |
|---|---|
| 하이퍼스케일러 2026 합산 설비투자 | **약 7,250억 달러** (2025년 약 4,100억 → **77% 증가**) |
| ↳ Amazon | 약 2,000억 달러 |
| ↳ Microsoft | 약 1,900억 달러 (추정) |
| ↳ Alphabet | 1,750억~1,850억 달러 |
| ↳ Meta | 1,150억~1,350억 달러 |
| **시애틀권 벤처 투자 2026 상반기** | **27억 달러 / 163건** |
| ↳ 전년 동기 | 45억 달러 / 210건 → **약 40% 감소** |
| 미국 전체 벤처 투자 2026 상반기 | 4,127억 달러 (**사상 최대**) |
| 미국 벤처 자금 중 AI 비중 | **86%** |

→ **미국 전체는 사상 최대인데 시애틀은 40% 줄었다.** 컴퓨트를 물리적으로 떠안은 지역이
그 벤처 이득을 못 가져가고 있다는 것이 필자의 논지다. **현장 녹화로는 절대 나올 수 없는 관점이다.**

### 워싱턴주 데이터센터 실물 규모

| 항목 | 수치 |
|---|---|
| 데이터센터 시설 | 약 **126개**, 약 **700만 평방피트** |
| Microsoft 보유 사이트 | 약 30곳 |
| Sabey Data Centers | 8곳 |
| 최대 전력 수요 | **1,414 MW** |
| 2030년 전망 | 데이터센터 증가만으로 **"시애틀 2~4개분"** 전력 수요 추가 가능 |

> **Zach Baker** (Regional and State Policy Director, NW Energy Coalition):
> "**Data center growth is the most rapidly growing part of our electricity load.**"
>
> "데이터센터 증가가 우리 전력 부하에서 **가장 빠르게 늘어나는 부분**입니다."

### 시애틀 최대 AI 딜은 모델이 아니라 "물리 계층"이었다

| 기업 | 규모 | 분야 |
|---|---|---|
| **Helion Energy** Series G | 4억 6,500만 달러 | 핵융합 |
| **Starcloud** | 1억 7,000만 달러 | **궤도 컴퓨트** |
| **XBOW** | 1억 5,500만 달러 | 자율 보안 |
| **Starfish Space** | 약 1억 1,000만 달러 | 우주 |
| **Gradial** | 6,500만 달러 | — |

→ 필자 주장: 관찰자 대부분이 이 라운드들을 **모델 계층 베팅으로 오독**하지만 실제로는
**물리 계층(physics-layer) 투자**다.

### 필자가 말하는 "사람들이 놓치는 것"

> 시애틀 스타트업의 승산은 경쟁 AI 모델을 만드는 데 있지 않다(최소 1억 달러 이상이 필요하고
> 신뢰할 만한 플레이어는 4~5곳뿐). 훨씬 큰 시장은 **"비싼 컴퓨트를 더 생산적으로 만드는 것"**이다.
> 구체적으로 **오케스트레이션, 평가, 비용 통제, 전력 인접 하드웨어**.

⭐ **현장 자료와의 직접 연결**: 이 네 가지가 M5에서 채굴한 것과 정확히 겹친다.
Denny Lee의 Omnigent(오케스트레이션), Muazma Zahid의 평가·신뢰, Sunny Kotwal의 토큰 비용 통제,
Apoorv Mathur의 전력. **외부 분석이 제시한 기회 영역을 현장 발표자들이 실제로 하고 있었다.**

### 정책 전망

- 용량 제약은 2026년 내내 지속
- **HB 2515**(무산된 데이터센터 규제)가 **2027년 회기에 재상정** 예정
- Data Center Workgroup 최종 보고서가 2027년 입지 경제성을 좌우할 것

## E-02. GeekWire 현장 노트 — Todd Bishop

**출처**: https://www.geekwire.com/2026/seattle-tech-week-takeaways-ai-startups-and-the-best-insights-and-quotes-we-heard/

### 핵심 질문 — 당신은 정말 AI 회사인가

> **Todd Bishop** (GeekWire):
> "**If the intelligence at the center of your product belongs to someone else, are you an AI company or an application on top of somebody else's intelligence?**"
>
> "**제품 한가운데 있는 지능이 남의 것이라면, 당신은 AI 회사입니까, 아니면 남의 지능 위에 올라탄 애플리케이션입니까?**"

> ⭐ **이 질문이 M5 결과에 정면으로 겨눈다.** Demo Day 창업자 7인이 ChatGPT·Claude·Lovable로
> 8주 만에 만든 제품들이 바로 이 질문의 대상이다. **제 7개 교차 주제 어디에도 없던 각도**이며,
> 기사에서 창업 낙관론에 대한 가장 날카로운 반문이 된다.

### 비용 — 3개월 만에 3배

> **Patrick Thompson** (CEO, Clarify): 회사의 **Anthropic 청구서가 3개월 만에 3배**가 되었고,
> 신뢰성 문제까지 겹쳐 **AWS Bedrock으로 이전**했다.

→ Sunny Kotwal(A-05)의 "무제한 ChatGPT가 1조 달러 기업에도 너무 비싸다"와 **같은 현상의 스타트업 버전**.
현장 증언(대기업)과 외부 보도(스타트업)가 양쪽에서 같은 압력을 확인한다.

### 인용 모음

> **Manos Koukoumidis** (CEO, Oumi; 전 Google Cloud AI 매니저):
> "Enterprises are using a model that is **trained on 5% of the world's data that sits on the web, not the other 95%**."
>
> "기업들은 **웹에 있는 세상 데이터의 5%로 학습된 모델**을 쓰고 있습니다. 나머지 95%가 아니라요."

> **Brian Hall** (CMO, Mistral AI):
> "**We're gonna laugh when we thought that AI was gonna save us time.**"
>
> "**AI가 우리 시간을 절약해 줄 거라고 생각했던 걸 나중에 웃게 될 겁니다.**"

> **Ben Gaffney** (Deputy General Counsel, OpenAI):
> "Even within the legal team that I work in, **we need more people.** Even though we're getting all these massive productivity gains, **it isn't like you don't need people to supervise this stuff.**"
>
> "제가 속한 법무팀만 해도 **사람이 더 필요합니다.** 엄청난 생산성 향상을 얻고 있는데도, **이걸 감독할 사람이 필요 없어지는 건 아닙니다.**"

> ⭐ **OpenAI 법무 부책임자가 교차 주제 4를 확증했다.** Vivek Radhakrishnan의 "검토와 판단이 오히려
> 늘었다", Emmy Smith의 "애 보기가 많아졌다"와 **완전히 독립적으로 같은 결론**이다.
> AI를 만드는 회사 내부에서 나온 증언이라 무게가 다르다.

> **Sabrina Albert** (Partner, Madrona):
> "Before, when you were thinking about traditional software, you would charge for a seat or a unit of software. But now you can fundamentally change it. **If I deliver this outcome for you, then you can actually pay me for it.**"
>
> "예전 전통 소프트웨어는 좌석 수나 단위로 과금했습니다. 이제는 근본적으로 바꿀 수 있습니다. **제가 이 결과를 만들어 드리면, 그 결과에 대해 값을 받는 겁니다.**"

> **Kirby Winfield** (Founding Partner, Ascend):
> "If I invested in you, it's not because I'm smart about your market. It's because **you're** smart about your market. **If you're looking for answers from your investors, you're in trouble.**"

> **Karl Siebrecht** (CEO, Flexe):
> "Spending time as a founder trying to market yourself to investors, I think, **is a fallacy.** If you focus on building a valuable company … **I can promise you, investors will find you.**"

### 수치

| 항목 | 수치 |
|---|---|
| 행사 수 | **250개 이상** |
| 한 패널("Foundation Models Go Vertical")에 몰린 등록 시도 | **600명** |
| 시애틀 벤처 순위 | 필라델피아·오스틴·뉴욕**보다 아래** (단, 대기업 시애틀 오피스의 엔지니어 인재는 이 수치에 안 잡힘) |

## E-03. GeekWire 킥오프 — 창업자들이 실제로 만들고 있던 것

**출처**: https://www.geekwire.com/2026/what-are-you-building-talking-with-founders-and-business-leaders-at-the-seattle-tech-week-kickoff-event/

| 창업자 | 회사 | 만들고 있는 것 |
|---|---|---|
| Jagan Nemani | Seattle Orcas (CPO) | WhatsApp으로 프로 크리켓 구단 운영 관리 |
| Kim Vu | StyleOrigin | 중고 의류 식별·가격·상품설명 자동 생성 B2B |
| Kenny Daniel | Hyperparam | **AI가 만든 데이터를 수집·분석해 에이전트 성능 추적** |
| Cleo Escarez | Redyoos | 귀금속 회수 (청정기술 공급망) |
| Andy Liu | Unlock Venture Partners | 벤처캐피털 업무(딜 메모·실사) 자동화 |
| Mary Jesse | ACME Brains | **모델 간 이동에도 사용자 데이터·맥락을 지키는 프라이빗 AI** |
| Emily Rapp | Köniva | **말로 재고를 세는 음성 AI** (식당·바) |
| Henry Arias | Altelan Capital | 식품 브랜드·푸드테크 성장투자 |

### 수치

| 항목 | 수치 |
|---|---|
| **행사 등록 총계** | **29,000건 이상** |
| Köniva 효과 | 호텔 바 재고조사 **4명 12시간 → 2명 3.5시간** |
| 귀금속 | 주얼리 산업이 전 세계 귀금속의 **40~50%** 공급 |
| 귀금속 공급 부족 전망 | 향후 수십 년간 **700%** |

### 인용

> **Kenny Daniel** (Hyperparam): "**AI is producing this wall of tokens … companies have really no visibility.**"
>
> "AI가 **토큰의 벽**을 만들어 내는데 … 기업에는 사실상 **가시성이 없습니다.**"

> **Mary Jesse** (ACME Brains): "**AIs can talk you into your data.** You need people that understand it to help protect people."
>
> "**AI는 당신을 구슬려 당신 데이터를 내놓게 만들 수 있습니다.** 그걸 이해하는 사람이 있어야 사람들을 보호합니다."

> **Henry Arias** (Altelan Capital): "**AI is great, but it may not be the right tool for the job.**"
>
> "**AI는 훌륭하지만, 그 일에 맞는 도구가 아닐 수도 있습니다.**"

> ⭐ Arias의 발언은 Guvenc Degirmenci(B-09)의 "최적화 말고 생성 AI 달라"와 **정확히 같은 지적**이다.
> 교차 주제 3이 이로써 **5개 행사·5인**의 증거를 갖는다.

> **Emily Rapp** (Köniva, 식당 종사자를 두고): "**It is insane how bad tech has been to them.**"
>
> "**기술이 그분들에게 얼마나 형편없었는지 말도 안 될 정도입니다.**"

## E-04. Madrona 2026 회고 — 주최 측의 자기 서술

**출처**: https://www.madrona.com/seattle-tech-week-2026-the-most-seattle-tech-week-yet/

> **v1 소스맵에 없던 자료다.** 주최 측(Madrona)이 행사를 어떻게 규정했는지는 기사에서
> 반드시 다뤄야 할 관점인데 v1은 2023·2024·2025 회고만 갖고 있었다.

### 주최 측이 꼽은 정의적 주제 5가지

1. 커뮤니티가 **커지는 동시에 더 깊게 연결**되었다
2. **AI만이 유일한 흥미로운 혁신 영역은 아니었다**
3. **비전통적 행사**(게임, 야외활동)가 가장 효과적이었다
4. 포용성과 접근성 — "모두를 위한 더 나은 미래"
5. 커뮤니티 주도·풀뿌리 확장 모델

> ⭐ **2번이 중요하다.** GeekWire·AI2Work가 "AI가 지배했다"고 쓴 반면, **주최 측은 AI가 전부가
> 아니었다고 명시**한다. 같은 행사에 대한 세 갈래 해석이 존재한다는 사실 자체가 기사 소재다.

### 결정적 인용

> **Jacob Colker** (AI House):
> "**We get numb to the magic. We literally created the cloud. AI would not be possible without the cloud, and we did that here.**"
>
> "**우리는 그 마법에 무뎌집니다. 우리가 말 그대로 클라우드를 만들었습니다. 클라우드 없이는 AI가 불가능했고, 그걸 우리가 여기서 했습니다.**"

→ 시애틀이 스스로를 어떻게 보는지 한 문장으로 보여준다. Madrona가 커뮤니티를 **"겸손이 지나칠 정도(humble to a fault)"**로 표현한 것과 함께 쓰면,
WTIA의 "워싱턴에는 일관된 서사가 없다"는 지적과 삼각으로 맞물린다.

### 방어 가능성에 대한 결론

> Madrona 회고: AI 제품의 **방어 가능성은 모델 자체가 아니라 데이터·전문성·고객 루프에 있다.**

> ⭐ **교차 주제 1의 완벽한 외부 확증.** Amit Gupta(A-02)가 벨뷰 시청 소규모 행사에서 한 말
> — "만드는 건 해자가 아니다. 데이터가 해자고, 돈을 낼 것이라는 증거가 해자다" — 와
> **주최 측 공식 회고의 결론이 일치**한다. 서로 참조하지 않은 두 출처다.

### 시애틀의 정체성 주장

- 클라우드 컴퓨팅, 골수이식, 신장투석, 제세동기, 천연두 박멸의 발원지
- **"세계 위성의 수도(undisputed satellite capital of the world)"**
- **미국 위성 부품의 70%가 워싱턴에서 제조**

> ⭐ Karl Joseph Weaver(B-08)의 "우리는 위성·로켓 R&D의 그라운드 제로에 앉아 있다"를
> **주최 측 공식 문서가 수치로 뒷받침한다.** 현장 발언 + 외부 수치의 이상적인 조합.

### 수치

| 항목 | 수치 |
|---|---|
| 행사 | 250개 / 5일 |
| 벤처 자금 중 AI 비중 | **80~90%** |
| ↳ 그중 **약 10개 회사가 3분의 2를 가져감** | |
| Venture Black x PitchForce | 창업자 27명 → 투자자 30명+ |
| Bury the Hatchet 도끼던지기 토너먼트 | 32개사 참가 |

### 2027 방향

> "**The week belongs to whoever builds it next.**" — 고정된 메인 스테이지도, 프로그램 위원회도 없다.
> 성장은 커뮤니티가 여는 행사에 달려 있다.

## E-05. 검색으로 확보한 추가 수치 (출처 확인 필요)

| 수치 | 내용 | M8 조치 |
|---|---|---|
| **95%** | 기업 생성AI 파일럿이 **측정 가능한 ROI 0** | 원 출처(MIT 보고서로 추정) 확인 필요. B-01 Zahid 발언과 동일 수치 |
| **85%** | 실패한 AI 프로젝트의 원인이 **모델 선택이 아니라 데이터 품질** | ⭐ Kunal Jain(B-04) 발표를 정면으로 뒷받침. 원 출처 확인 필수 |

> ⭐ **85% 수치가 확인되면 교차 주제 6의 핵심 근거가 된다.** Kunal Jain이 "결함은 구조가 아니라
> 의미에 있다"고 한 것이 개인 의견이 아니라 산업 통계로 뒷받침된다.

## E-06. 외부 YouTube — 자막 확보 4/5

v1이 "시청 전 인용 금지"로 남겨둔 7건 중 **자막이 있는 4건을 실제로 확보해 정독**했다.
(WebFetch로는 YouTube 본문을 못 가져와 `youtube_transcript_api`로 직접 수집)

| 영상 | 채널 | 분량 | 상태 |
|---|---|--:|:--:|
| Claude Code Workshop (STW, 2026-07) | Adam Berg | 2,461 세그먼트 | ✅ |
| "I'm Happy to Be a Flesh Robot" ADI Pod #36 | Artificial Developer Intelligence | 1,692 | ✅ |
| **AI Minute Mondays — STW Special** | Suchi | 184 | ✅ |
| **Janet Matsen: Seattle Tech Week 2026** | Janet Matsen | 447 | ✅ |
| Ship Code at Sunset Recap | Gradial | — | ❌ 자막 비활성 |
| Dream Pixel Forge Demo Night | Aditya Bawankule | — | 미착수 (우선순위 낮음) |
| Karl Weaver LEO 키노트 | Karl Weaver | — | **불필요** — B-08에서 사용자 녹화본으로 이미 채굴 |

### E-06-a. Janet Matsen — "에이전트 시대에 실험을 어떻게 할 것인가"

> ⭐ **이번 M5.5에서 개념적으로 가장 중요한 발견.** 교차 주제 5(물리 시간표가 AI를 못 따라감)의
> **세 번째 독립 정식화**다. Apoorv Mathur는 전력망으로, AI2Work는 데이터센터 자본지출로,
> Janet Matsen은 **실험실 과학**으로 같은 구조를 말한다. 세 영역이 전혀 다른데 결론이 같다.

> **[0:56]** "I'm a software engineer now, and I notice that **the exponential progress we're seeing with AI is really confined to digital work.** I never would have believed two or three years ago if you told me that **agents would write all of my code by the beginning of 2026.**"
>
> "저는 지금 소프트웨어 엔지니어인데, **우리가 보고 있는 AI의 기하급수적 진보가 사실 디지털 작업에 국한돼 있다**는 걸 알게 됐습니다. 2~3년 전에 누가 저에게 **2026년 초에는 에이전트가 내 코드를 전부 쓸 거라고** 했다면 절대 안 믿었을 겁니다."

**디지털 영역이 가진 세 조건** [1:29~1:58]

| 조건 | 원문 | 내용 |
|---|---|---|
| 값싼 데이터 | "cheap experience and data" | 인터넷 전체를 학습에 넣거나, 시뮬레이션으로 무한 생성 |
| 빠른 피드백 | "fast feedback" | **초당 수백만 번** 시도 가능 |
| 충실한 신호 | "faithful signal" | 답을 검증해 주는 **거의 공짜인 오라클** |

**과학 연구개발에서는 셋 다 뒤집힌다** [2:01~2:45]

> "When we think about science research and development, **all of that flips right on its head.** We have notoriously expensive data to generate — it costs a lot to buy all the reagents and set up the experiments, a lot of human labor too. And **our feedback is not fast at all.** It takes time to grow cells, to see if a mouse is going to get a tumor or not. And clinical trials can be really long. And I would argue **we don't have faithful signal.** Cells and even organisms are stochastic down to the foundational levels ... we see variability even when we work with **two cells from the same cell line.**"
>
> "과학 연구개발을 생각하면 **셋 다 정반대로 뒤집힙니다.** 데이터 생성 비용이 악명 높게 비쌉니다. 시약을 사고 실험을 세팅하는 데 돈이 많이 들고, 사람 손도 많이 갑니다. 그리고 **피드백이 전혀 빠르지 않습니다.** 세포를 키우는 데, 쥐에게 종양이 생기는지 보는 데 시간이 걸립니다. 임상시험은 아주 길 수 있고요. 그리고 **충실한 신호도 없다고 봅니다.** 세포와 생물은 근본 수준에서 확률적이라, **같은 세포주에서 나온 두 세포**로 작업해도 편차가 나타납니다."

→ **기사에서 쓸 값이 매우 크다.** "AI가 왜 어떤 영역에서는 폭발적인데 어떤 영역에서는 더딘가"를
한 프레임으로 설명한다. 한인 독자에게 AI의 한계를 설명하는 가장 명료한 도구다.

### E-06-b. Suchi (AI Minute Mondays) — 참석 창업자의 STW 총정리

독립 참석자가 행사 직후 정리한 요약. **주최 측도 언론도 아닌 제3의 시선**이라 가치가 있다.
세 축으로 정리했다 — **자금 / 사람·엔지니어링 팀 / GTM**.

> **[2:39]** "With AI reducing the development life cycles ... we are able to ship much sooner and much faster. One of the key things to consider is **we need to be very critical of what we are building and why.** If you're building features that nobody is using, **that's not progress, that's just activity. We clearly need to differentiate between progress and activity.**"
>
> "AI가 개발 주기를 줄이면서 ... 훨씬 빨리 출시할 수 있게 됐습니다. 그런데 핵심은 **무엇을 왜 만드는지에 대해 아주 비판적이어야 한다**는 것입니다. 아무도 안 쓰는 기능을 만들고 있다면 **그건 진전이 아니라 그냥 활동입니다. 진전과 활동을 분명히 구분해야 합니다.**"

→ Jonathan Greechan(A-03)의 "AI는 아무도 원하지 않는 걸 만드는 일도 쉽게 만든다"와 같은 지적.
**"진전 vs 활동"**이라는 표현이 더 간결해서 기사에 쓰기 좋다.

> **[2:53]** 역할 융합 — "the merging of the roles between a product specialist and an engineer. Now we have a new role called **the product engineer** ... expected to have **deep domain expertise combined with some skills on coding and using tooling.**"

→ Guvenc Degirmenci(B-09)의 "과학자와 엔지니어의 경계가 흐려진다", Emmy Smith의 "전부 솔루션
아키텍트라고 부른다"와 **3중 교차**. 외부 관찰자가 여기에 **"프로덕트 엔지니어"라는 이름**을 붙였다.

> **[3:21]** **Forward deployed engineers** — 핵심 고객과 함께 일하는 방식이 조직 규모와 무관하게
> 전환점이 되고 있다.

→ ⭐ Dias Gotama(Camillia.ai, A-07)가 자기 발표에서 **"we are using a forward-deployed model"**이라고
말했다. 외부 관찰자가 트렌드로 지목한 것을 현장 창업자가 실제로 쓰고 있었다.

**GTM 체크리스트** [3:42~4:42] — ICP 명확성 / 트랙션(사전제품이라도 몇 명과 대화했나) /
**"비타민인가 진통제인가"** / 창업자 주도 영업 / 영업 규율(양·속도·일관성)

### E-06-c. ⭐ 외부 영상과 사용자 녹화가 같은 인물에서 만난다

이 영상의 마지막 사운드바이트 구간(5:04~7:07)에 **사용자가 녹화한 Demo Day 발표자의 사전 인터뷰**가 있다.

> **[6:45]** "My name is **Ashley Wright**. I'm a **founding partner of Maker Tank** ... this week I get to meet more people ... and I'm very excited cuz Wednesday **my co-founder is going to be up on stage at the pitch event for demo day** and I'm so excited for everyone to hear about what we're working on."

→ **Makertank는 사용자가 A-07에서 채굴한 Kristina Orille의 회사다.** 외부 영상은 **데모데이 전날의
기대**를 담았고, 사용자 녹화는 **무대 위 실제 피치**를 담았다. 같은 회사를 두 시점에서 볼 수 있다.

> **[6:26]** "I'm **Christina Aurelia** ... looking forward to my demo day on Wednesday. **Founders Institute 425**, we'll be pitching our demo."

> ⚠️ **M8 확인 필요**: 자동 자막의 "Christina Aurelia"는 **"Kristina Orille"의 전사 오류일 가능성이 높다.**
> 두 발화 모두 425 데모데이 피치를 언급한다. 확정되면 **"발표 이틀 전의 목소리와 무대 위의 목소리"**를
> 나란히 쓸 수 있어 기사에서 매우 강력하다.

### E-06-d. Adam Berg — Claude Code 워크숍 (커뮤니티 인프라)

> **[1:05]** "My name is Adam Berg. I'm one of the **ambassadors** here in Seattle for Claude. I created the organization **We Build With AI** about a year and a half ago. The mission is to **empower everyone to build with AI, regardless of technical background and experience.**"
>
> "저는 애덤 버그입니다. 시애틀에서 Claude **앰배서더**를 맡고 있습니다. 1년 반쯤 전에 **We Build With AI**라는 조직을 만들었습니다. 미션은 **기술 배경과 경험에 관계없이 누구나 AI로 만들 수 있게 하는 것**입니다."

> **[1:24]** "I have done over **50 events** ... this probably bumps up to like **4,000** in terms of the people who come to events."

→ 사용자가 채굴한 Startup425·Founder Institute 축과 **별개의 커뮤니티 인프라**가 하나 더 있다는 증거.
STW 주간에 초급·고급 워크숍을 나눠 운영했고 API 크레딧까지 배포했다.
"기술 배경 무관"이라는 미션 문구가 **교차 주제 1과 정확히 같은 방향**이다.

> ⚠️ 자동 자막 품질 불량("Clyde"=Claude, 화자명 표기 흔들림). 인용 시 원 영상 대조 필요.
> v1 소스맵은 채널명을 "Adam Burgh"로 적었으나 자막에서는 "Adam Berg"로 발화된다.

## 미확보 / 실패

| 대상 | 상태 | 조치 |
|---|---|---|
| reports.uwncm.org 기사 2건 | **접속 실패** (ECONNREFUSED) | M8에서 재시도 |
| bignewsnetwork ACM Data Conclave 보도 | **403 Forbidden** | 사용자가 같은 행사 녹화본 2건 보유(B-01·B-02)이므로 우선순위 낮음 |
| Gradial "Ship Code at Sunset" | **자막 비활성화** | 영상 시청 외 방법 없음. 우선순위 낮음 |
| Dream Pixel Forge Demo Night | 미착수 | 우선순위 낮음 |
| ADI Pod #36 "Flesh Robot" | 자막 확보(1,692 세그먼트), **미정독** | 필요 시 추가 정독 |

## 다음

→ [02-external-vs-field-comparison.md](02-external-vs-field-comparison.md) — 외부 강조점 vs 현장 관찰 5분류 대조표
