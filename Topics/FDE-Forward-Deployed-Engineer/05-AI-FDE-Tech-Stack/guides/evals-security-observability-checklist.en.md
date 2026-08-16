# Evals, Security, and Observability Checklist

## Why This Checklist Matters

AI prototypes often look impressive but fail in production. FDEs must think beyond the demo. Three areas matter especially: evals, security boundaries, and observability.

## Evals Checklist

- [ ] Define the user task clearly.
- [ ] Create a small golden dataset of representative inputs.
- [ ] Include normal, edge, and failure cases.
- [ ] Define what a good answer means.
- [ ] Track citation accuracy if retrieval is used.
- [ ] Track classification or routing accuracy if decisions are made.
- [ ] Define human review thresholds.
- [ ] Log model failures and categorize them.
- [ ] Re-run evals after prompt, model, or retrieval changes.

## Security Checklist

- [ ] Identify sensitive data types.
- [ ] Define who can access which data.
- [ ] Avoid sending unnecessary sensitive data to the model.
- [ ] Use role-based access control where relevant.
- [ ] Keep audit logs for important actions.
- [ ] Define escalation for high-risk outputs.
- [ ] Confirm retention and deletion requirements.
- [ ] Separate demo data from production data.
- [ ] Document customer-specific compliance constraints.

## Observability Checklist

- [ ] Log user request metadata.
- [ ] Track model response, tool calls, and retrieval sources.
- [ ] Capture latency and cost.
- [ ] Track user feedback and overrides.
- [ ] Monitor error rates and fallback usage.
- [ ] Store examples of bad outputs for eval improvement.
- [ ] Create a dashboard for adoption and quality metrics.
- [ ] Define owner and escalation path for incidents.

## Common Failure Modes

| Failure | Symptom | Mitigation |
|---|---|---|
| Hallucination | Answer not supported by data | Require citations, add evals, use human review |
| Bad retrieval | Correct answer exists but is not found | Improve chunking, metadata, query rewrite |
| Permission leak | User sees data they should not see | Add auth filtering before retrieval |
| Low adoption | Users try once and stop | Improve workflow fit and training |
| High cost | Usage grows beyond budget | Add caching, routing, smaller model options |
| Slow response | Workflow becomes unusable | Optimize retrieval, streaming, async tasks |

## FDE Interview Use

When asked how to productionize an AI workflow, do not stop at "build a RAG app." Say:

1. I would define the workflow and success metric.
2. I would build a constrained prototype.
3. I would create evals before rollout.
4. I would enforce data and permission boundaries.
5. I would monitor quality, latency, cost, and user feedback.
6. I would use field failures to improve the product or deployment pattern.

