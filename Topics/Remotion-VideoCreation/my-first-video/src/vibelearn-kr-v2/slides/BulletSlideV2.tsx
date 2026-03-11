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

interface BulletSlideV2Props {
  data: SlideData;
  durationInFrames: number;
}

export const BulletSlideV2: React.FC<BulletSlideV2Props> = ({ data, durationInFrames }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const items = data.items || [];
  const sectionColor = SECTION_COLORS[
    (['intro', 'problem', 'intro2', 'howto', 'casestudy', 'outro'] as const)[data.section - 1]
  ];

  const headerSpring = spring({ frame, fps, config: { damping: 16, stiffness: 100 } });
  const headerOpacity = interpolate(frame, [0, 20], [0, 1], { extrapolateRight: 'clamp' });

  const fadeOut = interpolate(frame, [durationInFrames - 15, durationInFrames], [1, 0], {
    extrapolateRight: 'clamp',
  });

  const STAGGER = 18;
  // 모든 아이템이 등장 완료되는 프레임
  const allAppearedFrame = 20 + (items.length - 1) * STAGGER + 30;
  // 활성 highlight 사이클 (2초 = 60프레임씩)
  const CYCLE_FRAMES = 60;
  const activeIdx = frame >= allAppearedFrame
    ? Math.floor((frame - allAppearedFrame) / CYCLE_FRAMES) % items.length
    : -1;

  return (
    <AbsoluteFill style={{ opacity: fadeOut }}>
      <AnimatedBgV2 sectionColor={sectionColor} intensity={0.25} />

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
            <div style={{ fontSize: 42, fontWeight: 800, color: COLORS.text, fontFamily: 'sans-serif' }}>
              {data.title}
            </div>
            <div style={{ width: 80, height: 3, background: sectionColor, marginTop: 8, borderRadius: 2 }} />
          </div>
        </div>

        {/* 아이템 리스트 */}
        <div style={{ display: 'flex', flexDirection: 'column', gap: 20 }}>
          {items.map((item, i) => {
            const itemFrame = frame - 20 - i * STAGGER;
            const itemSpring = spring({ frame: itemFrame, fps, config: { damping: 18, stiffness: 100 } });
            const itemOpacity = interpolate(itemFrame, [0, 15], [0, 1], { extrapolateRight: 'clamp' });
            const itemX = interpolate(itemSpring, [0, 1], [-60, 0]);

            const isActive = activeIdx === i;
            // pulse: 0.5초 사이클로 border glow 강도 변화
            const pulseIntensity = isActive ? 0.5 + Math.sin(frame * 0.2) * 0.5 : 0;
            const activeBorder = isActive
              ? `3px solid ${sectionColor}`
              : `1px solid ${COLORS.cardBorder}`;
            const activeGlow = isActive
              ? `0 0 ${20 * pulseIntensity}px ${sectionColor}66`
              : 'none';
            const activeBg = isActive
              ? `${sectionColor}12`
              : COLORS.card;

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
                  background: activeBg,
                  border: activeBorder,
                  borderRadius: 12,
                  borderLeft: isActive ? `4px solid ${sectionColor}` : `3px solid ${sectionColor}`,
                  boxShadow: activeGlow,
                  transition: 'box-shadow 0.1s',
                }}
              >
                {item.emoji && (
                  <span style={{ fontSize: 28, lineHeight: 1, minWidth: 36 }}>{item.emoji}</span>
                )}
                <div>
                  <div style={{ fontSize: 22, color: COLORS.text, fontFamily: 'sans-serif', fontWeight: 500, lineHeight: 1.4 }}>
                    {item.text}
                  </div>
                  {item.sub && (
                    <div style={{ fontSize: 16, color: COLORS.textMuted, fontFamily: 'sans-serif', marginTop: 4 }}>
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
