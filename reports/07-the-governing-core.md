# The Governing Core

Status: public working report
Author: Njål Gaute Solland
Claim: `ACE-ORG-SIZE-01`  
Date: 2026-08-27

## Boundary correction

This simulator is not the primary organization model. The primary unit is the Governed Completion Unit (`GCU`). Required outcomes and their completion contracts are defined first. Candidate H-GCU and M-GCU configurations are then compared on quality, safety, latency, price, total resource cost and ACE demand.

Only after a GCU portfolio selects its admissible resource configurations may this diagnostic estimate the coordination cost of the human capacity that those configurations require.

Headcount must never be entered first and optimized as if humans were the production function.

## Secondary question

Given a human resource composition already derived from GCU demand, when does one integrated human coordination core consume more ACE than a federation of bounded cores?

The simulator compares integrated and federated topologies from 1 to 100 derived human units. It is a Monte Carlo sensitivity model, not empirical proof of a 50-person boundary or an organization optimizer.

## Hypotheses

- `H0`: after controlling for actual work dependencies, integrated and federated human structures have no material difference in coordination ACE.
- `H1`: coordination ACE rises with material human dependencies and reduces GCU capacity.
- `H2`: when cross-core interfaces are cheaper than internal coupling, bounded federation preserves more GCU-producing ACE.
- `H3`: there is no universal human threshold; the crossover moves with task dependencies, GCU composition, interface quality, context, authority and execution integrity.

Reject or revise the coordination bands if calibrated observations repeatedly support `H0`, if integrated cores above 50 dominate matched federations, or if federation losses exceed the coordination burden removed.

## Diagnostic model

For each trial:

`active human coordination edges ~ Binomial(possible edges, measured work coupling)`

`coordination ACE = active edges × events per edge × seconds per event`

`net GCU-supporting ACE = gross required ACE - coordination ACE`

Integrated topologies expose all possible human pairs. Federated topologies expose full edges only inside bounded cores and pay explicit cross-core interface and duplication costs.

The possible-edge equation is an upper-bound surface, not proof that every person communicates with every other person.

## Run

```bash
npm run ace:simulate > ace-organization-sweep.csv
```

The command remains available for secondary sensitivity analysis. `npm run gcu:simulate` is the primary task-first model.

## Required calibration

Measure for each GCU class and selected configuration:

- material human dependencies;
- coordination frequency and ACE-seconds;
- ACE response coverage and latency;
- sickness, leave and reserve coverage;
- cross-core interface cost;
- context loss, rework and incidents;
- valid GCUs produced and ACE-seconds consumed.

The earlier uncalibrated baseline found crossovers ranging from 17 to beyond 100 humans under different coupling assumptions. That spread is evidence that headcount cannot be the primary variable. The actual dependency and GCU portfolio must be measured first.
