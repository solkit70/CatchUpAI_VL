import { AbsoluteFill, useCurrentFrame, useVideoConfig } from 'remotion';
import { COLORS } from '../data';

const KEYWORDS = [
  'Python', 'React', 'AI', 'ML', 'Claude', 'GitHub', '학습', '성장',
  'TypeScript', 'API', 'Remotion', 'VibeLearn', '실습', '산출물',
  'WorkLog', 'Roadmap', 'Node.js', '데이터', '영상', '문서화',
  '체계', '지식', 'GPT', '자동화',
];

// 각 키워드의 위치/속도/페이즈 (의사랜덤 분포)
const KW_CONFIG = KEYWORDS.map((kw, i) => ({
  text: kw,
  x: 3 + (i * 17.3 + 5) % 90,
  y: 3 + (i * 13.7 + 7) % 90,
  size: 12 + (i % 4) * 2,
  phaseX: (i * 1.13) % (Math.PI * 2),
  phaseY: (i * 0.73) % (Math.PI * 2),
  speed: 0.25 + (i % 5) * 0.1,
  opPhase: (i * 0.91) % (Math.PI * 2),
}));

interface FloatingKeywordsProps {
  sectionColor?: string;
}

export const FloatingKeywords: React.FC<FloatingKeywordsProps> = ({
  sectionColor = COLORS.primary,
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  return (
    <AbsoluteFill style={{ pointerEvents: 'none', overflow: 'hidden' }}>
      {KW_CONFIG.map((kw, i) => {
        const t = frame / fps;
        const dx = Math.sin(t * kw.speed + kw.phaseX) * 2.5;
        const dy = Math.cos(t * kw.speed * 0.7 + kw.phaseY) * 1.8;
        const opacity = 0.06 + Math.abs(Math.sin(t * 0.25 + kw.opPhase)) * 0.05;

        return (
          <div
            key={i}
            style={{
              position: 'absolute',
              left: `${kw.x + dx}%`,
              top: `${kw.y + dy}%`,
              fontSize: kw.size,
              color: sectionColor,
              fontFamily: 'sans-serif',
              fontWeight: 600,
              opacity,
              userSelect: 'none',
              whiteSpace: 'nowrap',
              letterSpacing: 1,
            }}
          >
            {kw.text}
          </div>
        );
      })}
    </AbsoluteFill>
  );
};
