# Spec 분석: 07 - Capture

**분석일**: 2026-04-07
**원본 파일**: `gobi-monorepo/specs/07-capture.md`
**Vibe Guiding 관련도**: ⭐⭐⭐ 핵심

---

## 핵심 요약

Capture는 Brain에 새 정보가 들어오는 주요 관문. 음성 녹음, 노트, 앰비언트 브레인스토밍, 센서 데이터를 저마찰(low-friction)로 수집하고, 에이전트가 자동으로 처리·구조화.

---

## 주요 기능 정리

| 기능 | 제품 | 설명 |
|------|------|------|
| Audio Capture | Desktop | 녹음 → MD 파일로 저장 (YAML 메타데이터 + 전사 텍스트) |
| Ambient Canvas Brainstorming (ACB) | Desktop | 연속 음성 → 실시간 전사 + AI 구조화 캔버스 생성 |
| Quick Capture | Mobile | 음성/텍스트 빠른 입력 → 에이전트 자동 처리 |
| Share-to-Capture | Mobile | 다른 앱 콘텐츠 → Gobi로 공유 → Brain 통합 |
| Canvas Sync | Desktop | 생성된 캔버스 ↔ Vault 동기화 |

---

## Ambient Canvas Brainstorming (ACB) 상세

```
사용자 자유 발화
    ↓ 실시간 전사
    ↓ AI 구조화 캔버스 주기적 생성
    ↓ 타임스탬프 정리
    ↓ 자동 제목 생성
→ Vault/_Gobi_/Captures/YYYY-MM-DD-HH-MM-SS-{title}.md 저장
```

---

## Vibe Guiding 접점 분석

### 🎯 접점 1: ACB 세션 중 실시간 Vibe Guiding
**시나리오**: 사용자가 ACB로 브레인스토밍 중 Vibe Guiding이 관련 컨텍스트를 실시간 제공

```
사용자가 "PKM에 대해 생각해보자..." 발화
        ↓ 실시간 전사
        ↓ Vibe Guiding 감지: "PKM 관련 Brain 내용 있음"
        ↓ 사이드패널 또는 TTS로 안내:
"관련 자료: Brain의 '2026-03-15 PKM 노트'가 있습니다."
```

**실현 가능성**: ⭐⭐ 중간 — 전사 스트림 후킹 + Vibe Guiding 레이어 추가 필요

### 🎯 접점 2: 캡처 완료 후 Vibe Guiding 트리거
캡처 파일이 생성(`_Gobi_/Captures/`에 저장)되는 순간 Orchestrator Reflex 트리거:
```
새 캡처 파일 감지 (파일 변경 Reflex)
        ↓
Vibe Guiding Agent: 캡처 내용 분석
        ↓
관련 기존 지식 + 다음 행동 제안 제공
```

**실현 가능성**: ✅ 높음 — Orchestrator의 파일 변경 트리거 기능 활용

### 🎯 접점 3: Quick Capture 후 Vibe Guiding 안내 (Mobile)
모바일에서 Quick Capture 후:
- "이 내용이 Brain의 ○○ 주제와 관련 있습니다"
- "비슷한 캡처 3개가 있습니다. 통합할까요?"

**실현 가능성**: ⭐⭐ 중간 — 모바일 Vibe Guiding 별도 구현 필요

---

## Vibe Guiding 설계 함의

> **Capture = Vibe Guiding의 가장 자연스러운 트리거 포인트**

사용자가 새 정보를 입력하는 순간이 Vibe Guiding이 개입하기 가장 적합한 타이밍:
1. 캡처 **전**: "이 주제에 대해 이미 알고 있는 것" 컨텍스트 제공
2. 캡처 **중**: 관련 지식 실시간 표시 (ACB)
3. 캡처 **후**: 통합/연결 제안 (Reflex)

파일 저장 경로(`_Gobi_/Captures/`)가 명확하므로 Orchestrator Reflex로 Watch Pattern 설정 용이.
