---
title: "끊김 없는 시나리오별 시험표"
author:
  - Codex
created: 2026-11-05 07:47:00
visibility: public
tags:
  - muse-my-workflow
  - scenarios
---

## 시험 범위

[English](seamless-scenarios.en.md)

이 표는 M4의 이전 실습 근거와 이번 시험 결과를 구분한다. D(수동 전달)는 M2·M3의 기준선이다. **E(Claude Code Remote Control)는 Muse 외부의 대안 경로**로, 휴대폰에서 집 PC의 로컬 Claude Code 세션을 이어간다. E의 결과는 Muse 커넥터나 볼트 동기화의 검증으로 집계하지 않는다. [Claude Code 공식 안내](https://code.claude.com/docs/en/remote-control)

E의 첫 시험은 [가상 시험 폴더](../examples/trial-vault/)의 공개 표시 파일 세 개만 사용한다. 실제 볼트 사본 범위와 C(Google Drive) 시험은 다음 세션으로 미뤘다.

## 시나리오 비교

| 시나리오 | D · 수동 전달 | E · Claude Code Remote Control (대안) | C · Google Drive | A · Dropbox |
|---|---|---|---|---|
| S1 음성 메모를 저녁에 원문 그대로 Journal에 넣기 | 부분 근거: M2에서 받아 적힌 문장과 저장 파일의 동일성을 확인. Journal 자동 반영은 미시험. [M2 결과](../../02-Muse-to-Vault/guides/transfer-comparison.md#음성-원문-보존) | M4 미시험. 기존 모바일 원격 기록은 음성 입력→Journal 흐름을 검증하지 않음. [이전 Topic](../../../Claude-Code-Mobile-Remote-Execution/08-Native-Remote-Control/lab/remote-control-verification.md) | 미연결 | 미연결 |
| S2 밖에서 남긴 진행 중 Topic 메모를 집에서 이어가기 | 부분 검증: Muse Topic 파일 3개를 내려받아 볼트로 옮기고 기간 검토를 이어감. 이동은 수동. [M3 인계](../../vl_worklog/20261105_M3_Muse-My-Workflow.md#실습-4-결과) | 가상 시험 통과: 휴대폰에서 요청한 새 Markdown이 집 PC 시험 폴더에 생성됐다. 집 PC에서 내용을 읽고 입력 3개의 SHA-256이 그대로임을 확인했다. | 미연결 | 미연결 |
| S3 밖에서 허용된 볼트 자료 검색 | 제한적: 개별 전달·공개 레포 링크에서 전달한 자료는 읽을 수 있었음. 전체 볼트 검색은 아님. [M2 결과](../../02-Muse-to-Vault/guides/transfer-comparison.md#집-밖) | M4 미시험. 로컬 작업 폴더 범위 내 검색과 결과 회수 시간을 확인해야 함. | 미연결 | 미연결 |
| S4 집에서 하던 일을 밖에서 이어가기 | 부분 검증: 넘김 꾸러미 업로드 후 Muse가 다음 할 일을 이어갔음. 볼트 파일의 실시간 공유는 아님. [M2 결과](../../02-Muse-to-Vault/guides/transfer-comparison.md#집-밖) | 가상 시험 통과: 집 PC에서 가상 파일 3개를 읽은 세션에 휴대폰으로 이어서 요청했다. 같은 로컬 세션에서 새 파일 쓰기를 확인했다. 집 PC와 Claude Code 세션이 켜진 조건에서 시험했다. | 미연결 | 미연결 |
| S5 노트북 없이 보낸 하루의 결과가 집 PC에 자동 도착 | 미충족: 다운로드·메일은 사람의 전달 단계가 필요함. 자동 동기화는 확인되지 않음. [M2 비교](../../02-Muse-to-Vault/guides/transfer-comparison.md#밖-집) | 미충족 조건: 원격 작업은 집 PC와 로컬 Claude Code 실행이 필요함. 노트북이 꺼진 상태의 자동 회수는 아님. [M8 구조](../../../Claude-Code-Mobile-Remote-Execution/08-Native-Remote-Control/concepts/native-remote-control-model.md#연결-구조) | 미연결. 클라우드 결과가 로컬 PC에 자동 동기화되는지 미확인 | 미연결. 클라우드 결과가 로컬 PC에 자동 동기화되는지 미확인 |

## 다음 실험 순서

1. 사용자 확인 뒤 시험할 연결 후보를 선택한다. 후보와 권한 한계는 [해법 지도](solution-map.md#시험-후보-제안)에 있다.
2. 선택한 저장소에는 가상 시험 폴더만 연결한다. 읽기·쓰기·삭제·공유 권한과 폴더 범위를 확인하고, 권한이 필요 이상이면 중단한다.
3. 가상 행사를 검색하고, 겹침을 설명하게 한 뒤, 원본을 덮어쓰지 않고 새 결과 파일을 만든다. 집 PC에서 해당 결과가 보이는지 별도 확인한다.
4. 캡처는 가상 파일 이름만 보이도록 한다: 연결 목록, 권한 범위, 가상 파일 검색 결과, 새 결과 파일, 집 PC에서 회수한 결과.
5. 연결을 끊고 시험 자료·결과 파일을 정리하는 화면은 사용자 동의를 받은 뒤 캡처한다. 파일 삭제 동작은 별도 승인 전 수행하지 않는다.

## 상태

**2026-11-08 · E 첫 시험** — 가상 자료로 휴대폰에서 작업을 재개하고(S4) 집 PC에서 결과를 확인했다(S2). 이번 시험은 같은 로컬 세션에서 파일을 직접 썼다. 결과 파일의 작성자 메타데이터에 계정 이메일이 자동으로 들어가 원본 결과는 로컬에만 보관했다. [시험 WorkLog](../../vl_worklog/20261108_M4_Muse-My-Workflow.md#결과-검증)
