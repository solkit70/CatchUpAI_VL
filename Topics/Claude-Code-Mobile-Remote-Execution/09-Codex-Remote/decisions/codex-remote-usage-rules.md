# Codex Remote 운용 규칙

**상태**: 2026-08-30 실측 기준 부분 확정. iPad Remote 연결, 읽기, 파일 쓰기, 한글 입력은 성공. iPad 푸시 알림과 잠자기/복귀는 미검증/미완료.

## 기본 방침

**Codex Remote를 Claude Code Remote Control의 대체재로 보지 않는다.** 둘은 각자의 AI를 담당한다. 어떤 AI로 작업하느냐가 경로를 정한다.

| 작업 대상 | 경로 |
|---|---|
| Claude Code | Claude Code Remote Control |
| Codex | **Codex Remote** |
| Gemini 등 그 외 | SSH |
| AI가 아닌 셸 작업 | SSH |

## 오늘 기준으로 확정한 규칙

1. **Codex 작업은 iPad Remote로 가능하다.** 새 ChatGPT Desktop/Codex 앱에서 `Connections > Control this PC`를 켜고 iPad를 연결하면, iPad에서 Windows PC의 Codex 프로젝트를 조작할 수 있다.
2. **방송 중에는 읽기, 작은 파일 쓰기, 짧은 문서 수정까지만 허용한다.** 화면 포커스, 계정 정보, 알림 노출 가능성이 있으므로 방송 중에는 작업 범위를 좁힌다.
3. **대량 수정, `git commit`, `git push`, 설치, 권한 변경, 장시간 작업은 방송 중 하지 않는다.** 실패하거나 승인 창이 떠도 방송 흐름에 영향을 줄 수 있다.
4. **Computer Use는 기본적으로 사용하지 않는다.** 화면 조작 권한이 크고 Windows에서는 잠금 해제 + 포그라운드 요구가 있어 이 vault 작업에는 기본 경로로 부적합하다.
5. **SSH host 등록은 별도 승인 전까지 하지 않는다.** M1~M7의 Tailscale + OpenSSH 구조를 재활용할 수 있지만, SSH 키, 계정 권한, 보안 체크리스트를 다시 건드린다.
6. **Claude 작업은 Claude Remote Control, Codex 작업은 Codex Remote, 범용 shell/Gemini는 SSH로 분리한다.** 기능 이름이 비슷해도 실행 주체와 보안 경계가 다르다.
7. **같은 vault에서 Claude Remote와 Codex Remote를 동시에 켜더라도 같은 파일을 동시에 수정하지 않는다.** 원격 화면에서는 상대 작업 상태가 덜 보이므로 M7의 멀티 CLI 규칙을 더 보수적으로 적용한다.
8. **iPad 푸시 알림은 운영 근거로 믿지 않는다.** 테스트 결과 Windows 노트북 알림은 수신됐지만 iPad 알림은 오지 않았다. 장시간 작업은 앱 화면이나 노트북에서 직접 확인한다.
9. **잠자기/복귀는 미검증이므로 장시간 원격 작업 전 Windows가 깨어 있는지 확인한다.** 방송 중에는 Sleep 테스트를 하지 않는다.

## 실측으로 확인된 항목

| 항목 | 결과 | 비고 |
|---|---|---|
| 새 ChatGPT Desktop/Codex 앱 실행 | 성공 | `Codex view` 표시 확인 |
| `Connections > Control this PC` | 성공 | `Allow connections` On |
| iPad 연결 | 성공 | `iOS 26.6 iPad`, Last connected 확인 |
| 프로젝트 접근 | 성공 | `Changsoo_Vault`와 테스트 프로젝트 표시 |
| 현재 위치 구조 읽기 | 성공 | iPad에서 vault 구조 설명 성공 |
| 파일 쓰기 | 성공 | `codex-remote-test-20260830.txt` 생성 확인 |
| 한글 입력 | 성공 | `안녕하세요` 정상 저장, 자모 분리 없음 |
| Windows 알림 | 성공 | 노트북 알림 수신 |
| iPad 푸시 알림 | 미수신 | iPadOS 알림 권한 별도 점검 필요 |
| 잠자기/복귀 | 미검증 | 방송 중이라 보류 |

## 아직 최종 확정하지 않는 항목

아래는 실사용 전에는 판단할 수 없거나 추가 검증이 필요하다.

- [ ] Sleep 후 자동 복구 여부
- [ ] iPad 푸시 알림을 운영에 믿고 써도 되는지
- [ ] 장시간 작업 안정성
- [ ] 여러 Codex 프로젝트를 동시에 열 때의 충돌 방지 방식
- [ ] Handoff를 실제로 쓸 시나리오가 있는가

## 민감 작업 규칙

M8에서 정한 규칙을 그대로 적용한다. `Changsoo_Vault`의 아래 자료를 다룰 때는 원격 경로를 쓰지 않는다.

- `newsletters/Builders Lounge 메일링 리스트.md` — 이메일 32건
- 주택 워런티 기록 — 주소, 계약 정보
- 가족 의료 일정
- 세무 자료

**Codex Remote는 Claude Code보다 한 단계 더 보수적으로 본다.** 저장 범위가 문서에 명확히 드러나지 않는 부분이 있고, iPad 푸시 알림도 아직 안정 운영 근거로 확인되지 않았다. 알고 쓰는 것과 모르고 쓰는 것의 차이다.

## 영상화 포인트

이번 세션의 핵심 메시지는 "되는 기능을 찾는 과정"보다 "비슷해 보이는 경로를 구분하는 과정"이다. 공개 영상에서는 `ChatGPT Classic`, 새 ChatGPT Desktop/Codex 앱, `Codex CLI` 인증, `Codex Remote host` 등록을 분리해서 설명한다.

| 혼동 지점 | 영상에서 줄 결론 |
|---|---|
| Microsoft Store의 `ChatGPT Classic` | 공식 앱이어도 Codex Remote 메뉴가 없을 수 있다 |
| `.appinstaller` 오류 | Store 설치 성공과 별도 appinstaller 실패는 다른 문제다 |
| `Security and login > Codex CLI` | CLI 인증이지 Remote host 등록이 아니다 |
| `Connections > Control this PC` | iPad Remote 연결의 실제 성공 지점이다 |
| iPad에서 vault 구조 읽기/쓰기 | 모바일은 조작 화면이고 Windows PC가 실행/파일 접근 위치다 |
| iPad 푸시 미수신 | 장시간 작업은 모바일 알림만 믿지 않는다 |

## 참조

- 세팅 절차서: [../lab/setup-procedure.md](../lab/setup-procedure.md)
- 3자 비교: [../comparisons/three-way-remote-comparison.md](../comparisons/three-way-remote-comparison.md)
- M8 선택 기준: [../../08-Native-Remote-Control/decisions/which-path-when.md](../../08-Native-Remote-Control/decisions/which-path-when.md)
- M7 멀티 CLI 규칙: [../../07-Multi-Agent-CLI-Setup/guides/multi-cli-session-rules.md](../../07-Multi-Agent-CLI-Setup/guides/multi-cli-session-rules.md)
- 오늘 WorkLog: [../../vl_worklog/20260830_M9_Claude-Code-Mobile-Remote-Execution.md](../../vl_worklog/20260830_M9_Claude-Code-Mobile-Remote-Execution.md)
