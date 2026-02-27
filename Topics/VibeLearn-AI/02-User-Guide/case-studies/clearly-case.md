# 케이스 스터디: Clearly-BRD-PRD

> **"VibeLearn AI로 배운 예시 — Clearly 앱으로 BRD/PRD 작성하기"**

**작성일**: 2026-02-26
**Topic**: Clearly-BRD-PRD
**학습 기간**: 2026-02-01 ~ 2026-02-15 (실제 작업 5일)
**총 학습 시간**: 약 9.5시간
**최종 산출물**: YouTube 소개 영상 KR + EN

---

## 1. 시작 전 상태

### 학습자 배경

- Catch Up AI 채널 운영자
- Vibe Coding(AI 협업 개발)에 관심
- Clearly 앱에 대해 들어봤지만 직접 써본 적 없음
- **학습 목표**: Clearly 앱을 완전히 이해하고 소개 영상까지 만들기

### 해결하고 싶은 질문들

1. BRD와 PRD가 정확히 뭔지 모름
2. Clearly 앱이 어떤 문제를 해결하는지 불분명
3. "AI가 BRD/PRD를 만들어준다"는 게 실제로 어떤 건지 체험 미경험

---

## 2. 학습 과정 (3개 모듈)

### M1: Clearly 개요 및 핵심 개념 (2026-02-01, 3시간)

**한 것**:
- Clearly 앱 공식 사이트 및 문서 분석
- BRD vs PRD 개념 명확화
- Vibe Coding에서 요구사항 문서의 역할 이해

**만든 것** (`01-Clearly-Overview/`):
```
concepts/
├── what-is-clearly.md     ← Clearly가 무엇인지 (BRD/PRD 자동 생성 AI 도구)
├── brd-vs-prd.md          ← BRD(Why&What) vs PRD(What&How) 비교
└── vibe-coding-role.md    ← 아이디어 → 요구사항 → 코드의 연결점
guides/
└── clearly-quick-start.md ← 첫 번째 BRD 만들기까지 가이드
```

**핵심 발견**: Clearly의 핵심 가치는 단순한 문서 생성이 아니라
"BRD → PRD → Output Tool(AI 코딩 도구 설정 파일)" 자동 변환 파이프라인

---

### M2: 실제 BRD/PRD 작성 실습 (2026-02-08~15, 5.5시간, 3회 세션)

**한 것**:
- 실제 프로젝트(Catch Up AI 2026 홈페이지)로 BRD 3회, PRD 2회 작성
- Choose Output Tool로 Claude Code 설정 파일 자동 생성
- 버그 발견 및 개발자 보고 (4건)

**만든 것** (`02-CatchUpAI-BRD-PRD/`):
```
brd/
├── catchupai-2026-brd-v1.md   ← 첫 시도
├── catchupai-2026-brd-v2.md   ← 경험 기반 개선
└── catchupai-2026-brd-v3.md   ← 최종 (최고 품질)
prd/
├── catchupai-2026-prd-v1.md
└── catchupai-2026-prd-v2.md   ← 12개 섹션 상세 PRD
claude-code-output/             ← AI 코딩 도구 설정 파일 (자동 생성)
├── CLAUDE.md
├── PRD.md
└── REFERENCE_DOCUMENT.md
notes/
└── clearly-bug-report.md       ← 4건 버그 리포트
```

**반복의 힘 발견**:
- v1: "이렇게 쓰는 거구나" 파악
- v2: 이전 경험으로 빠르고 품질 좋게
- v3: v1,v2의 갭을 채워 최고 품질

> "같은 작업을 3번 하니 속도는 2배, 품질은 3배가 됐다" — Daily Retrospective 기록

---

### M3: 문서화 및 사용 가이드 (2026-02-15, 1시간)

**한 것**:
- M1~M2 경험을 바탕으로 "처음 사용자를 위한 가이드" 작성
- M2의 경험이 있어 계획(2-3h)의 절반 시간(1h)에 완료

**만든 것**:
```
guides/
└── clearly-usage-guide.md    ← 전체 워크플로우 상세 가이드 (핵심 산출물)
```

---

### M4 (추가): 소개 영상 제작 (Capstone, 2026-02-22~25, 약 8시간)

**한 것**:
- markdown-video 파이프라인으로 KR+EN 스크립트 작성
- Gemini API로 슬라이드 이미지 생성 (27개)
- OpenAI TTS로 오디오 생성 (27개 MP3)
- FFmpeg로 MP4 합성
- Remotion으로 애니메이션 버전 추가 제작
- YouTube 업로드

**만든 것** (`03-Clearly-Intro-Video/`):
- `clearly-intro-kr.mp4` (16:28, 한국어)
- `clearly-intro-en.mp4` (13:48, 영어)
- Remotion 버전 KR/EN (고품질)
- YouTube 업로드 메타데이터

---

## 3. 최종 산출물

### 교과서 품질 문서 (다른 학습자가 바로 사용 가능)

| 문서 | 위치 | 설명 |
|------|------|------|
| Clearly 소개 | `concepts/what-is-clearly.md` | Clearly가 뭔지 빠르게 파악 |
| BRD vs PRD | `concepts/brd-vs-prd.md` | 두 문서의 차이와 사용 시점 |
| 사용 가이드 | `guides/clearly-usage-guide.md` | 처음부터 끝까지 따라하는 가이드 |
| BRD v3 (최종) | `brd/catchupai-2026-brd-v3.md` | 실제 완성된 BRD 예시 |
| PRD v2 (최종) | `prd/catchupai-2026-prd-v2.md` | 12개 섹션 상세 PRD 예시 |

### YouTube 소개 영상

| 버전 | 링크 | 조회수 (업로드 후) |
|------|------|-----------------|
| 🇰🇷 한국어 | [AI가 질문 몇 가지로 BRD/PRD를 만들어준다?](https://youtu.be/crK2aO_uXkQ) | 16:28 |
| 🇺🇸 영어 | [AI Writes Your BRD & PRD in Minutes?](https://youtu.be/KwQOpU__BKo) | 13:48 |

---

## 4. 수치로 보는 결과

| 지표 | 수치 |
|------|------|
| 총 학습 시간 | 9.5시간 (계획: 7-10h ✅) |
| 실제 작업 일수 | 5일 (15일 기간 중) |
| 생성 산출물 | 22개 파일 |
| BRD/PRD 작성 횟수 | BRD 3회 + PRD 2회 |
| 발견한 버그 | 4건 (모두 개발자 보고) |
| YouTube 영상 | 2개 (KR + EN) |
| Self-Assessment | ⭐⭐⭐⭐⭐ (4.7/5) |

---

## 5. VibeLearn AI 없이 했다면?

### 방법 A: 유튜브 영상으로 공부
- 영상 3-5개 시청 → "이해했다" → 일주일 후 잊음
- 실제로 BRD/PRD 한 번도 안 써봄
- 소개 영상 제작은 엄두도 못 냄

### 방법 B: 공식 문서 읽기
- 영어 문서 읽기 → 개념은 이해 → 실습 없음
- 재현 가능한 산출물 없음
- 다음 사람에게 전달 불가

### VibeLearn AI로 한 것
- **9.5시간** → 완전한 이해 + 22개 산출물 + YouTube 영상 2개
- 다음 학습자가 이 폴더만 보고 Clearly를 배울 수 있음
- 영상을 통해 수천 명에게 지식 전파 가능

> "배움이 혼자 끝나지 않고, 다음 사람에게 이어진다"

---

## 6. VibeLearn AI 방법론 효과성 평가 (이 케이스에서)

| 요소 | 평가 | 비고 |
|------|------|------|
| Roadmap의 DoD 체크리스트 | ⭐⭐⭐⭐⭐ | 매 세션 완료 기준 명확 |
| WorkLog 실시간 작성 | ⭐⭐⭐⭐ | 3회 반복에도 이전 내용 재현 가능 |
| Daily Retrospective | ⭐⭐⭐⭐⭐ | "반복의 힘" 같은 인사이트 발견 |
| 산출물 중심 학습 | ⭐⭐⭐⭐⭐ | tangible한 결과물로 동기 유지 |
| 70/30 실습/이론 | ⭐⭐⭐⭐⭐ | M1(이론) → M2(실습 3회) 흐름이 자연스러움 |

---

## 7. 이 케이스에서 배울 수 있는 것

### Clearly를 배우고 싶은 사람에게
→ `Topics/Clearly-BRD-PRD/01-Clearly-Overview/` 폴더 참조

### VibeLearn AI 방법론을 이해하고 싶은 사람에게
→ 이 케이스가 방법론의 4단계가 실제로 작동하는 것을 보여줌:
1. Phase 1: topic_info.md 작성 → 폴더 구조 생성
2. Phase 2: Roadmap으로 3개 모듈 계획
3. Phase 3: 5번의 학습 세션, 22개 산출물
4. Phase 4: Final Retrospective + YouTube 영상 업로드

---

**케이스 작성자**: Claude with VibeLearn AI
**원본 학습 기록**: [Topics/Clearly-BRD-PRD/](../../Clearly-BRD-PRD/)
**YouTube 🇰🇷**: [https://youtu.be/crK2aO_uXkQ](https://youtu.be/crK2aO_uXkQ)
**YouTube 🇺🇸**: [https://youtu.be/KwQOpU__BKo](https://youtu.be/KwQOpU__BKo)
