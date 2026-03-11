import { AbsoluteFill, useCurrentFrame, useVideoConfig, interpolate } from 'remotion';
import { COLORS } from '../data';

// 배경 별 데이터 (골든앵글 분포)
const STARS = Array.from({ length: 60 }, (_, i) => {
  const goldenAngle = 2.399963;
  const r = Math.sqrt(i / 60) * 100;
  const theta = i * goldenAngle;
  return {
    x: 50 + r * Math.cos(theta),
    y: 50 + r * Math.sin(theta),
    size: Math.random() * 2 + 0.5,
    delay: i * 3,
  };
});

interface AnimatedBgProps {
  sectionColor?: string;
  intensity?: number; // 0-1
}

export const AnimatedBg: React.FC<AnimatedBgProps> = ({
  sectionColor = COLORS.primary,
  intensity = 0.3,
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const gradientAngle = interpolate(frame, [0, fps * 30], [0, 360], {
    extrapolateRight: 'wrap',
  });

  return (
    <AbsoluteFill style={{ background: COLORS.bg }}>
      {/* 동적 방사형 그라데이션 */}
      <AbsoluteFill
        style={{
          background: `radial-gradient(ellipse at ${
            50 + Math.sin((frame / fps) * 0.5) * 20
          }% ${
            50 + Math.cos((frame / fps) * 0.3) * 15
          }%, ${sectionColor}${Math.round(intensity * 40).toString(16).padStart(2, '0')} 0%, transparent 70%)`,
        }}
      />

      {/* 회전하는 코너 글로우 */}
      <AbsoluteFill
        style={{
          background: `conic-gradient(from ${gradientAngle}deg at 5% 5%, ${sectionColor}15, transparent 30%, transparent 70%, ${sectionColor}10, transparent 100%)`,
        }}
      />

      {/* 별 파티클 */}
      <AbsoluteFill>
        <svg width="100%" height="100%" style={{ position: 'absolute' }}>
          {STARS.map((star, i) => {
            const twinkle = interpolate(
              (frame + star.delay) % (fps * 3),
              [0, fps * 1.5, fps * 3],
              [0.2, 1, 0.2],
              { extrapolateRight: 'clamp' }
            );
            return (
              <circle
                key={i}
                cx={`${star.x}%`}
                cy={`${star.y}%`}
                r={star.size}
                fill="white"
                opacity={twinkle * 0.6}
              />
            );
          })}
        </svg>
      </AbsoluteFill>

      {/* 하단 그라데이션 페이드 */}
      <AbsoluteFill
        style={{
          background: `linear-gradient(to top, ${COLORS.bg} 0%, transparent 30%)`,
        }}
      />
    </AbsoluteFill>
  );
};
