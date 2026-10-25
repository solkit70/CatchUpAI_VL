# Muse 기능 확인 — v2 (2026-10-25)

> 이 Topic 에 필요한 기능이 Muse 에 있는지 확인한 표다. v1(2026-10-18)은 Meta 공식 자료만 봤고, v2(2026-10-25 · Roadmap v2.0 보강)는 그 뒤 직접 다뤄 본 결과와 새로 나온 공식 자료를 더했다. 행마다 **출처 종류**를 적는다 — **공식**(Meta · 파트너 공식 자료) · **직접**(박창수가 직접 다뤄 본 결과) · **2차**(보도 · 비공식 자료) · **미확인**(근거 없음). 화면 메뉴 이름은 도움말 표기를 따랐으며, 앱이 바뀌면 다를 수 있다.

## 기능 표

| 기능 | 상태 | 출처 종류 · 확인일 | 내용 | 이 Topic 에서 | 출처 |
|---|---|---|---|---|---|
| **파일(Artifact) 만들기** | ✅ | 공식 · 10/25 재확인 | 문서(PDF · DOCX · 텍스트 · **Markdown**), 표(XLSX · CSV), 이미지, 코드, 웹 파일을 읽고 만들고 고친다. 만든 파일은 Library 에 저장된다 | **Markdown 파일로 만들게 하면** 볼트에 넣기 쉽다 → M2 첫 시험 | [Artifacts 도움말](https://www.meta.com/help/artificial-intelligence/2074655449783957/) |
| **Library · System Files** | ✅ | 공식 · 10/25 | 올리거나 만든 파일은 Library 의 System Files 에 쌓이고 하나씩 지울 수 있다 | 밖에서 만든 것이 쌓이는 곳. 원본은 늘 볼트 | [데이터 관리 도움말](https://www.meta.com/help/superintelligence/2225571704857152/) |
| **파일 하나씩 내려받기** | ❓ | 미확인 · 10/25 재확인 | Artifacts · 데이터 관리 도움말 모두 개별 다운로드 방법이 없다 | **M2 에서 가장 먼저 해 볼 것** (웹 · 휴대폰) | — |
| **내 데이터 전체 내려받기** | ✅ | 공식 · 10/25 재확인 · **직접 · 10/25** | Settings → Data controls → 도움말 이름은 Download your Muse data, **앱 화면 이름은 「Download your agent data」**. 채팅 · 파일 · 기타 에이전트 정보. 직접 받아 보니 **zip 하나(약 4MB · 파일 103개)** — 대화 전체를 담은 txt 1개, `workspace/` 폴더(Muse 가 만든 Markdown 86개가 목표 · 폴더 구조 그대로, 올린 PDF · CSV · 이미지), `manifest.json`. 요청한 당일에 받았다 | 백업 · 한꺼번에 가져오기용. **전체를 받는 것이라 매일 쓰는 방법은 아니다** — M2 에서 하나씩 받는 방법과 비교 | [데이터 관리 도움말](https://www.meta.com/help/superintelligence/2225571704857152/) · 직접 사용 |
| **외부 공유** | ✅ | 공식 · 10/25 재확인 | 사용자가 공유를 켜거나 Muse 의 요청을 승인할 때만 밖으로 공유한다 | 공유 링크는 「옮긴 것」이 아니다 — 비교용 | [Artifacts 도움말](https://www.meta.com/help/artificial-intelligence/2074655449783957/) |
| **파일 올리기** | ✅ | 공식 · 10/25 | 파일을 올리거나 만들게 할 수 있다 | 집 → 밖 넘기기(M2) — 공개 · 개인 등급만 | [시작하기 도움말](https://www.meta.com/help/superintelligence/1331373868832401/) |
| **기억** | ✅ | 공식 · 10/25 | 중요한 것을 기억하고, 잊으라고 하면 「할 수 있는 만큼」 잊는다. 지운 내용에서 배운 정보를 기억할 수 있다 | 규칙을 기억시키는 시험(M3). 내부 자료는 처음부터 말하지 않는다 | [발표문](https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/) · [데이터 관리 도움말](https://www.meta.com/help/superintelligence/2225571704857152/) |
| **기억 가져오기 (Import memory)** | ✅ | **직접(앱 화면) · 10/25** | Settings → Data controls 에 「Import memory」 항목이 있다. 도움말에는 없던 기능이다. 무엇을 어떻게 가져오는지는 열어 보지 않음 | M3 에서 열어 본다 (규칙 요약을 넣는 방법 후보) | 직접 확인 |
| **Reset Muse (전체 삭제)** | ✅ | **직접(앱 화면) · 10/25** | Settings → Data controls → 「Reset Muse」. 채팅 기록 · 파일 · 진행 중 작업을 영구 삭제한다고 적혀 있다 | 되돌리는 마지막 수단. 누르지 않았다. 부분 삭제는 System Files · 「잊어줘」 | 직접 확인 |
| **앱을 닫아도 계속 일함** | ✅ | 공식 · 10/18 | 긴 작업은 앱을 닫은 뒤에도 계속하고, 바뀐 점이나 승인이 필요할 때 돌아온다 | 차에서 맡기고 내려서 결과 받기 · 긴 공개 리서치(#23) | [발표문](https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/) |
| **웹 접근** | ✅ | 공식 · 10/18 | 자기 브라우저로 웹을 열고 양식을 채운다. 인터넷으로 나가는 것은 Sentinel 이 승인한다 | 공개 행사 리서치(#11 · #22) · 공개 레포 읽기(M3) | [발표문](https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/) |
| **음성 입력** | ✅ | **직접 · 2026-10-22** (안드로이드) | 대부분 음성으로 지시해도 잘 됐다 | 차 안 음성 지시가 된다. 남은 확인은 **말한 그대로 파일로 남는가** (M2 실습 2) | 직접 사용 |
| **Gmail · Google Calendar** | ✅ | **직접 · 2026-10-20~22** (안드로이드) · 공식 | 연결 뒤 메일 확인 · 광고 메일 지우기 · 보내기, 일정 추가가 됐다. 도움말: 일할 때 필요한 만큼만 가져온다 | 메일 · 일정 일(#19 · #20) · 메일로 옮기기 · 넘기기(M2) — **연결 규칙에 따라** | 직접 사용 · [커넥터 도움말](https://www.meta.com/help/artificial-intelligence/1687253048996149/) |
| **반복 알림** | ✅ | **직접 · 2026-10-22** | 매주 반복 알림을 설정했다 | 일정 · 알림(#20) | 직접 사용 |
| **커넥터 (전체)** | ✅ | 공식 · 10/25 · **직접(앱 화면) · 10/25** | 도움말: Gmail · 캘린더 · Facebook · Instagram · Threads · Apple Health · Android SMS. 2026-09-23 발표: Notion · Granola · GitHub · Box 와 쇼핑 · 결제. **앱 Available 목록(화면에서 본 것)**: Google Drive · Messenger · Withings(추천), Gmail · Google Calendar · Finances(Plaid) · Google Sheets · Google Docs, Instagram · Facebook · Threads · Instagram Messages, Peloton · Function Health · HealthEx, Meta Business Manager · GitHub · Canva · Dropbox · Zoom. 연결 목록과는 별개로 **Browser** 항목이 있다. 연결을 끊어도 이미 쓴 정보는 기억에 남을 수 있다. Box · Notion · Granola · OneDrive · iCloud 는 본 화면에 안 보였다(「See all」은 펼치지 않아 전체 목록은 미확인) | M4 저장소 후보 3개가 앱에 모두 있다: **Google Drive · GitHub · Dropbox**. 연결 버튼은 누르지 않았다 | [커넥터 도움말](https://www.meta.com/help/artificial-intelligence/1687253048996149/) · [Meta Connect 2026](https://www.meta.com/blog/meta-connect-2026-everything-we-announced/) · 직접 확인 |
| **Dropbox** | ✅ | 공식(Dropbox) · 10/25 · **앱 목록 직접 · 10/25** | 미국 · 캐나다, 모든 Dropbox 플랜(무료 포함). 찾기 · 읽기 · 만들기 · 옮기기 · 지우기 · 공유 링크. 「연결로 공유된 데이터를 Meta 가 모델 학습에 쓸 수 있다」. 앱 Available 목록에 있음 | M4 해법 A 후보 | [Dropbox 도움말](https://help.dropbox.com/integrations/connect-to-meta-muse) |
| **GitHub** | 🔶 | 공식(발표) · 10/25 · **앱 목록 직접 · 10/25** | 2026-09-23 새 커넥터로 발표. 앱 Available 목록(Business 묶음)에 있음. 권한 범위(레포 하나 · 계정 전체 · 쓰기)는 공개 자료 없음 — 연결 화면에서만 확인 가능 | M4 해법 B 후보. M3 의 공개 레포 읽기는 웹으로 | [Meta Connect 2026](https://www.meta.com/blog/meta-connect-2026-everything-we-announced/) |
| **Google Drive** | ✅ | **직접(앱 화면) · 10/25** | 앱 Available 목록의 추천 맨 앞에 있다(「Search and manage your files and documents」). Google Sheets · Google Docs 커넥터도 따로 있다 | M4 해법 C 후보 — 이미 쓰는 Google 계정이라 저장소 후보 중 가장 가깝다. 폴더 하나로 좁힐 수 있는지는 M4 실습 3 | 직접 확인 |
| **OneDrive · iCloud (파일)** | ❌ | 2차 · 10/25 | 기본 커넥터 없음 — 외부 업체 MCP 를 거치는 우회만 있다 | 쓰지 않는다 | [첫 조사 §3](../../vl_materials/vault-connection-first-research.md) |
| **사용자 정의 커넥터** | ✅ | 공식 · 10/25 | Muse 가 만들 수 있다. 로그인 정보는 Secure Credentials Store 에 두고, Meta 가 검토하지 않는다 | M4 해법 H — 집 PC 를 인터넷에 여는 위험이 있어 시험하지 않는다 | [커넥터 도움말](https://www.meta.com/help/artificial-intelligence/1687253048996149/) |
| **연결 권한** | ✅ | 공식 · 10/25 · 직접 · 10/22 | Settings → Permissions → Connectors: 「Ask for some actions」(기본 — 모든 쓰기와 중요한 읽기 전에 묻기) · 「Always ask」(모든 작업 전에 묻기). 물을 때 Allow once · Allow for this task · Always allow · Deny 중 고른다 | [연결 규칙](../guides/do-not-upload.md)의 공통 설정 | [안내와 승인 도움말](https://www.meta.com/help/artificial-intelligence/1385290430137537/) |
| **커넥터별 권한 세부 설정** | ✅ | **직접(앱 화면) · 10/25** | Settings → Connectors → 커넥터 → 항목별로 Allow / Ask 를 고른다. Gmail 은 읽기(초안 · 라벨 · 메일 읽기 · 검색)와 쓰기 · 삭제(초안 쓰기 · 라벨 · 읽음 표시 · 가져오기 · **보내기** · **휴지통 이동** · **구독 해지**), 백그라운드 동기화로 나뉜다. 「Disconnect」 단추와 「Reset to defaults」(이 화면의 권한을 기본값으로) 가 있다. 한 커넥터에 계정을 여러 개 붙일 수 있다 | 연결 규칙의 「범위 좁히기」 — **폴더 · 레포 하나로 좁히는 것이 아니라 동작별로 Allow / Ask 를 고르는 방식**. 저장소 커넥터도 같은 화면인지는 M4 실습 3 | 직접 확인 |
| **학습 사용 끄기** | ⚠️ | 공식(도움말은 있다고 함) · **직접 · 10/25: 웹 화면에는 없음** · 휴대폰 앱 미확인 | 도움말은 Settings → Data controls 에서 끌 수 있다고 안내한다. 2026-10-25 웹 Muse 의 Data controls 에는 **Import memory · Download your agent data · Reset Muse 세 항목뿐**이었다. 휴대폰 앱 · 다른 메뉴(General · Learn more 링크의 개인정보 페이지)에 있는지는 확인하지 않았다. 10/18 · 10/22 기록에는 이 스위치를 직접 확인한 내용이 없다 | 확인될 때까지는 **끌 수 없다고 가정**하고 「올리지 않는 것」을 방어선으로 쓴다. 휴대폰 앱 Data controls 를 먼저 본다 → M3 · M4 실습 1 | [데이터 관리 도움말](https://www.meta.com/help/superintelligence/2225571704857152/) · 직접 확인 |
| **플랫폼** | ✅ | 공식 · 10/25 | 미국 iOS · Android, 웹, WhatsApp, Mac 데스크톱 앱. Windows 앱은 Microsoft 가 2026-10-07 발표(출시 전). AI 안경은 예정 | 밖은 휴대폰 앱, 집은 웹 | [발표문](https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/) · [Meta Connect 2026](https://www.meta.com/blog/meta-connect-2026-everything-we-announced/) · [Windows 블로그](https://blogs.windows.com/windowsexperience/2026/10/07/building-windows-for-hybrid-intelligence/) |
| **내 PC 직접 다루기** | 🔶 | 공식 · 10/25 | Mac 앱은 허락하면 Mac 의 모든 앱을 다룬다. Windows 는 앱이 나오기 전이라 웹만 — 웹 Muse 는 PC 파일에 닿지 않는다 | M4 해법 G — Windows 앱이 나오면 시험 | [Meta Connect 2026](https://www.meta.com/blog/meta-connect-2026-everything-we-announced/) |
| **무료 한도** | ✅ | 공식 · 10/18 | 무료는 사용량 한도가 있고, 다 쓰면 기다리거나 유료로. Power $20/월(주 500M 토큰) · Maximum $100/월(주 3B 토큰). 지역 · 계정마다 다를 수 있음 | 이 Topic 은 무료로 한다. M5 1주일 사용에서 한도에 걸리는지 기록 | [구독 도움말](https://www.meta.com/help/subscriptions/1021145227643680/) |
| **보안 · 개인정보** | ✅ | 공식 · 10/18 · 2차 · 10/25 | Secure VM(전용 클라우드 컴퓨터) · Sentinel · 학습 사용 거부 · 광고 시스템과 공유 안 함. 사용자만 키를 가진 Confidential VM 은 연내 예정. 보도(TIME, 2026-10-06): 사용자와 사용자가 아는 사람에 대한 기록을 매시간 갱신한다 | 그래도 클라우드다 — [do-not-upload.md](../guides/do-not-upload.md)의 규칙 · 이름 규칙 | [발표문](https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/) · [Malwarebytes 요약](https://www.malwarebytes.com/blog/privacy/2026/10/metas-muse-ai-files-away-your-friendships-arguments-and-secrets) |

## 다음 모듈로 넘기는 미확인 목록 (v2)

| # | 확인할 것 | 어디서 |
|---|---|---|
| 1 | 파일 하나씩 내려받기 — 웹 · 휴대폰에서 Markdown 이 그대로 받아지는지 | M2 실습 1 |
| 2 | 음성 메모가 말한 그대로 파일로 남는지 | M2 실습 2 |
| 3 | ~~전체 데이터 내려받기의 형식~~ → **풀림 (10/25 직접)**: zip 하나, 대화 txt + workspace 폴더(Markdown · 올린 파일) + manifest.json | 완료 |
| 4 | 공개 레포를 웹으로 읽는지 | M3 실습 1 |
| 5 | ~~기억 가져오기가 앱에 있는지~~ → **풀림 (10/25 직접)**: Data controls 에 「Import memory」 있음. 쓰는 방법은 아직 | M3 에서 열어 본다 |
| 6 | ~~앱의 실제 커넥터 목록~~ → **풀림 (10/25 직접)**: Google Drive · GitHub · Dropbox 있음. Box · Notion · Granola 는 「See all」을 안 펼쳐 미확인 | 완료 (Box 등은 M4 실습 1) |
| 7 | GitHub · Dropbox 커넥터를 레포 하나 · 폴더 하나로 좁힐 수 있는지 | M4 실습 3 |
| 8 | 학습 사용 끄기가 커넥터 데이터까지 막는지 | M4 실습 1 |
| 9 | Windows 앱 출시와, 허용한 폴더만 보게 할 수 있는지 | M4 (나오면) |

v1 미확인 4개 가운데 **음성 입력은 직접 확인으로 풀렸고**, GitHub 은 「커넥터 발표 · 권한 미확인」으로 바뀌었다. 개별 다운로드와 전체 다운로드 형식은 그대로 M2 로 넘어간다.

## 확인 방법

- **v1 (2026-10-18)**: Live #32 방송 중 Claude Code 가 Meta 발표문과 도움말 6개 페이지를 직접 열어 확인했다. Muse 앱 화면은 열지 않았다.
- **v2 (2026-10-25)**: Claude Code 가 Meta 도움말(Artifacts · 데이터 관리 · 시작하기 · 커넥터 · 안내와 승인) · Meta Connect 2026 발표 · Dropbox 도움말 · Microsoft 발표를 다시 열어 확인하고, 박창수가 2026-10-20~22 안드로이드에서 직접 다뤄 본 결과를 더했다. 근거 정리는 [첫 조사](../../vl_materials/vault-connection-first-research.md). 일부 도움말 주소는 `help/artificial-intelligence/` 에서 `help/superintelligence/` 로 옮겨 간 것으로 보여, 이번에 연 주소를 적었다.
- **앱 화면 (2026-10-25, Live #33)**: 박창수가 앱 Settings → Connectors 의 Available 목록 화면을 직접 확인했다(계정 정보 가림). 연결 여부 같은 계정별 설정 상태는 공개 문서에 적지 않는다. 전체 데이터 내려받기도 이날 직접 받아 구조를 확인했다(파일 이름 · 내용은 적지 않는다).
- **남은 것**: Connectors 「See all」 펼쳐 Box · Notion · Granola 확인 (M4 실습 1)
