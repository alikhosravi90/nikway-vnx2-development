# Contract-first boundary — proposal v0.1

## Current implemented interface
- `Session(session_id)`: in-memory local session, no identity verification
- `question()`: current step id, prompt and answer options; returns null after completion
- `submit(selected_index)`: validates integer choice, records feedback and advances once
- `snapshot()`: JSON-compatible session state; conforms conceptually to `contracts/study-session.schema.json` (automated JSON Schema validation not yet wired)
- `score()`: formative result only, never a credential

## Proposed future HTTP API (NOT implemented)
- `POST /v1/study/sessions`: create session with lesson reference and authorized tenant context
- `GET /v1/study/sessions/{id}/next`: read next step
- `POST /v1/study/sessions/{id}/answers`: submit answer with idempotency key
- `GET /v1/study/sessions/{id}/progress`: read progress with authorization

## Integration contracts to review
- Identity: verified OIDC subject, tenant isolation and role-based access; never trust caller-supplied tenant IDs.
- Knowledge: source IDs, revisions, provenance and license flags for instructional claims.
- Academy/Open edX: opt-in course linkage and completion events; do not claim integration exists.
- Insight: separate formative learning signals from validated organizational assessments.
- Improvement: learner-approved transfer of evidence to an improvement case.
- AI gateway: provider-neutral interface, request budgets, source validation, refusal on unsupported claims, prompt-injection boundaries.
- Teaching Studio: versioned board operations, explicit user approval, undo and provenance.

## Decisions / gates
D01 license for original public contributions; D02 learning-data retention/consent; D03 tenant/auth policy; D04 API/event versions; D05 pedagogical review; D06 model-provider cost and privacy. All OPEN.
No secrets, production credentials, real personal data, deployment, or private infrastructure access.
