---
title: First Search Test - Obsidian Omnisearch Google CMDS
created: 2026-06-28 07:00:00
tags:
  - obsidian
  - omnisearch
  - google-search
  - test
---

## 테스트 목적

Google 검색 화면에서 Obsidian Omnisearch Google CMDS userscript가 오른쪽 sidebar를 표시하고, 현재 vault의 검색 결과를 반환하는지 검증한다.

## 사전 조건

- [ ] Obsidian에서 `Omnisearch` plugin 활성화
- [ ] Omnisearch HTTP server ON
- [ ] Obsidian에서 `Local REST API with MCP` plugin 활성화
- [ ] Tampermonkey 설치
- [ ] userscript 설치 및 enabled
- [ ] userscript Vault 1 설정 입력
- [ ] 첫 localhost permission prompt 승인

## 설정값

| 항목 | 값 |
| --- | --- |
| Vault | `Changsoo_Vault` |
| Vault root | `C:\AI_study\2026\Changsoo_Vault` |
| Omnisearch port | `51361` 또는 실제 확인값 |
| Local REST API port | 미확인 |
| Local REST API key | 기록하지 않음 |

## 테스트 케이스

| # | Google 검색어 | 기대 결과 | 실제 결과 |
| --- | --- | --- | --- |
| 1 | `VibeLearn` | VibeLearn 관련 note 표시 | 미진행 |
| 2 | `GOBI` | GOBI 관련 note 표시 | 미진행 |
| 3 | `Peter Thiel` | Peter-Thiel-Vision 관련 note 표시 | 미진행 |

## 문제 발생 시 점검 순서

1. Obsidian에서 Omnisearch 자체 검색이 되는지 확인한다.
2. Omnisearch HTTP server port가 userscript `v1_port`와 같은지 확인한다.
3. Google page에서 Tampermonkey script가 enabled인지 확인한다.
4. Browser console에서 `localhost` 또는 `127.0.0.1` connection error가 있는지 확인한다.
5. Tampermonkey cross-origin prompt에서 localhost를 허용했는지 확인한다.
6. Local REST API preview만 안 되면 `v1_lrPort`, `v1_lrKey`, non-encrypted HTTP server 상태를 확인한다.

## 테스트 결과

2026-06-28 1차 자동 점검:

- `http://localhost:51361/search?q=VibeLearn` 요청은 timeout.
- `netstat`에서 `51361`에 대한 접속 시도는 보였으나 정상 LISTEN/응답은 확인되지 않음.
- `.obsidian/plugins/omnisearch/data.json`과 `.obsidian/plugins/obsidian-local-rest-api/data.json`은 아직 생성되지 않음.

해석: plugin 파일은 설치되어 있지만 Obsidian이 새 plugin을 로드하지 않았거나, Omnisearch HTTP server가 아직 켜지지 않은 상태로 보인다. Obsidian UI에서 plugin 활성화와 HTTP server 설정을 먼저 완료해야 Google 검색 테스트를 진행할 수 있다.
