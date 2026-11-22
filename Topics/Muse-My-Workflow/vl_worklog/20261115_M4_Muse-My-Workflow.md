---
title: "WorkLog - M4 Muse와 Google Drive Computers 왕복 시험"
author:
  - Codex
created: 2026-11-15 04:18:55
tags:
  - muse-my-workflow
  - worklog
---

## 오늘의 학습 목표

11월 14일에 Drive for desktop으로 동기화한 합성 폴더를 Muse의 기존 Google Drive 커넥터가 읽을 수 있는지 확인한다. 읽기가 확인되면 같은 합성 폴더에 새 결과 Markdown을 만들어 PC에서 경로와 내용을 대조한다. [이전 WorkLog](20261114_M4_Muse-My-Workflow.md#google-drive-for-desktop-설치-및-합성-computers-폴더-동기화-2026-11-14)

## 진행 내용

시험 대상은 `Computers → My PC → trial-vault`의 `planning-brief.md`, `continuation-note.md`, `event-catalog.md`다. 대응하는 [로컬 원본](../04-Vault-Connection/examples/trial-vault/) 세 개의 본문을 읽어 가상 일정과 작업 지시만 들어 있음을 확인했다. 모두 `visibility: public`과 `synthetic-fixture` 표식이 있다.

| 파일 | 로컬 SHA-256 |
|---|---|
| `planning-brief.md` | `068ED3D60A128D96C2C34CEB0C16A4F2014401213FAE6580E8FC6171DB229B14` |
| `continuation-note.md` | `725389D34146F6B0CB5ADA6CF360371B608C6A9163526494B584D48006508BEB` |
| `event-catalog.md` | `43B9DCD961A4FB0CF2FB5A3C312607F53D05DF7F0634CC49D719EBE530054188` |

기존 [사본 스크립트](../04-Vault-Connection/scripts/build_mirror.py)를 두 가지 미리 보기로 검증했다. 예시 설정에서는 합성 Markdown 세 개가 포함 후보였고 복사 0건이었다. 스크립트 자체 데모에서는 공개 표본 한 개만 포함 후보였고, 개인·내부·분류 누락·허용 외 형식 표본 각 한 개가 제외됐다. 복사 0건과 예시 사본 목적지 미생성을 확인했다. 이 결과는 이번 합성 표본에 적용된다. [사본 규칙](../04-Vault-Connection/guides/mirror-policy.md#승인-검토안)

## 문제 해결 로그

첫 읽기 요청은 자료와 목적지를 구체적으로 승인받아야 한다는 이유로 자동 승인 검토가 차단했다. 박창수가 지정한 폴더의 세 파일 읽기와 성공 시 결과 한 개 쓰기를 승인한 뒤, Muse 웹의 별도 시험 채팅에서 읽기 요청을 다시 제출했다. Google Drive의 기본 웹 계정에는 컴퓨터가 표시되지 않았으나, 시험 폴더를 직접 열자 해당 폴더가 있는 기존 계정으로 연결됐다.

## Google Drive Computers 읽기와 PC 자동 회수 — 통과

Muse가 커넥터로 `Computers → My PC → trial-vault`를 찾고 세 원본을 읽었다. 보고한 크기는 `planning-brief.md` 609 B, `continuation-note.md` 544 B, `event-catalog.md` 697 B였으며, 각 파일에서 돌려준 본문 한 줄과 크기가 로컬 원본과 일치했다. [Muse 시험 채팅](https://muse.ai/thread/4415bf86-1f7c-4ae7-9b9b-fe8528594ff3)

Muse의 파일 생성 확인에서 이번 생성만 승인했다. Muse는 동일한 폴더에 `muse-computers-return-20261115.md`를 `text/markdown`으로 만들고 다시 읽어 76 B와 SHA-256을 반환했다. Drive 웹 목록에서 새 파일을 확인했고, 04:29 PST에 원래 PC 동기화 폴더에서 파일을 확인했다. PC에서 직접 바이트를 비교한 결과, UTF-8 BOM 없이 약속한 세 줄과 마지막 LF가 일치했다. SHA-256은 `71928FA87744180635D66CAB110AAF747D564EC798CE6C19932EA52EA488FF34`로 Muse 보고와 같았고 원본 세 파일 해시도 앞 표와 모두 일치했다. [PC 회수 파일](../04-Vault-Connection/examples/trial-vault/muse-computers-return-20261115.md) · [Drive 웹 증거 화면](../04-Vault-Connection/assets/20261115-muse-drive-computers-return.jpg)

## DoD 진행 상태

M4는 **7/8**이다. 사본 규칙·미리 보기 보고서에 대한 사용자 검토와 승인이 남아 있다. 이번 합성 미리 보기 통과는 설정 예시와 데모를 재확인한 결과다. [로드맵 M4](../vl_roadmap/20261018_RoadMap_Muse-My-Workflow.md#m4---볼트-연결-해법--집과-밖을-끊김-없이)

## Daily Retrospective

이번 시험으로 PC가 켜진 상태에서 Drive for desktop으로 동기화한 한 합성 폴더의 Muse 읽기·쓰기와 PC 자동 회수를 확인했다. 기존 My Drive 웹 업로드의 404 결과는 해당 시험 경로의 기록으로 남는다. PC 종료 중 Drive 경유 회수, 커넥터의 기술적 폴더 제한, 실제 Vault 동기화는 미검증이다.
