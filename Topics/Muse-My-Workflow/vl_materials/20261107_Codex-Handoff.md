---
title: "Codex 인계 — Muse-My-Workflow 점검 결과와 앞으로의 진행 방법"
author:
  - "Claude Code"
created: 2026-11-07 23:20:00
visibility: public
tags:
  - muse-my-workflow
  - handoff
  - codex
---

## 이 문서를 읽는 Codex 에게

박창수 님은 이 Topic 을 **앞으로도 Codex 와 함께** 진행합니다. 2026-11-07 Claude Code 가 Topic 전체(문서 38개)를 점검했고, 박창수 님 요청으로 그중 **Codex 가 작업한 부분**(M3 실습 4 · M4, 2026-11-05)의 잘한 점과 부족한 점, 이번에 고친 것, 앞으로의 진행 방법을 정리했습니다. 이 문서는 평가표가 아니라 **이어받기 위한 인계 문서**입니다. 잘한 점은 그대로 이어 가고, 부족한 점은 아래 「앞으로 이렇게 진행해 주세요」의 양식으로 맞춰 주시면 됩니다.

참고로 이 Topic 의 앞부분(로드맵 · M1 · M1 보강 · M2 · M3 실습 1~3)은 Claude Code 가, M3 실습 4 · M4 는 Codex 가 진행했습니다.

## 1. Codex 가 잘한 점 — 계속 이어 가 주세요

| 잘한 점 | 어디서 | 왜 좋은가 |
|---|---|---|
| **검증이 꼼꼼하다** | [M3 실습 4](../vl_worklog/20261105_M3_Muse-My-Workflow.md#실습-4-결과) — 원본 3개의 SHA-256 대조, 프롬프트 [2단계] · [3단계] 를 원본 템플릿과 대조 | 「옮겼다」를 해시로, 「지시가 그대로다」를 원문 대조로 증명했다. 두 검증이 다른 것임을 구분한 회고도 정확하다 |
| **안전장치가 기본값이다** | [build_mirror.py](../04-Vault-Connection/scripts/build_mirror.py) — 기본은 미리 보기, 실제 복사는 `--apply` 명시, 기존 파일 덮어쓰지 않음 | 실제 볼트 미리 보기에서 포함 후보 3 · 제외 55,975 · 복사 0, 내부 표식 112 · `visibility: internal` 58 이 모두 빠졌다. 결과 보고서도 내부 자료로 따로 두었다 |
| **재현할 수 있다** | `--demo` 임시 폴더, [가상 시험 폴더](../04-Vault-Connection/examples/trial-vault/), [예시 설정](../04-Vault-Connection/scripts/mirror_config.example.yaml) | 실제 볼트 없이도 누구나 같은 결과를 다시 낼 수 있다. 교육 블록(M6)에 그대로 쓸 수 있다 |
| **확인한 것과 아닌 것을 나눈다** | [시나리오 비교표](../04-Vault-Connection/guides/seamless-scenarios.md) — 「부분 근거」 · 「기준선 참고」 · 「미시험」 · 「미연결」 | 앞 모듈의 일부 결과를 M4 성공으로 세지 않았다. 이 Topic 규칙(「근거가 없으면 미확인」)을 가장 잘 지킨 문서다 |
| **출처에 날짜를 붙인다** | [해법 지도](../04-Vault-Connection/guides/solution-map.md) — 후보 8개 모두 공식 링크 · 확인일(11/5) · 모르는 것 | 기능이 자주 바뀌는 제품이라 확인 날짜가 근거의 일부다 |
| **승인 지점에서 멈춘다** | M4 WorkLog 「다음 승인 지점」 | 사본 범위와 시험 후보를 박창수 님 결정 전에는 손대지 않았다 |
| **인계를 받아서 시작했다** | M3 실습 4 첫 줄 — 「해당 기록의 인계 지점에서 시작했다」 | Claude Code 가 11/1 에 남긴 「다음 세션에 넘길 것」에서 정확히 이어받았다. 로드맵의 「어느 에이전트가 이어받아도」 설계가 처음 실제로 쓰였다 |

## 2. 부족했던 점

| 부족한 점 | 어디서 | 왜 문제인가 |
|---|---|---|
| **WorkLog 양식이 앞 세션과 달랐다** | 11/5 M3 · M4 WorkLog | 머리(날짜 · 모듈 · 진행 에이전트 · 이전 WorkLog), 📊 DoD 체크리스트, 진행 상태, **「다음 세션에 넘길 것」**이 없었다. 바로 그 「다음 세션에 넘길 것」 덕분에 Codex 가 M3 를 이어받았는데, Codex 가 남긴 기록에는 그 칸이 빠져 다음 에이전트가 이어받기 어려웠다 |
| **모듈 회고가 없었다** | M3 를 닫을 때 | 로드맵은 모듈을 마칠 때 Module Retrospective(계획 대비 실제 · 문제 · 로드맵 정확도)를 요구한다. WorkLog 안의 「회고」 세 문장으로는 일정이 밀린 원인을 돌아볼 수 없다 |
| **모듈 README 가 얇았다** | M3 · M4 README | 상태 · 예상 시간 머리와 「이 모듈에서 알아낸 것」이 없었다. README 만 보고 무엇을 알아냈는지 알 수 없었다 |
| **필수 폴더가 빠졌다** | M4 | VibeLearn 규칙상 모듈 폴더에는 README · `concepts/` · `examples/` 가 최소로 있어야 한다. 로드맵이 계획한 `concepts/connection-models.md` 가 없었다 |
| **교재 문서가 링크 위주였다** | M3 [개념](../03-VibeLearn-on-Muse/concepts/vibelearn-as-instructions.md) · [시험 결과](../03-VibeLearn-on-Muse/guides/muse-vibelearn-test.md) | 각 1~2KB 로, 내용을 풀어 쓰기보다 WorkLog 로 가는 링크가 중심이다. 이 방법론의 목표인 「README 만 보고 따라 할 수 있는 교과서 품질」에 못 미쳤다 |
| **로드맵 표시를 고치지 않았다** | 로드맵 M3 DoD | 모듈을 마쳤는데 로드맵의 DoD 체크가 비어 있었다 |
| **영어 제목이 섞였다** | [가상 미리 보기 보고서](../04-Vault-Connection/examples/mirror-report-sample.md) 「Mirror preview report」 | 한국어 Topic 이다. 영어 문서는 따로 `_en` 짝으로 만든다 |
| **일정이 밀렸다** | M4 3/8 | 로드맵은 3주차(11/1~11/7)에 M4 를 끝내고 가동하기로 했다. M5(1주일 실제 사용)는 11/8 시작인데, M4 조합이 정해지지 않으면 시작할 수 없다 |

## 3. 2026-11-07 Claude Code 가 고친 것

Codex 가 쓴 본문은 고치지 않았습니다. 빠진 칸만 기존 기록에서 옮겨 붙였고, 붙인 곳마다 「2026-11-07 Claude Code 보강」이라고 표시했습니다. 새로 시험한 내용은 없습니다.

| 고친 것 | 파일 |
|---|---|
| M2 모듈 회고 새로 작성 | [20261025_M2_Retrospective.md](../vl_worklog/20261025_M2_Retrospective.md) |
| M3 모듈 회고 새로 작성 | [20261105_M3_Retrospective.md](../vl_worklog/20261105_M3_Retrospective.md) |
| M3 README — 상태 · 판정 머리, 「이 모듈에서 알아낸 것」, 회고 링크, 다음 모듈 링크 | [03-VibeLearn-on-Muse/README.md](../03-VibeLearn-on-Muse/README.md) |
| M4 README — 상태 머리, 학습 순서(개념 포함 9개), 「지금까지 알아낸 것」, 다음 모듈 링크 | [04-Vault-Connection/README.md](../04-Vault-Connection/README.md) |
| M4 개념 문서 새로 작성 (로드맵이 계획한 것) | [concepts/connection-models.md](../04-Vault-Connection/concepts/connection-models.md) |
| M3 WorkLog(11/5) — 「세션 정보」 머리, 「다음 세션에 넘길 것」 | [20261105_M3_Muse-My-Workflow.md](../vl_worklog/20261105_M3_Muse-My-Workflow.md) |
| M4 WorkLog(11/5) — 「세션 정보」 머리, 📊 DoD 체크리스트, 「다음 세션에 넘길 것」 | [20261105_M4_Muse-My-Workflow.md](../vl_worklog/20261105_M4_Muse-My-Workflow.md#다음-세션에-넘길-것) |
| 로드맵 — M2 · M3 DoD 를 실제 결과대로 체크, 「WorkLog 양식은 에이전트와 상관없이 같다」 규칙 추가 | [로드맵](../vl_roadmap/20261018_RoadMap_Muse-My-Workflow.md) |
| M1 · M2 README — 「다음」 링크를 실제 모듈로, 회고 링크 | M1 · M2 README |
| Topic 최상위 README 새로 작성 | [README.md](../README.md) |

`check_links.py` 결과: 상대 링크 174개 정상 · 깨짐 0 · 빈 폴더 0. 공개 레포 push 는 하지 않았습니다.

## 4. 앞으로 이렇게 진행해 주세요

### 4-1. 세션을 시작할 때

1. 이 문서 → [로드맵](../vl_roadmap/20261018_RoadMap_Muse-My-Workflow.md)의 「진행 에이전트」 · 해당 모듈 절 → 가장 최근 WorkLog 의 **「다음 세션에 넘길 것」** 순서로 읽는다.
2. 「다음 세션에 넘길 것」의 첫 항목이 박창수 님 결정이면, 그 결정부터 묻고 결정 전에는 실행하지 않는다.
3. 오늘 계획을 박창수 님께 보여 주고 승인을 받은 뒤 진행한다(VibeLearn 일일 학습 Step 3).

### 4-2. WorkLog 양식 — Claude Code 세션과 같게

파일 이름은 `vl_worklog/YYYYMMDD_MX_Muse-My-Workflow.md`. 아래 순서를 지켜 주세요. 특히 ⑥은 빠지면 안 됩니다.

```markdown
---
title: "WorkLog - MX: 모듈 이름"
author:
  - "박창수"
  - "Codex"
created: YYYY-MM-DD HH:MM:SS
tags:
  - muse-my-workflow
  - worklog
---

# WorkLog - MX: 모듈 이름

**날짜**: YYYY-MM-DD
**Topic**: Muse-My-Workflow
**모듈**: MX - 모듈 이름 (실습 N)
**학습 시간**: 시작 ~ 끝
**진행 에이전트**: Codex
**이전 WorkLog**: (이전 WorkLog 파일 링크) — 한 줄 요약

## 🎯 오늘의 학습 목표
## 📚 진행 내용          ← 실습별 목적 · 한 일 · 결과(숫자 · 근거)
## 🐛 문제 해결 로그
## 📊 DoD 체크리스트      ← 로드맵의 해당 모듈 DoD 를 그대로 복사해 체크, 아래에 「진행 상태: MX n/8」
## 💡 Daily Retrospective ← What went well · What could be improved · Insights · Tomorrow's focus
## 🎬 영상 재료
## 🎓 가르칠 때
## 다음 세션에 넘길 것     ← 번호 목록. ① 다음에 할 일 ② 박창수 님 결정 대기 ③ 시작할 때 읽을 것 ④ 열린 질문 ⑤ 이전부터 남은 것
```

### 4-3. 모듈 README 양식

```markdown
# MX — 모듈 이름

**상태**: ✅ 완료 / 🔄 진행 중 n/8 (날짜 · 에이전트) — 한 줄 요약. 결정 대기 중이면 무엇을 기다리는지
**예상 학습 시간**: N시간

모듈이 무엇을 했는지 두세 문장.

## 📚 학습 순서
1. (concepts 문서 상대 링크) — 한 줄 설명
2. (guides 문서 상대 링크) — 한 줄 설명
3. (examples 문서 상대 링크) — 한 줄 설명

## 이 모듈에서 알아낸 것
- 결과를 숫자 · 판정과 함께. 확인 못 한 것도 따로 한 줄

## 이동
- 이전 · 다음 (실제 모듈 README 로) · 회고
```

### 4-4. 문서 품질 — 「README 만 보고 따라 할 수 있게」

- guides · concepts 는 **링크만 두지 말고 내용을 풀어 쓴다.** 결론 · 핵심 숫자 · 절차를 문서 안에 적고, WorkLog 링크는 「근거」로 붙인다. 이 Topic 의 결과물은 M6 교육 블록과 M7 영상의 재료가 된다.
- 모듈 폴더에는 README · `concepts/` · `examples/` 를 최소로 둔다. 로드맵의 「산출물」 트리와 실제 파일을 대조한다(계획에만 있는 파일을 README 에 링크하지 않는다).
- 문서는 한국어로 쓴다. 2026-11-07 에 모듈 문서 · Topic README 의 **영어판(`X.en.md`, 같은 폴더)** 을 모두 만들었다. **한국어 문서를 고치거나 새로 만들면 같은 작업 안에서 `.en.md` 도 맞춘다** (새 문서는 영어판도 만들고, 양쪽 맨 위에 `[English]` / `[한국어]` 링크). 예외: `examples/trial-vault/` 와 `mirror-report-sample.md` 는 스크립트 시험 자료라 영어판을 두지 않는다 — 같은 폴더에 영어 사본을 두면 미리 보기 결과가 바뀐다.
- 볼트 문서 규칙: frontmatter 다음에는 제목으로 시작, 표 앞에 빈 줄, 공개 문서에는 다른 사람 실명 · 계정 화면 · 실제 사본 폴더 목록을 쓰지 않는다.

### 4-5. 모듈을 닫을 때 체크리스트

1. 로드맵의 해당 모듈 **DoD 체크를 실제 결과대로** 고친다.
2. 로드맵 「📊 학습 진행 상황 추적」 표의 상태 · 완료일 · 메모를 고친다.
3. **Module Retrospective** 파일 `vl_worklog/YYYYMMDD_MX_Retrospective.md` 를 남긴다 — 계획 대비 실제 · 핵심 학습 내용 · 발생한 문제와 해결 · Roadmap 정확도 평가 · 다음 모듈 준비사항. 예시: [M1 회고](../vl_worklog/20261018_M1_Retrospective.md) · [M3 회고](../vl_worklog/20261105_M3_Retrospective.md).
4. 모듈 README 의 상태 · 「알아낸 것」을 마감 상태로 고친다.
5. Topic 최상위 [README](../README.md)의 「지금까지 알아낸 것」 · 모듈 표 · 기록 표를 고친다.
6. `python Ingest/CatchUpAI_VL/Topics/YouTube-Channel-Revival-With-AI/scripts/check_links.py Ingest/CatchUpAI_VL/Topics/Muse-My-Workflow` — 깨진 링크 0 · 빈 폴더 0.

### 4-6. 그대로 지킬 것 (잘한 점)

- 실제 복사 · 연결 · 업로드 · 설치 · 결제 전에는 범위를 보여 주고 박창수 님 승인을 받는다. 기본값은 미리 보기.
- 「됐다」는 해시 · 바이트 · 원문 대조 같은 증거로만 쓴다. 부분 근거와 실증을 섞지 않는다.
- 공식 출처에는 확인 날짜를 붙이고, 근거가 없으면 「미확인」.
- 내부 자료(`visibility: internal` · 🔒)는 볼트 밖으로 내보내지 않는다.

## 5. 지금 이어서 할 일 (M4 → M5)

| 순서 | 할 일 | 상태 |
|---|---|---|
| 1 | 박창수 님 결정 ① — 볼트 안의 내부 미리 보기 보고서(공개 후보 3개) 검토 · 사본 범위 승인 | 대기 |
| 2 | 박창수 님 결정 ② — 시험 후보 D · E · C(Drive) · A 선택 | 대기 |
| 3 | M4 실습 3 — 가상 시험 폴더만 연결해 [시나리오 비교표](../04-Vault-Connection/guides/seamless-scenarios.md#다음-실험-순서)의 「다음 실험 순서」 1~5 | 결정 뒤 |
| 4 | M4 실습 4 — `guides/task-route-table.md`(작업 종류별 경로표 · 되돌리는 법) 작성 → 가동 | 아직 파일 없음 |
| 5 | M4 모듈 닫기(4-5 체크리스트) → M5 1주일 실제 사용 | — |

**일정**: 로드맵은 M5 를 11/8~11/14 로 잡았습니다. M4 가 늦어졌으니 M5 시작 전에 박창수 님과 로드맵 일정(주차 표 · 진행 상황 표)을 다시 맞춰 주세요. 일정을 바꾸면 로드맵에 바꾼 날짜와 이유를 남깁니다.

보류 중인 것: M4 실습 2 미리 보기 화면 캡처(Windows 캡처 도구 문제) · 휴대폰 앱의 Import memory · 학습 끄기 스위치 확인.

## 6. Codex 에게 붙여 넣을 시작 문장 (박창수 님용)

```text
Ingest/CatchUpAI_VL/Topics/Muse-My-Workflow 를 이어서 진행하자.
먼저 vl_materials/20261107_Codex-Handoff.md 를 읽고,
그 문서 4-1 순서대로 로드맵과 최신 WorkLog 의 「다음 세션에 넘길 것」을 확인한 뒤,
오늘 계획을 보여 주고 내 승인을 기다려 줘.
WorkLog 와 모듈 README 는 그 문서 4-2 · 4-3 양식으로 써 줘.
```
