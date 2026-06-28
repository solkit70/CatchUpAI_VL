---
name: Obsidian-Omnisearch-Google-CMDS
description: Google 검색 화면에서 Obsidian Omnisearch 결과를 함께 표시하는 Tampermonkey userscript를 학습하고 현재 컴퓨터에 설치·검증
type: project
author:
  - "[[Changsoo]]"
created: 2026-06-28 06:59:46
tags:
  - vibe-learn-ai
  - obsidian
  - omnisearch
  - tampermonkey
  - userscript
---

# Obsidian-Omnisearch-Google-CMDS Topic 정보

## Overview

`Obsidian-Omnisearch-Google-CMDS`는 Google 검색 결과 페이지 오른쪽 사이드바에 내 Obsidian vault 검색 결과를 함께 표시하는 브라우저 userscript를 배우고 설치하는 실습형 Topic이다. 학습 대상은 `johnfkoo951/obsidian-omnisearch-google-cmds` repo이며, 핵심 구조는 Tampermonkey userscript, Obsidian Omnisearch HTTP server, 선택 사항인 Local REST API plugin의 연동이다.

## Goals

- [ ] GitHub repo의 구조와 userscript 동작 원리를 설명할 수 있다.
- [ ] 현재 vault에 필요한 Obsidian 플러그인을 설치하고 활성화할 수 있다.
- [ ] Omnisearch HTTP server와 Local REST API 설정값을 확인하고 userscript 설정에 반영할 수 있다.
- [ ] Google 검색 화면에서 Obsidian 검색 결과가 표시되는지 검증할 수 있다.
- [ ] 설치 과정과 트러블슈팅 절차를 다음에도 재현 가능한 가이드로 정리할 수 있다.

## Learning Purpose

- Google 검색과 개인 지식 vault 검색을 연결해 외부 검색과 내부 기록 검색을 한 화면에서 수행한다.
- 방송에서 소개한 도구를 실제 작업 환경에 설치하고, VibeLearn AI 방식으로 학습·설치·검증 기록을 남긴다.
- 이후 CMDS vault, Changsoo_Vault, 기타 vault를 멀티 vault 검색 대상으로 확장할 수 있는 기반을 만든다.

## Duration

예상 기간: 1-2일, 총 3-5시간

## Environment

- OS: Windows 11
- Vault: `C:\AI_study\2026\Changsoo_Vault`
- Browser: Chrome 또는 Edge
- Tools:
  - Obsidian Desktop
  - Tampermonkey 또는 Violentmonkey
  - Obsidian Omnisearch plugin
  - Local REST API with MCP plugin
  - GitHub repo clone: `C:\tmp\obsidian-omnisearch-google-cmds`

## Prerequisites

필수:
- Obsidian community plugin 설치와 활성화 경험
- Chrome/Edge extension 설치와 권한 승인 경험
- Windows 파일 경로와 localhost 개념

권장:
- Obsidian vault 구조 이해
- Tampermonkey userscript 기본 개념
- HTTP port와 API key 개념

## Reference Materials

- GitHub repo: `https://github.com/johnfkoo951/obsidian-omnisearch-google-cmds`
- Raw userscript: `https://raw.githubusercontent.com/johnfkoo951/obsidian-omnisearch-google-cmds/main/obsidian-omnisearch-google-cmds.user.js`
- Omnisearch plugin: `https://github.com/scambier/obsidian-omnisearch`
- Local REST API plugin: `https://github.com/coddingtonbear/obsidian-local-rest-api`
- 자료 맵: [source-map.md](vl_materials/source-map.md)

## Expected Outputs

- `vl_prompts/roadmap_prompt.md`
- `vl_prompts/daily_learning_prompt.md`
- `vl_roadmap/20260628_RoadMap_Obsidian-Omnisearch-Google-CMDS.md`
- `vl_worklog/20260628_M1_Obsidian-Omnisearch-Google-CMDS.md`
- `01-Setup-and-Test/` 아래 설치·테스트 가이드 또는 검증 기록
