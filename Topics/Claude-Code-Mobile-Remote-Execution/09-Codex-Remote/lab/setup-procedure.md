# Codex Remote 세팅 절차서 (실행 대기)

**상태**: 문서 조사 완료, **설치·세팅 미실행** (2026-08-28 사용자 요청으로 분리)
**대상 계정**: `douggy.park@yahoo.com` · **ChatGPT Plus**
**호스트**: Windows 11, `dougg` 계정

이 문서는 실행 전 절차서다. 세팅을 진행하면 각 단계의 실제 결과를 이 문서에 채워 실기록으로 전환한다.

## 사전 점검 결과 (2026-08-28)

| 항목 | 상태 |
|---|---|
| Codex CLI | `codex-cli 0.149.1` 설치됨 — **다만 이 기능과 무관** |
| ChatGPT 데스크톱 앱 | ❌ **미설치** |
| `winget` | ❌ 사용 불가 (명령 없음) |
| ChatGPT 플랜 | Plus ✅ |
| ChatGPT 모바일 앱 | 미확인 — iPad/iPhone에 설치 여부 확인 필요 |

## Step 0 — 실행 전 확인

- [ ] ChatGPT 모바일 앱이 iPhone 또는 iPad에 설치되어 있고 최신 버전인가
- [ ] 모바일 앱에서 `douggy.park@yahoo.com` 으로 로그인되어 있는가
- [ ] 모바일 앱에 **Remote** 섹션이 보이는가 (안 보이면 앱 업데이트)
- [ ] ChatGPT 계정의 **데이터 관리 설정**을 확인했는가 → 문서에 저장 범위 명시가 없어 별도 확인이 필요하다

## Step 1 — ChatGPT 데스크톱 앱 설치

`winget`이 없으므로 웹에서 받는다.

1. https://chatgpt.com/download 에서 Windows 버전 다운로드
2. 설치 실행
3. `douggy.park@yahoo.com` 으로 로그인
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
| 1 | 실행 위치가 로컬인가 | 모바일에서 파일 생성 → 로컬에서 존재 확인 | |
| 2 | 승인 흐름 | 명령·파일 변경·네트워크 승인이 모바일에 뜨는가 | |
| 3 | 실행 계정 | `whoami` 결과가 `dougg`인지 | |
| 4 | 로컬 MCP·설정 유지 | 프로젝트 설정이 그대로 적용되는가 | |
| 5 | 푸시 알림 | 긴 작업 완료 시 알림이 오는가 | |
| 6 | 한글 입력 | 모바일에서 한글 프롬프트 정상 입력되는가 | |
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
