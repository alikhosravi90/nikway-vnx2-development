# ATS-01 — governed design review and ADR-001

Status: **design proposal; G1 research/design only; production NO-GO**. Reviewed 2026-11-07 against [PR #4](https://github.com/alikhosravi90/nikway-vnx2-development/pull/4), its three ATS documents, repository `README.md`, `CONTRIBUTING.md`, and `docs/ARCHITECTURE.md`. Baseline commit `d54c12aa0b0d37a0a391704c38e680facb88e568`. No runtime, model, media export, or commercial integration was tested.

## ADR-001: semantic lesson ledger with a replaceable visual renderer

**Decision (proposed):** Store lesson meaning, evidence status, approvals, and ordered operations in a tenant-scoped semantic model and append-only event ledger. Project committed state to a whiteboard adapter. The tutor proposes typed changes; an authenticated gateway and deterministic policy/semantic validator decide; a human approves the exact diff when required. A renderer cannot define scientific truth or bypass locks. Start evaluation with Excalidraw as canvas candidate, an internal allowlisted component registry, and a separate export adapter. Use Manim as an initial export evaluation candidate; retain Remotion as a licensed alternative.

**Why:** The public repository calls for contract-first, domain-modular, portable design and strong tenant isolation. PR #4 correctly requires human ownership, revision checks and semantic replay. The graphics SDK alone cannot provide these invariants. Separate models allow renderer replacement and provider-neutral AI APIs.

**Alternatives:** (1) tldraw for rich editing: production license is a commercial decision. (2) Konva/SVG custom editor: greater control but larger accessibility/editor build. (3) Penpot as runtime: strong design authoring and self-hosting, but plugin write access and editor scope are a poor default for constrained tutoring. (4) Remotion video: strong React composition, but proprietary commercial terms require legal and budget review. No candidate is selected for implementation.

**Consequences and decision gates:** Maintain stable IDs and schema migrations; validate semantic projections after human graphical edits; isolate rendering from authorization; pin renderer, fonts, assets, reducer and timeline versions for media reproducibility. A product/method owner, security owner, accessibility reviewer and legal owner must accept exact versions and rights before an executable pilot.

## Evidence-backed benchmark

| Candidate | Verified upstream property | Proposed ATS role | Unresolved evaluation |
|---|---|---|---|
| [Excalidraw](https://github.com/excalidraw/excalidraw/blob/master/LICENSE), [API](https://docs.excalidraw.com/docs/%40excalidraw/excalidraw/api/props/excalidraw-api) | MIT; scene update/read/change API | provisional editable canvas adapter | mapping editor changes to typed semantics, lock reconciliation, RTL/keyboard/mobile, exact release |
| [Konva](https://konvajs.org/docs/about.html) | MIT canvas framework with object editing/serialization | custom adapter fallback | editor, accessible DOM controls and collaboration cost |
| [Penpot](https://github.com/penpot/penpot), [self-host](https://penpot.app/self-host), [plugins](https://help.penpot.app/plugins/getting-started/) | MPL-2.0 and self-hosting; plugins may request content write | component/design authoring reference | runtime fit, plugin privileges, attribution and deployment scope |
| [tldraw](https://github.com/tldraw/tldraw/blob/main/LICENSE.md) | custom license; production key and commercial terms | interaction benchmark | legal approval and exact commercial terms |
| [A2UI](https://github.com/a2ui-project/a2ui/blob/main/docs/public/index.md) | Apache-2.0 declarative component protocol | allowlist/contract inspiration | maturity, compatibility and renderer security; not a semantic whiteboard |
| [Manim](https://github.com/ManimCommunity/manim/blob/main/LICENSE.community), [Scene API](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html) | MIT; scene animation, sound and subcaptions | initial export experiment candidate | visual fidelity, Persian shaping, CPU/time, exact dependencies |
| [Remotion](https://www.remotion.dev/docs/license/pricing), [terms](https://www.remotion.dev/docs/terms) | React timeline and commercial company licensing; automator pricing currently $0.01/render with $100/month minimum for eligible company use | export alternative | entity eligibility, embedding category, license cost and renderer resources |

These are documentation findings, not installed-version attestations or fitness tests. Licenses for transitive packages, fonts, voices and media require a pinned bill of materials. A method citation does not license reproducing a publisher's template or artwork.

## Science, lesson and component catalog

[IHI](https://www.ihi.org/library/tools/5-whys-finding-root-cause) and [ASQ](https://asq.org/quality-resources/five-whys) describe 5 Whys as investigation with potentially several causes and no fixed five-question requirement. [ASQ's fishbone](https://asq.org/quality-resources/fishbone) organizes competing possible causes. [Lean Enterprise Institute](https://www.lean.org/events-training/events/introduction-to-a3-problem-solving/) connects A3/PDCA to factual cause validation. The [IES practice guide](https://ies.ed.gov/ncee/wwc/PracticeGuide/1) supports worked examples, learner practice, explanatory questions and retrieval. Author original instructional text/art; [IHI's RCA2 toolkit](https://www.ihi.org/sites/default/files/lms/legacy/education/IHIOCC_RCA2TOOLKIT.pdf) restricts commercial reproduction.

Registry record: `component_id@version`, `semantic_type`, `method_compatibility`, `allowed_parent/edge_types`, `validation_rule_version`, `owner`, `approval_state`, `source_ref`, `asset_rights_ref`, `visual_adapter`, `accessible_label`, and locale. Catalog v0: `lesson-template`, `problem-statement`, `why-question`, `cause-hypothesis`, `observation`, `supporting-evidence`, `disconfirming-evidence`, `causal-link`, `alternative-branch`, `learner-note`, `countermeasure-proposal`, `check-metric`, `source-badge`, `narration-cue`. A graphical move changes view coordinates; a text or relationship edit requires semantic validation. `verified` needs an evidence reference and designated human review authority. The design must never infer verified status from a fluent explanation.

**Synthetic six-beat storyboard (proposed; not a fixed number of Whys):** 1. Define a measurable late-delivery problem and learning objective. 2. Work one possible delay explanation, marked hypothesis. 3. Learner suggests a next question and what would support/refute it. 4. Show competing scheduling and parts-availability branches; optional fishbone view. 5. Learner edits “maintenance missed” to “plan absent”; agent reads the new semantic revision, preserves the edit, and asks for evidence. 6. Retrieval/transfer prompt: choose a discriminating test and propose a PDCA check metric. All factory details are fictional. Rubric: precise problem, observation versus hypothesis, competing explanation, evidence request per link, no blame or unique-root-cause assertion.

## Tool and human interaction contract (proposed)

`Proposal = {contract_version, request_id, lesson_id, tenant_id, workspace_id, actor, expected_revision, method_id@version, template_id@version, registry_version, operation, target_ids, typed_payload, evidence_refs, rights_refs, budget_context}`. Actor identity is authenticated by the gateway, never trusted from model text. Operations: `lesson.plan`, `scene.inspect`, `step.propose`, `element.add/update/remove`, `narration.propose`, `validation.request`, `change.review`, `playback.preview`, `export.request`. `layer.lock/unlock` is human only. The agent has no direct canvas, DB, script, network or export capability.

State flow: `PROPOSED → VALIDATED_DENY | NEEDS_REVIEW | PERMITTED → COMMITTED`; review is bound to `(proposal hash, exact diff hash, scene revision, approver, expiry)`. Gateway authorizes tenant/workspace/lesson/layer/resource **before reads**. Validator checks schema/component/method compatibility, graph references and cycles, evidence labels, rights, locks, quotas and revision. Deny by default with rule IDs and policy version. Commit performs atomic compare-and-append keyed by `request_id`; event includes monotonic sequence, actor, before/after semantic hash, policy/registry/reducer versions, approval ID and causal parent. A human edit increments revision and invalidates stale proposals. Agent must `scene.inspect` again; undo appends a compensating event. Access/denial audit and retention/redaction rules need owner approval.

## Timeline, replay and narration (proposed)

Canonical lesson ledger carries semantic operations, not pixels. Separate timeline manifest maps `step_id`, ordered event range, `element_ids`, narration text/audio asset hash, voice/locale/license, start/end in integer milliseconds, captions and pauses. Render a frozen approved revision. Enforce ordering and no overlapping exclusive cues; derive keyframes from the ledger; synchronize at cue boundaries; produce caption transcript and source credits. Semantic replay PASS means identical canonical scene hash under pinned reducer, schema and registry versions. Pixel/video equality is a separate test requiring pinned renderer, fonts, codec, assets and execution environment. Speech may be human-recorded or synthesized through a provider-neutral adapter; no specific TTS quality, voice rights or Persian accuracy is verified. Export runs only on a human-approved request with per-job duration, compute, storage and spend caps.

For self-hosted speech evaluation, the former [Piper repository](https://github.com/rhasspy/piper) is archived; the maintained [OHF-Voice fork](https://github.com/OHF-Voice/piper1-gpl) uses GPL-3.0 and voices have separate model terms. [XTTS v2 documentation](https://docs.coqui.ai/en/dev/models/xtts.html) does not list Persian among supported languages and its model terms need separate review. [FFmpeg](https://ffmpeg.org/legal.html) licensing depends on build options and codecs. None is approved for the pilot baseline. Human-recorded narration is a viable design fallback if its consent and rights are recorded.

## Security, accessibility, licensing and cost

Threats: cross-tenant read/write, prompt injection via source material, arbitrary agent tool use, stale approvals, lock bypass through raw canvas state, rights violations, malicious media and render resource exhaustion. Controls: read authorization, allowlisted typed tools, untrusted-content isolation, exact-diff approvals, server-side validation, immutable logs, media scanning/sandboxing, output quotas and audit review. Verify against [OWASP LLM guidance](https://genai.owasp.org/llmrisk/llm01-prompt-injection/) during implementation. Accessible experience requires keyboard operations and nonvisual semantic outline, screen-reader labels, focus order, Persian RTL/English LTR, captions, reduced motion, contrast and touch alternatives; target [WCAG 2.2 AA](https://www.w3.org/TR/WCAG22/), with manual assistive-technology review.

**Proposed pilot ceiling, pending owner approval:** $0 external paid API/license spend and one synthetic lesson, 3-minute maximum export, 720p maximum, one concurrent render, 1 GiB artifact cap; stop before any purchase or metered call. This is a control proposal, not measured cost. Cost model: `model tokens × provider rate + TTS seconds × rate + render CPU/GPU time × host rate + storage/egress + licensed seats/renders + engineering time`. Local compute, staff time and exact vendor pricing are UNKNOWN; Remotion's currently published company minimum is a material alternative cost. Measure latency, peak memory, render time, file size and recovery only after PoC authorization.

## Ten acceptance-test specifications (design only)

| ID | Fixture/action | Expected evidence and pass rule |
|---|---|---|
| T01 | Load approved `5-whys@version` and request unknown component | Registry resolves exact IDs; unknown rejected; manifest/version recorded |
| T02 | Add unsupported cause, competing branch, then evidence | Cause stays hypothesis; branch retained; verified promotion requires authorized review and evidence |
| T03 | Human edits cause text and locks prior layer; agent resumes | Revision increments, stale proposal denied, reinspection shown, human edit and lock preserved |
| T04 | Malformed, unauthenticated, cross-tenant, unauthorized layer, stale revision inputs | Each read/write denied before mutation; explicit rule code and audit receipt |
| T05 | Replay same event stream twice and attempt duplicate request ID | Equal canonical semantic hashes; duplicate is idempotent; corrupted ordering fails |
| T06 | Freeze lesson, narration cues, captions and export | Cue/event timestamps within agreed tolerance; short video and captions produced, rights recorded |
| T07 | Pin dependency/font/media inventory including restricted asset | Commercial terms recorded; disallowed/unknown asset blocks export |
| T08 | Persian/English desktop/mobile, keyboard, screen reader, touch, captions, reduced motion | WCAG 2.2 AA checklist and manual findings accepted by accessibility owner |
| T09 | Prompt-injected source, forged actor, direct tool call and malicious media | No privilege gained or unapproved mutation; denial/audit and safe media handling observed |
| T10 | One bounded synthetic job under approved ceiling, failure/recovery drill | Measured token/render/storage/latency/memory; cap enforced; approved state recovered |

T01–T10 are specifications, not PASS results. T06/T08/T10 need executable and manual pilot work under separate approval.

## Phases, dependencies and independent decision

1. **G1 design (this PR):** method and source review, benchmark, ADR, registry/tool/timeline contracts and test specifications. No executable prototype.
2. **G2 owner decision:** name method/product, security, accessibility and legal owners; approve exact methods, license inventory, budget and synthetic fixture. Prerequisite to code.
3. **G3 separately authorized isolated PoC:** implement minimal validator, semantic ledger, canvas adapter and synthetic editable lesson; run T01–T05 and T09.
4. **G4 media/accessibility evaluation:** authorized export adapter, narration, captions, manual UAT, T06–T08 and T10; record costs and recovery.
5. **G5 independent review:** reconcile failures, threat model, commercial rights and evidence; decide whether a later production proposal is justified. Production remains a separate authorization.

**Independent Agent E disposition: GO for governed research/design; PARTIAL as a completed design package; NO-GO for prototype/production under current authorization.** Sources support plausible components and science guardrails. No integration, accessibility, security, TTS, render, cost or replay test has run. Key unresolved decisions: named approving owners; approved method/template and evidence authority; exact dependency/font/voice/media rights; Excalidraw edit mapping and lock behavior; Persian TTS and accessibility; retention/residency; pilot ceiling; acceptable replay tolerance and deployment profile. Confidence: high in repository scope and published license statements as of review; medium in architecture feasibility; low in operational performance and cost. PR #4's starter pack says “G0” and includes PoC/test work; this mission explicitly grants G1 research/design only, so executable WP2–WP5 and acceptance execution are deferred. Its fixed six-stage example is instructional pacing, not a requirement for exactly five causal links or one root cause.

**Exact next owner action:** approve or revise the named owners, method/asset rights, proposed zero-paid-API ceiling and isolated synthetic PoC scope, then issue a separate implementation authorization. Until then, review this design Draft PR only; do not merge, deploy or run an operational prototype.
