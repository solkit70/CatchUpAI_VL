---
title: "WorkLog - M4 볼트 연결 해법 · Claude Code Remote Control"
author:
  - Codex
created: 2026-11-08 04:16:06
tags:
  - muse-my-workflow
  - worklog
---

## 세션 정보

**날짜**: 2026-11-08
**Topic**: Muse-My-Workflow
**모듈**: M4 - 볼트 연결 해법 · 실습 3
**진행 에이전트**: Codex
**이전 WorkLog**: [11/5 M4 WorkLog](20261105_M4_Muse-My-Workflow.md#다음-세션에-넘길-것) — 가상 자료와 시나리오 비교표를 준비했다.

## 🎯 오늘의 학습 목표

E · Claude Code Remote Control을 Muse 외부의 대안 경로로 시험하고, 이어 C · Google Drive에서 지정한 가상 파일 3개를 읽고 결과를 회수한다. 사용자는 검토된 공개 사본 3개의 별도 Drive 업로드도 승인했다. 파일 삭제와 연결 해제는 별도 확인 전에는 하지 않는다.

## 📚 진행 내용

[가상 시험 폴더](../04-Vault-Connection/examples/trial-vault/)의 `continuation-note.md`, `event-catalog.md`, `planning-brief.md`만 볼트 밖 로컬 임시 시험 폴더에 복사했다. 세 사본 모두 원본과 SHA-256이 일치했다.

Claude Code v2.1.272를 해당 폴더에서 시작했다. `--restricted`로 파일 도구의 작업 범위를 제한하고 `--tools Read,Write`, `--strict-mcp-config`, `--no-chrome`을 적용했다. 새 결과 파일 이름은 `m4-e-remote-result.md`로 지정했다. E는 Claude Code가 집 PC의 로컬 세션을 휴대폰에서 조작하는 대안 경로다. [Claude Code 공식 안내](https://code.claude.com/docs/en/remote-control)

구독 계정 로그인 후 로컬 세션에서 `/rc active`를 확인했다. 집 PC에서 Claude에 가상 파일 3개를 읽고 현재 상태와 다음 작업을 요약하도록 요청했다. Claude는 겹치는 시간인 10:30–11:00을 찾고 다음 요청에서 새 파일에 결과를 쓰겠다고 답했다. 휴대폰에서 같은 세션을 열어 이어서 파일 작성을 요청하도록 안내했다.

### 결과 검증

휴대폰에서 보낸 요청을 같은 집 PC 세션이 받았고, 단일 파일 생성 확인 뒤 로컬 Claude Code가 29줄을 썼다. **04:25 PST**에 집 PC의 시험 폴더에 생성된 `m4-e-remote-result.md`를 직접 열었다. AI 글쓰기 실습과 자동화 실험실의 겹침 시간 **10:30–11:00**, 공개 데모 시간 **13:00–14:00**과 준비 목록이 가상 행사표·요청서와 일치했다.

시험 폴더에는 입력 3개와 결과 1개가 있었고, 세 입력 사본의 SHA-256이 시험 전 값과 볼트의 가상 원본에 모두 일치했다. 따라서 휴대폰에서 작업을 이어간 S4와 집 PC에서 결과를 확인한 S2는 가상 범위에서 통과했다. [시나리오 비교표](../04-Vault-Connection/guides/seamless-scenarios.md#시나리오-비교)

## C · Google Drive 시험

사용자가 Muse 로그인을 완료한 뒤 Settings → Connectors에서 Google Drive가 이미 연결된 것을 확인했다. 동작별 권한 설정은 보였으나 폴더 단위 접근 제한이나 OAuth 전체 범위는 이 화면에서 판정하지 못했다. 설정 변경이나 재연결은 하지 않았다.

Muse의 별도 대화에서 가상 시험 폴더의 `continuation-note.md`, `event-catalog.md`, `planning-brief.md`만 읽고 `m4-c-drive-result.md`를 같은 폴더에 만들도록 요청했다. 일회성 `Create` 확인을 승인한 뒤 Drive 폴더에서 입력 3개와 결과 파일을 확인했다. 결과 파일을 이 PC에 수동 다운로드했으며, `C:\Users\dougg\Downloads\m4-c-drive-result.md`의 내용도 열어 확인했다. 2026-12-04 AI 글쓰기 실습(10:00–11:00)과 자동화 실험실(10:30–11:30)이 10:30–11:00에 30분 겹치고, 공개 데모(13:00–14:00)는 겹치지 않는다. 준비 세부 정보가 원본에 없어 파일에 없는 내용을 만들지 않았다. 이는 S2의 수동 회수 확인이며, Muse 모바일 사용이나 자동 동기화 S5를 입증하지 않는다.

검토된 `visibility: public` 미리 보기 후보 3개는 `Muse M4 Approved Public Preview`라는 별도 Drive 폴더에 업로드되어 세 파일이 표시되는 것을 확인했다. 이 공개 사본들은 가상 시험 입력으로 사용하지 않았다. 실제 볼트 전체의 사본 범위 정책은 아직 결정하지 않았다.

## 🐛 문제 해결 로그

로컬 세션에 `Not logged in · Run /login`이 표시됐다. 사용자가 브라우저에서 로그인한 뒤 `/remote-control`을 실행해 해결했다. 결과의 YAML `author`에는 계정 이메일이 자동으로 들어갔다. 결과 원본은 시험 폴더에 그대로 두고 이 기록에는 이메일 주소를 옮기지 않았다.

## 📊 DoD 체크리스트

- [x] 해법 8가지 확인표 — 모든 행에 출처 종류 · 날짜
- [x] 시나리오 5개 × 시험한 해법 결과표 (실패·부분 검증·미시험 포함)
- [ ] 사본 규칙 박창수 승인 · 미리 보기 보고서에 내부 표시 문서 0개
- [x] 사용자 승인 후 첫 시험 업로드 실행, Drive 결과를 PC에서 수동 회수 확인
- [x] 작업 종류별 경로표 · 되돌리는 법 (초안, 실제 운영 경로 승인 대기)
- [x] 공개 문서에 실제 사본 설정 · 계정 정보 없음 · 산출물 폴더 README 작성
- [x] README 링크가 실제 파일을 가리키는지 확인 (`check_links.py`)
- [x] WorkLog (🎬 · 🎓 칸 포함) · Module Retrospective 작성 (M4 자체는 정책 결정 대기로 진행 중)

**진행 상태** — M4 7/8. E는 Muse 외부 대안 경로에서 가상 S2·S4 통과. C는 지정한 가상 Drive 폴더에서 읽기·결과 작성, PC 수동 회수를 확인했다. 모바일 접근·폴더 범위 강제는 미확인이다. Dropbox 데스크톱 앱 설정 후 깨어 있는 PC에서 로컬 동기화를 확인했다. 절전 요청 전후에도 네 파일은 로컬에서 사용 가능했으나 절전 전환과 절전 중 클라우드 동기화는 입증하지 못했다. 시나리오 표는 5개 시나리오별 D·E·C·A의 확인·부분 확인·미시험을 구분해 정리했다. S2의 C 결과는 커넥터 수준 합성 시험이며, 외부에서 시작한 작업을 집에서 이어간 시험이 아니다. S4의 C 결과는 PC 수동 회수 근거이며, 외부 연속 작업은 미시험이다. 작업별 경로와 중단·되돌림 초안 및 자동 미러를 끄고 수동 전달·로컬 처리를 권하는 임시 조합안을 작성했으나, 실제 볼트 사본 정책과 운영 경로는 승인 대기다.

## C · Google Drive 준비와 실행 기록

두 항목 승인에 따라 가상 자료 3개와 기존 `visibility: public` 미리 보기 후보 3개를 임시 로컬 폴더에 각각 준비했다. 후보 파일은 미리 보기 보고서에서 INCLUDE로 나온 세 파일이며, 각각의 frontmatter에 `visibility: public`이 있고 `visibility: internal` 표식과 `🔒 내부 자료` 표식이 없음을 확인했다. 원본 볼트 파일은 수정하지 않았다.

개인 Drive에서 `Muse M4 Test - Synthetic` 폴더를 만들었다. 처음에는 브라우저 자동화가 Windows 파일 선택 창을 감지하지 못했다. 사용자가 선택 창이 뒤늦게 열리는 것을 확인해 주었고, 재시도에서는 업로드 버튼을 누르기 전에 브라우저의 파일 선택 이벤트를 기다리도록 설정했다. `continuation-note.md`, `event-catalog.md`, `planning-brief.md`를 올린 뒤 Drive의 `3 uploads complete` 메시지와 파일 세 개를 확인했다.

승인된 `public` 후보 3개는 개인 Drive의 별도 폴더 `Muse M4 Approved Public Preview`에 올렸다. Drive의 `3 uploads complete` 메시지와 폴더에 표시된 세 Markdown 파일을 확인했다.

Muse에서 기존 Drive 연결을 확인하고 가상 파일 시험과 결과의 PC 수동 회수를 완료했다(위 「C · Google Drive 시험」). 연결을 끊거나 시험 파일을 삭제하지 않았다.

## 미리 보기 정책 검토 및 Dropbox 후보 조사

볼트 안의 내부 미리 보기 보고서를 다시 확인했다. 보고서에 표시된 공개 후보 3개는 사용자가 별도로 승인해 Drive에 올린 후보와 일치한다. 보고서 자체는 `visibility: internal`이므로 이 WorkLog와 외부 비교 문서에 경로·집계 세부를 복사하지 않았다. 이 승인 범위는 지정 후보 3개의 별도 Drive 업로드이며, 전체 볼트 사본 정책 확정이나 추가 저장소 연결 승인을 뜻하지 않는다.

사용자가 새 Dropbox 계정을 만들고 Muse에 연결했다. 최신 Connectors 화면에서 모든 동작별 권한은 **Allow**(다운로드·쓰기 권한은 Custom Allow)였다. 사용자는 Dropbox 사이트의 “Access other apps and services on this device” 확인에 이번 파일 업로드 범위로 Allow를 승인했다. 개인 전용 `Muse M4 Test - Synthetic` 폴더에 가상 파일 세 개를 업로드했고 Dropbox에서 3/3 완료를 확인했다. 업로드 전 정확한 파일명 검색은 0건을 반환했지만, 업로드 뒤 검색은 성공했다. 같은 폴더 경로를 지정해 세 파일을 읽고 `m4-dropbox-result.md`를 작성했다. Dropbox 폴더에는 원본 3개와 결과 1개가 있으며 결과 미리 보기에서 읽기·작성 내용을 확인했다. 원본은 수정되지 않았고 삭제나 연결 해제도 하지 않았다.

결과에는 2026-12-04의 “AI 글쓰기 실습”과 “자동화 실험실”이 10:30–11:00에 30분 겹친다고 적혔다. “공개 데모 시간”은 13:00–14:00, 가상실 A로 표시되며, 원본 세 자료에는 추가 준비 세부 항목이 없어 새로 만들어 넣지 않았다. 영상용으로 [권한 화면](../04-Vault-Connection/assets/20261108-muse-dropbox-permissions.jpg), [기기 접근 확인](../04-Vault-Connection/assets/20261108-dropbox-permission-prompt-1.jpg), [업로드 완료](../04-Vault-Connection/assets/20261108-dropbox-upload-success.jpg), [파일 4개](../04-Vault-Connection/assets/20261108-dropbox-four-files.jpg), [Muse 결과](../04-Vault-Connection/assets/20261108-muse-dropbox-analysis-result.jpg), [Dropbox 결과 상단](../04-Vault-Connection/assets/20261108-dropbox-result-content-top.jpg), [결과 하단](../04-Vault-Connection/assets/20261108-dropbox-result-content-bottom.jpg), [결과 검증 화면](../04-Vault-Connection/assets/20261108-dropbox-result-verified.jpg)을 저장했다. Dropbox 공식 안내는 연결 시 계정에서 접근 가능한 파일·폴더를 Muse가 사용할 수 있고, 파일 미리 보기는 Muse에서 지원되지 않으며, 연결 데이터가 Meta 정책에 따라 모델 성능 개선에 쓰일 수 있다고 알린다. [공식 도움말](https://help.dropbox.com/integrations/connect-to-meta-muse) · [Dropbox 안내](https://blog.dropbox.com/topics/company/put-dropbox-project-context-to-work-meta-muse)

### Dropbox 검색·권한 범위 후속 확인

재시험은 사용자 승인 후 읽기 전용으로 진행했다. 정확한 세 파일명을 `title_only` 검색 모드와 `/Muse M4 Test - Synthetic` 경로로 지정했을 때 각 파일이 1건씩 검색됐고, 같은 경로의 비재귀 목록에는 세 원본과 `m4-dropbox-result.md` 총 4개가 표시됐다. 파일 내용은 열지 않았으며 모든 Dropbox 작업이 `ok: true`로 보고됐다. 첫 0건 검색은 1:13 PM PST, 파일 업로드는 Dropbox 서버 시각 21:42 UTC(1:42 PM PST)이므로 업로드 전 검색이었다. 따라서 검색 누락 원인은 권한 문제가 아니라 검색 시점과 업로드 순서로 설명된다.

2026-11-08 갱신된 Dropbox 도움말은 Muse가 연결 계정을 통해 이용 가능한 콘텐츠를 검색·가져오며, 읽기·다운로드·생성·삭제·공유 등의 개별 동작 권한을 설정할 수 있다고 설명한다. 도움말에는 단일 폴더만 허용하는 범위 설정이 없다. 그러므로 지정 폴더만 사용하라는 Muse 요청은 작업 지시의 범위를 정할 뿐, 커넥터 권한이 해당 폴더로 기술적으로 제한됐다는 증거가 아니다. Muse 하단에는 `Error 403 - Forbidden` 배너가 계속 보였으나, 재시험의 Dropbox 검색·목록 요청은 모두 `ok: true`로 보고됐다. 이 배너와 Dropbox 작업 오류가 연결된 증거는 없어 배너의 원인은 미확정이다. [Dropbox 공식 도움말](https://help.dropbox.com/integrations/connect-to-meta-muse#security-and-permissions) · [시나리오 비교](../04-Vault-Connection/guides/seamless-scenarios.md#시나리오-비교)


### Dropbox 절전 시험 후 읽기 전용 재확인

Dropbox 앱을 실행한 상태에서 Muse의 기존 대화로 지정된 개인 시험 폴더만 다시 확인했다. `continuation-note.md`, `event-catalog.md`, `planning-brief.md` 각각이 폴더 한정 `title_only` 검색에서 1건씩 나왔고, 폴더의 비재귀 이름·메타데이터 목록은 결과 파일을 포함해 4개였다. 네 Dropbox 호출 모두 `ok: true`였으며 파일 내용을 열거나 외부 상태를 바꾸지 않았다.

Muse의 응답은 403 배너를 볼 수 없다고 했지만, 응답을 받은 뒤 읽은 Muse UI 접근성 상태에는 `Error 403 - Forbidden` 알림 항목이 계속 나타났다. 현재 화면 캡처의 본문에는 배너가 오버레이로 나타나지 않았고, Dropbox 작업은 모두 성공했다. 따라서 403은 앱 UI의 별도 알림 상태로 관찰되지만 원인은 여전히 미확정이다. 이 재시험은 영상용으로 대화 화면을 캡처했으나 계정 식별 정보가 함께 보이는 화면은 저장하지 않았다.
### PC 자동 회수·모바일 접근 점검

사용자가 Dropbox 데스크톱 앱을 설치한 뒤 설정을 마쳤다(무료 Basic 유지, 유료 업그레이드 없음). Windows 파일 탐색기에서 `Muse M4 Test - Synthetic` 폴더가 나타났고, `continuation-note.md`, `event-catalog.md`, `planning-brief.md`, `m4-dropbox-result.md` 네 파일 모두 상태가 **Available on this device**로 표시됐다. 따라서 PC가 깨어 있는 동안 클라우드 시험 폴더의 네 파일이 로컬 Dropbox 폴더에 자동으로 도착하는 것을 확인했다. 이 확인은 데스크톱 앱 설정 후의 깨어 있는 PC 동기화를 입증하지만 Windows Sleep 전후 동작이나 실제 모바일 Muse 접근은 입증하지 않는다.
### Windows Sleep 요청 후 상태 확인

사용자가 승인한 뒤 Windows의 절전 API로 S0 저전력 유휴 진입을 요청했다. 호출은 반환했고 PC는 다시 응답했다. 시험 직후 Dropbox 프로세스가 실행 중이지 않아 설치된 `C:\Program Files (x86)\Dropbox\Client\Dropbox.exe`를 실행했고 Dropbox 프로세스 두 개가 시작됐다. 파일 탐색기에서 시험 폴더의 파일 네 개 모두 계속 **Available on this device**로 표시됐다.

이 결과는 절전 요청 전후 로컬 파일 상태가 유지된 것만 보여 준다. 이 PC는 S0 저전력 유휴(네트워크 연결)를 지원하며, 일반 S3는 지원하지 않는다. 시스템 이벤트 로그 읽기는 권한 오류가 났고 `powercfg /lastwake`는 Wake History Count 0을 반환해 실제 S0 진입·복귀를 독립적으로 검증하지 못했다. 절전 중 클라우드 파일 변경을 발생시키지 않았으므로 절전 중 동기화 여부나 앞선 문제의 원인을 판정할 수 없다. 화면 캡처는 작업 중 확인했지만 인접한 브라우저에 계정 식별 정보가 표시되어 영상용 assets에는 저장하지 않았다.


### Chrome 업데이트 후 Muse 확인

사용자가 Chrome 업데이트와 Relaunch를 완료했다고 알려 주어 설치 파일 버전 `157.0.8103.39`를 확인했다. Chrome 재시작 뒤 Muse의 같은 대화를 다시 열었을 때 UI 접근성 상태와 화면에서 `Error 403 - Forbidden` 알림이 보이지 않았다. 이후 승인된 읽기 전용 재확인에서 `continuation-note.md`, `event-catalog.md`, `planning-brief.md`가 각각 폴더 한정 검색에서 1건씩 나왔고, 폴더 목록은 결과 파일을 포함해 네 항목이었다. 모든 Dropbox 요청은 `ok: true`였으며 내용 열람이나 파일 변경은 없었다.

브라우저 재시작 후 현재 대화에서는 403 표시가 보이지 않는 관찰을 기록한다. 사용자가 평소 Muse 사용 중 해당 오류를 자주 본다고 했으므로 해결됐다고 단정하지 않는다. 브라우저 업데이트가 원인·해결책인지도 인과관계가 입증되지 않았다. 화면 캡처에서 계정 식별 정보는 보이지 않았으며, 가상 파일 이름과 현재 결과를 확인할 수 있었다.
## 💡 Daily Retrospective

- **잘한 점** — E에서는 모바일 요청 후 집 PC의 결과와 입력 해시를 대조했다. C에서는 Muse의 Drive 결과를 실제 PC 다운로드 파일까지 대조했다.
- **개선할 점** — C의 연결 화면에 보이는 동작별 권한과 폴더 단위 범위는 별개로 기록해야 한다. 이번 화면만으로는 폴더 제한을 입증할 수 없었다.
- **인사이트** — E는 Muse 밖의 원격 세션 경로이고 C는 Muse의 연결된 Drive 저장소 경로다. 두 경로 모두 같은 결과물을 만들 수 있지만, S4와 S5 검증에는 다른 시험이 필요하다.

## 🎬 영상 재료

휴대폰의 가상 작업 요청과 집 PC의 새 결과 파일을 나란히 보여 줄 수 있다. 영상용 결과 화면은 계정 이메일이 담긴 작성자 필드를 제외하고 구성한다.

## 🎓 가르칠 때

가상 행사 표의 겹침 시간 10:30–11:00을 기대값으로 제시한다. 실제 결과가 맞는지, 휴대폰 요청으로 집 PC에 파일이 생성됐는지, 입력 해시가 유지됐는지를 각각 확인한다.

## Module Retrospective — M4 중간 회고 (모듈은 계속 진행)

### 학습 목표 달성도
- [x] 8개 후보를 비교하고 5개 시나리오의 D·E·C·A 근거를 구분했다. E는 Muse 밖의 대안으로 기록했다.
- [ ] 실제 볼트 사본 규칙을 확정하고 박창수 승인을 받는다. 내부 표시 문서 제외 결과는 확인됐지만 정책 승인은 아직 없다.
- [x] 미리 보기 방식과 분류 경계를 검토했다. 실제 복사·자동화는 실행하지 않았다.
- [x] 승인된 시험 범위에서 Drive·Dropbox 커넥터와 결과 회수 경로를 확인했다. 일부는 PC 브라우저 시험이고 모바일·절전·폴더 권한 강제는 미확인이다.
- [ ] 실제로 사용할 조합을 승인하고 가동한다. 현재 경로표는 초안이며 운영 조합은 미정이다.

### 핵심 인사이트
1. 클라우드 커넥터에서 읽기·쓰기 성공은 동기화나 폴더별 기술 권한 제한을 증명하지 않는다. 결과 회수도 수동 다운로드와 깨어 있는 PC의 Dropbox 데스크톱 동기화를 분리해 기록해야 한다.
2. Muse 안의 저장소 연결과 E · Claude Code Remote Control은 서로 다른 실행 모델이다. E는 Muse 자체 연결이 아닌 외부 대안이며 집 PC 세션이 켜져 있어야 한다.
3. 실제 볼트 정책은 포함할 경로·자료 등급·저장 위치·운영 주기가 정해져야 승인 가능한 형태가 된다. 내부 자료는 볼트 밖으로 내보내지 않는 경계를 유지한다. 현재 검토안은 자동 미러 없이 수동 전달과 로컬 작업을 우선하며, Dropbox·Drive의 합성 시험 성공을 실제 볼트 연결 승인으로 간주하지 않는다.

### 다음 모듈 준비
M4를 닫기 전에 사본 정책과 운영 경로의 미결정 항목을 검토하고 승인 범위를 기록한다. 그 뒤에만 실제 경로 실행 여부를 판단하고 M5 시작 일정을 갱신한다. 삭제·연결 해제는 별도 확인 전에는 하지 않는다.

## 다음 세션에 넘길 것

1. Dropbox 검색은 업로드 뒤 성공했다. Dropbox 데스크톱 앱 설정 뒤 네 파일 모두 로컬에서 Available on this device로 표시되어 깨어 있는 PC의 자동 동기화를 확인했다. 절전 API 요청 뒤 네 파일의 로컬 상태는 유지됐지만 S0 진입·복귀와 절전 중 동기화는 입증하지 못했다. 폴더 범위의 기술적 강제 여부와 Muse 403 배너 원인도 미확정이다. Dropbox 실행 후 지정 파일 3건 검색과 4개 목록은 모두 성공했다.
2. 실제 모바일 기기에서 Muse 접근을 확인해야 한다. 수면 효과를 판별하려면 절전 중 클라우드 변경을 만들고 복귀 뒤 도착 여부를 관찰할 수 있는 별도 시험 경로가 필요하다. C의 모바일 접근·자동 동기화·폴더 제한도 미시험이다.
3. 전체 볼트 사본 규칙은 여전히 초안이다. 시험 파일과 E 원격 세션은 보존했고, 삭제나 연결 해제는 실행 전에 사용자에게 묻는다.
