# BRD vs PRD Comparison

> **[← Korean Version](brd-vs-prd.md)**

## Overview

In software development, requirements documents are key to project success. BRD and PRD are two core documents with different purposes and audiences.

---

## Comparison Table

| Item | BRD (Business Requirements Document) | PRD (Product Requirements Document) |
|------|--------------------------------------|-------------------------------------|
| **Focus** | "Why" + "What" | "What" + "How" |
| **Perspective** | Business perspective | Product/technical perspective |
| **Audience** | Executives, stakeholders, investors | Dev team, designers, QA |
| **Abstraction Level** | High-level | Detailed |
| **When Written** | Early in the project | After BRD, before development |
| **Key Content** | Business goals, success metrics, stakeholder needs | Feature specs, user interactions, technical requirements |

---

## Detailed Comparison

### BRD (Business Requirements Document)

**Purpose**: Define why the project is needed for the business and what it must achieve

**Key Components**:
- Business objectives
- Stakeholder needs
- High-level requirements
- Success metrics

**Characteristics**:
- Does not cover technical implementation details
- Focuses on "why" and "what" rather than "how"
- Provides business justification for the project

**Example Questions**:
- Why is this project necessary?
- What business problem does it solve?
- How will success be measured?

---

### PRD (Product Requirements Document)

**Purpose**: Translate the BRD's business requirements into concrete product features

**Key Components**:
- Detailed feature specs
- User interactions
- Technical requirements
- Implementation details

**Characteristics**:
- Written based on the BRD
- Detailed enough for the dev team to implement directly
- Can include user stories and wireframes

**Example Questions**:
- How does a user use this feature?
- What data is needed?
- How should it behave in error conditions?

---

## Document Flow

```
[Idea / Vision]
      ↓
    [BRD]  ← Define business requirements (Why + What)
      ↓
    [PRD]  ← Elaborate on product requirements (What + How)
      ↓
[Development / Implementation]
```

---

## Importance in Vibe Coding

The importance of BRD/PRD has grown even more in the age of AI coding:

> "Clear requirements = better AI-generated code"
> — Clearly

- **Input quality = Output quality**: Clear requirements must be passed to AI for good code to be generated
- **Architect role**: The developer's role shifts from "code writer" to "architect + communicator"
- **Document reuse**: A well-written BRD/PRD can be used directly as an AI prompt

---

## Mode Selection in Clearly

| Mode | Audience | Output |
|------|----------|--------|
| **Plain Mode** | Non-technical users, business stakeholders | Prompts for AI coding tools |
| **Technical Mode** | Developers, technical teams | Sprint task lists, dependencies, priorities |

---

**Created**: 2026-02-01
**Topic**: Clearly-BRD-PRD / M1
