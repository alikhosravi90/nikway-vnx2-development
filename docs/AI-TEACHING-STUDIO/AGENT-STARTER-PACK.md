# Agent Starter Pack — Mission ATS-01 (NIKWAY vNx2)

**Mode:** G0 research / design / isolated synthetic PoC only. **Authorization:** no production access; no external agent writes outside an explicitly approved feature branch; no deployment/merge; do not request or store secrets. **Status:** Proposed, not executed.

## Objective
Demonstrate a standards-governed AI tutor that teaches 5 Whys on a shared editable whiteboard and exports/replays a reliable narrative, preserving owner edits and source/evidence status.

## Entry requirements
1. Read this pack, [proposal](README.md), [contract](AGENT-CONTRACT.md), repository README/CONTRIBUTING/ARCHITECTURE and existing governance.
2. Confirm designated reviewer, available sandbox, mock model/API interface, model cost ceiling, and approved registry version before any code actions.
3. Verify upstream library licenses/security for exact pinned versions; document whether embedding and SaaS use is permitted.
4. Use only synthetic data, stub/mock APIs and public/openly licensed illustrative assets.
5. Record baseline commit, current tests, scope, and STOP conditions; never use private infrastructure details in public repository.

## Team roles (parallel research allowed, writes serialized)
- **A — Teaching/Method**: source-backed 5 Whys lesson structure; hypotheses/evidence and prompts; learning objectives and assessment.
- **B — Design/Canvas**: registry and approved component definitions; accessible Persian RTL whiteboard and layered human edits.
- **C — Contracts/Policy**: JSON-schema proposals, rights/ACL, change approvals, event ledger and conflict handling.
- **D — Playback/Media**: timestamped narration, replay/export feasibility and license/CPU cost comparison.
- **E — Independent Review**: test gates, scientific accuracy, privacy, attribution, accessibility and reproducibility.
Only the nominated integration agent may commit to a feature branch following review; no uncontrolled concurrent edits to identical files.

## Work packages (bounded)
- WP0: Evidence-backed comparison: Excalidraw vs Konva; A2UI-like registry; Manim vs Remotion; exact licenses.
- WP1: Versioned manifest with 5 Whys semantic nodes/edges, allowed templates and provenance fields.
- WP2: Typed operations + deterministic validator rejecting nonexistent components, illegal edges and locked objects.
- WP3: Minimal editable board with 6 stage views, human edit capture and agent replan based on latest state.
- WP4: Append-only event log, replay and a narrated demo (sound may be stubbed initially).
- WP5: Automated tests, manual UAT, threat/privacy/media-rights checks and independent decision record.

## Synthetic golden scenario
Late delivery -> production delay -> machine stop -> preventive maintenance missed -> no maintenance plan -> ownership unclear. **Every causal step is a question/hypothesis until supported by evidence.** The agent asks the learner to inspect evidence before finalizing causes. User changes "maintenance missed" to "maintenance plan absent"; the revised scene remains stable. A locked object modification is denied. Playback can reconstruct accepted steps. No actual factory/customer diagnosis is implied.

## Required acceptance tests
| ID | Check | PASS condition |
|---|---|---|
| T01 | Template | Versioned 5 Whys component IDs resolve, no invented primitive |
| T02 | Scientific reasoning | Unsupported cause remains hypothesis; conflicting evidence presented |
| T03 | Human override | Human edit retained after agent continues; locked element untouched |
| T04 | Validation | Malformed, unauthorized, cross-tenant and stale-revision ops rejected |
| T05 | Event trace | Replaying the same committed events gives equal semantic state |
| T06 | Media | Narration cue/scene mapping reproducible; export works in sandbox |
| T07 | Licensing | Dependency and media licenses documented; no unattributed restricted asset |
| T08 | Usability | Persian RTL, mobile pen/touch, keyboard, captions and reduced-motion reviewed |
| T09 | Security | No secrets, real data or live infra changes; denied tool calls audited |
| T10 | Feasibility | Measured cost, latency, resource use, backup/recovery and stop rules reported |

## STOP rules
Stop on missing owner authorization; real/private data discovered; privileged production access requested; unknown asset rights; unsafe third-party license; unauthorized cross-tenant operation; nondeterministic destructive replay; budget overrun; unreviewed change to the baseline. Escalate rather than work around.

## Deliverables
- Source-backed benchmark and license inventory;
- semantic model and versioned approved catalog;
- proposed schema and operation examples;
- tiny, synthetic, local-only prototype (subject to separate approval);
- tests and screenshots/video evidence where possible;
- independent PASS/FAIL report, ADR choices and reviewed Draft PR.
No fixed delivery date or production-readiness claim is authorized.

## Agent kickoff prompt
> Mission ATS-01: Read docs/AI-TEACHING-STUDIO/README.md and AGENT-CONTRACT.md plus repository contribution and architecture rules. Work in research/design mode first. Prepare a scoped synthetic 5 Whys visual teaching pilot with a versioned standards registry, typed drawing operations, conflict-safe human edits, evidence status, and replayable narration. Benchmark exact upstream licenses and self-hosting. Do not change production, identity, infrastructure, real data or secrets. Do not merge. Produce tests, an independent review packet and a GO/NO-GO recommendation; request explicit owner authorization before executable PoC or deployment.
