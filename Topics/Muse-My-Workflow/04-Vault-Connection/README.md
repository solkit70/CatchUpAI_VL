# M4 — 볼트 연결 해법

## 진행 상태

실습 1에서 공식 문서와 Muse 화면을 확인했고, 실습 2에서 사본 규칙 초안과 가상·실제 볼트 미리 보기를 실행했다. 실습 3 준비로 가상 공개 시험 폴더와 시나리오 비교표를 만들었다. 실제 보고서는 내부 자료로 볼트 안에 두었으며 검토 대기 중이다. 외부 저장소 후보 선택·연결과 복사는 아직 하지 않았다.

1. [해법 지도](guides/solution-map.md) — 후보 8개, 제약과 비용, 다음 시험 범위.
2. [사본 정책 초안](guides/mirror-policy.md) — 포함·제외 기준과 승인 경계.
3. [시나리오 비교표](guides/seamless-scenarios.md) — D·E의 기존 근거와 C·A의 미검증 범위, 다음 시험과 캡처 장면.
4. [가상 시험 폴더](examples/trial-vault/) — 공개 표시된 가상 Markdown 자료 3개.
5. [미리 보기 스크립트](scripts/build_mirror.py) — 기본은 보고만 하며 실제 복사는 명시적 `--apply`가 필요하다.
6. [예시 설정](scripts/mirror_config.example.yaml) — 가상 시험 폴더만 대상으로 하는 JSON 문법의 YAML 호환 설정.
7. [가상 미리 보기 보고서](examples/mirror-report-sample.md) — 공개 1개 포함 후보, 개인·내부·미분류·비 Markdown 4개 제외.
8. [M4 WorkLog](../vl_worklog/20261105_M4_Muse-My-Workflow.md) — 실습 1·2 관찰과 다음 확인 지점.

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
