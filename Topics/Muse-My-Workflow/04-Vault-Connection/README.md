# M4 — 볼트 연결 해법 — 집과 밖을 끊김 없이

[English](README.en.md)

**상태**: 🔄 진행 중 7/8 (2026-11-05 시작 · Codex) — E의 가상 S2·S4, C의 Google Drive 웹 합성 폴더 읽기·결과 작성·PC 수동 회수, 승인된 공개 후보 3개 별도 Drive 업로드를 확인했다. 11/15에는 별도로 Drive for desktop의 `Computers → My PC → trial-vault`에서 Muse 읽기·쓰기와 켜져 있는 PC로의 자동 회수를 검증했다. Dropbox 합성 중첩 Vault의 읽기·쓰기·깨어 있는 PC 회수와 충돌 수동 병합을 확인했다. Muse-native에서는 중첩 합성 폴더 ZIP을 가져오고, 수정본과 새 파일을 포함한 전체 트리를 ZIP으로 되돌려 받아 4개 파일의 경로·해시를 검증했다. 작은 트리의 수동 전체 ZIP 왕복은 통과했지만 실제 Vault 규모 한도와 실제 Vault 자동 동기화는 미확인이다. 실제 Vault 전체 사본 정책은 미결정.
**예상 학습 시간**: 3시간

2026-11-14 합성 크기 시험에서 Muse는 5,777개 Markdown 파일·103.8 MiB payload를 ZIP으로 왕복했고, 검색·단일 파일 편집 후에도 경로를 유지했다. Obsidian fixture에서 경로가 있는 링크는 같은 basename의 Gamma 노트가 아닌 Beta 노트로 따라갔고, 경로 없는 중복 `[[note]]`는 모호하다고 판정해 대상을 선택하지 않았다. 별도 fixture에서 heading 링크 `#Target Heading`과 block 링크 `#^block-731`을 같은 노트 안의 서로 다른 fragment로 해석하고, 지정한 block 문단만 편집했다. 이미지 첨부 링크는 PNG 픽셀 판독을, PDF 첨부 링크는 명시 경로의 1페이지 텍스트 추출과 동명 decoy 구분을 확인했고, 각 반환 ZIP의 경로·내용을 로컬에서 대조했다. 이는 작은 표본에서의 링크·첨부 처리 결과이며 복잡한 PDF, Obsidian backlinks pane/index, 실제 Vault 전체 동작은 입증하지 않는다. Muse의 Library → System Files에서는 업로드·생성 파일 트리를 관리할 수 있지만 전체 용량 한도는 공개 자료나 화면에서 확인되지 않았다. 전체 Vault는 합성 payload보다 약 637배 크므로 Muse 내부 저장소가 전체 Vault를 수용한다고 아직 결론 내릴 수 없다. 내용 판독에서 Python·JSON·CSV는 정확했고, PNG OCR은 공백을 누락했다. Google Drive for desktop을 설치하고 합성 `trial-vault`의 동기화 완료를 확인했다. Muse의 `Computers` 접근은 아직 미시험이며, Dropbox 표준 동기화는 합성 폴더에서 성공했지만 실제 Vault 위치는 미시험이다. Dropbox Backup은 단방향이므로 Muse 편집 결과를 원본에 되돌리는 동기화 용도로 제외한다. 자세한 근거는 [경로표](guides/task-route-table.md#보조-저장소-비교-업데이트-2026-11-14), [11월 14일 WorkLog — heading/block](../vl_worklog/20261114_M4_Muse-My-Workflow.md#obsidian-headingblock-fragment-링크-시험-2026-11-14), [이미지 첨부](../vl_worklog/20261114_M4_Muse-My-Workflow.md#obsidian-이미지-첨부-wikilink-경로판독-시험-2026-11-14), [PDF 첨부](../vl_worklog/20261114_M4_Muse-My-Workflow.md#obsidian-pdf-첨부-wikilink-경로텍스트-판독-시험-2026-11-14) 기록에 있다.

추가 합성 시험에서는 Muse가 두 노트의 Obsidian wikilink 경로를 기준으로 대상 노트의 역링크 후보를 찾았다(확장자 생략·`.md` 명시 각각 한 건). 이는 작은 fixture를 훑은 결과이며 Obsidian backlinks pane/index나 전체 Vault 색인 기능과 같다고 볼 수 없다. 소비자 Muse Library의 전체 저장 한도는 공개 자료에서 찾지 못했고, Meta Model API의 저장 한도는 별도 제품이라 Muse app에 적용하지 않았다. Drive for desktop의 별도 컴퓨터 동기화에서는 Muse가 지정한 합성 폴더를 읽어 새 Markdown 결과 파일을 만들고, 켜져 있는 PC에서 자동 회수를 확인했다. PC 종료 중 회수와 실제 Vault 동기화는 시험하지 않았다. 근거는 [11월 15일 Drive 왕복 시험](../vl_worklog/20261115_M4_Muse-My-Workflow.md#google-drive-computers-읽기와-pc-자동-회수--통과), [역링크 WorkLog](../vl_worklog/20261114_M4_Muse-My-Workflow.md#obsidian-backlinks-링크-대상-탐색-시험-2026-11-14), [저장 한도 조사](../vl_worklog/20261114_M4_Muse-My-Workflow.md#muse-저장-용량-공식-문서-재확인-2026-11-14)에 있다.

추가로 실제 Vault와 같은 55,035개 파일 수를 가진 작은 합성 Markdown 트리를 Muse 내부에서 ZIP 왕복했다. 로컬에서 파일 수·payload·경로·검사 표식·ZIP integrity를 확인했다. 파일 개수 대응은 확인했지만 payload는 825,535 bytes뿐이라 64.614 GiB 전체 용량이나 형식별 실데이터를 수용하는지는 알 수 없다. 자세한 결과는 [파일 수 시험 WorkLog](../vl_worklog/20261114_M4_Muse-My-Workflow.md#muse-native-실제-vault-파일-수-대응-합성-시험-2026-11-14)와 [경로표](guides/task-route-table.md#실제-vault와-같은-파일-수의-합성-왕복-2026-11-14)에 기록했다.

2026-11-14 Dropbox의 합성 시험 폴더에서 PC 완전 종료 중 휴대폰 Muse로 만든 `pc-off-return-20261114.md`가 재시작 후 로컬 Dropbox 폴더에 나타났다. 상대 경로와 `PC-OFF-RETURN-731` 내용, 18-byte 크기와 SHA-256을 확인했다. 따라서 이 합성 폴더에서는 모바일 작성과 PC 종료 후 자동 회수를 확인했다. 실제 Vault 경로와 S0 절전, Dropbox 권한의 폴더 단위 강제는 미확인이다. [시험 WorkLog](../vl_worklog/20261114_M4_Muse-My-Workflow.md#pc-완전-종료-후-dropbox-결과-재확인--통과-2026-11-14)

## 진행 상태

실습 1에서 공식 문서와 Muse 화면을 확인했고, 실습 2에서 사본 규칙 초안과 실제 볼트 미리 보기를 실행했다. 내부 미리 보기 보고서를 검토했고, 표시된 공개 후보 3개는 사용자 승인 뒤 별도 Drive 폴더에 올려 확인했다. 이 승인은 실제 볼트 전체를 미러링하는 포괄 승인이 아니다. E · Claude Code Remote Control은 Muse 밖의 대안으로 가상 S2·S4를 시험했고, C · Google Drive는 지정 가상 폴더의 읽기·결과 작성과 PC 수동 다운로드를 확인했다. Dropbox의 2026-11-08 화면에서는 모든 동작별 권한이 **Allow**(다운로드·쓰기 권한은 Custom Allow)였다. 사용자가 기기 접근 확인창을 승인한 뒤 `Muse M4 Test - Synthetic` 개인 전용 폴더에 가상 자료 세 개를 올렸다. 업로드 뒤 폴더 범위 검색, 지정 경로 읽기, 결과 파일 작성과 PC 회수를 확인했다. 2026-11-14에는 PC 완전 종료 중 휴대폰 Muse에서 만든 새 합성 파일이 PC 재시작 후 Dropbox 폴더에 도착했다. 모바일 작성과 종료 후 회수는 합성 폴더에서 통과했다. S0 절전 효과와 폴더 범위 권한 강제는 미검증이며, 실제 Vault 경로도 시험하지 않았다.

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
- **Muse-native 합성 트리 전체의 수동 ZIP 왕복은 확인했다.** Muse 작업 공간에서 수정·추가한 파일을 포함해 네 파일을 경로와 해시를 보존한 ZIP으로 회수했다. 이는 Muse Library를 통한 수동 전달이며 로컬 Vault 자동 동기화가 아니다. 전체 Vault 크기·파일 수 한도와 PC가 꺼져 있을 때의 전체 절차는 아직 미검증이므로 S5는 자동 도착 시나리오로는 실증되지 않았다.
- **공개 표시만 담는 사본이 안전하게 동작한다.** 실제 볼트 미리 보기에서 포함 후보 3 · 제외 55,975 · 복사 0 — 내부 표식 112 · `visibility: internal` 58 은 모두 빠졌다.
- **확인 못 한 것** — Dropbox에서 실제 Vault 경로의 동기화, 폴더 범위의 기술적 강제, Windows 절전 중 새 변경 반영은 미확인이다. PC 완전 종료 후 자동 회수는 합성 폴더에서 통과했지만 실제 Vault의 S5 전체를 증명하지 않는다. 이전 Muse 화면의 403 알림은 Dropbox 요청 오류와 연결되지 않았다. Chrome 업데이트·재시작 후 현재 Muse 화면에는 알림이 보이지 않았지만, 사용자가 평소 반복된다고 보고해 해결 여부와 원인은 미확정이다. Google Drive에서는 Muse가 `Computers` 동기화 경로를 찾고 편집할 수 있는지, 새 변경이 PC로 자동 돌아오는지 확인해야 한다. Dropbox 표준 동기화가 현재 Vault 위치를 이동 없이 지원하는지도 미확인이다.

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
