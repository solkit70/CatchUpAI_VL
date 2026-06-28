---
title: M2-M3 WorkLog - Obsidian Plugin and Browser Setup
created: 2026-06-28 07:00:00
module: M2-M3 - Obsidian Plugin Setup and Browser Userscript Setup
tags:
  - worklog
  - obsidian
  - omnisearch
  - tampermonkey
  - vibelearn-ai
---

## 세션 정보

| 항목 | 내용 |
| --- | --- |
| 날짜 | 2026-06-28 |
| 방법론 | VibeLearn AI |
| Roadmap | `vl_roadmap/20260628_RoadMap_Obsidian-Omnisearch-Google-CMDS.md` |
| 목표 | M2 plugin 활성화 준비, M3 browser userscript 설치 준비, M4 첫 테스트 기록지 생성 |

## 현재 학습 상태

| 모듈 | 상태 | 비고 |
| --- | --- | --- |
| M1 Source Map & Architecture | 완료 | `vl_materials/source-map.md` |
| M2 Obsidian Plugin Setup | 부분 완료 | 파일 설치 완료, UI 활성화 대기 |
| M3 Browser Userscript Setup | 부분 진행 | Tampermonkey/raw script URL 열림, 사용자 설치 승인 필요 |
| M4 First Search Test | 대기 | Omnisearch HTTP server 응답 전까지 보류 |

## 오늘 완료한 일

- [x] VibeLearn AI skill과 `Ingest/CatchUpAI_VL` 지침을 다시 로드했다.
- [x] `daily_learning_prompt.md`, Roadmap, 최신 WorkLog를 읽고 현재 상태를 분석했다.
- [x] Obsidian plugin 파일 설치 상태를 재확인했다.
- [x] `.obsidian/community-plugins.json`에 `omnisearch`, `obsidian-local-rest-api`가 등록되어 있음을 확인했다.
- [x] Tampermonkey 사이트를 브라우저로 열었다.
- [x] raw userscript URL을 브라우저로 열었다.
- [x] `01-Setup-and-Test/browser-userscript-settings.md`를 작성했다.
- [x] `01-Setup-and-Test/first-search-test.md`를 작성했다.
- [x] `http://localhost:51361/search?q=VibeLearn` 자동 점검을 실행했다.

## 자동 점검 결과

| 항목 | 결과 |
| --- | --- |
| Obsidian process | 실행 중 |
| Omnisearch files | 설치 완료 |
| Local REST API files | 설치 완료 |
| Tampermonkey default profile | 미확인 |
| Omnisearch data.json | 없음 |
| Local REST API data.json | 없음 |
| `localhost:51361/search` | timeout |

## 해석

Obsidian plugin 파일은 설치되었지만, Obsidian이 새 plugin을 로드하거나 HTTP server를 켠 상태는 아직 확인되지 않았다. `data.json`이 없는 것으로 보아 plugin settings가 아직 생성되지 않았거나, Obsidian UI에서 plugin을 활성화하지 않은 상태일 가능성이 높다. 따라서 다음 단계는 코드/파일 편집이 아니라 Obsidian UI에서 plugin 활성화와 HTTP server 설정을 완료하는 것이다.

## 사용자 UI 작업 필요

- [ ] Obsidian에서 현재 vault를 reload하거나 앱을 재시작한다.
- [ ] Settings → Community plugins에서 `Omnisearch`를 활성화한다.
- [ ] Settings → Omnisearch에서 `HTTP server`를 ON으로 설정한다.
- [ ] Omnisearch port가 `51361`인지 확인한다.
- [ ] Settings → Community plugins에서 `Local REST API with MCP`를 활성화한다.
- [ ] Local REST API의 non-encrypted HTTP server를 켜고 port/API key를 확인한다.
- [ ] Tampermonkey를 설치한다.
- [ ] raw userscript URL에서 userscript를 설치한다.
- [ ] userscript settings에 `browser-userscript-settings.md`의 값을 입력한다.

## Tomorrow's Focus

- 사용자가 Obsidian/Tampermonkey UI 설정을 완료한 뒤 `localhost:51361/search?q=VibeLearn`을 다시 테스트한다.
- Google에서 `VibeLearn`, `GOBI`, `Peter Thiel` 검색을 실행하고 오른쪽 sidebar 표시 여부를 `first-search-test.md`에 기록한다.
