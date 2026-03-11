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

interface StepSlideProps {
  data: SlideData;
  durationInFrames: number;
}

export const StepSlide: React.FC<StepSlideProps> = ({ data, durationInFrames }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const items = data.items || [];
  const sectionColor = SECTION_COLORS.howto;

  // Step 숫자 (content 필드에 "Step 1" 형태로 저장)
  const stepLabel = data.content || '';
  const stepNum = stepLabel.replace('Step ', '');

  const fadeOut = interpolate(frame, [durationInFrames - 15, durationInFrames], [1, 0], {
    extrapolateRight: 'clamp',
  });

  const numSpring = spring({ frame, fps, config: { damping: 12, stiffness: 70 } });
  const numOpacity = interpolate(frame, [0, 20], [0, 1], { extrapolateRight: 'clamp' });

  const contentOpacity = interpolate(frame, [20, 40], [0, 1], { extrapolateRight: 'clamp' });
  const contentX = interpolate(frame, [20, 40], [40, 0], { extrapolateRight: 'clamp' });

  // 슬라이드 14 (Step 3: 이게 전부)의 강조 효과
  const isHighlight = data.id === 14;
  const pulseGlow = isHighlight
    ? `0 0 ${40 + Math.sin(frame * 0.1) * 20}px ${sectionColor}66`
    : undefined;

  return (
    <AbsoluteFill style={{ opacity: fadeOut }}>
      <AnimatedBg sectionColor={sectionColor} intensity={0.3} />

      <AbsoluteFill
        style={{
          display: 'flex',
          flexDirection: 'row',
          alignItems: 'center',
          padding: '60px 100px',
          gap: 60,
        }}
      >
        {/* 좌측: 대형 단계 번호 */}
        <div
          style={{
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
            gap: 8,
            minWidth: 200,
          }}
        >
          <div
            style={{
              fontSize: 14,
              color: sectionColor,
              letterSpacing: 4,
              fontFamily: 'sans-serif',
              fontWeight: 600,
              textTransform: 'uppercase',
              opacity: numOpacity,
            }}
          >
            STEP
          </div>
          <div
            style={{
              fontSize: 160,
              fontWeight: 900,
              color: sectionColor,
              fontFamily: 'sans-serif',
              lineHeight: 1,
              opacity: numOpacity,
              transform: `scale(${0.5 + numSpring * 0.5})`,
              textShadow: `0 0 60px ${sectionColor}44`,
            }}
          >
            {stepNum}
          </div>
          {/* 데코 서클 */}
          <div
            style={{
              width: 4,
              height: `${numSpring * 80}px`,
              background: sectionColor,
              borderRadius: 2,
            }}
          />
        </div>

        {/* 세로 구분선 */}
        <div
          style={{
            width: 2,
            height: `${numSpring * 300}px`,
            background: `linear-gradient(to bottom, transparent, ${sectionColor}, transparent)`,
          }}
        />

        {/* 우측: 내용 */}
        <div
          style={{
            flex: 1,
            opacity: contentOpacity,
            transform: `translateX(${contentX}px)`,
            display: 'flex',
            flexDirection: 'column',
            gap: 24,
          }}
        >
          {/* 제목 */}
          <div>
            <div style={{ fontSize: 18, color: sectionColor, fontFamily: 'sans-serif', marginBottom: 8 }}>
              {data.emoji}
            </div>
            <div
              style={{
                fontSize: 44,
                fontWeight: 800,
                color: COLORS.text,
                fontFamily: 'sans-serif',
                lineHeight: 1.2,
                boxShadow: pulseGlow,
              }}
            >
              {data.title}
            </div>
            <div style={{ width: 60, height: 3, background: sectionColor, marginTop: 12, borderRadius: 2 }} />
          </div>

          {/* 강조 텍스트 (slide 14용) */}
          {data.sub && (
            <div
              style={{
                fontSize: 36,
                fontWeight: 700,
                color: sectionColor,
                fontFamily: 'sans-serif',
                fontStyle: 'italic',
                background: `${sectionColor}15`,
                border: `2px solid ${sectionColor}`,
                borderRadius: 12,
                padding: '16px 24px',
                opacity: interpolate(frame, [40, 60], [0, 1], { extrapolateRight: 'clamp' }),
              }}
            >
              {data.sub}
            </div>
          )}

          {/* 아이템 목록 */}
          <div style={{ display: 'flex', flexDirection: 'column', gap: 16 }}>
            {items.map((item, i) => {
              const itemOpacity = interpolate(frame - 30 - i * 15, [0, 15], [0, 1], {
                extrapolateRight: 'clamp',
              });
              return (
                <div
                  key={i}
                  style={{
                    display: 'flex',
                    alignItems: 'center',
                    gap: 16,
                    opacity: itemOpacity,
                    padding: '12px 16px',
                    background: COLORS.card,
                    borderRadius: 10,
                    border: `1px solid ${COLORS.cardBorder}`,
                  }}
                >
                  <span style={{ fontSize: 22 }}>{item.emoji}</span>
                  <div>
                    <div style={{ fontSize: 20, color: COLORS.text, fontFamily: 'sans-serif' }}>
                      {item.text}
                    </div>
                    {item.sub && (
                      <div style={{ fontSize: 14, color: COLORS.textMuted, fontFamily: 'sans-serif', marginTop: 2 }}>
                        {item.sub}
                      </div>
                    )}
                  </div>
                </div>
              );
            })}
          </div>
        </div>
      </AbsoluteFill>

      <Audio src={staticFile(data.audioSrc)} />
    </AbsoluteFill>
  );
};
