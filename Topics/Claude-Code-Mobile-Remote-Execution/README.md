# 밖에서 폰으로 내 컴퓨터의 AI 쓰기

> AI에게 일을 시켜 놓고도 **승인 버튼 하나 누르려고 컴퓨터 앞을 못 뜨는** 문제를 해결하는 세 가지 방법을, 전부 직접 해 보고 정리한 자료입니다.

| | |
|---|---|
| **모듈** | M1 ~ M9 |
| **검증 기기** | iPhone · iPad · Windows 11 노트북 |
| **검증 대상 AI** | Claude Code · Codex · Gemini CLI |
| **기준일** | 2026-08-30 |
| **방법론** | [VibeLearn AI (CUA_VL)](https://github.com/solkit70/CatchUpAI_VL) |

**영상으로 보기** — 🇰🇷 [한국어](https://youtu.be/d308t2uQw3I) (11:18) · 🇺🇸 [English](https://youtu.be/OKxdx6KbOPg) (10:38)

## 무엇을 다루나

AI에게 자료 조사나 문서 작업을 맡기면 시간이 크게 줄어듭니다. 그런데 내 컴퓨터의 파일을 건드리는 일이라 **승인이 자주 필요합니다.** 결국 실제 일은 AI가 하고 사람은 보고 승인만 누르는데, **그 승인 하나 때문에 컴퓨터 앞에 묶입니다.**

이 자료는 그 승인을 휴대폰에서 하는 방법을 다룹니다. 세 가지 경로를 **전부 직접 세팅하고 실측**했습니다.

### 중요한 건 순서가 아니라 분기입니다

난이도 사다리를 올라가는 게 아닙니다. **쓰시는 AI에 맞는 방법 하나만** 고르시면 됩니다.

| 쓰는 AI | 방법 | 걸리는 시간 | 모듈 |
|---|---|---|---|
| 🟣 **Claude Code** | Remote Control — **앱에 이미 들어 있습니다** | 5분 | [M8](08-Native-Remote-Control/) |
| 🟢 **Codex** | ChatGPT 데스크톱 앱 설치 | 15분 | [M9](09-Codex-Remote/) |
| 🔵 **그 외 전부** | SSH — **모든 AI에서 됩니다** | 30분 | [M1~M7](#폴더-구조) |

> 🔵 SSH는 Gemini 전용이 아닙니다. **CLI를 쓸 수 있는 AI라면 Claude든 Codex든 전부** 이 방법으로 됩니다. 앞의 둘이 못 하는 일(임의 셸 작업, 프로그램이 꺼져 있을 때 다시 켜기)까지 되는 대신 손이 제일 많이 갑니다.

## 이 자료의 결론

**세 경로 모두 같은 모델입니다** — *모바일은 조작 콘솔, 실행은 로컬.* M1에서 세운 이 모델이 세 번 연속으로 확인됐습니다.

차이는 **무엇이 호스트 노릇을 하느냐**에서 갈립니다. 이 한 가지가 나머지 차이를 대부분 설명합니다.

| | SSH | Claude Remote Control | Codex Remote |
|---|---|---|---|
| **호스트 주체** | Windows OpenSSH 서버 | `claude` 프로세스 자신 | **ChatGPT 데스크톱 앱** |
| CLI에서 설정 | 가능 | 가능 | **불가** |
| 다룰 수 있는 AI | **무엇이든** | Claude Code만 | Codex만 |
| 임의 셸 작업 | **가능** | 불가 | 불가 |
| 실행 계정 | `catchupai` (격리) | 일상 계정 | 일상 계정 |
| 한글 입력 | ⚠️ iPad 자모 분리 | 정상 | 정상 |
| 푸시 알림 | 없음 | 지원 | 지원 |

→ 전체 비교표: [09-Codex-Remote/comparisons/three-way-remote-comparison.md](09-Codex-Remote/comparisons/three-way-remote-comparison.md)

### 세 방법 모두 필요한 것

- **집 컴퓨터가 켜져 있어야 합니다** — 절전 모드도 안 됩니다
- 컴퓨터와 폰 **양쪽 다 인터넷 연결**
- 쓰시는 AI에 **로그인**되어 있을 것
- **공유기 설정은 안 건드립니다** — 세 방법 다 인바운드 포트를 열지 않습니다

## 목적별 바로가기

### 지금 당장 따라 하고 싶다

| 원하는 것 | 문서 |
|---|---|
| SSH 전체 세팅 절차 | [M4 실험 절차서](04-Remote-Execution-Lab/lab/experiment-plan.md) |
| 명령어 전문·운영 규칙 | [M5 원격 작업 런북](05-Operations-Security/guides/remote-work-runbook.md) |
| Claude Remote Control 켜기 | [M8 연결 구조와 요건](08-Native-Remote-Control/concepts/native-remote-control-model.md) |
| Codex Remote 켜기 | [M9 모듈](09-Codex-Remote/) |

### 막혔을 때

| 증상 | 문서 |
|---|---|
| 접속이 안 된다 | [M5 복구 플레이북](05-Operations-Security/troubleshooting/recovery-playbook.md) |
| 세션이 자꾸 끊긴다 | [M4 접속/세션 문제 로그](04-Remote-Execution-Lab/troubleshooting/remote-session-issues.md) |
| **터미널에서만 Remote Control이 안 된다** | [M8 실측 기록](08-Native-Remote-Control/lab/remote-control-verification.md) — 원인은 버전이 아니라 `ANTHROPIC_API_KEY` |
| iPad에서 한글이 자모로 분리된다 | [M5 iPad 한글 IME 문제](05-Operations-Security/guides/ipad-korean-input-lessons.md) |
| GitHub push에서 계정 선택 창이 뜬다 | [M5 GitHub push 설정](05-Operations-Security/guides/github-push-and-local-review.md) |

### 어느 방법을 쓸지 정하고 싶다

- [M8 상황별 선택 기준](08-Native-Remote-Control/decisions/which-path-when.md)
- [M2 기술 구조 비교표](02-Architecture-Comparison/comparisons/structure-comparison-table.md)
- [M9 Codex Remote 운용 규칙](09-Codex-Remote/decisions/codex-remote-usage-rules.md) — 어디까지 해도 되는지

### 안전하게 쓰고 싶다

- [M5 보안 체크리스트](05-Operations-Security/guides/security-checklist.md)
- [M3 vault 작업 경계](03-Environment-Audit/audit/vault-safety-checklist.md)

> ⚠️ **Claude·Codex 방식은 평소 쓰던 계정에 그대로 붙고, 대화 내용이 서버를 거칩니다.** SSH 구조가 지키던 계정 격리(`catchupai`)가 없습니다. 민감한 자료를 다룰 때는 연결을 끄고 컴퓨터 앞에서 하는 편이 낫습니다. **끄는 것도 켤 때와 같은 자리에서 됩니다.**

## 이 자료에서 뒤집힌 전제들

직접 해 보고 나서 **처음 생각과 달라진 것**들입니다. 이 자료의 값어치는 대부분 여기 있습니다.

**① 우회로를 다 돈 뒤에 직행로를 발견했다**

M1~M7에서 SSH·Tailscale·Termius로 전체 구조를 만든 **뒤에야** Claude Code에 네이티브 Remote Control이 있다는 것을 알았습니다(2026-08-28). 원래 배우려던 게 이 기능이었는데 7개 모듈을 돌고 나서 발견한 셈입니다.

그런데 낭비가 아니었습니다. *"인바운드 포트를 열지 않는다"* 가 왜 중요한지는 **포트포워딩을 보안 2점으로 매겨 본 사람만** 압니다. **비교 대상이 없으면 편의성만 보입니다.**

**② "Claude 밖의 일은 안 된다"는 오해**

Remote Control로도 **명령 실행은 됩니다.** 클로드한테 시키면 클로드가 합니다. 진짜 제약은 **`claude` 프로세스가 살아 있어야 한다**는 것이고, 그게 죽으면 폰에서 다시 켤 방법이 없습니다. → **그때 필요한 게 SSH입니다.**

**③ Codex는 CLI로 설정할 수 없다**

Codex Remote의 호스트는 Codex CLI가 아니라 **ChatGPT 데스크톱 앱**입니다. 앱이 꺼지거나 컴퓨터가 잠자기로 들어가면 끊깁니다. 공식 문서 표현 그대로 — *"If that computer sleeps, loses network access, or closes the app, remote access stops."*

**④ 브라우저 조작은 되는데 폰에서 볼 수는 없다**

Codex의 Computer Use는 실제로 동작합니다. 시키면 페이지를 엽니다(Facebook → LinkedIn → Seattle Times 연속 확인). 그런데 **그 화면이 폰에는 안 보입니다.** 조작은 원격, 화면은 호스트에만 있습니다. 밖에서 쓰는 기능으로는 아직 아쉽습니다.

## 폴더 구조

```
Claude-Code-Mobile-Remote-Execution/
├── 01-Execution-Model/          M1  실행 구조 이해와 첫 모델링
├── 02-Architecture-Comparison/  M2  기술 구조 비교와 홈서버 옵션
├── 03-Environment-Audit/        M3  Windows 노트북 환경 점검
├── 04-Remote-Execution-Lab/     M4  모바일 원격 실행 1차 실험
├── 05-Operations-Security/      M5  보안·운영·백업 가이드
├── 06-Publishing-Video-Plan/    M6  최종 패키징과 영상화 계획
├── 07-Multi-Agent-CLI-Setup/    M7  iPad에서 Codex/Gemini CLI 검증
├── 08-Native-Remote-Control/    M8  Claude 네이티브 Remote Control
├── 09-Codex-Remote/             M9  Codex Remote 검증과 세팅
├── vl_roadmap/                  로드맵
├── vl_worklog/                  모듈별 작업 기록
└── topic_starter.md             Topic 시작 문서
```

**M1~M7**이 SSH 경로의 본체이고, **M8·M9**는 Topic Retrospective 이후에 추가한 유지보수 모듈입니다.

→ 전체 산출물 목록: [06-Publishing-Video-Plan/summary/final-recommendation.md](06-Publishing-Video-Plan/summary/final-recommendation.md)

## 출처와 주의사항

- **실측 환경은 Windows 11 + iPhone/iPad입니다.** macOS·Android는 검증하지 않았습니다
- 기준일은 **2026-08-30**입니다. Claude Code와 ChatGPT 데스크톱 앱은 빠르게 바뀌므로, 화면과 메뉴 이름이 다를 수 있습니다
- 성공한 것뿐 아니라 **실패와 그 원인**도 그대로 남겼습니다. 완성된 가이드보다 막히는 지점이 더 도움이 된다고 봤습니다
- **미검증으로 남긴 것**도 표시해 두었습니다 — iPad 푸시 알림, Windows 절전 후 재연결, 장시간 작업 안정성

## 라이선스와 문의

이 자료는 [CatchUpAI_VL](https://github.com/solkit70/CatchUpAI_VL) 저장소의 일부입니다.
질문이나 제안은 저장소 이슈로 남겨 주세요.

**만들고, 나누고, 함께 자랍니다.**
