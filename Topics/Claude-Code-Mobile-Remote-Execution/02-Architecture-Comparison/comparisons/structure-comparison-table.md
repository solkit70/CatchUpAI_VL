# 기술 구조 비교표

## 평가 기준

점수는 1-5점이다. 5점이 현재 목표에 가장 적합하다는 뜻이다.

| 구조                              |  보안 |  비용 | 안정성 | 모바일 사용성 | 세팅 난이도 | Vault 적합성 |  총점 | 판단    |
| ------------------------------- | --: | --: | --: | ------: | -----: | --------: | --: | ----- |
| 직접 SSH + 포트포워딩                  |   2 |   5 |   3 |       3 |      2 |         5 |  20 | 보류    |
| Tailscale 사설망 + Windows OpenSSH |   4 |   4 |   4 |       4 |      3 |         5 |  24 | 1차 추천 |
| ZeroTier 사설망 + Windows OpenSSH  |   4 |   4 |   4 |       4 |      3 |         5 |  24 | 대안    |
| GitHub Codespaces               |   4 |   3 |   5 |       4 |      3 |         2 |  21 | 별도 목적 |
| 현재 Windows 노트북 단독 실행 호스트        |   3 |   5 |   2 |       3 |      4 |         5 |  22 | 검증용   |
| 맥미니 홈서버                         |   4 |   3 |   5 |       4 |      3 |         5 |  24 | 2차 후보 |
| 맥 스튜디오 홈서버                      |   4 |   1 |   5 |       4 |      3 |         5 |  22 | 특수 목적 |

## 구조별 상세 평가

### 직접 SSH + 포트포워딩

직접 SSH는 이해하기 쉽고 비용이 거의 들지 않는다. 하지만 집 공유기에서 포트포워딩을 열어야 하는 경우가 많고, 공개 인터넷에 SSH 서버가 노출될 수 있다. 동적 IP, 방화벽, brute-force 시도, 계정 보안까지 관리해야 하므로 1차 실험 구조로는 비추천이다.

적합한 경우:
- 이미 고정 IP, 방화벽, SSH hardening, 로그 모니터링에 익숙한 경우
- 사설망 도구를 사용할 수 없는 특수 환경

보류 이유:
- 이번 목표는 빠르고 안전한 구조 검증이다.
- 공개 포트 개방은 M5 보안 가이드 작성 전에는 피하는 것이 맞다.

### Tailscale 사설망 + Windows OpenSSH

현재 가장 균형 잡힌 1차 실험 구조다. iPhone과 Windows 노트북을 같은 tailnet에 넣고, Windows에서 OpenSSH Server를 켠 뒤 Tailscale IP 또는 MagicDNS 이름으로 접속하는 방식이다. 공개 포트를 열지 않고도 접속 실험을 할 수 있다.

주의:
- `Tailscale SSH` 관리형 기능과 구분해야 한다.
- Windows 실행 호스트에서는 Tailscale 네트워크 위에 Windows OpenSSH Server를 사용하는 구조로 보는 것이 안전하다.
- Tailscale 계정과 장치 인증, ACL 정책은 별도 관리 대상이다.

추천 이유:
- 현재 Windows 노트북으로 바로 검증 가능하다.
- 공개 포트 개방을 피한다.
- M4 실험으로 이어지기 쉽다.

### ZeroTier 사설망 + Windows OpenSSH

ZeroTier도 유사한 사설망 방식이다. ZeroTier 문서는 연결된 장치의 Managed IP로 SSH 또는 RDP에 접속하는 흐름을 제시한다. Tailscale과 비교하면 개념은 비슷하지만, 사용성, 계정 관리, 모바일 앱 경험, ACL 운영 방식이 다르다.

적합한 경우:
- 이미 ZeroTier 네트워크를 쓰고 있는 경우
- Tailscale이 특정 네트워크에서 잘 동작하지 않는 경우

대안으로 둔 이유:
- 이번 1차 실험에서는 Tailscale 쪽 문서와 모바일 사용성이 더 단순한 편이다.
- 둘 다 설치해서 비교하면 M4 범위가 커진다.

### GitHub Codespaces

Codespaces는 클라우드 개발 환경이다. GitHub 문서에 따르면 codespace는 GitHub가 호스팅하는 VM 위 Docker container에서 실행되고, 브라우저/VS Code/command shell로 접근할 수 있다. 모바일에서도 브라우저 접근은 가능하지만, 집 노트북의 vault를 직접 조작하는 구조는 아니다.

적합한 경우:
- GitHub repo 중심 개발
- 환경 재현성, 팀 온보딩, PR 기반 작업
- 로컬 노트북이 꺼져 있어도 되는 구조

이번 Topic에서 보류하는 이유:
- 핵심 목표가 집 머신의 Claude Code 실행 환경을 모바일로 조작하는 것이다.
- Obsidian vault 로컬 작업과 바로 맞물리지 않는다.

### 현재 Windows 노트북 단독 실행 호스트

현재 보유한 장비로 가장 빠르게 검증할 수 있다. 비용이 없고, 기존 vault와 Claude Code 작업 환경을 그대로 쓸 수 있다. 다만 외부에서 접속해야 하므로 절전, 네트워크 유지, OpenSSH Server, Tailscale/ZeroTier 같은 연결 계층이 필요하다.

적합한 경우:
- 첫 구조 검증
- 구매 전 판단
- 실제 모바일 원격 조작 흐름 확인

한계:
- 노트북은 이동/절전/배터리/네트워크 변경의 영향을 받는다.
- 장기 운영 서버로는 불안정할 수 있다.

### 맥미니 홈서버

맥미니는 상시 실행 호스트로 가장 현실적인 2차 후보이다. 전력, 비용, 설치 공간, 성능의 균형이 좋고, macOS Remote Login으로 SSH 서버 역할을 할 수 있다. Claude Code, Git, Node.js, Obsidian vault, 자동화 작업을 집 서버에 모으는 구조에 적합하다.

적합한 경우:
- 집에 항상 켜진 실행 호스트가 필요하다.
- 노트북은 이동 작업기로 쓰고 싶다.
- 영상 렌더링보다 안정적인 개발/문서/자동화 서버가 우선이다.

주의:
- 저장공간과 백업 전략을 처음부터 잡아야 한다.
- Remote Login 사용자는 제한해야 한다.
- 절전/재시작/원격 복구 전략이 필요하다.

### 맥 스튜디오 홈서버

맥 스튜디오는 성능은 좋지만 Claude Code 원격 실행만 놓고 보면 과한 선택일 가능성이 높다. Remotion 영상 렌더링, 대형 미디어 처리, 로컬 AI/그래픽 작업, 여러 작업 동시 실행이 홈서버의 상시 역할에 포함될 때 의미가 커진다.

적합한 경우:
- Remotion 영상 렌더링을 서버에 자주 맡긴다.
- 대용량 미디어/AI 작업을 상시 수행한다.
- 초기 비용보다 성능 여유가 중요하다.

보류 이유:
- 1차 실험 전에는 실제 부하를 모른다.
- 비용 대비 Claude Code 서버 용도로는 맥미니가 더 합리적일 가능성이 높다.

## 1차 추천

1차 실험은 `Tailscale 사설망 + Windows OpenSSH Server + Claude Code` 구조로 진행한다. 목표는 구매 없이 현재 노트북으로 모바일 원격 조작이 실제로 가능한지 검증하는 것이다.

2차 후보는 `맥미니 홈서버 + Tailscale/SSH + 노트북 이동 클라이언트` 구조다. 맥 스튜디오는 Remotion 렌더링이나 대형 미디어 작업이 상시 요구로 확인된 뒤 검토한다.

## 참조

- Tailscale SSH docs: https://tailscale.com/docs/features/tailscale-ssh
- ZeroTier Remote Desktop docs: https://docs.zerotier.com/remotedesktop/
- Microsoft OpenSSH for Windows overview: https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh-overview
- GitHub Codespaces docs: https://docs.github.com/en/codespaces/about-codespaces/what-are-codespaces
- Apple Remote Login support: https://support.apple.com/guide/mac-help/allow-a-remote-computer-to-access-your-mac-mchlp1066/mac
