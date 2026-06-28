---
title: Obsidian-Omnisearch-Google-CMDS
created: 2026-06-28 06:59:46
methodology: VibeLearn AI
tags:
  - vibelearn-ai
  - obsidian
  - omnisearch
  - userscript
---

# Obsidian-Omnisearch-Google-CMDS

**핵심 질문**: Google 검색을 할 때 내 Obsidian vault 검색 결과를 함께 볼 수 있게 만들 수 있는가?

이 Topic은 `johnfkoo951/obsidian-omnisearch-google-cmds` userscript를 학습하고, 현재 컴퓨터의 Obsidian vault에서 실제로 동작하도록 설치·검증하는 VibeLearn AI 실습이다. 공식 VibeLearn AI 프로세스에 맞춰 `topic_info.md`, `topic_starter.md`, `vl_prompts/roadmap_prompt.md`, `vl_prompts/daily_learning_prompt.md`, Roadmap, WorkLog를 연결한다.

## 시작하기

1. [topic_info.md](topic_info.md) - Topic 기본 정보와 학습 목표
2. [topic_starter.md](topic_starter.md) - VibeLearn AI Topic Starter 입력값
3. [vl_prompts/roadmap_prompt.md](vl_prompts/roadmap_prompt.md) - template 기반 Roadmap 생성 prompt
4. [vl_roadmap/20260628_RoadMap_Obsidian-Omnisearch-Google-CMDS.md](vl_roadmap/20260628_RoadMap_Obsidian-Omnisearch-Google-CMDS.md) - 정식 학습 로드맵
5. [vl_prompts/daily_learning_prompt.md](vl_prompts/daily_learning_prompt.md) - 오늘 학습 시작용 prompt
6. [vl_worklog/20260628_M1_Obsidian-Omnisearch-Google-CMDS.md](vl_worklog/20260628_M1_Obsidian-Omnisearch-Google-CMDS.md) - 오늘 진행 기록
7. [vl_materials/source-map.md](vl_materials/source-map.md) - repo, 방송 슬라이드, 설치 자료 맵

## 진행 현황

| 단계 | 내용 | 상태 |
| --- | --- | --- |
| Phase 1 | Topic 입력 정보 생성 | 완료 |
| Phase 2 | template 기반 prompt와 Roadmap 생성 | 완료 |
| M1 | Source map과 architecture 이해 | 완료 |
| M2 | Obsidian plugin 파일 설치 | 부분 완료 |
| M3 | Obsidian plugin 활성화와 HTTP server 설정 | 대기 |
| M4 | Tampermonkey userscript 설치와 Google 검색 테스트 | 대기 |

## 다음 세션 ToDo

- [ ] Obsidian을 재시작하거나 현재 vault를 다시 로드한다.
- [ ] Community plugins에서 `Omnisearch`와 `Local REST API with MCP`를 활성화한다.
- [ ] Omnisearch 설정에서 HTTP server를 켜고 port를 확인한다.
- [ ] Local REST API 설정에서 non-encrypted HTTP server와 API key를 확인한다.
- [ ] Tampermonkey에 `obsidian-omnisearch-google-cmds.user.js`를 설치한다.
- [ ] userscript 설정에서 vault port, vault name, filesystem root를 현재 vault에 맞게 입력한다.
- [ ] Google 검색 결과 오른쪽 sidebar에 Obsidian 결과가 표시되는지 확인한다.
