# NIKWAY Study Engine v0.1 (experimental)

An isolated, dependency-free Python proof of concept for guided learning. **Not deployed, not production-ready, no real users or tenant data.**

## Scope
- A versioned 5 Whys lesson with synthetic packaging-line data
- A deterministic guided question/answer loop and formative feedback
- Explicit lesson/session contracts; no AI provider is called
- Unit tests with Python standard library

## Run
```sh
python -m unittest discover -s study-engine/tests -v
python study-engine/demo.py
```

## Architecture
The teaching engine is independent of model vendors. An optional AI adapter may later provide natural-language dialogue, but must not bypass deterministic grading, source requirements, tenant authorization, or human approval. Open edX integration is **proposed**, not implemented.

## Safety / limitations
No authentication, persistence, LLM calls, RAG, or network API is implemented. In-memory sessions are a synthetic local demo only. Do not expose this module as a public service. Do not store personal information in lesson responses.

## Acceptance gates
1. Unit tests pass.
2. Curriculum/domain expert approves lesson accuracy and feedback.
3. API schema and authorization model are reviewed.
4. AI adapter is evaluated for citation fidelity, prompt injection, cost and privacy.
5. No production rollout without explicit owner approval.
