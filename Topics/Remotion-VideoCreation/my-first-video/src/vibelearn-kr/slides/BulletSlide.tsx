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

interface BulletSlideProps {
  data: SlideData;
  durationInFrames: number;
}

export const BulletSlide: React.FC<BulletSlideProps> = ({ data, durationInFrames }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const items = data.items || [];
  const sectionColor = SECTION_COLORS[
    (['intro', 'problem', 'intro2', 'howto', 'casestudy', 'outro'] as const)[data.section - 1]
  ];

  // 헤더 등장
  const headerSpring = spring({ frame, fps, config: { damping: 16, stiffness: 100 } });
  const headerOpacity = interpolate(frame, [0, 20], [0, 1], { extrapolateRight: 'clamp' });

  // 아웃트로 페이드
  const fadeOut = interpolate(frame, [durationInFrames - 15, durationInFrames], [1, 0], {
    extrapolateRight: 'clamp',
  });

  return (
    <AbsoluteFill style={{ opacity: fadeOut }}>
      <AnimatedBg sectionColor={sectionColor} intensity={0.25} />

      <AbsoluteFill
        style={{
          display: 'flex',
          flexDirection: 'column',
          padding: '80px 120px',
        }}
      >
        {/* 헤더 */}
        <div
          style={{
            display: 'flex',
            alignItems: 'center',
            gap: 16,
            marginBottom: 48,
            opacity: headerOpacity,
            transform: `translateY(${interpolate(headerSpring, [0, 1], [30, 0])}px)`,
          }}
        >
          {data.emoji && <span style={{ fontSize: 40 }}>{data.emoji}</span>}
          <div>
            <div
              style={{
                fontSize: 42,
                fontWeight: 800,
                color: COLORS.text,
                fontFamily: 'sans-serif',
              }}
            >
              {data.title}
            </div>
            <div
              style={{ width: 80, height: 3, background: sectionColor, marginTop: 8, borderRadius: 2 }}
            />
          </div>
        </div>

        {/* 아이템 리스트 */}
        <div style={{ display: 'flex', flexDirection: 'column', gap: 20 }}>
          {items.map((item, i) => {
            const STAGGER = 18;
            const itemFrame = frame - 20 - i * STAGGER;
            const itemSpring = spring({
              frame: itemFrame,
              fps,
              config: { damping: 18, stiffness: 100 },
            });
            const itemOpacity = interpolate(itemFrame, [0, 15], [0, 1], {
              extrapolateRight: 'clamp',
            });
            const itemX = interpolate(itemSpring, [0, 1], [-60, 0]);

            return (
              <div
                key={i}
                style={{
                  display: 'flex',
                  alignItems: 'flex-start',
                  gap: 20,
                  opacity: itemOpacity,
                  transform: `translateX(${itemX}px)`,
                  padding: '16px 20px',
                  background: COLORS.card,
                  border: `1px solid ${COLORS.cardBorder}`,
                  borderRadius: 12,
                  borderLeft: `3px solid ${sectionColor}`,
                }}
              >
                {item.emoji && (
                  <span style={{ fontSize: 28, lineHeight: 1, minWidth: 36 }}>
                    {item.emoji}
                  </span>
                )}
                <div>
                  <div
                    style={{
                      fontSize: 22,
                      color: COLORS.text,
                      fontFamily: 'sans-serif',
                      fontWeight: 500,
                      lineHeight: 1.4,
                    }}
                  >
                    {item.text}
                  </div>
                  {item.sub && (
                    <div
                      style={{
                        fontSize: 16,
                        color: COLORS.textMuted,
                        fontFamily: 'sans-serif',
                        marginTop: 4,
                      }}
                    >
                      {item.sub}
                    </div>
                  )}
                </div>
              </div>
            );
          })}
        </div>
      </AbsoluteFill>

      <Audio src={staticFile(data.audioSrc)} />
    </AbsoluteFill>
  );
};
