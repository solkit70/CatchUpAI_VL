# M4 전 Go/No-Go 판단

## 현재 판단

**상태**: Conditional Go

현재 노트북은 Claude Code 로컬 실행 호스트로는 준비되어 있지만, 모바일 원격 접속 실험을 바로 수행할 상태는 아니다. M4에서 실험 절차서를 먼저 만들고, 아래 설정 변경 항목을 하나씩 승인받아 준비하면 진행 가능하다.

## Go 조건

M4 실험을 진행하려면 최소한 아래 조건을 만족해야 한다.

- [ ] Tailscale 또는 ZeroTier 중 하나의 사설망 도구 선택
- [ ] 선택한 사설망 도구 설치 및 로그인 승인
- [ ] iPhone에도 같은 사설망 도구 설치/로그인 가능
- [ ] Windows OpenSSH Server 설치/활성화 승인
- [ ] Windows 방화벽 SSH inbound rule 확인 또는 생성 승인
- [ ] 접속 테스트에 사용할 Windows 계정 확인
- [ ] 테스트 작업 경로를 현재 Topic M4 폴더로 제한
- [ ] 실험 전후 `git status` 확인

## No-Go 조건

아래 중 하나라도 해당하면 M4 실제 접속 실험을 보류한다.

- [ ] 사용자가 Tailscale/ZeroTier 계정 연결을 승인하지 않음
- [ ] OpenSSH Server 설치 또는 활성화를 승인하지 않음
- [ ] Windows 계정/권한을 확인할 수 없음
- [ ] 노트북이 외부 접속 실험 중 절전될 가능성이 높고 전원 설정 변경을 승인하지 않음
- [ ] Git 상태가 복잡해서 테스트 변경 범위를 안전하게 분리할 수 없음
- [ ] 사용자가 공개 포트 개방 외에는 방법이 없다고 판단되지만, 보안 검토가 끝나지 않음

## 추천 M4 준비 순서

1. M4 학습 계획 승인
2. 실험 절차서 작성
3. Tailscale 설치/로그인 여부 확인
4. Windows OpenSSH Server 설치/활성화 여부 확인
5. 방화벽 규칙 확인
6. iPhone SSH 앱 후보 확인
7. 로컬에서 `ssh localhost` 또는 equivalent 테스트
8. iPhone에서 Tailscale IP/MagicDNS로 접속 테스트
9. 안전한 shell 명령으로 실행 위치 검증
10. Claude Code 실행은 마지막 단계에서 진행

## 1차 실험 추천 구조

```text
iPhone
  -> Tailscale private network
  -> Windows OpenSSH Server
  -> PowerShell / shell session
  -> Claude Code
  -> Ingest/CatchUpAI_VL/Topics/Claude-Code-Mobile-Remote-Execution
```

## 대안

Tailscale 설치/로그인이 어렵다면 ZeroTier를 대안으로 검토한다. 두 도구를 동시에 설치해 비교하지는 않는다. M4의 목적은 원격 실행 구조 검증이지 VPN 제품 비교가 아니다.

## 결론

M4는 진행 가능하지만, 현재 상태에서는 바로 접속 실험을 시작하지 않는다. 먼저 실험 절차서를 만들고, 사설망 도구와 OpenSSH Server 관련 설정 변경을 사용자에게 별도 승인받아야 한다.
