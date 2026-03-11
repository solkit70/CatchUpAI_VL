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

interface DefinitionSlideV2Props {
  data: SlideData;
  durationInFrames: number;
}

export const DefinitionSlideV2: React.FC<DefinitionSlideV2Props> = ({ data, durationInFrames }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const sectionColor = SECTION_COLORS.intro2;
  const lines = (data.content || '').split('\n');

  const fadeOut = interpolate(frame, [durationInFrames - 15, durationInFrames], [1, 0], {
    extrapolateRight: 'clamp',
  });

  // 배경 글로우 펄스
  const glowScale = 1 + Math.sin((frame / fps) * 1.2) * 0.05;

  // 동심원 파문 (2가지 주기)
  const ripple1T = (frame % (fps * 2)) / (fps * 2);
  const ripple2T = ((frame + fps) % (fps * 2.5)) / (fps * 2.5);
  const ripple1Scale = 0.5 + ripple1T * 1.5;
  const ripple2Scale = 0.5 + ripple2T * 1.8;
  const ripple1Opacity = 0.05 * (1 - ripple1T);
  const ripple2Opacity = 0.04 * (1 - ripple2T);

  return (
    <AbsoluteFill style={{ opacity: fadeOut }}>
      <AnimatedBgV2 sectionColor={sectionColor} intensity={0.4} />

      {/* 중앙 글로우 */}
      <AbsoluteFill style={{ display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
        <div
          style={{
            width: 400,
            height: 400,
            borderRadius: '50%',
            background: `radial-gradient(circle, ${sectionColor}18 0%, transparent 70%)`,
            transform: `scale(${glowScale})`,
          }}
        />
      </AbsoluteFill>

      {/* 동심원 파문 1 */}
      <AbsoluteFill style={{ display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
        <div
          style={{
            width: 500,
            height: 500,
            borderRadius: '50%',
            border: `2px solid ${sectionColor}`,
            opacity: ripple1Opacity,
            transform: `scale(${ripple1Scale})`,
          }}
        />
      </AbsoluteFill>

      {/* 동심원 파문 2 */}
      <AbsoluteFill style={{ display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
        <div
          style={{
            width: 600,
            height: 600,
            borderRadius: '50%',
            border: `1px solid ${sectionColor}`,
            opacity: ripple2Opacity,
            transform: `scale(${ripple2Scale})`,
          }}
        />
      </AbsoluteFill>

      <AbsoluteFill
        style={{
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          justifyContent: 'center',
          padding: '80px 160px',
          textAlign: 'center',
          gap: 32,
        }}
      >
        {/* 소제목 */}
        <div
          style={{
            fontSize: 18,
            color: sectionColor,
            letterSpacing: 4,
            fontFamily: 'sans-serif',
            fontWeight: 600,
            textTransform: 'uppercase',
            opacity: interpolate(frame, [0, 20], [0, 1], { extrapolateRight: 'clamp' }),
          }}
        >
          {data.emoji} {data.title}
        </div>

        {/* 메인 텍스트 (라인별 등장 + shimmer) */}
        <div style={{ display: 'flex', flexDirection: 'column', gap: 16 }}>
          {lines.map((line, i) => {
            const lineSpring = spring({
              frame: frame - 15 - i * 20,
              fps,
              config: { damping: 14, stiffness: 80 },
            });
            const lineOpacity = interpolate(frame - 15 - i * 20, [0, 20], [0, 1], {
              extrapolateRight: 'clamp',
            });

            // shimmer: 2초 주기로 색상 전환 (white ↔ sectionColor)
            const shimmerT = 0.5 + Math.sin((frame / fps) * Math.PI) * 0.5;
            const isHighlight = i % 2 !== 0;
            const shimmerColor = isHighlight
              ? sectionColor
              : `rgb(${255 - Math.floor(shimmerT * 20)}, ${255 - Math.floor(shimmerT * 20)}, 255)`;

            return (
              <div
                key={i}
                style={{
                  fontSize: 52,
                  fontWeight: 900,
                  fontFamily: 'sans-serif',
                  lineHeight: 1.2,
                  opacity: lineOpacity,
                  transform: `scale(${0.8 + lineSpring * 0.2})`,
                  color: isHighlight ? shimmerColor : COLORS.text,
                  textShadow: isHighlight ? `0 0 ${30 + shimmerT * 20}px ${sectionColor}88` : undefined,
                }}
              >
                {line}
              </div>
            );
          })}
        </div>

        {/* 서브 텍스트 */}
        {data.sub && (
          <div
            style={{
              fontSize: 22,
              color: COLORS.textMuted,
              fontFamily: 'sans-serif',
              fontStyle: 'italic',
              opacity: interpolate(frame, [60, 80], [0, 1], { extrapolateRight: 'clamp' }),
              padding: '12px 24px',
              border: `1px solid ${sectionColor}44`,
              borderRadius: 8,
              background: `${sectionColor}0a`,
            }}
          >
            {data.sub}
          </div>
        )}
      </AbsoluteFill>

      <Audio src={staticFile(data.audioSrc)} />
    </AbsoluteFill>
  );
};
