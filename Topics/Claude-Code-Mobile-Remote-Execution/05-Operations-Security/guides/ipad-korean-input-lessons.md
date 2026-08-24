# iPad Termius에서 Claude Code 한글 입력 문제

## 현상

iPad Termius에서 Windows 노트북에 SSH로 접속한 뒤 Claude Code를 실행하면, 한글 입력이 완성형 음절로 들어가지 않고 자모 단위로 분리되어 입력된다.

사용자가 관찰한 예:

```text
프로세스 -> ㅍㅡㄹㅗㅅㅔㅅㅡ
```

영어 입력은 정상 동작했다. 이 현상은 SSH 접속, Tailscale, Windows OpenSSH Server, Claude Code 설치 문제가 아니라 입력기 조합 처리 문제에 가깝다.

## 왜 발생하는가

한글은 키를 누를 때마다 바로 최종 문자가 되는 것이 아니라, IME(Input Method Editor)가 자음과 모음을 조합해서 완성형 음절을 만든다. 일반 앱에서는 이 조합 과정이 앱에 잘 전달되지만, SSH 터미널 안에서 실행되는 TUI(Text User Interface) 프로그램은 키 입력을 낮은 수준에서 직접 읽는다.

이때 iPadOS + Termius + Claude Code 조합에서는 한글 IME의 조합 상태가 Claude Code의 interactive prompt에 완성형 문자로 전달되지 않고, 자모 또는 삭제/재삽입 시퀀스로 전달되는 것으로 보인다. 그 결과 Claude Code가 완성형 한글 대신 분해된 자모를 입력 버퍼에 남긴다.

## 중요한 구분

| 위치 | 한글 입력 가능성 | 판단 |
|---|---|---|
| iPad 일반 앱 | 정상 | iPad 한글 키보드 자체 문제 아님 |
| Termius 일반 shell/cmd | 환경에 따라 정상 가능 | SSH 연결 자체 문제 아님 |
| Claude Code interactive prompt | 자모 분리 발생 | Claude Code TUI 입력 처리 문제 가능성 높음 |
| 영어 입력 | 정상 | 네트워크/키보드 전체 문제 아님 |

## 관련 보고 사례

Anthropic Claude Code GitHub issue에도 iOS/iPadOS + Termius 환경에서 한글 입력이 사라지거나 자모로 분해되는 문제가 보고되어 있다.

- Korean input characters disappear on iOS mobile SSH: https://github.com/anthropics/claude-code/issues/15705
- iPadOS Korean character composition broken: https://github.com/anthropics/claude-code/issues/23226

위 보고들의 공통점은 다음과 같다.

| 공통점 | 의미 |
|---|---|
| iOS/iPadOS + Termius 환경 | 모바일 SSH 터미널 조합에서 재현 |
| Claude Code interactive mode에서 발생 | 일반 shell보다 TUI 입력 처리에 가까운 문제 |
| 영어 입력은 정상 | 전체 키보드 문제는 아님 |
| 한글/CJK 조합 입력에서 발생 | IME composition 처리 문제 |
| 복사/붙여넣기는 우회 가능 | 완성된 문자열을 한 번에 넣으면 비교적 안정적 |

## 현실적인 해결 방법

### 1. 영어로 프롬프트 입력

현재 가장 안정적인 방법이다. 사용자가 이미 확인했듯이 영어 입력은 정상 동작한다.

권장 상황:
- Claude Code에게 작업 지시
- 짧은 명령/승인/수정 요청
- M6 같은 학습 진행 프롬프트

### 2. 한글은 Notes/메모 앱에서 작성 후 붙여넣기

긴 한글 지시는 iPad 메모 앱, Drafts, Obsidian, Notion 같은 일반 텍스트 앱에서 작성한 뒤 복사해서 Claude Code prompt에 붙여넣는다.

장점:
- iPadOS 한글 IME가 일반 앱에서는 정상 조합
- 오탈자 확인 쉬움
- 긴 프롬프트 작성에 적합

주의:
- Termius가 붙여넣기 시 줄바꿈을 즉시 실행할 수 있으므로, 여러 줄 명령은 조심한다.
- shell 명령은 Markdown 링크로 자동 변환되지 않게 plain text로 붙여넣는다.

### 3. 한글 지시는 파일로 작성하고 Claude Code에게 읽게 하기

한글이 긴 경우, 터미널 prompt에 직접 입력하지 말고 파일로 저장한 뒤 Claude Code에게 읽게 하는 방식이 좋다.

예:

```cmd
notepad m6-request-ko.md
```

또는 SFTP/파일 앱으로 `m6-request-ko.md`를 넣고 Claude Code에서 다음처럼 요청한다.

```text
m6-request-ko.md 파일을 읽고 그 지시에 따라 진행해 주세요.
```

### 4. 영어 프롬프트 + 한국어 산출물 요청

입력은 영어로 하되 출력 언어를 명시한다.

예:

```text
Please continue M6 using the VibeLearn AI process. Read the roadmap and latest worklog first. Present the plan in Korean and wait for my approval before editing files.
```

이 방식은 iPad Termius에서 가장 안정적이다.

### 5. 다른 클라이언트 테스트

Termius 외의 SSH 앱이나 다른 환경에서는 한글 조합 동작이 달라질 수 있다. 다만 Claude Code의 TUI 입력 처리와 iPadOS IME 사이의 문제라면 완전히 해결되지 않을 수 있다.

테스트 후보:
- Blink Shell
- Web 기반 SSH client
- 노트북 직접 터미널
- Android + Termius

## 당장 권장 운영 방식

현재 iPad Termius에서 Claude Code를 쓸 때는 다음 원칙을 따른다.

| 상황 | 권장 방식 |
|---|---|
| 짧은 지시 | 영어로 입력 |
| 긴 한글 지시 | 메모 앱에서 작성 후 붙여넣기 |
| 매우 긴 학습 계획/요구사항 | Markdown 파일로 저장 후 Claude Code가 읽게 함 |
| shell 명령 | 영어/ASCII 명령으로 직접 입력 |
| 산출물 언어 | 프롬프트에 “write in Korean” 또는 “한국어로 작성” 명시 |

## 영상화 포인트

이 사례는 “모바일 원격 AI 코딩은 접속만 되면 끝이 아니다”라는 메시지를 보여주기에 좋다. iPad에서 Claude Code 화면까지 띄우는 데 성공했지만, 실제 입력 단계에서 한글 IME 문제가 드러났다.

### 장면 구성 후보

1. iPad Termius에서 Claude Code 실행 성공
2. 한글로 `프로세스` 입력 시 `ㅍㅡㄹㅗㅅㅔㅅㅡ`로 분해되는 장면
3. 영어 입력은 정상 동작하는 장면
4. 원인 설명: 한글 IME 조합과 TUI raw input 처리 문제
5. 우회 방법: 영어 지시, 메모 앱 작성 후 붙여넣기, 파일 기반 지시
6. 교훈: 모바일 원격 작업은 네트워크, 인증, 터미널 입력까지 모두 검증해야 한다

### 영상 메시지

```text
SSH 접속과 Claude Code 실행이 성공해도, 모바일 터미널의 입력기 문제는 별도로 검증해야 합니다.
한글처럼 IME 조합이 필요한 언어는 TUI 프로그램에서 자모 분리 문제가 생길 수 있습니다.
```

## M6 반영 메모

M6의 Remotion AI 영상화 후보에 이 사례를 포함한다. 특히 iPad에서 Claude Code를 실행한 실제 화면, 한글 자모 분리 화면, 영어 입력으로 우회한 화면은 교육적 가치가 높다.
