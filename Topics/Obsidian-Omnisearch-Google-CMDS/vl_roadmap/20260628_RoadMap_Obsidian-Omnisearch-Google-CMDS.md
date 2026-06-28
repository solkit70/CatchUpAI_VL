---
title: Obsidian Omnisearch Google CMDS RoadMap
created: 2026-06-28 06:59:46
methodology: VibeLearn AI
version: 2.0
tags:
  - vibelearn-ai
  - roadmap
  - obsidian
  - omnisearch
  - tampermonkey
---

# Obsidian-Omnisearch-Google-CMDS 학습 로드맵

## 학습 기간 적정성 분석

**사용자 입력 기간**: 1-2일, 총 3-5시간  
**Topic 복잡도**: 간단-중간. 독립 앱 개발이 아니라 Obsidian plugin, browser userscript, localhost HTTP 설정을 연결하는 설치형 실습이다.  
**권장 기간**: 1-2일이 적정하다. 다만 브라우저 권한, Obsidian plugin 활성화, localhost port 충돌이 생기면 추가 트러블슈팅 시간이 필요하다.

**분석 결과**: 입력한 기간으로 진행 가능하다. 오늘은 설치와 첫 Google 검색 성공을 목표로 하고, 멀티 vault 확장과 Local REST API 미리보기 튜닝은 다음 세션으로 분리하는 것이 적절하다.

## 학습 개요

### Topic 소개

`Obsidian-Omnisearch-Google-CMDS`는 Google 검색 페이지 오른쪽에 내 Obsidian vault 검색 결과를 함께 표시하는 Tampermonkey userscript를 학습하고 설치하는 실습 Topic이다. 핵심 구조는 browser userscript가 Google 검색어를 읽고, Obsidian Omnisearch HTTP server에 질의한 뒤, 선택적으로 Local REST API를 통해 노트 본문 미리보기와 안정적인 note open을 제공하는 방식이다.

### 학습 목표

- [ ] GitHub repo의 구조와 userscript 동작 원리를 설명할 수 있다.
- [ ] 현재 vault에 필요한 Obsidian 플러그인을 설치하고 활성화할 수 있다.
- [ ] Omnisearch HTTP server와 Local REST API 설정값을 확인하고 userscript 설정에 반영할 수 있다.
- [ ] Google 검색 화면에서 Obsidian 검색 결과가 표시되는지 검증할 수 있다.
- [ ] 설치 과정과 트러블슈팅 절차를 다음에도 재현 가능한 가이드로 정리할 수 있다.

### 학습 환경

- OS: Windows 11
- Vault: `C:\AI_study\2026\Changsoo_Vault`
- Browser: Chrome 또는 Edge
- Tools: Obsidian Desktop, Tampermonkey 또는 Violentmonkey, Omnisearch, Local REST API with MCP
- Source clone: `C:\tmp\obsidian-omnisearch-google-cmds`

## 전체 모듈 개요

| 모듈  | 제목                                  | 난이도 | 예상 시간  | 상태    | 산출물                                      |
| --- | ----------------------------------- | --- | ------ | ----- | ---------------------------------------- |
| M1  | Source Map & Architecture           | 낮음  | 45분    | 완료    | `vl_materials/source-map.md`             |
| M2  | Obsidian Plugin Setup               | 낮음  | 45분    | 부분 완료 | `.obsidian/plugins/` 설치 및 활성화            |
| M3  | Browser Userscript Setup            | 중간  | 60-90분 | 대기    | Tampermonkey userscript 설정               |
| M4  | First Search Test & Troubleshooting | 중간  | 60-90분 | 대기    | `01-Setup-and-Test/first-search-test.md` |

## 진행 상황 추적

| 항목 | 현재 상태 | 다음 확인 |
| --- | --- | --- |
| Topic 정보 | 완료 | `topic_info.md`, `topic_starter.md` 유지 |
| Template prompt | 완료 | `vl_prompts/roadmap_prompt.md`, `vl_prompts/daily_learning_prompt.md` |
| Obsidian plugin files | 완료 | Obsidian UI에서 활성화 필요 |
| Omnisearch HTTP server | 대기 | port 확인 필요 |
| Local REST API | 대기 | API key와 port 확인 필요 |
| Tampermonkey | 대기 | 브라우저 확장 설치 필요 |
| Google 검색 테스트 | 대기 | 오른쪽 sidebar 표시 확인 |

## M1 - Source Map & Architecture

### 1. 모듈 기본 정보

- 난이도: 낮음
- 예상 시간: 45분
- 산출물 폴더: `vl_materials/`
- 목표 상태: repo와 방송 슬라이드의 핵심 구조를 설명할 수 있다.

### 2. 학습 목표

- [x] GitHub repo 위치와 raw userscript URL을 확인한다.
- [x] 이 도구가 독립 앱이 아니라 userscript임을 이해한다.
- [x] Omnisearch HTTP server와 Local REST API의 역할을 구분한다.

### 3. 핵심 개념

이 도구의 중심은 “Google 검색어를 브라우저에서 읽어 Obsidian localhost endpoint로 보내는 것”이다. Omnisearch는 검색 결과를 제공하고, Local REST API는 실제 노트 본문 미리보기와 안정적인 열기를 보강한다.

### 4. 실습 과제

1. repo README를 읽고 설치 순서를 추출한다.
2. userscript header에서 `@match`, `@connect`, 기본 port 설정을 확인한다.
3. 방송 슬라이드의 요구사항과 repo README의 요구사항을 비교한다.

### 5. 예상 산출물

- `vl_materials/source-map.md`

### 6. Definition of Done

- [x] repo URL과 raw userscript URL이 기록됨
- [x] 설치 대상 vault가 기록됨
- [x] 의존 플러그인 두 개가 식별됨
- [x] 동작 흐름이 Mermaid diagram으로 정리됨

### 7. Self-Assessment

- [ ] “왜 Tampermonkey가 필요한가?”를 한 문장으로 설명할 수 있다.
- [ ] “Omnisearch와 Local REST API의 역할 차이”를 설명할 수 있다.

### 8. 시간 배분

- README 확인: 15분
- userscript 구조 확인: 15분
- source map 작성: 15분

### 9. 참조 자료

- `vl_materials/source-map.md`
- `C:\tmp\obsidian-omnisearch-google-cmds\README.md`
- `C:\tmp\obsidian-omnisearch-google-cmds\obsidian-omnisearch-google-cmds.user.js`

## M2 - Obsidian Plugin Setup

### 1. 모듈 기본 정보

- 난이도: 낮음
- 예상 시간: 45분
- 산출물 폴더: `.obsidian/plugins/`
- 목표 상태: 현재 vault에서 Omnisearch와 Local REST API를 활성화할 준비가 끝난다.

### 2. 학습 목표

- [x] 현재 vault의 community plugin 상태를 확인한다.
- [x] Omnisearch 최신 릴리스 파일을 설치한다.
- [x] Local REST API 최신 릴리스 파일을 설치한다.
- [ ] Obsidian UI에서 두 플러그인을 활성화한다.

### 3. 핵심 개념

Obsidian community plugin은 `.obsidian/plugins/{plugin-id}/` 아래의 `main.js`, `manifest.json`, `styles.css`로 설치된다. 파일이 있어도 Obsidian UI에서 community plugin을 활성화해야 실제로 로드된다.

### 4. 실습 과제

1. `.obsidian/community-plugins.json`에 `omnisearch`, `obsidian-local-rest-api`가 들어 있는지 확인한다.
2. Obsidian을 재시작하거나 command palette에서 reload app을 실행한다.
3. Settings → Community plugins에서 `Omnisearch`와 `Local REST API with MCP`를 활성화한다.
4. Omnisearch settings에서 HTTP server를 켜고 port를 기록한다.
5. Local REST API settings에서 non-encrypted HTTP server, port, API key를 확인한다.

### 5. 예상 산출물

- `.obsidian/plugins/omnisearch/`
- `.obsidian/plugins/obsidian-local-rest-api/`
- WorkLog에 port/API key 기록. API key는 전체 값을 공개 기록하지 말고 앞뒤 일부만 마스킹한다.

### 6. Definition of Done

- [x] Omnisearch `1.29.3` 파일 설치 완료
- [x] Local REST API with MCP `4.1.3` 파일 설치 완료
- [x] `community-plugins.json` 등록 완료
- [ ] Obsidian UI에서 Omnisearch 활성화
- [ ] Omnisearch HTTP server ON
- [ ] Local REST API 활성화와 port/API key 확인

### 7. Self-Assessment

- [ ] Obsidian plugin의 “파일 설치”와 “UI 활성화”의 차이를 설명할 수 있다.
- [ ] Omnisearch HTTP server port를 userscript 설정에 왜 넣어야 하는지 설명할 수 있다.

### 8. 시간 배분

- 설치 상태 확인: 10분
- Obsidian UI 활성화: 15분
- HTTP server 설정 확인: 20분

### 9. 참조 자료

- `.obsidian/community-plugins.json`
- `.obsidian/plugins/omnisearch/manifest.json`
- `.obsidian/plugins/obsidian-local-rest-api/manifest.json`

## M3 - Browser Userscript Setup

### 1. 모듈 기본 정보

- 난이도: 중간
- 예상 시간: 60-90분
- 산출물 폴더: `01-Setup-and-Test/`
- 목표 상태: Google 검색 페이지에서 userscript가 실행될 준비가 끝난다.

### 2. 학습 목표

- [ ] Tampermonkey 또는 Violentmonkey를 설치한다.
- [ ] raw userscript URL로 script를 설치한다.
- [ ] Chrome/Edge extension 권한을 설정한다.
- [ ] userscript vault slot에 Omnisearch port와 vault 정보를 입력한다.

### 3. 핵심 개념

브라우저 userscript는 Google 페이지 안에서 실행되므로 extension 권한이 필요하다. 또한 Obsidian은 localhost server로만 응답하기 때문에 Tampermonkey가 `localhost`와 `127.0.0.1` cross-origin 요청을 허용해야 한다.

### 4. 실습 과제

1. Tampermonkey를 설치한다.
2. raw userscript URL을 열어 script를 설치한다.
3. Chrome extension details에서 `Allow User Scripts`와 Google site access를 확인한다.
4. 첫 Google 검색 시 localhost 접근 prompt가 뜨면 Always allow domain을 선택한다.
5. userscript settings에서 vault slot을 현재 vault에 맞게 설정한다.

### 5. 예상 산출물

- `01-Setup-and-Test/browser-userscript-settings.md`

### 6. Definition of Done

- [ ] Tampermonkey 설치 확인
- [ ] userscript enabled 상태 확인
- [ ] Google 검색 페이지에서 script UI 또는 오류 메시지 확인
- [ ] vault slot 설정 저장
- [ ] localhost permission 승인

### 7. Self-Assessment

- [ ] 브라우저 extension 권한이 왜 필요한지 설명할 수 있다.
- [ ] `localhost` 접근 권한이 없을 때 어떤 증상이 생기는지 설명할 수 있다.

### 8. 시간 배분

- Tampermonkey 설치: 15분
- userscript 설치: 15분
- 권한 설정: 15분
- vault slot 설정: 15-45분

### 9. 참조 자료

- Raw userscript URL: `https://raw.githubusercontent.com/johnfkoo951/obsidian-omnisearch-google-cmds/main/obsidian-omnisearch-google-cmds.user.js`
- Repo README의 Chrome/Tampermonkey permissions 섹션

## M4 - First Search Test & Troubleshooting

### 1. 모듈 기본 정보

- 난이도: 중간
- 예상 시간: 60-90분
- 산출물 폴더: `01-Setup-and-Test/`
- 목표 상태: Google 검색 결과 오른쪽에 Obsidian 결과가 표시된다.

### 2. 학습 목표

- [ ] Google 검색어가 Obsidian Omnisearch 결과를 반환하는지 확인한다.
- [ ] 결과 card 클릭 시 Obsidian note가 열리는지 확인한다.
- [ ] Local REST API를 켠 경우 본문 preview와 tag 표시를 확인한다.
- [ ] 실패 시 port, permission, plugin 상태를 순서대로 점검한다.

### 3. 핵심 개념

첫 테스트는 기능 검증보다 연결 경로 검증이 중요하다. Google page → userscript → Omnisearch HTTP server → vault 검색 결과 → optional Local REST API 순서로 어디에서 끊기는지 확인해야 한다.

### 4. 실습 과제

1. `VibeLearn`, `GOBI`, `Peter Thiel`처럼 현재 vault에 존재할 가능성이 높은 검색어로 Google 검색을 실행한다.
2. 오른쪽 sidebar에 Obsidian 결과가 나타나는지 확인한다.
3. 결과가 없으면 Omnisearch plugin 내부 검색에서 같은 키워드를 먼저 테스트한다.
4. browser devtools console에서 localhost 연결 오류가 있는지 확인한다.
5. 성공/실패 결과를 기록한다.

### 5. 예상 산출물

- `01-Setup-and-Test/first-search-test.md`
- WorkLog 업데이트

### 6. Definition of Done

- [ ] Google 검색 sidebar 표시 확인
- [ ] 최소 1개 Obsidian note result 확인
- [ ] note open 동작 확인
- [ ] 실패 시 원인 후보와 다음 조치 기록
- [ ] 다음 세션 ToDo 정리

### 7. Self-Assessment

- [ ] 검색 결과가 안 뜰 때 점검 순서를 말할 수 있다.
- [ ] 멀티 vault 설정으로 확장할 때 추가로 필요한 값들을 말할 수 있다.

### 8. 시간 배분

- 첫 검색 테스트: 20분
- note open 테스트: 20분
- 실패 시 troubleshooting: 30-50분

### 9. 참조 자료

- `vl_materials/source-map.md`
- `vl_worklog/20260628_M1_Obsidian-Omnisearch-Google-CMDS.md`
- userscript settings 화면

## WorkLog 작성 가이드

WorkLog 파일명은 `vl_worklog/YYYYMMDD_MX_Obsidian-Omnisearch-Google-CMDS.md` 형식을 사용한다. 각 WorkLog에는 오늘 완료한 작업, 설치·설정 값, 발생한 문제, 해결 방법, Tomorrow's Focus를 기록한다. API key는 보안상 전체 값을 적지 말고 마스킹해서 기록한다.

## Retrospective 가이드

### Daily Retrospective

- 오늘 배운 것
- 성공한 연결 단계
- 막힌 지점과 원인 후보
- Tomorrow's Focus

### Module Retrospective

- 모듈 목표 달성 여부
- 실제 설치 환경에서 달라진 점
- 다음 모듈로 넘길 리스크

### Topic Retrospective

- Google 검색 + Obsidian 검색 통합의 실제 효용
- 멀티 vault 확장 여부
- 다른 사람에게 공유 가능한 설치 가이드 품질

## 성공 기준

- [ ] Google 검색 결과 오른쪽에 Obsidian Omnisearch 결과가 표시된다.
- [ ] 최소 1개 note를 클릭해 Obsidian에서 열 수 있다.
- [ ] Local REST API를 켠 경우 본문 미리보기와 tag가 표시된다.
- [ ] 설치·설정·검증 과정이 VibeLearn AI 산출물로 남아 있다.
