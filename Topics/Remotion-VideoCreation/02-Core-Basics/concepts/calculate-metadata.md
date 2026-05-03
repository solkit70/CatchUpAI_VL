# calculateMetadata — 동적 Composition 설정

## 개요

`calculateMetadata`는 Composition이 렌더링되기 **전에** 비동기적으로 실행되는 함수로,
영상 길이·해상도·Props를 런타임에 동적으로 결정할 수 있게 합니다.

**언제 쓰나?**
- 오디오 파일 길이에 맞춰 영상 길이를 자동 계산할 때
- 외부 API에서 데이터를 받아 Props를 채울 때
- 영상 파일의 해상도를 자동으로 맞출 때

---

## 기본 구조

```tsx
import { Composition, CalculateMetadataFunction } from 'remotion';

type MyProps = { audioSrc: string };

const calculateMetadata: CalculateMetadataFunction<MyProps> = async ({ props }) => {
  // 여기서 반환한 값이 Composition 설정을 덮어씀
  return {
    durationInFrames: 300,
    fps: 30,
    width: 1920,
    height: 1080,
    props,            // 변환된 props도 전달 가능
  };
};

export const RemotionRoot: React.FC = () => (
  <Composition
    id="MyComp"
    component={MyComponent}
    durationInFrames={300}   // fallback 기본값
    fps={30}
    width={1920}
    height={1080}
    calculateMetadata={calculateMetadata}
  />
);
```

---

## 패턴 1: 오디오 길이로 자동 Composition 길이 결정

TTS/나레이션 오디오를 기반으로 슬라이드 영상 길이를 동적으로 결정할 때 사용합니다.

```tsx
import { getAudioDurationInSeconds } from '@remotion/media-utils';
import { staticFile, CalculateMetadataFunction } from 'remotion';

type Props = { audioSrc: string };

export const calculateMetadata: CalculateMetadataFunction<Props> = async ({ props }) => {
  const fps = 30;
  const durationInSeconds = await getAudioDurationInSeconds(staticFile(props.audioSrc));

  return {
    durationInFrames: Math.ceil(durationInSeconds * fps) + 36, // +1.2s 여유
    fps,
  };
};
```

> **현재 프로젝트 방식**: `gen_audio.py`로 오디오 길이를 사전에 측정하여 `data.ts`에 직접 하드코딩.
> calculateMetadata를 쓰면 오디오 파일만 교체해도 자동으로 길이가 맞춰짐.

---

## 패턴 2: 외부 API에서 Props 채우기

```tsx
type Props = { dataUrl: string; items: string[] };

const calculateMetadata: CalculateMetadataFunction<Props> = async ({ props, abortSignal }) => {
  const response = await fetch(props.dataUrl, { signal: abortSignal });
  const data = await response.json();

  return {
    props: {
      ...props,
      items: data.items,
    },
    durationInFrames: data.items.length * 90, // 항목당 3초
  };
};
```

> `abortSignal`: Studio에서 Props가 바뀔 때 이전 요청을 자동 취소.

---

## 패턴 3: 여러 비디오/오디오 합산

```tsx
type Props = { clips: { src: string }[] };

const calculateMetadata: CalculateMetadataFunction<Props> = async ({ props }) => {
  const fps = 30;
  const durations = await Promise.all(
    props.clips.map((c) => getAudioDurationInSeconds(c.src))
  );
  const total = durations.reduce((s, d) => s + d, 0);

  return { durationInFrames: Math.ceil(total * fps), fps };
};
```

---

## 반환 가능한 필드

| 필드 | 타입 | 설명 |
|------|------|------|
| `durationInFrames` | number | 영상 총 프레임 수 |
| `fps` | number | 초당 프레임 |
| `width` | number | 영상 너비 (px) |
| `height` | number | 영상 높이 (px) |
| `props` | Props | 변환된 props (컴포넌트에 전달됨) |
| `defaultOutName` | string | 기본 출력 파일명 |
| `defaultCodec` | string | 기본 코덱 |

모든 필드는 선택적 — 반환하지 않으면 `<Composition>`의 설정값을 유지.

---

## useDelayRender — 비동기 렌더링 대기

컴포넌트 내부에서 데이터 로딩이 끝날 때까지 렌더링을 일시 중지합니다.

```tsx
import { useState, useEffect, useCallback } from 'react';
import { useDelayRender, continueRender, cancelRender } from 'remotion';

export const MyComponent: React.FC = () => {
  const [handle] = useState(() => useDelayRender('Loading data'));
  const [data, setData] = useState<any>(null);

  const load = useCallback(async () => {
    try {
      const res = await fetch('https://api.example.com/data');
      setData(await res.json());
      continueRender(handle);
    } catch (e) {
      cancelRender(e);
    }
  }, [handle]);

  useEffect(() => { load(); }, [load]);

  if (!data) return null;
  return <div>{data.title}</div>;
};
```

> `calculateMetadata`가 주로 Props 변환에 쓰인다면, `useDelayRender`는 컴포넌트 내부 데이터 로딩에 사용합니다.
