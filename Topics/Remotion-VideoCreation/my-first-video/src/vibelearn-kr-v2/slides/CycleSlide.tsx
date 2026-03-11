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

interface CycleSlideProps {
  data: SlideData;
  durationInFrames: number;
}

export const CycleSlide: React.FC<CycleSlideProps> = ({ data, durationInFrames }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const items = data.items || [];
  const sectionColor = SECTION_COLORS.problem;

  const headerOpacity = interpolate(frame, [0, 20], [0, 1], { extrapolateRight: 'clamp' });
  const fadeOut = interpolate(frame, [durationInFrames - 15, durationInFrames], [1, 0], {
    extrapolateRight: 'clamp',
  });

  const rotation = interpolate(frame, [0, fps * 30], [0, -360], {
    extrapolateRight: 'wrap',
  });

  const cx = 960;
  const cy = 580;
  const radius = 220;

  return (
    <AbsoluteFill style={{ opacity: fadeOut }}>
      <AnimatedBgV2 sectionColor={sectionColor} intensity={0.3} />

      <div
        style={{
          position: 'absolute',
          top: 60,
          left: 120,
          right: 120,
          opacity: headerOpacity,
          display: 'flex',
          alignItems: 'center',
          gap: 16,
        }}
      >
        {data.emoji && <span style={{ fontSize: 40 }}>{data.emoji}</span>}
        <div>
          <div style={{ fontSize: 40, fontWeight: 800, color: COLORS.text, fontFamily: 'sans-serif' }}>
            {data.title}
          </div>
          <div style={{ width: 80, height: 3, background: sectionColor, marginTop: 8, borderRadius: 2 }} />
        </div>
      </div>

      <AbsoluteFill>
        <svg width="1920" height="1080" viewBox="0 0 1920 1080" style={{ position: 'absolute' }}>
          <circle
            cx={cx}
            cy={cy}
            r={radius + 20}
            fill="none"
            stroke={sectionColor}
            strokeWidth={1}
            opacity={0.2}
            strokeDasharray="10 5"
          />

          <g transform={`rotate(${rotation}, ${cx}, ${cy})`}>
            {[0, 90, 180, 270].map((deg, i) => {
              const angle = (deg * Math.PI) / 180;
              const ax = cx + Math.cos(angle) * (radius + 20);
              const ay = cy + Math.sin(angle) * (radius + 20);
              return (
                <polygon
                  key={i}
                  points="0,-8 6,5 -6,5"
                  fill={sectionColor}
                  opacity={0.7}
                  transform={`translate(${ax}, ${ay}) rotate(${deg + 90})`}
                />
              );
            })}
          </g>

          {items.map((item, i) => {
            const angle = (i / items.length) * Math.PI * 2 - Math.PI / 2;
            const nx = cx + Math.cos(angle) * radius;
            const ny = cy + Math.sin(angle) * radius;
            const nodeSpring = spring({ frame: frame - i * 10, fps, config: { damping: 12, stiffness: 80 } });
            const nodeOpacity = interpolate(frame - i * 10, [0, 15], [0, 1], { extrapolateRight: 'clamp' });

            const highlight = (Math.floor(frame / (fps * 2)) % items.length) === i;
            const pulseScale = highlight ? 1 + Math.sin(frame * 0.15) * 0.08 : 1;

            return (
              <g key={i} opacity={nodeOpacity} transform={`scale(${nodeSpring})`}
                 style={{ transformOrigin: `${nx}px ${ny}px` }}>
                {highlight && (
                  <circle cx={nx} cy={ny} r={70} fill={sectionColor} opacity={0.1} />
                )}
                <circle
                  cx={nx}
                  cy={ny}
                  r={58 * pulseScale}
                  fill={COLORS.bg}
                  stroke={highlight ? sectionColor : `${sectionColor}66`}
                  strokeWidth={highlight ? 3 : 1.5}
                />
                <text x={nx} y={ny - 10} textAnchor="middle" fontSize={28} dy="0.35em">
                  {item.emoji}
                </text>
                <text
                  x={nx}
                  y={ny + 22}
                  textAnchor="middle"
                  fill={highlight ? sectionColor : COLORS.textMuted}
                  fontSize={16}
                  fontWeight={highlight ? '700' : '400'}
                  fontFamily="sans-serif"
                >
                  {item.text}
                </text>
              </g>
            );
          })}

          <text
            x={cx}
            y={cy}
            textAnchor="middle"
            fill={`${sectionColor}88`}
            fontSize={14}
            fontFamily="sans-serif"
            dy="0.35em"
            opacity={interpolate(frame, [30, 50], [0, 1], { extrapolateRight: 'clamp' })}
          >
            악순환
          </text>
        </svg>
      </AbsoluteFill>

      <div
        style={{
          position: 'absolute',
          bottom: 60,
          left: 0,
          right: 0,
          textAlign: 'center',
          opacity: interpolate(frame, [40, 60], [0, 1], { extrapolateRight: 'clamp' }),
        }}
      >
        <div style={{ fontSize: 20, color: COLORS.textMuted, fontFamily: 'sans-serif' }}>
          대부분의 학습이 이 패턴을 반복합니다
        </div>
      </div>

      <Audio src={staticFile(data.audioSrc)} />
    </AbsoluteFill>
  );
};
