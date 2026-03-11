import { AbsoluteFill, useCurrentFrame, useVideoConfig, interpolate } from 'remotion';
import { COLORS } from '../data';

// 120개 별 파티클 (골든앵글 분포)
const STARS = Array.from({ length: 120 }, (_, i) => {
  const goldenAngle = 2.399963;
  const r = Math.sqrt(i / 120) * 100;
  const theta = i * goldenAngle;
  return {
    x: 50 + r * Math.cos(theta),
    y: 50 + r * Math.sin(theta),
    size: (i % 5) * 0.5 + 0.3,
    delay: i * 2,
  };
});

// 흐르는 형광 수평 라인 3개
const NEON_LINES = [
  { speed: 0.4, opacity: 0.07, y: 22 },
  { speed: 0.65, opacity: 0.06, y: 58 },
  { speed: 0.5, opacity: 0.08, y: 83 },
];

interface AnimatedBgV2Props {
  sectionColor?: string;
  intensity?: number; // 0-1
}

export const AnimatedBgV2: React.FC<AnimatedBgV2Props> = ({
  sectionColor = COLORS.primary,
  intensity = 0.3,
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const gradientAngle = ((frame / (fps * 30)) * 360) % 360;

  // 중앙 방사 파동 (2초 주기)
  const rippleT = (frame % (fps * 2)) / (fps * 2);
  const rippleScale = 1 + rippleT * 0.8;
  const rippleOpacity = 0.06 * (1 - rippleT);

  const hexOpacity = 0.04 + Math.sin(frame * 0.01) * 0.02;
  const hexRotation = frame * 0.3;

  return (
    <AbsoluteFill style={{ background: COLORS.bg }}>
      {/* 동적 방사형 그라데이션 */}
      <AbsoluteFill
        style={{
          background: `radial-gradient(ellipse at ${
            50 + Math.sin((frame / fps) * 0.5) * 20
          }% ${
            50 + Math.cos((frame / fps) * 0.3) * 15
          }%, ${sectionColor}${Math.round(intensity * 55).toString(16).padStart(2, '0')} 0%, transparent 70%)`,
        }}
      />

      {/* 회전하는 코너 글로우 */}
      <AbsoluteFill
        style={{
          background: `conic-gradient(from ${gradientAngle}deg at 5% 5%, ${sectionColor}18, transparent 30%, transparent 70%, ${sectionColor}12, transparent 100%)`,
        }}
      />

      {/* 중앙 방사 파동 */}
      <AbsoluteFill style={{ display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
        <div
          style={{
            width: 500,
            height: 500,
            borderRadius: '50%',
            border: `2px solid ${sectionColor}`,
            opacity: rippleOpacity,
            transform: `scale(${rippleScale})`,
          }}
        />
      </AbsoluteFill>

      {/* 느리게 회전하는 육각형 와이어프레임 */}
      <AbsoluteFill style={{ display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
        <svg width={700} height={700} viewBox="-1 -1 2 2" style={{ transform: `rotate(${hexRotation}deg)` }}>
          <polygon
            points="0.5,0 0.25,0.433 -0.25,0.433 -0.5,0 -0.25,-0.433 0.25,-0.433"
            fill="none"
            stroke={sectionColor}
            strokeWidth="0.01"
            opacity={hexOpacity}
          />
          <polygon
            points="0.75,0 0.375,0.65 -0.375,0.65 -0.75,0 -0.375,-0.65 0.375,-0.65"
            fill="none"
            stroke={sectionColor}
            strokeWidth="0.007"
            opacity={hexOpacity * 0.6}
          />
        </svg>
      </AbsoluteFill>

      {/* 수평 흐르는 형광 라인 */}
      <AbsoluteFill>
        <svg width="100%" height="100%" style={{ position: 'absolute' }}>
          {NEON_LINES.map((line, i) => {
            const offset = ((frame * line.speed) % 100);
            return (
              <line
                key={i}
                x1={`${-10 + offset}%`}
                y1={`${line.y}%`}
                x2={`${60 + offset}%`}
                y2={`${line.y}%`}
                stroke={sectionColor}
                strokeWidth={1}
                opacity={line.opacity}
                strokeLinecap="round"
              />
            );
          })}
        </svg>
      </AbsoluteFill>

      {/* 별 파티클 120개 */}
      <AbsoluteFill>
        <svg width="100%" height="100%" style={{ position: 'absolute' }}>
          {STARS.map((star, i) => {
            const twinkle = interpolate(
              (frame + star.delay) % (fps * 2),
              [0, fps, fps * 2],
              [0.1, 0.9, 0.1],
              { extrapolateRight: 'clamp' }
            );
            return (
              <circle
                key={i}
                cx={`${star.x}%`}
                cy={`${star.y}%`}
                r={star.size}
                fill="white"
                opacity={twinkle * 0.65}
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
