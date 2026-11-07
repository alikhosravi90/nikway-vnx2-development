# NIKWAY vNx2 — AI Teaching Studio (proposal v0.1)
Status: **PROPOSED / documentation-only / NO-GO production** · 2026-11-07

## Product intent
Build a commercially viable, self-hosted visual teaching studio embedded in NIKWAY: an AI teacher explains a lesson, draws on a persistent shared whiteboard one approved element at a time, accepts human pen/text/layer edits, and produces a replayable, narrated lesson. Initial lesson: evidence-aware **5 Whys** (late customer delivery). The earlier concept collage is a **visual reference only**, not implementation or verified UI; no binary image is embedded in this public document.

## Experience
1. Owner selects a versioned method/template, learning outcome, audience and example.
2. Teaching agent drafts a lesson plan, structured concepts, permitted visual primitives and narration cues.
3. Validator checks permissions, schema, semantic relationships, evidence status, source licenses and tenant isolation.
4. Whiteboard renders each approved command; learner can pause, annotate, move items, lock layers or propose revisions.
5. Human edits become first-class versioned events; agent observes the updated *semantic state* before proposing next changes.
6. Timeline records drawing, narration and user actions separately; export is deterministically replayed and optionally rendered to MP4.

## Architecture boundaries
- **Teaching Orchestrator**: instructional strategy, lesson pacing, questions, adaptive explanations; provider-neutral LLM via API.
- **Standards Registry**: versioned approved components/method templates, source references, ownership, license and validation rules.
- **Semantic Lesson Model**: typed nodes/edges, hypotheses vs evidence, provenance, linked lesson objectives and stable element IDs.
- **Validator/Policy Gate**: fail-closed, schema checks, semantic constraints, immutable/locked elements, rights/ACL and review.
- **Agent Tool Gateway**: strictly typed commands; no direct arbitrary JS/HTML/SQL, network calls or unrestricted canvas writes.
- **Whiteboard UI**: self-hosted Excalidraw **candidate**, accessible mobile/desktop experience, human editing, snapshots.
- **Event Store & Playback**: ordered validated operations, branching/undo, event IDs, narration timestamps and audit history.
- **Export**: Manim/Remotion **candidates**, separate rendering process, license/fee review and media-rights tracking.

A2UI is an interface-contract/catalog **reference**, not an assertion that its components implement the semantic whiteboard. tldraw is a benchmark; assess its commercial license before selecting. Excalidraw does not automatically provide semantic validation or synchronized step-level playback. No third-party tool or API has been installed or tested by this PR.

## Scientific and content governance
- Distinguish official standards, established methods, NIKWAY internal conventions and user preferences; do not conflate authority.
- 5 Whys is an investigative technique, not proof of one root cause. Allow uncertainty, multiple causal branches and disconfirming evidence.
- Use synthetic examples; never imply a fictional diagnosis is validated against real operational evidence.
- Registry entries include ID, version, allowed composition, type constraints, author/owner, upstream citation, permission/license and review state.
- Images/references need provenance, attribution where required, permitted use/reproduction and retention fields; a citation alone is not a commercial license.
- AI must not override human-locked elements; conflicting edits stop for approval and can be reverted.
- Accessibility: Persian RTL and English LTR; responsive controls, keyboard/screen-reader, captions, reduced-motion and color contrast.

## Proposed baseline and alternatives
| Layer | Initial candidate | Alternative | Decision gate |
|---|---|---|---|
| Shared canvas | Excalidraw (MIT; verify exact upstream release) | Konva / SVG | Human editing, stable IDs, schema adapter, mobile |
| Declarative UI | Internal typed registry inspired by A2UI | A2UI renderer | License, integration maturity, security |
| Tutor/model | Provider-neutral API | Other model API | Reasoning, Persian quality, cost/latency |
| Animation/video | Manim (MIT) | Remotion (license review) | Replay fidelity, narrative sync, render cost |
| Backend | Existing NIKWAY APIs/contracts | Isolated local service | Isolation, identity, audit, restore |

## Pilot acceptance gates
- G0: Owner approves method sources, permitted asset licenses, scope and AI spend ceiling.
- G1: One synthetic lesson; six repeatable stages; approved registry version and schema; invalid action rejected.
- G2: Manual move/edit and locked-element conflict handled; undo and agent resumption without destroying edits.
- G3: Evidence labels and source references accurate, including ‘hypothesis’ vs ‘verified’.
- G4: Replaying identical approved events reconstructs identical semantic state; capture/export tests.
- G5: Narration sync, caption/RTL/mobile usability, accessibility, security, cost and deployment feasibility reviewed.
- G6: Independent reviewer signs PASS/FAIL evidence; only then propose production architecture.

## Non-goals
No autonomous deployment, production configuration, credentials, private customer data, unapproved writes, forced adoption of any vendor SDK, or guarantee of scientific truth from an LLM. No merge/deploy authorization implied.

See [agent contract](AGENT-CONTRACT.md) and [starter pack](AGENT-STARTER-PACK.md).
