---
title: "Pre-M4 Setup - Claude Code Mobile Remote Execution"
created: 2026-08-23 09:29:53
tags:
  - vibelearn-ai
  - claude-code
  - tailscale
  - openssh
  - remote-execution
---

## Summary

M4 본 실험 전에 필요한 Windows 노트북 원격 실행 준비를 완료했다. 이번 단계에서는 Tailscale을 설치하고 로그인한 뒤, Windows OpenSSH Server를 설치/활성화하고 SSH 방화벽 허용 범위를 Tailscale 네트워크로 제한했다.

## Completed Setup

| 항목 | 상태 | 확인값 |
|---|---:|---|
| Tailscale 설치 | 완료 | `Tailscale` service `Running`, `Automatic` |
| Tailscale 로그인 | 완료 | tailnet `solkit70@gmail.com` |
| Tailscale IPv4 | 완료 | `100.109.17.103` |
| Tailscale IPv6 | 완료 | `fd7a:115c:a1e0::e601:11c4` |
| MagicDNS | 완료 | `changsoo.tail8af0a9.ts.net` |
| OpenSSH Server 설치 | 완료 | `C:\Windows\System32\OpenSSH\sshd.exe` exists |
| SSH 서비스 | 완료 | `sshd` service `Running`, `Automatic` |
| 방화벽 제한 규칙 | 완료 | `OpenSSH-Server-In-TCP-Tailscale` enabled |
| 기본 OpenSSH 방화벽 규칙 | 제한 완료 | `OpenSSH-Server-In-TCP` disabled |

## Firewall Scope

SSH inbound TCP 22는 전체 인터넷에 열지 않고 Tailscale 네트워크에서 들어오는 연결만 허용하도록 설정했다.

| 규칙 | 값 |
|---|---|
| Rule name | `OpenSSH-Server-In-TCP-Tailscale` |
| Display name | `OpenSSH Server over Tailscale only` |
| Direction | `Inbound` |
| Protocol | `TCP` |
| Local port | `22` |
| Action | `Allow` |
| Profile | `Any` |
| Remote address | `100.64.0.0/10`, `fd7a:115c:a1e0::/48` |

## Notes

Windows Optional Feature 설치는 중복으로 세 번 큐에 들어가면서 처음에는 멈춘 것처럼 보였다. 중복된 두 항목을 취소하고 하나만 남기자 설치 진행 바가 정상적으로 움직였고 최종적으로 `OpenSSH Server`가 `Added` 상태가 되었다.

현재 구조는 M2에서 정한 1차 실험 구조와 일치한다: `iPhone -> Tailscale private network -> Windows OpenSSH Server -> Claude Code -> local vault`. 아직 M4 본 실험, 즉 모바일 기기에서 Tailscale 접속 후 SSH로 노트북에 들어가 Claude Code를 실행하는 검증은 수행하지 않았다.

## M4 Entry Condition

M4를 시작하기 전에 모바일 쪽에서 준비할 항목은 다음과 같다.

| 항목 | 상태 |
|---|---:|
| iPhone Tailscale 앱 설치 | 미확인 |
| iPhone Tailscale 로그인 | 미확인 |
| 모바일 SSH 클라이언트 선택 | 미정 |
| SSH 접속 계정/인증 방식 확정 | 미정 |
| Claude Code 원격 실행 테스트 | 미수행 |
