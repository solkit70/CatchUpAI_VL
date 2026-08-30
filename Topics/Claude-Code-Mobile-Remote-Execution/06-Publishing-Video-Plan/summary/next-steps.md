# 후속 개선 과제

M5에서 문서화만 하고 실제로 적용하지 않은 항목과, M4~M5에서 관찰만 하고 결론을 유보한 항목을 후속 과제로 정리한다. 모든 항목은 별도 승인 후 진행한다.

## M7 완료 기록

M7에서 iPad Termius 안에서 Claude Code뿐 아니라 Codex CLI와 Gemini CLI도 같은 Windows SSH 구조로 실행 가능한지 확인했다. 다음 단계는 Remotion 영상 제작 전 보안 검토와 사용자 최종 승인이다.

### 재검증 명령 세트

```bat
cd C:\AI_study\2026\Changsoo_Vault\Ingest\CatchUpAI_VL
whoami
hostname
claude --version
where codex
codex --version
where gemini
gemini --version
```

### 재검증 판단 기준

- Codex/Gemini가 이미 설치되어 있고 PATH에서 인식되면 실행 결과와 버전을 기록한다.
- `where codex` 또는 `where gemini`가 실패하면, 즉시 설치하지 말고 설치 방식/계정/PATH 영향 범위를 먼저 정리한 뒤 사용자 승인을 받는다.
- Claude Code, Codex, Gemini를 동시에 열 수 있더라도 같은 파일을 동시에 수정하지 않는 운영 규칙을 먼저 만든다.
- 이 검증은 완료되었으며, 이후에는 Topic Retrospective와 Remotion 영상 제작 Go/No-Go 확인으로 넘어간다.
## M9 추가 완료 기록

2026-08-30에 새 ChatGPT Desktop/Codex 앱 설치, iPad Remote 연결, 현재 vault 구조 읽기 테스트가 성공했다. 이 과정에서 `ChatGPT Classic`과 새 Codex 앱을 구분해야 한다는 점, `Codex CLI` 인증과 `Codex Remote host` 등록이 다르다는 점, `.appinstaller` 오류와 Store 설치 성공을 분리해서 해석해야 한다는 점이 확인됐다.

### 남은 M9 검증

| 과제 | 현재 상태 | 적용 시점 |
|---|---|---|
| 파일 쓰기 최소 테스트 | 완료: `codex-remote-test-20260830.txt` 생성 확인 | 2026-08-30 |
| 승인 흐름 확인 | 부분 완료: iPad에서 파일 쓰기 성공, 승인 UI 세부 기록은 대기 | 다음 경계 테스트 시 |
| 푸시 알림 확인 | 부분 성공: Windows 노트북 알림 수신, iPad 푸시는 미수신 | iPadOS 알림 권한 점검 시 |
| 잠자기/복구 확인 | 대기 | 방송 종료 후 |
| 운용 규칙 부분 확정 | 완료: 방송 중 사용 범위, 금지 작업, 경로 분리 원칙 정리 | 2026-08-30 |

## 우선순위 1 — 보안 강화

| 과제 | 현재 상태 | 왜 필요한가 | 적용 시점 |
|---|---|---|---|
| Windows OpenSSH 로그인용 SSH key 인증 전환 | 문서화만 완료 ([security-checklist.md](../../05-Operations-Security/guides/security-checklist.md)); GitHub push용 SSH key와는 별도 | password 인증은 iPhone/iPad 분실, 화면 노출, 반복 인증 실패 위험이 있음 | 장기 운영 전 |
| Tailscale 계정 MFA 확인 | 미확인 | tailnet 접근 자체를 보호하는 첫 번째 방어선 | 다음 세션 |
| `catchupai` 계정 권한 최소화 점검 | 최초 설정만 완료 | 원격 세션 탈취 시 피해 범위를 제한 | 정기 점검 |

## 우선순위 2 — 운영 확장

| 과제 | 현재 상태 | 왜 필요한가 | 적용 시점 |
|---|---|---|---|
| Tailscale ACL/Grants 적용 | 문서화만 완료 | 현재는 tailnet에 있는 모든 기기가 이론상 SSH에 접근 가능. iPhone/iPad만 허용하도록 제한 필요 | tailnet 장비가 늘어나기 전 |
| Tailscale device approval 검토 | 미적용 | 새 장비가 자동으로 tailnet에 들어오는 것을 방지 | tailnet 공유/확대 전 |
| Windows OpenSSH `AllowUsers catchupai` 적용 | 미적용 | SSH 로그인 가능한 계정을 명시적으로 제한 | SSH 사용자 계정이 늘어나기 전 |

## 우선순위 3 — 클라이언트/입력 경험 개선

| 과제 | 현재 상태 | 왜 필요한가 |
|---|---|---|
| iPad Termius 한글 IME 문제 대안 테스트 | 우회 방법만 문서화 ([ipad-korean-input-lessons.md](../../05-Operations-Security/guides/ipad-korean-input-lessons.md)) | Blink Shell, 웹 기반 SSH client 등 다른 클라이언트에서 재현되는지 확인되지 않음 |
| GitHub push 계정 규율 유지 확인 | `solkit70` SSH alias 고정 완료, 운영 습관은 지속 확인 필요 | `git add .` 금지 원칙이 실제로 매 세션 지켜지는지는 반복 검증이 필요함 |

## 우선순위 4 — 구조 전환 판단 (조건부)

| 과제 | 판단 조건 |
|---|---|
| 맥미니 홈서버 도입 재검토 | 노트북 상시 실행이 생활/업무에 지장을 주거나, 절전/이동으로 인한 접속 끊김이 반복될 때 |
| 맥 스튜디오 홈서버 도입 재검토 | Remotion 렌더링 등 상시 고부하 작업을 서버가 처리해야 할 근거가 생겼을 때 |
| ZeroTier 전환 검토 | Tailscale 계정/정책상 제약이 생겨 사설망 도구를 바꿔야 할 때 |

## 이번 Topic 범위 밖으로 분리할 것

- **Remotion AI 영상 실제 제작**: 이 Topic은 영상화 후보와 스토리라인 정리까지가 범위다. 실제 슬라이드 플랜/오디오/렌더링은 `remotion-video` 스킬을 사용하는 별도 작업으로 진행한다. → [../video/remotion-ai-video-brief.md](../video/remotion-ai-video-brief.md)
- **맥미니/맥 스튜디오 실제 구매 및 셋업**: 별도 Topic으로 분리해서 진행하는 것을 권장한다 (조건 충족 시).









