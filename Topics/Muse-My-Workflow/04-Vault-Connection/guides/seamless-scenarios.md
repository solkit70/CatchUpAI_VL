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

E 시험은 [가상 시험 폴더](../examples/trial-vault/)의 파일 세 개로 진행했다. C 시험은 별도 가상 시험 폴더만 Muse의 기존 Google Drive 연결로 읽고, 새 결과를 같은 폴더에 만들었다. Dropbox 시험도 같은 세 가상 파일만 개인 전용 시험 폴더에 올려 읽기·결과 작성을 확인했다. 검토된 `visibility: public` 사본 세 개는 별도 Drive 폴더에 업로드했으며 C·Dropbox 시험 입력으로 사용하지 않았다.

## 시나리오 비교

| 시나리오 | D · 수동 전달 | E · Claude Code Remote Control (대안) | C · Google Drive | A · Dropbox |
|---|---|---|---|---|
| S1 음성 메모를 저녁에 원문 그대로 Journal에 넣기 | 부분 근거: M2에서 받아 적힌 문장과 저장 파일의 동일성을 확인. Journal 자동 반영은 미시험. [M2 결과](../../02-Muse-to-Vault/guides/transfer-comparison.md#음성-원문-보존) | M4 미시험. 기존 모바일 원격 기록은 음성 입력→Journal 흐름을 검증하지 않음. [이전 Topic](../../../Claude-Code-Mobile-Remote-Execution/08-Native-Remote-Control/lab/remote-control-verification.md) | 연결 확인 · S1 미시험 | 미연결 |
| S2 밖에서 남긴 진행 중 Topic 메모를 집에서 이어가기 | 부분 검증: Muse Topic 파일 3개를 내려받아 볼트로 옮기고 기간 검토를 이어감. 이동은 수동. [M3 인계](../../vl_worklog/20261105_M3_Muse-My-Workflow.md#실습-4-결과) | 가상 시험 통과: 휴대폰에서 요청한 새 Markdown이 집 PC 시험 폴더에 생성됐다. 집 PC에서 내용을 읽고 입력 3개의 SHA-256이 그대로임을 확인했다. 이는 원격 세션의 가상 파일 작업 근거다. | 커넥터 수준 가상 확인 · Muse가 지정 시험 폴더의 세 파일을 읽고 결과 파일을 작성했다. 이는 외부 메모를 집에서 이어간 연속 작업 자체를 시험한 것은 아니다. 폴더 단위 권한 제한 여부도 UI에서 판정 못 함 | 미시험 · 파일은 수동 업로드 후 PC 브라우저에서 처리. 외부에서 남긴 Topic의 집 연속 작업은 검증하지 않음 |
| S3 밖에서 허용된 볼트 자료 검색 | 제한적: 개별 전달·공개 레포 링크에서 전달한 자료는 읽을 수 있었음. 전체 볼트 검색은 아님. [M2 결과](../../02-Muse-to-Vault/guides/transfer-comparison.md#집-밖) | M4 미시험. 로컬 작업 폴더 범위 내 검색과 결과 회수 시간을 확인해야 함. | 연결됨 · 검색 결과를 받지 못해 S3 미시험 | 부분 확인 · 업로드 전 검색은 0건, 업로드 후 지정 폴더 범위 검색에서 세 파일을 모두 찾고 폴더 목록의 결과 파일까지 확인. 전체 계정 검색이나 폴더 권한 강제 여부는 검증 아님 |
| S4 집에서 하던 일을 밖에서 이어가기 | 부분 검증: 넘김 꾸러미 업로드 후 Muse가 다음 할 일을 이어갔음. 볼트 파일의 실시간 공유는 아님. [M2 결과](../../02-Muse-to-Vault/guides/transfer-comparison.md#집-밖) | 가상 시험 통과: 집 PC에서 가상 파일 3개를 읽은 세션에 휴대폰으로 이어서 요청했다. 같은 로컬 세션에서 새 파일 쓰기를 확인했다. 집 PC와 Claude Code 세션이 켜진 조건에서 시험했다. | 부분 근거 · Muse에서 만든 결과를 PC에서 수동 다운로드로 회수했다. 집에서 하던 일을 밖에서 이어간 흐름은 시험하지 않았다. 자동 동기화도 미확인 | 미시험 · Dropbox 읽기와 결과 생성은 PC 브라우저에서 확인했으며 휴대폰 사용은 확인하지 않음 |
| S5 노트북 없이 보낸 하루의 결과가 집 PC에 자동 도착 | 미충족: 다운로드·메일은 사람의 전달 단계가 필요함. 자동 동기화는 확인되지 않음. [M2 비교](../../02-Muse-to-Vault/guides/transfer-comparison.md#밖-집) | 미충족 조건: 원격 작업은 집 PC와 로컬 Claude Code 실행이 필요함. 노트북이 꺼진 상태의 자동 회수는 아님. [M8 구조](../../../Claude-Code-Mobile-Remote-Execution/08-Native-Remote-Control/concepts/native-remote-control-model.md#연결-구조) | 미충족 · 수동 다운로드로 회수했으며 자동 동기화는 미확인 | 부분 통과 · Dropbox 데스크톱 앱 설정 뒤 깨어 있는 PC에서 네 파일 모두 Available on this device로 표시. 절전 요청 전후에도 로컬 상태는 유지됐지만 S0 전환 검증이나 절전 중 새 클라우드 변경 추적은 못 해 Sleep 효과는 미판정. Dropbox 재실행 후 Muse의 세 원본 검색과 폴더 네 파일 목록은 성공 |

## 다음 실험 순서

1. Dropbox 업로드 후 검색은 성공했고, 데스크톱 앱 설정 후 깨어 있는 PC에서 네 파일의 자동 로컬 동기화도 확인했다. 후속 범위는 S0 절전 진입·복귀 및 절전 중 클라우드 변경 추적, 폴더 범위 제한, 모바일 접근이다. Chrome 업데이트·재시작 뒤 현재 Muse 화면에서 403 알림은 보이지 않았지만 사용자가 반복 경험을 보고해 해결·원인은 미판정이다.
2. Google Drive의 폴더 범위·모바일 접근·자동 동기화는 별도 미시험으로 유지한다. 사용자 승인 범위 밖으로 자료를 추가 업로드하지 않는다.
3. 다음 모듈 전 전체 볼트 사본 정책을 결정하고, 공개 표시 후보의 범위와 내부 자료 제외 기준을 재검토한다.
4. 캡처는 가상 파일 이름만 보이도록 한다. 파일 삭제나 연결 해제 화면은 사용자 동의 전에 실행하지 않는다.

## 상태

**2026-11-08 · E · C · A 가상 시험** — E는 Muse 외부의 Claude Code Remote Control 대안 경로로 S2·S4를 통과했다. C는 지정된 Drive 가상 폴더에서 읽기·결과 작성과 PC 수동 회수를 통과했다. A는 개인 Dropbox 시험 폴더에서 읽기·결과 작성을 통과했고 업로드 후 검색에서 세 원본을 모두 찾았다. 첫 0건은 업로드 전 검색이었다. Dropbox PC 자동 회수는 데스크톱 앱 설정 후 깨어 있는 상태에서 네 파일의 로컬 동기화로 확인했다. 절전 요청 전후 같은 네 파일은 Available on this device였으나 S0 진입·복귀와 절전 중 새 클라우드 변경을 확인하지 못해 Sleep 효과는 미판정이다. Dropbox 재실행 후 원본 세 파일 검색과 폴더 네 파일 목록은 모두 성공했다. [시험 WorkLog](../../vl_worklog/20261108_M4_Muse-My-Workflow.md#dropbox-절전-시험-후-읽기-전용-재확인) 모바일 접근은 미검증이다. Chrome 업데이트·재시작 후 현재 Muse 화면에서는 403 알림이 보이지 않았지만, 반복 보고가 있어 해결 여부는 미판정이다. [시험 WorkLog](../../vl_worklog/20261108_M4_Muse-My-Workflow.md#c-google-drive-시험)
