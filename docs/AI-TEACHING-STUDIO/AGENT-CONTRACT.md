# AI Teaching Studio — Agent & Canvas Contract v0.1 (DRAFT)

**Status:** proposed, not executed. The JSON examples are illustrative contracts, not validated implementations.

## Mission and actors
- **Owner/learner** can author, annotate, approve, reject and lock specific layer/object IDs.
- **Teaching agent** proposes teaching steps, narration and drawing operations; it cannot bypass policy.
- **Validator** deterministically decides which operations may be committed; scientific claims require grounded evidence or explicit uncertainty.
- **Renderer** draws only committed approved operations; **Recorder** persists immutable event history and safe snapshots.
- **Reviewer** independently checks quality, security, scientific integrity and rights before release.

## Inputs
`lesson_id`, `tenant_id`, `method_id@version`, `standards_registry_version`, `scene_revision`, `actor_identity`, `approved_assets`, `evidence_refs`, `audience`, `locale`, `budget_limit`.

## Allowed actions (explicit tool allowlist)
`lesson.plan`, `scene.inspect`, `element.add`, `element.update`, `element.remove`, `layer.lock` (human only), `narration.propose`, `step.propose`, `validation.request`, `change.review`, `playback.preview`, `export.request` (human approval required).

**NO** free-form executing scripts, filesystem access, arbitrary remote URLs, direct DB writes, production mutations, secrets retrieval, privilege escalation or unreviewed publishing.

## Proposal envelope example
```json
{
  "contract_version": "0.1",
  "request_id": "synthetic-req-001",
  "lesson_id": "synthetic-5why-001",
  "tenant_id": "synthetic-tenant",
  "actor": {"kind": "agent", "id": "teaching-agent"},
  "expected_scene_revision": 4,
  "method": {"id": "5-whys", "version": "draft-1"},
  "operation": "element.add",
  "target": {"layer_id": "analysis", "element_id": "cause-02"},
  "payload": {
    "kind": "cause",
    "text": "Preventive maintenance was not scheduled",
    "status": "hypothesis",
    "parent_id": "cause-01",
    "visual_component_id": "cause-box@1"
  },
  "citations": [],
  "requires_human_approval": true
}
```

## Validation invariants
1. Authenticate actor; authorize tenant, workspace, operation, layer and resource before reading or mutating.
2. Every command uses a known versioned schema, registered component, operation and compatible method version.
3. `expected_scene_revision` mismatch -> **reject/conflict**; never silently overwrite human edits.
4. A locked layer/object cannot be changed by an agent; human unlock requires logged authorization.
5. Parent references must exist, edge types and causal relationships must be permitted and acyclic where appropriate.
6. A claim without evidence remains `hypothesis`; do not auto-promote it to `verified`.
7. Referenced external text/images must have provenance and permitted rights; if unverified, omit or quarantine.
8. The validator emits an explicit permit/deny/review reason and validation version; deny defaults to no mutation.
9. Commit appends an idempotent event exactly once per `request_id`; do not replay side effects twice.
10. Human approval covers only the reviewed diff and revision, never future blanket authorization.

## Review and event format
```json
{
  "event_id": "evt-0005",
  "lesson_id": "synthetic-5why-001",
  "revision": 5,
  "timestamp": "2026-11-07T00:00:00Z",
  "actor": {"kind": "human", "id": "synthetic-user"},
  "action": "element.update",
  "element_id": "cause-02",
  "before_hash": "example-before",
  "after_hash": "example-after",
  "approval_id": "human-review-05",
  "standards_version": "draft-1",
  "validation": {"status": "pass", "policy_version": "draft-1"}
}
```

## Narration & replay contracts
- Each instruction can reference `step_id`, `element_ids`, `voice_segment_id` and normalized start/end timestamps.
- Rendering is derived from committed operations, not uncontrolled image re-generation.
- Playback determinism means equivalent **semantic scene state** across runs; pixel/video equality requires separate locked dependencies, fonts, timing and rendering tests.
- Preserve RTL shaping, captions, source attribution and human-authored contributions.
- Export requires an authorized human request, reviewed media assets and an execution cost cap.

## Failure and escalation
Unauthorized action / missing source license / conflicting revision / unsupported component / invalid semantics / exceeded budget -> fail closed; preserve last approved state, display a concise reason and offer a reviewed alternative. Production and identity changes are out of scope.

## Ownership and review
Proposed owners: NIKWAY Product Owner (scope), Knowledge/Method Owner (science), Design-System Owner (components), Security Owner (policy/identity), Technical Owner (runtime), Independent Reviewer (evidence). Named accountable owners and formal policy must be assigned before implementation.
