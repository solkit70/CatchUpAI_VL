# GOBI Documentation Pipeline Diagram

**Created**: 2026-04-06

---

## Current Pipeline

```mermaid
flowchart TD
    A["gobi-monorepo/specs/\n(26 Markdown files)"]
    B["Developer / AI\nManual MDX conversion"]
    C["gobi-ai/docs\n(Mintlify MDX files)"]
    D["Mintlify\nAuto Build & Deploy"]
    E["docs.gobihq.com\n(User documentation site)"]

    A -->|"Manual ⚠️"| B
    B --> C
    C -->|"git push → Auto"| D
    D --> E

    style B fill:#ff9999,stroke:#cc0000
    style A fill:#ffe0b2
    style E fill:#c8e6c9
```

### Step-by-Step Details

| Step | Auto / Manual | Owner | Tool |
|------|--------------|-------|------|
| Write spec (gobi-monorepo/specs) | Manual | Dev team (Mika, Greg) + AI (CODE_TO_SPECS) | Claude Code |
| Convert specs → MDX | **Manual** ⚠️ | TBD | — |
| gobi-ai/docs push → docs.gobihq.com | Automatic | — | Mintlify |

---

## Identified Gap (Manual Conversion Step)

```
specs/05-second-brain-agent.md  ──┐
specs/06-voice-interaction.md   ──┤──► ??? ──► docs/products/desktop.mdx
specs/07-capture.md             ──┘
```

- specs are feature-centric (cross-cutting); docs are product-centric (per-product) — different structures
- Direct 1:1 mapping is not possible; restructuring is required
- **This is the opportunity for Vibe Guiding / VibeLearn AI to automate the conversion**

---

## Proposed Pipeline After Vibe Guiding Integration

```mermaid
flowchart TD
    A["gobi-monorepo/specs/\n(26 Markdown files)"]
    VL["VibeLearn AI\n(Auto conversion + user guide generation)"]
    C["gobi-ai/docs\n(Mintlify MDX)"]
    D["Mintlify Deploy"]
    E["docs.gobihq.com"]
    VG["Vibe Guiding\n(In-app real-time guidance)"]
    APP["GOBI Desktop\n/ Gobi Space App"]

    A -->|"Automatic ✅"| VL
    VL --> C
    C --> D
    D --> E
    VL -->|"Context generation"| VG
    VG -->|"Real-time guidance"| APP

    style VL fill:#b3e5fc,stroke:#0288d1
    style VG fill:#b3e5fc,stroke:#0288d1
    style A fill:#ffe0b2
    style E fill:#c8e6c9
    style APP fill:#c8e6c9
```

---

## CODE_TO_SPECS vs SPECS_TO_GUIDE

```
Current (gobi-monorepo):              Proposed (VibeLearn AI):
Code → CODE_TO_SPECS → Specs          Specs → SPECS_TO_GUIDE → User Guides
                                                              → Vibe Guiding Context
```

The dev team has already implemented the AI-driven direction of generating specs from code.
**Automating the reverse direction (specs → guides) with VibeLearn AI completes the full pipeline.**
