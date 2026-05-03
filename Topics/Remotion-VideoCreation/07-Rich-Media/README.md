# M7 - Rich Media (오디오·자막·미디어 임베드)

M1~M6에서 다루지 않은 **미디어 풍부화** 기능들을 정리한 모듈입니다.
유튜브 채널 수준의 영상 품질을 위한 실전 기법들을 다룹니다.

## 📖 학습 순서

| 순서 | 문서 | 설명 |
|------|------|------|
| 1 | [concepts/audio-tts-workflow.md](concepts/audio-tts-workflow.md) | TTS 오디오 생성 + Remotion 동기화 워크플로우 |
| 2 | [concepts/captions.md](concepts/captions.md) | 자동 자막 — @remotion/captions + Whisper |
| 3 | [concepts/audio-visualization.md](concepts/audio-visualization.md) | 오디오 시각화 — 스펙트럼·웨이브폼·베이스 리액티브 |
| 4 | [concepts/lottie-gif.md](concepts/lottie-gif.md) | Lottie 애니메이션 + GIF 임베드 |
| 5 | [concepts/video-embedding.md](concepts/video-embedding.md) | 영상 클립 임베드 — OffthreadVideo, 트리밍 |

**이전 모듈**: [06-YouTube-Project](../06-YouTube-Project/)

---

## 이 모듈에서 다루는 패키지

| 패키지 | 기능 | 설치 |
|--------|------|------|
| `@remotion/media` | `<Audio>` 컴포넌트 (볼륨, 루프, 피치) | `npx remotion add @remotion/media` |
| `@remotion/media-utils` | 오디오 시각화, 길이 측정 | `npx remotion add @remotion/media-utils` |
| `@remotion/captions` | TikTok 스타일 자막, 워드 하이라이트 | `npx remotion add @remotion/captions` |
| `@remotion/install-whisper-cpp` | 로컬 Whisper 설치 (자막 자동 생성) | `npx remotion add @remotion/install-whisper-cpp` |
| `@remotion/lottie` | Lottie JSON 애니메이션 | `npx remotion add @remotion/lottie` |
| `@remotion/gif` | GIF 임베드 | `npx remotion add @remotion/gif` |

---

## 핵심 인사이트

1. **TTS 워크플로우가 핵심**: OpenAI TTS → ffmpeg 가속 → 길이 측정 → 슬라이드 동기화 패턴이 이 프로젝트의 핵심 패턴
2. **자막은 접근성 + SEO**: `@remotion/captions`로 Whisper 자막을 자동 생성하면 YouTube 자막 품질이 크게 향상
3. **Lottie로 아이콘 동작**: 정적 이모지 대신 Lottie 아이콘을 쓰면 영상이 훨씬 생동감 있어짐
4. **오디오 시각화**: 팟캐스트 클립, 음악 리뷰 콘텐츠에 필수
