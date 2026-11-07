# NVX2.ai — Candidate Architecture Decisions and Verification Plan

**State:** PROPOSED / NOT APPROVED. Evidence baseline 1.2. No production changes authorized.

## Separation of concerns

The 36 capabilities form 9 responsibility domains; they do **not** imply 36 microservices. The baseline architecture is technology-neutral, vendor-neutral and deployment-neutral. Cross-cutting security/governance/tenant/observability controls may be shared without concentrating all business responsibilities in a single service.

## Cross-domain contracts (v0.1 candidate)

| Contract | Minimum fields | Must test |
|---|---|---|
| Request | request_id, identity, tenant, purpose, trace_id | auth propagation, idempotency |
| Agent | agent_id, version, owner, capabilities, permitted tools | registry version and revocation |
| Model | model_capabilities, modalities, budget, safety class | provider substitution and fallback |
| Tool | name, version, JSON schema, side effects, policy class | deny-by-default, action authorization |
| Skill | skill_id, digest, origin, version, permissions, tests | tamper detection, approval lifecycle |
| Knowledge | asset_id, origin, classification, version, citations | retrieval provenance and deletion |
| Execution | run_id, state, attempt, cancellation, compensation | crash/restart recovery |
| Evidence | trace_id, source_refs, artifact hashes, review_status | replay and retention |
| Policy | policy_id, version, subject, resource, action, decision | deny/permit reproducibility |
| Export/Import | schema_version, origin, manifests, checksums | cold restore |
| Federation | node identity, trust, protocol, scope, consent | trust revoke and isolation |
| Secret Lease | workload_id, audience, purpose, scope, expiry | expiry, revocation, no disclosure |

## ADR backlog

| ID | Candidate decision (no option selected yet) | Evidence/acceptance gate |
|---|---|---|
| ADR-001 | Modular vs distributed vs federated execution | dependency matrix, operational cost, failure boundaries |
| ADR-002 | Agent runtime boundary and isolation | sandbox attack/failure tests, workload identity |
| ADR-003 | Agent orchestration vs durable workflow orchestration | crash recovery, dedup, compensation |
| ADR-004 | Skills as immutable reviewed artifacts | signature/digest, revoke, provenance |
| ADR-005 | Multi-modal data ownership and storage patterns | retention, tenant isolation, backup/restore |
| ADR-006 | Credentials and secret lease delivery | short-lived scope, rotation, egress controls |
| ADR-007 | Model/provider neutrality with routing | portability, quality/latency/cost budgets |
| ADR-008 | Trust/evidence and evaluation lifecycle | traces, eval quality and auditable records |
| ADR-009 | Tenant data isolation controls | negative tests for relational/object/vector/event |
| ADR-010 | Deployment portability contract | second-environment clean-room restore |
| ADR-011 | Federation trust contract | mutual authentication, node revocation, partition |
| ADR-012 | Governance and FinOps controls | policy review, cost controls, anomaly response |

## Verification sequences

### Gate G0 — research validation
- [ ] Verify DOI, dates, publication venue and retraction status.
- [ ] Assess research quality and limitations, distinguish academic evidence from proposals.
- [ ] Add independent corroborating studies for high-impact decisions.
- [ ] Rebuild citation network when Litmaps access works.

### Gate G1 — architecture contracts
- [ ] Provide inputs, outputs, errors, ownership and versioning for all 36 capabilities.
- [ ] Trace data flows and trust boundaries.
- [ ] Produce dependency diagram and coupling matrix.
- [ ] Conduct threat and failure analysis by capability.

### Gate G2 — controlled evidence
- [ ] Skill provenance mutation + malicious skill + revocation tests.
- [ ] Data lifecycle, tenant leakage, derived index deletion and restore/replay.
- [ ] Secret expiry, rotation, credential leak prevention.
- [ ] Offline migration and federation link revocation.
- [ ] LLM/task accuracy, tool safety, trace consistency, latency, cost and recovery tests.

### Gate G3 — architecture decision
- [ ] Summarize technical validity, operational sustainability and unresolved risks separately.
- [ ] Approve ADRs individually; reject vendor selection without reproducible evidence.
- [ ] No deployment or production write until separate authorization and acceptance gates.

## Status

Literature discovery completed at initial coverage level; implementation and compliance validation remain **NO-GO / UNTESTED**. Nothing in this package is a security certification, a completed system implementation, an engineering readiness claim, or authorization to deploy.
