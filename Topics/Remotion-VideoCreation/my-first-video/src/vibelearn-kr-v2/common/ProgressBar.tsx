import { useCurrentFrame } from 'remotion';

interface ProgressBarProps {
  durationInFrames: number;
  color: string;
}

export const ProgressBar: React.FC<ProgressBarProps> = ({ durationInFrames, color }) => {
  const frame = useCurrentFrame();
  const progress = Math.min(1, frame / durationInFrames);

  return (
    <div
      style={{
        position: 'absolute',
        bottom: 0,
        left: 0,
        width: '100%',
        height: 4,
        background: 'rgba(255,255,255,0.06)',
      }}
    >
      <div
        style={{
          height: '100%',
          width: `${progress * 100}%`,
          background: color,
          boxShadow: `0 0 10px ${color}, 0 0 4px ${color}`,
        }}
      />
    </div>
  );
};
