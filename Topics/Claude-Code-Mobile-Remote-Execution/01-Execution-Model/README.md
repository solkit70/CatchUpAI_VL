# M1 - 실행 구조 이해와 첫 모델링

**상태**: 진행 중
**예상 학습 시간**: 1.5h
**Topic**: Claude-Code-Mobile-Remote-Execution

## 학습 순서

1. [concepts/mobile-to-local-execution.md](concepts/mobile-to-local-execution.md) - 모바일 조작과 로컬 실행의 역할 분리를 학습한다.
2. [concepts/command-file-session-flow.md](concepts/command-file-session-flow.md) - 명령, 파일, 인증, 세션 흐름을 정리한다.
3. [diagrams/execution-flow.md](diagrams/execution-flow.md) - 전체 실행 구조를 Mermaid 다이어그램으로 확인한다.

## 핵심 요약

이번 모듈의 핵심은 iPhone이 코드를 직접 실행하는 장치가 아니라 원격 조작 인터페이스라는 점을 분명히 하는 것이다. Claude Code 프로세스, shell, Git, vault 파일 접근은 실행 호스트인 집 노트북 또는 홈서버에서 일어난다.

## 산출물

- 실행 흐름 다이어그램
- 모바일 조작과 로컬 실행 설명
- 명령 실행 위치와 파일 변경 위치 설명
- 실패 지점과 확인 방법 목록

## 이전/다음 모듈

- 이전 모듈: 없음
- 다음 모듈: `02-Architecture-Comparison/`
