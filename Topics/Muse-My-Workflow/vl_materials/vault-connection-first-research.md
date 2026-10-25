---
title: "볼트 연결 해법 첫 조사 (2026-10-25)"
author:
  - "박창수"
  - "Claude Code"
created: 2026-10-25 01:11:00
tags:
  - muse-my-workflow
  - research
---

# 볼트 연결 해법 첫 조사 — 2026-10-25

> 「볼트를 Muse 의 컴퓨터와 자동 · 수동으로 동기화하거나 private GitHub 로 함께 보게 할 수 있는가」(2026-10-25 박창수 질문)에 대한 첫 조사다. [M4 볼트 연결 해법](../vl_roadmap/20261018_RoadMap_Muse-My-Workflow.md)의 출발점이다. 여기 적은 것은 조사 시점의 **공식 자료 · 2차 보도 · 직접 다뤄 본 결과**이며 시험으로 확인한 것이 아니다. M1 보강과 M4 에서 다시 확인한다.

## 1. 한 줄 요약

Muse 의 컴퓨터와 폴더를 직접 맞추는 기능은 공식 자료에 없다. 대신 Muse 가 연결할 수 있는 클라우드 저장소(Dropbox · GitHub 등)에 볼트를 두면 Muse 가 그것을 들여다볼 수 있다. 볼트 전체가 아니라 **골라 담은 사본**이 현실적이다 — 크기와 내부 자료 때문이다.

## 2. Muse 의 컴퓨터 (Secure VM)

| 확인한 것 | 출처 종류 |
|---|---|
| Muse 는 자기 브라우저가 있는 전용 클라우드 컴퓨터에서 일한다. 에이전트와 사용자 데이터가 함께 있고, 연결한 서비스의 데이터와 로그인 정보도 여기에 저장된다 | 공식 — [발표문](https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/) |
| 별도의 Sentinel 에이전트가 승인해야 인터넷으로 나간다 | 공식 — 발표문 |
| 사용자만 키를 가진 Confidential VM 은 「올해 안」 예정이다 | 공식 — 발표문 |
| 사용자가 그 컴퓨터에 직접 들어가 폴더를 맞추는 방법은 공식 자료에 없다. 파일은 올리기나 커넥터로 들어간다 | 공식 자료에 없음 |
| 올리거나 만든 파일은 Library 의 System Files 에 쌓이고 하나씩 지울 수 있다. Settings → Data controls → 「Download your Muse data」로 채팅 · 파일 · 에이전트 정보를 내려받는다 (형식은 안 나옴) | 공식 — [데이터 관리 도움말](https://www.meta.com/help/superintelligence/2225571704857152/) |
| 터미널 · 코드 실행이 된다는 이야기는 2차 자료에만 있다 | 2차 — 공식 확인 못 함 |

## 3. 커넥터

| 커넥터 | 상태 | 출처 종류 | 메모 |
|---|---|---|---|
| Gmail · 캘린더 · Facebook · Instagram · Threads · Apple Health · Android SMS | 있음 | 공식 — [커넥터 도움말](https://www.meta.com/help/artificial-intelligence/1687253048996149/) | 일할 때 필요한 만큼만 가져온다 — 「받은편지함 전체를 내려받지 않는다(시키지 않는 한)」 |
| Notion · Granola · GitHub · Box | 2026-09-23 발표 | 공식 — [Meta Connect 2026](https://www.meta.com/blog/meta-connect-2026-everything-we-announced/) | GitHub 커넥터의 권한 범위(레포 하나인지, 계정 전체 · 쓰기까지인지)는 공개 자료 없음 |
| Dropbox | 있음 — 미국 · 캐나다, 모든 Dropbox 플랜(무료 포함) | 공식 — [Dropbox 도움말](https://help.dropbox.com/integrations/connect-to-meta-muse) (2026-10-02 갱신) | 찾기 · 읽기 · 만들기 · 옮기기 · 지우기 · 공유 링크. 「이 연결로 공유된 데이터를 Meta 가 모델 학습에 쓸 수 있다」 |
| Google Drive | 확인 못 함 | 2차 — 비공식 커넥터 목록에만 나옴 | 앱의 Settings → Connectors 에서 확인 |
| OneDrive · iCloud (파일) | 기본 커넥터 없음 | 2차 · 외부 업체 자료 | 외부 업체 MCP 를 거치는 우회만 있다 |
| 사용자 정의 커넥터 | Muse 가 만들 수 있다. 로그인 정보는 Secure Credentials Store 에 두고, Meta 가 검토하지 않는다 | 공식 — 커넥터 도움말 | 집 PC 에 직접 붙이려면 PC 를 인터넷에 열어야 한다 — 시험하지 않는다 |

- 연결을 끊어도 이미 쓴 정보는 Muse 의 기억과 대화 기록에 남을 수 있다 (공식 — 커넥터 도움말).
- 연결마다 「쓰기 전에 묻기」 · 「모든 작업 전에 묻기」를 정할 수 있다 (공식 — [안내와 승인 도움말](https://www.meta.com/help/artificial-intelligence/1385290430137537/)).

## 4. 데스크톱 앱 — 내 PC 에 직접

- **Mac**: 「Computer use is now available with Muse for Mac」 — 허락하면 Mac 의 모든 앱을 다룰 수 있다 (공식 — Meta Connect 2026, 2026-09-23).
- **Windows**: Microsoft 가 2026-10-07 「Muse for Windows 곧 출시 — MXC 연동」을 발표했다. 날짜는 없다. MXC(Microsoft Execution Containers)는 에이전트가 닿을 파일 · 네트워크를 정책으로 정하는 실행 계층이다 (공식 — [Windows Experience Blog](https://blogs.windows.com/windowsexperience/2026/10/07/building-windows-for-hybrid-intelligence/)).
- 지금 Windows 에서는 웹만 쓸 수 있고, 웹 Muse 는 PC 의 파일에 닿지 않는다.

## 5. 개인정보 · 학습

- **학습 사용 끄기**: Settings → Data controls. 끄면 「상호작용」이 학습에 쓰이지 않고, 작업에 쓴 정보는 상호작용에 포함된다고 적혀 있다. 커넥터 데이터까지 막는다는 명시는 없다 (공식 — 데이터 관리 도움말). Dropbox 도움말은 연결 데이터가 학습에 쓰일 수 있다고 적는다.
- **지워도 남을 수 있다**: 지운 내용에서 배운 정보를 Muse 가 기억할 수 있다 (공식 — 데이터 관리 도움말).
- **다른 사람 정보**: TIME 보도(2026-10-06)에 따르면 Muse 는 사용자와 사용자가 아는 사람 — Muse 를 쓰지 않는 사람 포함 — 에 대한 기록을 매시간 갱신한다. Meta 는 광고 시스템과 공유하지 않는다고 했고, Meta 도 읽지 못하는 암호화는 아직 없다 (보도 — [Malwarebytes 요약, 2026-10-08](https://www.malwarebytes.com/blog/privacy/2026/10/metas-muse-ai-files-away-your-friendships-arguments-and-secrets)).

## 6. 직접 다뤄 본 결과 (박창수, 2026-10-20 ~ 10-22, 안드로이드)

- **음성 입력** — 대부분 음성으로 지시해도 잘 됐다
- **Gmail · Google Calendar 연결** — 메일 확인 · 광고 메일 지우기 · 보내기, 일정 추가, 반복 알림까지 됐다
- **설치 · 가입 · 메일 연결** — 안드로이드 휴대폰에서 문제없이 됐다

## 7. 볼트 쪽 사실 (2026-10-25)

- md 파일은 약 4,800개 · 약 95MB 이고, 그 절반은 YouTube 자막 모음이다. 볼트 전체는 약 54GB 로 대부분 영상 · 오디오다 → md 만 고른 사본은 무료 저장소로도 충분하다.
- 내부 표시 문서가 100개가 넘는다 → 사본에서 반드시 빼야 한다.
- 볼트 루트는 git 레포가 아니고, 루트 `.gitignore` 는 내용 폴더를 통째로 빼게 돼 있다. 볼트 안에 공개 레포(CatchUpAI_VL)가 따로 있다 → 볼트를 그대로 레포로 만들기보다 **사본 폴더를 따로** 두는 쪽이 안전하다.
- PC 에는 Dropbox · Google Drive 앱이 없다. 회사 계정 클라우드는 쓰지 않는다.

## 8. 첫 가설 — M4 에서 시험한다

**골라 담은 사본 + Muse 전용 받는 곳**

1. 원본 볼트는 그대로 둔다
2. 스크립트가 공개 · 개인 등급 md 만 사본 폴더(Dropbox 또는 private GitHub)로 한 방향 복사한다 — 내부 · 비밀 · 의뢰인 · 연락처 · 개인 문서 · 영상은 뺀다
3. Muse 는 사본을 읽기만 하고, 결과는 받는 곳에만 쓴다 — 사본은 다음 복사 때 덮어써진다
4. 받는 곳이 집 PC 로 내려오면 Claude Code 가 볼트 규칙에 맞춰 정리한다

볼트 규칙이 필요한 일은 Claude Code(집 PC 원격 콘솔 또는 클라우드 세션)로 한다 — 한 도구로 다 하지 않는다.

## 9. M1 보강 · M4 에서 확인할 것

- [ ] 앱의 실제 커넥터 목록 (Dropbox · GitHub · Box · Google Drive)
- [ ] GitHub · Dropbox 커넥터를 레포 하나 · 폴더 하나로 좁힐 수 있는가
- [ ] 학습 사용 끄기가 커넥터 데이터까지 막는가
- [ ] 음성 메모가 원문 그대로 파일로 남는가 (M2)
- [ ] Windows 앱 출시 여부와, MXC 로 허용한 폴더만 보게 할 수 있는가

## 출처 (확인 2026-10-25)

- [Meta — Introducing Muse](https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/)
- [Meta Help — How Muse works with Connectors](https://www.meta.com/help/artificial-intelligence/1687253048996149/)
- [Meta Help — How Muse works with your guidance and approval](https://www.meta.com/help/artificial-intelligence/1385290430137537/)
- [Meta Help — How to manage your Muse data](https://www.meta.com/help/superintelligence/2225571704857152/)
- [Meta Help — How to get started with Muse](https://www.meta.com/help/superintelligence/1331373868832401/)
- [Meta — Everything We Announced at Meta Connect 2026](https://www.meta.com/blog/meta-connect-2026-everything-we-announced/)
- [Dropbox Help — Connect Dropbox to Meta Muse](https://help.dropbox.com/integrations/connect-to-meta-muse) · [Dropbox — Meta Muse integration](https://www.dropbox.com/en_GB/app-integrations/meta-muse)
- [Windows Experience Blog — Building Windows for hybrid intelligence (2026-10-07)](https://blogs.windows.com/windowsexperience/2026/10/07/building-windows-for-hybrid-intelligence/)
- [Malwarebytes — TIME 조사 요약 (2026-10-08)](https://www.malwarebytes.com/blog/privacy/2026/10/metas-muse-ai-files-away-your-friendships-arguments-and-secrets)
- 2차: [TechAIWire — GitHub 커넥터](https://techaiwire.com/articles/meta-muse-computer-control-github-connector/) · [Carly — OneDrive 우회](https://www.usecarly.com/blog/how-to-connect-multiple-onedrive-accounts-to-meta-muse/) · [postfa.st — 비공식 커넥터 목록](https://postfa.st/blog/meta-muse-connectors-list)
