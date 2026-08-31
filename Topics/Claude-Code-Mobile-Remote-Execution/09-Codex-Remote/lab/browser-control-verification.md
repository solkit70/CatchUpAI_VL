---
title: "Codex 내장 브라우저 원격 조작 실측"
created: 2026-08-30 21:40:00
tags:
  - codex
  - remote
  - computer-use
  - verification
---

## 무엇을 확인했나

M9 1단계에서 Computer Use는 **문서 조사만** 하고 "화면 조작 권한이라 위험이 크다"는 이유로 1차 세팅에서 제외했었다. 이번에 사용자가 직접 켜서 **브라우저 조작 부분만** 시험했다.

결과를 한 줄로 줄이면 이렇다 — **조작은 원격에서 되는데, 화면은 원격에서 못 본다.**

## 실측 결과

| # | 항목 | 결과 |
|---|---|---|
| 1 | ChatGPT 데스크톱 앱에 브라우저 패널이 있는가 | ✅ 있다. 창 **오른쪽에 패널**로 열리고 탭을 여러 개 유지한다 |
| 2 | 자연어로 페이지를 열 수 있는가 | ✅ *"Please Open Linkedin Page"* → *"LinkedIn 페이지를 브라우저 패널에 열었습니다"* |
| 3 | 아이패드에서 원격으로 조작되는가 | ✅ 된다 |
| 4 | **아이패드에서 브라우저 화면이 보이는가** | ❌ **안 보인다** |
| 5 | 기존 Chrome 로그인 세션을 그대로 쓰는가 | ❌ 아니다. 내장 브라우저는 **별도 상태**를 쓴다 |

### 4번이 이 실측의 핵심이다

원격에서 *"이 페이지 열어 줘"* 라고 시키면 **집 컴퓨터의 화면에서는** 실제로 열린다. 그런데 **아이패드 ChatGPT 앱에는 그 화면이 안 뜬다.** 텍스트 응답으로 *"열었습니다"* 라는 말만 돌아온다.

그래서 밖에서 이 기능을 쓰면 **결과를 확인할 수 없는 조작**이 된다. 눈으로 확인하려면 결국 집 컴퓨터 앞으로 가야 한다. Windows에서 잠금 해제 + 포그라운드가 필요하다는 기존 제약보다 **이쪽이 실사용에서 더 결정적이다** — 앞의 것은 준비 조건이지만, 이건 목적 자체를 무너뜨린다.

> 밖에서 쓰려고 켜는 기능인데, 밖에서는 결과를 못 본다.

## 기존 문서의 오류 — Chrome 확장이 전제가 아니다

`concepts/codex-remote-model.md` 에 *"Chrome 확장 설치가 필요하다"* 라고 적어 두었는데 **정확하지 않다.** 둘은 다른 물건이다.

| | 내장 브라우저 | Codex Chrome 확장 |
|---|---|---|
| 설치 | 데스크톱 앱에 **이미 들어 있다** | 별도 설치 |
| 브라우저 상태 | 앱 전용의 **독립된 상태** | 쓰던 Chrome 그대로 |
| 기존 로그인 | 없음 (가져와야 함) | 있음 |
| 확장 프로그램·열린 탭 | 없음 | 그대로 |

**확장은 "쓰던 Chrome 세션이 필요할 때" 쓰는 것**이지, 브라우저 조작 자체의 전제 조건이 아니다.

여는 단축키는 **`Ctrl + Shift + B`** (Windows) / **`⌘ + Shift + B`** (macOS).

## 로그인 세션을 넘기려면 — 가볍게 볼 일이 아니다

내장 브라우저는 빈 상태로 시작한다. 기존 로그인을 쓰려면 Chrome에서 **가져오기(Import)** 를 해야 하는데, 가져오는 항목이 이렇다.

- **Saved passwords**
- **Cookies**
- **Browsing history**

게다가 안내문이 이렇게 붙는다.

> Windows protects Chrome cookies and passwords with App-Bound Encryption, so ChatGPT also needs administrator approval

즉 **관리자 승인**까지 받아야 하고, 가져오기 전에 **Chrome을 완전히 종료**해야 한다.

**이건 "편의 기능"이 아니라 자격증명 이전이다.** 저장된 비밀번호 전부와 쿠키 전부가 대상이다. 이 Vault처럼 개인정보가 섞인 환경에서는 **가져오기를 하지 않는 쪽을 기본값으로 둔다.** 필요한 사이트가 있으면 내장 브라우저 안에서 그 사이트만 직접 로그인한다.

→ 운용 규칙: [../decisions/codex-remote-usage-rules.md](../decisions/codex-remote-usage-rules.md)

## 증거

실측 화면 3장. **개인정보(사이드바 대화 목록·LinkedIn 계정 화면)가 찍혀 있어 저장소에는 넣지 않는다.**

| 파일 | 무엇 |
|---|---|
| `Codex_Browser.png` | 오른쪽 브라우저 패널 · `Start browsing` · Chrome 가져오기 배너 |
| `Codex_Browser_navigate_Linkedin.png` | *"Please Open Linkedin Page"* 지시 → 탭이 열린 상태 |
| `Codex_Browser_import_Approve.png` | 가져오기 대화상자 · 관리자 승인 안내 |

위치: `AI/RemotionStudio/public/claude-mobile-remote/images/`

## 아직 확인 안 한 것

| 항목 | 왜 남겨 두나 |
|---|---|
| **브라우저 외 데스크톱 조작** (앱 클릭·입력) | 이번엔 브라우저만 시험했다. 위험도가 더 높아 별도 판단이 필요하다 |
| 원격 조작 중 승인 프롬프트가 **모바일에** 뜨는지 | 사이트 접근 권한 요청의 표시 위치를 확인하지 못했다 |
| 잠금 해제·포그라운드 제약의 **실제 체감** | 문서 기준으로만 알고 있다 |
| 모바일에서 **스크린샷이라도** 받아볼 수 있는지 | 화면을 못 보는 것에 우회로가 있는지 미확인 |

## 판단

**밖에서 쓰는 기능으로는 아직 못 쓴다.** 화면을 못 보는 한 원격에서는 "열어 줘"까지가 한계다.

쓸 만한 자리는 **집 컴퓨터 앞에 있을 때**다. 브라우저를 직접 몰지 않고 Codex에게 시키는 용도라면 화면이 눈앞에 있으니 문제가 없다.

## 참조

- 모델 정리: [../concepts/codex-remote-model.md](../concepts/codex-remote-model.md)
- 세팅 절차: [setup-procedure.md](setup-procedure.md)
- 3자 비교: [../comparisons/three-way-remote-comparison.md](../comparisons/three-way-remote-comparison.md)
- 공식 문서: https://learn.chatgpt.com/docs/remote-connections
