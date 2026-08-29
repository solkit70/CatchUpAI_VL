# Remotion AI 영상 제작 계획 - 모바일에서 집 컴퓨터의 AI CLI를 관리하기

## 제작 상태

**상태**: 계획 검토 대기  
**작성일**: 2026-08-25  
**Topic**: Claude-Code-Mobile-Remote-Execution  
**GitHub Topic 링크**: https://github.com/solkit70/CatchUpAI_VL/tree/main/Topics/Claude-Code-Mobile-Remote-Execution

이 문서는 `Claude-Code-Mobile-Remote-Execution` Topic을 바탕으로 Remotion AI 영상을 만들기 위한 승인용 제작 계획이다. 이 단계에서는 아직 Remotion 컴포넌트, TTS 오디오, MP4 렌더링을 진행하지 않는다. 사용자가 이 계획을 승인한 뒤 `remotion-video` 프로세스의 첫 단계인 `video-slide-plan.md` 작성으로 넘어간다.

## 영상의 문제의식

AI와 함께 일하는 방식은 점점 "사람이 직접 계속 타이핑하는 일"에서 "AI에게 일을 맡기고, 사람은 중간중간 방향과 승인만 관리하는 일"로 바뀌고 있다. 그런데 AI CLI가 로컬 컴퓨터에서 긴 작업을 하는 동안, 사람이 승인 버튼을 누르기 위해 계속 컴퓨터 앞에 앉아 있는 것은 비효율적이다. 잠깐 밖에 나갈 때마다 노트북을 들고 다니는 것도 같은 이유로 번거롭다.

이 Topic은 그 문제를 해결하기 위해 시작되었다. 휴대폰과 iPad는 항상 들고 다니므로, 모바일 기기에서 집에 있는 Windows 컴퓨터에 안전하게 접속하고, 그 컴퓨터에서 실행되는 Claude Code, Codex, Gemini 같은 AI CLI를 모니터링하고 관리할 수 있는 구조를 연구했다. 핵심은 모바일이 작업을 실행하는 것이 아니라, 집 컴퓨터에서 일하는 AI를 조작하고 관리하는 콘솔이 된다는 점이다.

## 핵심 메시지

> AI가 일하는 현장에 사람이 계속 앉아 있을 필요는 없다. 모바일은 작업 머신이 아니라 관리 콘솔이 될 수 있고, 실제 실행은 집 컴퓨터에서 계속된다.

영상은 세부 설치 튜토리얼 전체를 설명하지 않는다. 대신 왜 이 구조가 필요한지, 어떤 계층으로 동작하는지, 실제로 어떤 시행착오가 있었는지, 더 자세한 절차는 어디에서 볼 수 있는지를 전달한다. 세부 명령과 문서는 영상 안의 QR 코드와 GitHub Topic 링크로 안내한다.

## 대상 시청자

- Claude Code, Codex, Gemini 같은 AI CLI를 로컬 컴퓨터에서 사용하는 사람
- 외부 활동 중에도 집 컴퓨터의 AI 작업을 확인하고 싶은 사람
- AI에게 작업을 맡기되 승인/검토는 직접 하고 싶은 사람
- 노트북을 항상 들고 다니는 방식이 비효율적이라고 느끼는 사람
- Tailscale, SSH, Termius 같은 도구의 역할 차이를 알고 싶은 사람

## 영상 형식 제안

| 항목 | 제안 |
|---|---|
| 예상 길이 | 7~9분 |
| 언어 | 한국어 내레이션 |
| 톤 | 문제 제기 → 구조 설명 → 실제 시행착오 → 해결 구조 → 더 알아볼 링크 안내 |
| 화면 구성 | Remotion 슬라이드 + 실제 모바일/터미널 스크린샷 + 구조 다이어그램 + QR 코드 |
| 세부 튜토리얼 처리 | 영상에서는 요약만 설명하고 GitHub Topic 문서로 유도 |
| 최종 CTA | QR 코드로 Topic 문서 확인, 자신의 환경에 맞게 Tailscale/SSH 구조부터 검토 |

## GitHub QR 코드 전략

영상에는 Topic 전체 문서로 이동하는 QR 코드를 최소 2번 노출한다.

| 위치 | 목적 | QR 대상 |
|---|---|---|
| 초반 문제 제기 후 | "이 실험 전체 기록은 여기" 안내 | Topic root 링크 |
| 후반 실전 팁/실패 사례 후 | 세부 설치 절차와 troubleshooting 문서 안내 | Topic root 링크 또는 `06-Publishing-Video-Plan` |

기본 QR 대상은 아래 링크로 한다.

```text
https://github.com/solkit70/CatchUpAI_VL/tree/main/Topics/Claude-Code-Mobile-Remote-Execution
```

QR 이미지는 실제 제작 단계에서 `AI/RemotionStudio/public/claude-mobile-remote/qr-topic.png` 같은 경로로 생성해 사용한다. 영상에는 QR 코드와 함께 짧은 텍스트로 "자세한 설정 절차와 문서는 QR에서 확인"이라고 안내한다.

## 스토리라인 초안

| 순서 | 장면 | 핵심 내용 | 시각 자료 |
|---:|---|---|---|
| 1 | 오프닝 문제 제기 | AI에게 일을 시켜도 사람은 승인 때문에 컴퓨터 앞에 묶인다 | 사람은 밖에 있고 집 컴퓨터에서 AI가 일하는 구조 다이어그램 |
| 2 | 기존 방식의 비효율 | 노트북을 들고 다니거나, 컴퓨터 앞에서 기다리는 방식의 한계 | 노트북/모바일 대비, 간단한 Before/After |
| 3 | 핵심 아이디어 | 휴대폰은 실행 머신이 아니라 관리 콘솔이다 | Mobile -> Tailscale -> Windows -> AI CLI 계층도 |
| 4 | 선택한 구조 | iPhone/iPad + Tailscale + Termius + Windows OpenSSH + catchupai 계정 | Topic의 실행 구조 Mermaid를 Remotion SVG로 재구성 |
| 5 | 실제 성공 장면 | iPad Termius에서 집 Windows에 접속하고 AI CLI를 실행 | 제공 스크린샷 중 민감정보 마스킹 후 사용 |
| 6 | 실패 사례 1 | iPad에 Termius만 있고 Tailscale이 없으면 접속 timeout | Tailscale/Termius 역할 분리 다이어그램 |
| 7 | 실패 사례 2 | GitHub 계정이 두 개면 모바일에서 push 팝업을 처리하기 어렵다 | GitHub SSH alias 구조 요약 |
| 8 | 실패 사례 3 | 한글 입력이 자모로 분리되는 Termius/IME 문제 | 한글 자모 분리 스크린샷 또는 재현 화면 마스킹 |
| 9 | 확장 검증 | Claude뿐 아니라 Codex, Gemini도 같은 구조로 사용 가능 | 세 CLI 카드: Claude / Codex / Gemini |
| 10 | 운영 원칙 | 동시에 열 수는 있지만 같은 파일을 동시에 고치면 안 된다 | 단일 편집자/역할 분리/순차 핸드오프 표 |
| 11 | 더 자세한 방법 | 세부 명령과 설정은 GitHub Topic 문서로 안내 | QR 코드 + 문서 목록 하이라이트 |
| 12 | 결론 | 관리자는 현장에 붙어 있을 필요가 없다. 모바일로 AI 작업을 관리한다 | 최종 구조 다이어그램 + QR 코드 |

## 영상에서 자세히 설명하지 않고 문서로 넘길 항목

| 영상에서는 요약 | 자세한 문서 안내 |
|---|---|
| Tailscale과 Termius의 역할 차이 | `05-Operations-Security/guides/mobile-client-setup-lessons.md` |
| Windows OpenSSH 설치/방화벽 설정 | `04-Remote-Execution-Lab/README.md`, `05-Operations-Security/guides/remote-work-runbook.md` |
| GitHub push 계정 고정 | `05-Operations-Security/guides/github-push-and-local-review.md`, `github-push-video-lessons.md` |
| 한글 IME 문제와 우회 | `05-Operations-Security/guides/ipad-korean-input-lessons.md` |
| Codex/Gemini까지 확장 | `07-Multi-Agent-CLI-Setup/README.md`, `checks/ipad-termius-cli-check.md` |
| 병행 사용 규칙 | `07-Multi-Agent-CLI-Setup/guides/multi-cli-session-rules.md` |
| 맥미니/맥 스튜디오 홈서버 판단 | `02-Architecture-Comparison/comparisons/mac-mini-vs-mac-studio-server.md` |

## 스크린샷 활용 계획

스크린샷 위치:

```text
C:\AI_study\2026\Changsoo_Vault\Ingest\CatchUpAI_VL\Topics\Claude-Code-Mobile-Remote-Execution\vl_materials\video-assets\screenshots
```

스크린샷은 영상의 신뢰도를 높이는 데 유용하지만, 공개 전에 반드시 민감정보 검토가 필요하다. 현재 원본 이미지는 GitHub에 올리지 않고 로컬에만 두는 것이 맞다.

### 사용할 수 있는 장면 후보

- iPhone/iPad Termius에서 Windows SSH 세션에 접속된 화면
- Claude Code가 모바일 SSH 세션 안에서 실행되는 화면
- `where codex`, `codex --version`, `gemini` 실행 확인 장면
- Tailscale 미설치로 timeout이 발생한 장면
- 한글 입력이 자모로 분리되는 장면
- GitHub SSH key/계정 관련 설정 장면은 계정 정보 마스킹 후 사용

### 반드시 마스킹할 정보

- Tailscale IP 주소
- Windows host name
- Windows 사용자명
- 이메일 주소
- GitHub 계정명 노출 범위
- API key, password, private key, 인증 코드
- SSH config 상세 경로 중 개인 식별 정보가 들어간 부분

## 디자인 방향

기술 튜토리얼이지만 딱딱한 설치 강의처럼 만들지 않는다. 핵심은 "AI에게 일을 맡기는 시대의 관리 방식"이므로, 초반에는 문제의식과 워크플로우 변화를 보여주고, 중반에는 구조를 계층으로 설명하며, 후반에는 실제 실패 사례와 해결책을 빠르게 보여준다.

| 요소 | 방향 |
|---|---|
| 배경 | 밝은 회색/잉크/전기 초록 포인트의 기술 문서형 팔레트 |
| 폰트 | Noto Sans KR + JetBrains Mono 계열 |
| 애니메이션 | 계층도 선 연결, terminal cursor blink, 카드 전환, QR pulse |
| 화면 비율 | 16:9 기본, 필요 시 shorts용 리컷은 별도 |
| 실제 화면 | 전체 노출보다 crop + blur/mask + callout 방식 |

## 제작 단계

Remotion 작업은 아래 승인 흐름으로 진행한다.

1. **Phase 1 - video-slide-plan.md 작성**: 이 계획을 바탕으로 슬라이드별 내레이션 스크립트와 시각 자료를 상세화한다. 작성 후 사용자 리뷰와 승인 필요.
2. **Phase 1.5 - asset/image/QR plan 작성**: 사용할 스크린샷 후보를 고르고 마스킹 대상 목록을 확정한다. QR 코드 생성 계획도 포함한다. 승인 전 원본 스크린샷은 공개/커밋하지 않는다.
3. **Phase 2 - Remotion 컴포넌트 구현**: `AI/RemotionStudio/`에 새 video-id로 컴포넌트를 만든다. Studio preview를 먼저 확인하고 사용자 승인 전 최종 렌더링하지 않는다.
4. **Phase 3a - edge-tts 초벌 음성**: 빠른 초벌 오디오를 만들어 길이와 호흡을 확인한다. 이 단계에서는 MP4 최종 렌더링 금지.
5. **Phase 3b - Qwen3-TTS 최종 음성 교체**: 최종 음성으로 교체하고 timing을 재측정한다. 사용자 최종 리뷰 후에만 렌더링한다.
6. **Phase 4 - MP4 렌더링**: 보안 마스킹, 내레이션, 자막/화면 sync 승인 후 최종 MP4를 렌더링한다.

## 승인 전 확인할 사항

- 이 영상의 중심 메시지가 "모바일로 집 컴퓨터의 AI CLI를 관리한다"로 충분히 명확한가?
- Claude Code 중심으로 설명하되 Codex/Gemini 확장을 후반부에 넣는 구성이 적절한가?
- QR 코드는 Topic root 하나로 충분한가, 아니면 특정 문서별 QR을 추가할 것인가?
- 스크린샷을 어느 정도까지 사용할 것인가: 실제 화면 중심 vs Remotion 재구성 중심
- 공개 영상에서 GitHub 계정명과 이메일을 어느 수준까지 마스킹할 것인가?
- 영상 길이는 7~9분으로 진행할 것인가, 10~12분 상세형으로 갈 것인가?

## 다음 작업

사용자가 이 계획을 승인하면 다음 파일을 만든다.

```text
AI/RemotionStudio/claude-mobile-remote/video-slide-plan.md
```

또는 RemotionStudio의 기존 구조에 맞춰 같은 의미의 video-id 폴더를 생성한다. 다음 단계에서는 슬라이드별 제목, 화면 텍스트, 내레이션 전문, 사용할 문서 링크, 사용할 스크린샷 후보를 확정한다.
