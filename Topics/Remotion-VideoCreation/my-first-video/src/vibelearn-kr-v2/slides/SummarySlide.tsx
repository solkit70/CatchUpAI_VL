import {
  AbsoluteFill,
  Audio,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
  interpolate,
  spring,
} from 'remotion';
import { COLORS, SECTION_COLORS } from '../data';
import { AnimatedBgV2 } from '../common/AnimatedBgV2';
import type { SlideData } from '../data';

const ROW_COLORS = [COLORS.primary, COLORS.accent, COLORS.green, COLORS.coral, '#a78bfa'];

interface SummarySlideProps {
  data: SlideData;
  durationInFrames: number;
}

export const SummarySlide: React.FC<SummarySlideProps> = ({ data, durationInFrames }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const items = data.items || [];
  const sectionColor = SECTION_COLORS.outro;

  const headerOpacity = interpolate(frame, [0, 20], [0, 1], { extrapolateRight: 'clamp' });
  const fadeOut = interpolate(frame, [durationInFrames - 15, durationInFrames], [1, 0], {
    extrapolateRight: 'clamp',
  });

  return (
    <AbsoluteFill style={{ opacity: fadeOut }}>
      <AnimatedBgV2 sectionColor={sectionColor} intensity={0.3} />

      <AbsoluteFill
        style={{
          display: 'flex',
          flexDirection: 'column',
          padding: '60px 120px',
          gap: 32,
        }}
      >
        <div style={{ opacity: headerOpacity, display: 'flex', alignItems: 'center', gap: 16 }}>
          {data.emoji && <span style={{ fontSize: 36 }}>{data.emoji}</span>}
          <div style={{ fontSize: 40, fontWeight: 800, color: COLORS.text, fontFamily: 'sans-serif' }}>
            {data.title}
          </div>
        </div>

        <div style={{ flex: 1, display: 'flex', flexDirection: 'column', gap: 12, justifyContent: 'center' }}>
          {items.map((item, i) => {
            const delay = 20 + i * 20;
            const rowSpring = spring({ frame: frame - delay, fps, config: { damping: 16, stiffness: 100 } });
            const rowOpacity = interpolate(frame - delay, [0, 15], [0, 1], { extrapolateRight: 'clamp' });
            const color = ROW_COLORS[i % ROW_COLORS.length];

            return (
              <div
                key={i}
                style={{
                  display: 'flex',
                  alignItems: 'center',
                  gap: 0,
                  opacity: rowOpacity,
                  transform: `translateX(${interpolate(rowSpring, [0, 1], [-50, 0])}px)`,
                }}
              >
                <div
                  style={{
                    width: 300,
                    padding: '14px 20px',
                    background: `${color}20`,
                    border: `1px solid ${color}44`,
                    borderRight: 'none',
                    borderRadius: '10px 0 0 10px',
                    display: 'flex',
                    alignItems: 'center',
                    gap: 10,
                  }}
                >
                  <span style={{ fontSize: 22 }}>{item.emoji}</span>
                  <span style={{ fontSize: 18, fontWeight: 700, color, fontFamily: 'sans-serif' }}>
                    {item.text}
                  </span>
                </div>
                <div
                  style={{
                    flex: 1,
                    padding: '14px 20px',
                    background: COLORS.card,
                    border: `1px solid ${COLORS.cardBorder}`,
                    borderRadius: '0 10px 10px 0',
                    fontSize: 18,
                    color: COLORS.text,
                    fontFamily: 'sans-serif',
                  }}
                >
                  {item.sub}
                </div>
              </div>
            );
          })}
        </div>
      </AbsoluteFill>

      <Audio src={staticFile(data.audioSrc)} />
    </AbsoluteFill>
  );
};
