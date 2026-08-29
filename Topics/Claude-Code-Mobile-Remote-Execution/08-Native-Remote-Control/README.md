# M8 - Claude Code 네이티브 Remote Control 검증과 구조 비교

## 요약

M8은 Topic Retrospective를 마친 뒤에 추가한 유지보수 모듈이다. **Claude Code에 SSH 없이 모바일에서 로컬 세션을 조종하는 네이티브 기능이 있다**는 사실을 2026-08-28에 발견하고, M1~M7에서 만든 SSH 구조와 어떤 관계인지 정리했다.

발견 경위 자체가 이 모듈의 성격을 보여준다. 사용자가 iPad Claude 앱의 `Code` 탭에서 이 세션이 `Connected` 상태로 떠 있는 것을 보고 스크린샷을 보냈다. **이미 쓰고 있었는데 그게 무엇인지 몰랐던 것이다.**

## 결론

| 질문 | 답 |
|---|---|
| M1~M7의 학습 모델이 틀렸나 | **아니다.** "모바일은 조작 콘솔, 실행은 로컬"은 두 방식 모두에 적용된다 |
| SSH 구조가 무의미해졌나 | **아니다.** Codex·Gemini 실행, 임의 셸 작업, 계정 격리, 홈서버는 대체되지 않는다 |
| 기본 경로를 바꿔야 하나 | **그렇다.** Claude Code만 쓸 거면 Remote Control이 압도적으로 간단하다 |
| 이 환경에서 바로 쓸 수 있나 | 앱에서는 이미 쓰고 있다. **터미널에서는 막혀 있다** — `ANTHROPIC_API_KEY` 때문 |

## 실측에서 나온 문제 두 가지

**버전 격차.** PATH의 CLI는 `2.1.143`인데 VS Code 확장은 `2.1.250`이다. 이 세션은 확장에서 돌아 최신 기능을 쓰지만, 터미널에서 `claude`를 치면 100판 이상 낡은 바이너리가 실행된다. `--continue`, 교차 세션 메시징 등 7개 기능이 버전 게이트에 걸린다.

**API key 충돌.** 셸에 `ANTHROPIC_API_KEY`가 설정되어 있어 `claude remote-control`이 자격 검사에서 거부된다. 나머지 조건은 전부 통과다. "앱에서는 되는데 터미널에서는 안 되는" 증상의 원인이 버전이 아니라 환경변수라는 점이 실무에서 헷갈리기 쉬운 지점이다.

## 보안 관점의 후퇴 두 가지

SSH 구조와 비교하면 Remote Control이 잃는 것이 있다.

**계정 격리가 없다.** SSH 방식은 모바일 접속을 `catchupai`라는 별도 Windows 계정에 묶었고, M5 보안 체크리스트가 그 전제 위에 있었다. Remote Control은 `dougg` 세션에 그대로 붙는다.

**트랜스크립트가 서버에 저장된다.** 연결된 동안 메시지·응답·도구 활동이 Anthropic 서버에 저장된다. 기기 간 동기화에 필요한 설계지만, 이 Vault에는 메일링 리스트·워런티·의료·세무 자료가 있어 의식하고 써야 한다.

## 산출물

- [concepts/native-remote-control-model.md](concepts/native-remote-control-model.md) — 연결 구조, 실행 위치, 시작 방법 4가지, 요건
- [lab/remote-control-verification.md](lab/remote-control-verification.md) — 이 환경 실측, 경계 테스트 6건, 미검증 항목
- [comparisons/ssh-vs-native-remote-control.md](comparisons/ssh-vs-native-remote-control.md) — 항목별 비교, 서로 대체하지 못하는 영역
- [decisions/which-path-when.md](decisions/which-path-when.md) — 결정 흐름, 시나리오별 판단, 민감 작업 규칙

## 영상 제작에 미치는 영향

기존 Remotion 영상 브리프는 SSH 구조를 따라 하는 내용이었다. **그대로 만들면 "쉬운 길이 있는데 왜 이 고생을 하느냐"는 반응이 나온다.**

방향을 바꾸는 편이 낫다. 두 경로를 나란히 보여주고 각각 언제 쓰는지 말하는 구성이 훅도 강하고 정직하다. 실제로 사용자가 겪은 일 — *"이미 쓰고 있었는데 그게 뭔지 몰랐다"* — 이 그대로 도입부가 된다.

### 영상용 스크린샷 (2026-08-28 확보)

기존 Remotion 프로젝트 `claude-mobile-remote` 의 이미지 폴더에 넣어 뒀다.
경로: `AI/RemotionStudio/public/claude-mobile-remote/images/`

| 파일 | 내용 | 쓸 자리 |
|---|---|---|
| `shot-rc-banner.png` | 터미널 배너 — *"Remote Control is active · Continue here, on your phone, or at claude.ai/code"* | 발견 장면. 가장 작고 자막처럼 얹기 좋다 |
| `shot-rc-desktop-session.png` | VS Code 세션 전체 + 배너 + **휴대폰에서 보낸 메시지가 들어온 화면** | "원격에서 조종한다"를 한 장으로 보여주는 컷 |
| `shot-rc-ipad-sessions.png` | iPad ChatGPT… 아니라 Claude 앱 `Code` 탭 — 로컬 세션 2개가 `Connected` | 세션 목록. 자동 생성 이름(`changsoo-modular-teapot`) 규칙이 보인다 |
| `shot-rc-ipad-detail.png` | iPad에서 세션 내용을 읽는 화면 (`Remote control` 라벨) | 실제 사용 장면 |

> ⚠️ `shot-rc-desktop-session.png` 에는 대화 내용(Builders Lounge SNS 홍보 계획표)이 **읽을 수 있는 크기로** 들어 있다. 공개 영상에 쓸 때는 크롭하거나 블러 처리를 판단할 것.

## 이전/다음

- 이전 모듈: [../07-Multi-Agent-CLI-Setup/README.md](../07-Multi-Agent-CLI-Setup/README.md)
- 다음: Remotion 영상 브리프 개정 → [../06-Publishing-Video-Plan/video/remotion-ai-video-brief.md](../06-Publishing-Video-Plan/video/remotion-ai-video-brief.md)
