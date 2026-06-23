# Documentation

The logic and theory behind LLM-Wiki vaults, in three layers. Read them in order for
the full picture, or jump to the one you need.

| Document | Answers | Read it when |
|---|---|---|
| [**theory.md**](theory.md) | *Why* the contract is shaped the way it is — the design principles, their lineage in library/archival/information science, and the one tradeoff underneath them all. | You want to understand the reasoning, or are deciding whether the approach fits your problem. |
| [**architecture.md**](architecture.md) | *What* a vault is made of — the contract and template, the fleet model, the page schema, source tiers, roles vs. topics, controlled vocabulary, negative space, and sanctioned-divergence regions. | You're building or modifying a vault, or working on the tooling. |
| [**pipeline.md**](pipeline.md) | *How* content gets in — plan → ingest → review → evaluate, the supporting skills, and the human-in-the-loop gates. | You're ingesting sources, or want to understand the workflow and its safeguards. |

For a high-level overview and install instructions, see the [project README](../README.md).
For how to *use* a finished vault with an LLM, see the README's
[Using the vault](../README.md#using-the-vault) section. To contribute, see
[CONTRIBUTING.md](../CONTRIBUTING.md).

## In one paragraph

A vault is a small encyclopedia governed by a machine-read **contract**: every page has
a defined shape, every claim cites a stable surrogate record, what was deliberately
left out is recorded as first-class **negative space**, and nothing is deleted — stale
pages are archived. An LLM does the writing (so the vault is optimised for *retrieval*,
not for teaching you the way writing your own notes would), but it is never the sole
judge of its own work: an independent review runs after every chapter and a human stays
the curator. A linter and a conformance checker enforce all of it, so a fleet of domain
vaults can grow while staying findable, trustworthy, and honest about its own limits.
