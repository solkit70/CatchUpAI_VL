# Spec 분석: 06 - Voice Interaction

**분석일**: 2026-04-07
**원본 파일**: `gobi-monorepo/specs/06-voice-interaction.md`
**Vibe Guiding 관련도**: ⭐⭐⭐ 핵심

---

## 핵심 요약

음성이 GOBI의 1등급 입력 수단. STT/TTS/VAD/Wake Word/Ambient Mode를 포함한 완전한 음성 스택. 특히 **Ambient Mode**는 Vibe Guiding의 가장 자연스러운 채널.

---

## 주요 기능 정리

| 기능 | 설명 |
|------|------|
| STT | Local Whisper / Google Cloud Speech / 확장 가능 아키텍처 |
| TTS | Kokoro(로컬) / OpenAI / ElevenLabs / Google Cloud TTS |
| VAD | SmartTurn 데몬, 음성 감지 자동 시작/중지 |
| Wake Word | 설정 가능한 트리거 단어, SmartTurn 데몬이 감지 |
| Sleep Word | 비활성화 트리거 단어 |
| Voice Modes | Push-to-Talk / Continuous / Ambient / Manual |
| Pre-roll Buffer | ~500ms 버퍼 (웨이크 워드 직전 음성 캡처) |
| Global Hotkey | 앱 비포커스 상태에서도 동작 |

---

## Ambient Mode 상세 (Vibe Guiding 핵심 채널)

```
마이크 항상 활성 (패시브 리스닝)
        ↓
Wake Word 감지
        ↓
대화형 턴-테이킹 모드 진입
        ↓
사용자 발화 → STT → 에이전트 처리 → TTS 응답
        ↓
침묵 또는 Sleep Word → 패시브 리스닝으로 복귀
```

---

## Vibe Guiding 접점 분석

### 🎯 접점 1: Ambient Mode + Vibe Guiding 컨텍스트
**시나리오**: 사용자가 GOBI Desktop을 사용하는 동안 Vibe Guiding이 Ambient Mode로 대기

```
사용자: "캡처 어떻게 해?"  (Wake Word 없이 자연스럽게)
        ↓
Vibe Guiding Agent (Ambient Mode):
"캡처 탭을 열고 녹음 버튼을 누르세요. 
 말씀하시면 실시간으로 전사되고, 
 AI가 구조화된 캔버스를 자동 생성합니다."
```

**실현 가능성**: ✅ 높음 — Ambient Mode는 이미 구현됨. Vibe Guiding 전용 System Prompt만 추가

### 🎯 접점 2: Wake Word 커스터마이징
Vibe Guiding 전용 Wake Word 설정:
- "Hey Gobi, 도움말" → Vibe Guiding 모드 활성화
- 현재 기능 또는 화면 컨텍스트 기반 맞춤 안내

**실현 가능성**: ⭐⭐ 중간 — Wake Word 동작은 구현됨, Vibe Guiding 라우팅 추가 필요

### 🎯 접점 3: TTS로 Vibe Guiding 안내 제공
Vibe Guiding 텍스트 안내 → TTS → 사용자에게 음성으로 안내
- 사용자가 화면을 보지 않아도 안내 수신 가능
- 멀티태스킹 중 도움 요청 가능

**실현 가능성**: ✅ 높음 — TTS 인프라 완성됨

---

## Vibe Guiding 설계 함의

> **Ambient Mode = Vibe Guiding의 자연스러운 UX 채널**

현재 Ambient Mode는 일반 Second Brain Agent에게 연결됨. 이를 Vibe Guiding 에이전트로 라우팅하거나, Vibe Guiding 컨텍스트를 시스템 프롬프트에 포함시키면 음성 기반 Vibe Guiding이 완성.

특히 **Pre-roll Buffer (~500ms)** 는 사용자가 도움 요청을 시작하자마자 첫 단어를 놓치지 않는 UX — Vibe Guiding 음성 인터페이스 품질에 직접 기여.
