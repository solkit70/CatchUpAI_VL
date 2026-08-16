# Original FDE vs AI FDE Comparison

## Comparison Table

| Dimension | Palantir-Style FDE | AI-Era FDE |
|---|---|---|
| Primary Product | Data/operations platform | LLMs, AI applications, developer tools, agent platforms |
| Customer Problem | Operational data and decision workflows | AI adoption inside real business processes |
| Technical Core | Data modeling, platform configuration, integration | APIs, RAG, agents, evals, observability, security boundaries |
| Deployment Context | Government, defense, finance, large enterprise | AI labs, startups, enterprise AI, public sector, developer tools |
| Success Signal | Operational use of platform | Production AI workflow adoption |
| Feedback Loop | Field workflow becomes platform pattern | Customer AI use case becomes product/eval/deployment signal |

## What Did Not Change

The core FDE pattern remains the same:

- work close to the customer
- understand the real workflow
- build or adapt technical systems
- handle ambiguity and constraints
- drive usage, not just demos
- bring field learnings back to the product

## What Changed

AI FDE roles add new layers of complexity:

- model behavior is uncertain
- evals become central to quality control
- data privacy and permission boundaries are more visible
- hallucination and trust must be managed
- latency and cost affect adoption
- human-in-the-loop design is often required

## Example: Same Pattern, Different Technology

| Step | Palantir-Style Example | AI FDE Example |
|---|---|---|
| Discovery | Understand how analysts investigate cases | Understand how support teams triage tickets |
| Data Work | Map fragmented operational data | Prepare ticket history, policies, and customer metadata |
| Build | Configure platform workflows | Build RAG or classification workflow |
| Deploy | Put tool into analyst operation | Pilot AI assistant with support agents |
| Measure | Track operational decisions enabled | Track triage time, routing accuracy, and override rate |
| Feedback | Generalize workflow into platform feature | Improve prompts, evals, connectors, or product UX |

## Candidate Implication

Candidates should not say only "I know AI tools." A stronger FDE narrative is: "I can enter a messy customer workflow, identify the adoption blocker, build a technical solution under constraints, measure whether it works, and convert the field learning into a reusable pattern."

## Summary

Palantir-style FDE and AI-era FDE share the same deployment philosophy. The customer problem comes first, technical implementation follows, and product feedback closes the loop. The AI era changes the stack, not the underlying need for forward deployed engineering.

