---
title: "공유 링크가 옛 버전을 보여준다 (9/7) — 재해석"
created: 2026-09-13 08:09:00
tags:
  - claude-artifacts-routines
  - m2
  - troubleshooting
---

## 증상 (9/7, Builders Lounge 입장 안내)

소유자 브라우저에선 최신인데 다른 사람에게 보낸 링크는 이전 버전이 보였다. 당시 "pin 동작"이라 적었다 `[9/7 추정]`.

## 문서가 말하는 것

> *"Each publish becomes a version, and from the Share control in the page header you can choose which version viewers see."* `[문서]`

문서 스크린샷의 Share 메뉴에는 **"Always share latest version" 토글 + "Sharing version 2" 버전 선택**이 있다. 즉 공유되는 버전은 **고정될 수 있고**, 소유자는 항상 최신을 본다.

## 재해석

pin 은 사이드바에 꽂는 기능이라 무관 `[도구 설명]`. 9/7 증상은 **공유 버전이 이전 버전에 고정**돼 있었거나(토글 off), 그날 시크릿 창으로 확인해 v3 로 맞춘 것이 곧 그 조치였다 `[실측 9/7]`.

⬜ 오늘(9/13) 이 계정의 Share 메뉴 스크린샷에는 그 토글이 **안 보였다** — 공개로 바꾸기 전 상태였기 때문인지, 플랜 차이인지 미확인. 공개 후 메뉴를 다시 열어 확인한다.

## 확인 순서

1. Share 메뉴에서 공유 중인 버전 번호 확인
2. "Always share latest version" 이 있으면 켠다
3. 시크릿 창으로 검증 — 소유자 브라우저는 증거가 아니다
