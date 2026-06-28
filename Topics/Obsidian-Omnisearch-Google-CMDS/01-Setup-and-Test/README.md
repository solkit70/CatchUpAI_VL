---
title: Setup and Test - Obsidian Omnisearch Google CMDS
created: 2026-06-28 07:50:58
tags:
  - vibelearn-ai
  - obsidian
  - omnisearch
  - setup
  - test
---

## 목적

이 폴더는 VibeLearn AI 로드맵의 M3 Browser Userscript Setup과 M4 First Search Test 산출물을 모아 둔 작업 공간이다. `Obsidian Omnisearch Google CMDS`를 현재 vault에서 실제로 사용할 수 있도록 브라우저 userscript 설정값을 정리하고, Google 검색 화면에서 Obsidian 검색 결과가 표시되는지 검증한다.

## 문서 목록

| 문서 | 용도 | 상태 |
| --- | --- | --- |
| `browser-userscript-settings.md` | Obsidian, Tampermonkey, userscript 설정값 정리 | 작성 완료 |
| `first-search-test.md` | 첫 Google 검색 테스트 케이스와 결과 기록 | UI 설정 대기 |

## 진행 순서

1. `browser-userscript-settings.md`를 열어 Obsidian plugin 활성화와 userscript 설정값을 확인한다.
2. Obsidian UI에서 `Omnisearch`와 `Local REST API with MCP`를 활성화한다.
3. Omnisearch 설정에서 HTTP server를 켜고 port를 확인한다.
4. Tampermonkey에 raw userscript를 설치하고 Vault 1 설정값을 입력한다.
5. Google에서 `VibeLearn`, `GOBI`, `Peter Thiel` 검색을 실행한다.
6. 결과를 `first-search-test.md`에 기록한다.

## 현재 상태

plugin 파일 설치와 `.obsidian/community-plugins.json` 등록은 완료되어 있다. 다음 단계는 Obsidian과 브라우저 UI에서 사용자가 직접 권한을 승인하고 plugin/userscript를 활성화하는 것이다. 이 UI 작업이 끝난 뒤 `first-search-test.md`의 테스트 케이스를 진행한다.
