# Claude-Code-Mobile-Remote-Execution 학습 로드맵

**생성일**: 2026-08-23  
**방법론**: VibeLearn AI  
**버전**: 1.1  
**최종 확정 기간**: 2주, 총 8-12시간

## 학습 개요

이 Topic은 모바일에서 Claude Code를 조작하고, 실제 명령 실행과 파일 변경은 집의 Windows 노트북 또는 향후 맥미니/맥 스튜디오 홈서버에서 일어나도록 구성하는 원격 AI 코딩 환경을 학습하고 검증하는 과정이다. 1차 범위는 현재 Windows 노트북으로 구조를 검증하고, 맥미니/맥 스튜디오 도입은 구매 전 설계와 비교 산출물로 정리하는 것이다.

## 학습 목표

- [x] 모바일에서 Claude Code를 조작하는 구조를 다이어그램과 설명으로 정리할 수 있다.
- [x] 명령이 집/로컬 머신에서 실행되는 네트워크, 인증, 세션, 파일 시스템 흐름을 설명할 수 있다.
- [x] SSH, Tailscale/ZeroTier, 클라우드 개발 환경, 홈서버, 노트북 클라이언트 구조를 비교표로 평가할 수 있다.
- [x] 현재 Windows 노트북에서 모바일 원격 접속 기반 Claude Code 실행 실험을 완료할 수 있다.
- [x] 맥미니/맥 스튜디오 홈서버 도입 시 필요한 장비, 운영 방식, 보안/백업 전략을 설계할 수 있다.
- [x] 최종 운영 가이드와 영상화 가능한 스토리라인을 만들 수 있다.

## 전체 로드맵 구조

| 모듈 | 모듈명 | 난이도 | 예상 시간 | 산출물 폴더 | 상태 |
|---|---|---:|---:|---|---|
| M1 | 실행 구조 이해와 첫 모델링 | 1 | 1.5h | `01-Execution-Model/` | done |
| M2 | 기술 구조 비교와 홈서버 옵션 평가 | 2 | 2h | `02-Architecture-Comparison/` | done |
| M3 | 현재 Windows 노트북 환경 점검 | 2 | 1.5h | 03-Environment-Audit/ | done |
| M4 | 모바일 원격 실행 1차 실험 설계 및 수행 | 3 | 2.5h | `04-Remote-Execution-Lab/` | done |
| M5 | 보안, 운영, 백업 가이드 정리 | 2 | 1.5h | `05-Operations-Security/` | done |
| M6 | 최종 패키징과 Remotion AI 영상화 후보 정리 | 2 | 1h | `06-Publishing-Video-Plan/` | done |

**총 예상 시간**: 약 10시간, 20% 버퍼 포함

## M1 - 실행 구조 이해와 첫 모델링

**난이도**: 1  
**예상 시간**: 1.5h  
**산출물 폴더**: `01-Execution-Model/`  
**상태**: 완료

### 학습 목표

- [ ] 모바일, 원격 접속 계층, 로컬 실행 머신, Claude Code의 역할을 분리해서 설명한다.
- [ ] 모바일에서 조작하는 것과 집 머신에서 실행되는 것의 차이를 다이어그램으로 표현한다.
- [ ] 명령 실행 위치, 파일 변경 위치, 인증 위치를 구분한다.
- [ ] 실패 지점 5개 이상을 식별한다.

### 주요 개념

- 클라이언트와 실행 호스트
- 원격 터미널 세션
- 파일 시스템 경계
- 세션 유지
- Claude 모바일 앱과 Claude Code 원격 실행의 차이

### 실습 과제

- 실행 흐름 다이어그램 작성
- 명령, 파일, 인증, 세션 흐름 설명
- 실패 지점 목록화

### 산출물

```text
01-Execution-Model/
  README.md
  concepts/mobile-to-local-execution.md
  concepts/command-file-session-flow.md
  diagrams/execution-flow.md
```

### Definition of Done

- [x] 실행 흐름 다이어그램 작성
- [x] 모바일 조작과 로컬 실행의 차이 설명
- [x] 명령 실행 위치와 파일 변경 위치 명시
- [x] 세션/인증/네트워크 실패 지점 5개 이상 정리
- [x] README.md에 학습 순서와 문서 링크 정리
- [x] WorkLog 작성

## M2 - 기술 구조 비교와 홈서버 옵션 평가

**난이도**: 2  
**예상 시간**: 2h  
**산출물 폴더**: `02-Architecture-Comparison/`  
**상태**: 완료

### 학습 목표

- [ ] SSH 직접 접속, Tailscale/ZeroTier, 클라우드 개발 환경, 홈서버 구조를 비교한다.
- [ ] 맥미니/맥 스튜디오 서버와 노트북 클라이언트 구조의 장단점을 평가한다.
- [ ] 보안, 비용, 안정성, 이동성, 관리 난이도 기준으로 추천안을 만든다.
- [ ] 내 환경의 1차 실험 구조를 하나 선정한다.

### 주요 개념

- 직접 SSH와 공개 포트 노출
- Tailscale/ZeroTier 사설망 + SSH
- GitHub Codespaces 같은 클라우드 개발 환경
- 현재 Windows 노트북 실행 호스트
- 맥미니/맥 스튜디오 홈서버

### 실습 과제

- 기술 구조 비교표 작성
- 맥미니/맥 스튜디오 도입 시나리오 작성
- 현재 환경 기준 1차 실험 추천안 작성

### 산출물

```text
02-Architecture-Comparison/
  README.md
  concepts/remote-architecture-patterns.md
  comparisons/structure-comparison-table.md
  comparisons/mac-mini-vs-mac-studio-server.md
  decisions/recommended-first-experiment.md
```

### Definition of Done

- [x] 최소 5개 기술 구조 비교
- [x] 맥미니/맥 스튜디오 홈서버 구조 비교
- [x] 노트북 이동 작업기 + 홈서버 상시 실행 구조 설명
- [x] 현재 환경 기준 1차 추천 구조 선정
- [x] 선택하지 않은 구조의 보류 이유 기록
- [x] README.md와 WorkLog 작성

## M3 - 현재 Windows 노트북 환경 점검

**난이도**: 2  
**예상 시간**: 1.5h  
**산출물 폴더**: `03-Environment-Audit/`  
**상태**: 대기

### 학습 목표

- [ ] 현재 노트북의 Claude Code, Git, Node.js/npm, SSH 상태를 확인한다.
- [ ] 외부 접속 실험에 필요한 네트워크와 권한 조건을 정리한다.
- [ ] vault 경로와 원격 작업 시 주의할 파일 변경 범위를 정의한다.
- [ ] 실제 설정 변경 전 체크리스트를 만든다.

### 주요 개념

- 실행 호스트 준비성
- Windows OpenSSH Client와 Server 구분
- Node.js/npm 의존성
- vault 작업 경계
- 설정 변경 전 승인 절차

### 실습 과제

- 로컬 도구 상태 점검
- 원격 실험 전 안전 체크리스트 작성
- Go/No-Go 기준 정리

### 산출물

```text
03-Environment-Audit/
  README.md
  audit/windows-host-readiness.md
  audit/vault-safety-checklist.md
  decisions/preflight-go-no-go.md
```

### Definition of Done

- [ ] Claude Code 로컬 실행 여부 확인
- [ ] Git, Node.js/npm, SSH 상태 기록
- [ ] vault 작업 경계와 백업 기준 정리
- [ ] 외부 설치/계정 연결/보안 변경 승인 필요 항목 분리
- [ ] 1차 실험 Go/No-Go 기준 작성
- [ ] README.md와 WorkLog 작성

## M4 - 모바일 원격 실행 1차 실험 설계 및 수행

**난이도**: 3  
**예상 시간**: 2.5h  
**산출물 폴더**: `04-Remote-Execution-Lab/`  
**상태**: 완료

### 학습 목표

- [ ] 모바일에서 집 노트북 터미널에 접근하는 1차 실험을 설계한다.
- [ ] Claude Code를 원격 세션에서 실행하고 간단한 vault 작업을 수행한다.
- [ ] 명령 실행 위치와 파일 변경 결과를 검증한다.
- [ ] 접속 끊김, 절전, 권한 문제를 관찰하고 기록한다.

### 주요 개념

- 실험 설계
- 인증 경로
- 세션 지속성
- 검증 가능한 작은 작업
- 원격 접속 성공과 안전한 Claude Code 작업 가능 상태의 차이

### 실습 과제

- 1차 실험 절차서 작성
- 모바일 원격 접속 및 Claude Code 실행 테스트
- 실패/복구 로그 작성

### 산출물

```text
04-Remote-Execution-Lab/
  README.md
  lab/experiment-plan.md
  lab/mobile-ssh-claude-code-test.md
  lab/validation-results.md
  troubleshooting/remote-session-issues.md
```

### Definition of Done

- [ ] 실험 절차서 작성
- [ ] 사용자 승인 후 원격 접속 방식 적용
- [ ] 모바일에서 집 머신 터미널 접근 확인
- [ ] Claude Code 또는 안전한 shell 작업 실행 확인
- [ ] 파일 변경 위치 검증
- [ ] 실패/복구 로그 작성
- [ ] README.md와 WorkLog 작성

## M5 - 보안, 운영, 백업 가이드 정리

**난이도**: 2  
**예상 시간**: 1.5h  
**산출물 폴더**: `05-Operations-Security/`  
**상태**: 완료

### 학습 목표

- [ ] 원격 Claude Code 운영 시 지켜야 할 보안 규칙을 정리한다.
- [ ] 절전, 네트워크, 세션, 백업, vault 동기화 운영 절차를 만든다.
- [ ] 홈서버 도입 시 운영 체크리스트를 만든다.
- [ ] 하지 말아야 할 위험한 운영 방식을 명시한다.

### 주요 개념

- 최소 노출 원칙
- 권한 최소화
- 작업 전 상태 확인
- 서버 운영성
- 장기간 안전 운영과 단순 접속 성공의 차이

### 실습 과제

- 보안 체크리스트 작성
- 운영 런북 작성
- 홈서버 운영 체크리스트 작성

### 산출물

```text
05-Operations-Security/
  README.md
  guides/security-checklist.md
  guides/remote-work-runbook.md
  guides/home-server-operations.md
  troubleshooting/recovery-playbook.md
```

### Definition of Done

- [ ] 보안 체크리스트 작성
- [ ] 원격 작업 운영 런북 작성
- [ ] 맥미니/맥 스튜디오 서버 운영 체크리스트 작성
- [ ] 금지할 운영 방식 명시
- [ ] 세션 끊김/절전/백업 문제 복구 절차 작성
- [ ] README.md와 WorkLog 작성

## M6 - 최종 패키징과 Remotion AI 영상화 후보 정리

**난이도**: 2  
**예상 시간**: 1h  
**산출물 폴더**: `06-Publishing-Video-Plan/`  
**상태**: 완료

### 학습 목표

- [ ] 전체 산출물을 학습 순서대로 정리한다.
- [ ] 최종 추천 구조와 후속 개선 과제를 명시한다.
- [ ] Remotion AI 영상화에 적합한 스토리라인을 만든다.
- [ ] 영상 제작으로 넘어갈지 판단하는 기준을 만든다.

### 주요 개념

- 교과서 품질 산출물
- 의사결정 기록
- 영상화 가능성
- 후속 Topic 분리
- 공개용 가이드 전 보안 검토

### 실습 과제

- 최종 학습 패키지 정리
- Remotion AI 영상 기획 후보 작성

### 산출물

```text
06-Publishing-Video-Plan/
  README.md
  summary/final-recommendation.md
  summary/next-steps.md
  video/remotion-ai-video-brief.md
```

### Definition of Done

- [x] 전체 모듈 산출물 링크 정리
- [x] 최종 추천 구조 작성
- [x] 후속 개선 과제 작성
- [x] Remotion AI 영상 기획 후보 작성
- [x] 영상 제작 전 확인 조건 작성
- [x] Topic Retrospective 준비

## WorkLog 작성 가이드

각 학습 세션마다 `vl_worklog/YYYYMMDD_MX_Claude-Code-Mobile-Remote-Execution.md` 형식으로 WorkLog를 작성한다.

필수 섹션:
1. 오늘의 학습 목표
2. 진행 내용
3. 문제 해결 로그
4. DoD 체크리스트
5. Daily Retrospective
6. 참조 및 산출물

각 모듈 시작 전에는 `vl_prompts/daily_learning_prompt.md`를 읽고, 오늘의 학습 계획을 먼저 제시한 뒤 사용자 승인을 받아야 한다.

## Retrospective 가이드

### Daily Retrospective

각 세션 종료 시 WorkLog에 작성한다.

- What went well
- What could be improved
- Insights
- Tomorrow's focus

### Module Retrospective

모듈 완료 시 15-20분 동안 작성한다.

- 학습 목표 달성도
- 실제 소요 시간과 계획 비교
- 핵심 인사이트
- 발생한 문제와 해결
- 다음 모듈 준비 사항

### Topic Retrospective

전체 Topic 완료 시 30-60분 동안 작성한다.

- 전체 학습 목표 달성도
- 최종 추천 구조
- 실무 적용 계획
- 보안/운영 리스크
- Remotion AI 영상화 여부
- VibeLearn AI 방법론 개선점

## 학습 진행 상황 추적

| 모듈 | 시작일 | 종료일 | 상태 | DoD 달성률 | 비고 |
|---|---|---|---|---:|---|
| M1 | 2026-08-23 | 2026-08-23 | done | 100% | M1 WorkLog complete |
| M2 | 2026-08-23 | 2026-08-23 | done | 100% | M2 WorkLog complete |
| M3 | 2026-08-23 | 2026-08-23 | done | 100% | M3 WorkLog complete |
| M4 | 2026-08-23 | 2026-08-23 | done | 100% | iPhone Termius + Tailscale + OpenSSH + Claude Code 실행 검증 완료 |
| M5 | 2026-08-24 | 2026-08-24 | done | 100% | 보안/운영/백업 런북 작성 완료 |
| M6 | 2026-08-24 | 2026-08-24 | done | 100% | 최종 추천 구조 + 후속 과제 + Remotion AI 영상 브리프 작성 완료 |

## 성공 기준

- [x] 6개 모듈의 DoD 100% 달성
- [x] 모바일 조작과 로컬 실행 구조 설명 문서 완성
- [x] 기술 구조 비교표와 홈서버 도입 판단표 완성
- [x] 현재 Windows 노트북 기준 1차 원격 실행 실험 완료
- [x] 보안/운영/백업 런북 완성
- [x] Remotion AI 영상화 후보 문서 완성
- [x] Topic Retrospective 작성

## 진행 규칙

- 각 모듈 시작 전 Daily Learning 계획을 먼저 제시하고 사용자 승인을 받는다.
- 외부 설치, 계정 연결, 원격 접속 설정 변경, 보안 설정 변경은 별도 승인 후 진행한다.
- 조사 단계에서 최신 정보가 필요한 공식 문서는 해당 모듈 실행 시 확인한다.
- 실험은 작은 성공 기준부터 시작하고, vault 변경 전 항상 작업 범위를 확인한다.

**생성자**: Codex with VibeLearn AI  
**Roadmap 버전**: 1.1  
**방법론 버전**: VibeLearn AI 2.0



