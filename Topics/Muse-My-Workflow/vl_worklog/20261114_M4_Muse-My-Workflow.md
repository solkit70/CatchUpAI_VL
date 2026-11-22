---
title: "WorkLog - M4 Muse의 Vault 폴더 구조 가져오기"
author:
  - Codex
created: 2026-11-14 07:46:34
tags:
  - muse-my-workflow
  - worklog
---

## 세션 정보

**날짜**: 2026-11-14  
**모듈**: M4 볼트 연결 해법  
**진행 에이전트**: Codex  
**이전 WorkLog**: [11월 8일 WorkLog](20261108_M4_Muse-My-Workflow.md#다음-세션에-넘길-것)

## 오늘의 학습 목표

가상 Vault를 Muse 내부 작업 공간에 가져와 상대 경로와 첨부 관계가 유지되는지 확인한다. Muse 내부를 우선 시험한다. [작업별 경로표](../04-Vault-Connection/guides/task-route-table.md#vault-구조-재현과-동기화-조사)

## 진행 내용

[가상 Vault ZIP](../vl_materials/Muse-M4-Structure-20261114.zip)에 `Topics/Alpha/note.md`, `Topics/Beta/note.md`, `assets/sample.png`를 넣었다. ZIP 무결성을 검사했다. Alpha 노트는 Beta 노트와 PNG를 상대 경로로 참조한다. Alpha의 식별값은 `ALPHA-731`, Beta는 `BETA-462`다.

Muse의 새 사이드 채팅에서 파일 첨부 입력이 여러 파일 선택을 지원하는 것을 확인했다. Chrome 확장 프로그램으로 파일을 선택하는 단계는 확장 프로그램의 파일 URL 접근 권한이 꺼져 있어 실패했다. Windows 기본 파일 선택 창을 이용하려 했으나 Chrome 창 제어 승인 요청이 시간 초과됐다. 이후 사용자가 ZIP을 Muse에 첨부해 작업 공간으로 풀었고, ZIP 안 경로의 보존을 확인했다.

## DoD 진행 상태

사용자가 ZIP을 첨부한 뒤 Muse에 작업 공간으로 압축 해제를 요청했다. Library → System Files → workspace에서 `Muse-M4-Structure-20261114`의 `Topics/Alpha/note.md`, `Topics/Beta/note.md`, `assets/sample.png` 세 파일을 확인했다. Muse가 작업 공간에서 계산해 보고한 SHA-256 3개를 로컬 ZIP 항목의 SHA-256과 대조했고 모두 일치했다.

Alpha의 상대 링크 두 개가 가리키는 파일은 해당 경로에 존재했다. 채팅 답변에 인용된 이미지 링크는 `Image not found`로 표시되어 미리 보기에서의 링크 동작은 별도로 남긴다.

M4는 7/8이다. 가상 Vault ZIP의 Muse 작업 공간 가져오기와 상대 경로 보존을 확인했다. 모바일 변경분의 PC 수동 회수와 가상 Vault 반영도 통과했다. Dropbox 합성 경로의 읽기·쓰기, 충돌 수동 병합, 깨어 있는 PC 자동 회수와 PC 완전 종료 중 모바일 Muse가 만든 파일의 재시작 후 자동 회수를 확인했다. 실제 Vault 규모 적합성과 실제 Vault 경로 동기화는 여전히 검증되지 않았다. 남은 DoD는 사본 규칙 및 미리 보기 보고서의 최종 검토·승인이다.

## 모바일 변경분 회수

사용자가 휴대폰에서 요청을 처리했다고 알렸다. PC 웹의 Muse Library에서 `Topics/Alpha/note.md`의 `MOBILE-EDIT-20261114`와 새 파일 `Topics/Beta/mobile-result.md`의 `MOBILE-NEW-20261114`를 직접 열어 확인했다.

Library에서 두 파일을 개별 다운로드했다. 원래 ZIP을 임시 시험 폴더에 풀고 두 다운로드본을 원래 상대 경로에 배치했다. Alpha의 기존 본문과 상대 링크를 유지한 채 요청한 한 줄만 추가됐으며, Beta 새 파일의 내용은 요청과 일치했다. 변경 대상이 아니었던 기존 Beta 노트와 PNG는 ZIP 원본과 바이트가 일치했다.

## 같은 파일의 양쪽 수정과 최신본 회수 확인

이전 PC 다운로드본에는 `MOBILE-EDIT-20261114`가 있었고, Muse에서 해당 파일에 `MUSE-SIDE-EDIT-20261114`가 추가되었다. Library의 파일 편집 화면에서 두 표식과 기존 본문·상대 링크가 함께 보이고 파일 크기는 125 B로 표시됐다. 따라서 Muse 쪽에 최신 내용이 보존된 사실은 확인했지만, PC 다운로드본과 자동 병합되거나 충돌을 자동 해결하는 기능은 확인되지 않았다.

이후 Library 파일 편집기의 More actions → Download를 다시 실행해 최신본을 내려받았다. `Downloads/note (2).md`는 125 B이며, 파일을 읽어 모바일 표식과 Muse 측 표식, 기존 본문 및 상대 경로 링크가 모두 보존됐음을 확인했다. 앞서 잘못 내려받은 45 B 채팅 첨부본은 별개의 오래된 사본으로 판별했다. PC에서 받은 최신 파일은 로컬의 101 B 모바일 수정본보다 Muse 측 한 줄이 추가된 상태다. 두 사본의 차이를 확인했지만 자동 병합은 일어나지 않았다. 사용자가 최신본을 검토하고 로컬에 반영하는 수동 회수 단계가 필요하다.

System Files 목록에서 시험 폴더와 하위 폴더를 확인했으나, 목록 UI에서 폴더 전체 ZIP 내보내기 조작은 찾지 못했다. 당시 확인된 Library Download 동작은 파일 편집 화면의 개별 파일에 대한 것이었다. 이어서 사용자가 Muse에 기존 합성 작업 공간 전체를 ZIP으로 패키징해 Library에서 회수하도록 요청했다.

## Muse-native 전체 합성 폴더 회수 시험 (2026-11-14)

사용자가 `Muse-M4-Structure-Return-20261114.zip`을 Downloads에 전달했다. 실제 파일 크기는 2,109 bytes였고 SHA-256 `7fbe774f2cd18f607dbbe9d4d452e21f87f5a8f7fe4824ec4546082ef97dbb9b`로 사용자가 제공한 값과 일치했다. 압축 구조에는 `Muse-M4-Structure-20261114/` 루트와 `Topics/Alpha/`, `Topics/Beta/`, `assets/`가 유지됐고, 파일 네 개의 총 압축 해제 크기는 230 bytes였다.

반환 ZIP의 파일별 바이트와 SHA-256을 대조했다. `Topics/Alpha/note.md`(125 bytes)는 앞서 내려받은 125-byte Muse 최신본과 일치하며 `MOBILE-EDIT-20261114`, `MUSE-SIDE-EDIT-20261114` 두 표식과 원래 본문·상대 링크를 보존했다. `Topics/Beta/mobile-result.md`(20 bytes)는 앞서 내려받은 모바일 결과 파일과 일치했다. 변경 대상이 아니었던 `Topics/Beta/note.md`(17 bytes)와 `assets/sample.png`(68 bytes)는 원본 ZIP과 각각 SHA-256이 일치했다. 누락·경로 변경 없이 수정 파일 둘과 원본 유지 파일 둘을 하나의 ZIP으로 회수했으므로 합성 트리의 Muse-native ZIP 왕복은 통과했다.

이 결과는 Muse 작업 공간에 둔 작은 합성 트리의 일괄 수동 회수를 입증한다. Vault 전체의 파일 수·총 용량 처리 한도나 자동 동기화는 입증하지 않으며, Muse Library에서 일반 폴더 ZIP 내보내기를 직접 누르는 UI 기능과도 구분한다. 실제 Vault는 업로드하지 않았다. 반환 ZIP은 새 추출 폴더를 만들지 않고 메모리에서 확인했다.

## Vault 규모 메타데이터 확인 (2026-11-14)

전체 Vault 트리의 파일 내용은 열지 않고 파일 시스템 메타데이터만 집계했다. `.git` 내부를 제외하면 55,035개 파일, 총 69,378,578,875 bytes(64.614 GiB)였고, 이 중 `.md`는 5,777개·108,846,930 bytes(약 103.8 MiB), 다른 확장자는 49,258개였다. 파일 형식별로는 `.mp4` 498개가 50,151,983,801 bytes를 차지해 전체 용량의 대부분이었다. 이 집계는 숨김 파일을 포함한 경로 전체 기준이므로 실제 포함 허용 정책에 따른 사본 용량과는 다르다.

Meta의 사용자용 Muse 안내에서 ZIP/Library 전체 업로드 크기나 전체 작업 공간 파일 수 한도를 확인하지 못했다. Meta Model API의 파일 업로드 문서는 별도 개발자 API를 설명하므로 Muse 앱·Library 한도로 적용하지 않는다. 따라서 현재 근거로는 64.614 GiB 전체 Vault가 Muse에 들어갈 수 있는지 결론 내릴 수 없으며, 실제 파일을 업로드해 시험하지 않는다. 비-MD 형식은 사본 정책에서 제외로 고정하지 않았고, 크기와 내부 표시 기준에 따라 허용 목록을 검토해야 한다.

다음 단계의 합성 부하 시험을 위해 `vl_materials/Muse-M4-Scale-104MiB-Synthetic-20261114.zip`을 만들었다. 파일 내용은 공개 단어 목록으로 생성한 비민감 테스트 텍스트뿐이며 실제 Vault 내용이나 파일명은 포함하지 않는다. ZIP에는 합성 Markdown 5,777개가 들어 있고 압축 해제 payload는 정확히 108,846,930 bytes(103.8 MiB), ZIP 파일은 18,124,227 bytes(약 18.1 MB), SHA-256 `990642fef391311d9348c98ec06fd3283b4edcab9731c3d871478f2abf6e0461`이다. 파일 수·압축 해제 크기·경로 접두사를 생성 직후 검증했다.

사용자가 해당 합성 ZIP을 Muse에 올리고, 반환 파일 `Muse-M4-Scale-Return-20261114.zip`을 Downloads에 전달했다. 반환 ZIP은 18,437,057 bytes, SHA-256 `e1085df9fe7d495a7e3cae7d07b3f0539ebbac90215f6cbc9c26d40f7416b3de`다. Muse 반환 ZIP의 5,777개 파일과 108,846,930-byte payload를 원본 합성 ZIP과 경로별 SHA-256으로 전부 비교했다. 누락 0, 추가 0, 내용 불일치 0으로, 약 104 MiB Markdown 트리의 업로드→작업 공간 처리→전체 ZIP 회수 왕복이 통과했다. Muse가 ZIP 압축률을 바꾸었으므로 반환 ZIP의 파일 크기는 달랐지만 payload는 바이트 단위로 동일했다.

이 성공은 5,777개 작은 텍스트 파일·104 MiB payload 규모의 합성 시험에 한정된다. 비-Markdown 형식과 큰 단일 미디어 파일 처리, 실제 Vault 64.614 GiB 전체 수용, 자동 동기화는 입증하지 않는다. 실제 Vault를 Muse에 전송하지 않았다.

## 혼합 비-Markdown 합성 시험 패키지 준비 (2026-11-14)

다음 형식 확인을 위한 `vl_materials/Muse-M4-NonMarkdown-Formats-Synthetic-20261114.zip`을 만들었다. ZIP에는 합성 Python 소스 1개, JSON 1개, CSV 1개, PNG 이미지 1개, PDF 1개, 1초짜리 MPEG-4 시험 영상 1개가 들어 있다. 파일 형식 시그니처를 확인했고, 모든 내용은 합성 자료다.

압축 해제 총량은 4,822 bytes, ZIP 크기는 3,239 bytes, SHA-256은 `197b8ea6e55ca2a8410401dbadf0af84190aab3956c9d4b3822457f9d619e8cb`이다. Muse 첨부 후 압축 해제와 전체 ZIP 재회수를 통해 경로·파일별 해시를 대조할 예정이다. 아직 Muse에 업로드하지 않았다.

사용자가 반환 ZIP `Muse-M4-NonMarkdown-Formats-Return-20261114.zip`을 Downloads에 전달했다. 반환 파일은 4,557 bytes, SHA-256 `6347b394cb10a616ea7a4727d62fcb110e19ba71b92a92b0425413c2d286486f`다. 여섯 파일의 payload는 4,822 bytes로 원본과 같고, 경로별 SHA-256 비교에서 누락 0·추가 0·불일치 0이었다. PNG·PDF·MP4 시그니처를 갖춘 합성 파일 포함, 여섯 비-Markdown 형식의 Muse ZIP 왕복 바이트 보존 시험을 통과했다. 이는 ZIP 속 파일 보존을 입증할 뿐 Muse가 각 형식을 읽고 이해하거나 편집하는 능력을 입증하지 않는다.

## 보조 저장소 동기화 방식 리서치

Meta의 [Muse 생산성 소개](https://ai.meta.com/muse/productivity/)는 클라우드 저장소 연결과 Muse의 파일 정리를 안내한다. Muse의 작은 합성 작업 공간에서는 수정·신규 파일을 포함해 전체 폴더 트리를 ZIP으로 수동 회수하는 데 성공했다. 다만 공개 안내만으로 실제 Vault 규모 한도나 Muse와 로컬 Vault 사이의 자동 양방향 동기화는 확인되지 않았다. 따라서 Muse-native는 적어도 소규모 트리의 수동 일괄 회수 경로로 쓸 수 있지만, 자동화 수단이나 전체 Vault 수용 가능 여부는 한도 조사 후 판단한다.

Google Drive 도움말은 컴퓨터 폴더 동기화에 대해 이렇게 안내한다.

> “Drive changes reflect on your computer.”

`Folders from your computer → Sync with Google Drive`로 지정한 기존 폴더는 `Computers` 아래에 저장되며, 원본 위치와 Drive 간 변경이 양방향으로 반영된다고 한다. 현재 Vault 경로를 옮기지 않고 동기화할 수 있는 후보라는 점에서 Dropbox 표준 폴더 동기화보다 사용자 의도에 더 잘 맞을 가능성이 있다. 다만 Muse의 Drive 커넥터는 이전에 My Drive 합성 폴더만 시험했다. `Computers` 아래 경로에서 검색·읽기·쓰기 되는지는 아직 확인되지 않았다. [Google Drive 도움말](https://support.google.com/drive/answer/10838124?hl=en) · [Drive 스트리밍·미러링](https://support.google.com/drive/answer/13401938?hl=en)

Dropbox는 Muse 커넥터에서 합성 파일 검색·읽기·결과 쓰기를 확인했고, 깨어 있는 PC에서 Dropbox 데스크톱이 시험 폴더를 회수했다. Muse 연결 앱 권한 화면에서는 파일·폴더 전체 편집과 공유 관리가 표시되어 시험 폴더만 접근하도록 기술적으로 한정되지는 않았다. Dropbox Backup은 다음과 같이 설명된다.

> “one direction, from your device to the cloud.”

따라서 Dropbox Backup은 Vault 위치를 유지한 보관 사본용으로는 가능해도, Muse가 클라우드 사본을 수정한 뒤 PC 원본으로 되돌리는 동기화에는 부적합하다. Dropbox 표준 동기화는 양방향이지만 보통 Dropbox 폴더 내부가 동기화 기준이므로 현재 Vault 경로에서 쓸 수 있는지 혹은 원본 위치를 옮겨야 하는지 검증해야 한다. [Dropbox-Muse 커넥터](https://help.dropbox.com/integrations/connect-to-meta-muse) · [Dropbox Backup FAQ](https://help.dropbox.com/organize/dropbox-backup-faq) · [Dropbox 동기화 개요](https://help.dropbox.com/sync/sync-overview)

## Google Drive 웹 폴더 업로드와 Muse 커넥터 확인 (2026-11-14)

Google Drive for desktop을 설치하지 않고 웹의 `Folder upload`로 합성 Vault 폴더를 My Drive의 `Muse-M4-Web-Synthetic-20261114`에 업로드했다. Drive는 `1 upload complete`, `8 of 8`을 표시했고, 업로드된 `Muse-GDrive-Synthetic-20261114/Muse-M4-Structure-20261114/Topics/Alpha/note.md`, `Topics/Beta`, `assets` 경로를 웹에서 확인했다. Drive 웹 화면에는 해당 Alpha 폴더의 `note.md`가 보였다.

Muse의 Google Drive 커넥터는 이미 연결되어 있었다. 설정 화면에서 파일 접근과 개인 파일 생성 권한은 `Allow`였고, 공유될 수 있는 파일 생성은 `Ask`, 삭제·휴지통 이동·개인 파일 수정은 `Allow`였다. 권한을 변경하지 않았다. 지정된 합성 경로만 검색하도록 요청했으나 Muse는 폴더명 검색에서 결과를 찾지 못했고, Drive 웹에서 확인한 시험 폴더와 Alpha 폴더 ID를 사용한 조회도 `404 File not found`를 반환했다. 따라서 `ALPHA-731` 읽기와 결과 Markdown 생성은 완료하지 못했다.

같은 계정 여부를 확인하기 위해 Muse에 계정 연결 메타데이터만 대조하도록 요청했다. Muse는 Drive 인증 사용자 정보가 연결된 Gmail 계정 중 하나와 단일 Google Calendar 계정에 일치한다고 답했다. 현재 Drive 웹 계정의 Google Account 「Linked apps」 화면에는 Muse가 Gmail 데이터에 접근하는 항목이 보였으나 Google Drive 권한은 표시되지 않았다. 이 화면은 Muse Drive 커넥터의 계정 식별자를 직접 보여주지 않으므로 계정 일치에 대한 독립 증거로는 부족하다. [Google 계정 연결 앱 도움말](https://support.google.com/accounts/answer/13533235?hl=en-A)

메타데이터 대조 뒤 합성 파일 읽기를 재시도했지만 Alpha 폴더 ID 조회는 다시 `404 File not found`였고 부모 폴더 목록도 비어 있었다. 읽기와 별도로 시험 루트에 개인 Markdown 파일을 쓰는 요청도 실행했으나 시험 루트 ID가 `404 File not found`여서 중단됐고 파일은 생성되지 않았다. 계정 불일치 가능성은 낮아졌지만 완전히 배제되지는 않았으며, 색인 지연이나 Drive 커넥터의 폴더 가시성·범위 문제도 미해결이다. 실제 Vault 파일은 전혀 연결하지 않았고 기존 파일의 읽기·수정·공유·삭제도 없었다. 업로드 당시 Drive 저장공간은 `14.25 GB / 15 GB (94%)`로 거의 가득 참 경고가 표시됐다.

영상 제작용 증거 화면을 저장했다: [Drive 업로드와 Alpha/note.md](../04-Vault-Connection/assets/20261114-drive-web-upload-alpha-note.jpg), [Drive의 합성 Vault 루트](../04-Vault-Connection/assets/20261114-drive-web-uploaded-vault-tree.jpg), [Topics 하위 구조](../04-Vault-Connection/assets/20261114-drive-web-uploaded-topics.jpg), [Muse 커넥터의 초기 404](../04-Vault-Connection/assets/20261114-muse-drive-folder-not-found.jpg), [커넥터 권한 상태](../04-Vault-Connection/assets/20261114-muse-drive-permissions.jpg), [계정 일치 메타데이터 응답](../04-Vault-Connection/assets/20261114-muse-drive-account-match.jpg), [Google Account의 Muse Gmail 권한](../04-Vault-Connection/assets/20261114-google-muse-gmail-access.jpg), [계정 대조 뒤 읽기·쓰기 404 재시험](../04-Vault-Connection/assets/20261114-muse-drive-404-after-account-match.jpg).

**다음 시험 제안:** Muse의 혼합 파일 내용 판독을 마쳤다. 다음은 이 결과의 범위와 오류 유형을 경로표에 반영하고, 포맷별 실제 작업에 어느 정도 신뢰할 수 있는지 추가 합성 시험이 필요한지 판단한다. 실제 Vault 자료나 실제 대용량 미디어는 시험에 넣지 않는다.

## 혼합 파일 형식 내용 판독 시험 (2026-11-14)

기존 Muse 작업 공간 경로 `workspace/m4-nonmarkdown-extract-20261114/Muse-M4-NonMarkdown-20261114/`의 합성 파일 여섯 개만 대상으로 읽기 질의를 실행했다. Muse는 다른 경로에 접근하지 않았고 파일을 수정하거나 만들지 않았다고 보고했다. 아래 결과는 반환 ZIP 바이트 검증과 별개의 내용 판독 시험이며, 응답을 로컬 합성 ZIP 원본과 대조했다.

| 형식 | Muse 보고 | 원본 대조 및 판정 |
|---|---|---|
| Python | `marker()` → `SYNTH-CODE-731` | 원본 코드와 일치 |
| JSON | `fixture=synthetic-only`, `marker=SYNTH-JSON-462`, `items=[1,2,3]` | 원본과 일치 |
| CSV | `id,label,value`; 행 `1,synthetic-alpha,731`, `2,synthetic-beta,462` | 원본과 일치 |
| PDF | `SYNTHETIC PDF FIXTURE 462`를 언급했으나, 동시에 페이지가 이미지로 판정되어 텍스트로 읽지 못했다고 명시 | 정확한 PDF 텍스트 추출은 **검증 실패/불확정**. 답변의 문자열을 추출 성공으로 간주하지 않음 |
| PNG | 160×96 RGB, 파란 배경과 흰 사각 테두리; 가시 문구 `SYNTH731` | 크기·도형은 원본과 일치. 원본의 문구 `SYNTH 731`에서 공백을 누락했으므로 OCR은 근사 일치 |
| MP4 | 1.000초, 320×240, 12 fps/12 frames; 모든 프레임 단색 파랑, 텍스트·도형 없음 | 원본의 길이·해상도·프레임과 일치. 미디어를 영상처럼 재생해 본 것이 아니라 메모리에서 디코딩한 픽셀 분석이라고 Muse가 한정함 |

따라서 Muse는 합성 코드·JSON·CSV를 정확히 읽었고 PNG/MP4의 기본 속성과 단순 시각 내용을 상당 부분 설명했다. PDF는 읽기 가능성을 입증하지 못했고 PNG OCR은 공백을 보존하지 못했다. 이 표본은 작은 단순 파일 하나씩의 성능만 보여 주며 임의 PDF·이미지·영상 전반의 신뢰도를 입증하지 않는다. 전체 비-Markdown ZIP의 경로·바이트 보존 성공과도 구분해야 한다. 원본 합성 ZIP은 그대로 두었으며 실제 Vault 자료는 사용하지 않았다.

## Dropbox Muse 연결 권한 범위 확인 및 충돌 처리 리서치 (2026-11-14)

Dropbox 웹의 `Settings → Apps`에서 연결된 Muse 항목을 펼쳐 권한을 읽기 전용으로 확인했다. 표시된 권한은 Dropbox 파일·폴더 전체의 내용 보기와 편집, 파일 요청·공유 설정·협력자 관리, 계정 기본 정보 조회였다. 시험 폴더 한 곳만 허용하는 선택 항목은 이 화면에 없었다. 따라서 프롬프트에 시험 폴더만 사용하라고 제한해도 계정 연결 자체가 해당 폴더에 기술적으로 묶인 것은 아니다. Dropbox의 연결 앱 안내는 `Select Access`, `App Folder`, `Full Dropbox` 구분을 설명하지만 Muse의 상세 권한 화면은 이 중 정확히 어떤 라벨인지 보여주지 않는다. 실제로 표시된 넓은 권한을 근거로 전체 Dropbox 범위에 가까운 권한으로 취급하고, 실제 Vault를 연결하기 전에 계정 권한 범위를 별도 검토해야 한다. 권한을 바꾸거나 Muse 연결을 끊지 않았다. [Dropbox 연결 앱 권한 안내](https://help.dropbox.com/integrations/third-party-apps)

Dropbox 공식 문서에 따르면 같은 파일을 동시에 수정하거나 한쪽이 오프라인으로 수정하는 동안 다른 쪽에서 편집하면 `conflicted copy`가 생길 수 있다. Dropbox는 마지막 저장본을 그 사본으로 남기며, 두 버전은 직접 비교해 수동 병합하도록 안내한다. 이 항목을 처음 기록한 시점에는 재현 실험 전이었으나, 아래 합성 Dropbox 시험에서 실제 충돌 사본 생성과 수동 병합을 확인했다. [Dropbox 충돌 사본 안내](https://help.dropbox.com/organize/conflicted-copy)

영상 참고용으로 연결 앱의 Muse 권한 화면을 현재 세션에서 캡처해 보여 주었다. 화면 이미지는 Topic의 로컬 assets 파일로 저장되지 않았다. 공개 영상에 사용하기 전에 개인 계정 UI와 불필요한 항목을 정리한 깨끗한 캡처를 다시 만들 필요가 있다.

충돌 재현을 위해 승인된 합성 폴더의 새 경로 `Topics/Alpha/Conflict-Experiment-20261114.md`에 기준 사본을 만들었다. Muse 응답과 Dropbox 동기화 로컬 폴더에서 `BASE-VERSION-0` 및 `END-BASE` 두 줄, 24 bytes를 확인했다. 첫 시도에서는 Dropbox 일시중지 UI를 열지 못해 중단했지만, 이후 사용자가 데스크톱에서 30분 일시중지를 설정해 실험을 이어갔다. 기준 파일 생성 및 확인 화면은 대화에서 캡처했지만 로컬 asset으로 저장하지 않았다.

사용자가 Dropbox 동기화를 30분간 일시중지했다고 확인한 뒤, 로컬 합성 파일에 `LOCAL-OFFLINE-EDIT`를 추가하고 Muse 커넥터로 클라우드 원본에 `MUSE-CLOUD-EDIT`를 추가했다. 사용자가 `Resume`을 누른 뒤 Dropbox 웹과 로컬 폴더를 확인했다. Dropbox는 클라우드 원본 `Conflict-Experiment-20261114.md`(40 bytes, BASE + MUSE 표식)를 보존하고 로컬 수정은 `Conflict-Experiment-20261114 (Changsoo's conflicted copy 2026-11-14).md`(44 bytes, BASE + LOCAL 표식)로 만들었다. 두 변경을 자동 병합하지 않고 별도 conflicted copy로 보존했다.

수동 복구 단계도 합성 파일에서 확인했다. Muse 커넥터를 이용해 원본 파일에 `LOCAL-OFFLINE-EDIT`를 수동으로 추가했고, Muse가 같은 파일 ID의 59-byte 결과(BASE, MUSE, LOCAL 세 표식)를 다시 내려받아 검증했다. 그 변경은 Dropbox 동기화를 통해 로컬 원본에 돌아왔으며 로컬 파일도 같은 세 줄과 59 bytes였다. conflicted copy는 별도 44-byte 파일로 유지되어 로컬 변경 증거를 보존한다. 충돌 사본은 검토·병합 전 삭제하지 않는 절차가 안전하다는 점을 확인했다. 실제 Vault는 연결하지 않았고 다른 Dropbox 파일은 열거나 바꾸지 않았다. Dropbox 파일 목록과 Muse 병합 결과 화면은 이번 대화에 캡처했으며, 로컬 video asset으로 저장하지 않았다.

## Google Drive `Computers` 경로의 설치 전제 확인 (2026-11-14)

Google Drive 공식 도움말을 다시 확인했다. 기존 컴퓨터 폴더를 `Computers` 아래에 양방향 동기화하려면 컴퓨터에서 Drive for desktop을 열고 `Settings → Preferences → Folders from your computer → Sync with Google Drive`를 선택해야 한다. 웹에서 폴더를 업로드해 `My Drive`에 넣는 절차와는 다른 기능이다. [Google Drive for desktop 도움말](https://support.google.com/drive/answer/10838124?hl=en)

따라서 Drive for desktop 설치·설정 없이 현재 업로드된 합성 폴더만으로는 `Computers` 경로 시험을 만들 수 없다. 사용자가 앞서 데스크톱 앱은 설치하지 않는 방향을 지시했으므로 설치하지 않았고, `Computers`의 Muse 커넥터 검색·읽기·쓰기와 PC 자동 회수 시험은 진행하지 않았다. Google 공식 도움말 화면을 영상 참고용으로 현재 세션에서 캡처했다. Dropbox 표준 동기화는 별도의 합성 폴더에서 후속 검증했다.

## Dropbox 표준 동기화의 경로 제약 확인 (2026-11-14)

Dropbox 공식 도움말은 표준 동기화 파일을 Dropbox 폴더에 두고 데스크톱 앱이 계정과 다른 기기 사이에 변경을 반영하는 흐름으로 설명한다. 별도 위치의 컴퓨터 폴더를 대상으로 하는 Dropbox Backup은 PC에서 클라우드로 가는 단방향 백업이며, 백업본은 dropbox.com에서 편집할 수 없어 Muse가 수정한 내용을 원래 Vault로 되돌리는 데 쓸 수 없다. Windows에서는 junction과 symlink도 Dropbox가 지원하지 않으며, Dropbox 폴더 바깥을 가리키는 링크 대상 파일을 동기화하지 않는다고 명시한다. [Dropbox 동기화 도움말](https://help.dropbox.com/sync/check-sync-status) · [Dropbox Backup FAQ](https://help.dropbox.com/organize/dropbox-backup-faq) · [Windows junction/symlink 지원](https://help.dropbox.com/sync/symlinks)

이번 공식 자료 검토 범위에서는 현재 Vault 경로를 그대로 유지하면서 Dropbox 표준 동기화가 그 경로를 양방향으로 동기화하는 지원 절차를 확인하지 못했다. 이는 지원 경로를 찾지 못했다는 뜻이며, 다른 제품 기능의 존재 여부까지 부정하는 것은 아니다. 이미 통과한 합성 Dropbox 커넥터 읽기·쓰기 시험은 별개로 유효하지만, 사용자의 PC에 결과를 자동 회수하려면 동기화 대상이 Dropbox 데스크톱 폴더 안에 있는 구조인지 추가로 확인해야 한다. 실제 Vault 이동·새 사본 생성은 진행하지 않았다.

## Dropbox 동기화 폴더의 중첩 합성 Vault 시험 (2026-11-14)

앞서 승인된 Dropbox 합성 시험 폴더 안에 `Muse-M4-Structure-20261114`를 추가했다. 포함된 파일은 `Topics/Alpha/note.md`(80 bytes), `Topics/Beta/note.md`(17 bytes), `assets/sample.png`(68 bytes)다. Dropbox 웹 검색에서 새 하위 폴더를 찾았고, 폴더를 열어 `Topics`와 `assets` 트리를 확인했다. 이로써 로컬 Dropbox 동기화 폴더에 놓은 중첩 구조가 클라우드 Dropbox 웹에 도착한 것을 검증했다.

Muse의 Dropbox 커넥터에 해당 합성 폴더만 지정해 읽기 전용 확인을 요청했다. Muse는 `Topics/Alpha/note.md`에서 `ALPHA-731`을 읽었고 `[Beta](../Beta/note.md)` 및 `![Sample](../../assets/sample.png)` 상대 링크의 대상이 각각 `Topics/Beta/note.md`, `assets/sample.png`라고 확인했다. Dropbox 웹에서도 대상 파일들이 해당 위치에 있었다. 이미지 링크는 Muse 응답의 미리 보기에서 `Image not found`로 나타났으므로 상대 경로의 대상 확인과 Muse 미리 보기 표시는 별개로 기록한다. 기존 노트는 수정하지 않았다.

쓰기 시험은 두 위치에서 했다. Muse는 Dropbox 합성 폴더 루트에 `Muse-M4-Connector-Probe-20261114.md`를 새로 만들고 `DROPBOX-WRITE-731` 한 줄(18 bytes)을 확인했다. 이어 `Topics/Alpha/Muse-Result-20261114.md`를 중첩 경로에 만들고 `ALPHA-WRITE-731` 한 줄(끝 개행 포함 16 bytes)을 확인했다. 두 파일 모두 PC의 로컬 Dropbox 동기화 폴더에서도 같은 상대 경로와 내용으로 나타났다. 따라서 PC가 깨어 있고 Dropbox 데스크톱이 실행 중일 때 Muse가 클라우드에 쓴 루트·중첩 합성 파일이 Dropbox 웹을 거쳐 PC로 자동 회수되는 흐름을 확인했다. 실제 Vault나 기존 합성 원본은 수정하지 않았으며 공유·이동·삭제도 없었다.

이번 UI 확인 화면은 대화에서 캡처했다. 공개 영상에 쓸 때는 관련 합성 결과만 보이도록 화면을 다시 구성하고 주변 사이드바의 다른 작업 제목을 제외해야 한다. 별도의 로컬 영상 asset 파일로 저장한 캡처는 아직 없다.

## 📊 DoD 체크리스트 (M4)

- [x] 해법 8가지 확인표에 출처 종류와 날짜 기록
- [x] 시나리오 5개별 시험·미시험 결과표 작성
- [ ] 사본 규칙 승인 및 미리 보기에서 내부 표시 문서 0개 확인
- [x] 사용자 승인 범위의 합성 저장소 시험과 결과 회수 확인
- [x] 작업 종류별 경로표와 중단·되돌림 초안 작성
- [x] 실제 사본 설정·계정 정보 없이 공개 문서 정리 및 산출물 README 작성
- [x] 산출물 README 링크 확인
- [x] WorkLog와 회고 기록

**진행률: 7/8** — 현재 남은 필수 항목은 사본 규칙과 미리 보기 보고서의 사용자 검토다. M4의 저장소 시험은 실제 Vault를 사용하지 않고 계속한다.

## 🎬 영상 재료

이번 세션에서 Google 도움말의 Drive for desktop 설치 전제, Dropbox 웹의 중첩 합성 트리, Muse의 상대 링크 읽기와 루트·중첩 새 파일 작성 결과를 화면으로 캡처했다. 캡처는 현재 작업 대화에서 확인할 수 있지만 로컬 영상 asset 파일로 저장하지 않았다. 공개 영상에 쓸 때는 합성 자료만 보이는 화면을 다시 캡처하고 다른 Side chat 제목을 제외한다.

## 🎓 가르칠 때

세 단계는 서로 다르다. 로컬 Dropbox 동기화 폴더에 둔 합성 트리가 먼저 웹 Dropbox에 올라갔고, Muse 커넥터가 그 클라우드 파일을 읽고 썼으며, Dropbox 데스크톱이 Muse의 새 파일을 PC의 Dropbox 동기화 폴더로 가져왔다. 이 실험은 Dropbox 로컬 동기화 폴더에서의 왕복을 보여 주며, 원래 Vault 경로 자체가 동기화된다는 뜻은 아니다.

## Daily Retrospective

### What went well

Dropbox에 놓은 가상 Vault의 계층과 상대 링크 대상을 Muse가 읽었고, 루트와 중첩 경로에 새 파일을 만든 뒤 두 파일이 로컬 Dropbox 폴더로 돌아오는 것을 확인했다. Google Drive `Computers`가 데스크톱 클라이언트 설정을 필요로 한다는 조건도 공식 도움말로 확인했다.

### What could be improved

이번 세션 화면 캡처는 대화에 표시했지만 Topic의 로컬 assets로 저장하지 못했다. 공개 영상에는 관련 화면만 남도록 주변 Side chat 목록을 제외한 캡처를 따로 준비해야 한다.

### Insights

Dropbox 커넥터가 중첩된 폴더 구조에서 읽기와 쓰기를 수행하고, Dropbox 데스크톱 폴더가 깨어 있는 PC로 변경을 돌려주는 것은 합성 시험에서 통과했다. 양쪽에서 같은 파일을 오프라인·온라인으로 수정하면 자동 병합 없이 로컬 변경을 이름이 붙은 conflicted copy로 보존하고, 클라우드 원본은 Muse 변경을 유지했다. 두 파일을 직접 비교한 뒤 Muse로 수동 병합하자 결과가 PC로 돌아왔고 충돌 사본도 별도로 남았다. 이 검증은 합성 Dropbox 폴더에 한정되며, Muse-native 1순위나 실제 Vault 경로 동기화 결정을 대신하지 않는다.

### Tomorrow's focus

Dropbox 충돌 수동 병합, Muse-native Markdown 규모 ZIP, 혼합 비-Markdown 형식 ZIP의 경로·바이트 보존이 통과했다. 다음은 합성 코드·구조화 문서·이미지·PDF·MP4를 Muse가 실제로 읽고 설명할 수 있는지 형식별 이해 시험이다. Muse ZIP 흐름은 현재 수동 회수이며 자동 동기화가 아니다. Dropbox 권한 판단과 Drive for desktop 설치는 계속 미결·보류다.

## 다음 세션에 넘길 것

Muse-native Markdown 규모 시험과 비-Markdown 혼합 형식 ZIP의 바이트 보존 시험은 통과했다. 내용 판독에서는 코드·JSON·CSV가 정확했고 PNG의 OCR은 공백을 누락했으며 PDF 텍스트 추출은 확인되지 않았다. MP4는 기본 메타데이터와 단색 프레임 분석이 일치했다. 다음은 이런 형식별 한계를 반영해 경로표를 갱신하고, 실제 Vault 파일을 넣지 않은 채 남은 Muse 우선 조사 항목을 이어간다. Drive for desktop 설치는 사용자가 재고하기 전까지 보류한다.

## Muse 저장 파일 관리 표시 및 대규모 검색·편집 시험 (2026-11-14)

Meta 도움말 「How to manage your Muse data」(2026-11-14 확인)는 Muse가 업로드하거나 만든 파일을 `System Files`에 저장한다고 설명하며, Library → System Files에서 파일을 보고 개별 파일을 삭제할 수 있다고 안내한다. 화면에서 `System files` 루트는 폴더 트리와 각 파일의 `Name / Type / Last modified / Size` 열을 보여 주었다. 이 화면에는 전체 저장공간 사용량이나 총 한도가 표시되지 않았다. 공개된 사용자 도움말에서도 Muse 워크스페이스 총 용량 또는 전체 파일 수 제한을 확인하지 못했다. 따라서 한도 미공개는 무제한을 뜻하지 않는다. [Meta 도움말 — How to manage your Muse data](https://www.meta.com/help/superintelligence/2225571704857152/)

앞서 Muse에서 압축 해제한 합성 Markdown 5,777개를 대상으로, 로컬 원본에서 단 한 번만 등장하는 네 토큰 구절 `syntheticword0353 syntheticword0148 syntheticword1422 syntheticword0988`를 재귀 검색하도록 요청했다. Muse는 전체 5,777개 파일을 검색했다고 답했고, `Topics/Batch-001/Note-00001.md` 5번째 줄의 일치 경로와 줄을 보고했다. 로컬 합성 ZIP 전체를 별도로 검색한 결과도 해당 구절이 이 경로·한 줄에서만 발견되어 검색 결과가 맞았다. Muse가 제시한 검색 명령은 `grep -rnF`였다. 이는 5,777개 합성 텍스트 노트의 키워드 검색 가능성을 보인 한 번의 통제된 시험이며, 실제 Vault 인덱싱이나 Obsidian 링크 추론을 입증하지 않는다.

이어 동일한 합성 트리에서 `Topics/Batch-001/Note-00001.md`에만 `MUSE-SCALE-EDIT-20261115` 한 줄을 추가하고 전체 폴더를 같은 최상위 디렉터리 구조로 ZIP 반환하도록 했다. Muse는 해당 파일 크기가 18,842에서 18,867 bytes로 25 bytes 늘었다고 보고했다. 다운로드한 `Muse-M4-Scale-Edited-Return-20261114.zip`은 18,437,082 bytes, SHA-256 `331b860f4e23327b558b67d806377438d3a1d826882942eabac9c2ab3f3dc90d`였다. 로컬 원본 ZIP과 반환 ZIP을 5,777개 모든 경로의 SHA-256으로 대조한 결과, 누락 0·추가 0·변경 1이며 변경 경로는 지정한 `Muse-M4-Scale-20261114/Topics/Batch-001/Note-00001.md` 하나뿐이었다. 압축 해제 payload는 예상대로 108,846,930에서 108,846,955 bytes로 25 bytes 증가했다. Muse가 보고한 편집 파일 SHA-256 `e98c959c6f2fcee807fef66e2e92fa796d8be726aa26ae922481889d50485681`도 로컬 반환 ZIP 내부에서 일치했다. 따라서 이 규모의 합성 트리에서는 전체 검색, 한 파일 수정, 동일 경로로 전체 ZIP 회수까지 확인했다.

실제 Vault 메타데이터 집계는 55,035개 파일·64.614 GiB였고 Muse에 올린 대규모 합성 테스트는 5,777개 파일·103.8 MiB였다. 전체 Vault는 테스트 payload보다 약 637배 크고 파일 수는 약 9.5배다. 전체 크기의 대부분은 실제 MP4 498개에서 나온다. 그러므로 현재 결과는 전체 Vault 수용이나 대용량 동영상 묶음 반입을 증명하지 않는다. 실제 Vault, 실제 파일명·내용, Dropbox, Google Drive는 이번 실험에 사용하지 않았다.

**다음 단계:** 전체 Vault를 Muse에 그대로 넣을 수 있다는 결론을 보류한다. 사용자용 용량 한도가 공개되어 있지 않고 이번 테스트 크기와 전체 Vault 사이의 차이가 크므로 실제 Vault 업로드로 추측을 확인하지 않는다. M4 경로표에는 Muse 내부 파일 관리가 지속 저장·검색·편집·ZIP 회수까지 가능한 합성 검증 경로로 정리하고, 자동 로컬 동기화와 전체 Vault 용량 적합성은 미확인으로 남긴다. 이후에는 전체 복제 여부를 결정하기보다 허용된 자료를 제한해 Muse에서 원격 작업하고 집에서 결과를 가져오는 운영 경로를 기준으로 나머지 보조 저장소 비교를 이어간다.

## Obsidian 위키링크 해석·대상 편집·경로 회수 시험 (2026-11-14)

기존 fixture에는 Markdown 상대 링크만 있고 Obsidian `[[wikilink]]`가 없어, Muse 작업 공간에 새 격리 합성 fixture를 만들었다: `Muse-M4-Obsidian-Links-20261115/`. `Topics/Alpha/index.md`에는 `[[Topics/Beta/note|Beta target]]`, Beta와 Gamma 폴더에는 같은 basename `note.md`를 만들고 각각 `TARGET-BETA-731`, `DECOY-GAMMA-462`를 넣었다. 총 세 파일, 각 파일 끝 LF를 사용했다.

Muse는 `|` 앞의 `Topics/Beta/note`를 vault-relative path로 보고 `.md`를 붙여 `Muse-M4-Obsidian-Links-20261115/Topics/Beta/note.md`로 해석했다. `Beta target`은 표시 alias이며 경로가 아니라고 구분했고, 같은 basename의 `Topics/Gamma/note.md`를 링크 대상으로 잘못 선택하지 않았다. 대상 노트에만 `MUSE-WIKILINK-EDIT-731`을 추가했다. Muse가 제공한 전후 해시와 바이트 수는 index·decoy 불변을 나타냈다.

Library에서 ZIP을 다운로드해 확인했다. `Muse-M4-Obsidian-Links-20261115.zip` 크기는 1,854 bytes, SHA-256 `14c4bf247458d984a1a0367673cb375f1b67d8fca5858a6c56f60d25280cc8fc`; 세 파일 payload는 총 88 bytes이며 최상위 폴더와 모든 상대 경로가 보존됐다. ZIP 내부에서 index는 33 bytes 및 SHA-256 `d3a0c46b44301edcded7ff5f0741251e1d070e978bdb3f28bcfabbc1b52ec8d2`, Beta target은 39 bytes 및 SHA-256 `982db11d51308635c41f4102e5183df2abd06005b52daeaedff623914553eaf8`, Gamma decoy는 16 bytes 및 SHA-256 `6469bf570365a1a45bc9b4f2665331320eb319783345592e774375eef84302b6`였다. ZIP 안의 세 경로·내용은 fixture 및 Muse의 편집 결과와 일치했다.

**판정:** 아주 작은 합성 예제에서 Muse는 vault-relative Obsidian wikilink의 경로와 alias를 구분하고, 동명 노트 중 지정 폴더의 대상만 찾아 편집한 뒤 상위 트리와 경로를 보존해 반환했다. 이어진 시험에서 경로 없는 중복 basename은 모호하다고 안전하게 처리했고, 별도의 후속 fixture에서 기본 heading/block fragment 처리도 확인했다. 실제 Vault 링크 구성과 동작, 더 복잡한 fragment·임의 YAML·첨부 링크·링크 역참조(backlinks)는 검증하지 않았다. 실제 Vault 파일·내용은 사용하지 않았다.

**다음 단계:** 경로 지정·모호한 basename·기본 heading/block 처리를 작은 규모에서 확인했다. M4 경로표와 모듈 요약에 반영하며, 첨부 링크가 실제 사용상 필요하면 별도 합성 fixture로 확인한다. 전체 볼트 용량과 자동 동기화는 미확인으로 유지하며, 계속 Muse 우선으로 조사한다.

## Obsidian 모호한 basename wikilink 안전 처리 시험 (2026-11-14)

같은 이름의 노트가 두 폴더에 있을 때 경로가 없는 `[[note]]`를 어떻게 처리하는지 확인하기 위해 기존 격리 합성 fixture에 `Topics/Alpha/ambiguous-index.md` 한 개만 추가했다. 내용은 `[[note]]` 한 줄과 마지막 LF이며, Muse는 추가 전 세 파일의 SHA-256이 그대로라고 보고했다. 이 단계에서 실제 Vault나 fixture 밖 경로는 접근하지 않았다.

Muse는 `[[note]]`가 basename만 제공해 고유하게 해석되지 않는다고 판정하고 대상을 선택하지 않았다. 후보는 `Topics/Beta/note.md` (`TARGET-BETA-731`와 기존 편집 표식) 및 `Topics/Gamma/note.md` (`DECOY-GAMMA-462`) 두 개였다. 읽기 전용 판정 과정에서 파일을 수정·생성·삭제하지 않았다고 보고했다.

Muse Library에서 `Muse-M4-Obsidian-Links-Ambiguous-Return-20261114.zip`을 다운로드했다. 로컬 ZIP은 2,117 bytes, SHA-256 `9a4b5f1cdcdcb87b34376f966c471abd179e3c05e49aaddf3b4f5a47868aaa8b`로 Muse 보고와 일치했다. 압축 내부에는 최상위 `Muse-M4-Obsidian-Links-20261115/` 아래 Markdown 네 파일이 있었고 payload는 97 bytes (33 + 9 + 39 + 16)였다. index `d3a0c46b44301edcded7ff5f0741251e1d070e978bdb3f28bcfabbc1b52ec8d2`, ambiguous index `aacd908cf21d352b39fafa8c8f2f9147b3c772f24a8459fcd7183f11a388071d`, Beta note `982db11d51308635c41f4102e5183df2abd06005b52daeaedff623914553eaf8`, Gamma note `6469bf570365a1a45bc9b4f2665331320eb319783345592e774375eef84302b6`로 Muse의 보고된 해시와 일치했다.

**판정:** 이 fixture에서는 Muse가 명시 경로가 있는 vault-relative wikilink를 올바른 같은 basename 파일로 따라갔고, 경로가 없는 중복 basename 링크는 모호하다고 알리며 임의 선택을 피했다. ZIP 회수와 네 파일의 바이트·경로 확인도 통과했다. 이 모듈 시점의 검증은 기본 링크 안전 처리에 한정됐다. 후속 heading/block 시험은 다음 절에 기록했으며, Obsidian 전체 해석 규칙, alias가 없는 다양한 링크 표기, backlinks, 실제 Vault 동작을 보증하지 않는다.

**다음 단계:** 경로가 있는 링크와 중복 basename의 모호성 처리를 확인했다. heading/block 후속 결과는 다음 절에 기록했다. 남은 링크 확인은 첨부 링크가 실제 사용상 필요한 경우의 합성 시험이며, 전체 Vault 용량과 자동 동기화는 별도 미검증으로 유지한다.

## Obsidian heading·block fragment 링크 시험 (2026-11-14)

별도 격리 fixture `Muse-M4-Obsidian-Fragments-20261114/`에 세 파일을 만들었다. `Topics/Alpha/index.md`에는 `[[Topics/Beta/note#Target Heading|Heading target]]`과 `[[Topics/Beta/note#^block-731|Block target]]`을 두었다. `Topics/Beta/note.md`에는 `## Target Heading` 및 그 아래 `HEADING-731` 본문, 그리고 `BLOCK-731 ^block-731` 문단을 넣었으며, 같은 경로·basename의 혼동 여부를 볼 Gamma decoy도 만들었다. 생성 직후 세 파일은 96, 104, 19 bytes로 총 219 bytes였다.

읽기 전용 확인에서 Muse는 두 링크 모두 `Muse-M4-Obsidian-Fragments-20261114/Topics/Beta/note.md`로 해석했다. heading 링크는 정확히 `## Target Heading` 단락의 `Heading body marker HEADING-731`을 반환했고, block 링크는 `^block-731`이 붙은 `Block body marker BLOCK-731 ^block-731` 문단을 반환했다. 두 링크는 같은 노트 안의 서로 다른 fragment를 가리켰으며, `Topics/Gamma/note.md`의 `DECOY-FRAGMENT-462`는 양쪽 대상이 아니라고 구분했다.

이후 Beta 노트의 block 문단에만 `MUSE-FRAGMENT-EDIT-731`을 block ID 바로 앞에 삽입했다. Muse는 line 7만 바뀌었다고 보고했다. index는 전후 96 bytes 및 SHA-256 `c5d0e7cbb23bc4066f285cefb5e7208efa66962808cb006ad05fb45078b701f8`로 동일했고, Gamma decoy는 19 bytes 및 `c1f89ab06a94ea17bb74765ed40a3d5b63fc1348360756ba64a3cfe1ac5d20e7`로 동일했다. Beta 노트는 104 bytes / `a683fc2aa0cbcc1b8a9e24194059f02fe4d9dd4e345e33245af9747e1d08223a`에서 127 bytes / `7a9257e5a59379d2b6542ecdd01ec0b54bae64d7af11e4567d08d0e26f7cfff4`가 됐다. Muse는 삽입 문구가 Gamma와 index에 없고 나머지 Beta 줄이 byte-identical이라고 보고했다.

반환 ZIP `Muse-M4-Obsidian-Fragments-Return-20261114.zip`을 다운로드해 로컬 검사했다. 크기 2,016 bytes, SHA-256 `9a0b3ff8c740b831bc25131da61d95220658f7cf74fb7cdd3042768c8de246ea`; 세 파일 payload 합계는 242 bytes (96 + 127 + 19)였다. ZIP 내 모든 경로와 각 파일 SHA-256은 Muse 보고와 일치했다. 원본 ZIP 사본은 `vl_materials/`에 보관했다.

**판정:** 이 합성 표본에서 Muse는 `#Heading`과 `#^block-id`를 같은 노트의 서로 다른 fragment로 찾고, 지정한 block만 편집해 경로를 유지한 ZIP으로 회수했다. 이는 기본 heading/block 링크 처리의 좁은 사례 검증이다. 대소문자·공백 정규화, 중첩 heading, 여러 block 유형, 첨부 링크, backlinks, Obsidian 앱의 실제 링크 resolution과 동일함, 실제 Vault에서의 성능을 검증한 것은 아니다.

**다음 단계:** M4 경로표와 모듈 요약에 결과를 반영한다. 링크 유형 중 첨부 링크가 필요하면 별도 합성 시험으로 확인하고, 전체 Vault 적합성·자동 동기화는 미확인으로 둔다.

## Obsidian 이미지 첨부 wikilink 경로·판독 시험 (2026-11-14)

새 합성 fixture `Muse-M4-Obsidian-Attachments-20261114/`에 Markdown 두 개와 32×20 RGB PNG 두 개를 두었다. `assets/sample.png`는 빨간 바탕에 가운데 파란 10×10 사각형, `assets/Elsewhere/sample.png`는 녹색 바탕에 노란 사각형으로 만들어 같은 basename의 decoy로 썼다. index에는 임베드(`![[assets/sample.png]]`)와 일반 파일 wikilink(`[[assets/sample.png]]`)를 두고, description 노트에는 의도된 이미지 설명을 넣어 PNG 자체를 읽었는지 구분 가능하게 했다.

Muse는 두 링크를 fixture의 같은 `assets/sample.png` 대상으로 보고했고, `assets/Elsewhere/sample.png`는 다른 경로라 대상이 아니라고 설명했다. 지정 경로 PNG의 실제 헤더와 픽셀을 읽어 32×20 RGB, 빨간 모서리/바탕, 가운데 파란 10×10 사각형, 이미지 전체에 두 색만 있음을 보고했다. 결과는 description의 설명과 일치했다. Muse 채팅 화면의 원문 미리보기에서는 두 번째 bracket link가 `Direct: ]`로 보였지만, 반환 ZIP을 로컬에서 풀어 확인한 `index.md` 원시 UTF-8 바이트는 아래 두 줄을 모두 정확히 보존했다. 이 차이는 채팅 화면의 렌더링/표시에만 있었고 ZIP 파일에는 없었다.

반환 ZIP `Muse-M4-Obsidian-Attachments-Return-20261114.zip`은 2,440 bytes, SHA-256 `fb471aa49b998a931f8a92fa13ce7196f680deca0c125afdd9fac300ae2bc063`였다. 로컬 확인에서 네 파일, 총 333 payload bytes와 모든 경로가 Muse 보고와 일치했다. `index.md` 63 bytes의 SHA-256은 `cfd73de45cb288c05eca230b2caafb84431bc8002170d8e423d64b656f9935b7`; description 57 bytes `e05c88545bf963b07aa150235cfda3131c7110dfd26649e663d8b353fb82dde8`; intended PNG 108 bytes `5723dd2d25b3892d4e6c12dd7c68447e49e9d485ee881be06169a9d085a2d213`; same-basename decoy 105 bytes `d799b9fa60e95f30ea498ad4c93a6c47da00e78db0b1bb24a54e21c539783157`였다. 원본 ZIP 사본은 `vl_materials/`에 보관했다.

**판정:** 이 fixture에서 Muse는 명시된 경로의 Obsidian 이미지 임베드와 일반 파일 링크를 동일한 PNG 파일로 연결해 읽었고, 같은 basename의 다른 경로를 구분했으며, 실제 이미지 픽셀을 설명과 대조해 판독했다. 반환 ZIP에서 raw Markdown 문법·PNG bytes·상대 경로도 보존됐다. 이는 한 가지 명시 경로와 작은 PNG에서의 합성 검증이다. Vault 내 경로 우선순위 설정별 처리, Obsidian 앱과 동일한 resolve semantics, PDF/다른 첨부 종류, 링크 없는 이미지 검색, 실제 Vault 규모, 자동 동기화는 입증하지 않는다.

**다음 단계:** M4 경로표와 모듈 요약에 첨부 링크 결과와 화면/원본 차이를 반영한다. Vault 전체 규모 적합성과 자동 회수는 별도 미검증으로 유지하고, 필요하면 PDF나 경로 우선순위처럼 질문이 남는 구체 사례만 추가로 시험한다.

## Obsidian PDF 첨부 wikilink 경로·텍스트 판독 시험 (2026-11-14)

격리 합성 fixture `Muse-M4-Obsidian-PDF-20261114/`에는 `Topics/Alpha/index.md`의 `Report: ![[assets/field-note.pdf]]`, 1페이지 선택 가능한 텍스트 PDF `assets/field-note.pdf`, 그리고 같은 basename의 다른 내용 PDF `assets/Archive/field-note.pdf`를 두었다. 세 파일은 각각 35, 705, 701 bytes로 총 1,441 payload bytes였다. 지정 PDF의 텍스트는 `TITLE: FIELD NOTE ALPHA`, `BODY: PDF-TARGET-731`, `TABLE: count=17, status=ready`였고 Archive decoy에는 서로 다른 표식을 넣었다.

Muse는 임베드 링크를 fixture-relative `assets/field-note.pdf`로 해석했고, PDF 자체에서 1페이지와 세 필드를 정확히 추출했다. 링크에 `Archive/` 경로가 없으므로 같은 basename인 `assets/Archive/field-note.pdf`가 아니라 명시 경로 파일을 대상으로 구분했다. Muse가 ZIP을 Library에 제공한 뒤 다운로드한 `Muse-M4-Obsidian-PDF-Return-20261114.zip`은 2,519 bytes, SHA-256 `4fb63dbb9d9fb7fe0415c5abf9d2f501a3614790704e4b593d4cb24b0c1af4d1`로 Muse 보고와 일치했다. ZIP 내부는 세 파일과 예상 상대 경로·크기(35 + 705 + 701 bytes)였으며, 로컬 pypdf 추출 결과도 `TITLE: FIELD NOTE ALPHA\nBODY: PDF-TARGET-731\nTABLE: count=17, status=ready`로 Muse 응답과 일치했다. 원본 ZIP 사본은 `vl_materials/`에 보관했다.

**판정:** 이 작은 합성 사례에서는 Muse가 명시 경로의 Obsidian PDF embed를 따라가고, 1페이지 PDF의 선택 가능한 텍스트를 읽으며, 같은 이름의 다른 폴더 PDF와 구분했다. 기존 혼합 형식 시험에서 PDF 추출이 미검증이었던 점은 이 한 가지 PDF 케이스로 보완됐다. 스캔 PDF/OCR, 주석, 다중 페이지 및 복잡한 표, 다른 경로 우선순위, 실제 Vault는 여전히 검증하지 않았다. 실제 Vault 용량 적합성 및 자동 동기화 결론에도 영향을 주지 않는다.

**다음 단계:** M4 경로표와 요약에 이미지와 1페이지 PDF 첨부 링크 시험을 각각 작은 합성 표본의 통과로 반영한다. backlinks, 다양한 PDF 유형, 실제 Vault, Muse 내부 전체 Vault 용량 한도와 자동 동기화는 미확인으로 유지한다.

## Muse 저장 용량 공식 문서 재확인 (2026-11-14)

Meta의 소비자용 Muse 페이지는 파일 작업을 기능으로 소개하지만, 검토한 공개 페이지에서 Library/System Files의 계정별 총 저장 공간이나 전체 Vault 업로드 한도는 찾지 못했다 ([Muse for Productivity](https://ai.meta.com/muse/productivity/)). 앞서 확인한 Muse Library 화면도 파일별 크기만 보였고 총량/잔여 한도는 표시하지 않았다. 이 결과는 “한도가 없다”는 뜻이 아니라 공개된 자료로 그 한도를 판정할 수 없다는 뜻이다.

별도로 Meta Model API 공식 문서는 Files API 업로드의 파일당 1 GiB와 팀 전체 100 GiB 기본 저장 허용량을 명시한다 ([Model API file handling](https://dev.meta.ai/docs/file-handling), [Files API schemas](https://dev.meta.ai/docs/api-reference/files/schemas)). 이 용량은 API의 팀 저장소에만 적용되는 것으로 문서화되어 있으며 소비자 Muse 앱의 Library와 같다고 볼 근거가 없다. 따라서 M4의 64.614 GiB 실제 Vault 수용 여부를 이 수치로 추론하거나 실제 Muse 저장량으로 적용하지 않는다. 실제 Vault는 계속 업로드하지 않았다.

**판정:** 소비자 Muse 내부의 총 저장 용량과 ZIP 최대 크기/파일 개수 한도는 공개 자료와 UI에서 확인되지 않았다. 현재까지 검증된 Muse-native 왕복은 5,777개 Markdown 파일·103.8 MiB 합성 payload까지이며, 이는 64.614 GiB 전체 Vault 적합성을 입증하지 않는다. 저장 한도 확인을 위해 실제 Vault를 시험 대상으로 삼지 않는다.

**다음 단계:** 작은 합성 fixture에 대한 wikilink·첨부 판독을 마쳤고 공식 한도 조사에서는 소비자 Muse 한도가 불명확하다는 점을 확인했다. 남은 핵심은 안전한 증분 합성 크기 시험의 실익을 평가하고, 자동 동기화 부재/수동 ZIP 회수와 함께 Muse 우선 대안의 조건을 정리하는 것이다. 실제 Vault 사본 방식과 목적지는 모든 실험 뒤 결정한다.

## Obsidian backlinks 링크 대상 탐색 시험 (2026-11-14)

격리 합성 fixture `Muse-M4-Obsidian-Backlinks-20261114/`에는 대상 `Topics/Shared/target.md`, 링크를 거는 두 source 노트(`Topics/Alpha/source.md`, `Topics/Beta/source.md`), 그리고 링크 없는 `Topics/Gamma/decoy.md`를 두었다. 두 source의 wikilink는 각각 extensionless `[[Topics/Shared/target|Target]]` 및 `.md`가 명시된 `[[Topics/Shared/target.md|Beta target]]`이었다. Muse는 총 네 파일을 만들었다고 보고했다.

읽기 전용 역방향 탐색에서 Muse는 fixture 안의 두 raw `[[...]]` 링크를 따라가 모두 `Topics/Shared/target.md`를 가리킨다고 찾았다. 다른 두 파일은 target heading/marker를 자체 본문에 포함하거나 decoy marker만 담고 있었으며 target을 가리키는 wikilink가 없다고 구분했다. Muse는 표시 alias나 `Target` 일반 단어를 찾는 것이 아니라 링크 구문 내부의 경로를 비교했다고 설명했다.

Library 반환물 `Muse-M4-Obsidian-Backlinks-Return-20261114.zip`은 로컬 Downloads에서 2,434 bytes, SHA-256 `16afcccdd65b31f9eb61687abc6938ae1cf34008291dcbcf49118ca27b3e52ac`로 Muse 보고와 일치했다. 내부에는 Markdown 네 파일, 125 payload bytes와 기대한 top-level/상대 경로가 있었다. 각 entry byte 수는 target 34, Alpha source 32, Beta source 40, Gamma decoy 19였다. 원본 ZIP 사본은 `vl_materials/`에 보관했다.

**판정:** 이 작은 fixture에서 Muse는 두 종류의 경로 표기(확장자 생략 및 `.md` 명시)를 이용해 대상 노트의 역링크 후보 두 개를 찾아내고, 단순 alias/단어·자기 marker 검색과 구분했다. 이는 텍스트 fixture를 검색해 backlink를 복원한 사례다. Muse에 Obsidian의 backlinks pane이나 실제 Vault의 전체·변경 감지 기반 역링크 색인이 있음을 증명하지 않는다. 다른 링크 형식, 깨진 링크, heading/block fragment를 포함한 역링크, 대규모 fixture, 실제 Vault는 이 시험에서 다루지 않았다.

**다음 단계:** 합성 경로·alias·ambiguity·heading/block·PNG/PDF 첨부·backlink 탐색 시험을 한/영 M4 경로표와 요약에 반영한다. 소비자 Muse 저장 용량은 공식 수치가 확인되지 않았고 API 한도와 구별해야 한다. 전체 Vault 용량 적합성 및 자동 동기화는 여전히 미확인이다.

## Muse-native 실제 Vault 파일 수 대응 합성 시험 (2026-11-14)

전체 Vault를 올리지 않고 파일 수 처리만 분리해 확인하기 위해 실제 Vault 총 파일 수와 같은 55,035개의 작은 Markdown 파일을 `Muse-M4-File-Count-20261114/` 합성 트리에 만들었다. `Notes/Batch-001/`부터 `Batch-054/`까지 각 1,000개, `Batch-055/`에 1,035개를 두고 모든 파일에 경로와 맞는 고유한 ASCII 표식 한 줄을 넣었다. 마지막 파일 `Notes/Batch-055/note-1035.md`는 `COUNT-VERIFICATION-55035`와 LF 한 개로 25 bytes였다. Muse는 총 55,035개, 825,535 payload bytes, 중복 0, pattern mismatch 0이라고 보고했다.

Muse는 모든 파일과 고유 표식을 다시 확인한 뒤 파일 수정 없이 ZIP을 만들었다. 다운로드한 `Muse-M4-File-Count-Return-20261114.zip`은 14,045,667 bytes, SHA-256 `c522fd8abf4ffb4b30ee37d9a0bc556bb681bc73c56127a483f3f7d08b95b9b0`였다. 로컬 ZIP 검사에서도 regular file 55,035개(모두 `.md`), 총 payload 825,535 bytes, ZIP entry 55,092개(상위/Batch 디렉터리 entry 57 포함), CRC integrity 검사 통과, 첫·마지막 상대 경로와 marker가 든 단일 마지막 파일을 확인했다. Muse가 보고한 ZIP byte size·SHA-256과 일치했고, ZIP 사본을 `vl_materials/`에 보관했다. 압축률이 낮아 ZIP 크기가 payload보다 커졌으며 이는 파일별 ZIP 헤더·중앙 디렉터리 오버헤드를 포함한다.

**판정:** Muse는 작은 파일 55,035개를 하나의 폴더 트리로 만들고 검색/검증한 뒤 ZIP 왕복할 수 있었다. 이 시험은 실제 Vault의 파일 개수와 동일한 수를 다뤄 파일 개수 병목을 부분적으로 점검했지만, payload는 825,535 bytes뿐이다. 따라서 64.614 GiB 실제 전체 Vault의 크기 수용성, 비-Markdown 대용량 파일과 실제 이름/폴더 분포, Muse 계정 저장 한도는 여전히 확인하지 못했다. ZIP 반송은 수동이며 자동 동기화를 검증하지도 않는다.

**다음 단계:** M4 경로표와 한/영 요약에 파일 개수 시험을 반영한다. 남은 핵심은 전체 payload 용량이 공개되지 않은 소비자 Muse Library에서 얼마나 수용되는지이며, 실제 Vault를 올리지 않고는 확정할 수 없다. 작은 합성 크기를 무리하게 누적하기보다 현재 증거의 경계와 수동 회수 방식을 명확히 한 뒤, 실제 사본 정책·목적지는 사용자가 실험 결과를 검토한 후 결정한다.

## PC 완전 종료 중 Dropbox 결과 회수 — 로컬 확인 (2026-11-14)

> 예 컴퓨터 꺼진 상태에서 Muse 에서 작업 진행 하고 컴퓨터도지금 다시 켰습니다.

사용자는 PC가 꺼진 동안 휴대폰 Muse에서 작업을 진행한 뒤 PC를 다시 켰다고 보고했다. PC 재시작 후 기존 Dropbox 동기화 폴더 `C:\Users\dougg\Dropbox\Muse M4 Test - Synthetic`에서 안내한 시험 파일 `pc-off-return-20261114.md`를 확인하지 못했다. 합성 시험 폴더의 파일 목록과 Markdown 텍스트에서도 표식 `PC-OFF-RETURN-731`을 찾지 못했다. 기존 최신 항목은 이전 구조·충돌 시험 파일이었고 이번 시험 표식은 없었다.

**판정:** 아직 미확정이다. 파일이 Dropbox에 저장되지 않았는지, 다른 경로·이름으로 저장됐는지, Dropbox 동기화가 완료되지 않았는지 Muse 저장 확인 및 Dropbox 상태 화면을 받지 못해 구분할 수 없다. S5는 계속 부분 검증으로 둔다. 추가 파일을 만들거나 실제 Vault에 복사하지 않는다.

**다음 단계:** 휴대폰 Muse의 저장 성공 응답에 적힌 전체 경로와 파일명을 확인하고, PC에서 Dropbox 앱의 동기화 완료 상태를 확인한다. Muse가 성공을 확인한 경로에 파일이 존재하지만 PC에 없으면 해당 화면을 캡처해 동기화 상태를 재확인한다. 저장 실패 또는 경로 오류라면 그 응답을 기록하고 이번 결과를 미통과로 분류한다.

## PC 완전 종료 후 Dropbox 결과 재확인 — 통과 (2026-11-14)

> 예 컴퓨터 꺼진 상태에서 Muse 에서 작업 진행 하고 컴퓨터도지금 다시 켰습니다.

최초 로컬 검사에서는 안내한 파일이 보이지 않았다. 후속 검사에서 Dropbox 동기화 폴더 `C:\Users\dougg\Dropbox\Muse M4 Test - Synthetic\pc-off-return-20261114.md`가 나타났다. 파일 크기는 18 bytes이고 내용은 `PC-OFF-RETURN-731` 뒤 LF 한 개(바이트 `0A`)였으며 SHA-256은 `DD753DDCF1DA01EADC5E50A23CA64C7B6708C882AC38806C0E718D74F94A307D`였다. 파일 수정 시각은 로컬 기준 2026-11-14 18:41:45다. 사용자는 완전 종료 중 휴대폰 Muse에서 작업하고 PC를 다시 켰다고 확인했다.

**판정:** PC가 꺼져 있는 동안 휴대폰 Muse에서 Dropbox 시험 폴더에 만든 합성 파일이 PC 재시작 후 로컬 Dropbox 동기화 폴더에 도착했고, 요청한 상대 경로와 내용이 맞았다. 따라서 Dropbox의 이 합성 경로에서 PC 완전 종료 중 작성 → 재시작 후 자동 회수를 확인했다. 실제 Vault 경로, 하루 동안의 예약/백그라운드 시나리오, Muse-native 자동 로컬 동기화는 여전히 미검증이며 Dropbox 폴더 권한의 기술적 제한도 확인하지 않았다. 화면 캡처는 제공되지 않아 영상용 증거는 남기지 못했다.

**다음 단계:** M4 시나리오 표와 작업 경로표를 갱신한다. Dropbox 자동 회수는 합성 폴더 범위에서 PC 종료 구간까지 통과로, S5 전체는 실제 Vault 경로와 운영 조건 미검증으로 부분 상태를 유지한다. 실제 사본 규칙·목적지·권한·주기는 실험 전체를 검토한 뒤 결정한다.

## Google Drive `Computers`와 API 문서 범위 조사 (2026-11-14)

Google Drive for desktop 도움말은 기존 로컬 폴더를 `Folders from your computer → Sync with Google Drive`로 설정해 `Computers` 아래에 양방향 동기화하는 절차를 안내한다 ([Google Drive for desktop 도움말](https://support.google.com/drive/answer/10838124?hl=en)). 별도로 Google Drive API의 파일 개요는 API가 다루는 corpus를 `user`, `domain`, `drive`, `allDrives`로 열거하며, `user`는 My Drive와 사용자에게 직접 공유된 파일이라고 설명한다 ([Drive API 파일·폴더 개요](https://developers.google.com/workspace/drive/api/guides/about-files)).

> “The corpora for Drive are: `user`, `domain`, `drive`, and `allDrives`.”

**판정:** 확인한 API 문서는 Drive for desktop의 `Computers` 화면 항목과 Muse 커넥터의 접근 가능 여부를 명시하지 않는다. 이는 API에 해당 항목이 없거나 Muse가 접근할 수 없다는 증거가 아니다. Drive `Computers` 경로를 확인하려면 Drive for desktop 설치 및 PC 폴더 연결이 필요하고, 사용자는 앞서 설치를 보류했다. 따라서 이번 단계에서는 추가 설치나 업로드 없이 미검증으로 유지한다. Dropbox PC 종료 후 모바일 Muse 파일 회수는 이미 합성 폴더에서 통과했으므로, 현재 직접 검증된 보조 경로는 Dropbox 합성 폴더다. 실제 Vault 경로·권한 범위는 별도 미결정이다.

## Google Drive for desktop 설치 및 합성 `Computers` 폴더 동기화 (2026-11-14)

사용자가 Drive for desktop을 설치해 `Computers` 경로 시험을 이어가기로 했다. Google 공식 설치 프로그램을 내려받고 Authenticode 서명이 `Valid`, 서명자가 `Google LLC`임을 확인했다. Drive for desktop 133.0.2.0 설치 후 앱을 실행했다. 설정 중 Documents, Desktop, Downloads 기본 선택을 해제하고 공개 합성 자료만 든 `Ingest/CatchUpAI_VL/Topics/Muse-My-Workflow/04-Vault-Connection/examples/trial-vault/`만 선택했다. 실제 Vault 전체 폴더나 개인 폴더는 선택하지 않았다.

Google Drive 데스크톱 앱의 Sync activity 화면에는 `Up to date` 및 `Synced less than a minute ago`가 표시됐다. `planning-brief.md` 609 bytes, `continuation-note.md` 544 bytes, `event-catalog.md` 697 bytes가 모두 `Successfully uploaded`로 표시됐다. 앱은 `trial-vault`와 `My PC` 항목도 보여 주었다. 이는 해당 합성 폴더의 Drive 동기화 완료를 입증한다. 아직 Muse 커넥터가 `Computers` 아래의 `My PC/trial-vault`를 검색·읽기·쓰기 할 수 있는지 시험하지 않았다.

> “Up to date” · “Successfully uploaded”

완료 화면은 영상용 캡처로 [20261114-google-drive-desktop-sync-complete.png](../04-Vault-Connection/assets/20261114-google-drive-desktop-sync-complete.png)에 보관했다.

**판정:** Drive for desktop 설치와 사용자가 지정한 합성 폴더의 PC→Drive 동기화는 통과했다. 이 확인만으로 Muse의 Drive `Computers` 접근성이나 Muse→PC 변경 회수를 판정할 수 없다. 추가 파일이나 실제 Vault 자료를 Drive에 올리지 않는다.

**다음 단계:** 다음 세션에서 휴대폰 Muse의 기존 Google Drive 커넥터에 `Computers/My PC/trial-vault`에서 세 Markdown 파일을 찾고 읽도록 요청한다. 읽기 전용 확인이 통과하면 같은 합성 폴더에 새 결과 Markdown을 쓰게 하고, Drive for desktop이 그 파일을 원래 PC 폴더로 되돌리는지 경로·내용·해시로 대조한다. Muse가 `Computers`에 접근하지 못하면 오류와 실제 커넥터 검색 범위를 기록한다.
