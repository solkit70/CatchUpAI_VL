# M5 - 렌더링 & 내보내기

Remotion CLI를 사용하여 영상을 MP4로 렌더링하고, YouTube 업로드에 최적화된 설정을 학습한 모듈입니다.

## 📖 학습 순서

이 폴더를 처음 여는 분은 아래 순서대로 읽으세요.

| 순서 | 문서 | 설명 |
|------|------|------|
| 1 | [concepts/rendering-basics.md](concepts/rendering-basics.md) | CRF, 비트레이트, 코덱 개념 (품질 vs 파일 크기) |
| 2 | [guides/youtube-render-settings.md](guides/youtube-render-settings.md) | YouTube 최적 렌더링 설정 (8Mbps, H.264) |
| 3 | [examples/render-comparison/comparison-notes.md](examples/render-comparison/comparison-notes.md) | 품질별 렌더링 비교 메모 (실제 테스트 결과) |
| 4 | [concepts/studio-features.md](concepts/studio-features.md) | Studio 활용 — 파형 시각화, 단축키, Props 패널 ✨NEW |
| 5 | [concepts/html-in-canvas.md](concepts/html-in-canvas.md) | HTML-in-Canvas 실험적 렌더링 모드 ✨NEW (4.0.447+) |

**이전 모듈**: [04-Skills](../04-Skills/) | **다음 모듈**: [06-YouTube-Project](../06-YouTube-Project/)

---

## 학습 요약

| 항목 | 내용 |
|------|------|
| 학습일 | 2026-02-10 |
| 소요 시간 | 약 1.5시간 |
| 렌더링 영상 | 9개 파일 (품질 비교 포함) |
| 핵심 기술 | CLI render, CRF, 비트레이트, H.264 코덱 |

## 렌더링 결과

### 기본 렌더링
| Composition | 길이 | 파일 크기 |
|-------------|------|----------|
| HelloWorld | 7초 | 2.2 MB |
| ChannelIntro | 5초 | 2.2 MB |
| ExplanationScene | 11초 | 1.1 MB |

### 품질 비교 (ChannelIntro 기준)
| 설정 | 파일 크기 | 품질 |
|------|----------|------|
| 기본 (CRF 미지정) | 2.2 MB | 보통 |
| CRF 18 (고품질) | 2.2 MB | 높음 |
| CRF 28 (저품질) | 949 KB | 낮음 |
| **비트레이트 8Mbps** | **4.8 MB** | **YouTube 최적** |

### YouTube 최적 렌더링
| Composition | 파일 크기 |
|-------------|----------|
| ChannelIntro_youtube.mp4 | 4.8 MB |
| ExplanationScene_youtube.mp4 | 4.2 MB |
| SkillsHelloWorld_youtube.mp4 | 2.9 MB |

## 핵심 명령어

```bash
# 기본 렌더링
npx remotion render <CompositionId> out/<filename>.mp4

# YouTube 최적 렌더링
npx remotion render <CompositionId> out/<filename>.mp4 --video-bitrate="8M" --codec=h264

# CRF로 품질 조절 (0=무손실, 51=최저)
npx remotion render <CompositionId> out/<filename>.mp4 --crf=18

# 오디오만 렌더링 (배경음악 추출 등)
npx remotion render <CompositionId> out/<filename>.mp3

# 특정 프레임 PNG로 추출 (썸네일 생성)
npx remotion still <CompositionId> --frame=0 out/thumbnail.png
```

## ✨ 4.0.452 업그레이드 신규 CLI 옵션

```bash
# 오디오 출력 샘플레이트 지정 (기본값: 48000Hz)
npx remotion render <CompositionId> out/video.mp4 --sample-rate=44100

# HTML-in-Canvas 실험 모드 활성화 (Chrome Canary 필요)
npx remotion render <CompositionId> out/video.mp4 --allow-html-in-canvas

# 기본 출력 파일명을 Props로 지정 (calculateMetadata의 defaultOutName 활용)
npx remotion render <CompositionId>
```

### renderStillOnWeb() 반환값 변경 (Breaking Change)

4.0.447부터 `renderStillOnWeb()`의 반환 포맷이 변경됐습니다:

```tsx
// 이전 (4.0.447 미만)
const result = await renderStillOnWeb({ ... });
// result: ArrayBuffer

// 신규 (4.0.447+)
const result = await renderStillOnWeb({ ... });
// result: { canvas: HTMLCanvasElement, blob: Blob, url: string }

// 사용 예
const { url } = await renderStillOnWeb({ ... });
document.getElementById('preview').src = url;
```

> **이 프로젝트는 CLI 렌더링만 사용하므로 영향 없음.**

## ✨ 추가된 내용 (2026-04 업데이트)

### TTS 오디오 + 영상 동기화 워크플로우

현재 프로젝트에서 사용하는 TTS 통합 방식:

```
1. gen_audio.py 실행 → OpenAI TTS API로 MP3 생성 + ffmpeg 1.03x 가속
2. ffprobe로 오디오 길이 측정 → durations.json 출력
3. data.ts의 SLIDE_DURATIONS에 측정값 + 1.2s 패딩 입력
4. 각 슬라이드 컴포넌트에서 <Sequence from={AUDIO_HEAD_PAD_FRAMES}><Audio /></Sequence>
5. npx remotion render 로 최종 MP4 생성
```

→ 상세 가이드: [07-Rich-Media/concepts/audio-tts-workflow.md](../07-Rich-Media/concepts/audio-tts-workflow.md)

### Still 렌더링 — 썸네일 생성

```bash
npx remotion still Live7Highlight --frame=0 out/live7-thumbnail.png
```

Props를 JSON으로 전달:
```bash
npx remotion still TitleCard out/thumbnail.png \
  --props='{"title":"AI in Action","subtitle":"Live #7 하이라이트"}'
```

### 렌더링 성능 최적화

| 옵션 | 효과 | 권장 상황 |
|------|------|-----------|
| `--concurrency=4` | 병렬 렌더링 코어 수 지정 | 멀티코어 시스템 |
| `--image-format=jpeg` | PNG 대신 JPEG 중간 프레임 | 파일 크기 중요할 때 |
| `--every-nth-frame=2` | 짝수 프레임만 렌더링 | 빠른 프리뷰 확인용 |
| `--frames=0-30` | 특정 구간만 렌더링 | 부분 테스트 |

```bash
# 실전 YouTube 렌더링 (최적 설정)
npx remotion render Live7Highlight out/live7-highlight.mp4 \
  --video-bitrate="8M" \
  --codec=h264 \
  --concurrency=4
```

## 폴더 구조

```
05-Rendering/
├── README.md                     # 이 파일
├── concepts/
│   └── rendering-basics.md       # CRF, 비트레이트, 코덱 개념
├── examples/
│   └── render-comparison/        # 품질별 렌더링 비교 메모
└── guides/
    └── youtube-render-settings.md # YouTube 최적 렌더링 설정
```

## 참조

- [렌더링 가이드](https://www.remotion.dev/docs/render)
- [CLI render 명령](https://www.remotion.dev/docs/cli/render)
- 렌더링 출력 폴더: `my-first-video/out/`
