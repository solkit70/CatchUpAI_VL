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
- [x] iPad Termius에서 Claude Code, Codex, Gemini를 각각 실행 가능한 모바일 AI CLI 작업 환경으로 검증한다.

## 전체 로드맵 구조

| 모듈 | 모듈명 | 난이도 | 예상 시간 | 산출물 폴더 | 상태 |
|---|---|---:|---:|---|---|
| M1 | 실행 구조 이해와 첫 모델링 | 1 | 1.5h | `01-Execution-Model/` | done |
| M2 | 기술 구조 비교와 홈서버 옵션 평가 | 2 | 2h | `02-Architecture-Comparison/` | done |
| M3 | 현재 Windows 노트북 환경 점검 | 2 | 1.5h | 03-Environment-Audit/ | done |
| M4 | 모바일 원격 실행 1차 실험 설계 및 수행 | 3 | 2.5h | `04-Remote-Execution-Lab/` | done |
| M5 | 보안, 운영, 백업 가이드 정리 | 2 | 1.5h | `05-Operations-Security/` | done |
| M6 | 최종 패키징과 Remotion AI 영상화 후보 정리 | 2 | 1h | `06-Publishing-Video-Plan/` | done |
| M7 | iPad Termius에서 Codex/Gemini CLI 세팅 검증 | 1 | 1h | `07-Multi-Agent-CLI-Setup/` | done |
| M8 | 네이티브 Remote Control 검증과 구조 비교 | 2 | 2h | `08-Native-Remote-Control/` | done |
| M9 | Codex Remote 검증과 세팅 | 2 | 2.5h | `09-Codex-Remote/` | **2단계 진행 중 · 10/12 · 오늘 세션 종료** |

**총 예상 시간**: 약 11시간, 20% 버퍼 포함

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

- [x] 전체 산출물을 학습 순서대로 정리한다.
- [x] 최종 추천 구조와 후속 개선 과제를 명시한다.
- [x] Remotion AI 영상화에 적합한 스토리라인을 만든다.
- [x] 영상 제작으로 넘어갈지 판단하는 기준을 만든다.

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


## M7 - iPad Termius에서 Codex/Gemini CLI 세팅 검증

**목표 기간**: 1일  
**예상 시간**: 1h  
**상태**: 완료

### 학습 목표

- [x] iPad Termius의 새 SSH 탭에서 Codex CLI 설치/인식 여부를 확인한다.
- [x] iPad Termius의 새 SSH 탭에서 Gemini CLI 설치/인식 여부를 확인한다.
- [x] Claude Code, Codex, Gemini를 동시에 열 때의 세션/작업 디렉터리/파일 충돌 위험을 정리한다.
- [x] Codex/Gemini 미설치 또는 PATH 미등록 상태에서 다음 조치 기준을 만든다.

### 핵심 질문

- iPad Termius는 하나의 Windows SSH 서버에 여러 탭을 동시에 열 수 있는가?
- Codex와 Gemini는 `catchupai` 사용자 계정에서 바로 실행 가능한가, 아니면 별도 설치/PATH 설정이 필요한가?
- 여러 AI CLI를 동시에 사용할 때 같은 repository에서 안전하게 작업하려면 어떤 규칙이 필요한가?
- 이 검증이 끝나야 Topic을 완료 처리하고 Remotion 영상 제작으로 넘어갈 수 있는가?

### 학습 내용

1. iPad Termius에서 새 탭 또는 새 연결을 열어 기존 `Catchup AI Windows` host에 접속
2. `where codex`, `codex --version`, `where gemini`, `gemini --version` 실행 결과 기록
3. 미설치/미인식 시 설치 후보와 보류 기준 정리
4. Claude Code가 작업 중일 때 Codex/Gemini를 병행 실행하는 운영 규칙 작성
5. 영상화 관점에서 "Claude만 되는 상태"와 "Codex/Gemini까지 확장한 상태"의 차이 정리

### 실습

- iPad Termius 새 탭에서 `cd C:\AI_study\2026\Changsoo_Vault\Ingest\CatchUpAI_VL`
- `claude --version`, `codex --version`, `gemini --version` 비교
- 각 CLI가 실행되는 계정과 현재 작업 디렉터리 확인: `whoami`, `hostname`, `cd`
- 동시에 열려 있는 탭에서 같은 파일을 수정하지 않는 운영 규칙 확인

### 산출물

- `07-Multi-Agent-CLI-Setup/README.md`
- `07-Multi-Agent-CLI-Setup/checks/ipad-termius-cli-check.md`
- `07-Multi-Agent-CLI-Setup/guides/multi-cli-session-rules.md`
- `vl_worklog/YYYYMMDD_M7_Claude-Code-Mobile-Remote-Execution.md`

### DoD

- [x] iPad Termius에서 Codex 실행 가능 여부 기록
- [x] iPad Termius에서 Gemini 실행 가능 여부 기록
- [x] 미설치/미인식 시 원인과 다음 조치 기록
- [x] Claude/Codex/Gemini 병행 사용 규칙 작성
- [x] Topic 완료 조건을 M7 검증 이후로 갱신
- [x] WorkLog 작성

### 리뷰 포인트

- Codex/Gemini 설치를 지금 진행할지, 문서화만 하고 별도 Topic으로 분리할지 판단
- 세 CLI를 동시에 실행할 때 repository 변경 충돌을 피하는 규칙이 충분한지 확인
- Remotion 영상에 "다른 AI CLI도 같은 구조로 붙일 수 있다"는 확장 포인트를 넣을지 결정

### 출력 폴더

```text
07-Multi-Agent-CLI-Setup/
  README.md
  checks/ipad-termius-cli-check.md
  guides/multi-cli-session-rules.md
```
## M8 - 네이티브 Remote Control 검증과 구조 비교

**목표 기간**: 1일
**예상 시간**: 2h
**상태**: 완료
**성격**: Topic Retrospective 이후 추가된 유지보수 모듈 (CVL)

### 배경

2026-08-28, 사용자가 iPad Claude 앱의 `Code` 탭에서 로컬 세션이 `Connected` 상태로 떠 있는 것을 발견했다. Claude Code에는 SSH 없이 모바일에서 로컬 세션을 조종하는 **네이티브 Remote Control** 기능이 있었다. M1~M7 전체와 Vault 어디에도 이 기능에 대한 기록이 없었다. 원래 학습하려던 것이 이 기능이었고, SSH 경로로 우회해 7개 모듈을 완주한 뒤에야 직행 경로를 발견한 셈이다.

### 학습 목표

- [x] Remote Control의 연결 구조를 설명하고 SSH 방식과 대조할 수 있다.
- [x] 활성화·연결 상태를 이 환경에서 실측하고 기록한다.
- [x] 두 방식의 경계를 판별한다 — 무엇이 Remote Control로 가능하고 무엇이 SSH를 필요로 하는가.
- [x] 상황별로 어느 방식을 쓸지 결정 기준을 만든다.

### 핵심 질문

- Remote Control은 어디서 실행되고 무엇이 어디에 저장되는가?
- M1의 "모바일은 조작 콘솔, 실행은 로컬" 모델이 여전히 유효한가?
- SSH 구조가 담당하던 것 중 무엇이 대체되고 무엇이 남는가?
- 이 Vault의 개인정보를 다룰 때 어떤 기준이 필요한가?

### 학습 내용

1. 공식 문서(`code.claude.com/docs/en/remote-control`)로 연결 구조·요건·제약 확인
2. `ListAgents`, `claude --version`, 확장 버전, 환경변수, 설정 파일로 현재 상태 실측
3. 경계 테스트 — 실행 위치, MCP 유지, 인바운드 포트, 계정 경계, 터미널 시작 가능 여부, 트랜스크립트 저장 위치
4. M2 구조 비교표와 같은 형식으로 SSH 방식 대비 비교표 작성
5. 민감 작업 규칙을 포함한 결정 흐름 작성

### 실습

- `ListAgents`로 같은 계정의 Remote Control 세션 조회
- `claude remote-control --help` 실행 → 자격 검사 실패 원인 특정
- 인증 관련 환경변수 9종 점검
- `~/.claude.json`, `settings.json` 3종에서 Remote Control 관련 키 확인
- iPad 스크린샷과 `ListAgents` 출력 교차 검증

### 산출물

- `08-Native-Remote-Control/README.md`
- `08-Native-Remote-Control/concepts/native-remote-control-model.md`
- `08-Native-Remote-Control/lab/remote-control-verification.md`
- `08-Native-Remote-Control/comparisons/ssh-vs-native-remote-control.md`
- `08-Native-Remote-Control/decisions/which-path-when.md`
- `vl_worklog/20260828_M8_Claude-Code-Mobile-Remote-Execution.md`

### DoD

- [x] Remote Control 연결 구조 문서화 (Mermaid 다이어그램 포함)
- [x] 활성화·연결 절차 실측 기록
- [x] 경계 테스트 6건 이상 수행 및 결과 기록
- [x] SSH 방식과의 비교표 작성
- [x] 상황별 선택 기준 작성
- [x] 로드맵 추적표·성공 기준 갱신
- [x] WorkLog 작성

### 핵심 발견

| 항목 | 내용 |
|---|---|
| 학습 모델 | M1의 "모바일은 조작 콘솔, 실행은 로컬"은 **두 방식 모두에 유효** |
| 대체되지 않는 것 | Codex·Gemini 실행, 임의 셸 작업, 계정 격리, 홈서버, 오프라인 LAN |
| 보안 후퇴 1 | 계정 격리 없음 — `catchupai`가 아니라 `dougg` 세션에 붙는다 |
| 보안 후퇴 2 | 트랜스크립트가 Anthropic 서버에 저장된다 |
| 환경 문제 1 | PATH CLI `2.1.143` vs VS Code 확장 `2.1.250` — 버전 게이트 7건 |
| 환경 문제 2 | `ANTHROPIC_API_KEY` 설정으로 터미널에서 `claude remote-control` 차단 |

### 리뷰 포인트

- 터미널 CLI 업데이트 후 서버 모드(`claude remote-control`) 재검증 필요
- 자동 연결(`remoteControlAtStartup`)을 켤지 판단 — 민감 작업 규칙과 함께
- Remotion 영상 브리프를 "두 경로 비교" 구성으로 개정할지 결정

### 출력 폴더

```text
08-Native-Remote-Control/
  README.md
  concepts/native-remote-control-model.md
  lab/remote-control-verification.md
  comparisons/ssh-vs-native-remote-control.md
  decisions/which-path-when.md
```
## M9 - Codex Remote 검증과 세팅

**목표 기간**: 2일 (1단계 / 2단계 분리)
**예상 시간**: 2.5h
**상태**: **1단계 완료** (문서 조사·3자 비교) / **2단계 진행 중** (Desktop 설치·iPad 연결·읽기/쓰기 테스트 완료, 운용 규칙 부분 확정, 남은 iPad 푸시·잠자기 복구 대기)
**성격**: M8에 이은 유지보수 모듈 (CVL)

### 배경

M8에서 Claude Code 네이티브 Remote Control을 정리한 뒤, Codex에도 같은 성격의 원격 기능이 있다는 것을 확인했다. M7에서 Codex CLI를 iPad Termius로 실행하는 것까지 검증했으므로, 이 모듈이 완료되면 **SSH · Claude RC · Codex Remote 3자 비교**가 성립한다.

사용자 요청으로 **문서 조사와 비교를 1단계**, **설치와 세팅을 2단계**로 나눴다.

### 학습 목표

- [x] Codex Remote의 연결 구조를 설명하고 Claude Code Remote Control과 대조할 수 있다.
- [x] Handoff · SSH 호스트 등록 · Computer Use가 무엇인지 설명할 수 있다.
- [x] 세 경로의 비교표를 만들고 각각 언제 쓸지 판단할 수 있다.
- [ ] 이 환경에 Codex Remote를 세팅하고 모바일에서 실제로 사용할 수 있다.

### 핵심 질문

- Codex Remote의 호스트는 무엇인가? Codex CLI인가 다른 것인가?
- Claude Code Remote Control에 없는 기능은 무엇인가?
- 데이터 저장 범위는 어떻게 되는가?
- M1~M7에서 만든 SSH 구조가 여기서도 쓰이는가?

### 학습 내용 (1단계)

1. 공식 문서 조사 — `learn.chatgpt.com/docs/remote-connections`, 실무 워크플로우 블로그
2. Claude Code Remote Control과의 구조 대조
3. Handoff · SSH 호스트 등록 · Computer Use 정리
4. 3자 비교표 작성
5. 이 환경의 세팅 요건 점검 및 절차서 준비

### 실습 (2단계, 대기)

- ChatGPT 데스크톱 앱 설치 (`winget` 없음 → 웹 다운로드)
- Settings → Connections → Control this Mac or PC → Set up
- 모바일 QR 페어링
- 경계 테스트 7항목 (실행 위치 · 승인 흐름 · 실행 계정 · 로컬 설정 유지 · 푸시 · 한글 입력 · 잠자기 복구)

### 산출물

- `09-Codex-Remote/README.md`
- `09-Codex-Remote/concepts/codex-remote-model.md`
- `09-Codex-Remote/comparisons/three-way-remote-comparison.md`
- `09-Codex-Remote/lab/setup-procedure.md`
- `09-Codex-Remote/decisions/codex-remote-usage-rules.md`
- `vl_worklog/20260828_M9_Claude-Code-Mobile-Remote-Execution.md`

### DoD

**1단계**

- [x] Codex Remote 연결 구조 문서화 (Mermaid 포함)
- [x] Handoff · SSH 호스트 등록 · Computer Use 정리
- [x] 3자 비교표 작성
- [x] 세팅 요건 점검
- [x] 설치·페어링 절차서 작성 (경계 테스트 7항목 포함)
- [x] 운용 규칙 잠정안 작성
- [x] WorkLog 작성

**2단계**

- [x] ChatGPT 데스크톱 앱 설치
- [x] 호스트 등록 + 모바일 QR 페어링
- [>] 경계 테스트 7항목 수행 (읽기/쓰기 테스트 완료, 남은 장시간 테스트 대기)
- [ ] 절차서를 실기록으로 전환
- [x] 운용 규칙 부분 확정

### 핵심 발견 (1단계)

| 항목 | 내용 |
|---|---|
| 호스트 주체 | **ChatGPT 데스크톱 앱**. Codex CLI로는 설정 불가 |
| 고유 기능 | Handoff(대화+Git 상태 이전) · SSH 호스트 등록 · Computer Use |
| M1~M7과의 연결 | **SSH 호스트 등록으로 기존 구조를 재활용 가능** — 세 경로가 배타적이지 않다 |
| 데이터 취급 | 공식 문서에 저장 범위 **명시 없음** (Claude Code는 명시) |
| 공통 보안 후퇴 | Claude RC와 마찬가지로 **계정 격리 없음** — 일상 계정 세션에 붙는다 |
| 환경 | ChatGPT 데스크톱 앱 설치됨 (`OpenAI.ChatGPT-Desktop 1.2026.190.0`), `winget` 없음, 플랜 Plus 확인 |

### 리뷰 포인트

- 1차 세팅에서 **Computer Use는 제외** — Windows에서 잠금 해제 + 포그라운드 필요, 화면 조작 권한 위험
- **SSH 호스트 등록도 1차에서 제외** — M5 보안 체크리스트를 다시 건드리므로 별도 승인
- 세팅 전 **ChatGPT 계정 데이터 관리 설정 확인** 필수
- Claude RC와 Codex Remote를 동시에 켜 둘 경우 M7의 "같은 파일 동시 수정 금지" 규칙을 어떻게 적용할지

### 출력 폴더

```text
09-Codex-Remote/
  README.md
  concepts/codex-remote-model.md
  comparisons/three-way-remote-comparison.md
  lab/setup-procedure.md
  decisions/codex-remote-usage-rules.md
```
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
| M7 | 2026-08-24 | 2026-08-24 | done | 100% | iPad Termius에서 Codex/Gemini CLI 실행 가능 여부 검증 완료 |
| M8 | 2026-08-28 | 2026-08-28 | done | 100% | 네이티브 Remote Control 검증. SSH 방식과 비교·선택 기준 작성 |
| M9 | 2026-08-28 | 진행 중 | 오늘 세션 종료 | 10/12 | 읽기/쓰기/한글 입력/운용 규칙 부분 확정 완료. iPad 푸시·잠자기 복구 대기 |

## 성공 기준

- [>] 9개 모듈 — M1~M8 DoD 100%, M9는 1단계 완료 / 2단계 진행 중
- [x] 모바일 조작과 로컬 실행 구조 설명 문서 완성
- [x] 기술 구조 비교표와 홈서버 도입 판단표 완성
- [x] 현재 Windows 노트북 기준 1차 원격 실행 실험 완료
- [x] 보안/운영/백업 런북 완성
- [x] Remotion AI 영상화 후보 문서 완성
- [x] Topic Retrospective 작성
- [x] 네이티브 Remote Control과 SSH 구조 비교·선택 기준 완성 (M8, 2026-08-28 추가)
- [>] Codex Remote 조사·3자 비교 완성 (M9 1단계, 2026-08-28) — ChatGPT Desktop 설치, iPad 연결, 읽기/쓰기 테스트 완료. 운용 규칙 부분 확정, 남은 iPad 푸시·잠자기 복구 대기

## 진행 규칙

- 각 모듈 시작 전 Daily Learning 계획을 먼저 제시하고 사용자 승인을 받는다.
- 외부 설치, 계정 연결, 원격 접속 설정 변경, 보안 설정 변경은 별도 승인 후 진행한다.
- 조사 단계에서 최신 정보가 필요한 공식 문서는 해당 모듈 실행 시 확인한다.
- 실험은 작은 성공 기준부터 시작하고, vault 변경 전 항상 작업 범위를 확인한다.

**생성자**: Codex with VibeLearn AI  
**Roadmap 버전**: 1.3 (2026-08-28 M9 추가)  
**방법론 버전**: VibeLearn AI 2.0













