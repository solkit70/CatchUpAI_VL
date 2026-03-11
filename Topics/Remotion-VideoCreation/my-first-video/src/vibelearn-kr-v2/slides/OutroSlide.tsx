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

interface OutroSlideProps {
  data: SlideData;
  durationInFrames: number;
}

export const OutroSlide: React.FC<OutroSlideProps> = ({ data, durationInFrames }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const items = data.items || [];
  const sectionColor = SECTION_COLORS.outro;

  const buttonPulse = 1 + Math.sin((frame / fps) * 3) * 0.04;
  const buttonGlow = 20 + Math.sin((frame / fps) * 3) * 10;

  const fadeIn = interpolate(frame, [0, 20], [0, 1], { extrapolateRight: 'clamp' });

  const channelSpring = spring({ frame, fps, config: { damping: 14, stiffness: 70 } });
  const msgSpring = spring({ frame: frame - 20, fps, config: { damping: 16, stiffness: 80 } });
  const subSpring = spring({ frame: frame - 40, fps, config: { damping: 18, stiffness: 90 } });

  return (
    <AbsoluteFill style={{ opacity: fadeIn }}>
      <AnimatedBgV2 sectionColor={sectionColor} intensity={0.5} />

      <AbsoluteFill
        style={{
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          justifyContent: 'center',
          gap: 32,
          padding: '60px 120px',
          textAlign: 'center',
        }}
      >
        {/* 채널명 */}
        <div
          style={{
            fontSize: 56,
            fontWeight: 900,
            color: COLORS.text,
            fontFamily: 'sans-serif',
            opacity: interpolate(channelSpring, [0, 1], [0, 1]),
            transform: `scale(${0.7 + channelSpring * 0.3})`,
            textShadow: `0 0 30px ${sectionColor}66`,
          }}
        >
          {data.content}
        </div>

        {/* 구분선 */}
        <div
          style={{
            width: `${channelSpring * 300}px`,
            height: 2,
            background: `linear-gradient(90deg, transparent, ${sectionColor}, transparent)`,
          }}
        />

        {/* 메인 메시지 */}
        <div
          style={{
            fontSize: 26,
            color: COLORS.textMuted,
            fontFamily: 'sans-serif',
            lineHeight: 1.6,
            opacity: interpolate(msgSpring, [0, 1], [0, 1]),
            transform: `translateY(${interpolate(msgSpring, [0, 1], [20, 0])}px)`,
            maxWidth: 900,
            whiteSpace: 'pre-line',
          }}
        >
          {data.sub}
        </div>

        {/* 구독 버튼 */}
        <div
          style={{
            background: 'linear-gradient(135deg, #ff0000, #cc0000)',
            color: '#ffffff',
            padding: '16px 48px',
            borderRadius: 48,
            fontSize: 22,
            fontWeight: 700,
            fontFamily: 'sans-serif',
            opacity: interpolate(subSpring, [0, 1], [0, 1]),
            transform: `scale(${(0.7 + subSpring * 0.3) * buttonPulse})`,
            boxShadow: `0 0 ${buttonGlow}px rgba(255,0,0,0.5)`,
            cursor: 'pointer',
          }}
        >
          🔔 구독 & 좋아요
        </div>

        {/* 아이콘 버튼들 */}
        <div
          style={{
            display: 'flex',
            gap: 32,
            opacity: interpolate(frame, [60, 80], [0, 1], { extrapolateRight: 'clamp' }),
          }}
        >
          {items.map((item, i) => (
            <div
              key={i}
              style={{
                display: 'flex',
                flexDirection: 'column',
                alignItems: 'center',
                gap: 8,
                padding: '16px 24px',
                background: COLORS.card,
                border: `1px solid ${sectionColor}44`,
                borderRadius: 16,
                cursor: 'pointer',
              }}
            >
              <span style={{ fontSize: 28 }}>{item.emoji}</span>
              <span style={{ fontSize: 14, color: COLORS.textMuted, fontFamily: 'sans-serif' }}>{item.text}</span>
            </div>
          ))}
        </div>

        {/* GitHub 링크 */}
        <div
          style={{
            fontSize: 18,
            color: sectionColor,
            fontFamily: 'monospace',
            opacity: interpolate(frame, [70, 90], [0, 1], { extrapolateRight: 'clamp' }),
          }}
        >
          🔗 github.com/solkit70/VibeLearn-AI
        </div>
      </AbsoluteFill>

      <Audio src={staticFile(data.audioSrc)} />
    </AbsoluteFill>
  );
};
