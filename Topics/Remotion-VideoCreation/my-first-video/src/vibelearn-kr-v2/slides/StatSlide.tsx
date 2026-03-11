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

const STAT_COLORS = [COLORS.primary, COLORS.accent, COLORS.green];
const STAT_MAX = [9.5, 22, 2];

interface StatSlideProps {
  data: SlideData;
  durationInFrames: number;
}

export const StatSlide: React.FC<StatSlideProps> = ({ data, durationInFrames }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const items = data.items || [];
  const sectionColor = SECTION_COLORS.casestudy;

  const headerOpacity = interpolate(frame, [0, 20], [0, 1], { extrapolateRight: 'clamp' });
  const fadeOut = interpolate(frame, [durationInFrames - 15, durationInFrames], [1, 0], {
    extrapolateRight: 'clamp',
  });

  const CIRCLE_R = 90;
  const CIRCUMFERENCE = 2 * Math.PI * CIRCLE_R;

  return (
    <AbsoluteFill style={{ opacity: fadeOut }}>
      <AnimatedBgV2 sectionColor={sectionColor} intensity={0.3} />

      <AbsoluteFill
        style={{
          display: 'flex',
          flexDirection: 'column',
          padding: '60px 100px',
          gap: 40,
        }}
      >
        <div style={{ opacity: headerOpacity, display: 'flex', alignItems: 'center', gap: 16 }}>
          {data.emoji && <span style={{ fontSize: 36 }}>{data.emoji}</span>}
          <div>
            <div style={{ fontSize: 38, fontWeight: 800, color: COLORS.text, fontFamily: 'sans-serif' }}>
              {data.title}
            </div>
            <div style={{ width: 80, height: 3, background: sectionColor, marginTop: 8, borderRadius: 2 }} />
          </div>
        </div>

        <div style={{ display: 'flex', gap: 40, justifyContent: 'center', flex: 1, alignItems: 'center' }}>
          {items.map((item, i) => {
            const DELAY = 20 + i * 25;
            const cardSpring = spring({ frame: frame - DELAY, fps, config: { damping: 14, stiffness: 80 } });
            const cardOpacity = interpolate(frame - DELAY, [0, 20], [0, 1], { extrapolateRight: 'clamp' });
            const color = STAT_COLORS[i];
            const maxVal = STAT_MAX[i];

            const countProgress = interpolate(frame - DELAY, [0, 60], [0, maxVal], { extrapolateRight: 'clamp' });
            const displayVal = countProgress.toFixed(maxVal % 1 !== 0 ? 1 : 0);

            const gaugeProgress = spring({ frame: frame - DELAY, fps, config: { damping: 20, stiffness: 60 } });
            const dashOffset = CIRCUMFERENCE * (1 - gaugeProgress);

            return (
              <div
                key={i}
                style={{
                  display: 'flex',
                  flexDirection: 'column',
                  alignItems: 'center',
                  gap: 20,
                  opacity: cardOpacity,
                  transform: `scale(${0.7 + cardSpring * 0.3})`,
                }}
              >
                <div style={{ position: 'relative' }}>
                  <svg width={240} height={240} viewBox={`0 0 ${CIRCLE_R * 2 + 40} ${CIRCLE_R * 2 + 40}`}>
                    <circle cx={CIRCLE_R + 20} cy={CIRCLE_R + 20} r={CIRCLE_R} fill="none" stroke={`${color}22`} strokeWidth={12} />
                    <circle
                      cx={CIRCLE_R + 20}
                      cy={CIRCLE_R + 20}
                      r={CIRCLE_R}
                      fill="none"
                      stroke={color}
                      strokeWidth={12}
                      strokeLinecap="round"
                      strokeDasharray={CIRCUMFERENCE}
                      strokeDashoffset={dashOffset}
                      transform={`rotate(-90 ${CIRCLE_R + 20} ${CIRCLE_R + 20})`}
                      style={{ filter: `drop-shadow(0 0 8px ${color})` }}
                    />
                    <text x={CIRCLE_R + 20} y={CIRCLE_R + 5} textAnchor="middle" fontSize={32}>{item.emoji}</text>
                    <text x={CIRCLE_R + 20} y={CIRCLE_R + 38} textAnchor="middle" fill={color} fontSize={28} fontWeight="900" fontFamily="sans-serif">
                      {displayVal}
                    </text>
                  </svg>
                </div>
                <div style={{ fontSize: 20, color: COLORS.textMuted, fontFamily: 'sans-serif', textAlign: 'center' }}>
                  {item.sub}
                </div>
              </div>
            );
          })}
        </div>

        <div
          style={{
            textAlign: 'center',
            opacity: interpolate(frame, [80, 100], [0, 1], { extrapolateRight: 'clamp' }),
            fontSize: 20,
            color: COLORS.textMuted,
            fontFamily: 'sans-serif',
          }}
        >
          VibeLearn AI 방법론으로 달성한 실제 성과
        </div>
      </AbsoluteFill>

      <Audio src={staticFile(data.audioSrc)} />
    </AbsoluteFill>
  );
};
