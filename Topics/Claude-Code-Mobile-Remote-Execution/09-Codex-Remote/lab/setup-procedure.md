# Codex Remote 세팅 절차서 (실행 대기)

**상태**: 문서 조사 완료, **설치·세팅 미실행** (2026-08-28 사용자 요청으로 분리)
**대상 계정**: 개인 ChatGPT 계정 · **Plus**
**호스트**: Windows 11, `dougg` 계정

이 문서는 실행 전 절차서다. 세팅을 진행하면 각 단계의 실제 결과를 이 문서에 채워 실기록으로 전환한다.

## 사전 점검 결과 (2026-08-28)

| 항목 | 상태 |
|---|---|
| Codex CLI | `codex-cli 0.149.1` 설치됨 — **다만 이 기능과 무관** |
| ChatGPT 데스크톱 앱 | ✅ 설치됨: `OpenAI.ChatGPT-Desktop 1.2026.190.0` (2026-08-30) |
| `winget` | ❌ 사용 불가 (명령 없음) |
| ChatGPT 플랜 | Plus ✅ |
| ChatGPT 모바일 앱 | 미확인 — iPad/iPhone에 설치 여부 확인 필요 |

## Step 0 — 실행 전 확인

- [ ] ChatGPT 모바일 앱이 iPhone 또는 iPad에 설치되어 있고 최신 버전인가
- [ ] 모바일 앱에서 **데스크톱과 같은 계정**으로 로그인되어 있는가
- [ ] 모바일 앱에 **Remote** 섹션이 보이는가 (안 보이면 앱 업데이트)
- [ ] ChatGPT 계정의 **데이터 관리 설정**을 확인했는가 → 문서에 저장 범위 명시가 없어 별도 확인이 필요하다

## Step 1 — ChatGPT 데스크톱 앱 설치

**실행 결과 (2026-08-30)**: 공식 Microsoft 설치 링크의 `.appinstaller`를 실행해 설치 완료. 확인된 패키지: `OpenAI.ChatGPT-Desktop 1.2026.190.0`. 재부팅, 로그아웃, 호스트 등록, QR 페어링은 수행하지 않음.


`winget`이 없으므로 웹에서 받는다.

1. https://chatgpt.com/download 에서 Windows 버전 다운로드
2. 설치 실행
3. 데스크톱과 **같은 계정**으로 로그인
4. 버전 확인 — **최신이어야 Remote 기능이 보인다**

> 설치 파일 실행은 사용자가 직접 수행한다.

## Step 2 — 호스트 등록

1. 데스크톱 앱 → **Settings → Connections**
2. **Control this Mac or PC** → **Set up**
3. 원격 접근 승인, 인증 요청 처리

기록할 것:

| 항목 | 값 |
|---|---|
| 앱 버전 | |
| 호스트 표시 이름 | |
| 인증 방식 (MFA / 패스키 / SSO) | |

## Step 3 — 모바일 페어링

1. 호스트 화면의 **QR 코드** 표시
2. ChatGPT 모바일 앱 카메라로 스캔
3. 계정·워크스페이스 일치 확인
4. MFA · 패스키 인증
5. 모바일 앱 **Remote** 섹션에 호스트가 나타나는지 확인

## Step 4 — 실사용 검증

M8에서 Claude Code에 적용한 것과 같은 경계 테스트를 수행한다.

| # | 항목 | 확인 방법 | 결과 |
|---|---|---|---|
| 1 | 실행 위치가 로컬인가 | 모바일에서 파일 생성 후 로컬에서 존재 확인 | 성공: `04-Remote-Execution-Lab/lab/codex-remote-test-20260830.txt` 생성 및 내용 확인 |
| 2 | 승인 흐름 | 명령·파일 변경·네트워크 승인이 모바일에 뜨는가 | 부분 성공: iPad에서 파일 쓰기 작업 완료. 승인 UI 세부 캡처는 대기 |
| 3 | 실행 계정 | `whoami` 결과가 `dougg`인지 | |
| 4 | 로컬 MCP·설정 유지 | 프로젝트 설정이 그대로 적용되는가 | 부분 성공: 새 프로젝트에서 현재 위치 구조 접근 및 파일 쓰기 확인 |
| 5 | 푸시 알림 | 긴 작업 완료 시 알림이 오는가 | 부분 성공: Windows 노트북 알림 수신. iPad 푸시는 미수신 |
| 6 | 한글 입력 | 모바일에서 한글 프롬프트 정상 입력되는가 | 성공: 테스트 파일 2번째 줄에 `안녕하세요` 정상 기록. 자모 분리 없음 |
| 7 | 호스트 잠자기 | 노트북 잠자기 → 연결 끊김 → 복귀 시 재연결되는가 | |

## Step 5 — Handoff 확인 (선택)

Git 저장소가 있는 프로젝트에서만 가능하다. 대상 호스트에 **같은 저장소의 저장된 프로젝트**가 있어야 한다.

호스트가 하나뿐이면 이 기능은 시험할 수 없다. 실기기가 둘 이상 생겼을 때 진행한다.

## Step 6 — SSH 호스트 등록 (선택, 흥미로운 지점)

M1~M7에서 만든 구조를 재활용하는 부분이다.

1. `~/.ssh/config`에 Tailscale 경유 Windows 호스트 정의
2. `ssh <호스트>` 로 접속 확인
3. 원격 호스트의 PATH에 `codex` 존재 확인 — M7에서 `catchupai` 계정에 설치했다
4. 데스크톱 앱 → **Settings → Connections → SSH** → 호스트와 프로젝트 폴더 등록

> ⚠️ 이 단계는 **M5 보안 체크리스트의 항목들을 다시 건드린다.** SSH 키, 최소 권한 계정, 공개 리스너 없음이 전제다. 공식 문서도 *"Keep the remote host configured with the same security expectations you use for normal SSH access"* 라고 명시한다.

## Step 7 — Computer Use (보류 권장)

브라우저·데스크톱 조작 기능이다. Chrome 확장 설치가 필요하다.

**Windows에서는 잠금 해제 상태 + 포그라운드 실행이 요구된다.** 원격에서 쓰기엔 제약이 크고, 화면을 통째로 조작하는 기능이라 이 Vault의 개인정보 관점에서도 위험이 있다. **1차 세팅에서는 켜지 않는 것을 권한다.**

## 세팅 후 정리할 것

- [ ] 이 문서를 실기록으로 전환 (각 Step의 실제 결과 기입)
- [ ] [../decisions/codex-remote-usage-rules.md](../decisions/codex-remote-usage-rules.md) 의 미정 항목 채우기
- [ ] [../comparisons/three-way-remote-comparison.md](../comparisons/three-way-remote-comparison.md) 의 추정 항목을 실측값으로 교체
- [ ] WorkLog M9 갱신 및 DoD 완료 처리

## 참조

- 공식 문서: https://learn.chatgpt.com/docs/remote-connections
- 구조 설명: [../concepts/codex-remote-model.md](../concepts/codex-remote-model.md)
- M5 보안 체크리스트: [../../05-Operations-Security/guides/security-checklist.md](../../05-Operations-Security/guides/security-checklist.md)

## 방송 중 안전 모드 (2026-08-30)

2026-08-30 세션은 사용자가 라이브 방송 중이므로 설치, 권한 변경, 계정 연결, 재부팅 가능성이 있는 작업을 진행하지 않는다. 오늘은 실행 전 점검표를 정리하고, 방송 후 실제 세팅으로 넘길 항목만 확정한다.

방송 중 하지 않을 작업:

- ChatGPT 데스크톱 앱 설치
- 호스트 등록 또는 QR 페어링
- Computer Use 활성화
- SSH 호스트 등록
- 네트워크, 방화벽, 권한, 시작 프로그램 설정 변경
- 재부팅, 로그아웃, 앱 강제 종료가 필요할 수 있는 작업
- 방송 화면을 가리거나 포커스를 빼앗을 수 있는 테스트

방송 중 허용할 작업:

- 기존 문서와 공식 문서 기준의 절차 재확인
- 모바일 앱 설치 여부, 로그인 계정, Remote 섹션 존재 여부의 수동 확인
- 계정 데이터 관리 설정 위치 확인
- 단, 설정값 변경은 방송 후로 미룬다.

## 설치 실행 기록 (2026-08-30)

사용자 재승인 후 방송 중에도 ChatGPT Desktop 설치만 예외적으로 진행했다. 공식 다운로드 페이지 `https://chatgpt.com/download`와 Microsoft Store 앱 페이지를 열었고, 공식 Microsoft 설치 링크에서 `.appinstaller` 파일을 받아 실행했다.

확인 결과:

| 항목 | 값 |
|---|---|
| 패키지명 | `OpenAI.ChatGPT-Desktop` |
| 버전 | `1.2026.190.0` |
| 상태 | 설치 완료 |
| 재부팅 | 요청/수행 없음 |
| 호스트 등록 | 완료: `Control this PC`에서 `Allow connections` On |
| QR 페어링 | 완료: `iOS 26.6 iPad`, Last connected 1m 확인 |
| Computer Use | 미수행 |
| SSH 호스트 등록 | 미수행 |


## iPad Remote 연결 기록 (2026-08-30)

사용자가 새 ChatGPT Desktop의 Codex view를 실행한 뒤 `Connections > Control this PC`에서 iPad 연결을 완료했다.

| 항목 | 값 |
|---|---|
| 연결 허용 | On |
| 연결 기기 | `iOS 26.6 iPad` |
| 상태 | Last connected 1m 확인 |
| 프로젝트 | `Changsoo_Vault`, `아이패드 작업 가능 여부 확인` 확인 |
| 읽기 테스트 | 성공: iPad에서 현재 위치의 vault 구조를 설명함 |
| 파일 쓰기 테스트 | 성공: `04-Remote-Execution-Lab/lab/codex-remote-test-20260830.txt` 생성 및 한 줄 내용 확인 |
| Computer Use | 미수행 |
| SSH 호스트 등록 | 미수행 |

## 영상화 기록 포인트

이번 세팅 과정은 공개용 영상에서 "정답 경로만 보여 주는 튜토리얼"보다 "실제 혼선을 해결하는 과정"으로 쓰는 편이 교육적 가치가 높다.

| 단계 | 실제 이슈 | 영상에서 설명할 포인트 |
|---|---|---|
| 방송 중 설치 판단 | 설치가 방송을 방해할 수 있음 | 재부팅, 권한 팝업, 화면 노출 위험을 먼저 분리 |
| ChatGPT Classic 설치 | Store 공식 앱이지만 `Connections` 없음 | 공식 앱이어도 Remote 기능 노출 여부는 별도 확인 필요 |
| `.appinstaller` 오류 | 별도 설치 파일이 invalid로 표시 | Store 설치 성공과 appinstaller 실패를 분리 |
| Codex CLI 연결 확인 | `Security and login`에 Codex CLI가 보임 | CLI 인증은 Remote host 등록과 다름 |
| 새 Codex 앱 실행 | `Codex view`와 `Connections` 확인 | 올바른 앱을 판별하는 화면 단서 |
| iPad 연결 | `iOS 26.6 iPad` Last connected 확인 | 모바일 조작, Windows 실행 모델 검증 |
| vault 구조 읽기 | iPad에서 현재 위치 구조 설명 성공 | 읽기 테스트와 쓰기 테스트를 분리 |

## 파일 쓰기 테스트 기록 (2026-08-30)

사용자가 iPad Remote Codex에서 최소 파일 쓰기 테스트를 수행했고 성공했다. 로컬 확인 결과 아래 파일이 생성되어 있었다.

| 항목 | 값 |
|---|---|
| 파일 | `04-Remote-Execution-Lab/lab/codex-remote-test-20260830.txt` |
| 내용 | `Codex Remote iPad write test 2026-08-30.` + `안녕하세요` |
| 결과 | 성공 |
| 범위 | 단일 파일 생성 |
| 남은 검증 | 푸시 알림, 잠자기/복귀 재연결, 장시간 작업 안정성 |

## 한글 입력 테스트 기록 (2026-08-30)

사용자가 iPad Remote Codex에서 기존 테스트 파일에 한글을 추가했다. 로컬 확인 결과 `안녕하세요`가 정상적으로 저장되어 있었고, 자모 분리나 인코딩 깨짐은 없었다.

| 항목 | 값 |
|---|---|
| 파일 | `04-Remote-Execution-Lab/lab/codex-remote-test-20260830.txt` |
| 추가 내용 | `안녕하세요` |
| 결과 | 성공 |
| 관찰 | 자모 분리 없음 |
| 남은 확장 테스트 | 긴 한국어 문장, Markdown 여러 줄 편집 |

## 푸시 알림 테스트 기록 (2026-08-30)

사용자가 Codex Remote 알림 테스트를 수행했고, 알림이 Windows 노트북으로 도착했다고 보고했다.

| 항목 | 값 |
|---|---|
| 테스트 결과 | 부분 성공 |
| 수신 기기 | Windows 노트북 |
| iPad 푸시 | 미수신 |
| 해석 | 작업 완료 알림 체계는 동작하지만, 모바일 백그라운드 푸시는 별도 확인 필요 |
| 다음 확인 | iPadOS 알림 권한, Focus/Do Not Disturb, ChatGPT 앱 알림 설정 확인 |

