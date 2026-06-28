# VibeLearn AI Topic Starter - Obsidian-Omnisearch-Google-CMDS

## Topic 기본 정보

Topic 이름: `Obsidian-Omnisearch-Google-CMDS`

설명: Google 검색 화면에서 Obsidian Omnisearch 결과를 함께 표시하는 Tampermonkey userscript를 학습하고 현재 컴퓨터에 설치·검증한다.

학습 목적:
- Google 검색과 Obsidian vault 검색을 한 화면에서 연결한다.
- 방송에서 소개된 userscript를 실제 컴퓨터에 설치하고 사용 가능 상태로 만든다.
- 설치 과정, 설정값, 트러블슈팅을 VibeLearn AI 형식으로 기록해 다음에도 재현 가능하게 만든다.

예상 기간: 1-2일, 총 3-5시간

## 학습 목표

- [ ] GitHub repo의 구조와 userscript 동작 원리를 설명할 수 있다.
- [ ] 현재 vault에 필요한 Obsidian 플러그인을 설치하고 활성화할 수 있다.
- [ ] Omnisearch HTTP server와 Local REST API 설정값을 확인하고 userscript 설정에 반영할 수 있다.
- [ ] Google 검색 화면에서 Obsidian 검색 결과가 표시되는지 검증할 수 있다.
- [ ] 설치 과정과 트러블슈팅 절차를 다음에도 재현 가능한 가이드로 정리할 수 있다.

## 학습 환경

OS: Windows 11

주요 도구 및 기술 스택:
- Obsidian Desktop
- Chrome 또는 Edge
- Tampermonkey 또는 Violentmonkey
- Obsidian Omnisearch plugin
- Local REST API with MCP plugin
- GitHub repo clone: `C:\tmp\obsidian-omnisearch-google-cmds`

사전 지식:

필수:
- Obsidian community plugin 설치와 활성화 경험
- Chrome/Edge extension 설치와 권한 승인 경험
- Windows 파일 경로와 localhost 개념

권장:
- Obsidian vault 구조 이해
- Tampermonkey userscript 기본 개념
- HTTP port와 API key 개념

## 참조 자료

공식 문서:
- GitHub repo: `https://github.com/johnfkoo951/obsidian-omnisearch-google-cmds`
- Raw userscript: `https://raw.githubusercontent.com/johnfkoo951/obsidian-omnisearch-google-cmds/main/obsidian-omnisearch-google-cmds.user.js`

관련 GitHub 저장소:
- Omnisearch plugin: `https://github.com/scambier/obsidian-omnisearch`
- Local REST API plugin: `https://github.com/coddingtonbear/obsidian-local-rest-api`

vl_materials/ 폴더에 추가할 자료:
- repo README와 userscript 구조 요약
- 방송 슬라이드에서 확인한 설치 순서와 기능 요약
- 현재 컴퓨터 설치 경로와 설정값

## 학습 접근 방식

- [x] 실습 중심, 필요한 이론만
- [ ] 이론 먼저, 실습 나중
- [ ] 이론과 실습 병행

시간 투자 계획:
- 총 학습 시간: 3-5시간
- 1회당 학습 시간: 1-2시간
- 우선순위: 설치 성공과 Google 검색 테스트

특별히 집중하고 싶은 영역:
- 현재 vault에서 실제 동작 확인
- 브라우저 권한과 localhost 연결 문제 해결
- 멀티 vault 확장 가능성 확인
