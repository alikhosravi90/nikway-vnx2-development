# NVX2.ai — Research Evidence Package

**Status:** Research baseline / proposed architecture; not an implementation approval.  
**Date:** 2026-11-07  
**Scope:** Clean-slate, provider-neutral reference architecture, 36 capabilities across 9 responsibility domains.

## Purpose

Preserve literature discovery, evidence links, scientific limitations and architectural implications for all 36 NVX2.ai capabilities. No assumption about existing NIKWAY systems, vendors, deployment topology, or operational readiness is introduced. This folder is a standalone research artifact hosted in a development repository; its location does not imply product or technology dependency.

## Evidence snapshot

- Original coverage: 36 capability-to-paper associations, one candidate study per capability.
- Supplementary research: 15 article associations for four previously under-supported capabilities.
- Combined selections: **48 distinct article IDs** (some supplementary articles already appear in the baseline).
- Preliminary strength labels: **15 Strong / 17 Medium / 4 Limited**. These are screening judgments, not formal quality scores or proof of fitness.
- All 36 have at least one relevant candidate; no claim of production readiness or validated architecture.
- Litmaps graph was visualized but **not saved** because workspace access returned HTTP 401; related-article expansion returned HTTP 403.

## Contents

1. [36-capability evidence matrix](36-capability-evidence.md)
2. [Four-gap deep research and architectural implications](four-gap-deep-dive.md)
3. [Source register](source-register.md)
4. [Architecture decisions, contracts and verification backlog](decisions-and-verification.md)

## Research integrity

Source records were discovered through Litmaps article search (Semantic Scholar-backed results). The summaries here are an initial secondary synthesis of returned titles/abstracts, not a critical full-text appraisal or systematic literature review. Verify publication metadata, peer-review status, versions, citations, retractions, methods, reproducibility and external validity before claiming design validation. Treat vendor/product names solely as study subjects/examples, never prescribed architecture.

> **Counting correction:** Prior conversational chart reported 14 Strong / 18 Medium / 4 Limited. A re-count of the explicitly labeled 36 rows gives **15 / 17 / 4**, which is used here.

## Architecture invariants (proposed)

Contract-first, independent identity and authorization, least privilege, provable provenance/evidence, human oversight proportional to action risk, failure isolation, observability, data lifecycle ownership, evolutionary boundaries, testable portability. Cross-cutting controls must be enforced at runtime, not only documented.

## Topology decision remains open

Modular, distributed and federated are valid candidate deployment patterns. The 36 items are **capabilities, not 36 required network services**. Choose service boundaries and technologies only after dependency analysis, SLO/security testing and operational cost assessment.
