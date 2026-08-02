# M2 — 파이프라인 아키텍처와 App Boundary 확정

**상태**: ✅ 완료
**예상 학습 시간**: 7h
**Topic**: [[../topic_starter|Live-CoMC-App]]

---

## 이 모듈에서 배우는 것

Wake Word부터 화면 오버레이/TTS 재생까지 이어지는 9단계 파이프라인을 데이터 흐름 관점에서 정리하고, MVP 첫 버전에 반드시 포함할 11개 항목과 제외할 11개 항목을 하드 게이트 문서로 확정한다. 동시에 Electron+Python 사이드카 구조를 Tauri·순수 Python과 비교해 채택 근거를 남긴다.

## 문서 목록 (학습 순서)

1. [concepts/pipeline-diagram.md](concepts/pipeline-diagram.md) — Wake→VAD→STT→Intent→Context→LLM→Verify→Overlay/TTS 9단계 Mermaid 다이어그램과 단계별 데이터 요약
2. [guides/app-boundary.md](guides/app-boundary.md) — 포함 11개 + 제외 11개 항목 표, 컴포넌트별 "절대 하지 말아야 할 일"
3. [guides/tech-choice.md](guides/tech-choice.md) — Electron vs Tauri vs 순수 Python 4기준 비교표, Electron 채택 근거

## 핵심 결론 (다음 모듈로 넘어가는 것)

- **하드 게이트 확정**: `app-boundary.md`가 이 문서에 없는 기능 요청을 v2로 미루는 기준이 된다 — M7·M9 범위 팽창 억제용으로 그대로 재사용
- **Electron + Python 사이드카** 채택 확정. 이유: OBS Browser Source와의 자연스러운 궁합, M1~M8 파일 기반 파이프라인을 재작성 없이 엔진으로 재사용 가능, 프로세스 분리로 안전장치(패닉 스톱)가 엔진 장애와 독립
- M1에서 확인한 "Rundown 단일 문서만 신뢰 소스로 삼는다" 원칙이 제외 범위 7번(다중 Rundown 조회)으로 공식 반영됨
- 안전 검증 게이트(⑦단계)는 규칙 기반이어야 하며 LLM 자기평가에 위임하지 않는다는 원칙이 컴포넌트별 금지 목록에 명시됨 — M3·M8 설계의 전제 조건

## 다음 모듈

→ M3 - 데이터 계약과 안전 정책 스펙 (`03-Data-Contracts-and-Safety/`)
