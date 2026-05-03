# @remotion/transitions — 슬라이드 전환 효과

## 개요

`@remotion/transitions`는 씬 간 전환 효과를 간단하게 구현하는 공식 패키지입니다.
`TransitionSeries`로 기존 `<Series>`/`<Sequence>` 배열을 대체하면 fade, slide, wipe 등의
전환 효과를 몇 줄로 추가할 수 있습니다.

**실제 사용 예**: 이 프로젝트의 Live6/Live7 하이라이트 영상 (`src/live6-highlight/`, `src/live7-highlight/`)

---

## 설치

```bash
npx remotion add @remotion/transitions
```

---

## 기본 구조

```tsx
import { TransitionSeries, linearTiming, springTiming } from '@remotion/transitions';
import { fade } from '@remotion/transitions/fade';
import { slide } from '@remotion/transitions/slide';

export const MyVideo: React.FC = () => (
  <TransitionSeries>
    <TransitionSeries.Sequence durationInFrames={90}>
      <SceneA />
    </TransitionSeries.Sequence>

    <TransitionSeries.Transition
      presentation={fade()}
      timing={linearTiming({ durationInFrames: 18 })}
    />

    <TransitionSeries.Sequence durationInFrames={90}>
      <SceneB />
    </TransitionSeries.Sequence>

    <TransitionSeries.Transition
      presentation={slide({ direction: 'from-right' })}
      timing={springTiming({ config: { damping: 200 }, durationInFrames: 24 })}
    />

    <TransitionSeries.Sequence durationInFrames={90}>
      <SceneC />
    </TransitionSeries.Sequence>
  </TransitionSeries>
);
```

---

## 사용 가능한 전환 타입

| 전환 | import 경로 | 옵션 | 특징 |
|------|-------------|------|------|
| `fade()` | `@remotion/transitions/fade` | — | 크로스페이드, 가장 부드러움 |
| `slide()` | `@remotion/transitions/slide` | `direction` | 슬라이드 밀어내기 |
| `wipe()` | `@remotion/transitions/wipe` | `direction` | 와이프 (커튼 효과) |
| `flip()` | `@remotion/transitions/flip` | `direction` | 3D 플립 |
| `clockWipe()` | `@remotion/transitions/clock-wipe` | `degreeOffset` | 시계 방향 와이프 |

### slide / wipe direction 옵션

```tsx
slide({ direction: 'from-left' })   // 왼쪽에서 오른쪽으로
slide({ direction: 'from-right' })  // 오른쪽에서 왼쪽으로
slide({ direction: 'from-top' })    // 위에서 아래로
slide({ direction: 'from-bottom' }) // 아래에서 위로
```

---

## 타이밍 옵션

### linearTiming — 일정한 속도

```tsx
import { linearTiming } from '@remotion/transitions';

linearTiming({ durationInFrames: 18 }) // 0.6초 (30fps 기준)
```

### springTiming — 물리 기반 (자연스러운 감속)

```tsx
import { springTiming } from '@remotion/transitions';

springTiming({
  config: { damping: 200 },        // 높을수록 빠르게 안정
  durationInFrames: 24,            // 명시적 길이 지정
})
```

> **권장**: 슬라이드/섹션 전환은 `springTiming`, 일반 콘텐츠 전환은 `linearTiming`

---

## Overlay — 타임라인 길이 유지하며 오버레이 추가

`Transition`은 두 씬이 겹치며 총 길이가 줄어들지만,
`Overlay`는 컷 포인트에 효과를 올릴 뿐 길이가 유지됩니다.

```tsx
import { TransitionSeries } from '@remotion/transitions';

<TransitionSeries>
  <TransitionSeries.Sequence durationInFrames={60}>
    <SceneA />
  </TransitionSeries.Sequence>
  <TransitionSeries.Overlay durationInFrames={20}>
    {/* 컷 포인트 중심으로 20프레임 오버레이 */}
    <FlashEffect />
  </TransitionSeries.Overlay>
  <TransitionSeries.Sequence durationInFrames={60}>
    <SceneB />
  </TransitionSeries.Sequence>
</TransitionSeries>
```

---

## 총 길이 계산

`Transition`은 두 씬이 동시 재생되므로 총 길이가 **짧아집니다**:

```
씬 A (90f) + 씬 B (90f) - 전환 (18f) = 162f  ← 총 길이
```

`getDurationInFrames()`로 정확한 전환 길이를 계산할 수 있습니다:

```tsx
const timing = springTiming({ config: { damping: 200 }, durationInFrames: 24 });
const transFrames = timing.getDurationInFrames({ fps: 30 });
```

---

## 실전 패턴: 슬라이드 타입별 전환 차별화

```tsx
// 이 프로젝트 live7-highlight 방식 — 슬라이드 타입에 따라 전환 분기
const isSection = slideData.type === 'section' || slideData.type === 'title';
const transFrames = isSection ? 24 : 18;
const presentation = isSection ? slide({ direction: 'from-right' }) : fade();
const timing = isSection
  ? springTiming({ config: { damping: 200 }, durationInFrames: transFrames })
  : linearTiming({ durationInFrames: transFrames });
```

---

## 주요 규칙

- `Overlay`는 `Transition`이나 다른 `Overlay`에 인접할 수 없음
- `TransitionSeries`의 자식은 절대 위치(`AbsoluteFill`) 기반으로 렌더링됨
- `springTiming`에 `durationInFrames` 생략 시 fps에 따라 길이가 달라짐
