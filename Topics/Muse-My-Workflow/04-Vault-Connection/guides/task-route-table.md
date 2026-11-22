---
title: "작업 종류별 Muse·볼트 경로표 초안"
author:
  - Codex
created: 2026-11-08 15:38:59
tags:
  - muse-my-workflow
  - task-routing
  - draft
---

## 상태와 범위

[English](task-route-table.en.md)

**검토에서 정한 방향.** 원격 작업은 Muse 내부를 우선한다. Vault 폴더 구조를 Muse에 재현하는 방법부터 시험하고, 필요하면 Dropbox와 Google Drive를 보조 경로로 비교한다. 이메일은 결과 회수의 마지막 수단이다. 실제 Vault 자료의 사본 범위와 동기화 방식은 실험 후 정한다.

## 작업별 경로

| 작업 | 사용할 경로 또는 실험 순서 | 확인 결과와 남은 검증 |
|---|---|---|
| 음성 메모를 원문으로 보존 | 받아 적은 원문을 Muse 내부에 Markdown으로 저장한다. 귀가 후 아래 순서로 회수하고, 원문을 확인한 뒤 Vault의 `_Inbox_/`에 반영한다 | Vault 자동 동기화와 Journal 자동 반영은 미검증 |
| 이메일·일정 확인 | 이미 연결된 메일 및 Google Calendar를 사용해 Muse에서 직접 처리한다. 로컬 보관이 필요한 내용만 Markdown 파일로 저장하고, 귀가 후 Vault에 추가한다 | 메일·일정 전체를 로컬에 복사할 필요는 없다. 외부 발송·일정 변경은 앱 확인 절차를 따른다 |
| 밖에서 시작한 Topic을 집에서 이어가기 | Muse Library에서 M2/M3 인계 꾸러미를 내려받아 로컬 Vault에서 이어간다 | M3에서 폴더 구조를 유지해 Markdown 3개를 가져오고 Codex가 작업을 이어받았다 |
| AI로 실제 볼트 자료 검색·편집 | 1순위는 Muse 내부에서 작업하고 Library에서 결과를 회수하는 방식이다. 2순위 보조 경로는 Muse 커넥터가 접근할 수 있는 클라우드 폴더다. 전체 Vault 재현·자동 동기화는 별도 검증한다 | Muse에 합성 ZIP을 가져올 때 상대 경로가 보존됐다. Muse에서 수정한 중첩 파일과 새 파일을 포함해 폴더 전체를 ZIP으로 패키징한 뒤 귀가 후 회수했고, 경로와 4개 파일 SHA-256을 검증했다. 작은 합성 트리의 수동 전체 ZIP 왕복은 통과했지만 Vault 전체 용량 한도와 자동 Muse-native 동기화는 미검증. Dropbox 표준 동기화 폴더의 중첩 합성 Vault에서 읽기·쓰기·깨어 있는 PC 회수·충돌 후 수동 병합을 확인했고, PC 완전 종료 중 휴대폰 Muse가 만든 새 시험 파일도 PC 재시작 후 같은 경로·내용으로 도착했다. 이는 실제 Vault 경로 동기화가 아니다. 중첩 My Drive 웹 업로드 시험에서는 404가 나왔다. 이후 별도의 `Computers → My PC → trial-vault` 합성 폴더에서는 Muse 읽기·쓰기 및 PC 자동 회수가 통과했다 |
| Muse 결과를 집 PC에서 회수 | ① Muse Library에서 필요한 개별 파일 또는 합성 폴더 ZIP 회수 후 검토·수동 편입 ② 자동 회수가 필요하면 Drive 또는 Dropbox의 양방향 동기화 경로를 시험 ③ 두 경로 모두 어려울 때만 이메일 | Muse Library 개별 파일 및 작은 중첩 합성 트리 ZIP 회수를 검증했다. Dropbox 표준 동기화 폴더에서는 깨어 있는 PC 회수에 이어 PC 완전 종료 중 휴대폰 Muse가 만든 `pc-off-return-20261114.md`도 재시작 후 도착했다. 파일은 18 bytes, 내용 `PC-OFF-RETURN-731`+LF, SHA-256 `DD753DDCF1DA01EADC5E50A23CA64C7B6708C882AC38806C0E718D74F94A307D`였다. 이는 Muse-native 수동 회수와 Dropbox 합성 폴더 자동 회수의 구분을 확인한 결과이며 실제 Vault 위치는 시험하지 않았다. Drive의 합성 `trial-vault`에서는 Muse가 만든 Markdown 한 개가 켜져 있는 PC에 자동으로 도착했다. Dropbox Backup은 단방향이라 Muse 변경의 복귀에 부적합 |
| 볼트 사본 자동화 | 구조 보존과 변경분 회수 실험 뒤 자동화 가능 범위를 정한다 | 같은 상대 경로로 새 파일과 수정본을 반영하고, 같은 파일을 양쪽에서 수정한 경우를 확인한다. 실제 외부 사본에는 사본 규칙을 적용한다 |

## PC 완전 종료 시험 — 절차와 결과 (2026-11-14)

Dropbox의 깨어 있는 PC 동기화는 확인했지만, 완전히 꺼진 PC 구간의 동작은 아직 확인하지 않았다. 다음은 이미 허가된 `Muse M4 Test - Synthetic` 합성 폴더만 사용한다. 실제 Vault, 새 공유, 새 권한 연결, Dropbox Backup은 사용하지 않는다.

1. PC가 켜져 있을 때 Dropbox가 최신 상태인지 확인한다. 시험 폴더의 기존 파일은 바꾸지 않는다.
2. PC를 Windows의 절전이 아닌 **완전 종료** 상태로 둔다.
3. 휴대폰 Muse에서 기존 Dropbox 연결을 사용해 시험 폴더에 새 Markdown 파일 `pc-off-return-20261114.md`를 만들고 본문에 고유 표식 `PC-OFF-RETURN-731`을 넣는다. Muse가 저장 성공을 확인할 때까지 기다린다.
4. PC를 켜고 Dropbox 앱이 실행된 뒤 동기화 완료를 확인한다. 로컬 시험 폴더에서 같은 경로·파일명·표식이 나타나는지 확인한다.
5. Muse에 저장된 파일과 PC 회수본의 경로·내용을 비교한다. 새 파일이 돌아오지 않거나 내용이 다르면 추가 변경을 멈추고 원인을 기록한다.

**결과 (2026-11-14): 통과.** `pc-off-return-20261114.md`가 PC 재시작 후 지정된 Dropbox 합성 폴더에 나타났고 경로·내용·SHA-256을 확인했다. 이 결과도 Dropbox 합성 폴더 경로만 검증하며 실제 Vault 위치나 Muse-native 자동 동기화를 뜻하지 않는다. S5 전체 판정은 실제 Vault 경로와 일상 운영 조건이 남아 있어 부분으로 유지한다. 상세는 [M4 WorkLog](../../vl_worklog/20261114_M4_Muse-My-Workflow.md#pc-완전-종료-후-dropbox-결과-재확인--통과-2026-11-14)를 참조한다.

## M5에서 확인한 실제 업무 회수 경로

승인된 Dropbox 경로에서 행사 결과 두 파일이 로컬 Dropbox에 도착했다. PC에서 직접 열어 본 뒤 필요한 수정과 함께 원본 Vault의 업무 폴더에 수동 편입했다. 공개 영상 글은 Muse 편집기에서 회수해 해당 글 폴더에서 원어 자막을 대조했다. [M5 일상 사용 가이드](../../05-Daily-Use-Guide/guides/daily-use-guide.md)

## 멈춤과 되돌림

실험 중 결과가 누락되거나 내용이 다르면 Vault 반영을 멈추고 Muse 결과와 회수본을 대조한다. 시험 사본은 원인을 확인할 때까지 보관한다.

실제 운영의 재시도·복구 절차와 외부 사본 정리 기준은 실험 결과를 바탕으로 정한다.

## 원격 작업과 결과 회수 순서

원격 작업 파일은 Muse 내부에서 관리한다. 귀가 후 Vault에 반영하는 데 필요한 결과는 우선 Muse에서 회수한다. 이 경로로 회수가 어려울 때 Google Drive와 Dropbox를 비교해 보조로 쓰고, 두 경로 모두 어려울 때 이메일로 전달한다.

## Vault 구조 재현과 동기화 조사

Meta 도움말은 Muse에서 파일을 업로드하고 작업 공간의 파일을 생성·편집할 수 있다고 설명한다. M3에서 Muse가 만든 하위 폴더와 Markdown 파일의 개별 다운로드를 확인했고, M2의 전체 데이터 내보내기 ZIP에는 작업 공간의 상대 경로가 유지됐다. 2026-11-14 확인한 도움말에서는 로컬 폴더 트리 일괄 가져오기, Vault 규모의 파일 수·용량 한도, Windows Vault와의 변경분 자동 동기화 방법을 찾지 못했다. [Meta 파일 도움말](https://www.meta.com/help/superintelligence/2074655449783957/) · [Meta 데이터 내보내기](https://www.meta.com/help/superintelligence/2225571704857152/) · [M2 회수 실험](../../02-Muse-to-Vault/guides/transfer-comparison.md)

1. **Muse 내부부터 시험한다.** 하위 폴더, 같은 이름의 노트, 링크와 첨부를 넣은 가상 Vault로 폴더 업로드 또는 ZIP 가져오기가 되는지 확인한다. 가져온 트리를 추가 폴더 생성이나 경로 재지정 없이 사용할 수 있는지 확인한다.
2. **변경분 회수를 확인한다.** 집 PC를 끈 상태에서 휴대폰으로 기존 노트를 수정하고 새 노트를 만든다. PC를 켠 뒤 같은 상대 경로로 변경분을 회수할 수 있는지, 양쪽에서 수정한 파일을 어떻게 처리하는지 확인한다.
3. **보조 경로를 비교한다.** Drive for desktop의 합성 `trial-vault`에서 Muse가 세 파일을 읽고 새 Markdown 한 개를 만들었으며, 켜져 있는 PC에서 자동 회수했다. Dropbox 표준 동기화 폴더에서 Muse의 읽기·쓰기와 PC 회수를 합성 중첩 트리로 확인했다. 실제 Vault 경로 자체의 동기화는 입증하지 않았다. 상세 근거와 남은 시험은 아래 [보조 저장소 비교](#보조-저장소-비교-업데이트-2026-11-14)에 기록했다.

## 보조 저장소 비교 업데이트 (2026-11-14)

Meta의 Muse 소개는 클라우드 저장소 연결과 파일 정리를 안내하지만, 공개 도움말은 Vault 크기 제한이나 Muse 저장공간과 로컬 Vault 사이의 자동 양방향 동기화를 설명하지 않는다. Muse 내부 경로는 폴더 구조를 ZIP으로 가져오고 파일별로 회수하는 데는 유효하지만, 최신 파일 회수와 폴더 전체 내보내기는 별도 단계다. 같은 파일이 두 쪽에서 바뀌면 Muse가 자동 병합하지 않는 실험 결과가 나와 수동 검토가 필요하다. [Muse 파일 도움말](https://www.meta.com/help/superintelligence/2074655449783957/) · [Muse 생산성 소개](https://ai.meta.com/muse/productivity/)

Dropbox는 Muse 커넥터를 통해 파일을 읽고 쓸 수 있다. Dropbox 계정의 연결 앱 설정에서 Muse 권한을 확인했더니 파일·폴더 전체의 내용 편집과 파일 요청·공유 설정·협력자 관리 권한이 표시됐다. 이 설정에는 시험 폴더 한 곳으로 기술적으로 제한하는 항목이 없었다. Dropbox 문서는 Select Access·App Folder·Full Dropbox 구분을 설명하지만 Muse 화면은 정확한 권한 라벨을 표시하지 않아 전체 Dropbox에 가까운 넓은 권한으로 취급해야 한다. 프롬프트로 작업 경로를 제한하는 것만으로 계정 권한이 좁아지지는 않는다. 권한 변경이나 연결 해제는 하지 않았다. [Dropbox 연결 앱 권한 안내](https://help.dropbox.com/integrations/third-party-apps)

Dropbox 표준 동기화는 Dropbox 폴더 안의 파일을 클라우드·기기 사이에 반영하므로 기존 Vault 경로를 그대로 쓸 수 있는지 또는 Vault 이동이 필요한지 추가 검토해야 한다. Dropbox Backup은 임의 폴더를 클라우드에 백업할 수 있지만 단방향이고 백업 사본은 Dropbox 웹에서 편집할 수 없다고 안내하므로 Muse 편집 결과를 로컬 원본에 되돌리는 통로로는 부적합하다. [Dropbox-Muse 커넥터 안내](https://help.dropbox.com/integrations/connect-to-meta-muse) · [Dropbox Backup FAQ](https://help.dropbox.com/organize/dropbox-backup-faq) · [Dropbox 동기화 상태](https://help.dropbox.com/sync/check-sync-status)

추가로 공식 안내를 확인했다. 표준 동기화는 Dropbox 폴더 안의 파일을 동기화하는 흐름이며, Windows의 junction·symlink는 지원되지 않는다. Dropbox Backup은 외부 폴더를 고를 수 있지만 단방향이고 클라우드 백업본을 편집할 수 없다. 확인한 공식 자료에는 현재 Vault 경로를 유지하면서 그 폴더 자체를 Dropbox 표준 동기화하는 절차가 없었다. 이는 문서에서 지원 절차를 찾지 못했다는 뜻이며, 미확인 기능 전체를 부정하는 판정은 아니다. 실제 Vault 이동이나 별도 사본 생성을 통한 연결 시험은 하지 않았다. [Dropbox 동기화하기](https://help.dropbox.com/sync/check-sync-status) · [Dropbox Backup FAQ](https://help.dropbox.com/organize/dropbox-backup-faq) · [Windows junction/symlink 정책](https://help.dropbox.com/sync/symlinks)

Google Drive for desktop은 기존 컴퓨터 폴더를 `Folders from your computer → Sync with Google Drive`로 선택할 수 있다. 공식 안내상 폴더는 `Computers` 아래에 나타나고 컴퓨터 폴더와 Drive 사이의 변경은 서로 반영된다. Drive API 문서는 `user`, `domain`, `drive`, `allDrives` corpus를 열거하지만 `Computers` 화면 경로나 Muse 커넥터의 접근 여부를 설명하지 않는다. 따라서 그 API 문서만으로 접근 가능/불가를 추론할 수 없다. 11월 14일에는 합성 `trial-vault`의 PC→Drive 동기화를 확인했다. 11월 15일에는 Muse가 `Computers → My PC → trial-vault`의 원본 세 개를 읽고 같은 위치에 새 Markdown 한 개를 만들었다. PC에서 회수한 76바이트와 SHA-256이 Muse가 확인한 값과 일치했다. PC 종료 중 회수와 실제 Vault 동기화는 미검증이다. [11월 15일 WorkLog](../../vl_worklog/20261115_M4_Muse-My-Workflow.md#google-drive-computers-읽기와-pc-자동-회수--통과) [Google Drive for desktop 안내](https://support.google.com/drive/answer/10838124?hl=en) · [Drive API 파일·폴더 개요](https://developers.google.com/workspace/drive/api/guides/about-files) · [Drive 동기화·미러링 설명](https://support.google.com/drive/answer/13401938?hl=en)

**혼합 형식 판독·대규모 검색/편집·Obsidian wikilink 결과 (2026-11-14):** 여섯 비-Markdown 표본에서 Python·JSON·CSV는 정확했다. PNG는 160×96 크기와 도형을 맞혔지만 `SYNTH 731`의 공백을 누락했고, MP4의 길이·해상도·단색 프레임 분석은 일치했다. PDF는 별도 1페이지 합성 시험에서 명시된 `![[assets/field-note.pdf]]`를 따라가 선택 가능한 텍스트의 TITLE·BODY·TABLE 세 필드를 정확히 추출하고 같은 basename의 Archive decoy와 구분했다. 반환 ZIP은 3파일·1,441 payload bytes, 2,519 bytes였고 SHA-256 `4fb63dbb9d9fb7fe0415c5abf9d2f501a3614790704e4b593d4cb24b0c1af4d1` 및 로컬 pypdf 추출이 Muse 보고와 일치했다. 이는 한 페이지 텍스트 PDF 사례에 한정되며 스캔/OCR·주석·복잡한 표·다중 페이지는 미검증이다. 별도 5,777개 Markdown 합성 트리에서 Muse가 전체 파일을 검색해 원본상 유일한 4단어 구절의 경로·줄을 맞혔다. 지정한 노트 한 개를 편집해 전체 트리를 ZIP으로 돌려준 결과, 로컬 해시 대조에서 경로 누락·추가 없이 정확히 한 파일만 바뀌었고 증가량 25 bytes가 요청과 일치했다. Obsidian fixture에서 `[[Topics/Beta/note|Beta target]]`는 같은 basename의 Gamma 노트가 아닌 Beta로 해석됐고, 경로 없는 중복 `[[note]]`는 두 후보를 제시한 뒤 모호하다고 판정해 대상을 선택하지 않았다. 별도 fixture에서 `[[Topics/Beta/note#Target Heading|Heading target]]`은 `## Target Heading`의 본문으로, `[[Topics/Beta/note#^block-731|Block target]]`은 `^block-731` 문단으로 해석됐다. 두 링크가 동일한 Beta 노트 안의 서로 다른 fragment로 이어지는 것을 확인했고, 지정 block 줄만 편집해 3파일·242 payload bytes ZIP으로 반환했다. 반환 ZIP 크기 2,016 bytes, SHA-256 `9a0b3ff8c740b831bc25131da61d95220658f7cf74fb7cdd3042768c8de246ea`는 로컬 결과와 일치했으며 파일 경로와 해시도 보존됐다. 이미지·한 페이지 PDF 첨부 링크와 작은 fixture의 backlink 경로 탐색을 확인했다. 실제 Vault와 전체 Vault 링크 색인은 시험하지 않았다. 전체 Vault 연결은 입증되지 않았으며 64.614 GiB는 103.8 MiB Markdown 합성 payload보다 약 637배 크고 파일 수도 약 9.5배여서 용량 적합성은 미확인이다. Meta 도움말은 업로드·생성 파일이 `System Files`에 저장된다고 설명하며, Library 화면에 파일별 크기는 보였지만 전체 용량 한도나 합계는 표시되지 않았다. Muse ZIP 회수는 수동이며 자동 로컬 동기화를 증명하지 않는다. 11월 14일에는 Drive for desktop의 합성 폴더 동기화 설정까지 확인했다. 상세: [M4 WorkLog — 이미지 첨부 wikilink 시험](../../vl_worklog/20261114_M4_Muse-My-Workflow.md#obsidian-이미지-첨부-wikilink-경로판독-시험-2026-11-14), [M4 WorkLog — PDF 첨부 wikilink 시험](../../vl_worklog/20261114_M4_Muse-My-Workflow.md#obsidian-pdf-첨부-wikilink-경로텍스트-판독-시험-2026-11-14). 상세 근거: [M4 WorkLog — Obsidian wikilink 시험](../../vl_worklog/20261114_M4_Muse-My-Workflow.md#obsidian-위키링크-해석대상-편집경로-회수-시험-2026-11-14), [M4 WorkLog — 모호한 wikilink 안전 처리 시험](../../vl_worklog/20261114_M4_Muse-My-Workflow.md#obsidian-모호한-basename-wikilink-안전-처리-시험-2026-11-14), [M4 WorkLog — heading·block fragment 링크 시험](../../vl_worklog/20261114_M4_Muse-My-Workflow.md#obsidian-headingblock-fragment-링크-시험-2026-11-14), [M4 WorkLog — 검색·편집·저장소 표시](../../vl_worklog/20261114_M4_Muse-My-Workflow.md#muse-저장-파일-관리-표시-및-대규모-검색-편집-시험-2026-11-14), [Meta 도움말](https://www.meta.com/help/superintelligence/2225571704857152/).

## Muse 내부 저장 한도 확인 (2026-11-14)

소비자용 Muse 공개 페이지와 Library 화면에서는 계정별 전체 파일 용량/ZIP 한도를 찾지 못했다. Meta Model API 문서에 나오는 Files API의 파일당 1 GiB·팀별 기본 100 GiB 저장 허용량은 API 제품의 수치이며 소비자 Muse Library에 적용된다고 볼 근거가 없다. 따라서 실제 Vault 64.614 GiB의 Muse 내부 수용 가능성은 미확인으로 둔다. Muse-native 왕복으로 확인된 최대 합성 표본은 5,777개 Markdown 파일·103.8 MiB payload다. 자세한 조사 한계와 출처: [M4 WorkLog — Muse 저장 용량 공식 문서 재확인](../../vl_worklog/20261114_M4_Muse-My-Workflow.md#muse-저장-용량-공식-문서-재확인-2026-11-14), [Meta Model API 파일 처리](https://dev.meta.ai/docs/file-handling).

## Obsidian 역링크 탐색 확인 (2026-11-14)

격리된 네 노트 fixture에서 Muse는 대상 노트로 향하는 두 incoming wikilink를 찾았다. 한 링크는 확장자를 생략하고(`[[Topics/Shared/target|Target]]`), 다른 하나는 `.md`를 적었다(`[[Topics/Shared/target.md|Beta target]]`). Muse는 alias/일반 단어 검색과 구분해 link target path를 기준으로 source 노트 두 개를 보고했다. 로컬 반환 ZIP은 네 Markdown 파일·125 payload bytes, 2,434 bytes, SHA-256 `16afcccdd65b31f9eb61687abc6938ae1cf34008291dcbcf49118ca27b3e52ac`였고 경로·크기도 Muse 보고와 일치했다. 이 시험은 작은 fixture에 대한 텍스트 링크 탐색이며 실제 Obsidian backlinks pane/index, 전체 Vault 색인, 깨진 링크, 대규모 성능을 증명하지 않는다. [M4 WorkLog — backlinks 탐색 시험](../../vl_worklog/20261114_M4_Muse-My-Workflow.md#obsidian-backlinks-링크-대상-탐색-시험-2026-11-14)

## 실제 Vault와 같은 파일 수의 합성 왕복 (2026-11-14)

55,035개의 작은 Markdown 파일을 포함한 별도 합성 트리를 Muse 내부에서 만들고 ZIP 왕복했다. Muse가 확인한 payload는 825,535 bytes였고, ZIP은 14,045,667 bytes였다(55,035 파일 + 57 디렉터리 entry). 다운로드본 로컬 검사에서 정확한 regular file 수·payload 크기·처음/마지막 경로·유일 marker 위치를 확인했고 `testzip` 무결성 검사를 통과했으며 SHA-256 `c522fd8abf4ffb4b30ee37d9a0bc556bb681bc73c56127a483f3f7d08b95b9b0`는 Muse 보고와 같았다. 이는 실제 Vault와 같은 파일 개수 수준의 작은 Markdown 표본 시험이다. 64.614 GiB의 실제 payload, 다양한 형식·크기 분포, consumer Muse 저장 용량 한도나 자동 동기화는 입증하지 않는다. [M4 WorkLog — 55,035개 파일 수 시험](../../vl_worklog/20261114_M4_Muse-My-Workflow.md#muse-native-실제-vault-파일-수-대응-합성-시험-2026-11-14)

## 실험 후 정할 항목

가상 Vault 실험을 시작하는 데 필요한 사용자 결정은 끝났다. 실제 사본 운영에 아래 설정이 필요해지면 실험 결과를 보고 정한다.

- 실제 Vault 자료를 가져올 때 허용할 자료 등급·포함 경로·파일 형식
- 보조 저장소가 필요할 때 서비스·목적지 폴더·커넥터 권한
- 수동·자동 반영 방식, 예약 실행을 선택한 경우의 주기, 사본 보존 기간
- 실패 시 재시도·복구 절차와 목적지 사본 정리 기준

## 관련 자료

- [시나리오 비교표](seamless-scenarios.md#시나리오-비교)
- [사본 규칙 초안](mirror-policy.md#승인-대기-사항)
- [최신 M4 WorkLog](../../vl_worklog/20261114_M4_Muse-My-Workflow.md#보조-저장소-동기화-방식-리서치)
