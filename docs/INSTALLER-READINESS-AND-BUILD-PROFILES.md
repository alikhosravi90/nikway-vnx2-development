# NIKWAY Installer Readiness and Build Profiles

**Status:** Proposed design note  
**Scope:** Public, sanitized vNx2 collaboration work  
**Purpose:** Define a safe path from NIKWAY specifications to a customer-specific installer. This document is not an implementation, deployment authorization, or production-readiness claim.

## Design intent

A deployment agent is a bounded running process that gathers environment facts, evaluates explicit rules, invokes approved tools, checks results, and reports what can proceed. A model may help interpret evidence and explain options; it does not authorize actions or establish capability by assertion.

The intended output is a reproducible installer bundle and a clear readiness report for the target environment.

## Required building blocks

1. **Versioned deployment specification**
   - Components, versions, supported platforms, dependencies, resource ranges and ports.
   - Required secrets and permissions (names and scopes only; never store secret values here).
   - Health checks, data-migration rules, backup/restore expectations and rollback boundaries.
   - Explicit definitions of full, limited and unsupported deployment.

2. **Read-only preflight assessor**
   - Collect OS/architecture, CPU, RAM, storage, container/runtime availability, installed services, network reachability and available permissions.
   - Record evidence, timestamp and uncertainty; avoid collecting customer data or secret values.
   - Produce a machine-readable capability report.

3. **Deterministic capability policy**
   - Map observed facts and test results to allowed installation steps.
   - Treat unknown or failed checks as blocked, not as permission to guess.
   - Keep authorization and safety gates outside the language model.

4. **Model and agent evaluation (optional for the first installer)**
   - Probe the selected local or hosted model for required context, structured output/tool calling, latency and task quality with a small fixed test suite.
   - Test the actual configured endpoint and enabled tools; do not infer capability from model name alone.
   - A local model can support offline operation only when the runtime, model files and all required dependencies are already available locally.

5. **Reproducible package builder**
   - Build version-pinned packages from reviewed source in a trusted build environment.
   - Generate a manifest with component versions, platform, dependencies, hashes, licenses and build provenance.
   - Sign release metadata and verify signatures and hashes before installation.
   - For air-gapped delivery, include every required package, container image, model/runtime asset and instruction in the transfer bundle; document how updates are delivered.

6. **Staged installer and verifier**
   - Run preflight, show a plan, install one bounded stage at a time, and run health checks after each stage.
   - Stop on unmet prerequisites or failed checks; support documented recovery/rollback where technically safe.
   - Emit an audit report of actions, results and unresolved items.

## Initial environment profiles

| Profile | Conditions | Expected behavior |
|---|---|---|
| **Offline / isolated** | No internet; local compute only; no remote server | Use only preloaded, verified assets. Disable features that require remote services and disclose the resulting limits. |
| **Connected / restricted** | Internet or network exists, but egress, ports or credentials are limited | Probe only approved endpoints; install only components whose dependencies and permissions are confirmed. |
| **Connected / server available** | Approved target servers and required access are available | Validate connectivity, identity and least-privilege access, then offer the wider deployment plan. |

These are test profiles, not claims that any particular customer environment is supported.

## Controlled execution loop

1. Read the signed deployment specification.
2. Gather read-only environment facts.
3. Run deterministic prerequisite and capability checks.
4. Produce a proposed plan and readiness report.
5. Require an explicit approval gate before changes with material operational impact.
6. Execute approved, allow-listed installation actions in stages.
7. Verify health, record evidence, and stop or recover when a gate fails.

## First proof of concept

Start with one small, non-production NIKWAY component and three synthetic environment profiles. Implement:

- A versioned manifest and capability-report schema.
- A read-only preflight collector.
- A deterministic ruleset with pass / fail / unknown outcomes.
- A dry-run plan and a simple staged installer.
- Health checks and an installation report.
- Offline bundle creation and hash/signature verification.

Keep model-driven planning optional until the deterministic checks and installation path are reproducible.

## Acceptance criteria

- The same inputs and package versions produce the same plan.
- Unknown prerequisites never become an automatic pass.
- Preflight makes no system changes.
- Offline installation succeeds with networking disabled after bundle delivery.
- An altered or incomplete bundle is rejected before installation.
- Failed stages stop safely and report the exact blocked prerequisite.
- The report distinguishes verified facts, model suggestions and unresolved assumptions.
- All scenarios use synthetic data and avoid secrets.

## Open decisions

- Which operating systems and CPU architectures are in the first supported scope?
- Which deployment runtime is required, optional or unsupported?
- Which NIKWAY component is the first proof-of-concept target?
- What is the supported offline update and signing-key rotation process?
- Which actions require human approval, and which are safe to run automatically?
