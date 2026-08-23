# M2 - 기술 구조 비교와 홈서버 옵션 평가

**상태**: 완료
**예상 학습 시간**: 2h
**Topic**: Claude-Code-Mobile-Remote-Execution

## 학습 순서

1. [concepts/remote-architecture-patterns.md](concepts/remote-architecture-patterns.md) - 원격 실행 구조의 주요 패턴을 먼저 이해한다.
2. [comparisons/structure-comparison-table.md](comparisons/structure-comparison-table.md) - 후보 구조를 같은 기준으로 비교한다.
3. [comparisons/mac-mini-vs-mac-studio-server.md](comparisons/mac-mini-vs-mac-studio-server.md) - 맥미니/맥 스튜디오 홈서버 도입안을 비교한다.
4. [decisions/recommended-first-experiment.md](decisions/recommended-first-experiment.md) - 현재 환경 기준 1차 실험안을 확인한다.

## 핵심 결론

현재 1차 실험은 `iPhone -> Tailscale 사설망 -> Windows OpenSSH Server -> Claude Code -> Vault` 구조가 가장 적합하다. 공개 포트를 열지 않고도 모바일에서 집 노트북에 접근할 수 있고, 이미 보유한 Windows 노트북으로 구조를 검증한 뒤 맥미니/맥 스튜디오 홈서버 도입 여부를 판단할 수 있다.

맥미니/맥 스튜디오는 "지금 바로 구매해서 해결"할 대상이 아니라, 1차 실험 성공 후 상시 실행 호스트가 실제로 필요한지 확인하고 결정하는 것이 좋다. Claude Code 중심의 원격 코딩 서버라면 맥미니가 우선 후보이고, 영상 렌더링/멀티미디어 작업까지 상시 서버에 맡길 경우에만 맥 스튜디오가 설득력을 갖는다.

## 산출물

- 원격 실행 구조 패턴 설명
- 기술 구조 비교표
- 맥미니/맥 스튜디오 홈서버 도입 판단표
- 현재 환경 기준 1차 추천 구조

## 이전/다음 모듈

- 이전 모듈: `01-Execution-Model/`
- 다음 모듈: `03-Environment-Audit/`
