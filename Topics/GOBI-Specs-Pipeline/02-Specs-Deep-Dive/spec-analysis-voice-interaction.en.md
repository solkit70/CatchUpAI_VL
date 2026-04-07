# Spec Analysis: 06 - Voice Interaction

**Analysis Date**: 2026-04-07
**Source File**: `gobi-monorepo/specs/06-voice-interaction.md`
**Vibe Guiding Relevance**: ⭐⭐⭐ Core

---

## Summary

Voice is a first-class input method in GOBI. A complete voice stack including STT/TTS/VAD/Wake Word/Ambient Mode. **Ambient Mode** in particular is the most natural channel for Vibe Guiding.

---

## Key Features

| Feature | Description |
|---------|-------------|
| STT | Local Whisper / Google Cloud Speech / extensible architecture |
| TTS | Kokoro (local) / OpenAI / ElevenLabs / Google Cloud TTS |
| VAD | SmartTurn daemon, automatic voice activity detection start/stop |
| Wake Word | Configurable trigger word, detected by SmartTurn daemon |
| Sleep Word | Deactivation trigger word |
| Voice Modes | Push-to-Talk / Continuous / Ambient / Manual |
| Pre-roll Buffer | ~500ms buffer (captures audio immediately before wake word) |
| Global Hotkey | Works even when the app is not in focus |

---

## Ambient Mode in Detail (Core Vibe Guiding Channel)

```
Microphone always active (passive listening)
        ↓
Wake Word detected
        ↓
Enter conversational turn-taking mode
        ↓
User speaks → STT → Agent processes → TTS response
        ↓
Silence or Sleep Word → Return to passive listening
```

---

## Vibe Guiding Touchpoint Analysis

### 🎯 Touchpoint 1: Ambient Mode + Vibe Guiding Context
**Scenario**: Vibe Guiding waits in Ambient Mode while the user works in GOBI Desktop

```
User: "How do I capture?"  (naturally, without a wake word)
        ↓
Vibe Guiding Agent (Ambient Mode):
"Open the Capture tab and press the record button.
 Speak freely — your words will be transcribed in real time,
 and AI will automatically generate a structured canvas."
```

**Feasibility**: ✅ High — Ambient Mode is already implemented. Only a Vibe Guiding-specific System Prompt needs to be added.

### 🎯 Touchpoint 2: Custom Wake Word for Vibe Guiding
Set a dedicated Vibe Guiding wake word:
- "Hey Gobi, help" → Activate Vibe Guiding mode
- Deliver contextual guidance based on the current feature or screen

**Feasibility**: ⭐⭐ Medium — Wake Word itself works; Vibe Guiding routing needs to be added

### 🎯 Touchpoint 3: TTS-Delivered Vibe Guiding
Vibe Guiding text guidance → TTS → spoken to the user
- User can receive guidance without looking at the screen
- Guidance can be requested during multitasking

**Feasibility**: ✅ High — TTS infrastructure is complete

---

## Vibe Guiding Design Implication

> **Ambient Mode = the natural UX channel for Vibe Guiding**

Currently, Ambient Mode routes to the general Second Brain Agent. Routing it to a Vibe Guiding agent — or including Vibe Guiding context in the system prompt — completes voice-based Vibe Guiding.

The **Pre-roll Buffer (~500ms)** ensures the first word of the user's help request is never missed — directly contributing to voice interface quality for Vibe Guiding.
