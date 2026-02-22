# WorkLog - M3: Clearly 앱 소개 영상 제작

**날짜**: 2026-02-22
**Topic**: Clearly-BRD-PRD
**모듈**: M3 - Clearly App 소개 영상 제작
**학습 시간**: 약 2시간

---

## 오늘의 학습 목표

- [x] WorkLog 생성 및 M3 작업 계획 수립
- [x] 영상 스크립트 작성 (`03-Clearly-Intro-Video/clearly-intro-script.md`)
- [x] `/markdown-slides` 스킬로 Deckset 슬라이드 변환
- [ ] 스크린샷 수집 및 `_files_/` 폴더에 저장 (다음 세션)
- [ ] `/markdown-video` 스킬로 MP4 영상 생성 (다음 세션)
- [x] `03-Clearly-Intro-Video/README.md` 작성
- [x] GitHub 커밋 & 푸시

---

## 작업 컨텍스트

**이 작업은 M2 완료 후의 연장 학습입니다.**
M1 (Clearly 개념), M2 (BRD/PRD 실습)에서 얻은 모든 산출물과 인사이트를 활용하여
Clearly 앱을 소개하는 YouTube 영상을 제작합니다.

**사용 스킬**:
- `markdown-slides`: 마크다운 스크립트 → Deckset 슬라이드 변환 (SKILL.md 지침 준수)
- `markdown-video`: Deckset 슬라이드 → MP4 영상 (다음 세션 예정)

**참조한 기존 산출물**:
- `01-Clearly-Overview/concepts/` (3개 개념 문서)
- `01-Clearly-Overview/guides/` (2개 가이드 문서)
- `02-CatchUpAI-BRD-PRD/notes/wizard-experience.md`

---

## 진행 내용

### Phase 0: WorkLog 생성 ✅
- `vl_worklog/20260222_M3_Clearly-BRD-PRD.md` 생성
- `03-Clearly-Intro-Video/` 폴더 구조 준비
- `_files_/` 폴더 생성 (스크린샷 준비용)

---

### Phase 1: 영상 스크립트 작성 ✅

**산출물**: `03-Clearly-Intro-Video/clearly-intro-script.md`

**구성**:
| 섹션 | 슬라이드 | 예상 시간 |
|------|---------|---------|
| 1. 인트로 | 4장 | 2분 |
| 2. Vibe Coding & 문제 제기 | 4장 | 3분 |
| 3. Clearly 앱 소개 | 5장 | 3분 |
| 4. 단계별 사용법 데모 | 9장 | 5분 |
| 5. 실제 결과물 시연 | 4장 | 2분 |
| 6. 핵심 인사이트 & 아웃트로 | 3장 | 1분 |
| **합계** | **27장** | **~17-20분** |

**참조 문서**: M1, M2 학습 산출물 6개 파일 활용

**인사이트**:
- 기존 학습 산출물(개념 문서, 가이드, 실습 경험)이 영상 스크립트의 기반이 됨
- CUA_VL 방법론에서 "교과서 품질 산출물" 원칙이 이렇게 활용될 수 있다는 것을 확인

---

### Phase 2: Deckset 슬라이드 변환 ✅

**산출물**: `03-Clearly-Intro-Video/clearly-intro-script - slides.md`

**변환 작업 (SKILL.md 지침 준수)**:
- `slidenumbers: true` 프론트매터 추가
- 섹션 구분 H1 슬라이드 삽입
- 나레이션 텍스트 → `^` 스피커노트 변환 (각 슬라이드 끝)
- 테이블, 불릿, 코드 블록은 슬라이드 본문으로 유지
- 이미지 없음 (스크린샷 수집 후 추가 예정)

**주요 변환 패턴**:
- `### 슬라이드 N:` 레이블 → 제거 (Deckset에서 불필요)
- `## 섹션 N:` → H1 섹션 인트로 슬라이드로 변환
- 긴 설명 단락 → `^` 스피커노트

---

### Phase 3: 스크린샷 수집 ⏳ (다음 세션)

**필요한 스크린샷 목록**:
| # | 파일명 | 내용 |
|---|--------|------|
| 1 | `clearly-main.png` | clearlyreqs.com 메인 화면 |
| 2 | `project-create.png` | 프로젝트 생성 화면 |
| 3 | `brd-wizard.png` | BRD Wizard 질문 화면 |
| 4 | `brd-result.png` | 생성된 BRD 화면 |
| 5 | `prd-result.png` | 생성된 PRD 화면 |
| 6 | `output-tool.png` | Output Tool 선택 화면 |
| 7 | `homepage.png` | 완성된 홈페이지 화면 |

저장 위치: `03-Clearly-Intro-Video/_files_/`

---

### Phase 4: MP4 영상 생성 ⏳ (다음 세션)

스크린샷 수집 후 `/markdown-video` 스킬 실행 예정:
1. 슬라이드에 스크린샷 이미지 경로 삽입
2. OpenAI TTS로 오디오 생성 (nova 음성, 한국어)
3. Gemini로 AI 이미지 생성 (professional 스타일)
4. FFmpeg으로 MP4 합성

---

## DoD 체크리스트

| 항목 | 상태 |
|------|------|
| `03-Clearly-Intro-Video/` 폴더 생성 | ✅ |
| 영상 스크립트 (clearly-intro-script.md) 작성 | ✅ |
| Deckset 슬라이드 (clearly-intro-script - slides.md) 변환 | ✅ |
| README.md 작성 | ✅ |
| WorkLog 작성 | ✅ |
| GitHub 커밋 & 푸시 | ✅ |
| 스크린샷 수집 | ⏳ 다음 세션 |
| MP4 영상 생성 | ⏳ 다음 세션 |

**완료율**: 6/8 (75%) — 스크린샷 & 영상 생성은 다음 세션에 완료 예정

---

## Daily Retrospective

### What went well (잘된 점)
- **기존 산출물 재활용 성공**: M1, M2에서 만든 개념 문서와 가이드가 영상 스크립트의 완벽한 기반이 됨. CUA_VL의 "교과서 품질 산출물" 원칙이 실제로 가치를 발휘한 사례
- **구조적 스크립트**: 27장, 17-20분 분량의 체계적인 영상 스크립트를 효율적으로 작성
- **Deckset 변환 품질**: SKILL.md 지침에 따라 스피커노트, 슬라이드 구분, 섹션 구조를 정확하게 변환
- **GitHub 연결 이미 설정**: 연결 작업 없이 바로 푸시 가능한 상태임을 확인

### What could be improved (개선할 점)
- 스크린샷을 사전에 준비해두었다면 오늘 영상까지 완성 가능했음
- 다음 유사 작업 시: 영상 제작에 필요한 시각 자료를 먼저 수집하고 스크립트 작성하기

### Insights (인사이트)
- **학습 산출물의 재사용 가치**: M1, M2에서 만든 문서들이 새로운 산출물(영상 스크립트) 제작에 직접적으로 활용됨. CUA_VL의 "다음 학습자를 위한 길을 만든다" 철학이 자신에게도 적용됨
- **Deckset 슬라이드 포맷의 장점**: 스피커노트(`^`)가 TTS 나레이션 텍스트로 직접 변환되는 구조가 영상 제작 워크플로우를 크게 단순화
- **markdown-slides 스킬**: Claude Code에 등록된 스킬이 아닌 로컬 SKILL.md 파일임. 직접 실행 불가, SKILL.md 지침을 읽고 수동 구현 필요

### Tomorrow's focus (다음 집중할 것)
1. 스크린샷 7장 캡처 → `_files_/` 저장
2. 슬라이드 파일에 스크린샷 이미지 경로 삽입
3. `/markdown-video` 스킬로 MP4 영상 생성

---

## 산출물 요약

### 오늘 생성된 파일

| 파일 | 위치 | 설명 |
|------|------|------|
| WorkLog | `vl_worklog/20260222_M3_Clearly-BRD-PRD.md` | 이 파일 |
| 영상 스크립트 | `03-Clearly-Intro-Video/clearly-intro-script.md` | 27 슬라이드, 한국어 |
| Deckset 슬라이드 | `03-Clearly-Intro-Video/clearly-intro-script - slides.md` | 스피커노트 포함 |
| README | `03-Clearly-Intro-Video/README.md` | 모듈 요약 |
| 스크린샷 폴더 | `03-Clearly-Intro-Video/_files_/` | 비어있음 (다음 세션 채움) |

### 전체 03-Clearly-Intro-Video 폴더 구조

```
03-Clearly-Intro-Video/
├── README.md                                    (오늘 생성)
├── clearly-intro-script.md                      (오늘 생성)
├── clearly-intro-script - slides.md             (오늘 생성)
├── _files_/                                     (스크린샷 폴더, 비어있음)
├── audio/                                       (다음 세션 자동 생성)
├── slides-gemini/                               (다음 세션 자동 생성)
└── clearly-intro.mp4                            (다음 세션 완성)
```

---

**작성자**: CUA_VL 학습자
**방법론**: CUA_VL (VibeLearn AI)
