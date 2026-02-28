# M3 Module Retrospective: 소개 영상 제작 (Capstone)

**Topic**: VibeLearn-AI
**모듈**: M3 — 소개 영상 제작 (Capstone)
**작성일**: 2026-02-27
**학습일**: 2026-02-27
**실제 소요 시간**: ~4시간 (예상 6-8h → 실제 4h)

---

## 📊 DoD (Definition of Done) 최종 평가

| 항목 | 완료 | 비고 |
|------|:----:|------|
| KR 스크립트 완성 (24개 슬라이드) | ✅ | 6개 섹션, vibelearn-intro-script-kr.md |
| EN 스크립트 완성 (자연스러운 번역) | ✅ | vibelearn-intro-script-en.md |
| KR Deckset 슬라이드 파일 생성 | ✅ | `vibelearn-intro-script-kr - slides.md` |
| EN Deckset 슬라이드 파일 생성 | ✅ | `vibelearn-intro-script-en - slides.md` |
| KR TTS 오디오 (24개 MP3) | ✅ | nova 음성, 7.6MB |
| EN TTS 오디오 (24개 MP3) | ✅ | alloy 음성, 6.4MB |
| KR Gemini 슬라이드 (24개 JPEG) | ✅ | gemini-3-pro-image-preview |
| EN Gemini 슬라이드 (24개 JPEG) | ✅ | gemini-3-pro-image-preview |
| vibelearn-intro-kr.mp4 생성 | ✅ | 8분 15초, 18.6MB |
| vibelearn-intro-en.mp4 생성 | ✅ | 7분 00초, 16.4MB |
| README.md 작성 | ✅ | 03-Intro-Video/README.md |
| YouTube 메타데이터 준비 | ✅ | youtube-metadata.md |
| YouTube 업로드 | ⏳ | 다음 세션 |
| WorkLog 작성 + Daily Retrospective | ✅ | 20260227_M3_VibeLearn-AI.md |

**DoD 달성률**: 93% (YouTube 업로드 1개 항목 미완)

---

## 🎯 학습 목표 달성 평가

### M3 학습 목표

| 목표 | 달성도 | 비고 |
|------|:------:|------|
| 기존 모듈 산출물을 영상 스크립트 자료로 활용 | ✅ | M1·M2 → 스크립트 직접 변환 |
| KR/EN 듀얼 영상 제작 파이프라인 실행 | ✅ | 오디오 + 슬라이드 + MP4 |
| Capstone으로서 Topic 전체를 집약 | ✅ | 6개 섹션이 Topic 전체를 커버 |
| Deckset 슬라이드 형식 파이프라인 적용 | ✅ | 테이블 구분자 문제 해결 포함 |

---

## ✅ 잘 된 것 (What Went Well)

### 1. M1·M2 산출물 → 스크립트 자동 완성 효과
M1에서 만든 개념 문서(what-is-vibelearn-ai.md, system-architecture.md 등)와 M2에서 만든 케이스 스터디가 스크립트의 뼈대가 됐다. 따로 자료 조사 없이 기존 파일에서 바로 내용을 끌어올 수 있었기 때문에 60분 안에 24슬라이드 KR 스크립트를 완성할 수 있었다.

**핵심 인사이트**: VibeLearn AI의 "모듈 산출물이 다음 모듈의 입력이 된다"는 특성이 Capstone에서 극대화된다.

### 2. Clearly 케이스 경험 완전 재사용
Clearly-BRD-PRD M3에서 markdown-video 파이프라인을 처음 학습했다. VibeLearn-AI M3에서는 동일한 파이프라인을 그대로 재사용 — 추가 학습 없이 즉시 실행 가능했다.

### 3. 실제 소요 시간이 예상보다 50% 단축
예상 6-8h → 실제 4h. KR+EN 동시 제작임에도 불구하고. 이유: Clearly 케이스에서 학습한 경험(파이프라인 사용법, 테이블 구분자 문제, Gemini API 키 설정)이 그대로 적용됐기 때문.

---

## 🔧 개선할 것 (What Could Be Improved)

### 1. 영상 길이 목표 미달
- **목표**: 15-18분
- **실제**: KR 8:15, EN 7:00
- **원인**: 나레이션(슬라이드당 1-2 문단)이 의도한 것보다 짧게 작성됨
- **개선 방향**: 슬라이드당 나레이션을 3-4 문단으로 확장하거나, 슬라이드 수를 늘리거나, 실제 화면 공유 데모 섹션 추가

### 2. 테이블 구분자 문제는 파이프라인에서 처리해야
현재: 사용자가 수동으로 `|------|` → `|:--:--|` 교체
이상적: make_video.py가 파싱 전에 자동 처리
→ GitHub Issue로 등록 권장

### 3. Section divider 슬라이드의 오디오 없음
섹션 제목 슬라이드 6개는 speaker notes가 없어 오디오가 없다. 결과적으로 화면 전환이 매우 빠름 (약 0.5초). 섹션 전환 효과음이나 최소 2-3초 패딩이 있으면 더 좋을 것.

---

## 💡 핵심 인사이트 (Key Insights)

### Capstone의 진짜 의미
M3가 "Capstone"인 이유를 직접 체험했다:
- M1 개념 문서 → M3 섹션 3 (VibeLearn AI 소개) 자료
- M2 케이스 스터디 → M3 섹션 5 (케이스 스터디) 자료
- M2 사용 가이드 → M3 섹션 4 (사용법) 자료

전 모듈의 산출물이 Capstone 하나로 집약된다. 이게 설계된 것이었지만, 직접 해보니 "자연스럽게 가져다 쓸 수 있다"는 느낌이 매우 강했다.

### VibeLearn AI가 자기 자신을 증명
이번 Topic은 VibeLearn AI 방법론을 배우면서, VibeLearn AI 방법론으로 진행되었다. 즉, 방법론을 배우는 과정이 그 방법론의 산 증거가 됐다. 이 Topic의 산출물(문서, 영상)이 곧 VibeLearn AI의 실제 작동 증거.

### 다음 Topic에서 적용할 것
파이프라인 경험이 축적될수록 Capstone 소요 시간이 줄어든다. 다음 Topic M3는 아마 3시간 이내로 가능할 것.

---

## 📈 M3 역량 평가 (AI 시대 기준)

| 역량 | 수준 | 근거 |
|------|:----:|------|
| 영상 스크립트 구성 (KR/EN) | ★★★★☆ | 24슬라이드, 6섹션 스토리라인 자연스러움 |
| markdown-video 파이프라인 운용 | ★★★★★ | 독립적으로 실행, 오류 즉시 해결 |
| TTS + Gemini 이미지 생성 API 활용 | ★★★★☆ | 유료 키 전환, 음성 선택 최적화 |
| Deckset 슬라이드 형식 마스터 | ★★★★☆ | 구분자 문제 해결 포함 |
| Capstone 통합 사고 | ★★★★★ | 모든 모듈 산출물을 영상으로 집약 |

---

## 🔗 M3 산출물 링크

- [vibelearn-intro-kr.mp4](vibelearn-intro-kr.mp4) — KR 소개 영상 (8:15)
- [vibelearn-intro-en.mp4](vibelearn-intro-en.mp4) — EN 소개 영상 (7:00)
- [vibelearn-intro-script-kr.md](vibelearn-intro-script-kr.md) — KR 스크립트
- [vibelearn-intro-script-en.md](vibelearn-intro-script-en.md) — EN 스크립트
- [youtube-metadata.md](youtube-metadata.md) — YouTube 업로드 메타데이터
- [WorkLog](../vl_worklog/20260227_M3_VibeLearn-AI.md)

---

**작성자**: Claude with VibeLearn AI
**방법론**: VibeLearn AI v2.0
