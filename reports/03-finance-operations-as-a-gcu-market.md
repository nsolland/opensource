# Finance Operations as a GCU Market

Status: public market thesis  
Author: Njål Gaute Solland  
Date: 2026-08-30

## Thesis

Finance operations is a strong first market for Governed Completion Units (GCU) because the work contains large volumes of digital completions with explicit acceptance criteria, existing evidence and visible exception paths.

The target is not “automate finance.” The target is a portfolio of specific completions.

## Candidate GCU classes

Examples include:

- invoice exception resolution;
- transaction reconciliation;
- expense-policy exception handling;
- collections preparation and follow-up;
- close and accrual preparation;
- management-report preparation;
- document validation;
- evidence assembly for review.

Each class requires its own completion contract.

## Why this market is attractive

Finance operations has several useful properties:

1. inputs are largely digital;
2. outputs are often deterministic or bounded;
3. evidence already exists in ledgers, bank records, invoices and policy;
4. exceptions are visible;
5. consequences can be staged before final execution;
6. existing automation provides a baseline.

## Existing automation must be credited correctly

ERP, e-invoicing, OCR, rules engines and RPA already complete substantial work.

AI should not claim these completions as new value.

The relevant comparison is:

```text
current automated completion
+
current human completion
vs.
incremental machine completion
+
residual human completion
```

## The first useful wedge: exceptions

The high-value starting point is often not extraction. It is exception completion.

A reconciliation exception may require:

```text
collect evidence
→ identify candidate correction
→ test acceptance conditions
→ escalate ambiguity
→ execute accepted correction
→ observe result
→ record evidence
```

The machine creates value by converting an unresolved exception into a completed outcome.

## Commercial unit

The commercial model can move from:

```text
software seat
or
consulting hour
```

toward:

```text
price per accepted completion
```

That gives buyer and supplier a clearer unit of value.

## Human role

Humans remain necessary where:

- evidence is incomplete;
- alternatives are ambiguous;
- consequence is material;
- authority is not already bounded;
- judgment or accountability cannot be delegated.

The objective is not zero humans. It is minimum necessary human attention per valid completion.

## What should be measured

For each GCU class:

- monthly required volume;
- current automation share;
- current human handling time;
- remaining machine eligibility;
- valid completion probability;
- escalation probability;
- human evaluation seconds;
- retry rate;
- evidence cost;
- incident cost;
- time to completion;
- cost per valid GCU.

## Falsification

The market thesis weakens if real exception rates, integration cost, human review demand, rework or incident loss consistently remove the economic advantage of machine-first completion.
