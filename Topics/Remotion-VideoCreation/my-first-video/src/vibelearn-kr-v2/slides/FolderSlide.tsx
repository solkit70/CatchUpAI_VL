import {
  AbsoluteFill,
  Audio,
  staticFile,
  useCurrentFrame,
  interpolate,
} from 'remotion';
import { COLORS, SECTION_COLORS } from '../data';
import { AnimatedBgV2 } from '../common/AnimatedBgV2';
import type { SlideData } from '../data';

interface FolderSlideProps {
  data: SlideData;
  durationInFrames: number;
}

export const FolderSlide: React.FC<FolderSlideProps> = ({ data, durationInFrames }) => {
  const frame = useCurrentFrame();
  const items = data.items || [];
  const sectionColor = SECTION_COLORS.casestudy;

  const fadeOut = interpolate(frame, [durationInFrames - 15, durationInFrames], [1, 0], {
    extrapolateRight: 'clamp',
  });
  const headerOpacity = interpolate(frame, [0, 20], [0, 1], { extrapolateRight: 'clamp' });

  return (
    <AbsoluteFill style={{ opacity: fadeOut }}>
      <AnimatedBgV2 sectionColor={sectionColor} intensity={0.25} />

      <AbsoluteFill
        style={{
          display: 'flex',
          flexDirection: 'row',
          padding: '60px 100px',
          gap: 60,
          alignItems: 'center',
        }}
      >
        {/* 좌측: 헤더 + 설명 */}
        <div style={{ flex: 1, display: 'flex', flexDirection: 'column', gap: 24 }}>
          <div style={{ opacity: headerOpacity }}>
            {data.emoji && <span style={{ fontSize: 36 }}>{data.emoji}</span>}
            <div style={{ fontSize: 38, fontWeight: 800, color: COLORS.text, fontFamily: 'sans-serif', marginTop: 8 }}>
              {data.title}
            </div>
            <div style={{ width: 80, height: 3, background: sectionColor, marginTop: 8, borderRadius: 2 }} />
          </div>

          <div
            style={{
              opacity: interpolate(frame, [30, 50], [0, 1], { extrapolateRight: 'clamp' }),
              fontSize: 20,
              color: COLORS.textMuted,
              fontFamily: 'sans-serif',
              lineHeight: 1.6,
            }}
          >
            학습이 끝나면 이런 폴더 구조가 자동으로 쌓입니다.
            <br />다음 학습자가 바로 재사용할 수 있는 교과서 품질.
          </div>
        </div>

        {/* 우측: 폴더 트리 */}
        <div
          style={{
            flex: 1.4,
            background: '#0d0d1a',
            border: `1px solid ${sectionColor}33`,
            borderRadius: 16,
            padding: '32px 36px',
            fontFamily: 'monospace',
            fontSize: 18,
            display: 'flex',
            flexDirection: 'column',
            gap: 4,
          }}
        >
          {/* 터미널 헤더 */}
          <div style={{ display: 'flex', gap: 8, marginBottom: 20 }}>
            {['#ff5f57', '#ffbd2e', '#28c840'].map((c, i) => (
              <div key={i} style={{ width: 12, height: 12, borderRadius: '50%', background: c }} />
            ))}
          </div>

          {items.map((item, i) => {
            const delay = 20 + i * 20;
            const itemOpacity = interpolate(frame - delay, [0, 15], [0, 1], { extrapolateRight: 'clamp' });
            const itemX = interpolate(frame - delay, [0, 15], [-20, 0], { extrapolateRight: 'clamp' });

            const isRoot = i === 0;
            const indent = isRoot ? 0 : 24;
            const color = isRoot ? sectionColor : COLORS.primary;
            const prefix = isRoot ? '' : '  ├── ';

            return (
              <div
                key={i}
                style={{
                  opacity: itemOpacity,
                  transform: `translateX(${itemX}px)`,
                  display: 'flex',
                  alignItems: 'center',
                  gap: 8,
                  paddingLeft: indent,
                  paddingTop: isRoot ? 0 : 2,
                  paddingBottom: isRoot ? 0 : 2,
                }}
              >
                <span style={{ color: COLORS.textMuted }}>{prefix}</span>
                <span style={{ fontSize: 18 }}>{item.emoji}</span>
                <span style={{ color }}>{item.text}</span>
                {item.sub && (
                  <span style={{ color: COLORS.textMuted, fontSize: 14, marginLeft: 8 }}>
                    # {item.sub}
                  </span>
                )}
              </div>
            );
          })}

          {/* 타이핑 커서 */}
          <div
            style={{
              color: sectionColor,
              opacity: frame % 20 < 10 ? 1 : 0,
              paddingLeft: 24,
              marginTop: 8,
            }}
          >
            │
          </div>
        </div>
      </AbsoluteFill>

      <Audio src={staticFile(data.audioSrc)} />
    </AbsoluteFill>
  );
};
