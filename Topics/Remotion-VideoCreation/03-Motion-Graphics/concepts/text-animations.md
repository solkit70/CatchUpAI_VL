# 텍스트 애니메이션 패턴

## 1. 타이프라이터 효과 (Typewriter)

문자열을 프레임 단위로 잘라 타이핑되는 효과를 만듭니다.

```tsx
import { useCurrentFrame, useVideoConfig } from 'remotion';

const CHARS_PER_SECOND = 20;

export const Typewriter: React.FC<{ text: string }> = ({ text }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // 현재 프레임에서 보여줄 문자 수 계산 (문자열 슬라이싱)
  const visibleChars = Math.min(
    Math.ceil((frame / fps) * CHARS_PER_SECOND),
    text.length,
  );

  return (
    <div style={{ fontSize: 60, fontFamily: 'sans-serif', color: 'white' }}>
      {text.slice(0, visibleChars)}
      {/* 커서 깜빡임 */}
      {visibleChars < text.length && (
        <span style={{ opacity: frame % 15 < 8 ? 1 : 0 }}>|</span>
      )}
    </div>
  );
};
```

> **규칙**: 항상 `string.slice()`를 사용할 것. 글자별 opacity 방식은 피한다.

---

## 2. 단어별 순차 등장 (Word Stagger)

각 단어를 약간의 딜레이를 두고 순차적으로 나타내는 패턴입니다.

```tsx
import { useCurrentFrame, useVideoConfig, spring, interpolate } from 'remotion';

const STAGGER_FRAMES = 6; // 단어 간 딜레이

export const WordReveal: React.FC<{ text: string }> = ({ text }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const words = text.split(' ');

  return (
    <div style={{ display: 'flex', flexWrap: 'wrap', gap: 12 }}>
      {words.map((word, i) => {
        const delay = i * STAGGER_FRAMES;
        const sp = spring({
          frame: frame - delay,
          fps,
          config: { damping: 14, stiffness: 100 },
        });
        return (
          <span
            key={i}
            style={{
              opacity: interpolate(sp, [0, 1], [0, 1]),
              transform: `translateY(${interpolate(sp, [0, 1], [20, 0])}px)`,
              fontSize: 48,
              color: 'white',
              fontFamily: 'sans-serif',
            }}
          >
            {word}
          </span>
        );
      })}
    </div>
  );
};
```

---

## 3. 워드 하이라이트 (Word Highlight — 형광펜 효과)

현재 말해지는 단어에 형광펜 색상을 입히는 자막 스타일.

```tsx
import { useCurrentFrame, useVideoConfig, interpolate, spring } from 'remotion';

interface Word { text: string; startFrame: number; endFrame: number }

export const WordHighlight: React.FC<{ words: Word[] }> = ({ words }) => {
  const frame = useCurrentFrame();

  return (
    <div style={{ display: 'flex', flexWrap: 'wrap', gap: 8, padding: 40 }}>
      {words.map((word, i) => {
        const isActive = frame >= word.startFrame && frame < word.endFrame;
        return (
          <span
            key={i}
            style={{
              fontSize: 52,
              color: 'white',
              fontWeight: 'bold',
              background: isActive ? '#39E508' : 'transparent',
              borderRadius: 6,
              padding: '2px 8px',
              transition: 'background 0.1s',
            }}
          >
            {word.text}
          </span>
        );
      })}
    </div>
  );
};
```

> TTS 오디오와 함께 쓸 때: `@remotion/captions`의 `createTikTokStyleCaptions()`로
> 단어별 타임스탬프를 자동 생성할 수 있습니다 → [07-Rich-Media/concepts/captions.md](../../07-Rich-Media/concepts/captions.md)

---

## 4. 글자별 등장 (Char Stagger)

제목 텍스트를 글자 단위로 팝인시키는 고급 효과.

```tsx
const CharReveal: React.FC<{ text: string }> = ({ text }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  return (
    <div style={{ display: 'flex' }}>
      {[...text].map((char, i) => {
        const sp = spring({
          frame: frame - i * 3, // 글자마다 3프레임 딜레이
          fps,
          config: { damping: 12, stiffness: 150 },
        });
        return (
          <span
            key={i}
            style={{
              opacity: sp,
              transform: `scale(${sp}) translateY(${(1 - sp) * -20}px)`,
              display: 'inline-block',
              fontSize: 80,
              fontWeight: 900,
              color: 'white',
            }}
          >
            {char === ' ' ? ' ' : char}
          </span>
        );
      })}
    </div>
  );
};
```

---

## 5. 텍스트 카운트업 (Counter Animation)

숫자가 증가하는 인포그래픽 효과 (M3 CounterInfoGraphic에서 구현됨):

```tsx
const frame = useCurrentFrame();
const { fps, durationInFrames } = useVideoConfig();

const progress = interpolate(frame, [0, durationInFrames * 0.7], [0, 1], {
  extrapolateRight: 'clamp',
  easing: Easing.out(Easing.cubic),
});

const value = Math.floor(progress * targetValue);
```

---

## 패턴 선택 가이드

| 상황 | 권장 패턴 |
|------|-----------|
| 자막, 나레이션 동기화 | 워드 하이라이트 + @remotion/captions |
| 인트로 제목 | 글자별 등장 (CharReveal) |
| 설명 텍스트 | 단어별 순차 등장 (WordReveal) |
| 코드/대화 시뮬레이션 | 타이프라이터 (Typewriter) |
| 인포그래픽 통계 | 카운트업 (Counter Animation) |
