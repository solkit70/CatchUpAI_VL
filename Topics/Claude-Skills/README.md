# Claude Skills Collection

**Claude Code를 위한 실용적인 Skill 모음**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Claude Code](https://img.shields.io/badge/Claude-Code-blueviolet)](https://claude.ai)

---

## 소개

이 Repository는 Claude Code에서 사용할 수 있는 3개의 실용적인 Skill을 포함합니다.
CUA_VL (Catch Up AI Vibe Learning) 방법론을 사용하여 2주간 학습하며 개발했습니다.

### 포함된 Skill

| Skill | 설명 | 폴더 |
|-------|------|------|
| **CUA_VL Skill** | AI 학습 방법론 자동화 - Topic 시작, Roadmap 생성, Daily 학습 지원 | `02-Skill-A-CUA-VL/` |
| **YouTube→MD Skill** | YouTube 영상을 한국어 마크다운으로 변환 - 자막 추출, AI 요약, 구조화 | `03-Skill-B-YouTube-MD/` |
| **Video Edit Skill** | 영상 편집 자동화 - 무음 구간 제거, 필러 단어 제거 | `04-Skill-C-Video-Edit/` |

---

## 🎬 이 Topic 으로 만든 영상

| 날짜 | 영상 | 길이 |
|---|---|---|
| 2026-01-29 | [재미로 하는 Vibe Coding 번외편 — 유튜브 영어 영상 자막을 한국어로 요약해 주는 Skill 을 커뮤니티 GitHub Repo 에 PR 하기](https://youtu.be/NWy139jzKwg) | 1:12:33 |
| 2026-01-30 | [AI-powered PKM 실습 — 영어 유튜브 영상을 한글로 요약해 주는 Skill 소개 및 GitHub PR 실전 데모](https://youtu.be/HWU3iYJK-8Y) | 33:48 |

YouTube→MD Skill(`03-Skill-B-YouTube-MD/`)을 만들고 공개하는 과정입니다.

---

## 빠른 시작

### 1. CUA_VL Skill

새로운 학습 Topic을 시작할 때 사용합니다.

```
/cua-vl

사용 예:
- "새 Topic을 시작하고 싶어"
- "Roadmap을 생성해줘"
- "오늘의 학습 계획을 세워줘"
```

### 2. YouTube→MD Skill

YouTube 영상을 구조화된 마크다운 문서로 변환합니다.

```bash
# 스크립트 직접 실행
python md-generator.py "https://www.youtube.com/watch?v=VIDEO_ID" "영상 제목"

# 또는 Claude Code에서
/youtube-to-md
```

**결과물**:
- AI 요약 (한국어)
- 핵심 포인트
- 주요 섹션별 정리
- 5분 간격 타임라인
- 전체 자막 (타임스탬프 포함)

### 3. Video Edit Skill

영상에서 무음 구간과 필러 단어를 자동으로 제거합니다.

```bash
# 무음 구간만 제거
python video-editor.py video.mp4 --remove-silence

# 필러 단어만 제거 (Whisper 필요)
python video-editor.py video.mp4 --remove-fillers --model base

# 모두 제거 (권장)
python video-editor.py video.mp4 --all
```

**결과**:
- 테스트 영상: 3분 34초 → 2분 28초 (30.9% 단축)
- 무음 58개, 필러 12개 자동 제거

---

## 설치

### 필수 요구사항

- Python 3.10+
- FFmpeg (영상 처리용)
- Claude Code Extension

### Python 라이브러리 설치

```bash
# YouTube→MD Skill
pip install youtube-transcript-api anthropic

# Video Edit Skill
pip install pydub ffmpeg-python openai-whisper
```

### FFmpeg 설치

```bash
# Windows
choco install ffmpeg

# Mac
brew install ffmpeg

# Linux
apt install ffmpeg
```

---

## 폴더 구조

```
Claude-Skills/
├── README.md                          # 이 파일
├── CHANGELOG.md                       # 버전 히스토리
├── LICENSE                            # MIT 라이선스
├── topic_info.md                      # Topic 정보
│
├── 01-Claude-Skills-Basics/           # M1: 기본 개념
│   ├── README.md
│   ├── concepts/                      # 개념 문서
│   ├── examples/                      # Hello Skill 예제
│   └── guides/                        # 가이드
│
├── 02-Skill-A-CUA-VL/                 # M2: CUA_VL Skill
│   ├── README.md
│   ├── examples/cua-vl-skill/         # Skill 코드
│   │   └── SKILL.md
│   └── guides/                        # 사용 가이드
│
├── 03-Skill-B-YouTube-MD/             # M3: YouTube→MD Skill
│   ├── README.md
│   ├── examples/
│   │   ├── youtube-transcript-test.py # 자막 추출 테스트
│   │   ├── md-generator.py            # MD 생성 (메인)
│   │   └── youtube-to-md-skill/
│   │       └── SKILL.md
│   └── guides/user-guide.md           # 사용 가이드
│
├── 04-Skill-C-Video-Edit/             # M4: Video Edit Skill
│   ├── README.md
│   ├── examples/
│   │   ├── silence-detection.py       # 무음 감지
│   │   ├── silence-remover.py         # 무음 제거
│   │   ├── filler-detection.py        # 필러 감지
│   │   ├── video-editor.py            # 통합 편집 (메인)
│   │   └── video-edit-skill/
│   │       └── SKILL.md
│   └── outputs/                       # 테스트 결과
│
├── 05-Integration-Deploy/             # M5: 통합 및 배포
│   ├── README.md
│   └── retrospective/                 # 최종 회고
│
├── vl_materials/                      # 학습 자료
│   ├── AI-Memory-360-Tour-Silicon-Valley/  # 변환된 MD 14개
│   └── AI-Memory-360-Tour-Seattle/         # Seattle 행사용
│
├── vl_prompts/                        # 프롬프트 템플릿
├── vl_roadmap/                        # 학습 로드맵
└── vl_worklog/                        # 학습 기록
```

---

## 학습 여정

### 진행 현황

| 모듈 | 기간 | 내용 | 상태 |
|------|------|------|------|
| M1 | Day 1-2 | Claude Skills 기본 개념 | ✅ 완료 |
| M2 | Day 3-4 | CUA_VL Skill 개발 | ✅ 완료 |
| M3 | Day 5-8 | YouTube→MD Skill 개발 | ✅ 완료 |
| M4 | Day 9-12 | Video Edit Skill 개발 | ✅ 완료 |
| M5 | Day 13-14 | 통합, 배포, 회고 | ✅ 완료 |

### 주요 성과

1. **YouTube→MD Skill**
   - AI Memory 360 Tour 14개 영상 → 463KB MD 문서
   - 영상당 2-3분 만에 구조화된 학습 자료 생성
   - 90% 시간 절약 (35-70분 → 2-3분)

2. **Video Edit Skill**
   - 실제 영상 테스트: 3분 34초 → 2분 28초 (30.9% 단축)
   - 무음 58개, 필러 12개 자동 감지 및 제거
   - 파일 크기 32.3% 감소

3. **CUA_VL Skill**
   - Output 중심 학습 방법론 자동화
   - Topic 시작 → Roadmap → Daily 학습 워크플로우

---

## 기술 스택

- **Python**: 스크립트 개발
- **pydub**: 오디오 분석 및 편집
- **FFmpeg**: 영상 처리
- **OpenAI Whisper**: 음성 인식 (필러 단어 감지)
- **youtube-transcript-api**: YouTube 자막 추출
- **Anthropic Claude API**: AI 요약 생성

---

## 기여

이 프로젝트는 CUA_VL 방법론 학습의 결과물입니다.
개선 제안이나 버그 리포트는 Issue로 등록해주세요.

---

## 라이선스

MIT License - 자유롭게 사용, 수정, 배포 가능합니다.

---

## 참조

- [Claude Code 공식 문서](https://docs.anthropic.com/claude/docs)
- [CUA_VL 방법론](./vl_prompts/)
- [학습 로드맵](./vl_roadmap/)

---

**개발 기간**: 2026-01-04 ~ 2026-01-18 (2주)
**방법론**: CUA_VL (Catch Up AI Vibe Learning)
