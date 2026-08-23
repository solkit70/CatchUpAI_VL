# WorkLog - M1: 실행 구조 이해와 첫 모델링

**날짜**: 2026-08-23
**Topic**: Claude-Code-Mobile-Remote-Execution
**모듈**: M1 - 실행 구조 이해와 첫 모델링
**학습 시간**: 진행 중

## 오늘의 학습 목표

- [x] 모바일, 원격 접속 계층, 로컬 실행 머신, Claude Code의 역할을 분리해서 설명한다.
- [x] "모바일에서 조작"과 "집 머신에서 실행"의 차이를 다이어그램으로 표현한다.
- [x] 명령 실행 위치, 파일 변경 위치, 인증 위치를 구분한다.
- [x] 실패 지점 5개 이상을 식별한다.

## 진행 내용

### 1. 공식 문서 확인

**목적**: Claude Code가 어디에서 실행되는 도구인지 확인했다.

**과정**:
1. Anthropic Claude Code overview, setup, CLI reference를 확인했다.
2. Claude Code가 터미널에서 동작하고 프로젝트 디렉터리에서 `claude`로 시작하는 구조임을 확인했다.
3. CLI reference에서 interactive REPL과 print mode 명령을 확인했다.

**결과**:
- 모바일은 실행 호스트가 아니라 원격 조작 클라이언트라는 M1의 기본 전제를 확인했다.

### 2. 실행 구조 문서 작성

**목적**: iPhone, 원격 접속 계층, 집 머신, Claude Code, vault의 역할을 분리했다.

**결과**:
- `01-Execution-Model/concepts/mobile-to-local-execution.md`
- `01-Execution-Model/concepts/command-file-session-flow.md`

### 3. 실행 흐름 다이어그램 작성

**목적**: 모바일 조작과 로컬 실행의 흐름을 시각화했다.

**결과**:
- `01-Execution-Model/diagrams/execution-flow.md`

## 문제 해결 로그

### 문제 1: Claude Code 관련 최신 동작 전제 확인 필요

**증상**: M1 문서가 실행 구조를 설명하므로 Claude Code가 로컬 터미널에서 실행되는 도구라는 전제를 확인해야 했다.

**해결**: Anthropic 공식 문서의 overview, setup, CLI reference를 확인하고 문서에 참조 링크를 남겼다.

## DoD 체크리스트

- [x] 실행 흐름 다이어그램 작성
- [x] 모바일 조작과 로컬 실행의 차이 설명
- [x] 명령 실행 위치와 파일 변경 위치 명시
- [x] 세션/인증/네트워크 실패 지점 5개 이상 정리
- [x] README.md에 학습 순서와 문서 링크 정리
- [x] WorkLog 작성

**완료율**: 6/6 (100%)

## Daily Retrospective

### What went well

- 모바일 조작과 로컬 실행을 명확히 분리해 이후 실험의 기준을 세웠다.
- 맥미니/맥 스튜디오 홈서버 구조도 M1 다이어그램에 확장 형태로 포함해 다음 모듈의 비교 작업으로 자연스럽게 이어지게 했다.

### What could be improved

- 실제 세션 유지 방식은 아직 확정하지 않았다. Windows에서 session manager를 어떻게 쓸지는 M3-M4에서 환경 확인 후 결정해야 한다.

### Insights

- 이 Topic의 핵심은 "모바일에서 Claude Code를 실행한다"가 아니라 "모바일에서 집 머신의 Claude Code 실행 환경을 조작한다"는 표현으로 정리된다.
- 이후 모든 실험은 어느 머신의 어느 디렉터리에서 명령이 실행되는지 증거를 남기는 방식으로 설계해야 한다.

### Tomorrow's focus

- M2에서 SSH, Tailscale/ZeroTier, 클라우드 개발 환경, 맥미니/맥 스튜디오 홈서버 구조를 비교한다.
- 현재 사용 패턴 기준으로 1차 실험 구조 후보를 좁힌다.

## 참조 및 산출물

**생성된 파일/폴더**:
- `01-Execution-Model/README.md`: M1 학습 순서
- `01-Execution-Model/concepts/mobile-to-local-execution.md`: 모바일 조작과 로컬 실행 설명
- `01-Execution-Model/concepts/command-file-session-flow.md`: 명령, 파일, 인증, 세션 흐름
- `01-Execution-Model/diagrams/execution-flow.md`: Mermaid 실행 흐름 다이어그램

**참조 자료**:
- Anthropic Claude Code overview: https://docs.anthropic.com/ko/docs/claude-code/overview
- Anthropic Claude Code setup: https://docs.anthropic.com/en/docs/claude-code/getting-started
- Anthropic Claude Code CLI reference: https://docs.anthropic.com/en/docs/claude-code/cli-usage

**작성자**: Codex
**방법론**: VibeLearn AI
