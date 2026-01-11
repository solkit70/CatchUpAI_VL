# Building the visual memory layer for AI - Ben Zhou (Memories.ai)

**원본 영상**: [https://www.youtube.com/watch?v=FbRcb8XryNg](https://www.youtube.com/watch?v=FbRcb8XryNg)
**작성일**: 2026-01-11
**Video ID**: FbRcb8XryNg

---

## 요약

Memories.ai의 CTO Ben Zhou가 AI를 위한 시각적 메모리 레이어 구축에 대해 발표했습니다. 이 회사는 비디오를 효율적으로 압축하고 인덱싱하여 AI 에이전트가 대량의 시각 정보를 처리할 수 있도록 하는 인프라와 모델을 개발하고 있습니다. 온디바이스 처리를 통해 프라이버시를 보호하면서도 낮은 지연시간으로 개인 미디어와 인터넷 비디오를 효율적으로 활용할 수 있게 합니다.

---

## 핵심 포인트

- AI가 인간처럼 문제를 해결하기 위해서는 텍스트뿐만 아니라 시각적 메모리가 필수적
- 비디오는 용량이 크기 때문에 효율적인 압축 및 인덱싱 레이어가 필요
- 온디바이스 처리를 통해 개인정보 보호 및 대역폭 절약 가능
- 삼성과 협력하여 로컬에서 작동하는 스마트 앨범 데모 개발
- 출시 3개월 만에 60개 이상의 기업 고객 확보

---

## 주요 내용

### 섹션 1: 회사 및 팀 소개
- Ben Zhou는 Memories.ai의 공동창업자 겸 CTO
- 공동창업자 Sean은 케임브리지에서 박사, 브리스톨 대학교 교수 출신
- Ben은 이전에 Meta에서 AI 제품 및 Llama 모델 개발 담당
- 약 3년 전 시작하여 현재 15명 규모의 팀으로 성장

### 섹션 2: 시각적 메모리의 중요성
- 인간이 "어제 뭘 먹었나?"라는 질문에 답할 때 텍스트뿐 아니라 이미지나 비디오 스냅샷을 떠올림
- 인간 두뇌는 텍스트로 요약하는 것뿐만 아니라 이미지와 비디오를 메모리에 저장
- AI도 효과적으로 문제를 해결하려면 시각적 메모리가 필요

### 섹션 3: 기술 아키텍처
- **압축 레이어**: 비디오에서 중요한 정보 추출 및 압축 (H.264와 유사한 개념)
- **인덱싱**: 임베딩을 통해 정보를 단일 데이터 공간에 인덱싱
- **검색 및 생성**: 질문이 있을 때 관련 정보를 검색하고 답변 생성
- **집계(Aggregation)**: 개별 임베딩을 병합하여 계층적 이벤트 형성, 경험과 통찰력 구축

### 섹션 4: AI가 시각 데이터를 필요로 하는 이유
- 현재 사람들은 텍스트뿐 아니라 비디오로도 콘텐츠 게시 (TikTok, Instagram 등)
- 전 세계적으로 TikTok에만 매일 8천만 개의 비디오 게시
- 효율적인 압축 및 인덱싱 시스템 없이는 AI가 이 정보를 효과적으로 처리 불가능

### 섹션 5: 온디바이스 처리
- 비디오 전송에 많은 대역폭과 네트워크 비용 발생
- 임베딩 모델을 Qualcomm 및 ARM 칩에 최적화하여 디바이스에 배포
- 압축 및 인덱싱이 모두 디바이스에서 발생
- 낮은 지연시간, 낮은 전력 소비, 프라이버시 보호
- 원본 비디오 대신 모델 데이터만 전송하면 됨

### 섹션 6: 삼성과의 협력 사례
- 삼성 Galaxy S25에 전체 시스템 구축
- 개인 AI 앨범에서 검색 및 채팅 가능한 데모 앱 개발
- Google 및 삼성의 갤러리는 클라우드 업로드 필요, Memories.ai는 모든 것을 로컬에서 처리
- 올해의 중요한 마일스톤

### 섹션 7: 주요 사용 사례

**1. 스마트 앨범**
- 모든 사람의 휴대폰에 이미지와 비디오 존재
- 단순한 키워드 검색(개, 차)이 아닌 맥락적 검색 가능 ("금요일 밤 친구들과 맥주 마시기")
- 삼성 및 Android 모바일 기업들과 협력

**2. 스마트 웨어러블**
- Humane Pin, Meta의 스마트 글래스, Rabbit 등 상시 착용 기기
- 항상 켜져 있는 카메라와 마이크로 많은 컨텍스트 수집
- 수신하는 모든 비디오와 오디오를 효율적으로 처리
- 메모리로 만들어 나중에 문제 해결, Q&A, 검색에 활용

**3. 감시 카메라**
- 가정용 보안 카메라에 초점
- 기존 문제: 오탐지가 많음 (사람이나 차량만 감지)
- 사용자는 누가 나타났는지 알고 싶어함 (가족, 친구, 직원, 낯선 사람)
- 얼굴 인식만으로는 불충분 (50% 이상 얼굴을 명확히 캡처 못함)
- 걸음걸이 패턴, 옷차림 등 시각적 메모리를 통한 인식
- Eufy, Wyze 등 카메라 회사와 협력

### 섹션 8: 비즈니스 성과
- 2024년 7월 정식 출시
- 매일 20명의 활성 사용자 (B2C)
- 3개월 내 60개 이상의 기업 고객 확보
- 주요 고객: 삼성 등 모바일 기업, Eufy/Wyse 등 카메라 기업, 멀티모달 AI 에이전트 기업
- 웹사이트에 500만 개 이상의 비디오 업로드됨
- 원본 비디오의 약 1% 크기로 데이터 생성 (1GB 비디오 → 10MB 처리 데이터)

### 섹션 9: 향후 계획
- 2년 전 사전학습 시작
- 내년까지 SDK와 모델을 Snapdragon A 시리즈 및 MediaTek 칩에 배포 예정

### 섹션 10: 기술적 질문 답변

**Q: 긴 비디오 처리 방법?**
- 1시간 비디오를 단일 임베딩으로 변환하는 것은 불가능
- 세그멘테이션 모델로 비디오를 이벤트, 액션, 카메라 변경 기준으로 분할
- 각 세그먼트마다 임베딩 생성
- 집계(aggregation)를 통해 전체 비디오 개요 생성 - 임베딩을 병합하여 새로운 임베딩 생성

**Q: 모델 변경 시 임베딩 재계산 문제?**
- 검색을 위해 다른 인코더와 다른 모달리티가 동일한 데이터 공간에 있도록 보장
- 디코더는 인코더와 함께 학습되어 호환성 유지

---

## 타임라인

- **00:00**: Um hello everyone uh we are members of aai and I'm Ben uh I'm co-ounder and CTO of memories AAI uh we'll talk I'll start with introducing our company and uh team member of our company and how we start resp our team members the founder is Sean uh he Bishi at Cambridge and then to University of Bristol as a professor and I was previously working at Maine working on two products. One is the ribbon meta the AI process. I was leading models and also I was part of written development and also our chef Alex is Ji on the screen as well. So how do we started this with me? So I met like three years ago uh when we were were working uh target algorithms and we think that um when I'm solving problems it's basically on the current context without having much logical like we think like when you're solving a real problem like me is very important. So like uh that's why we have this idea and we start to do app last year and turn or like company of around like 15 people. Um yeah so I quickly introduce like how we build like visual memory uh uh and and like what what what does vision memory mean in order for build? So like visual memory like mainly comes from like videos. So um like why why is important? uh for human have vision before but I have vision. So if I ask you a question um what did you eat yesterday like not only remember the names of the food or the name of the restaurant but you also vividly recall a few images or uh yesterday. So that means like inside human boo you not only summarize things into text and remember text but you also like save images uh video tape snippets into your memory and when you uh when I ask you something you recall those visual stuff so that's why important to have visual memory but videos are very heavy like takes a lot of bandwidth like...
- **05:00**: week like even on Tik Tok that's 80 million videos posted every day globally so if there's no efficient system to compress to induct information from those videos the AI and agent cannot efficiently pro those information and utilize information when solving problems when answering questions. So there so we are building this smart AI both infrastructure and the model to do that to help AI agents that uh to enable it to process large amount of information from both network all over the internet and also from personal media. Yeah. So uh in terms of like uh the as videos are heavy you don't want to like submit and transfer videos uh every day over the internet lot of bandwidth lot of network fee. So what we are doing is that for some of our embedding modes it's not enough which is too deploy. So we are specifically uh working on optimizing our model on certain attitudes because most of like current day smart wearables uh mobile phones uh which are like main input sensors for videos uh they are like supported by like Hong Kong chips or AR chips. So while optimizing our models on their MPUs and CPUs in order to be deployable on the device. So the pre prep-processing the compress the compression and indexing can all happen on device. Uh that's one thing that we're doing and that's uh we also launch like corporation last few weeks ago. Yeah. So the all all the goal is to make the inferencing uh with low latency low power efficient enough to run on local device. So you don't have to transfer the whole video the whole raw data into the cloud and waiting for response. uh everything is processed locally and you just need to transfer some of the uh like data from the model and it's it's more safe it's more uh it's it's like uh protects more about your privacy and uh it's uh requires less back. Yeah. Um yeah so one of our uh just uh...
- **10:00**: single family memory house per camera is that u one thing is that there's a lot of false alarms because it only use currently only use like same kind of architecture to detect what's inside the view of the camera. Like if a person appears it generates if there's a car moving it generate the events but it doesn't know like who the person is like whether the car is is the car from your house or like a car just on the street. So, so those are the important things that the users want to know about know from their their camera at home. Not just like single event detection or human detection. They want to detect if that human is if that person is one of their family or is their friends or is he just a working employee in the community. So those are but those have to be done through memory is because facial recognition does is not always useful on those cameras. You cannot always capture a very clear face on the camera. But like how human recognize if a person appears in the camera uh is a rat or it's not a rat. You not recognize not only from the face but also how he walk uh the pattern the the clothes he wears. So like the bone memorize that person. So that's uh how they do it from like facial memory. So we don't do like facial recognition like facial recognition helps but like more than 50% of the time you cannot capture their face. So we recognize like the human identification from the pattern of this person and the pattern comes from the past visual. Um yeah so we launched our uh uh members of AI uh in July uh July and since then like like we uh we we grew very fast and we it's mostly like on the enterprise side on on like customer side we have like 20 users live every day uh and um uh and on the customer side we sign over like 60 uh companies uh within like three months and most of them are like either uh mobile phone companies like Samsung or like uh camera companies also...
- **15:00**: >> Yes, please. >> I think if I understand correctly, when you have embeddings and you change the model with you, you have to recalate. >> Yeah. So are trying to keep them backward compatible or because otherwise you rec. >> Yeah. So for search uh definitely you have different encoder differentities and make sure they live in the same data space that's one thing you have to do and for like uh decoders like decoder they decode embeddings and generate attacks. So we coin this encoder with our model so that they are tra together. So uh that's why we can develop guidance into general....

---

## 전체 자막 (타임스탬프 포함)

**[00:03]** Um hello everyone uh we are members of

**[00:05]** aai and I'm Ben uh I'm co-ounder and CTO

**[00:08]** of memories AAI uh we'll talk I'll start

**[00:11]** with introducing our company and uh team

**[00:14]** member of our company and how we start

**[00:16]** resp

**[00:27]** our team members the founder is Sean uh

**[00:29]** he Bishi at Cambridge and then to

**[00:32]** University of Bristol as a professor and

**[00:34]** I was previously working at Maine

**[00:37]** working on two products. One is the

**[00:40]** ribbon meta the AI process. I was

**[00:43]** leading

**[00:44]** models and also I was part of

**[00:48]** written development and also our chef

**[00:51]** Alex is Ji

**[00:55]** on the screen as well. So how do we

**[00:58]** started this with me? So I met like

**[01:00]** three years ago uh when we were were

**[01:03]** working uh target

**[01:06]** algorithms and we think that um when I'm

**[01:09]** solving problems it's basically on the

**[01:11]** current context without having much

**[01:14]** logical like we think like when you're

**[01:17]** solving a real problem like me is very

**[01:19]** important. So like uh that's why we have

**[01:22]** this idea and we start to do app last

**[01:25]** year and turn or like company of around

**[01:28]** like 15 people. Um yeah so I quickly

**[01:33]** introduce like how we build like visual

**[01:35]** memory uh uh and and like what what what

**[01:39]** does vision memory mean in order for

**[01:42]** build? So like visual memory like mainly

**[01:45]** comes from like videos. So um like why

**[01:48]** why is important? uh for human have

**[01:50]** vision before but I have vision. So if I

**[01:53]** ask you a question um what did you eat

**[01:56]** yesterday like not only remember the

**[02:00]** names of the food or the name of the

**[02:02]** restaurant but you also vividly recall a

**[02:04]** few images or

**[02:08]** uh yesterday. So that means like inside

**[02:10]** human boo you not only summarize things

**[02:13]** into text and remember text but you also

**[02:15]** like save images uh video tape snippets

**[02:19]** into your memory and when you uh when I

**[02:22]** ask you something you recall those

**[02:24]** visual stuff so that's why important to

**[02:26]** have visual memory but videos are very

**[02:28]** heavy like takes a lot of bandwidth like

**[02:31]** even like 12 videos takes a long time

**[02:34]** especally as the dating uh the the

**[02:39]** public

**[02:40]** square. So we have a compression layer

**[02:43]** uh that radio uh inside what's important

**[02:47]** inside what's important in the time like

**[02:50]** uh to those connections and those are

**[02:53]** important

**[02:55]** similar to like H64

**[02:58]** like top indicators. So we uh detect the

**[03:03]** P and the areas along both facial and

**[03:07]** visual uh both facial and temporal

**[03:10]** information into

**[03:12]** representations. Uh first uh so we

**[03:14]** provide information and that's one

**[03:17]** layer. So we pre model to index

**[03:20]** differenties into a line single data

**[03:24]** space and then within those space uh

**[03:27]** information as vector to so that later

**[03:31]** on when you have a question like you

**[03:33]** want to search you can directly use but

**[03:36]** when do you want to ask a question for

**[03:38]** answer we have a pair to model to

**[03:42]** information from those detect generation

**[03:46]** and then the next aggregate here. So um

**[03:50]** if you remember things and not a single

**[03:52]** one like you don't have to remember like

**[03:54]** single information a single video

**[03:57]** remember another information you have to

**[03:59]** connect those information between

**[04:01]** individuals in order to form your data

**[04:04]** like experience insights some areations.

**[04:08]** So we have aggregation here that merge

**[04:11]** embeddings merge information from

**[04:13]** embeddings then form in

**[04:16]** different hierarchical events that's the

**[04:19]** memory that's aggregation and also if

**[04:21]** there's any metadata it's any structure

**[04:24]** data or also good

**[04:26]** but the most important thing how you

**[04:28]** emerging embeddings emerging information

**[04:29]** from embeddings yeah

**[04:32]** the most top of it that's where we have

**[04:34]** our API so you can search you can you

**[04:37]** can embeddings for text generation

**[04:42]** >> yeah and as um as like why AI or agent

**[04:47]** need visualize. So nowadays people not

**[04:50]** only post with uh blogs like not only

**[04:52]** post with text they also post with

**[04:54]** videos like uh Tik Tok Instagram

**[04:58]** there are like around V posted every

**[05:00]** week like even on Tik Tok that's 80

**[05:03]** million videos posted every day globally

**[05:06]** so if there's no efficient system to

**[05:08]** compress to induct information from

**[05:10]** those videos the AI and agent cannot

**[05:12]** efficiently pro those information and

**[05:15]** utilize information when solving

**[05:17]** problems when answering questions. So

**[05:19]** there so we are building this smart AI

**[05:22]** both infrastructure and the model to do

**[05:24]** that to help AI agents that uh to enable

**[05:28]** it to process large amount of

**[05:30]** information from both network all over

**[05:33]** the internet and also from personal

**[05:36]** media.

**[05:39]** Yeah. So uh in terms of like uh the as

**[05:44]** videos are heavy you don't want to like

**[05:46]** submit and transfer videos uh every day

**[05:49]** over the internet lot of bandwidth lot

**[05:51]** of network fee. So what we are doing is

**[05:54]** that for some of our embedding modes

**[05:56]** it's not enough which is too deploy. So

**[06:00]** we are specifically uh working on

**[06:02]** optimizing our model on certain

**[06:04]** attitudes because most of like current

**[06:06]** day smart wearables uh mobile phones uh

**[06:10]** which are like main input sensors for

**[06:12]** videos uh they are like supported by

**[06:15]** like Hong Kong chips or AR chips. So

**[06:18]** while optimizing our models on their

**[06:20]** MPUs and CPUs in order to be deployable

**[06:23]** on the device. So the pre

**[06:25]** prep-processing the compress the

**[06:26]** compression and indexing can all happen

**[06:29]** on device. Uh that's one thing that

**[06:31]** we're doing and that's uh we also launch

**[06:34]** like corporation last few weeks ago.

**[06:38]** Yeah. So the all all the goal is to make

**[06:41]** the inferencing uh with low latency low

**[06:44]** power efficient enough to run on local

**[06:46]** device. So you don't have to transfer

**[06:48]** the whole video the whole raw data into

**[06:50]** the cloud and waiting for response. uh

**[06:53]** everything is processed locally and you

**[06:55]** just need to transfer some of the uh

**[06:58]** like data from the model and it's it's

**[07:01]** more safe it's more uh it's it's like uh

**[07:05]** protects more about your privacy and uh

**[07:08]** it's uh requires less back. Yeah.

**[07:14]** Um yeah so one of our uh just uh

**[07:18]** showcase like that we will build a demo

**[07:20]** app on Samsung uh that's uh we do this

**[07:23]** year with Samsung and uh they invited

**[07:26]** like six companies to review every year

**[07:28]** with them. So that we we built our like

**[07:32]** whole system onto Samsung's snap driven

**[07:34]** Samsung S25 also and it's app where you

**[07:38]** can search and chat with your own

**[07:40]** personal AI album and like we compared

**[07:43]** to Google and Samsung like Google and

**[07:46]** Samsung their own gallery requires you

**[07:48]** to upload your images to their cloud and

**[07:50]** deal with it and then all the

**[07:51]** information from the cloud but we can do

**[07:54]** can do everything locally. So that's uh

**[07:57]** that's one of the use uh milestone that

**[07:59]** we did this year.

**[08:02]** Yeah. So uh about use cases. So the

**[08:06]** first one is our qu model album. So

**[08:09]** that's that's also like what we're

**[08:11]** targeting with Samsung to to to achieve

**[08:13]** this year. And uh everyone have images

**[08:16]** and videos on your phone. You want to

**[08:18]** make your album more more like uh

**[08:21]** intelligence. You want to search for an

**[08:22]** album. We just we don't want just want

**[08:24]** to search for like certain keywords or

**[08:27]** tags uh like like I want to search a dog

**[08:30]** search for car instead you want to

**[08:31]** search uh for like um having beer with

**[08:35]** my friends on Friday night those kind of

**[08:37]** things are like like important for me

**[08:40]** you know your personal memory those are

**[08:42]** important things but sim is not done on

**[08:45]** like mobile device so we do that with

**[08:48]** Samsung and most mobile like Android

**[08:50]** mobile companies uh to achieve that

**[08:53]** that's the first use case.

**[08:54]** >> Yeah.

**[08:55]** >> And second one is smart robos like uh

**[08:58]** like ribbon meta like rocket like rabbit

**[09:01]** those are like always on or like all day

**[09:02]** wear smart they keep uh includes like

**[09:06]** lots of contacts every day. So some of

**[09:08]** them has camera always on some of them

**[09:09]** has always on. So um you definitely they

**[09:13]** definitely want an efficient way to uh

**[09:16]** absorb or in intake those contexts uh

**[09:18]** when they receive uh when they receive

**[09:20]** it and that's also like another thing

**[09:23]** that we help them to enable that uh

**[09:25]** every every seconds of video every

**[09:27]** second of audio we receive on the device

**[09:30]** could be processed could be efficiently

**[09:32]** processed you know in order to make them

**[09:34]** into memory and then provide context for

**[09:36]** later uh like problem solving uh QA or

**[09:39]** search yeah so that's for small levels

**[09:44]** and also like for surveillance cameras.

**[09:46]** So this is not like like like security

**[09:48]** camera for like factories or like for uh

**[09:52]** commercial use case. This is also

**[09:53]** security camera for like uh single

**[09:55]** family houses like for home use cases.

**[09:57]** So uh one problem that we find that in

**[10:01]** single family memory house per camera is

**[10:02]** that u one thing is that there's a lot

**[10:05]** of false alarms because it only use

**[10:07]** currently only use like same kind of

**[10:09]** architecture to detect what's inside the

**[10:12]** view of the camera. Like if a person

**[10:14]** appears it generates if there's a car

**[10:17]** moving it generate the events but it

**[10:19]** doesn't know like who the person is like

**[10:21]** whether the car is is the car from your

**[10:23]** house or like a car just on the street.

**[10:26]** So, so those are the important things

**[10:28]** that the users want to know about know

**[10:30]** from their their camera at home. Not

**[10:32]** just like single event detection or

**[10:35]** human detection. They want to detect if

**[10:37]** that human is if that person is one of

**[10:40]** their family or is their friends or is

**[10:43]** he just a working employee in the

**[10:44]** community. So those are but those have

**[10:47]** to be done through memory is because

**[10:49]** facial recognition does is not always

**[10:51]** useful on those cameras. You cannot

**[10:53]** always capture a very clear face on the

**[10:55]** camera. But like how human recognize if

**[10:58]** a person appears in the camera uh is a

**[11:00]** rat or it's not a rat. You not recognize

**[11:03]** not only from the face but also how he

**[11:05]** walk uh the pattern the the clothes he

**[11:08]** wears. So like the bone memorize

**[11:11]** that person. So that's uh how they do it

**[11:15]** from like facial memory. So we don't do

**[11:16]** like facial recognition like facial

**[11:18]** recognition helps but like more than 50%

**[11:21]** of the time you cannot capture their

**[11:23]** face. So we recognize like the human

**[11:26]** identification from the pattern of this

**[11:29]** person and the pattern comes from the

**[11:30]** past visual.

**[11:37]** Um yeah so we launched our uh uh members

**[11:40]** of AI uh in July uh July and since then

**[11:45]** like like we uh we we grew very fast and

**[11:48]** we it's mostly like on the enterprise

**[11:50]** side on on like customer side we have

**[11:53]** like 20 users live every day uh and um

**[11:57]** uh and on the customer side we sign over

**[11:59]** like 60 uh companies uh within like

**[12:02]** three months and most of them are like

**[12:05]** either uh mobile phone companies like

**[12:07]** Samsung or like uh camera companies also

**[12:12]** use wise those very popular ones and

**[12:15]** also uh the others like multi- model

**[12:18]** agent companies uh their agent has to

**[12:21]** intake uh information from different

**[12:23]** modalities and the one is on the video

**[12:26]** so we're enable us enabling them with

**[12:29]** our API to deal with video information

**[12:33]** I think uh yeah basically Uh that's all.

**[12:37]** Um yeah and also we launched

**[12:39]** preparations for uh two years ago and uh

**[12:42]** I think uh by next year we'll deploy our

**[12:44]** SDK and our model onto the uh new chip

**[12:47]** snap driven a series and also the MX

**[12:50]** series for smart.

**[12:54]** Thank you.

**[12:58]** Uh yeah,

**[13:01]** >> technical questions about your video arh

**[13:08]** size videos

**[13:10]** what is the size of a typical video

**[13:16]** and how

**[13:19]** >> okay so in terms of like all we do is

**[13:21]** long videos uh definitely we like we

**[13:23]** don't turn like a one hour video into a

**[13:26]** singly ing that's not impossible like a

**[13:28]** single embedding with a dimension of

**[13:30]** like 40 cannot capture enough

**[13:32]** information for a long video. But often

**[13:35]** uh you don't have to uh like you don't

**[13:38]** have like uh like by capturing

**[13:40]** information from a lot like a one hour

**[13:42]** long video we have a segmentation model

**[13:45]** that segment not only like from the

**[13:48]** pixel level but also from a tempo level.

**[13:50]** So it's either event detection action

**[13:52]** detection or like camera change. So

**[13:55]** that's are important things where you

**[13:56]** can set them a long video into different

**[13:58]** SW segments and you generate embeddings

**[14:01]** for each one of them but also like like

**[14:03]** how how do you have an overview of the

**[14:05]** whole video that's by aggregation so you

**[14:08]** merge so merge embeddings you merge

**[14:10]** information from embedded into new

**[14:13]** embeddings and that's works also like

**[14:15]** for a list of small videos and you can

**[14:18]** also aggregate them. So it's uh it's a

**[14:20]** general way to deal with both long

**[14:22]** videos and large amounts of videos. And

**[14:25]** in terms of like the the site we

**[14:27]** generated for each uh video on our

**[14:30]** website uh this right now I think we

**[14:32]** have over like five million videos on

**[14:35]** our like people upload like more than

**[14:37]** that uh to our website. So on average we

**[14:40]** generate around like 1%

**[14:43]** uh like internal site of data like 1% of

**[14:46]** the original data. So for example, if

**[14:48]** you upload a 1 GB of video to our

**[14:51]** website, then the the the the process

**[14:55]** process data embeddings metadata

**[14:57]** generated from this video will cost you

**[14:59]** like $10. Yeah.

**[15:02]** >> Yes, please.

**[15:03]** >> I think if I understand correctly, when

**[15:05]** you have embeddings and you change the

**[15:07]** model with you, you have to recalate.

**[15:10]** >> Yeah. So are trying to keep them

**[15:12]** backward compatible or because otherwise

**[15:15]** you rec.

**[15:17]** >> Yeah. So for search uh definitely you

**[15:20]** have different encoder differentities

**[15:22]** and make sure they live in the same data

**[15:24]** space that's one thing you have to do

**[15:26]** and for like uh decoders like decoder

**[15:28]** they decode embeddings and generate

**[15:30]** attacks. So we coin this encoder with

**[15:33]** our model so that they are tra together.

**[15:36]** So uh that's why we can develop guidance

**[15:38]** into general.


---

*이 문서는 YouTube 자막을 기반으로 자동 생성되었습니다.*
*생성 도구: YouTube-to-MD Skill*
