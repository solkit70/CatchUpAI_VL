---
title: "Scenario - GOBI Desktop Custom Homepage Applet"
created: 2026-05-10 07:22:45
tags:
  - vibe-guiding
  - gobi-desktop
  - applet
  - scenario-test
sources:
  - "[[Ingest/CatchUpAI_VL/Topics/GOBI-Guiding/2026-04-13 Gobi Desktop Vibe Guiding 기능 수준 테스트#2. 테스트 결과 및 분석|GOBI Desktop Vibe Guiding 기능 수준 테스트]]"
---

## 시나리오 목적

이 시나리오는 GOBI Desktop에서 Custom Homepage/Applet을 만들려는 사용자가 실제 앱 상태를 확인하지 못해 막히는 상황을 검증한다. 핵심은 Applet 생성 절차를 바로 안내하는 것이 아니라, Desktop 버전, Vault Path, Applet 경로, 사용자가 실제로 보는 Settings 메뉴를 먼저 확인하도록 guide가 제동을 거는지 확인하는 것이다.

> **컨텍스트 단절**: 사용자의 현재 설정 상태(Vault Path, Applet 경로 등)를 실시간으로 정확히 파악하여 가이드에 반영하는 능력이 아직 부족함.

이 인용문은 M5에서 Desktop/Applet 시나리오를 추가한 직접 근거다. 사용자가 앱 화면을 보고 있는 상황에서 Vibe Guiding이 존재하지 않는 메뉴를 단정하면 guide 자체가 blocker가 된다.

## 입력 context

| 항목 | 값 |
|---|---|
| OS | Windows 11 |
| 앱 | GOBI Desktop |
| Desktop 버전 | `unknown` |
| Vault Path | `unknown` |
| Applet 경로 | `unknown` |
| 현재 보이는 Settings 메뉴 | `unknown` |
| problem signal | `desktop_custom_homepage_blocked` |

## 기대 guide

`desktop_applet_context_missing` rule과 `gobi-desktop-applet-context-check` manual이 선택되어야 한다. guide는 확인되지 않은 UI 메뉴나 버튼 위치를 단정하지 않아야 하며, 사용자가 실제로 보는 화면과 경로를 먼저 확인하도록 안내해야 한다.

## 검증 결과

| 입력 | 선택 rule | 선택 manual | 평가 |
|---|---|---|---|
| `desktop_custom_homepage_blocked` | `desktop_applet_context_missing` | `gobi-desktop-applet-context-check` | 통과 |

생성된 guide는 Desktop 버전, Vault Path, Applet 경로, Settings 메뉴 확인을 첫 단계로 제시했다. 또한 확인되지 않은 메뉴 이름이나 버튼 위치를 단정하지 말라고 fallback에 명시했으므로 Desktop/Applet 품질 기준을 충족한다.

## 실패 시 수정 위치

앱 상태가 context에 없으면 context collector를 보강해야 한다. 상태가 있는데도 CLI manual이 선택되면 trigger 또는 retrieval index가 문제다. 올바른 manual을 골랐는데도 존재하지 않는 메뉴명을 안내하면 compose 단계의 guardrail을 강화해야 한다.
