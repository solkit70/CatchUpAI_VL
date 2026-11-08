---
title: "WorkLog - M4 볼트 연결 해법 확인"
author:
  - Codex
created: 2026-11-05 06:39:13
tags:
  - muse-my-workflow
  - worklog
---

## 세션 정보

> 2026-11-07 Claude Code 보강 — 앞 세션 WorkLog 와 같은 머리 정보를 맞췄다. 아래 본문(실습 1 결과 ~ 실습 3 준비)은 Codex 원문 그대로다.

**날짜**: 2026-11-05
**Topic**: Muse-My-Workflow
**모듈**: M4 - 볼트 연결 해법 — 집과 밖을 끊김 없이 (실습 1 · 2 · 실습 3 준비)
**진행 에이전트**: Codex
**이전 WorkLog**: [20261105_M3_Muse-My-Workflow.md](20261105_M3_Muse-My-Workflow.md) — M3 완료

## 실습 1 결과

11월 5일 공식 자료와 Muse 웹의 Settings를 확인하고, 해법 8개의 비용 조건, 설치 요구 사항, 권한 관련 미확인 항목을 기록했다. Dropbox·GitHub·Box는 Business 목록에서 확인했고 Google Drive는 Productivity 목록에서 확인했다. Google Drive 상세 화면에서 파일 접근, 비공개·공유 파일 작업, 삭제, 백그라운드 동작을 별도로 설정하는 것을 확인했다. [해법 지도](../04-Vault-Connection/guides/solution-map.md#후보-8개-확인표)

웹의 Data controls에는 Import memory, Download your agent data, Reset Muse가 있었다. 이 화면에서 모델 학습을 끄는 스위치는 찾지 못했다. 해당 화면과 비즈니스 커넥터 목록을 영상 재료로 저장했다. [캡처 두 장](../04-Vault-Connection/README.md#영상용-화면)

## 판정과 다음 단계

- 후보 확인표 작성 완료. 시험 후보는 수동 다운로드, Claude Code Remote Control, Google Drive, Dropbox를 제안했고 사용자 확인이 남았다.
- 기존 연결 결정과 현재 UI 관찰의 차이는 사용자에게 알렸다. 실습 중 한 동작은 조회와 캡처였다.
- 다음 실습은 사본 포함·제외 규칙과 미리 보기 모드다. 5개 시나리오의 실제 저장소 시험과 가동은 이후 단계다. [시험 후보](../04-Vault-Connection/guides/solution-map.md#시험-후보-제안)

## 회고

공식 발표로 알 수 있는 지원 여부와 계정에서 볼 수 있는 권한을 함께 확인했다. 특히 Drive의 동작별 제어 화면은 볼 수 있었지만, 그 화면만으로 특정 폴더로 접근이 제한되는지는 판정할 수 없었다.

## 🎬 영상 재료

Business 목록에서 GitHub·Dropbox를 확인한 화면과 Data controls 화면을 준비했다. 화면의 메뉴가 무엇을 확인해 주는지 짧게 설명할 수 있다.

## 🎓 가르칠 때

커넥터 이름이 목록에 보이는 것, 사용자가 승인한 파일 동작, 접근할 수 있는 폴더 범위를 각각 확인하게 한다. 기존 수동 방법으로 같은 작업을 해 보고 새 연결로 줄어드는 단계를 센다.

## 실습 2 결과

사용자 승인 후 사본 규칙 초안과 실행 스크립트를 준비했다. 먼저 임시 가상 자료 다섯 개로 동작을 확인한 다음, 전체 볼트를 대상으로 읽기 전용 미리 보기를 실행했다. 실제 복사와 외부 연결은 하지 않았다.

- [사본 정책 초안](../04-Vault-Connection/guides/mirror-policy.md): `.md`와 명시적 `visibility: public`만 기본 포함한다. 내부 표식·개인·미분류·허용되지 않은 경로·큰 파일·비 Markdown은 제외한다.
- [미리 보기 스크립트](../04-Vault-Connection/scripts/build_mirror.py): 기본은 `PREVIEW ONLY`; 실제 복사에는 `--apply`가 필요하고 기존 파일은 기본적으로 덮어쓰지 않는다.
- [가상 예시 설정](../04-Vault-Connection/scripts/mirror_config.example.yaml): 표준 라이브러리만 쓰도록 JSON 문법의 YAML 호환 파일로 두었다.
- [가상 미리 보기 보고서](../04-Vault-Connection/examples/mirror-report-sample.md): 가상 파일 5개에서 포함 후보 1개, 제외 4개, 복사 0개.
- 실제 미리 보기는 `visibility: public` Markdown만 후보로 삼았다. 포함 후보 3개, 제외 55,975개, 복사 0개였다. 내부 표식 112개와 `visibility: internal` 58개는 전부 제외됐다. 그 밖에 분류 표식 없음 4,914개, 제외 경로 608개, 비 Markdown 50,283개가 제외됐다.
- 실제 미리 보기 보고서는 **`visibility: internal`**로 WorkLog 폴더에 저장했다. 제외 파일 경로는 보고서에 싣지 않고 사유별 건수로 집계했으며, 포함 후보 경로만 개별 표시했다.
- `--demo`는 가상 폴더를 임시로 만들고 종료 뒤 정리했다. 전체 볼트 시험은 포함 후보만 읽을 수 있도록 분류했고 내용을 보고서로 복사하지 않았다.

### 다음 승인 지점

내부 미리 보기 보고서에서 표시된 공개 후보 3개가 사본 범위에 들어가도 되는지 검토하고, 필요하면 포함 경로를 더 좁혀야 한다. `personal` 등급은 여전히 제외 상태다. M4 실습 1에서 제안한 시험 후보 D/E/C(Drive)/A 중 무엇을 시험할지도 사용자 선택이 필요하다. 이 검토 전에는 실제 복사·Muse 연결·외부 저장소 업로드를 하지 않는다.

### 화면 캡처 상태

미리 보기 결과를 화면 캡처하려 했지만 Windows 캡처 도구가 Obsidian 대신 다른 앱 화면을 반환했다. 무관한 화면은 저장하지 않았다. M4 실습 2의 캡처는 보류 상태다.

## 실습 3 준비

- [시나리오 비교표](../04-Vault-Connection/guides/seamless-scenarios.md)를 작성했다. M2 수동 전달과 M3 Topic 인계 결과를 기준선으로 기록하고, 이전 Remote Control Topic은 일반적인 모바일 세션·로컬 파일 작업의 참고 근거로만 표시했다. 이를 M4의 5개 시나리오 실증으로 간주하지 않는다.
- [가상 시험 폴더](../04-Vault-Connection/examples/trial-vault/)에 공개 표시된 Markdown 자료 세 개를 만들었다. 실제 행사·인물·장소가 없는 일정 충돌 예시이며, 원본을 덮어쓰지 않고 새 결과 파일을 쓰도록 지시를 넣었다.
- [예시 설정](../04-Vault-Connection/scripts/mirror_config.example.yaml)은 이 세 파일만 원본으로 삼도록 바꿨다. M4 실제 전체 볼트 보고서는 이 시험 폴더를 만들기 전에 생성한 스냅샷이며, 새 가상 파일은 해당 보고서에 포함되지 않는다.
- 예시 설정을 미리 보기로 실행해 포함 후보 3개, 제외 0개, 복사 0개를 확인했다. 목적지 파일은 만들지 않았다.
- 외부 연결·업로드는 아직 하지 않았다. 다음 UI 시험에서 가상 파일 카드, 권한 범위, 검색 결과, 새 결과 파일, 집 PC 회수 화면을 캡처할 예정이다. M4 실습 2 화면 캡처도 아직 보류 중이다.

### 실습 3 시작 전 필요한 확인

1. 볼트 내부의 미리 보기 보고서에서 실제 볼트의 공개 후보 3개와 현재 전체 범위를 검토한다.
2. 시험할 후보 D(수동), E(Remote Control), C(Drive), A(Dropbox)를 정한다. Drive·Dropbox 연결이나 파일 업로드는 구체적인 범위 승인 전에는 하지 않는다.

## 📊 DoD 체크리스트 (M4)

> 2026-11-07 Claude Code 보강 — 로드맵 M4 의 Definition of Done 을 이 세션까지의 실제 결과로 표시했다.

- [x] 해법 8가지 확인표 — 모든 행에 출처 종류 · 날짜 (11/5)
- [ ] 시나리오 5개 × 시험한 해법 결과표 (실패 포함) — 기준선 표만 있음, 실제 시험 전
- [ ] 사본 규칙 박창수 승인 · 미리 보기 보고서에 내부 표시 문서 0개 — 내부 표시 0개는 확인, **승인 대기**
- [ ] 첫 업로드는 박창수 승인 뒤 실행, 받는 곳 회수 확인
- [ ] 작업 종류별 경로표 · 되돌리는 법
- [x] 공개 문서에 실제 사본 설정 · 계정 정보 없음 · 산출물 폴더 README 작성
- [x] README 링크가 실제 파일을 가리키는지 확인 (`check_links.py`)
- [ ] WorkLog (🎬 · 🎓 칸 포함) · Module Retrospective 작성 — WorkLog 는 있음, 회고는 모듈을 닫을 때

**진행 상태**: 🔄 M4 3/8 (2026-11-05)

## 다음 세션에 넘길 것

> 2026-11-07 Claude Code 보강 — 위 「다음 승인 지점」 · 「실습 3 시작 전 필요한 확인」을 다음 에이전트가 바로 쓰게 한 곳에 모았다.

1. **박창수 결정 두 가지가 먼저다.** ① 볼트 안의 내부 미리 보기 보고서(공개 후보 3개)를 검토해 사본 범위를 승인하거나 좁힌다 ② 시험 후보 D · E · C(Drive) · A 중 무엇을 시험할지 고른다. 결정 전에는 실제 복사 · Muse 연결 · 외부 업로드를 하지 않는다.
2. 결정 뒤 **실습 3**: [가상 시험 폴더](../04-Vault-Connection/examples/trial-vault/) 만 연결해 [시나리오 비교표](../04-Vault-Connection/guides/seamless-scenarios.md#다음-실험-순서)의 「다음 실험 순서」 1~5 대로 진행한다. 권한이 필요 이상이면 중단한다.
3. 이어서 **실습 4**: 작업 종류별 경로표(`guides/task-route-table.md`, 아직 없음)와 되돌리는 법 → 가동.
4. 시작할 때 읽을 것: [M4 README](../04-Vault-Connection/README.md) · [두 가지 연결 모델](../04-Vault-Connection/concepts/connection-models.md) · [해법 지도](../04-Vault-Connection/guides/solution-map.md) · [사본 정책 초안](../04-Vault-Connection/guides/mirror-policy.md).
5. 보류 중: 실습 2 미리 보기 화면 캡처(Windows 캡처 도구 문제).
6. **일정 주의**: 로드맵은 M5(1주일 실제 사용)를 11/8 에 시작하도록 잡았다. M4 조합이 정해지지 않으면 M5 를 시작할 수 없으므로, Live #35(11/8)에서 후보를 정하거나 로드맵 일정을 다시 잡는다.
