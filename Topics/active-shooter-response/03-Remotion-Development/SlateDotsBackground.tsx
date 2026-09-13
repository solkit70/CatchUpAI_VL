import React from 'react';
import { AbsoluteFill, useCurrentFrame } from 'remotion';

// VibeLearn AI v2.1 Learning Artifact - SlateDotsBackground Component
// This component renders the premium high-contrast Slate Charcoal ('L3' band) background
// utilizing a subtle breathing radial light glow and an SVG 40x40 dot grid pattern.

export const SlateDotsBackground: React.FC = () => {
  const frame = useCurrentFrame();

  // Low-frequency breathing movement for cool high-tech ambient light
  const t = frame / 30;
  const gX1 = 50 + Math.sin(t * 0.2) * 15;
  const gY1 = 40 + Math.cos(t * 0.15) * 12;
  const gX2 = 20 + Math.cos(t * 0.25) * 10;
  const gY2 = 70 + Math.sin(t * 0.18) * 15;

  return (
    <AbsoluteFill style={{ backgroundColor: '#161B22', overflow: 'hidden' }}>
      {/* 1. Subtle high-contrast light leaks / radial gradients (Slate Charcoal Palette) */}
      <div
        style={{
          position: 'absolute',
          inset: 0,
          background: `radial-gradient(circle at ${gX1}% ${gY1}%, rgba(24, 144, 255, 0.04) 0%, transparent 60%),
                       radial-gradient(circle at ${gX2}% ${gY2}%, rgba(255, 77, 79, 0.02) 0%, transparent 50%)`,
        }}
      />

      {/* 2. SVG 40px Dot Grid Pattern (3.5% opacity as specified in v2.1 guidelines) */}
      <svg
        width="100%"
        height="100%"
        style={{ position: 'absolute', inset: 0, pointerEvents: 'none' }}
      >
        <pattern
          id="slate-dots-pattern"
          width="40"
          height="40"
          patternUnits="userSpaceOnUse"
        >
          <circle cx="3" cy="3" r="1.5" fill="#F0F6FC" opacity="0.035" />
        </pattern>
        <rect width="100%" height="100%" fill="url(#slate-dots-pattern)" />
      </svg>
    </AbsoluteFill>
  );
};
