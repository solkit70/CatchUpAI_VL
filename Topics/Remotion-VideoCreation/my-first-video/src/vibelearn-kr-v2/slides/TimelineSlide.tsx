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

const MODULE_COLORS = [COLORS.primary, COLORS.accent, COLORS.green];

interface TimelineSlideProps {
  data: SlideData;
  durationInFrames: number;
}

export const TimelineSlide: React.FC<TimelineSlideProps> = ({ data, durationInFrames }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const items = data.items || [];
  const sectionColor = SECTION_COLORS.casestudy;

  const headerOpacity = interpolate(frame, [0, 20], [0, 1], { extrapolateRight: 'clamp' });
  const fadeOut = interpolate(frame, [durationInFrames - 15, durationInFrames], [1, 0], {
    extrapolateRight: 'clamp',
  });

  const lineWidth = interpolate(frame, [20, 60], [0, 100], { extrapolateRight: 'clamp' });

  return (
    <AbsoluteFill style={{ opacity: fadeOut }}>
      <AnimatedBgV2 sectionColor={sectionColor} intensity={0.3} />

      <AbsoluteFill
        style={{
          display: 'flex',
          flexDirection: 'column',
          padding: '60px 120px',
          gap: 48,
        }}
      >
        <div style={{ opacity: headerOpacity, display: 'flex', alignItems: 'center', gap: 16 }}>
          {data.emoji && <span style={{ fontSize: 36 }}>{data.emoji}</span>}
          <div>
            <div style={{ fontSize: 40, fontWeight: 800, color: COLORS.text, fontFamily: 'sans-serif' }}>
              {data.title}
            </div>
            <div style={{ width: 80, height: 3, background: sectionColor, marginTop: 8, borderRadius: 2 }} />
          </div>
        </div>

        <div style={{ position: 'relative', flex: 1, display: 'flex', alignItems: 'center' }}>
          <div
            style={{
              position: 'absolute',
              top: '50%',
              left: 0,
              width: `${lineWidth}%`,
              height: 3,
              background: `linear-gradient(90deg, ${MODULE_COLORS[0]}, ${MODULE_COLORS[1]}, ${MODULE_COLORS[2]})`,
              transform: 'translateY(-50%)',
              boxShadow: `0 0 12px ${sectionColor}66`,
            }}
          />

          <div style={{ display: 'flex', justifyContent: 'space-between', width: '100%', position: 'relative' }}>
            {items.map((item, i) => {
              const DELAY = 25 + i * 20;
              const nodeSpring = spring({ frame: frame - DELAY, fps, config: { damping: 14, stiffness: 80 } });
              const nodeOpacity = interpolate(frame - DELAY, [0, 20], [0, 1], { extrapolateRight: 'clamp' });
              const color = MODULE_COLORS[i];

              return (
                <div
                  key={i}
                  style={{
                    display: 'flex',
                    flexDirection: 'column',
                    alignItems: 'center',
                    gap: 24,
                    opacity: nodeOpacity,
                    transform: `scale(${0.7 + nodeSpring * 0.3})`,
                    width: '30%',
                  }}
                >
                  {i % 2 === 0 && (
                    <div
                      style={{
                        background: `${color}15`,
                        border: `2px solid ${color}`,
                        borderRadius: 16,
                        padding: '20px 24px',
                        textAlign: 'center',
                        boxShadow: `0 0 20px ${color}22`,
                        minHeight: 130,
                        display: 'flex',
                        flexDirection: 'column',
                        gap: 8,
                      }}
                    >
                      <div style={{ fontSize: 28 }}>{item.emoji}</div>
                      <div style={{ fontSize: 22, fontWeight: 700, color, fontFamily: 'sans-serif' }}>{item.text}</div>
                      <div style={{ fontSize: 15, color: COLORS.textMuted, fontFamily: 'sans-serif' }}>{item.sub}</div>
                    </div>
                  )}

                  {i % 2 === 0 && <div style={{ width: 2, height: 30, background: color }} />}

                  <div
                    style={{
                      width: 48,
                      height: 48,
                      borderRadius: '50%',
                      background: color,
                      display: 'flex',
                      alignItems: 'center',
                      justifyContent: 'center',
                      fontWeight: 900,
                      fontSize: 18,
                      color: COLORS.bg,
                      fontFamily: 'sans-serif',
                      boxShadow: `0 0 16px ${color}`,
                      zIndex: 1,
                    }}
                  >
                    ✓
                  </div>

                  {i % 2 !== 0 && <div style={{ width: 2, height: 30, background: color }} />}

                  {i % 2 !== 0 && (
                    <div
                      style={{
                        background: `${color}15`,
                        border: `2px solid ${color}`,
                        borderRadius: 16,
                        padding: '20px 24px',
                        textAlign: 'center',
                        boxShadow: `0 0 20px ${color}22`,
                        minHeight: 130,
                        display: 'flex',
                        flexDirection: 'column',
                        gap: 8,
                      }}
                    >
                      <div style={{ fontSize: 28 }}>{item.emoji}</div>
                      <div style={{ fontSize: 22, fontWeight: 700, color, fontFamily: 'sans-serif' }}>{item.text}</div>
                      <div style={{ fontSize: 15, color: COLORS.textMuted, fontFamily: 'sans-serif' }}>{item.sub}</div>
                    </div>
                  )}
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
