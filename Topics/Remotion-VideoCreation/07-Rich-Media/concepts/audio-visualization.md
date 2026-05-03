# 오디오 시각화 — @remotion/media-utils

## 개요

`@remotion/media-utils`는 오디오 파일의 주파수·파형 데이터를 실시간으로 분석하여
Remotion 영상에 시각화할 수 있게 합니다.

팟캐스트 클립, 음악 리뷰, 채널 인트로 BGM 시각화 등에 활용됩니다.

---

## 설치

```bash
npx remotion add @remotion/media-utils
```

---

## 1. 스펙트럼 바 (Spectrum Bars)

주파수 데이터로 이퀄라이저 스타일의 바 차트를 만듭니다.

```tsx
import { useWindowedAudioData, visualizeAudio } from '@remotion/media-utils';
import { staticFile, useCurrentFrame, useVideoConfig, AbsoluteFill } from 'remotion';

export const SpectrumBars: React.FC<{ src: string }> = ({ src }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const { audioData, dataOffsetInSeconds } = useWindowedAudioData({
    src: staticFile(src),
    frame,
    fps,
    windowInSeconds: 30,
  });

  if (!audioData) return null;

  const frequencies = visualizeAudio({
    fps, frame, audioData,
    numberOfSamples: 64,       // 32, 64, 128, 256, 512 (2의 거듭제곱)
    optimizeFor: 'speed',
    dataOffsetInSeconds,
  });

  return (
    <div style={{
      display: 'flex',
      alignItems: 'flex-end',
      height: 120,
      gap: 2,
      padding: '0 40px',
    }}>
      {frequencies.map((v, i) => (
        <div
          key={i}
          style={{
            flex: 1,
            height: `${Math.max(4, v * 100)}%`,
            background: `hsl(${220 + v * 60}, 80%, 60%)`,  // 값에 따라 색상 변화
            borderRadius: '2px 2px 0 0',
          }}
        />
      ))}
    </div>
  );
};
```

**파라미터 가이드:**
- `numberOfSamples`: 바 개수 (2의 거듭제곱, 64~256 권장)
- 배열 왼쪽 = 저음역(베이스), 오른쪽 = 고음역
- 값 범위: 0~1

---

## 2. 웨이브폼 (Oscilloscope)

음성/팟캐스트 파형을 SVG 경로로 표시합니다.

```tsx
import {
  createSmoothSvgPath,
  useWindowedAudioData,
  visualizeAudioWaveform,
} from '@remotion/media-utils';
import { staticFile, useCurrentFrame, useVideoConfig } from 'remotion';

export const Waveform: React.FC<{ src: string }> = ({ src }) => {
  const frame = useCurrentFrame();
  const { fps, width } = useVideoConfig();
  const HEIGHT = 80;

  const { audioData, dataOffsetInSeconds } = useWindowedAudioData({
    src: staticFile(src),
    frame, fps,
    windowInSeconds: 30,
  });

  if (!audioData) return null;

  const waveform = visualizeAudioWaveform({
    fps, frame, audioData,
    numberOfSamples: 128,
    windowInSeconds: 0.5,     // 현재 시점 기준 0.5초 구간
    dataOffsetInSeconds,
  });

  const path = createSmoothSvgPath({
    points: waveform.map((y, i) => ({
      x: (i / (waveform.length - 1)) * width,
      y: HEIGHT / 2 + (y * HEIGHT) / 2,
    })),
  });

  return (
    <svg width={width} height={HEIGHT}>
      <path d={path} fill="none" stroke="#1a73e8" strokeWidth={2} />
    </svg>
  );
};
```

---

## 3. 베이스 리액티브 효과 (Bass-Reactive)

저음역(베이스)에 반응하는 배경 펄스·글로우 효과.

```tsx
import { visualizeAudio, useWindowedAudioData } from '@remotion/media-utils';
import { staticFile, useCurrentFrame, useVideoConfig, interpolate } from 'remotion';

export const BassReactiveBg: React.FC<{ src: string }> = ({ src }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const { audioData, dataOffsetInSeconds } = useWindowedAudioData({
    src: staticFile(src),
    frame, fps,
    windowInSeconds: 30,
  });

  if (!audioData) return null;

  const frequencies = visualizeAudio({
    fps, frame, audioData,
    numberOfSamples: 64,
    optimizeFor: 'speed',
    dataOffsetInSeconds,
  });

  // 저음역 (하위 25%) 평균값 = 베이스 강도
  const bassFreqs = frequencies.slice(0, 16);
  const bassIntensity = bassFreqs.reduce((s, v) => s + v, 0) / bassFreqs.length;

  const scale = 1 + bassIntensity * 0.08;
  const glowRadius = 20 + bassIntensity * 60;
  const glowOpacity = 0.3 + bassIntensity * 0.5;

  return (
    <div style={{
      width: '100%', height: '100%',
      background: `radial-gradient(circle, rgba(26,115,232,${glowOpacity}) 0%, transparent 70%)`,
      transform: `scale(${scale})`,
    }} />
  );
};
```

---

## 4. 볼륨 기반 단순 시각화

주파수 분석 없이 전체 볼륨 크기만 필요할 때:

```tsx
import { getWaveformPortion } from '@remotion/media-utils';
import { useCurrentFrame, useVideoConfig } from 'remotion';

export const VolumeBar: React.FC<{ audioData: AudioData }> = ({ audioData }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const waveform = getWaveformPortion({
    audioData,
    startTimeInSeconds: frame / fps,
    durationInSeconds: 0.1,
    numberOfSamples: 1,
  });

  const volume = waveform[0]?.amplitude ?? 0;

  return (
    <div style={{
      width: `${volume * 100}%`,
      height: 8,
      background: '#1a73e8',
      borderRadius: 4,
    }} />
  );
};
```

---

## 주의사항

1. **child 컴포넌트에 frame 전달**: `<Sequence>` 안에서 `useCurrentFrame()`은 로컬 프레임을 반환하므로, 부모에서 `frame`을 받아서 `visualizeAudio()`에 전달해야 연속성 유지
2. **numberOfSamples**: 반드시 2의 거듭제곱 (32, 64, 128, 256, 512, 1024)
3. **로그 스케일**: 저음역이 자연적으로 값이 크게 나오므로 시각적 균형을 위해 로그 변환 권장:

```tsx
const scaled = frequencies.map((v) => {
  const db = 20 * Math.log10(Math.max(v, 1e-10));
  return Math.max(0, (db - (-80)) / ((-10) - (-80)));
});
```

---

## 활용 아이디어

| 콘텐츠 유형 | 추천 시각화 |
|------------|------------|
| 팟캐스트/인터뷰 클립 | 웨이브폼 (화자 식별) |
| 음악 리뷰/쇼케이스 | 스펙트럼 바 |
| 채널 인트로 BGM | 베이스 리액티브 배경 |
| 라이브 하이라이트 | 볼륨 인디케이터 |
