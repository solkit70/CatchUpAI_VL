# Lottie 애니메이션 + GIF 임베드

## Lottie — 벡터 애니메이션

### 개요

Lottie는 Adobe After Effects에서 내보낸 JSON 애니메이션 포맷입니다.
정적 이모지/아이콘 대신 Lottie를 쓰면 영상에 생동감이 크게 높아집니다.

**무료 Lottie 파일 소스**: [LottieFiles.com](https://lottiefiles.com)

### 설치

```bash
npx remotion add @remotion/lottie
```

### 기본 사용

```tsx
import { Lottie, LottieAnimationData } from '@remotion/lottie';
import { useState, useEffect } from 'react';
import { cancelRender, continueRender, delayRender, staticFile } from 'remotion';

export const LottieIcon: React.FC<{ src: string }> = ({ src }) => {
  const [handle] = useState(() => delayRender('Loading Lottie'));
  const [animationData, setAnimationData] = useState<LottieAnimationData | null>(null);

  useEffect(() => {
    fetch(staticFile(src))
      .then((r) => r.json())
      .then((json) => {
        setAnimationData(json);
        continueRender(handle);
      })
      .catch((e) => cancelRender(e));
  }, [handle, src]);

  if (!animationData) return null;

  return (
    <Lottie
      animationData={animationData}
      style={{ width: 120, height: 120 }}
    />
  );
};
```

### 파일을 public/에 직접 포함

```tsx
// 빌드 시 번들에 포함 (권장)
import rocketJson from '../public/lottie/rocket.json';

export const RocketIcon: React.FC = () => (
  <Lottie
    animationData={rocketJson}
    style={{ width: 80, height: 80 }}
  />
);
```

### 슬라이드 불릿에 Lottie 아이콘 적용 (실전 패턴)

```tsx
import { AbsoluteFill, Sequence } from 'remotion';
import { Lottie } from '@remotion/lottie';
import checkmarkJson from '../public/lottie/checkmark.json';

const AnimatedBulletItem: React.FC<{ text: string; delay: number }> = ({ text, delay }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const sp = spring({ frame: frame - delay, fps, config: { damping: 14 } });

  return (
    <div style={{
      display: 'flex', alignItems: 'center', gap: 16,
      opacity: sp,
      transform: `translateX(${(1 - sp) * -30}px)`,
    }}>
      <Lottie animationData={checkmarkJson} style={{ width: 48, height: 48 }} />
      <span style={{ fontSize: 36, color: '#202124' }}>{text}</span>
    </div>
  );
};
```

### 스타일 제어

```tsx
<Lottie
  animationData={data}
  style={{
    width: 200,
    height: 200,
    opacity: interpolate(frame, [0, 30], [0, 1]),
    transform: `scale(${spring({ frame, fps })})`,
  }}
/>
```

---

## GIF 임베드 — @remotion/gif

### 개요

`@remotion/gif`는 GIF 파일을 Remotion 영상에 정확하게 임베드합니다.
일반 `<img>` 태그는 렌더링 서버에서 GIF를 재생하지 않으므로 반드시 이 컴포넌트를 사용해야 합니다.

### 설치

```bash
npx remotion add @remotion/gif
```

### 기본 사용

```tsx
import { Gif } from '@remotion/gif';
import { staticFile } from 'remotion';

export const MyComp: React.FC = () => (
  <Gif
    src={staticFile('animations/loading.gif')}
    width={200}
    height={200}
    fit="contain"
  />
);
```

### 원격 GIF

```tsx
<Gif
  src="https://media.giphy.com/media/xyz/giphy.gif"
  width={300}
  height={300}
  fit="cover"
/>
```

### fit 옵션

| 값 | 설명 |
|----|------|
| `fill` | 지정 크기에 꽉 채움 (비율 무시) |
| `contain` | 비율 유지, 여백 생김 |
| `cover` | 비율 유지, 클리핑 |

### GIF 속도 제어

```tsx
<Gif
  src={staticFile('confetti.gif')}
  width={400}
  height={300}
  playbackRate={2.0}  // 2배 빠르게
  loop={false}        // 1회만 재생
/>
```

---

## Lottie vs GIF 선택 기준

| 기준 | Lottie | GIF |
|------|--------|-----|
| 파일 크기 | 매우 작음 (JSON) | 큼 |
| 화질 | 벡터, 무한 확대 | 픽셀, 확대 시 열화 |
| 색상 | 무제한 | 256색 제한 |
| 소스 | LottieFiles, AE | Giphy, Tenor |
| 속도 제어 | 가능 | 가능 |
| **권장 용도** | 아이콘, UI 요소 | 밈, 반응, 이모지 GIF |

---

## 실전 활용 아이디어

| 상황 | 추천 |
|------|------|
| 불릿 체크마크 아이콘 | Lottie checkmark |
| 로딩/처리 중 표시 | Lottie spinner |
| 섹션 전환 이펙트 | Lottie confetti |
| 밈/유머 요소 | GIF |
| 인포그래픽 아이콘 | Lottie (벡터) |
| 반응/감정 표현 | GIF (자연스러움) |
