---
title: M1 WorkLog - Obsidian Omnisearch Google CMDS
created: 2026-06-28 06:59:46
module: M1 - Source Map & Setup Preparation
tags:
  - worklog
  - obsidian
  - omnisearch
  - userscript
  - vibelearn-ai
---

## 세션 정보

| 항목 | 내용 |
| --- | --- |
| 날짜 | 2026-06-28 |
| 방법론 | VibeLearn AI |
| 목표 | 방송에서 소개된 Obsidian Omnisearch Google CMDS를 학습하고 현재 컴퓨터에 설치 준비 |
| 대상 vault | `C:\AI_study\2026\Changsoo_Vault` |
| 참조 repo | `johnfkoo951/obsidian-omnisearch-google-cmds` |

## 프로세스 교정 기록

처음 생성한 로드맵과 기록은 설치 체크리스트 중심으로 작성되어 VibeLearn AI 공식 프로세스를 충분히 따르지 않았다. 이후 `_Settings_/Skills/vibelearn-ai/SKILL.md`, `Ingest/CatchUpAI_VL/templates/workflow_guide.md`, `topic_starter.md`, `roadmap_prompt_template.md`, `daily_learning_prompt.md`를 확인하고, 정식 순서에 맞게 Topic 입력 문서와 prompt 파일을 보강했다.

정식 교정으로 추가·수정한 파일은 다음과 같다.

- [x] `topic_info.md` 생성
- [x] `topic_starter.md` 생성
- [x] `vl_prompts/roadmap_prompt.md` 생성
- [x] `vl_prompts/daily_learning_prompt.md` 생성
- [x] `vl_roadmap/20260628_RoadMap_Obsidian-Omnisearch-Google-CMDS.md`를 모듈별 9개 필수 항목 구조로 재작성

## 오늘 완료한 일

- [x] GitHub repo를 `C:\tmp\obsidian-omnisearch-google-cmds`에 clone했다.
- [x] README와 userscript 구조를 확인했다.
- [x] 현재 vault의 `.obsidian/community-plugins.json` 상태를 확인했다.
- [x] Omnisearch `1.29.3`을 `.obsidian/plugins/omnisearch`에 설치했다.
- [x] Local REST API with MCP `4.1.3`을 `.obsidian/plugins/obsidian-local-rest-api`에 설치했다.
- [x] `.obsidian/community-plugins.json`에 `omnisearch`, `obsidian-local-rest-api`를 추가했다.
- [x] VibeLearn AI 공식 template prompt 구조를 적용했다.

## 핵심 이해

이 앱은 독립 실행 앱이 아니라 브라우저 userscript다. Google 검색 페이지에 삽입된 Tampermonkey script가 Obsidian의 Omnisearch HTTP server로 검색 요청을 보내고, 결과를 Google 오른쪽 sidebar에 표시한다. Local REST API는 선택 사항이지만, 실제 note 본문 preview와 안정적인 note open에는 필요하다.

> A Tampermonkey/Violentmonkey userscript that injects your Obsidian Omnisearch results into the Google search sidebar

## 설치 상태

| 구성요소 | 상태 | 비고 |
| --- | --- | --- |
| Omnisearch | 파일 설치 완료 | Obsidian UI에서 활성화 필요 |
| Local REST API with MCP | 파일 설치 완료 | Obsidian UI에서 활성화 필요 |
| Tampermonkey | 미확인 | 브라우저에서 설치/활성화 필요 |
| Userscript | 설치 대기 | raw script URL로 설치 필요 |
| Google 검색 테스트 | 대기 | HTTP server 설정 후 진행 |

## 다음 세션 ToDo

- [ ] Obsidian을 재시작하거나 현재 vault를 다시 로드한다.
- [ ] Community plugins에서 `Omnisearch`를 활성화한다.
- [ ] Community plugins에서 `Local REST API with MCP`를 활성화한다.
- [ ] Omnisearch 설정에서 HTTP server를 켠다.
- [ ] Omnisearch HTTP port를 확인해서 이 WorkLog에 기록한다.
- [ ] Local REST API의 non-encrypted HTTP server를 켜고 port/API key를 기록한다. API key는 전체 값을 기록하지 말고 마스킹한다.
- [ ] Tampermonkey에서 userscript를 설치한다.
- [ ] Userscript 설정에서 vault name, Omnisearch port, filesystem root, Local REST API 정보를 입력한다.
- [ ] Google에서 `Peter Thiel`, `GOBI`, `VibeLearn` 같은 vault 내부 단어를 검색해 표시 여부를 확인한다.

## 남은 리스크

- 브라우저 확장 권한은 로컬 파일로 강제 설정할 수 없으므로 Chrome/Tampermonkey UI에서 사용자가 직접 승인해야 한다.
- Omnisearch HTTP server의 실제 port는 Obsidian plugin 설정 화면에서 확인해야 한다.
- `C:\AI_study\2026\cmds-vault`에도 같은 설치가 필요하면 별도 vault에 대한 설치 작업이 추가로 필요하다.

## Daily Retrospective

### 오늘 배운 것

- VibeLearn AI Topic은 단순 폴더와 로드맵만 있으면 충분하지 않고, `topic_info.md`, `topic_starter.md`, `vl_prompts/roadmap_prompt.md`, `vl_prompts/daily_learning_prompt.md`가 template 기반으로 연결되어야 한다.
- Obsidian Omnisearch Google CMDS는 Obsidian plugin 자체가 아니라 Google page에서 실행되는 userscript이며, Obsidian은 localhost 검색 service 역할을 한다.

### 잘한 점

- Obsidian plugin 파일 설치와 community plugin 등록은 완료했다.
- 프로세스 오류를 확인한 뒤 공식 skill과 template을 기준으로 산출물을 교정했다.

### 개선할 점

- VibeLearn AI 요청이 들어오면 설치나 분석을 먼저 진행하기 전에 반드시 `_Settings_/Skills/vibelearn-ai/SKILL.md`와 `Ingest/CatchUpAI_VL/templates/`를 먼저 확인해야 한다.

### Tomorrow's Focus

- Obsidian UI에서 plugin 활성화와 HTTP server 설정을 완료한다.
- Tampermonkey 설치 후 userscript를 설치한다.
- Google 검색에서 오른쪽 sidebar 표시 여부를 확인하고 `01-Setup-and-Test/first-search-test.md`에 결과를 기록한다.
