# 원격 세션 문제 해결 로그

## 현재 알려진 이슈

### Windows Optional Feature 설치 중복 큐

**증상**: OpenSSH Server가 설정 앱에서 세 개의 `Adding` 항목으로 중복 표시되고 10분 이상 멈춘 것처럼 보였다.

**원인**: OpenSSH Server 설치 요청이 중복으로 큐에 들어가 Windows Optional Feature 설치가 지연되었다.

**해결**: 중복된 두 항목을 취소하고 하나만 남기자 진행 바가 정상적으로 움직였고 설치가 완료되었다.

## M4 접속 중 확인할 문제

| 증상 | 우선 확인 |
|---|---|
| SSH timeout | iPhone Tailscale 연결 상태, 노트북 Tailscale 상태, 주소 `100.109.17.103` |
| Connection refused | `sshd` 서비스 실행 여부 |
| Password denied | Windows 계정 비밀번호 또는 Microsoft 계정 로그인 방식 |
| 접속은 되지만 `claude` 없음 | 원격 shell PATH와 npm global path |
| 접속 중 끊김 | 노트북 절전, iPhone 네트워크 전환, SSH 앱 세션 설정 |
### Termius username 오타로 인한 인증 실패

**증상**: SSH 연결과 handshake는 성공했지만 인증 단계에서 `No more authentication methods to try` 또는 password authentication failure가 발생했다.

**로그 단서**: Termius 로그에 `Authenticating ... as " catchupat"`가 표시되었다.

**원인**: username에 앞 공백이 들어가고 마지막 글자가 `catchupai`가 아니라 `catchupat`로 입력되어 있었다.

**해결**: Termius Host 설정에서 username을 정확히 `catchupai`로 수정했다. 수정 후 `catchupai@CHANGSOO C:\Users\catchupai>` 프롬프트까지 접속 성공했다.
### catchupai 계정의 Claude Code PATH 미반영

**증상**: Claude Code 설치 후 `C:\Users\catchupai\.local\bin\claude.exe --version`은 성공했지만, `claude --version`은 계속 `not recognized`로 실패했다.

**원인**: 설치 위치 `C:\Users\catchupai\.local\bin`이 현재 SSH 세션의 PATH에 반영되지 않았다.

**해결**: 사용자 환경변수 PATH에 `C:\Users\catchupai\.local\bin`을 추가하고 Termius 연결을 끊었다가 다시 접속했다. 이후 `claude --version`이 `2.1.241`로 정상 출력되었다.

