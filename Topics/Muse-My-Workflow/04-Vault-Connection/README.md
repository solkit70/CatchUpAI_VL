# M4 — 볼트 연결 해법 — 집과 밖을 끊김 없이

[English](README.en.md)

**상태**: 🔄 진행 중 3/8 (2026-11-05 시작 · Codex) — 실습 1 확인표 · 실습 2 미리 보기 완료, 실습 3 준비(가상 시험 폴더 · 시나리오 비교표). **미리 보기 보고서 검토와 시험 후보(D / E / C Drive / A) 선택을 박창수가 하면 실습 3 을 시작한다**
**예상 학습 시간**: 3시간

## 진행 상태

실습 1에서 공식 문서와 Muse 화면을 확인했고, 실습 2에서 사본 규칙 초안과 가상·실제 볼트 미리 보기를 실행했다. 실습 3 준비로 가상 공개 시험 폴더와 시나리오 비교표를 만들었다. 실제 보고서는 내부 자료로 볼트 안에 두었으며 검토 대기 중이다. 외부 저장소 후보 선택·연결과 복사는 아직 하지 않았다.

## 📚 학습 순서

1. [두 가지 연결 모델](concepts/connection-models.md) — 클라우드 대리형 · 원격 콘솔형, 동기화가 아니라 연결, 사본과 받는 곳, 연결 전 확인 세 가지.
2. [해법 지도](guides/solution-map.md) — 후보 8개, 제약과 비용, 다음 시험 범위.
3. [사본 정책 초안](guides/mirror-policy.md) — 포함·제외 기준과 승인 경계.
4. [시나리오 비교표](guides/seamless-scenarios.md) — D·E의 기존 근거와 C·A의 미검증 범위, 다음 시험과 캡처 장면.
5. [가상 시험 폴더](examples/trial-vault/) — 공개 표시된 가상 Markdown 자료 3개.
6. [미리 보기 스크립트](scripts/build_mirror.py) — 기본은 보고만 하며 실제 복사는 명시적 `--apply`가 필요하다.
7. [예시 설정](scripts/mirror_config.example.yaml) — 가상 시험 폴더만 대상으로 하는 JSON 문법의 YAML 호환 설정.
8. [가상 미리 보기 보고서](examples/mirror-report-sample.md) — 공개 1개 포함 후보, 개인·내부·미분류·비 Markdown 4개 제외.
9. [M4 WorkLog](../vl_worklog/20261105_M4_Muse-My-Workflow.md) — 실습 1·2 관찰과 다음 확인 지점.

## 지금까지 알아낸 것

- **후보 8개** 모두 공식 자료와 Muse 화면으로 확인 날짜(11/5)와 함께 정리했다. Muse 커넥터 목록에서 GitHub · Dropbox · Google Drive 를 직접 확인했다(연결은 안 함).
- **동기화 기능은 없다.** 커넥터는 필요할 때 들여다보는 연결이다. 그래서 「밖에서 한 일이 집 PC 에 저절로 도착」(S5)은 아직 어떤 후보로도 충족되지 않는다.
- **공개 표시만 담는 사본이 안전하게 동작한다.** 실제 볼트 미리 보기에서 포함 후보 3 · 제외 55,975 · 복사 0 — 내부 표식 112 · `visibility: internal` 58 은 모두 빠졌다.
- **확인 못 한 것** — 커넥터를 폴더 하나 · 레포 하나로 좁힐 수 있는지, 웹 Data controls 에 학습 끄기 스위치가 없는데 다른 곳에 있는지, Windows 용 Muse 데스크톱 배포.
- 실습 2 의 미리 보기 화면 캡처는 Windows 캡처 도구 문제로 보류 중이다.

## 실습 2 재현 방법

다음 명령은 임시 폴더에 가상 Markdown 자료 다섯 개를 만들고 미리 보기만 실행한다. 임시 폴더는 실행 뒤 자동 정리되며 실제 볼트 자료는 읽거나 복사하지 않는다.

```powershell
python Ingest/CatchUpAI_VL/Topics/Muse-My-Workflow/04-Vault-Connection/scripts/build_mirror.py --demo --report Ingest/CatchUpAI_VL/Topics/Muse-My-Workflow/04-Vault-Connection/examples/mirror-report-sample.md
```

고정된 세 자료를 대상으로 다시 미리 보려면 예시 설정을 사용한다. 실제 복사 옵션은 붙이지 않는다.

```powershell
python Ingest/CatchUpAI_VL/Topics/Muse-My-Workflow/04-Vault-Connection/scripts/build_mirror.py --config Ingest/CatchUpAI_VL/Topics/Muse-My-Workflow/04-Vault-Connection/scripts/mirror_config.example.yaml --report Ingest/CatchUpAI_VL/Topics/Muse-My-Workflow/vl_worklog/trial-vault-preview-internal.md
```

실제 경로를 대상으로 할 때는 먼저 설정 파일의 원본·목적지·포함 경로를 사용자가 검토해야 한다. 기본 실행은 미리 보기이며, 정책과 보고서를 승인하기 전에는 `--apply`를 붙이지 않는다. `--apply`는 별도 승인 없이 실행하지 않는다.

## 영상용 화면

- [Muse 비즈니스 커넥터](assets/muse-business-connectors.jpg) — GitHub와 Dropbox가 표시된 목록.
- [Muse Data controls](assets/muse-data-controls.jpg) — 메모리 가져오기, 데이터 내려받기, 초기화 메뉴.

## 이동

- 이전 · [M3 — VibeLearn AI on Muse](../03-VibeLearn-on-Muse/README.md)
- 다음 · M5 — 1주일 실제 사용과 사용 가이드 ([로드맵](../vl_roadmap/20261018_RoadMap_Muse-My-Workflow.md#m5---1주일-실제-사용과-사용-가이드)) — M4 에서 정한 조합으로 시작한다
