# Open Source

Public index for open-source work maintained, published, or forked under `nsolland`.

This repository is the map, not another runtime or product. Each linked repository keeps its own scope, status, upstream history, and license.

## VALO execution-governance stack

The public execution path is:

```text
candidate action
      |
      v
REHT
fresh admissibility / authorization at consequence time
      |
      v
RACS
deterministic decision <-> exact action binding
      |
      v
VALO Gateway
mechanical enforcement and one-shot execution
      |
      v
external consequence
      |
      v
Veritas
receipt, provenance and deterministic verification
```

- [reht-standard](https://github.com/nsolland/reht-standard) — public, model-agnostic standard for fresh execution-boundary admissibility. Apache-2.0.
- [Racs](https://github.com/nsolland/Racs) — RACS protocol/schema infrastructure for deterministic decision/action, permit and receipt bindings. Apache-2.0.
- [valo-gateway](https://github.com/nsolland/valo-gateway) — vendor-neutral reference enforcement infrastructure. Apache-2.0.
- [Veritas](https://github.com/nsolland/Veritas) — receipt, attestation and verification layer for governed actions. MIT.

These repositories are separated intentionally. Authorization, deterministic binding, enforcement, and evidence verification are distinct responsibilities.

## Open protocols and contracts

- [open-agent-contract](https://github.com/nsolland/open-agent-contract) — vendor-neutral contracts for governed agent consequence. MIT. Its canonical relationship to other VALO contract work remains explicitly unresolved in that repository.
- [peace-protocol](https://github.com/nsolland/peace-protocol) — protocol for keeping authority and authoritative state in the governed domain while models, agents, devices and providers remain replaceable. Apache-2.0.

## Research publications

- [research](https://github.com/nsolland/research) — public archive for papers, technical reports, research notes, publication controls, and selected evidence. The working laboratories and canonical experiment provenance remain separate.

## External forks and research baselines

These are upstream projects or research baselines retained as forks. Their upstream identity and license remain authoritative.

- [rlfinance-valoresearch](https://github.com/nsolland/rlfinance-valoresearch) — fork of [yhilpisch/rlfinance](https://github.com/yhilpisch/rlfinance), used as a reinforcement-learning-in-finance baseline. MIT.
- [unsloth](https://github.com/nsolland/unsloth) — fork of [unslothai/unsloth](https://github.com/unslothai/unsloth). Apache-2.0.
- [dramaclaw-gateway](https://github.com/nsolland/dramaclaw-gateway) — fork in the [QuantumNous/new-api](https://github.com/QuantumNous/new-api) lineage. AGPL-3.0.

A fork listed here is not presented as original authorship.

## Status language

Where used across these repositories:

- **standard / protocol** — interoperability or conformance surface
- **reference implementation** — executable implementation of a public contract or boundary
- **experimental / research baseline** — used to test, compare, or extend a hypothesis
- **fork** — retains upstream project identity and licensing

Repository-specific `README`, `PUBLICATION_STATUS`, `CANONICAL`, provenance, and license files take precedence over this index.

## Licensing

The contents of this `nsolland/opensource` repository are licensed under the MIT License.

Each linked repository retains its own license. The MIT license of this index does not relicense, replace, or override the license of any linked repository or upstream project.
