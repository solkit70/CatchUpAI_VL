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
import { AnimatedBg } from '../common/AnimatedBg';
import type { SlideData } from '../data';

interface DefinitionSlideProps {
  data: SlideData;
  durationInFrames: number;
}

export const DefinitionSlide: React.FC<DefinitionSlideProps> = ({ data, durationInFrames }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const sectionColor = SECTION_COLORS.intro2;
  const lines = (data.content || '').split('\n');

  const fadeOut = interpolate(frame, [durationInFrames - 15, durationInFrames], [1, 0], {
    extrapolateRight: 'clamp',
  });

  // 배경 글로우 펄스
  const glowScale = 1 + Math.sin((frame / fps) * 1.2) * 0.05;

  return (
    <AbsoluteFill style={{ opacity: fadeOut }}>
      <AnimatedBg sectionColor={sectionColor} intensity={0.4} />

      {/* 중앙 글로우 */}
      <AbsoluteFill
        style={{
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
        }}
      >
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

        {/* 메인 텍스트 (라인별 등장) */}
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
                  color: i % 2 === 0 ? COLORS.text : sectionColor,
                  textShadow: i % 2 !== 0 ? `0 0 30px ${sectionColor}66` : undefined,
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
