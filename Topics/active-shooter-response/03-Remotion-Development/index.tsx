import React from 'react';
import { Composition } from 'remotion';
import { ActiveShooter0908 } from '../../../AI/RemotionStudio/src/active-shooter-0908/ActiveShooter0908';
import { TOTAL_FRAMES } from '../../../AI/RemotionStudio/src/active-shooter-0908/data';

// VibeLearn AI v2.1 Learning Artifact - Remotion Registration Index Backup
// This file serves as a blueprint of how the ActiveShooter0908 composition was registered 
// in the root of the Remotion project with its corresponding dimensions, FPS, and durations.

export const ActiveShooterVideoRegister: React.FC = () => {
  return (
    <>
      {/* 1. Active Shooter Response Civilian Emergency Training Composition */}
      <Composition
        id="ActiveShooter0908"
        component={ActiveShooter0908}
        durationInFrames={TOTAL_FRAMES} // Automatically binding total frames dynamically from data.ts
        fps={30}
        width={1920}
        height={1080}
      />
    </>
  );
};
