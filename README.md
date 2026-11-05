# NIKWAY vNx2 — Development Collaboration

**NIKWAY — The Way of Continuous Betterment**

This is a public, sanitized collaboration repository for prototyping, open-source integration research, documentation and development contributions to the NIKWAY ecosystem.

> **Status:** Early design and community development. This repository is **not** a production deployment, does not contain the private enterprise platform, and does not grant access to private systems.

## Product vision
Help individuals and organizations transform knowledge into capability, capability into action, and action into measurable improvement.

## Conceptual product areas
- **Platform:** Knowledge, Insight, Improvement, Capability and AI-assisted workflows.
- **Academy:** Learning and workshops; Open edX is the selected LMS candidate for integration.
- **Tools:** Reusable open-source Lean, quality, process, statistics and project tools.
- **Store:** Digital and physical improvement kits and materials.
- **Community:** Peer learning, expert networks and shared practice.
- **Consulting & Marketplace:** Professional services and partner offerings.

## Architectural direction
- Reuse open-source software before building custom alternatives.
- Domain-modular services and contract-first APIs; avoid premature microservices.
- Portable container deployment: cloud, economical production and offline/local profiles.
- Optional AI through a provider-neutral gateway.
- Strong tenant isolation, privacy, role-based authorization, evidence and recoverability.
- Independent logical resource pools for Tools, Knowledge, Academy and Store.
- No claims of operational readiness without testing.

## Proposed open-source ecosystem
Frappe / ERPNext, Open edX, Temporal, Keycloak, React / Next.js, Python, OpenTelemetry and compatible OSS tools. All dependencies are candidates until license, security and integration checks pass.

## Get involved
Start with [CONTRIBUTING.md](CONTRIBUTING.md), [architecture overview](docs/ARCHITECTURE.md) and [starter backlog](docs/STARTER-BACKLOG.md).

## Security and confidentiality
**Do not submit** credentials, API keys, tokens, real customer records, private infrastructure details, internal IPs, proprietary source files or copied private repository history. Use synthetic test data. Report vulnerabilities privately to repository maintainers, not in public issues.

## Licensing
No blanket license is granted for the NIKWAY brand, private platform or future proprietary assets. Individual third-party dependencies retain their own licenses. A license for original contributions must be selected and documented before accepting code contributions.
