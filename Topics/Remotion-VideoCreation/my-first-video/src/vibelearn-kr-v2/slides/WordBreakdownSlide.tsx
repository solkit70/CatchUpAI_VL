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

interface WordBreakdownSlideProps {
  data: SlideData;
  durationInFrames: number;
}

const WORD_COLORS = [COLORS.primary, COLORS.accent, COLORS.coral];

export const WordBreakdownSlide: React.FC<WordBreakdownSlideProps> = ({
  data,
  durationInFrames,
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const items = data.items || [];
  const sectionColor = SECTION_COLORS.intro2;

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
          alignItems: 'center',
          justifyContent: 'center',
          gap: 40,
          padding: '60px 80px',
        }}
      >
        <div
          style={{
            opacity: interpolate(frame, [0, 20], [0, 1], { extrapolateRight: 'clamp' }),
            textAlign: 'center',
          }}
        >
          <div style={{ fontSize: 20, color: sectionColor, letterSpacing: 4, fontFamily: 'sans-serif' }}>
            {data.emoji} {data.title}
          </div>
        </div>

        <div style={{ display: 'flex', gap: 32, alignItems: 'stretch', width: '100%' }}>
          {items.map((item, i) => {
            const DELAY = i * 25;
            const boxSpring = spring({ frame: frame - DELAY, fps, config: { damping: 14, stiffness: 80 } });
            const boxOpacity = interpolate(frame - DELAY, [0, 20], [0, 1], { extrapolateRight: 'clamp' });
            const color = WORD_COLORS[i];

            return (
              <div
                key={i}
                style={{
                  flex: 1,
                  opacity: boxOpacity,
                  transform: `scale(${0.7 + boxSpring * 0.3}) translateY(${interpolate(boxSpring, [0, 1], [40, 0])}px)`,
                  background: `${color}15`,
                  border: `2px solid ${color}`,
                  borderRadius: 20,
                  padding: '36px 28px',
                  display: 'flex',
                  flexDirection: 'column',
                  alignItems: 'center',
                  gap: 16,
                  boxShadow: `0 0 30px ${color}22`,
                }}
              >
                <div style={{ fontSize: 40 }}>{item.emoji}</div>
                <div
                  style={{
                    fontSize: 52,
                    fontWeight: 900,
                    color,
                    fontFamily: 'sans-serif',
                    textShadow: `0 0 20px ${color}66`,
                  }}
                >
                  {item.text}
                </div>
                <div style={{ width: 60, height: 2, background: color, borderRadius: 1 }} />
                <div
                  style={{
                    fontSize: 18,
                    color: COLORS.textMuted,
                    fontFamily: 'sans-serif',
                    textAlign: 'center',
                    lineHeight: 1.5,
                    opacity: interpolate(frame - DELAY - 15, [0, 20], [0, 1], { extrapolateRight: 'clamp' }),
                  }}
                >
                  {item.sub}
                </div>
              </div>
            );
          })}
        </div>

        <div
          style={{
            opacity: interpolate(frame, [80, 100], [0, 1], { extrapolateRight: 'clamp' }),
            transform: `scale(${interpolate(frame, [80, 100], [0.8, 1], { extrapolateRight: 'clamp' })})`,
            fontSize: 32,
            fontWeight: 700,
            fontFamily: 'sans-serif',
          }}
        >
          <span style={{ color: COLORS.primary }}>Vibe</span>
          <span style={{ color: COLORS.accent }}>Learn</span>
          <span style={{ color: COLORS.coral }}> AI</span>
          <span style={{ color: COLORS.textMuted }}> = 배우고 싶은 것을 말하면 AI가 이끌어주는 시스템</span>
        </div>
      </AbsoluteFill>

      <Audio src={staticFile(data.audioSrc)} />
    </AbsoluteFill>
  );
};
