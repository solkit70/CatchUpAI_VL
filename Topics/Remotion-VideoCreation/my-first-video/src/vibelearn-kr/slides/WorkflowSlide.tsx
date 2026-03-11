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

const STEP_COLORS = [COLORS.primary, COLORS.accent, COLORS.green, COLORS.coral];

interface WorkflowSlideProps {
  data: SlideData;
  durationInFrames: number;
}

export const WorkflowSlide: React.FC<WorkflowSlideProps> = ({ data, durationInFrames }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const items = data.items || [];
  const sectionColor = SECTION_COLORS.intro2;

  const headerOpacity = interpolate(frame, [0, 20], [0, 1], { extrapolateRight: 'clamp' });
  const fadeOut = interpolate(frame, [durationInFrames - 15, durationInFrames], [1, 0], {
    extrapolateRight: 'clamp',
  });

  return (
    <AbsoluteFill style={{ opacity: fadeOut }}>
      <AnimatedBg sectionColor={sectionColor} intensity={0.3} />

      <AbsoluteFill
        style={{
          display: 'flex',
          flexDirection: 'column',
          padding: '60px 100px',
          gap: 32,
        }}
      >
        {/* 헤더 */}
        <div
          style={{
            opacity: headerOpacity,
            display: 'flex',
            alignItems: 'center',
            gap: 16,
          }}
        >
          {data.emoji && <span style={{ fontSize: 36 }}>{data.emoji}</span>}
          <div style={{ fontSize: 40, fontWeight: 800, color: COLORS.text, fontFamily: 'sans-serif' }}>
            {data.title}
          </div>
        </div>

        {/* 워크플로우 단계 */}
        <div style={{ display: 'flex', alignItems: 'center', gap: 0, flex: 1 }}>
          {items.map((item, i) => {
            const DELAY = 15 + i * 20;
            const stepSpring = spring({
              frame: frame - DELAY,
              fps,
              config: { damping: 14, stiffness: 80 },
            });
            const stepOpacity = interpolate(frame - DELAY, [0, 20], [0, 1], {
              extrapolateRight: 'clamp',
            });
            const color = STEP_COLORS[i];
            const isLast = i === items.length - 1;

            return (
              <div
                key={i}
                style={{
                  display: 'flex',
                  alignItems: 'center',
                  flex: 1,
                  opacity: stepOpacity,
                }}
              >
                {/* 스텝 박스 */}
                <div
                  style={{
                    flex: 1,
                    background: `${color}15`,
                    border: `2px solid ${color}`,
                    borderRadius: 16,
                    padding: '28px 20px',
                    display: 'flex',
                    flexDirection: 'column',
                    alignItems: 'center',
                    gap: 12,
                    transform: `scale(${0.7 + stepSpring * 0.3}) translateY(${interpolate(stepSpring, [0, 1], [30, 0])}px)`,
                    boxShadow: `0 0 20px ${color}33`,
                  }}
                >
                  {/* 단계 번호 */}
                  <div
                    style={{
                      width: 40,
                      height: 40,
                      borderRadius: '50%',
                      background: color,
                      display: 'flex',
                      alignItems: 'center',
                      justifyContent: 'center',
                      fontSize: 18,
                      fontWeight: 800,
                      color: COLORS.bg,
                      fontFamily: 'sans-serif',
                    }}
                  >
                    {i + 1}
                  </div>

                  {/* 이모지 */}
                  <span style={{ fontSize: 32 }}>{item.emoji}</span>

                  {/* 제목 */}
                  <div
                    style={{
                      fontSize: 18,
                      fontWeight: 700,
                      color,
                      fontFamily: 'sans-serif',
                      textAlign: 'center',
                    }}
                  >
                    {item.text}
                  </div>

                  {/* 서브 */}
                  {item.sub && (
                    <div
                      style={{
                        fontSize: 14,
                        color: COLORS.textMuted,
                        fontFamily: 'sans-serif',
                        textAlign: 'center',
                        lineHeight: 1.4,
                      }}
                    >
                      {item.sub}
                    </div>
                  )}
                </div>

                {/* 화살표 */}
                {!isLast && (
                  <div
                    style={{
                      color,
                      fontSize: 28,
                      padding: '0 8px',
                      opacity: interpolate(frame - DELAY - 10, [0, 15], [0, 1], {
                        extrapolateRight: 'clamp',
                      }),
                    }}
                  >
                    →
                  </div>
                )}
              </div>
            );
          })}
        </div>

        {/* 하단 메시지 */}
        <div
          style={{
            textAlign: 'center',
            opacity: interpolate(frame, [70, 90], [0, 1], { extrapolateRight: 'clamp' }),
            fontSize: 18,
            color: COLORS.textMuted,
            fontFamily: 'sans-serif',
            fontStyle: 'italic',
          }}
        >
          "배우고 싶어" 한 마디 → AI가 Phase 1~4 전과정을 이끌어줍니다
        </div>
      </AbsoluteFill>

      <Audio src={staticFile(data.audioSrc)} />
    </AbsoluteFill>
  );
};
