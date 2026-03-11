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

// 파티클 데이터
const PARTICLES = Array.from({ length: 20 }, (_, i) => ({
  angle: (i / 20) * Math.PI * 2,
  distance: 300 + Math.random() * 200,
  size: 3 + Math.random() * 5,
  delay: i * 4,
}));

interface TitleSlideProps {
  data: SlideData;
  durationInFrames: number;
}

export const TitleSlide: React.FC<TitleSlideProps> = ({ data, durationInFrames }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // 채널명 타이핑 효과
  const channelChars = (data.content || '').split('');
  const channelReveal = Math.min(
    channelChars.length,
    Math.max(0, Math.floor((frame - 10) / 3))
  );

  // 타이틀 스프링 등장
  const titleSpring = spring({ frame: frame - 30, fps, config: { damping: 14, stiffness: 80 } });
  const titleOpacity = interpolate(frame, [30, 60], [0, 1], { extrapolateRight: 'clamp' });

  // 서브타이틀 페이드
  const subOpacity = interpolate(frame, [60, 90], [0, 1], { extrapolateRight: 'clamp' });
  const subY = interpolate(frame, [60, 90], [20, 0], { extrapolateRight: 'clamp' });

  // 아웃트로 페이드아웃
  const fadeOut = interpolate(
    frame,
    [durationInFrames - 20, durationInFrames],
    [1, 0],
    { extrapolateRight: 'clamp' }
  );

  return (
    <AbsoluteFill style={{ opacity: fadeOut }}>
      <AnimatedBg sectionColor={SECTION_COLORS.intro} intensity={0.5} />

      {/* 파티클 폭발 */}
      <AbsoluteFill>
        <svg width="100%" height="100%" viewBox="0 0 1920 1080" style={{ position: 'absolute' }}>
          {PARTICLES.map((p, i) => {
            const progress = spring({
              frame: frame - p.delay,
              fps,
              config: { damping: 20, stiffness: 60 },
            });
            const x = 960 + Math.cos(p.angle) * p.distance * progress;
            const y = 540 + Math.sin(p.angle) * p.distance * progress;
            const opacity = interpolate(progress, [0, 0.2, 0.8, 1], [0, 1, 1, 0]);
            return (
              <circle
                key={i}
                cx={x}
                cy={y}
                r={p.size}
                fill={COLORS.primary}
                opacity={opacity}
              />
            );
          })}
        </svg>
      </AbsoluteFill>

      {/* 중앙 컨텐츠 */}
      <AbsoluteFill
        style={{
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          justifyContent: 'center',
          gap: 24,
        }}
      >
        {/* 채널명 타이핑 */}
        <div
          style={{
            fontSize: 20,
            color: COLORS.primary,
            letterSpacing: 8,
            fontFamily: 'sans-serif',
            fontWeight: 600,
            textTransform: 'uppercase',
          }}
        >
          {channelChars.slice(0, channelReveal).join('')}
          {channelReveal < channelChars.length && (
            <span style={{ opacity: frame % 20 < 10 ? 1 : 0 }}>|</span>
          )}
        </div>

        {/* 구분선 */}
        <div
          style={{
            width: `${titleSpring * 400}px`,
            height: 2,
            background: `linear-gradient(90deg, transparent, ${COLORS.primary}, transparent)`,
            transition: 'none',
          }}
        />

        {/* 메인 타이틀 */}
        <div
          style={{
            fontSize: 88,
            fontWeight: 900,
            color: COLORS.text,
            fontFamily: 'sans-serif',
            textAlign: 'center',
            lineHeight: 1.1,
            opacity: titleOpacity,
            transform: `scale(${0.7 + titleSpring * 0.3})`,
            textShadow: `0 0 40px ${COLORS.primary}66`,
          }}
        >
          {data.title}
        </div>

        {/* 서브타이틀 */}
        <div
          style={{
            fontSize: 28,
            color: COLORS.textMuted,
            fontFamily: 'sans-serif',
            textAlign: 'center',
            fontWeight: 400,
            maxWidth: 800,
            opacity: subOpacity,
            transform: `translateY(${subY}px)`,
          }}
        >
          {data.sub}
        </div>

        {/* 하단 데코 라인 */}
        <div style={{ display: 'flex', gap: 8, marginTop: 16, opacity: subOpacity }}>
          {[COLORS.primary, COLORS.accent, COLORS.coral].map((c, i) => (
            <div
              key={i}
              style={{
                width: 40,
                height: 3,
                background: c,
                borderRadius: 2,
                boxShadow: `0 0 8px ${c}`,
              }}
            />
          ))}
        </div>
      </AbsoluteFill>

      <Audio src={staticFile(data.audioSrc)} />
    </AbsoluteFill>
  );
};
