# VibeLearn AI Topic Starter

---

## 📌 Topic 기본 정보

### Topic 이름

```
Topic 이름: Live-CoMC-App
```

### Topic 설명

```
설명: 매주 일요일 3시간 라이브 방송(AI in Action Live)을 함께 진행할 로컬 데스크톱 보조
MC 앱을 만드는 프로젝트형 Topic. 진행자가 호출어로 깨워 목소리로 지시하면, 이 앱이
매주 축적되는 방송 문서(Rundown, Daily Roundup, Weekly Progress, Weekly Dashboard)를
읽고 화면 텍스트 + 음성으로 공동 MC처럼 방송을 진행한다.
```

### 학습 목적

```
학습 목적:
- VibeLearn AI 방법론을 "학습"이 아니라 "제품 개발"에 실제로 적용해 그 유효성을 검증한다
- 실시간 음성 파이프라인(Wake Word → STT → LLM → TTS)을 설계·구현할 수 있게 된다
- 라이브 방송처럼 되돌릴 수 없는 실시간 환경에서 AI 발화를 안전하게 통제하는 설계 역량을 기른다
- Live21 Rundown에 이미 적힌 목표 — "이 앱이 완성되면 오늘 이 Rundown 문서 자체가 앱의 입력이 된다" — 를 실현한다
```

### 예상 학습 기간

```
예상 기간: 약 3개월 — 12주 (주당 7~8시간, 총 약 90시간)
```

> 2026-08-02 HITL-1(학습 기간 적정성 분석) 결과, 사용자가 권장 범위(1~3개월)의
> 상한인 3개월(12주, 90시간)로 확정했다. 원래 추정치는 6~8주/59시간이었으나,
> 안전장치 검증과 리허설에 더 여유를 두기 위해 확장했다.

---

## 🎯 학습 목표

```
- [ ] 매주 형식이 조금씩 달라지는 Rundown 문서를 안정적으로 파싱하는 계약(스키마)을 설계할 수 있다
- [ ] 근거 없는 발화를 구조적으로 차단하는 안전 검증 파이프라인(Claim-Evidence 강제, 커버리지 화이트리스트)을 구현할 수 있다
- [ ] Wake Word → VAD → STT → LLM → TTS로 이어지는 실시간 음성 파이프라인을 직접 구현할 수 있다
- [ ] LLM(OpenAI/Claude/Gemini)과 TTS(Edge-TTS/Qwen3-TTS/OpenAI/ElevenLabs)를 프로바이더 교체 가능한 구조로 추상화할 수 있다
- [ ] Electron 셸 + Python 사이드카로 데스크톱 앱을 만들고 OBS와 연동할 수 있다
- [ ] 실제 방송 환경에서 리허설을 거쳐 라이브 투입 가능 여부를 스스로 판단할 수 있다
```

---

## 🛠️ 학습 환경

### 운영 체제

```
OS: Windows 11
버전: i7-1355U (15W), 16GB RAM, GPU 없음 — 클라우드 API 우선, 로컬 추론은 wake word/VAD 등 경량 작업만
```

### 주요 도구 및 기술 스택

```
- VS Code (Claude Code + Codex Extension — 방송 중 실제 사용 도구)
- Python 3.13
- Node.js 22 / Electron
- ffmpeg
- OpenAI API, Anthropic API, Google Gemini API (LLM 멀티 프로바이더)
- Edge-TTS, Qwen3-TTS(DashScope), OpenAI TTS, ElevenLabs (TTS 멀티 프로바이더)
- OBS Studio (Browser Source, VoiceMeeter Banana, VB-CABLE)
```

### 사전 지식 (Prerequisites)

```
필수:
- Python 파일/JSON 처리
- Markdown 문서 구조 파싱 경험
- VS Code 기본 사용

권장:
- 이 볼트의 Vibe-Guiding-VSCode Topic(파일 기반 계약 패턴)
- Node.js/Electron 기초
- 실시간 오디오 스트리밍 개념
```

---

## 📚 참조 자료 (Optional)

### 관련 GitHub 저장소

```
- openWakeWord: https://github.com/dscripka/openWakeWord
- Silero VAD: https://github.com/snakers4/silero-vad
```

### 추가 학습 자료

```
vl_materials/ 폴더에 추가할 자료:
- Live20/Live21 Weekly Rundown 실제 파일 사본 (파서 검증용)
- 방송 안전 규약 원본: _Settings_/Skills/live-broadcast/SKILL.md, rundown-writer/SKILL.md
```

**Topic 내 참조 (볼트 내 선례)**:
- 파일 기반 파이프라인 패턴: `Topics/Vibe-Guiding-VSCode/04-Guiding-Engine-POC/`
- API 연결 검증 하네스 패턴: `Topics/Qwen3-TTS/03-Setup-API/harness/connection_probe.py`
- 학습 산출물과 실행 앱 분리 배치: `Topics/Remotion-VideoCreation/my-first-video/`
- 승인 설계안: `C:\Users\dougg\.claude\plans\ethereal-puzzling-seahorse.md` (2026-08-02 사용자 승인)

---

## 🎓 학습 접근 방식 (Optional)

### 선호하는 학습 스타일

```
- [x] 실습 중심, 필요한 이론만 (권장)
```

### 시간 투자 계획

```
- 주당 학습 시간: 8~10시간
- 학습 가능 요일: 방송 준비 주간 내 (일요일 방송 제외)
- 1회당 학습 시간: 2~3시간 권장
```

### 특별히 집중하고 싶은 영역

```
- 실시간 시스템에서의 안전장치 설계 (되돌릴 수 없는 라이브 발화 통제)
- 멀티 프로바이더 추상화 (LLM 3종, TTS 4종)
- 방송 사고 사후 분석이 가능한 파일 기반 추적(trace) 설계
```

---

*이 파일은 승인된 설계 계획(`ethereal-puzzling-seahorse.md`)의 요약본이다. 세부 모듈 구성·기술 아키텍처·안전장치·MVP 경계는 해당 계획 문서 및 이후 생성될 Roadmap을 참조한다.*

**Template Version**: 1.0
**Created**: 2026-08-02
