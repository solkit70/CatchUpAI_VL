# M5 - 렌더링 & 내보내기

Remotion CLI를 사용하여 영상을 MP4로 렌더링하고, YouTube 업로드에 최적화된 설정을 학습한 모듈입니다.

## 📖 학습 순서

이 폴더를 처음 여는 분은 아래 순서대로 읽으세요.

| 순서 | 문서 | 설명 |
|------|------|------|
| 1 | [concepts/rendering-basics.md](concepts/rendering-basics.md) | CRF, 비트레이트, 코덱 개념 (품질 vs 파일 크기) |
| 2 | [guides/youtube-render-settings.md](guides/youtube-render-settings.md) | YouTube 최적 렌더링 설정 (8Mbps, H.264) |
| 3 | [examples/render-comparison/comparison-notes.md](examples/render-comparison/comparison-notes.md) | 품질별 렌더링 비교 메모 (실제 테스트 결과) |

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
