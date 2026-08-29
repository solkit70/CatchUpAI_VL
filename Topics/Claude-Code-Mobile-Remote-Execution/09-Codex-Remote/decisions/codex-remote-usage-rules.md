# Codex Remote 운용 규칙

**상태**: 문서 조사 기준 잠정안. **세팅·실사용 후 확정한다.**

## 기본 방침

**Codex Remote를 Claude Code Remote Control의 대체재로 보지 않는다.** 둘은 각자의 AI를 담당한다. 어떤 AI로 작업하느냐가 경로를 정한다.

| 작업 대상 | 경로 |
|---|---|
| Claude Code | Claude Code Remote Control |
| Codex | **Codex Remote** |
| Gemini 등 그 외 | SSH |
| AI가 아닌 셸 작업 | SSH |

## 세팅 시 지킬 것

**1. Computer Use는 켜지 않는다.** 브라우저·데스크톱을 통째로 조작하는 기능이고, Windows에서는 잠금 해제 + 포그라운드가 필요하다. 이 Vault에는 개인정보가 있어 화면 조작 권한을 원격에 열어 둘 이유가 없다. 필요해지면 그때 별도로 판단한다.

**2. 데이터 취급을 먼저 확인한다.** 공식 문서에 저장 범위 서술이 없다. ChatGPT 계정의 데이터 관리 설정을 확인하고, 확인 결과를 `lab/setup-procedure.md` Step 0에 기록한 뒤 진행한다.

**3. SSH 호스트 등록은 나중에.** M1~M7 구조를 재활용할 수 있어 흥미롭지만, M5 보안 체크리스트 항목을 다시 건드린다. 1차 세팅은 로컬 호스트만으로 끝내고, SSH 연동은 별도 승인 후 진행한다.

**4. 승인은 가장 좁은 권한으로.** 공식 문서의 권고이기도 하다. 낯선 명령은 1회 승인, 신뢰하는 작업만 대화 범위 승인. 이 Vault에서 `bypassPermissions` 성격의 설정은 쓰지 않는다.

## 민감 작업 규칙

M8에서 정한 규칙을 그대로 적용한다. `Changsoo_Vault`의 아래 자료를 다룰 때는 원격 경로를 쓰지 않는다.

- `newsletters/Builders Lounge 메일링 리스트.md` — 이메일 32건
- 주택 워런티 기록 — 주소, 계약 정보
- 가족 의료 일정
- 세무 자료

**Codex Remote는 Claude Code보다 한 단계 더 보수적으로 본다.** 저장 범위가 문서에 명시되지 않았기 때문이다. 알고 쓰는 것과 모르고 쓰는 것의 차이다.

## 세팅 후 확정할 항목

아래는 실사용 전에는 판단할 수 없다. 세팅 후 채운다.

- [ ] 호스트 잠자기 정책 — 노트북을 계속 깨워 둘 것인가
- [ ] 푸시 알림 설정 범위
- [ ] Handoff를 실제로 쓸 시나리오가 있는가 (호스트가 하나뿐이면 무의미)
- [ ] Claude Code Remote Control과 동시에 켜 둘 것인가, 필요할 때만 켤 것인가
- [ ] M7의 멀티 CLI 규칙(같은 파일 동시 수정 금지)을 원격 환경에도 어떻게 적용할 것인가

마지막 항목이 특히 중요하다. **Claude Code Remote Control과 Codex Remote를 동시에 켜 두면 서로 다른 기기에서 같은 저장소를 건드릴 수 있다.** M7에서 정한 "동시에 여러 CLI를 열 수는 있지만 같은 파일을 동시에 수정하지 않는다"는 규칙이 원격에서는 지키기 더 어렵다 — 상대가 뭘 하는지 화면에 안 보이기 때문이다.

## 참조

- 세팅 절차서: [../lab/setup-procedure.md](../lab/setup-procedure.md)
- 3자 비교: [../comparisons/three-way-remote-comparison.md](../comparisons/three-way-remote-comparison.md)
- M8 선택 기준: [../../08-Native-Remote-Control/decisions/which-path-when.md](../../08-Native-Remote-Control/decisions/which-path-when.md)
- M7 멀티 CLI 규칙: [../../07-Multi-Agent-CLI-Setup/guides/multi-cli-session-rules.md](../../07-Multi-Agent-CLI-Setup/guides/multi-cli-session-rules.md)
