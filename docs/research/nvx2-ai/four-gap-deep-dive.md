# NVX2.ai — Four-Gap Research Deep Dive

**Date:** 2026-11-07 | **Scope:** literature-derived hypotheses; technology selection deferred.

## A. Skill Management

Sources: [Agentic skills lifecycle](https://app.litmaps.com/seed/326225407), [Skill Constellations / supply chain](https://app.litmaps.com/seed/331845735), [ClawHub scanner disagreements](https://app.litmaps.com/seed/314190809), [SkillFab lifecycle](https://app.litmaps.com/seed/316962994), [Anything2Skill](https://app.litmaps.com/seed/314831137), [AgentHub](https://app.litmaps.com/seed/302623466).

**Research insight:** A skill may bundle instructions, executable scripts, references and tool relationships; copy-based distribution complicates provenance and revocation. Scanner verdicts can disagree. This is not merely prompt storage.

**Proposed capability decomposition:** (1) skill manifest/schema and owner; (2) immutable content digest, version and origin; (3) discovery/catalog and dependency declarations; (4) signed/reviewed publication; (5) permissions, isolation and approval gates at execution; (6) usage telemetry, deprecation, rollback and revocation.

**Initial contracts:** SkillManifest (id, version, digest, origin, owner, required privileges, dependencies, input/output, tests, license, status); SkillExecutionRequest (principal, tenant, purpose, approved scope, trace_id); SkillExecutionEvidence (artifact digests, result, policy decision, tool calls).

**Threats:** skill poisoning, hidden remote dependencies, exfiltration, confused-deputy privileges, copied vulnerable content, malicious upgrades.

**Acceptance tests:** same digest reproducibly loads; changed content invalidates approval; revoked skill cannot run; sensitive tool calls require authorization; provenance remains traceable across copies.

**Open question:** what skills are declarative-only vs executable, and which trust tiers apply? Research signal improved, but no implementation candidate is approved.

## B. Data Infrastructure

Sources: [AI-ready data infrastructure](https://app.litmaps.com/seed/287838899), [AI-driven Data Mesh](https://app.litmaps.com/seed/281953008), [AI-CRM patterns](https://app.litmaps.com/seed/288199047). Existing baseline paper [modular monolith cloud](https://app.litmaps.com/seed/292461389) is **indirect**, not primary data architecture evidence.

**Research insight:** Operational records, files, events, retrieval indexes, audit evidence and lineage have different consistency, lifecycle and query needs. Vector storage is only one component.

**Proposed logical services (not necessarily separate databases):** Transactional State; Object/Document Storage; Event Transport/Journal; Search/Vector Indexes; Evidence Store; Metadata Catalog/Lineage. Define data ownership, classification, durability, backup, deletion and retention independent of storage engines.

**Initial contracts:** DataAsset (asset_id, tenant, owner, classification, version, source, retention, consent_basis); EventEnvelope (event_id, schema_version, producer, timestamp, idempotency_key, trace_id); DatasetExport (schema, manifest, digests, redaction policy, provenance); DeletionReceipt (scope, indexes, artifacts, completion status).

**Threats:** cross-tenant leakage through indexes, event replay, partial deletion, lost provenance, stale retrieval, uncontrolled replication.

**Acceptance tests:** tenant-isolation for relational/file/vector search; restore and replay with idempotency; lineage from generated answer to original source; deletion/retention applied to derived indexes; stable schema export/import.

**Open question:** Data Mesh, Lakehouse, CQRS or simpler modular storage remain alternatives, not predetermined choices.

## C. Secrets Management

Sources: [Full lifecycle distributed key management](https://app.litmaps.com/seed/318655201), [Zero Trust O-RAN survey](https://app.litmaps.com/seed/294591819), [Automated TLS certificate lifecycle](https://app.litmaps.com/seed/286410912).

**Research insight:** Encryption at rest does not constitute a complete secrets capability; issuance, authenticated access, scope, rotation, expiry, revocation, auditing and compromise response matter.

**Proposed capabilities:** credential issuance/lease; workload identity binding; per-tenant/provider policy; short-lived token exchange; non-exportable keys where appropriate; rotation and revocation; audit with redaction; emergency disable and recovery.

**Initial contracts:** SecretLease (secret_ref, workload_identity, purpose, audience, permitted_scope, issued_at, expires_at, revocable_id); PolicyDecision (subject, resource, action, context, outcome); RotationEvent (secret_ref, old/new version references, effective_at, rollback window).

**Threats:** shared permanent credentials, logging secrets, prompt/tool leakage, overprivileged agents, stale secret copies, unsafe fallback.

**Acceptance tests:** expired/revoked credential denied; agent cannot access secret outside scoped identity; no secrets appear in logs/traces; rotation does not require restarting unrelated workloads; loss/compromise test exercises revocation and recovery.

**Open question:** whether a centralized vault, federated vault or workload-local KMS is appropriate is a deployment-dependent decision.

## D. Portability & Federation

Sources: [Cloud lock-in systematic review](https://app.litmaps.com/seed/40747202), [Portability-driven government cloud architecture](https://app.litmaps.com/seed/313562228), [Hybrid multi-cloud interoperability model](https://app.litmaps.com/seed/298391428).

**Research insight:** portability (move/reconstruct deployment) and federation (secure collaboration among independent deployments) are **distinct contracts**. Standards and infrastructure abstractions do not automatically eliminate semantic lock-in.

**Portability boundary:** release artifact + dependency manifest + infrastructure/environment specification + config and secret references + data/metadata export + restore procedure + automated compatibility tests.

**Federation boundary:** independent node identity; trust establishment; service discovery; versioned event/API interoperability; consent/authorization per exchange; data residency constraints; revocation and disconnected operation.

**Initial contracts:** DeploymentManifest (version, capabilities, dependencies, runtime constraints); ExportBundle (format, schema, digests, ownership, retention, portability exclusions); FederationHandshake (node_id, trust metadata, protocol version, permitted domains); FederationEvent (origin, tenant, authority, classification, purpose, expiry).

**Threats:** hidden provider lock-in, incompatible exported data, trust confusion, cross-border leakage, replay, federated privilege escalation.

**Acceptance tests:** independent clean-room restore on a second environment; backup/export integrity; full-function and policy parity checks; independently revocable federation link; network partition and reconnection recovery; no implicit cross-node authority.

**Open questions:** federation topology, interoperability standards and country-specific legal requirements must be decided using actual deployment scenarios.

## Conclusions and caveats

- All four gaps now have **more directly relevant research**. They are not thereby certified as Strong: peer review, evidence quality, operational feasibility and independent replication remain open.
- Treat each architecture recommendation as a **candidate ADR**, not a selected product or implementation order.
- Prioritize hands-on verification of (a) skill provenance and revocation, (b) derived-data deletion and recovery, (c) credentials scoped to agents, and (d) clean-room migration plus federation trust revocation.
