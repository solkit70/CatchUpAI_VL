import {
  AbsoluteFill,
  useCurrentFrame,
  useVideoConfig,
  interpolate,
  spring,
} from 'remotion';
import { COLORS } from '../data';
import type { SectionHeaderData } from '../data';

interface SectionHeaderProps {
  data: SectionHeaderData;
}

export const SectionHeader: React.FC<SectionHeaderProps> = ({ data }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const lineWidth = spring({ frame, fps, config: { damping: 20, stiffness: 100 } });
  const textOpacity = interpolate(frame, [10, 25], [0, 1], { extrapolateRight: 'clamp' });
  const textY = interpolate(frame, [10, 25], [20, 0], { extrapolateRight: 'clamp' });

  return (
    <AbsoluteFill
      style={{
        background: `linear-gradient(135deg, ${COLORS.bg} 0%, ${data.color}22 100%)`,
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'center',
      }}
    >
      {/* 섹션 번호 */}
      <div
        style={{
          fontSize: 18,
          color: data.color,
          letterSpacing: 6,
          textTransform: 'uppercase',
          fontFamily: 'sans-serif',
          fontWeight: 600,
          opacity: textOpacity,
          transform: `translateY(${textY}px)`,
          marginBottom: 16,
        }}
      >
        {data.number}
      </div>

      {/* 구분선 */}
      <div
        style={{
          width: `${lineWidth * 200}px`,
          height: 2,
          background: data.color,
          marginBottom: 24,
          boxShadow: `0 0 12px ${data.color}`,
        }}
      />

      {/* 섹션 제목 */}
      <div
        style={{
          fontSize: 48,
          fontWeight: 800,
          color: COLORS.text,
          fontFamily: 'sans-serif',
          opacity: textOpacity,
          transform: `translateY(${textY}px)`,
        }}
      >
        {data.title}
      </div>
    </AbsoluteFill>
  );
};
