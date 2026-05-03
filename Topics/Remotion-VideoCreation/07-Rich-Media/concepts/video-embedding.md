# 영상 클립 임베드 — OffthreadVideo + 트리밍

## 개요

Remotion에서 기존 영상 파일을 컴포지션에 임베드할 때는
`<Video>` 또는 `<OffthreadVideo>`를 사용합니다.

**`<Video>` vs `<OffthreadVideo>` 차이:**

| | `<Video>` | `<OffthreadVideo>` |
|-|-----------|-------------------|
| 렌더링 방식 | HTML `<video>` 태그 | 프레임별 추출 (ffmpeg) |
| Studio 미리보기 | 실시간 재생 | 느릴 수 있음 |
| 렌더링 정확도 | 낮을 수 있음 | **높음 (권장)** |
| 투명 영상 (webm) | 지원 | 지원 |
| `from` / `durationInFrames` | ✅ 4.0.452+ | ✅ 지원 |
| `objectFit` prop | ✅ 4.0.452+ 추가 | CSS style로 지정 |

> **렌더링 시 품질이 중요하면 `OffthreadVideo`를 사용하세요.**

### ✨ 4.0.452 신규 Props — `from`, `durationInFrames`, `objectFit`

```tsx
import { Video, staticFile } from 'remotion';
import { useVideoConfig } from 'remotion';

const { fps } = useVideoConfig();

// from: Sequence 없이 시작 시점 지정
// durationInFrames: Sequence 없이 재생 구간 지정
// objectFit: CSS object-fit을 prop으로 직접 지정
<Video
  src={staticFile('clips/interview.mp4')}
  from={5 * fps}             // 5초 뒤에 등장
  durationInFrames={10 * fps} // 10초만 재생
  objectFit="cover"           // cover / contain / fill
/>
```

> `from` + `durationInFrames`는 `<Sequence>`를 대체하는 간편 표기법입니다.
> 기존 코드에서 `<Sequence from={...}><Video .../></Sequence>` 패턴도 계속 사용 가능합니다.

---

## 기본 사용

```tsx
import { OffthreadVideo, staticFile } from 'remotion';

export const VideoSlide: React.FC = () => (
  <OffthreadVideo
    src={staticFile('clips/intro.mp4')}
    style={{ width: '100%', height: '100%', objectFit: 'cover' }}
  />
);
```

원격 URL도 지원:
```tsx
<OffthreadVideo src="https://remotion.media/video.mp4" />
```

---

## 트리밍 — 구간 잘라 재생

```tsx
import { OffthreadVideo, staticFile, useVideoConfig } from 'remotion';

export const ClipPlayer: React.FC = () => {
  const { fps } = useVideoConfig();

  return (
    <OffthreadVideo
      src={staticFile('clips/raw-footage.mp4')}
      startFrom={30 * fps}    // 30초부터 시작
      endAt={60 * fps}        // 60초에서 종료
    />
  );
};
```

트리밍 후 실제 재생 구간: `[startFrom, endAt]` 프레임 범위.
Composition의 길이와 독립적으로 설정 가능.

---

## 볼륨 + 음소거

```tsx
<OffthreadVideo
  src={staticFile('clips/interview.mp4')}
  volume={0.8}          // 80% 볼륨
/>

<OffthreadVideo
  src={staticFile('clips/broll.mp4')}
  muted                 // 영상 음소거 (BGM만 들리게)
/>
```

---

## 영상 위에 오버레이 합성

```tsx
import { AbsoluteFill, OffthreadVideo, staticFile } from 'remotion';

export const VideoWithOverlay: React.FC = () => (
  <AbsoluteFill>
    {/* 배경 영상 */}
    <OffthreadVideo
      src={staticFile('clips/background.mp4')}
      style={{ width: '100%', height: '100%', objectFit: 'cover' }}
      muted
    />

    {/* 상단 제목 오버레이 */}
    <AbsoluteFill style={{
      justifyContent: 'flex-start',
      padding: 60,
      background: 'linear-gradient(to bottom, rgba(0,0,0,0.6) 0%, transparent 40%)',
    }}>
      <h1 style={{ color: 'white', fontSize: 64, fontWeight: 900 }}>
        AI in Action Live #7
      </h1>
    </AbsoluteFill>
  </AbsoluteFill>
);
```

---

## 영상 길이에 맞는 Composition 자동 설정

```tsx
import { CalculateMetadataFunction, OffthreadVideo, staticFile } from 'remotion';

type Props = { videoSrc: string };

export const calculateMetadata: CalculateMetadataFunction<Props> = async ({ props }) => {
  // getVideoMetadata는 @remotion/media-utils 함수
  const { durationInSeconds, width, height } = await getVideoMetadata(props.videoSrc);

  return {
    durationInFrames: Math.ceil(durationInSeconds * 30),
    width,
    height,
  };
};
```

---

## 투명 영상 (Alpha Channel) — WebM

배경이 투명한 영상(예: 캐릭터 애니메이션)을 합성할 때:

```tsx
import { OffthreadVideo, staticFile, AbsoluteFill } from 'remotion';

export const CharacterOverlay: React.FC = () => (
  <AbsoluteFill>
    {/* 배경 슬라이드 */}
    <BulletSlide data={slideData} durationInFrames={300} />

    {/* 투명 WebM — AbsoluteFill 위에 올라감 */}
    <OffthreadVideo
      src={staticFile('characters/presenter.webm')}
      style={{
        position: 'absolute',
        bottom: 0,
        right: 80,
        height: 400,
      }}
    />
  </AbsoluteFill>
);
```

---

## 썸네일 이미지로 표시 (VideoGrid 패턴)

실제 영상 대신 썸네일 이미지를 그리드로 배치하는 패턴
(이 프로젝트 Live7 슬라이드 2에서 사용):

```tsx
import { Img, staticFile } from 'remotion';

const ThumbnailGrid: React.FC<{ items: VideoGridItem[] }> = ({ items }) => (
  <div style={{
    display: 'grid',
    gridTemplateColumns: 'repeat(4, 1fr)',
    gap: 14,
  }}>
    {items.map((item, i) => (
      <div key={i} style={{ borderRadius: 12, overflow: 'hidden' }}>
        <Img
          src={staticFile(item.thumbnail)}
          style={{ width: '100%', height: 'auto' }}
        />
      </div>
    ))}
  </div>
);
```

> `<Img>`는 `<img>` 대신 사용 — 렌더링 전 이미지 로딩을 자동으로 대기.

---

## 실전 활용 아이디어

| 콘텐츠 | 패턴 |
|--------|------|
| 라이브 방송 하이라이트 리캡 | 영상 클립 트리밍 + 자막 오버레이 |
| 유튜브 영상 쇼케이스 | 썸네일 그리드 (VideoGridSlide) |
| 제품 데모 | OffthreadVideo + 설명 텍스트 오버레이 |
| 브이로그 편집 | 여러 클립 TransitionSeries로 연결 |
| 화면 녹화 튜토리얼 | OffthreadVideo + 하이라이트 박스 |
