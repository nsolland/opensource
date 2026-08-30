# Finance Exception GCU

Status: public working report
Author: Njål Gaute Solland
Canonical base: `174a39c713539d1b7d8807cf458f4a6d0c23f75e`  
Date: 2026-08-27

## Active claim

The first useful finance GCU is not invoice extraction. It is governed completion of reconciliation exceptions: collect evidence, evaluate a bounded correction, verify fresh authority at effect time, execute through one governed effect port, observe the result, and emit a receipt.

## Boundary

The pilot is deterministic and synthetic. It does not connect to a ledger or bank, create accounting advice, or grant authority. A machine path must never produce a financial effect directly.

The implemented chain is:

`ledger + bank evidence -> deterministic evaluation -> ALLOW / DENY / ESCALATE -> governed effect port -> observed outcome -> GCU receipt`

Only a unique candidate inside the declared amount, currency, counterparty and booking-date policy can be allowed. Missing evidence and ambiguity escalate. Stale or revoked authority, prohibited actions, currency mismatch and direct machine effects deny.

## Run

```bash
npm run gcu:finance
```

The bundled five-case batch contains an exact match, a bounded variance, missing evidence, ambiguous candidates and stale authority. It reports completed GCU, decisions, governed effect calls, ACE seconds, elapsed work and cost under explicit synthetic assumptions.

## Acceptance

- exact and policy-bounded matches may reach the governed effect port;
- missing evidence or ambiguous candidates escalate;
- stale authority and prohibited actions deny;
- attempted direct effects fail closed;
- only an observed accepted effect with complete evidence measures one GCU;
- the batch exposes completion, escalation, denial, time, cost and ACE demand.

## Not yet claimed

The synthetic economics are not market evidence. The next calibration input is a real anonymized reconciliation-exception sample with observed handling time, exception reason, disposition, retries, loss, authority path and outcome evidence.
