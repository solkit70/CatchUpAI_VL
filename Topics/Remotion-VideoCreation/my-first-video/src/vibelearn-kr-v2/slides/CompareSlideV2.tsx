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

interface CompareSlideV2Props {
  data: SlideData;
  durationInFrames: number;
}

export const CompareSlideV2: React.FC<CompareSlideV2Props> = ({ data, durationInFrames }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const items = data.items || [];

  const sectionColorKey = (['intro', 'problem', 'intro2', 'howto', 'casestudy', 'outro'] as const)[
    data.section - 1
  ];
  const sectionColor = SECTION_COLORS[sectionColorKey];

  const headerOpacity = interpolate(frame, [0, 20], [0, 1], { extrapolateRight: 'clamp' });
  const fadeOut = interpolate(frame, [durationInFrames - 15, durationInFrames], [1, 0], {
    extrapolateRight: 'clamp',
  });

  const isTwoColumn = items.length <= 2;
  const isArrowStyle = data.id === 5;

  // 행 교대 highlight (등장 완료 후 1초씩 순환)
  const allAppearedFrame = 15 + (items.length - 1) * 18 + 30;
  const CYCLE_FRAMES = 60; // 2초 per item
  const activeRowIdx = frame >= allAppearedFrame && !isTwoColumn
    ? Math.floor((frame - allAppearedFrame) / CYCLE_FRAMES) % items.length
    : -1;

  return (
    <AbsoluteFill style={{ opacity: fadeOut }}>
      <AnimatedBgV2 sectionColor={sectionColor} intensity={0.25} />

      <AbsoluteFill
        style={{
          display: 'flex',
          flexDirection: 'column',
          padding: '60px 100px',
          gap: 32,
        }}
      >
        {/* 헤더 */}
        <div style={{ opacity: headerOpacity, display: 'flex', alignItems: 'center', gap: 16 }}>
          {data.emoji && <span style={{ fontSize: 36 }}>{data.emoji}</span>}
          <div>
            <div style={{ fontSize: 38, fontWeight: 800, color: COLORS.text, fontFamily: 'sans-serif' }}>
              {data.title}
            </div>
            <div style={{ width: 80, height: 3, background: sectionColor, marginTop: 8, borderRadius: 2 }} />
          </div>
        </div>

        {isTwoColumn ? (
          /* 2컬럼 레이아웃 (slide 20: 기본 vs 고급) */
          <div style={{ display: 'flex', gap: 32, flex: 1 }}>
            {items.map((item, i) => {
              const delay = 20 + i * 25;
              const cardSpring = spring({ frame: frame - delay, fps, config: { damping: 14, stiffness: 80 } });
              const cardOpacity = interpolate(frame - delay, [0, 20], [0, 1], { extrapolateRight: 'clamp' });
              const color = i === 0 ? COLORS.primary : COLORS.accent;
              // 카드 생동감: 부드러운 glow pulse
              const cardGlow = 20 + Math.sin((frame / fps) * Math.PI + i * Math.PI) * 10;
              return (
                <div
                  key={i}
                  style={{
                    flex: 1,
                    background: `${color}15`,
                    border: `2px solid ${color}`,
                    borderRadius: 20,
                    padding: '36px 32px',
                    opacity: cardOpacity,
                    transform: `scale(${0.8 + cardSpring * 0.2})`,
                    display: 'flex',
                    flexDirection: 'column',
                    gap: 16,
                    boxShadow: `0 0 ${cardGlow}px ${color}33`,
                  }}
                >
                  <div style={{ fontSize: 32 }}>{item.emoji}</div>
                  <div style={{ fontSize: 28, fontWeight: 700, color, fontFamily: 'sans-serif' }}>
                    {item.text}
                  </div>
                  <div style={{ width: 40, height: 2, background: color }} />
                  <div style={{ fontSize: 20, color: COLORS.text, fontFamily: 'sans-serif', lineHeight: 1.5, background: `${color}0a`, padding: '12px 16px', borderRadius: 10, fontStyle: 'italic' }}>
                    {item.sub}
                  </div>
                </div>
              );
            })}
          </div>
        ) : isArrowStyle ? (
          /* 화살표 스타일 (slide 5: 문제→해결) */
          <div style={{ display: 'flex', flexDirection: 'column', gap: 16, flex: 1, justifyContent: 'center' }}>
            {items.map((item, i) => {
              const delay = 15 + i * 18;
              const itemOpacity = interpolate(frame - delay, [0, 15], [0, 1], { extrapolateRight: 'clamp' });
              const itemX = interpolate(frame - delay, [0, 15], [-40, 0], { extrapolateRight: 'clamp' });
              const parts = item.text.split(' → ');
              const isActive = activeRowIdx === i;
              const rowGlow = isActive ? `0 0 ${15 + Math.sin(frame * 0.2) * 8}px ${COLORS.green}55` : 'none';
              return (
                <div
                  key={i}
                  style={{
                    display: 'flex',
                    alignItems: 'center',
                    gap: 16,
                    opacity: itemOpacity,
                    transform: `translateX(${itemX}px)`,
                    padding: isActive ? '4px 0' : 0,
                  }}
                >
                  <div
                    style={{
                      flex: 1,
                      padding: '14px 20px',
                      background: `${COLORS.coral}15`,
                      border: `1px solid ${isActive ? COLORS.coral : `${COLORS.coral}44`}`,
                      borderRadius: 10,
                      fontSize: 18,
                      color: COLORS.coral,
                      fontFamily: 'sans-serif',
                    }}
                  >
                    {item.emoji} {parts[0]}
                  </div>
                  <div style={{ fontSize: 24, color: COLORS.accent }}>→</div>
                  <div
                    style={{
                      flex: 2,
                      padding: '14px 20px',
                      background: `${COLORS.green}15`,
                      border: `1px solid ${isActive ? COLORS.green : `${COLORS.green}44`}`,
                      borderRadius: 10,
                      fontSize: 18,
                      color: COLORS.green,
                      fontFamily: 'sans-serif',
                      boxShadow: rowGlow,
                    }}
                  >
                    {parts[1]}
                  </div>
                </div>
              );
            })}
          </div>
        ) : (
          /* 일반 비교 목록 (slide 17) — 행 교대 highlight */
          <div style={{ display: 'flex', flexDirection: 'column', gap: 16, flex: 1, justifyContent: 'center' }}>
            {items.map((item, i) => {
              const delay = 15 + i * 18;
              const itemOpacity = interpolate(frame - delay, [0, 15], [0, 1], { extrapolateRight: 'clamp' });
              const itemX = interpolate(frame - delay, [0, 15], [-40, 0], { extrapolateRight: 'clamp' });
              const parts = item.text.split(' → VibeLearn AI로 → ');
              const hasSplit = parts.length === 2;
              const isActive = activeRowIdx === i;
              const rowGlow = isActive ? `0 0 ${12 + Math.sin(frame * 0.2) * 6}px ${COLORS.green}55` : 'none';
              return (
                <div
                  key={i}
                  style={{
                    display: 'flex',
                    alignItems: 'center',
                    gap: 16,
                    opacity: itemOpacity,
                    transform: `translateX(${itemX}px)`,
                  }}
                >
                  <div
                    style={{
                      flex: 1,
                      padding: '12px 18px',
                      background: `${COLORS.coral}15`,
                      border: `1px solid ${isActive ? COLORS.coral : `${COLORS.coral}33`}`,
                      borderRadius: 10,
                      fontSize: 17,
                      color: COLORS.coral,
                      fontFamily: 'sans-serif',
                    }}
                  >
                    {item.emoji} {hasSplit ? parts[0] : item.text}
                  </div>
                  {hasSplit && (
                    <>
                      <div style={{ fontSize: 22, color: COLORS.accent }}>→</div>
                      <div
                        style={{
                          flex: 1.5,
                          padding: '12px 18px',
                          background: `${COLORS.green}15`,
                          border: `1px solid ${isActive ? COLORS.green : `${COLORS.green}33`}`,
                          borderRadius: 10,
                          fontSize: 17,
                          color: COLORS.green,
                          fontFamily: 'sans-serif',
                          boxShadow: rowGlow,
                        }}
                      >
                        {parts[1]}
                      </div>
                    </>
                  )}
                </div>
              );
            })}
          </div>
        )}
      </AbsoluteFill>

      <Audio src={staticFile(data.audioSrc)} />
    </AbsoluteFill>
  );
};
