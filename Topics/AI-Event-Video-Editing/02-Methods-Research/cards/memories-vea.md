---
title: "조사 카드 — Memories.ai VEA / Edit Video"
author:
  - "Codex"
created: 2026-10-24 22:52:50
source: "https://docs.memories.ai/visual-agents/video-editing-agent"
tags:
  - ai-event-video-editing
  - research-card
---

## 요약

**범주 B · 확인일 2026-10-24 · 자료로만 / 계정·유료 API 체험 안 함.** VEA 개요와 관리형 Edit Video API를 구분한다. 긴 영상을 이해해 하이라이트를 구성한다는 개요가 있지만, 정확한 3분 길이와 Premiere 전달까지 한 경로에서 검증된 것은 아니다.

> “it cannot be manually specified.”
> — [Edit Video API의 출력 길이 안내](https://docs.memories.ai/visual-agents/video-edit), 2026-10-24 확인

## 기능과 서로 다른 문서의 경계

[VEA 개요](https://docs.memories.ai/visual-agents/video-editing-agent)는 색인·프롬프트 기반 하이라이트 대본·클립 조립·음악·자막·MP4와 Final Cut Pro XML을 안내한다. 예시는 로컬 서비스 주소를 사용하므로 이 개요만으로 바로 쓸 수 있는 완성형 웹 편집기가 있다고 판단하지 않는다.

[Edit Video API](https://docs.memories.ai/visual-agents/video-edit)는 여러 업로드 자산과 가로·세로 출력, 500자 이내 지시를 받으며 영어를 권장한다. **출력 길이는 AI가 정하며 수동 지정할 수 없고**, 비동기 결과를 받으려면 webhook 설정이 필요하다. 응답 예시는 MP4 자산이며 개요의 XML 기능이 이 API에서도 동일하게 제공되는지는 미확인이다.

## 비용·한도·한국어

| 항목 | 확인 결과 |
|---|---|
| 편집 요금 | API 문서와 [요금표](https://memories.ai/pricing)에 $0.15/분 표시 |
| 총비용 | 색인·저장·전사·편집이 별도 항목. 어떤 길이에 편집 분당 요금이 적용되는지와 전체 합계는 미확인 |
| 무료 체험 | 편집 API의 무료량·카드 필요 여부 미확인 |
| 입력 한도 | 이 두 편집 문서에서 계정별 최대 영상 길이·파일 크기를 확정하지 못함 |
| 한국어 | 영어 권장. 다른 지시 언어는 보장하지 않는다고 명시; 한국어 전사·자막 품질은 미확인 |
| 데이터 | 자산 업로드와 비동기 처리를 사용하는 클라우드 API 경로 |

## 이 Topic에서의 판단

편집 목표는 가까우나 정확한 길이·XML 전달·개발 설정을 추가 확인해야 한다. 문서 기반으로는 개발자 보조가 필요한 비교 후보이며, 의뢰인에게 곧바로 따라 할 웹 매뉴얼을 제공할 수 있다고 확정하지 않는다.

후속 검증은 API와 VEA 전체 파이프라인의 관계, Premiere에서 XML이 열리는 형식, 3분 구성 방법, 총비용·파일 한도다. 가격 수치만으로 원본 몇 시간의 전체 비용을 계산하지 않는다.
