# Spec Analysis: 07 - Capture

**Analysis Date**: 2026-04-07
**Source File**: `gobi-monorepo/specs/07-capture.md`
**Vibe Guiding Relevance**: ⭐⭐⭐ Core

---

## Summary

Capture is the primary gateway through which new information enters the Brain. Voice recordings, notes, ambient brainstorming, and sensor data are collected with low friction, and agents automatically process and structure the content.

---

## Key Features

| Feature | Product | Description |
|---------|---------|-------------|
| Audio Capture | Desktop | Recording → saved as MD file (YAML metadata + transcription text) |
| Ambient Canvas Brainstorming (ACB) | Desktop | Continuous speech → real-time transcription + AI-structured canvas generation |
| Quick Capture | Mobile | Fast voice/text input → automatically processed by agent |
| Share-to-Capture | Mobile | Content from other apps → share to Gobi → integrated into Brain |
| Canvas Sync | Desktop | Sync generated canvas ↔ Vault |

---

## Ambient Canvas Brainstorming (ACB) in Detail

```
User speaks freely
    ↓ Real-time transcription
    ↓ AI-structured canvas generated periodically
    ↓ Timestamps organized
    ↓ Title auto-generated
→ Saved to Vault/_Gobi_/Captures/YYYY-MM-DD-HH-MM-SS-{title}.md
```

---

## Vibe Guiding Touchpoint Analysis

### 🎯 Touchpoint 1: Real-Time Vibe Guiding During ACB Session
**Scenario**: Vibe Guiding provides relevant context in real time while the user brainstorms with ACB

```
User says "Let me think about PKM..."
        ↓ Real-time transcription
        ↓ Vibe Guiding detects: "PKM-related Brain content found"
        ↓ Side panel or TTS guidance:
"Related content: 'PKM Note from 2026-03-15' exists in your Brain."
```

**Feasibility**: ⭐⭐ Medium — requires hooking into the transcription stream + adding a Vibe Guiding layer

### 🎯 Touchpoint 2: Post-Capture Vibe Guiding Trigger
The moment a capture file is created (saved to `_Gobi_/Captures/`), an Orchestrator Reflex triggers:
```
New capture file detected (file-change Reflex)
        ↓
Vibe Guiding Agent: analyze capture content
        ↓
Provide related existing knowledge + next-action suggestions
```

**Feasibility**: ✅ High — leverages Orchestrator's file-change trigger functionality

### 🎯 Touchpoint 3: Post-Quick-Capture Vibe Guiding (Mobile)
After Quick Capture on mobile:
- "This content is related to the ○○ topic in your Brain"
- "There are 3 similar captures. Would you like to consolidate them?"

**Feasibility**: ⭐⭐ Medium — requires separate mobile Vibe Guiding implementation

---

## Vibe Guiding Design Implication

> **Capture = the most natural trigger point for Vibe Guiding**

The moment a user inputs new information is when the need for "how do I use this?" is strongest:
1. **Before** capture: Provide context on what is already known about this topic
2. **During** capture: Show related knowledge in real time (ACB)
3. **After** capture: Suggest integration / connections (Reflex)

The file save path (`_Gobi_/Captures/`) is well-defined, making it easy to configure a Watch Pattern via Orchestrator Reflex.
