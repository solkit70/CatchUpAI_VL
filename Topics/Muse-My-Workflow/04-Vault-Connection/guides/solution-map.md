# 볼트 연결 해법 지도

[English](solution-map.en.md)

## 후보 8개 확인표

공식 문서와 Muse 웹 화면 확인일은 **2026-11-05**다. Muse에는 사용량이 제한된 무료 이용 범위가 있으며, 저장소 플랜이나 Claude 구독은 별도로 적용된다. [Meta Muse 이용 안내](https://ai.meta.com/muse/)

| 후보 | 출처와 화면 관찰 | 비용·설치·확인할 제약 |
|---|---|---|
| A · Dropbox 사본 | 2026-11-08 공식 도움말과 Muse 화면 확인. [Dropbox 도움말](https://help.dropbox.com/integrations/connect-to-meta-muse) · [Dropbox 발표](https://blog.dropbox.com/topics/company/put-dropbox-project-context-to-work-meta-muse) | 연결 계정에서 이용 가능한 콘텐츠에 접근하고 개별 동작 권한은 설정할 수 있지만, 폴더별 허용 목록은 문서화되어 있지 않다. 11/8 화면에서는 검색·읽기, 다운로드, 쓰기, 공유 등이 모두 Allow(다운로드·쓰기 Custom Allow)였다. 합성 파일 세 개의 읽기·쓰기와 업로드 후 폴더 범위 검색이 성공했다. 11/14에는 PC 완전 종료 중 휴대폰 Muse에서 `Muse M4 Test - Synthetic` 폴더에 만든 `pc-off-return-20261114.md`가 PC 재시작 후 로컬 Dropbox 폴더에 도착했다. 18 bytes, `PC-OFF-RETURN-731`+LF, SHA-256 `DD753DDCF1DA01EADC5E50A23CA64C7B6708C882AC38806C0E718D74F94A307D`로 확인했다. 따라서 모바일 Muse 작성과 PC 종료 후 회수는 이 합성 폴더에서 통과했으나 실제 Vault 경로는 미시험이다. 커넥터가 지정 폴더만 기술적으로 접근하도록 강제하는지 확인되지 않았다. 403 표시의 원인은 미확정이다. Dropbox PC 절전 효과는 S0 전환·절전 중 클라우드 변경 시험이 없어 미판정이다. Dropbox 재실행 후 세 원본 검색과 폴더의 네 항목 목록은 성공했다. Chrome 업데이트·재시작 후 현재 Muse 화면에서 403 알림은 보이지 않았지만, 사용자의 반복 보고가 있어 해결 여부와 원인은 미확정이다. |
| B · GitHub private 사본 | Meta 공식 발표와 Muse Business 목록에서 확인. [Meta Connect 발표](https://www.meta.com/blog/meta-connect-2026-everything-we-announced/) | GitHub 계정과 시험 저장소 필요. 별도 커넥터 비용과 private 저장소 하나로 제한 가능한지는 미확인. |
| C · Google Drive 또는 Box | Muse 화면에서 두 항목 확인. Meta는 Box를 공식 발표했고 Google 연결 데이터에 대한 정책을 안내한다. [Meta Connect 발표](https://www.meta.com/blog/meta-connect-2026-everything-we-announced/) · [Meta 커넥터 도움말](https://www.meta.com/help/superintelligence/1687253048996149/) | Drive는 지정된 My Drive 합성 폴더에서 읽기·쓰기와 PC 수동 회수를 확인했다. Drive for desktop은 기존 컴퓨터 폴더를 `Computers`에 양방향 동기화할 수 있지만 Muse가 그 경로를 읽고 쓰는지는 미검증이다. 2026-11-14 Drive for desktop을 설치하고 `trial-vault`만 선택해 동기화 완료를 확인했다. Muse 커넥터의 `Computers` 접근은 다음 세션에서 시험한다. 커넥터의 폴더별 제한과 별도 비용은 미확인. Box의 실제 권한 범위도 미확인. |
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
| 3 | C · Google Drive | Drive의 `Computers` 경로를 Muse가 검색·읽기·쓰기 가능한지 확인한다. Drive for desktop을 설치하고 합성 `trial-vault`의 동기화 완료를 확인했다. Muse가 `Computers`에 접근하는지와 Muse 작성 파일이 PC로 자동 복귀하는지는 다음 세션에 시험한다. |
| 4 | A · Dropbox | 합성 폴더에서 Muse 읽기·쓰기·모바일 작성과 깨어 있는 PC 및 완전 종료 후 재시작 회수를 통과했다. 실제 Vault 경로와 폴더 접근의 기술적 강제는 미검증이다. Dropbox Backup은 단방향이며 기존 Vault 경로를 보존하는 표준 동기화도 미확인이다. |

후보는 제안 단계다. 저장소 시험 전에는 사본 규칙과 읽기·쓰기 범위를 먼저 확정한다. [M4 실습 순서](../../vl_roadmap/20261018_RoadMap_Muse-My-Workflow.md#m4---볼트-연결-해법--집과-밖을-끊김-없이)

최신 비교와 근거는 [작업별 경로표의 보조 저장소 비교](task-route-table.md#보조-저장소-비교-업데이트-2026-11-14)와 [11월 14일 M4 WorkLog](../../vl_worklog/20261114_M4_Muse-My-Workflow.md#보조-저장소-동기화-방식-리서치)를 참고한다.
