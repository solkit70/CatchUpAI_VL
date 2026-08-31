# WorkLog - M9: Codex Remote 검증과 세팅

**날짜**: 2026-08-30
**Topic**: Claude-Code-Mobile-Remote-Execution
**모듈**: M9 - Codex Remote 검증과 세팅
**작성자**: Codex with VibeLearn AI
**상태**: 오늘 세션 종료 - ChatGPT Desktop/Codex 설치, iPad Remote 연결, 읽기/쓰기/한글 입력, 운용 규칙 부분 확정 완료

## 오늘의 학습 목표

- M9 1단계 이후 남은 2단계 작업을 복습한다.
- 라이브 방송에 지장을 줄 수 있는 작업과 안전한 점검 작업을 분리한다.
- Codex Remote 설치·페어링·경계 테스트를 방송 후 실행 가능한 체크리스트로 유지한다.
- 사용자 재승인 후 ChatGPT Desktop 설치와 iPad Remote 연결을 진행했다. Computer Use와 SSH 호스트 등록은 오늘 세션에서 실행하지 않는다.

## 진행 내용

### 1. 이전 학습 상태 확인

최신 Roadmap과 `20260828_M9_Claude-Code-Mobile-Remote-Execution.md`를 확인했다. M9는 1단계인 문서 조사, 구조 비교, 절차서 작성이 완료된 상태였다. 2단계 중 ChatGPT 데스크톱 앱 설치, 새 Codex view 실행, iPad Remote 연결, 프로젝트 생성, 현재 위치 구조 읽기 테스트를 이번 세션에서 완료했다. 파일 쓰기 최소 테스트도 성공했다. 푸시 알림, 잠자기 복구, 운용 규칙 최종 확정은 대기 상태다.

### 2. 공식 문서 재확인

2026-08-30 기준 공식 OpenAI 문서 `learn.chatgpt.com/docs/remote-connections`를 다시 확인했다. Remote 연결은 ChatGPT 데스크톱 앱에서 호스트를 켜고 모바일 앱에서 같은 계정과 워크스페이스로 접근하는 구조이며, Handoff는 연결된 호스트 간 chat과 Git 상태를 이전하는 기능으로 설명된다.

### 3. 방송 중 안전 범위 재설계

사용자가 라이브 방송 중이라고 알려 주었으므로, 방송에 영향을 줄 수 있는 작업을 모두 제외했다. 처음에는 설치, 권한 변경, 계정 연결, 포커스 전환, 화면 조작, 재부팅 가능성이 있는 작업을 제외했다. 이후 사용자가 화면 포커스 방해와 재부팅 거부가 가능하다고 판단해 ChatGPT Desktop 설치만 예외적으로 승인했다. 오늘의 성공 기준은 방송을 방해하지 않는 범위에서 ChatGPT Desktop 설치, iPad Remote 연결, 읽기 전용 구조 확인까지 검증하고, 파일 쓰기 최소 테스트까지 성공했고, 푸시 알림과 잠자기 복구 같은 장시간 경계 테스트는 방송 후로 남기는 것이다.

### 4. 절차서 업데이트

`09-Codex-Remote/lab/setup-procedure.md`에 `방송 중 안전 모드 (2026-08-30)` 섹션을 추가했다. 이 섹션은 방송 중 하지 않을 작업과 허용할 작업을 분리한다.

## 문제 해결 로그

| 문제 | 원인 | 해결/기록 |
|---|---|---|
| 원래 계획에 설치·호스트 등록이 포함됨 | ChatGPT 데스크톱 앱 설치와 연결 설정은 방송 중 화면 포커스, 권한 요청, 재시작 가능성을 만들 수 있음 | 방송 중 안전 모드로 범위를 축소 |
| Computer Use와 SSH 호스트 등록의 범위가 큼 | 화면 조작 권한과 네트워크/SSH 보안 설정을 건드릴 수 있음 | 1차 세팅에서도 제외, 방송 중에는 명시적으로 금지 |
| Codex Remote 데이터 저장 범위가 문서상 명확하지 않음 | 공식 문서에 Claude Remote Control처럼 저장 범위 설명이 분명히 보이지 않음 | 계정 데이터 관리 설정 확인을 방송 후 실행 전 필수 점검으로 유지 |

## DoD 체크리스트

**1단계**

- [x] Codex Remote 연결 구조 문서화 (Mermaid 다이어그램 포함)
- [x] Handoff · SSH 호스트 등록 · Computer Use 정리
- [x] SSH · Claude RC · Codex Remote 3자 비교표 작성
- [x] 이 환경의 세팅 요건 점검
- [x] 설치·페어링 절차서 작성 (경계 테스트 7항목 포함)
- [x] 운용 규칙 잠정안 작성
- [x] WorkLog 작성

**2단계 - 방송 중 안전 모드**

- [x] 방송 중 하지 않을 작업 분리
- [x] 방송 중 허용 가능한 저위험 점검 항목 분리
- [x] 사용자 재승인 후 ChatGPT Desktop 설치만 예외적으로 진행
- [x] 설치 완료 확인: OpenAI.ChatGPT-Desktop 1.2026.190.0
- [x] iPad Remote 연결 확인
- [x] Codex 프로젝트 생성 후 현재 위치 구조 읽기 테스트 성공
- [x] Computer Use·SSH 호스트 등록은 보류

**2단계 - 방송 후 대기**

- [x] ChatGPT 데스크톱 앱 설치
- [x] 호스트 등록 + 모바일 QR 페어링
- [>] 경계 테스트 7항목 수행 (읽기/쓰기 테스트 완료, 장시간 테스트 대기)
- [>] 절차서를 실기록으로 전환 (설치, 연결, 읽기/쓰기 테스트 기록 완료)
- [x] 운용 규칙 부분 확정

## Daily Retrospective

### What went well

설치로 바로 들어가지 않고, 현재 사용자의 환경 제약을 먼저 반영했다. 라이브 방송 중에는 원격 제어 기능 자체보다 운영 안전성이 더 중요하므로, M9 2단계를 안전 점검과 실제 세팅으로 분리한 판단이 적절했다.

### What could be improved

다음 세션에서는 사용자가 방송 중인지, 재부팅이나 화면 전환이 가능한 상태인지 먼저 물어보면 더 좋다. 원격 실행, 데스크톱 앱 설치, 권한 설정은 학습 작업처럼 보이지만 실제 운영 환경에는 영향을 줄 수 있다.

### Insights

1. 원격 실행 학습에서는 "기능이 가능한가"보다 "지금 실행해도 되는가"가 먼저다.
2. 설치와 페어링은 단순한 체크리스트가 아니라 계정, 화면, 권한, 알림, 잠자기 정책을 건드리는 운영 작업이다.
3. 방송 중에는 실험 성공보다 환경 안정성을 우선해야 한다.

### Tomorrow's focus

- iPadOS ChatGPT 알림 권한과 Focus/Do Not Disturb 설정 점검
- Windows 잠자기/복귀 후 iPad Remote 재연결 테스트 수행
- 남은 경계 테스트 결과를 setup-procedure.md에 반영하고 M9 완료 여부 판단

## 참조 및 산출물

- [09-Codex-Remote/lab/setup-procedure.md](../09-Codex-Remote/lab/setup-procedure.md)
- [09-Codex-Remote/decisions/codex-remote-usage-rules.md](../09-Codex-Remote/decisions/codex-remote-usage-rules.md)
- [vl_worklog/20260828_M9_Claude-Code-Mobile-Remote-Execution.md](20260828_M9_Claude-Code-Mobile-Remote-Execution.md)
- 공식 문서: https://learn.chatgpt.com/docs/remote-connections
- 실무 워크플로우: https://developers.openai.com/blog/mastering-codex-remote-for-engineering

### 5. ChatGPT Desktop 설치 시도 및 결과

사용자가 방송 중이라도 화면 포커스 방해 정도는 감수할 수 있고, 재부팅 요청이 나오면 거부하겠다고 재승인했다. 공식 `chatgpt.com/download` 페이지와 Microsoft Store 앱 링크를 열었고, 공식 Microsoft 설치 링크에서 `ChatGPT-Windows-Installer.appinstaller`를 임시 폴더로 다운로드해 실행했다.

설치 후 `Get-AppxPackage -Name '*ChatGPT*'`로 확인한 결과 `OpenAI.ChatGPT-Desktop 1.2026.190.0` 패키지가 등록되었다. 재부팅, 로그아웃, 호스트 등록, QR 페어링, Computer Use, SSH 호스트 등록은 수행하지 않았다.


### 6. Microsoft Store 설치와 appinstaller 오류 해석

사용자 스크린샷에서 Microsoft Store의 `ChatGPT Classic` 앱은 `OpenAI` 게시자의 공식 ChatGPT Windows 앱으로 표시되며, Store 쪽에는 `Open` 버튼이 보여 설치 자체는 완료된 상태로 판단된다. 로컬 확인에서도 `OpenAI.ChatGPT-Desktop 1.2026.190.0` 패키지가 등록되어 있었다.

두 번째 스크린샷의 `Cannot open app package` / `The .appinstaller file is invalid.` 메시지는 Store 설치 실패가 아니라, 별도로 다운로드해 실행한 `.appinstaller` 파일을 Windows App Installer가 열지 못한 오류로 해석한다. 따라서 현재 상태는 "앱은 Store를 통해 설치됨, 별도 appinstaller 실행은 실패"다.

남은 확인은 설치된 앱이 Codex Remote에 필요한 새 ChatGPT Desktop인지, 아니면 Classic 앱만 설치된 것인지 구분하는 것이다. 앱을 열어 좌상단 또는 사이드바에 `Codex`, `Work`, `Connections`, `Control this Mac or PC` 항목이 보이는지 확인해야 한다.

### 7. Connections 메뉴 미노출 판정

사용자가 ChatGPT Classic 앱 실행과 인증을 완료한 뒤 Settings에서 `Connections`, `Remote`, `Control this Mac or PC`를 검색했지만 결과가 없고, 왼쪽 설정 목록에도 `Connections` 메뉴가 없다고 확인했다. 화면에는 `Chat`과 `Work` 전환, `Security and login` 안의 `Codex CLI` 연결, `Enable device code authorization for Codex` 항목만 보인다.

따라서 현재 상태는 `ChatGPT Classic 설치 및 로그인 완료`, `Codex CLI 계정 인증 확인`, `Codex Remote 호스트 등록 메뉴 미노출`로 판정한다. 공식 문서 기준 Remote 세팅은 `Settings > Connections > Control this Mac or PC`에서 시작해야 하므로, 이 메뉴가 없는 현재 화면에서는 모바일 Remote 페어링을 계속 진행할 수 없다.

### 8. 업데이트 확인 후에도 변화 없음

사용자가 `Settings > General > App updates > Check for updates`를 실행했지만 앱 상태와 메뉴 구성에 변화가 없다고 확인했다. 따라서 2026-08-30 현재 이 Windows 환경에서는 ChatGPT Classic `1.2026.190` 설치와 로그인, Codex CLI 인증 연결까지는 확인되었지만, 공식 문서의 `Settings > Connections > Control this Mac or PC` 메뉴는 노출되지 않는다.

오늘은 모바일 QR 페어링과 경계 테스트를 진행하지 않는다. 다음 조사는 새 ChatGPT Desktop 배포/롤아웃 여부, 계정의 Codex Local/Remote 권한, 또는 별도 Codex 앱 업데이트 경로 확인으로 넘긴다.

### 9. iPad Remote 연결 및 읽기 테스트 성공

사용자가 새 ChatGPT Desktop 앱의 Codex view를 실행했고, `Connections > Control this PC` 화면에서 `Allow connections`가 켜진 상태와 `iOS 26.6 iPad` 연결을 확인했다. 이후 iPad에서 새 프로젝트를 만들어 현재 위치에서 작업할 수 있도록 설정했고, Codex가 현재 vault 구조를 읽어 설명하는 데 성공했다.

스크린샷 기준으로 새 앱은 왼쪽 상단에 `Codex` view가 표시되며, 프로젝트 목록에 `Changsoo_Vault`와 사용자가 만든 `아이패드 작업 가능 여부 확인` 프로젝트가 보인다. Codex 응답은 `Journal`, `Limitless`, `Topics`, `Projects`, `Roundup`, `_Settings_`, `.gobi`, `.git`, `AGENTS.md`, `CLAUDE.md`, `orchestrator.yaml`, `VAULTS.md`, `BRAIN.md`, `PUBLISH.md` 등 현재 위치의 구조를 올바르게 요약했다.

따라서 M9의 핵심 목표인 "iPad에서 Codex Remote로 Windows PC의 현재 작업 위치를 읽고 작업할 수 있는가"는 읽기 기준으로 성공했다. 파일 쓰기 최소 테스트까지 성공했지만, 푸시 알림과 잠자기 복구까지는 아직 끝난 것이 아니므로 경계 테스트는 부분 완료로 남긴다.

## 영상화 관점 정리

### 이야기 흐름

이번 세션은 단순한 설치 성공기가 아니라, 원격 AI 코딩 환경을 실제로 세팅할 때 생기는 혼선을 해결해 가는 과정을 보여 준다. 처음에는 방송 중 안정성을 이유로 설치를 미뤘고, 이후 사용자가 화면 포커스 방해와 재부팅 거부를 감수할 수 있다고 판단해 설치만 제한적으로 진행했다. Microsoft Store의 `ChatGPT Classic` 설치, `.appinstaller` 오류, Classic 앱의 `Connections` 메뉴 미노출, 새 ChatGPT Desktop/Codex 앱 발견, iPad Remote 연결 성공이 순서대로 이어졌다.

### 핵심 장면 후보

| 장면 | 내용 | 교육 포인트 |
|---|---|---|
| 1 | 방송 중 설치를 할지 말지 판단 | 원격 도구 세팅은 기능보다 운영 상황을 먼저 본다 |
| 2 | Microsoft Store의 `ChatGPT Classic` 설치 | 공식 앱이어도 원하는 기능이 없을 수 있다 |
| 3 | `.appinstaller` 오류 | 설치 실패와 앱 패키지 실행 실패를 분리해서 해석한다 |
| 4 | Classic 앱에서 `Codex CLI` 연결 확인 | CLI 인증과 Remote host 등록은 다르다 |
| 5 | 새 ChatGPT Desktop/Codex 앱 실행 | `Codex view`가 보이는지가 결정적 단서다 |
| 6 | `Connections > Control this PC`에서 iPad 연결 | Remote host 등록 성공 지점 |
| 7 | iPad에서 현재 vault 구조 읽기 | 모바일은 조작 화면, Windows PC가 실행/파일 접근 위치라는 모델 검증 |

### 공개 전 마스킹 필요 항목

- 계정 이메일, 프로필 이름, 프로젝트명 중 공개하지 않을 항목
- vault의 실제 폴더명 중 개인 정보가 드러나는 항목
- Recent chat 제목과 pinned/project 목록
- iPad 기기명, 호스트명, 사용자 계정명
- `.git`, `.gobi`, `BRAIN.md`, `PUBLISH.md` 등 내부 운영 파일의 세부 내용

### 남은 테스트 계획

방송 중에는 읽기 테스트까지만 성공으로 인정한다. 이번 세션에서 파일 쓰기 최소 테스트까지 성공했다. 다음 세션에서는 푸시 알림과 잠자기 복구를 각각 별도 항목으로 기록한다. Computer Use와 SSH host 등록은 여전히 제외한다.

### 10. 파일 쓰기 최소 테스트 성공

사용자가 iPad Remote Codex에서 최소 파일 쓰기 테스트를 수행했고 성공했다고 보고했다. 로컬 검색으로 `04-Remote-Execution-Lab/lab/codex-remote-test-20260830.txt` 파일이 존재하며, 내용이 `Codex Remote iPad write test 2026-08-30.` 한 줄임을 확인했다.

이 테스트로 iPad Remote가 Windows PC의 현재 프로젝트 위치에서 실제 파일 쓰기까지 수행할 수 있음이 확인됐다. 단, 이것은 작은 단일 파일 쓰기 검증이며, 대량 수정, Git 작업, 푸시 알림, 잠자기 복구 안정성까지 검증한 것은 아니다.

### 11. 한글 입력 파일 쓰기 테스트 성공

사용자가 iPad Remote Codex에서 기존 테스트 파일에 한글 입력을 추가했다. 로컬 확인 결과 `04-Remote-Execution-Lab/lab/codex-remote-test-20260830.txt`의 2번째 줄에 `안녕하세요`가 정상적으로 기록되어 있었다. 자모 분리나 인코딩 깨짐은 관찰되지 않았다.

이 테스트로 iPad Remote Codex에서는 Termius에서 겪었던 한글 IME 자모 분리 문제가 재현되지 않음을 확인했다. 단, 긴 한국어 문장, 여러 줄 편집, Markdown 문서 수정에서도 같은 품질이 유지되는지는 별도 확장 테스트가 필요하다.

### 12. 푸시 알림 테스트 - 노트북 알림 수신

사용자가 푸시 알림 테스트를 수행한 결과, 알림 메시지가 iPad가 아니라 Windows 노트북으로 도착했다고 보고했다. 따라서 현재 판정은 `호스트/데스크톱 알림 수신 성공`, `iPad 모바일 푸시 수신은 미수신`이다.

이 결과는 Codex Remote 작업 완료 이벤트가 알림 체계로 전달된다는 점은 확인하지만, 모바일 백그라운드 푸시가 동작한다는 증거는 아니다. 사용자가 이후 iPad 쪽에는 알림이 오지 않았다고 확인했으므로, 2026-08-30 기준 iPad 모바일 푸시는 미수신으로 기록한다.


### 13. 운용 규칙 부분 확정

사용자가 오늘 기준으로 확정 가능한 Codex Remote 운용 규칙 정리를 승인했다. `09-Codex-Remote/decisions/codex-remote-usage-rules.md`를 부분 확정판으로 갱신했다.

확정한 규칙은 Codex 작업은 iPad Remote로 가능하되, 방송 중에는 읽기, 작은 파일 쓰기, 짧은 문서 수정까지만 허용한다는 것이다. 대량 수정, `git commit`, `git push`, 설치, 권한 변경, 장시간 작업은 방송 중 하지 않는다. Computer Use와 SSH host 등록은 별도 승인 전까지 사용하지 않는다.

아직 최종 확정하지 않는 항목은 iPad 푸시 알림 신뢰 여부, Sleep 후 자동 복구 여부, 장시간 작업 안정성, 여러 Codex 프로젝트 동시 사용 규칙이다.

## 오늘 세션 마무리

오늘은 방송 중이라는 제약이 있었지만, M9의 핵심 실사용 검증을 상당 부분 완료했다. 처음에는 ChatGPT Classic 앱과 새 ChatGPT Desktop/Codex 앱을 구분하지 못해 `Connections` 메뉴를 찾지 못했고, `.appinstaller` 오류도 있었지만, 최종적으로 새 Codex view를 실행하고 `Connections > Control this PC`에서 iPad 연결까지 성공했다.

검증 결과 iPad Remote Codex는 현재 vault 구조를 읽을 수 있었고, `codex-remote-test-20260830.txt` 파일 생성과 `안녕하세요` 한글 입력까지 정상 동작했다. Windows 노트북 알림은 수신됐지만 iPad 푸시는 오지 않았고, 잠자기/복귀 테스트는 방송 중이라 수행하지 않았다.

오늘 기준으로 Codex Remote는 `읽기`, `작은 파일 쓰기`, `짧은 문서 수정`에는 사용할 수 있는 상태로 본다. 다만 방송 중 대량 수정, `git commit`, `git push`, 설치, 권한 변경, 장시간 작업은 금지하고, Computer Use와 SSH host 등록은 별도 승인 전까지 사용하지 않는 것으로 부분 확정했다.

### 세션 종료 상태

| 항목 | 상태 |
|---|---|
| ChatGPT Desktop/Codex 앱 설치 | 완료 |
| iPad Remote 연결 | 완료 |
| 현재 위치 구조 읽기 | 완료 |
| 파일 쓰기 최소 테스트 | 완료 |
| 한글 입력 테스트 | 완료 |
| Windows 알림 | 완료 |
| iPad 푸시 알림 | 미수신 |
| 잠자기/복귀 재연결 | 미실행 |
| 운용 규칙 | 부분 확정 |

### 다음 세션 시작점

다음에 이 Topic을 이어서 열면 M9의 남은 2개 항목만 처리한다. 첫째, iPadOS의 ChatGPT 알림 권한과 Focus 설정을 확인해 iPad 푸시 미수신 원인을 점검한다. 둘째, 방송이 아닌 상태에서 Windows 잠자기/복귀 후 iPad Remote가 재연결되는지 확인한다. 이 두 항목까지 정리하면 M9를 완료 처리할 수 있다.


