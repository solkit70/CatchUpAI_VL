# Remotion AI 영상화 후보 브리프

## 왜 이 Topic이 영상화 후보인가

이 Topic은 "성공만 정리한 가이드"가 아니라, 실제로 겪은 실패 3건(iPad Tailscale 미설치, GitHub 계정 두 개, iPad 한글 IME 자모 분리)이 모두 원인 규명과 해결까지 문서화되어 있다. 시청자가 똑같이 겪을 가능성이 높은 문제들이라 교육적 가치가 크고, 이미 각 문서에 "영상화 포인트"와 "장면 구성 후보"가 정리되어 있어 스토리라인 초안 작업 자체가 빠르다.

## 핵심 메시지

```text
모바일에서 Claude Code를 쓴다는 것은 "앱 하나 설치"가 아니라
네트워크 계층(Tailscale) - 터미널 계층(SSH/Termius) - 실행 계층(Claude Code) -
결과 확인 계층(Git/GitHub)을 각각 이해하고 검증하는 일입니다.
```

## 대상 시청자

- Claude Code를 이미 로컬에서 쓰고 있고, 외출 중에도 쓰고 싶은 개발자/파워유저
- SSH, VPN 개념은 낯설지만 따라 하면서 배우고 싶은 학습자

## 전체 스토리라인 (초안)

| 순서 | 장면 | 소스 |
|---|---|---|
| 1 | 문제 제기 — 모바일에서 집 컴퓨터의 Claude Code를 쓰고 싶다 | [01-Execution-Model](../../01-Execution-Model/README.md) |
| 2 | 구조 설명 — 모바일은 조작, 로컬 머신은 실행 | [mobile-to-local-execution.md](../../01-Execution-Model/concepts/mobile-to-local-execution.md) |
| 3 | 구조 선택 — 왜 Tailscale + Windows OpenSSH인가 (공개 포트 노출 없이) | [recommended-first-experiment.md](../../02-Architecture-Comparison/decisions/recommended-first-experiment.md) |
| 4 | 실전 성공 — iPhone에서 접속, Claude Code 실행, 파일 변경 검증 | [validation-results.md](../../04-Remote-Execution-Lab/lab/validation-results.md) |
| 5 | 실패 사례 1 — iPad 추가 시 `connection timed out`, 원인은 Tailscale 미설치 | [mobile-client-setup-lessons.md](../../05-Operations-Security/guides/mobile-client-setup-lessons.md) |
| 6 | 실패 사례 2 — GitHub 계정 두 개, push 팝업을 모바일에서 누를 수 없는 문제 | [github-push-video-lessons.md](../../05-Operations-Security/guides/github-push-video-lessons.md) |
| 7 | 실패 사례 3 — iPad Termius에서 한글이 자모로 분리되는 IME 문제 | [ipad-korean-input-lessons.md](../../05-Operations-Security/guides/ipad-korean-input-lessons.md) |
| 8 | 운영 규칙 정리 — 하지 말아야 할 것 vs 좋은 원격 작업 후보 | [remote-work-runbook.md](../../05-Operations-Security/guides/remote-work-runbook.md) |
| 9 | 마무리 — 지금 노트북으로 충분한 이유, 맥미니는 언제 검토하는가 | [final-recommendation.md](../summary/final-recommendation.md) |

## 장면별 상세 후보 (실패 사례 3건)

각 문서에 이미 mermaid 시퀀스 다이어그램과 "장면 구성 후보" 섹션이 있어 그대로 스토리보드 초안으로 쓸 수 있다.

1. **iPad Tailscale 미설치** — [mobile-client-setup-lessons.md](../../05-Operations-Security/guides/mobile-client-setup-lessons.md) `## 영상화 포인트`
2. **GitHub push 계정 고정** — [github-push-video-lessons.md](../../05-Operations-Security/guides/github-push-video-lessons.md) `## 영상 장면 구성 후보` (Scene 1~6)
3. **한글 IME 자모 분리** — [ipad-korean-input-lessons.md](../../05-Operations-Security/guides/ipad-korean-input-lessons.md) `## 영상화 포인트`

## 영상 형식 후보

- **길이**: 8~12분 (실패 사례 3건 + 도입/결론 포함)
- **형식**: 화면 녹화(Termius/터미널 실제 화면) + Remotion 슬라이드로 구조 다이어그램 설명을 교차
- **톤**: "나도 이렇게 실수했다" 톤 — 완성된 가이드보다 실제 시행착오를 보여주는 방식이 이 소재와 더 잘 맞음

## 영상 제작 전 확인 조건 (Go/No-Go)

Remotion 실제 제작 단계(`remotion-video` 스킬)로 넘어가기 전에 아래를 확인해야 한다.

- [ ] **보안 검토**: 화면 녹화/스크린샷에 Tailscale IP(`100.109.17.103`), 호스트명(`Changsoo`), 사용자명(`catchupai`), SSH config 경로 등 실제 값이 노출되는지 확인하고, 공개용에는 마스킹하거나 예시 값으로 교체
- [ ] **계정 정보 재확인**: GitHub 계정명(`solkit70`), 이메일(`solkit70@gmail.com`) 노출 범위를 사용자가 직접 승인
- [ ] **개인키/비밀번호 미노출 확인**: 녹화 원본에 SSH private key, password 입력 화면이 찍히지 않았는지 확인
- [ ] **재현 가능성 확인**: 시청자가 따라 할 수 있도록 Tailscale/Termius/OpenSSH 설치 단계가 영상 안에서 최소한 언급되는지 확인
- [x] **M7 검증 완료**: iPad Termius에서 Codex/Gemini 실행 가능 여부와 병행 사용 규칙을 기록
- [ ] **사용자 최종 승인**: 위 항목을 모두 확인한 뒤 사용자가 "영상 제작 시작"을 명시적으로 승인

## 다음 단계

이 브리프가 승인되면 `remotion-video` 스킬을 호출해 슬라이드 플랜 단계부터 진행한다. 이 Topic 자체의 범위는 여기(브리프 작성)까지이며, 실제 영상 제작은 별도 세션/작업으로 분리한다.



