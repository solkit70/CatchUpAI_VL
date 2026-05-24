---
title: "Qwen3-TTS 학습 로드맵"
created: 2026-05-16 15:00:00
updated: 2026-05-16 17:30:00
author:
  - "[[Changsoo]]"
tags:
  - vibe-learn-ai
  - roadmap
  - tts
  - alibaba-qwen
---

# Qwen3-TTS 학습 로드맵 (API 기반)

**생성일**: 2026-05-16 · **개정**: 2026-05-16 (로컬 → API 전환)
**방법론**: VibeLearn AI 2.0 · **버전**: 2.0

> **환경 전환 메모**: 이 PC는 GPU 없음 + Intel i7-1355U(15W 저전력) + RAM 16GB.
> 공식 `qwen-tts`는 CPU 미지원, 비공식 Rust/Q4도 이 칩에선 비효율 → **API 기반으로 확정**.
> 근거·분석: 플랜 파일 / [02-Setup-Windows](../02-Setup-Windows/README.md)(로컬 부적합 부록).

## 📚 학습 개요

### Topic 소개
Qwen3-TTS는 알리바바 Qwen 팀이 2026-01 Apache-2.0으로 공개한 오픈소스 TTS 패밀리(0.6B/1.7B). 본 토픽은 **Alibaba Cloud Model Studio / DashScope API**(OpenAI 호환 엔드포인트)로 Qwen3-TTS를 사용해, 그 음성을 Remotion 영상 제작 파이프라인에 연동하는 것을 목표로 한다. 로컬 설치·GPU 불필요.

### 학습 목표
- Qwen3-TTS의 기능·모델군·라이선스를 파악한다 (M1 완료)
- DashScope Intl API 키를 발급하고 한국어 합성을 호출할 수 있다
- API로 보이스 클론·음색 설계를 수행하고 기존 TTS와 품질을 비교한다
- Qwen3-TTS(API) 음성 제작 Skill을 만들어 Remotion에 연동한다
- 교과서/매뉴얼 수준 산출물을 남긴다

### 예상 학습 기간
1주 집중 · 5개 모듈 · 총 약 20시간 (API 전환으로 설치 부담 감소)

### 학습 환경
- 실행: **Cloud API — Alibaba Cloud Model Studio / DashScope (Intl, 싱가포르)**, OpenAI 호환 엔드포인트
- 도구: Python, `dashscope`(>=1.23.9) 또는 `openai` SDK, ffmpeg(길이 측정/변환)
- 백업 제공자: Replicate `qwen/qwen3-tts`
- 기존 자산: Remotion 영상 제작 Skill (현행 OpenAI TTS / edge-tts 기반 `gen_audio.py`·`durations.json`)
- 사전 지식: Python·TTS 파이프라인 운용 경험(필수)

> **AI 시대 학습 원칙**: 정확한 모델명/파라미터는 공식 Model Studio 문서를 1차 출처로 직접 확인. 검증 가능한 산출물(재생되는 mp3/스크립트/MP4)로 마무리.

## 🗺️ 전체 로드맵 구조

| 모듈 | 모듈명 | 난이도 | 예상 시간 | 산출물 폴더 |
| --- | --- | --- | --- | --- |
| M1 | 개요·아키텍처·자료 조사 | ⭐ | 3h | `01-Overview/` (✅ 완료) |
| M2 | DashScope API 환경 구축 | ⭐⭐ | 3h | `02-Setup-API/` |
| M3 | API 보이스 클론 & 음색 설계 | ⭐⭐ | 5h | `03-VoiceClone/` |
| M4 | Qwen3-TTS(API) Skill 제작 | ⭐⭐⭐ | 5h | `04-Skill/` |
| M5 | Remotion 통합 (Capstone) | ⭐⭐⭐ | 5h | `05-Remotion-Integration/` |

**총 예상 시간**: 약 21시간

## 📖 모듈별 상세 계획

### M1 - 개요·아키텍처·자료 조사  ✅ 완료 (2026-05-16)

**난이도**: ⭐ · **산출물**: `01-Overview/`
M1은 완료됨. 공식 1차 출처(GitHub `QwenLM/Qwen3-TTS`, 블로그)·모델 변형 5종·Apache-2.0·10개 언어(한국어)·3초 클론+`ref_text`·비교 매트릭스 확정.
→ [01-Overview/README.md](../01-Overview/README.md)

### M2 - DashScope API 환경 구축

**난이도**: ⭐⭐
**예상 시간**: 3h
**산출물 폴더**: `02-Setup-API/`

#### 학습 목표
- [ ] Alibaba Cloud 계정 + DashScope **Intl** API 키를 발급할 수 있다
- [ ] `dashscope`(또는 OpenAI 호환) SDK를 설치하고 키를 안전하게 설정할 수 있다
- [ ] OpenAI 호환 엔드포인트로 **한국어 1문장**을 합성해 mp3로 저장할 수 있다
- [ ] 호출 절차를 재현 가능한 가이드(완료 신호 포함)로 문서화할 수 있다

#### 주요 개념
1. **DashScope Intl vs China 키**: 비중국 사용자는 Intl(싱가포르) 키 필요, China 키와 비호환.
2. **OpenAI 호환 모드**: `base_url=https://dashscope-intl.aliyuncs.com/compatible-mode/v1` → 기존 OpenAI SDK 코드 재사용.
3. **모델명**: `qwen3-tts-vc-*`(클론), `qwen3-tts-vd-*`(음색 디자인) — 정확한 최신명은 공식 문서로 확정.
4. **키 보안**: API 키는 환경변수(`DASHSCOPE_API_KEY`)로, 코드/노트에 평문 금지.

#### 실습 과제

**실습 1: 계정·키 발급** ⭐⭐
- **목적**: Intl API 접근 확보
- **단계**:
  1. Alibaba Cloud 가입 → Model Studio(국제) 활성화
  2. DashScope 콘솔 → API-KEY 관리 → Intl 키 생성
  3. 키를 환경변수로 설정 (PowerShell: `setx DASHSCOPE_API_KEY "..."`)
- **예상 시간**: 45분
- **검증**: 키 발급 완료, 새 셸에서 환경변수 인식. (발급 불가 시 Replicate로 폴백 — troubleshooting 기록)

**실습 2: 첫 한국어 합성** ⭐⭐
- **목적**: 엔드투엔드 호출 검증
- **단계**:
  1. `pip install -U dashscope` (또는 `openai`)
  2. OpenAI 호환 모드로 한국어 1문장 합성 → `02-Setup-API/examples/hello_ko.mp3`
  3. 영어 1문장 → `hello_en.mp3`, 호출 지연 기록
- **예상 시간**: 60분
- **검증**: mp3 2개 생성 + 정상 재생

**실습 3: 가이드 문서화** ⭐⭐
- **목적**: 재현성
- **단계**: 키 발급~첫 합성을 `guides/api-setup.md`에 명령어 + 완료 신호로 정리, 오류는 troubleshooting에 기록
- **예상 시간**: 45분
- **검증**: 처음 보는 사람이 가이드만으로 한국어 합성 1건 성공

#### 산출물
```
02-Setup-API/
├── README.md
├── guides/
│   └── api-setup.md       ← 키 발급·SDK·첫 합성(완료 신호)
├── examples/
│   ├── hello_ko.mp3
│   └── hello_en.mp3
└── troubleshooting/
    └── known-issues.md    ← 키 리전·인증·과금·폴백
```

#### Definition of Done
- [ ] DashScope Intl 키 발급 + 환경변수 설정
- [ ] SDK 설치
- [ ] 한국어·영어 mp3 각 1개 생성·재생
- [ ] `api-setup.md`(완료 신호 포함) 작성
- [ ] 트러블슈팅 1건 이상 + WorkLog/Retrospective

#### Self-Assessment
**개념 이해**: Intl/China 키 차이·OpenAI 호환 모드를 설명 가능
**실무 활용**: AI에게 합성 호출 코드 작성을 지시 가능
**문제 해결**: 인증/리전 오류 시 디버깅 방향 제시 가능

#### 예상 시간 배분
- 개념: 20분 / 실습1: 45분 / 실습2: 60분 / 실습3: 45분 / 문서화: 10분 — **약 3h**

#### 참조 자료
- Alibaba Cloud Model Studio: qwen-tts API / 첫 API 호출 가이드
- DashScope Intl OpenAI 호환 엔드포인트 문서
- (폴백) Replicate `qwen/qwen3-tts`

### M3 - API 보이스 클론 & 음색 설계

**난이도**: ⭐⭐
**예상 시간**: 5h
**산출물 폴더**: `03-VoiceClone/`

#### 학습 목표
- [ ] API로 3초 참조 샘플을 등록해 voice id를 발급받을 수 있다
- [ ] 등록한 음성으로 한국어·영어 합성을 수행할 수 있다
- [ ] 자연어 음색 디자인(voice design) API로 톤을 제어할 수 있다
- [ ] 기존 TTS(edge-tts/OpenAI)와 품질을 4축으로 A/B 비교할 수 있다

#### 주요 개념
1. **클론 플로우(API)**: 참조 오디오(3초)+필요 시 텍스트 → 등록 → voice id → 합성 시 지정.
2. **보이스 디자인**: 자연어 instruct로 새 음색 생성(`qwen3-tts-vd-*`).
3. **과금 단위**: 클론 $0.01/건, 합성 ≈ $0.013/1k자 — 테스트량 관리.
4. **품질 4축**: 명료도·자연스러움·화자 유사도·발음 정확도(고유명사).

#### 실습 과제
**실습 1: API 보이스 클론** ⭐⭐ — 본인 3초 샘플 등록 → voice id → KR/EN 합성 → `examples/` (80분, 검증: 합성본+유사도 메모)
**실습 2: 음색 디자인** ⭐⭐ — instruct 3종(차분 설명체/밝은 소개체/진중 마무리체) 비교 → 영상 섹션 매핑 표 (70분)
**실습 3: 3엔진 A/B** ⭐⭐⭐ — 동일 한국어 내레이션을 Qwen3-TTS(API)/edge-tts/OpenAI로 생성, 4축 점수표 (60분)

#### 산출물
```
03-VoiceClone/
├── README.md
├── guides/{voice-clone-api.md, timbre-design.md}
├── examples/        ← 합성 mp3
└── concepts/quality-eval.md
```

#### Definition of Done
- [ ] API 클론 KR/EN 합성 성공 · [ ] 음색 3종 비교 · [ ] 3엔진 A/B 표 · [ ] 섹션 톤 매핑 · [ ] WorkLog/Retrospective

#### Self-Assessment
개념: 클론 API 플로우 설명 / 실무: 원하는 톤을 instruct로 획득 / 문제해결: 품질 저하 원인(샘플/프롬프트/언어) 진단

#### 예상 시간 배분
개념 40분 / 실습 80+70+60분 / 문서화 40분 — **약 5h**

#### 참조 자료
- Model Studio: Qwen voice cloning API / voice design API 레퍼런스
- 기존 `gen_audio.py`·OpenAI TTS(비교 기준)

### M4 - Qwen3-TTS(API) Skill 제작

**난이도**: ⭐⭐⭐
**예상 시간**: 5h
**산출물 폴더**: `04-Skill/`

#### 학습 목표
- [ ] 텍스트→음성(API)을 재사용 Skill(스크립트+SKILL.md)로 캡슐화할 수 있다
- [ ] 입력(text/voice/lang/speed)·배치·재시도·에러 처리를 설계할 수 있다
- [ ] 기존 Remotion 규약(`slide_XX.mp3` + `durations.json`)과 호환 출력을 낸다
- [ ] 백엔드 인자(`qwen3-api`/`openai`/`edge`)로 교체 가능한 인터페이스를 만든다

#### 주요 개념
1. **API 호출 캡슐화**: 키·엔드포인트·모델명을 설정으로 분리.
2. **Remotion 규약 호환**: 파일명·`durations.json` 포맷 동일 산출.
3. **배치/재시도/요금 가드**: 슬라이드 N개 일괄, 실패 재시도, 호출량/비용 로깅.
4. **백엔드 추상화**: 동일 인터페이스로 다중 TTS 백엔드.

#### 실습 과제
**실습 1: 생성기** ⭐⭐ — `04-Skill/qwen3_tts_api_gen.py`(단일/배치, 길이 측정) (90분)
**실습 2: Remotion 규약 출력** ⭐⭐⭐ — 스크립트 목록→`slide_XX.mp3`+`durations.json`(기존 포맷 일치) (90분)
**실습 3: SKILL.md** ⭐⭐ — 목적/사전조건/사용법/입력 스키마/완료 신호/알려진 오류 Atomic Guide Unit (60분)

#### 산출물
```
04-Skill/{README.md, SKILL.md, qwen3_tts_api_gen.py, examples/sample_durations.json, troubleshooting/known-issues.md}
```

#### Definition of Done
- [ ] 생성기 단일/배치 동작 · [ ] `durations.json` 호환 · [ ] SKILL.md(완료 신호·오류) · [ ] 백엔드 인자화 · [ ] WorkLog/Retrospective

#### Self-Assessment
개념: Skill 입출력 계약 설명 / 실무: AI에게 Skill 확장 지시 / 문제해결: 배치 일부 실패 복구 전략

#### 예상 시간 배분
설계 45분 / 실습 90+90+60분 / 문서화 45분 — **약 5h**

#### 참조 자료
- 기존 Remotion `gen_audio.py`·`durations.json`(호환 기준)
- 기존 vault Skills의 SKILL.md 구조

### M5 - Remotion 통합 (Capstone)

**난이도**: ⭐⭐⭐
**예상 시간**: 5h
**산출물 폴더**: `05-Remotion-Integration/`

#### 학습 목표
- [ ] OpenAI 호환 `base_url` 교체로 Qwen3-TTS(API)를 Remotion 오디오 단계에 드롭인할 수 있다
- [ ] 실제 짧은 영상의 내레이션을 Qwen3-TTS로 생성·렌더할 수 있다
- [ ] OpenAI/edge-tts 대비 채택 기준(품질/비용/지연)을 문서화할 수 있다
- [ ] 토픽 전체를 교과서/매뉴얼로 통합한다

#### 주요 개념
1. **OpenAI 호환 드롭인**: 기존 OpenAI TTS 코드의 `base_url`/`api_key`/`model` 교체.
2. **엔드투엔드**: 텍스트→API 음성→`durations.json`→타임라인→MP4.
3. **채택 의사결정**: 상황별(클론/일관 캐릭터/비용) 백엔드 가이드.
4. **비용 추정**: 영상 분량 기준 월 비용 산정.

#### 실습 과제
**실습 1: 파이프라인 연결** ⭐⭐⭐ — 한 컴포지션 오디오를 M4 Skill로 교체 → `slide_XX.mp3`+`durations.json` → data.ts 반영 → Studio 싱크 (100분)
**실습 2: 영상 1편 렌더** ⭐⭐⭐ — 짧은 샘플 영상 Qwen3-TTS 음성으로 렌더 → `out/` (90분)
**실습 3: 채택 가이드 + 통합 매뉴얼** ⭐⭐ — 3엔진 결론·비용 → adoption-guide.md, M1~M5 통합 MANUAL.md (60분)

#### 산출물
```
05-Remotion-Integration/{README.md, guides/{integration.md, adoption-guide.md}, out/, MANUAL.md}
```

#### Definition of Done
- [ ] Remotion 오디오 Qwen3-TTS(API) 연동 · [ ] 샘플 MP4 1편 · [ ] 채택 기준표(비용 포함) · [ ] 통합 MANUAL.md · [ ] Module+Topic Retrospective

#### Self-Assessment
개념: 백엔드 교체 영향 설명 / 실무: 프로젝트별 백엔드 선택 / 문제해결: 싱크·품질 이슈 단계 진단

#### 예상 시간 배분
설계 40분 / 실습 100+90+60분 / 문서화 50분 — **약 5h**

#### 참조 자료
- Remotion 영상 제작 Skill(연동 대상) · M4 `04-Skill/SKILL.md`

## 📝 WorkLog 작성 가이드
파일명: `vl_worklog/YYYYMMDD_MX_Qwen3-TTS.md`. 섹션: 오늘 목표 / 진행 내용 / 문제 해결 로그 / DoD / Daily Retrospective / 참조·산출물.

## 🔍 Retrospective 가이드
- Daily(WorkLog 내): well/improve/insights/tomorrow
- Module 완료: `YYYYMMDD_MX_Retrospective.md`
- Topic 완료: `YYYYMMDD_Qwen3-TTS_Final_Retrospective.md`

## 📂 전체 폴더 구조
```
Qwen3-TTS/
├── topic_info.md
├── vl_prompts/ · vl_roadmap/ · vl_worklog/ · vl_materials/
├── 01-Overview/            (M1 ✅)
├── 02-Setup-Windows/       (로컬 검토 부록 — superseded)
├── 02-Setup-API/           (M2)
├── 03-VoiceClone/          (M3)
├── 04-Skill/               (M4)
└── 05-Remotion-Integration/(M5)
```

## 📊 학습 진행 상황 추적

| 모듈 | 시작일 | 종료일 | 상태 | DoD 달성률 | 비고 |
|------|--------|--------|------|-----------|------|
| M1 | 2026-05-16 | 2026-05-16 | ✅ | 100% | 개요·자료 조사 완료 |
| M2 | | | ⏳ | 0% | API 환경(키 발급 선행) |
| M3 | | | ⏳ | 0% | |
| M4 | | | ⏳ | 0% | |
| M5 | | | ⏳ | 0% | |

**범례**: ⏳ 대기 · 🔄 진행 중 · ✅ 완료

## 🎯 성공 기준
- [ ] M2~M5 DoD 100%
- [ ] Qwen3-TTS(API) Skill이 Remotion에서 동작 (Capstone)
- [ ] OpenAI/edge-tts 대비 채택 기준 + 비용 추정 문서화
- [ ] 토픽 통합 MANUAL.md(교과서 품질)
- [ ] Topic Retrospective

---

**생성자**: Claude with VibeLearn AI · **Roadmap 버전**: 2.0 (API) · **방법론**: VibeLearn AI 2.0
