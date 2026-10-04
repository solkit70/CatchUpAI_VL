---
title: "M0 — 시작의 기록"
created: 2026-10-02 10:43:41
tags:
  - personal-ops-board
  - vibelearn-ai
---

## M0 — 시작의 기록

**상태**: 학습 산출물 정리 완료 · 사용자 검토 완료 (2026-10-02). **예상 학습 시간**: 2시간. 앱의 시작 배경과 현재 설계·변경 가능한 경계를 읽고, 기능과 아키텍처를 함께 키우는 개발 절차를 이해한다.

## 읽는 순서

1. [시작의 기록](../vl_materials/2026-09-27%20시작의%20기록.md#1-왜-만드나): 왜 만들고 무엇을 준비했는지
2. [AI Agent Application](concepts/ai-agent-application.md): 원본·캐시·제안·화면의 역할
3. [스펙 기반 개발의 접목](concepts/spec-driven-development.md): Kiro와 VibeLearn AI의 공통점과 변형
4. [멀티 에이전트 구조](concepts/multi-agent-structures.md): 파일 공유로 시작하고 연결 변경 가능성 유지
5. [현재 아키텍처](../architecture/ARCHITECTURE.md#3-에이전트-계약): 권한과 연결 계약

## 확인할 것

원본과 생성물을 구분하고, 새 기능을 구현하기 전에 요구·설계 승인을 거치는 이유를 설명해 본다. Go 보류는 현재 Python 선택이며 필요성이 생기면 새 ADR과 사용자 승인으로 재검토할 수 있다. → [ADR 005](../architecture/decisions/005-Go%20는%20보류.md#결정)

[Topic 안내](../README.md) · 다음: [M1 스키마·인덱서](../01-Schema-Indexer/README.md)
