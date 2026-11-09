# M4 — 볼트 연결 해법 — 집과 밖을 끊김 없이

[English](README.en.md)

**상태**: 🔄 진행 중 7/8 (2026-11-05 시작 · Codex) — E의 가상 S2·S4, C의 가상 Drive 파일 읽기·결과 작성·PC 수동 회수, 승인된 공개 후보 3개 별도 Drive 업로드를 확인했다. Dropbox는 연결·동작별 Allow 설정을 확인하고 개인 전용 가상 시험 폴더에 파일 세 개를 올려 Muse 읽기·결과 쓰기를 확인했다. 업로드 전 검색은 0건이었고 업로드 후 재검색에서는 세 파일 모두 찾았다. 폴더 목록에도 결과 파일을 포함해 네 파일을 확인했다. 실제 볼트 전체 사본 정책은 미결정.
**예상 학습 시간**: 3시간

## 진행 상태

실습 1에서 공식 문서와 Muse 화면을 확인했고, 실습 2에서 사본 규칙 초안과 실제 볼트 미리 보기를 실행했다. 내부 미리 보기 보고서를 검토했고, 표시된 공개 후보 3개는 사용자 승인 뒤 별도 Drive 폴더에 올려 확인했다. 이 승인은 실제 볼트 전체를 미러링하는 포괄 승인이 아니다. E · Claude Code Remote Control은 Muse 밖의 대안으로 가상 S2·S4를 시험했고, C · Google Drive는 지정 가상 폴더의 읽기·결과 작성과 PC 수동 다운로드를 확인했다. Dropbox의 2026-11-08 화면에서는 모든 동작별 권한이 **Allow**(다운로드·쓰기 권한은 Custom Allow)였다. 사용자가 기기 접근 확인창을 승인한 뒤 `Muse M4 Test - Synthetic` 개인 전용 폴더에 가상 자료 세 개를 올렸다. 업로드 전에 실행한 파일명 검색은 0건이었지만, 업로드 뒤 폴더 범위를 지정해 다시 검색하자 세 파일 모두 찾았다. 지정 경로 읽기와 `m4-dropbox-result.md` 작성도 성공했다. Dropbox 화면에서 원본 세 개와 결과 파일, 결과 내용을 확인했다. Dropbox 데스크톱 앱 설정 후 네 파일이 깨어 있는 PC에 자동 동기화되어 자동 PC 회수는 깨어 있는 상태에서 확인했다. 절전 요청 전후 네 파일의 로컬 상태는 유지됐으나 S0 진입·복귀와 절전 중 클라우드 변경은 검증하지 못해 Sleep 효과는 미판정이다. Dropbox 재실행 후 파일명 세 개 검색과 폴더 네 항목 목록도 성공했다. 모바일 시험·폴더 범위 제한은 미검증이다.

## 📚 학습 순서

1. [두 가지 연결 모델](concepts/connection-models.md) — 클라우드 대리형 · 원격 콘솔형, 동기화가 아니라 연결, 사본과 받는 곳, 연결 전 확인 세 가지.
2. [해법 지도](guides/solution-map.md) — 후보 8개, 제약과 비용, 다음 시험 범위.
3. [사본 정책 초안](guides/mirror-policy.md) — 포함·제외 기준과 승인 경계.
4. [시나리오 비교표](guides/seamless-scenarios.md) — D·E·C·A의 기존·합성 시험 근거, 미확인 범위, 다음 시험과 캡처 장면.
5. [가상 시험 폴더](examples/trial-vault/) — 공개 표시된 가상 Markdown 자료 3개.
6. [미리 보기 스크립트](scripts/build_mirror.py) — 기본은 보고만 하며 실제 복사는 명시적 `--apply`가 필요하다.
7. [예시 설정](scripts/mirror_config.example.yaml) — 가상 시험 폴더만 대상으로 하는 JSON 문법의 YAML 호환 설정.
8. [가상 미리 보기 보고서](examples/mirror-report-sample.md) — 공개 1개 포함 후보, 개인·내부·미분류·비 Markdown 4개 제외.
9. [작업 종류별 경로표 초안](guides/task-route-table.md) — 현재 근거가 있는 흐름과 미승인 경계, 중단·되돌림 원칙.
10. [M4 WorkLog](../vl_worklog/20261108_M4_Muse-My-Workflow.md) — 실습 1·2 관찰과 다음 확인 지점.

## 지금까지 알아낸 것

- **후보 8개** 모두 공식 자료와 Muse 화면으로 확인 날짜와 함께 정리했다. Dropbox 연결과 가상 폴더의 읽기·쓰기 시험도 수행했다.
- **동기화 기능은 없다.** 커넥터는 필요할 때 들여다보는 연결이다. 그래서 「밖에서 한 일이 집 PC 에 저절로 도착」(S5)은 아직 어떤 후보로도 충족되지 않는다.
- **공개 표시만 담는 사본이 안전하게 동작한다.** 실제 볼트 미리 보기에서 포함 후보 3 · 제외 55,975 · 복사 0 — 내부 표식 112 · `visibility: internal` 58 은 모두 빠졌다.
- **확인 못 한 것** — 업로드 전 검색은 0건, 업로드 후 지정 폴더 범위 검색은 세 파일 모두 성공했다. 모바일 접근, 폴더 범위의 기술적 강제, Windows 절전 효과는 미판정이다. 깨어 있는 PC의 자동 회수는 Dropbox 데스크톱 앱 설정 뒤 네 파일이 Available on this device로 표시되어 확인했다. 이전 Muse 화면에 나타난 403 알림은 Dropbox 요청 오류와 연결되지 않았다. Chrome 업데이트·재시작 후 현재 Muse 화면에는 알림이 보이지 않았지만, 사용자가 평소 반복된다고 보고해 해결 여부와 원인은 미확정이다. Google Drive 폴더 범위와 자동 동기화도 미확인이다.

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
- [Dropbox 권한 화면 (2026-11-08)](assets/20261108-muse-dropbox-permissions.jpg) — 연결 및 동작별 Allow 상태. 영상에는 계정 식별 정보가 노출되지 않는지 먼저 확인한다.
- [Dropbox 기기 접근 확인창 (2026-11-08)](assets/20261108-dropbox-permission-prompt-1.jpg) — 전용 가상 시험 폴더와 파일 업로드 전 권한 확인.
- [Dropbox 업로드 완료 화면](assets/20261108-dropbox-upload-success.jpg) · [시험 폴더 파일 4개](assets/20261108-dropbox-four-files.jpg).
- [Muse 분석 결과 상단](assets/20261108-muse-dropbox-analysis-result.jpg) · [Dropbox 결과 내용 상단](assets/20261108-dropbox-result-content-top.jpg) · [결과 내용 하단](assets/20261108-dropbox-result-content-bottom.jpg).
- [Dropbox 결과 파일 검증 화면](assets/20261108-dropbox-result-verified.jpg).

## 이동

- 이전 · [M3 — VibeLearn AI on Muse](../03-VibeLearn-on-Muse/README.md)
- 다음 · M5 — 1주일 실제 사용과 사용 가이드 ([로드맵](../vl_roadmap/20261018_RoadMap_Muse-My-Workflow.md#m5---1주일-실제-사용과-사용-가이드)) — M4 에서 정한 조합으로 시작한다
