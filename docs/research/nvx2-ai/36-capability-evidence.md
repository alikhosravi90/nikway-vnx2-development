# NVX2.ai — 36 Capability Evidence Matrix

**Version:** research-baseline-1.2 | **Date:** 2026-11-07

A single candidate paper mapped to a capability is *coverage for further investigation*, not evidence that the particular design recommendation has been empirically proven. Grades are **Strong**, **Medium**, **Limited** for screening relevance; research quality appraisal remains pending.

| # | Domain | Capability | Selected literature | Screening | Research-to-design question |
|---:|---|---|---|---|---|
| 1 | Experience & Access | User Experience | [Human-centered user modeling](https://app.litmaps.com/seed/287808241) | Medium | Human-centered interaction, accessibility, and user control |
| 2 | Experience & Access | API Gateway | [Zero-trust API gateway](https://app.litmaps.com/seed/316789441) | Medium | Ingress authentication, limits, routing, enforcement |
| 3 | Experience & Access | Identity Management | [Federated identity management](https://app.litmaps.com/seed/310852413) | Medium | Users, workloads, agents and identity lifecycle |
| 4 | Experience & Access | Authorization | [Zero-trust policy enforcement](https://app.litmaps.com/seed/299933831) | Medium | Resource/action policies and least privilege |
| 5 | Agent Platform | Agent Gateway | [AI agent protocols survey](https://app.litmaps.com/seed/286735838) | Strong | Agent entry and inter-agent protocol boundaries |
| 6 | Agent Platform | Agent Registry | [Agent Name Service](https://app.litmaps.com/seed/286964270) | Medium | Discovery, identity, descriptions and version ownership |
| 7 | Agent Platform | Agent Runtime | [Agentic AI systems survey](https://app.litmaps.com/seed/320682195) | Strong | Execution isolation, lifecycle and control |
| 8 | Agent Platform | Coding Agent | [SWE-rebench](https://app.litmaps.com/seed/287797193) | Strong | Coding task evaluation and verified change |
| 9 | Agent Platform | Agent Orchestration | [Multi-agent collaboration](https://app.litmaps.com/seed/316176756) | Medium | Delegation, handoffs, failure propagation |
| 10 | Process & Composition | Workflow Orchestration | [Durable execution for agents](https://app.litmaps.com/seed/319611502) | Medium | Retries, recovery and durable process state |
| 11 | Process & Composition | Visual AI Builder | [Low-code LLM GUI](https://app.litmaps.com/seed/274073510) | Medium | Visual composition with validated export |
| 12 | Process & Composition | Tool Integration | [MCP safety audit](https://app.litmaps.com/seed/286181141) | Strong | Tool contracts, permission enforcement and risks |
| 13 | Process & Composition | Skill Management | [Agentic skills lifecycle](https://app.litmaps.com/seed/326225407) | Limited | Skill provenance, versioning, safety and portability |
| 14 | Model Intelligence | Model Gateway | [MixLLM dynamic routing](https://app.litmaps.com/seed/284958616) | Strong | Model-independent routing and selection |
| 15 | Model Intelligence | Model Providers | [ICL-Router](https://app.litmaps.com/seed/291992102) | Medium | Provider capability metadata and fallback contracts |
| 16 | Model Intelligence | Prompt Management | [Prompt-with-Me](https://app.litmaps.com/seed/291390975) | Medium | Templates, versioning and prompt evaluation |
| 17 | Knowledge & Data | Knowledge & RAG | [RAG survey](https://app.litmaps.com/seed/267704079) | Strong | Ingestion, retrieval, grounding and citations |
| 18 | Knowledge & Data | Embedding & Reranking | [Dense vector reranking](https://app.litmaps.com/seed/225543770) | Medium | Retrieval stages and ranking quality |
| 19 | Knowledge & Data | Vector Database | [Graph ANN retrieval](https://app.litmaps.com/seed/281209142) | Medium | Indexing, search quality and update semantics |
| 20 | Knowledge & Data | Agent Memory | [LLM agent memory survey](https://app.litmaps.com/seed/292987044) | Strong | Short/long memory, persistence and deletion |
| 21 | Knowledge & Data | Data Infrastructure | [Modular monolith cloud review (indirect)](https://app.litmaps.com/seed/292461389) | Limited | Broader data architecture needs direct evidence |
| 22 | Trust & Assurance | Evaluation & Testing | [Evaluation of LLM agents survey](https://app.litmaps.com/seed/289442061) | Strong | Task outcomes, regression and reliability |
| 23 | Trust & Assurance | Guardrails & Safety | [Prompt injection threat landscape](https://app.litmaps.com/seed/300276180) | Strong | Policy, untrusted content and defenses |
| 24 | Trust & Assurance | Secrets Management | [Distributed key lifecycle](https://app.litmaps.com/seed/318655201) | Limited | Credential issuance, scoping, rotation and revocation |
| 25 | Trust & Assurance | Audit & Evidence | [Agent evidence tracing survey](https://app.litmaps.com/seed/316146385) | Strong | Execution provenance and tamper-evident evidence |
| 26 | Trust & Assurance | Security Testing | [MCP Security Bench](https://app.litmaps.com/seed/291787176) | Strong | Tool abuse and red-team tests |
| 27 | Platform Engineering | Infrastructure Monitoring | [Distributed observability](https://app.litmaps.com/seed/312936830) | Medium | Hosts, system metrics, logs, alerts and SLOs |
| 28 | Platform Engineering | Containerization | [Container security survey](https://app.litmaps.com/seed/284030055) | Strong | Workload isolation and image supply chain |
| 29 | Platform Engineering | Deployment Orchestration | [Kubernetes scheduling survey](https://app.litmaps.com/seed/262682855) | Strong | Scheduling, scaling and failure recovery |
| 30 | Platform Engineering | CI/CD | [DevSecOps security controls](https://app.litmaps.com/seed/288193290) | Medium | Reproducible tests, build and release gates |
| 31 | Platform Engineering | Infrastructure as Code | [Infrastructure code practices review](https://app.litmaps.com/seed/261174767) | Strong | Reproducible, reviewed infrastructure changes |
| 32 | Operations & Economics | AI Observability | [AgentTelemetry](https://app.litmaps.com/seed/316922995) | Strong | Agent/model/tool traces, quality and failures |
| 33 | Operations & Economics | Cost Management & FinOps | [Cost-aware coding agent model routing](https://app.litmaps.com/seed/310721871) | Medium | Metering, budgets, price-performance and unit economics |
| 34 | Governance & Distribution | Multi-Tenancy | [Multi-tenant cloud security analysis](https://app.litmaps.com/seed/291032108) | Medium | Tenant isolation across data, compute and policies |
| 35 | Governance & Distribution | AI Governance | [Bridging AI risk frameworks](https://app.litmaps.com/seed/320076084) | Medium | Accountability, review, impact and change controls |
| 36 | Governance & Distribution | Portability & Federation | [Hybrid multi-cloud interoperability](https://app.litmaps.com/seed/298391428) | Limited | Export/migration and multi-node trust must be separately tested |

## Coverage integrity

- Total: 36; by domain: Experience & Access 4; Agent Platform 5; Process & Composition 4; Model Intelligence 3; Knowledge & Data 5; Trust & Assurance 5; Platform Engineering 5; Operations & Economics 2; Governance & Distribution 3.
- Grade tally: Strong 15, Medium 17, Limited 4.
- The four initial Limited capabilities were Skill Management, Data Infrastructure, Secrets Management, and Portability & Federation; each was re-researched, but formal evidence quality and acceptance gates remain pending.
- Source list contains Litmaps IDs and DOI where available; no links claim a full-text review was performed.

## Evidence appraisal gate for each capability

1. Validate bibliographic identity, publisher, article version and retraction status.
2. Identify research method (survey, experiment, case study, proposal), sample and limitations.
3. Link specific architecture claim to section/page and independently corroborate if high impact.
4. Draft contract and threat/failure assumptions; record competing approaches.
5. Define measurable acceptance criteria; run controlled technical tests before selecting a vendor.
