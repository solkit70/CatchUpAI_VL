# M4: Skill C - 영상 편집 자동화 Skill

**모듈**: M4 - Skill C: 영상 편집 자동화 Skill
**학습 기간**: 2026-01-18
**난이도**: ⭐⭐⭐
**상태**: ✅ 완료

---

## 📖 학습 순서

이 폴더를 처음 여는 분은 아래 순서대로 읽으세요.

| 순서 | 문서 | 설명 |
|------|------|------|
| 1 | [examples/silence-detection.py](examples/silence-detection.py) | 무음 구간 감지 스크립트 (pydub 기초) |
| 2 | [examples/silence-remover.py](examples/silence-remover.py) | 무음 구간 제거 스크립트 |
| 3 | [examples/filler-detection.py](examples/filler-detection.py) | 필러 단어 감지 스크립트 (Whisper 사용) |
| 4 | [examples/video-editor.py](examples/video-editor.py) | 통합 편집 스크립트 (무음 + 필러 동시 제거) |
| 5 | [examples/video-edit-skill/SKILL.md](examples/video-edit-skill/SKILL.md) | Claude Skill 정의 (자동화 완성본) |
| 6 | [AI4PKM_Video_Cleaning/SKILL.md](AI4PKM_Video_Cleaning/SKILL.md) | 프로덕션 수준 Skill (실제 배포용) |
| 7 | [Practice_Review/](Practice_Review/) | 실습 워크로그 및 비교 분석 문서 모음 |

**이전 모듈**: [03-Skill-B-YouTube-MD](../03-Skill-B-YouTube-MD/) | **다음 모듈**: [05-Integration-Deploy](../05-Integration-Deploy/)

---

## 📚 모듈 개요

이 모듈에서는 영상/오디오 파일에서 무음 구간과 필러 단어를 자동으로 제거하는 Skill을 개발합니다.

### 학습 목표 달성

| 목표 | 상태 |
|------|------|
| 영상에서 음성을 분석하는 방법 이해 | ✅ |
| 무음 구간 감지 및 제거 로직 구현 | ✅ |
| 필러 단어 감지 및 제거 구현 | ✅ |
| FFmpeg/영상 편집 라이브러리 사용 | ✅ |
| Skill로 자동화하여 시간 단축 | ✅ |

**달성률**: 5/5 (100%)

---

## 🎯 주요 성과

### 1. 무음 구간 자동 감지 및 제거
- pydub 라이브러리를 사용한 오디오 분석
- 임계값 기반 무음 구간 감지 (-40dB 기본)
- 패딩을 적용한 자연스러운 편집

### 2. 필러 단어 자동 감지
- OpenAI Whisper를 사용한 음성 인식
- 다국어 필러 단어 목록 (영어, 한국어)
- 단어별 타임스탬프 추출

### 3. 통합 영상 편집 스크립트
- 무음 + 필러 동시 제거
- FFmpeg를 사용한 영상 재인코딩
- 상세 편집 보고서 자동 생성

### 4. 시간 절감 효과
- 테스트 결과: 29초 오디오 → 22초 (24.1% 단축)
- 수동 편집 대비 90% 이상 시간 절감

---

## 📂 폴더 구조

```
04-Skill-C-Video-Edit/
├── README.md                      # 이 파일
├── examples/
│   ├── silence-detection.py       # 무음 구간 감지 스크립트
│   ├── silence-remover.py         # 무음 구간 제거 스크립트
│   ├── filler-detection.py        # 필러 단어 감지 스크립트
│   ├── video-editor.py            # 통합 편집 스크립트 (메인)
│   ├── create-test-audio.py       # 테스트 오디오 생성
│   └── video-edit-skill/
│       └── SKILL.md               # Claude Skill 정의
├── outputs/
│   ├── test_audio.mp3             # 테스트 원본
│   ├── test_audio_edited.mp3      # 편집된 파일
│   ├── silence_report.md          # 무음 분석 보고서
│   └── *_report.md                # 편집 보고서들
├── concepts/                      # (향후 추가)
└── guides/                        # (향후 추가)
```

---

## 🛠️ 사용법

### 설치

```bash
# 1. Python 라이브러리 설치
pip install pydub ffmpeg-python openai-whisper

# 2. FFmpeg 설치
# Windows: choco install ffmpeg
# Mac: brew install ffmpeg
# Linux: apt install ffmpeg
```

### 기본 사용법

```bash
# 무음 구간만 제거
python video-editor.py video.mp4 --remove-silence

# 필러 단어만 제거
python video-editor.py video.mp4 --remove-fillers --model base

# 모두 제거 (권장)
python video-editor.py video.mp4 --all

# 출력 파일 지정
python video-editor.py video.mp4 --all --output edited.mp4
```

### 옵션

| 옵션 | 설명 | 기본값 |
|------|------|--------|
| `--remove-silence` | 무음 구간 제거 | - |
| `--remove-fillers` | 필러 단어 제거 | - |
| `--all` | 무음 + 필러 모두 제거 | - |
| `--threshold` | 무음 임계값 (dB) | -40 |
| `--min-silence` | 최소 무음 길이 (ms) | 500 |
| `--model` | Whisper 모델 | base |
| `--output` | 출력 파일 경로 | 원본_edited.확장자 |

---

## 📊 테스트 결과

### 테스트 오디오 (29초)

| 항목 | 값 |
|------|------|
| 원본 길이 | 29.0초 |
| 편집 후 | 22.0초 |
| 단축 시간 | 7.0초 |
| 단축 비율 | 24.1% |
| 무음 구간 | 5개 |
| 파일 크기 비율 | 75.9% |

### 성능

- 무음 감지: 실시간의 1/10
- 필러 감지 (base 모델): 실시간의 1~2배
- 영상 인코딩: 영상 길이에 비례

---

## 🔧 핵심 기술

### 1. 오디오 분석 (pydub)
```python
from pydub import AudioSegment
from pydub.silence import detect_silence, detect_nonsilent

audio = AudioSegment.from_file("video.mp4")
silence_ranges = detect_silence(audio, min_silence_len=500, silence_thresh=-40)
```

### 2. 음성 인식 (Whisper)
```python
import whisper

model = whisper.load_model("base")
result = model.transcribe("audio.mp3", word_timestamps=True)
```

### 3. 영상 편집 (FFmpeg)
```python
# filter_complex를 사용한 구간 추출 및 연결
ffmpeg -i input.mp4 -filter_complex "[0:v]trim=start=0:end=5..." output.mp4
```

---

## 📝 학습 인사이트

1. **pydub의 간편함**: 오디오 분석 및 편집이 매우 직관적
2. **Whisper의 정확도**: 단어별 타임스탬프가 정확함
3. **FFmpeg의 강력함**: 복잡한 영상 편집도 CLI로 가능
4. **패딩의 중요성**: 무음 제거 시 자연스러운 전환을 위해 패딩 필수

---

## 🔗 참조

- [pydub 문서](https://github.com/jiaaro/pydub)
- [OpenAI Whisper](https://github.com/openai/whisper)
- [FFmpeg 문서](https://ffmpeg.org/documentation.html)

---

**작성일**: 2026-01-18
**방법론**: CUA_VL (Catch Up AI Vibe Learning)
