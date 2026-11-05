# 볼트 연결 해법 지도

## 후보 8개 확인표

공식 문서와 Muse 웹 화면 확인일은 **2026-11-05**다. Muse에는 사용량이 제한된 무료 이용 범위가 있으며, 저장소 플랜이나 Claude 구독은 별도로 적용된다. [Meta Muse 이용 안내](https://ai.meta.com/muse/)

| 후보 | 출처와 화면 관찰 | 비용·설치·확인할 제약 |
|---|---|---|
| A · Dropbox 사본 | Dropbox 공식 도움말과 Muse Business 목록에서 확인. [Dropbox 도움말](https://help.dropbox.com/integrations/connect-to-meta-muse) | 미국·캐나다 Dropbox 전 플랜. 브라우저에서 계정 연결이 필요하며, 읽기·쓰기·삭제·공유 등 동작별 설정이 있다. 특정 폴더만 허용하는지, 집 PC로 자동 회수되는지는 시험 필요. |
| B · GitHub private 사본 | Meta 공식 발표와 Muse Business 목록에서 확인. [Meta Connect 발표](https://www.meta.com/blog/meta-connect-2026-everything-we-announced/) | GitHub 계정과 시험 저장소 필요. 별도 커넥터 비용과 private 저장소 하나로 제한 가능한지는 미확인. |
| C · Google Drive 또는 Box | Muse 화면에서 두 항목 확인. Meta는 Box를 공식 발표했고 Google 연결 데이터에 대한 정책을 안내한다. [Meta Connect 발표](https://www.meta.com/blog/meta-connect-2026-everything-we-announced/) · [Meta 커넥터 도움말](https://www.meta.com/help/superintelligence/1687253048996149/) | 각 서비스 계정 필요. 연결의 별도 비용은 미확인. Drive에는 읽기·쓰기·삭제·공유 및 백그라운드 동작별 설정이 보인다. 화면의 동작 설정만으로 단일 폴더 접근 범위를 판정할 수 없다. Box의 실제 권한 범위는 미확인. |
| D · 수동 전달 | 볼트 실증으로 Library 다운로드와 Codex 인계 확인. [M3 실습 4](../../vl_worklog/20261105_M3_Muse-My-Workflow.md#실습-4-결과) | 별도 저장소 연결 없이 브라우저에서 가능. 내려받기와 Inbox 복사가 수동이며 원본 3개 보존은 검증했다. |
| E · Claude Code Remote Control | Anthropic 공식 문서와 이전 Topic 실증을 확인. [Anthropic Remote Control](https://code.claude.com/docs/en/remote-control) · [이전 Topic 결론](../../../Claude-Code-Mobile-Remote-Execution/README.md#이-자료의-결론) | 지원 Claude 구독과 로컬 Claude Code가 필요하다. 집 PC의 실행·네트워크가 필요하고 작업 폴더는 로컬에서 읽는다. |
| F · Claude Code 웹·모바일 | Anthropic 공식 문서에서 클라우드 세션 및 GitHub 연동 확인. [Claude Code 클라우드](https://code.claude.com/docs/en/claude-code-on-the-web) · [Claude 요금제](https://claude.com/pricing) | Claude Code 지원 플랜과 GitHub 접근 필요. Claude GitHub App 설치 범위와 로컬 토큰 연결 범위가 다르다. 이 실습에서는 별도 시험 레포가 선행 조건이다. |
| G · Muse 데스크톱 | Meta 다운로드에서 macOS 확인. Microsoft는 Windows MXC 연동을 예고했다. [Meta 다운로드](https://ai.meta.com/muse/download/) · [Microsoft Windows 발표](https://blogs.windows.com/windowsexperience/2026/10/07/building-windows-for-hybrid-intelligence/) | Mac 앱 설치가 필요하다. Windows 설치 배포와 별도 비용은 이번 공식 자료 확인에서 확인하지 못해 Windows 시험을 대기한다. |
| H · 사용자 정의 커넥터 | Meta는 사용자 정의 커넥터를 안내한다. [Meta 커넥터 도움말](https://www.meta.com/help/superintelligence/1687253048996149/) | API·자격 증명과 서비스 운영이 필요할 수 있다. 집 PC 직접 연결의 접근 범위와 운영 비용은 미확인. 이번에는 문서 검토 범위다. |

## 시험 후보 제안

| 순서 | 후보 | 확인할 점 |
|---|---|---|
| 1 | D · 수동 다운로드 | S1·S2에서 손으로 해야 하는 단계와 원문 보존을 기준으로 삼는다. |
| 2 | E · Remote Control | S2·S4에서 집의 작업을 휴대폰으로 이어가는 데 걸리는 단계와 PC 가동 조건을 비교한다. |
| 3 | C · Google Drive | 사용자가 시험 범위를 확정하면 공개 샘플로 S3·S5의 검색과 회수 가능성을 본다. 파일 동작과 폴더 범위는 구분해 기록한다. |
| 4 | A · Dropbox | 새 연결을 결정할 경우 공개 샘플만 담은 시험 공간에서 Drive와 같은 조건으로 비교한다. |

후보는 제안 단계다. 저장소 시험 전에는 사본 규칙과 읽기·쓰기 범위를 먼저 확정한다. [M4 실습 순서](../../vl_roadmap/20261018_RoadMap_Muse-My-Workflow.md#m4---볼트-연결-해법--집과-밖을-끊김-없이)
