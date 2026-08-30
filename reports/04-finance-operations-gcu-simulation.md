# Finance Operations GCU Simulation

Status: public working report
Author: Njål Gaute Solland
Canonical base: `0fdefd9d4ca1bdca1bcab385fed3b0d76d9bf412`  
Date: 2026-08-27

## Claim

Start from the finance completions required, account for automation already in production, then compare current delivery with governed machine completion. Human capacity and disciplinary composition are outputs.

This corrects the earlier industry model in one important way: existing ERP, e-invoice, rules, OCR and RPA are a separate producer class. AI cannot claim their completed work as new value. It can address only the remaining manual population.

## Portfolio

The first profile contains 100,000 monthly GCU across routine and exceptional invoice processing, reconciliation, expense audit, collections, close/accrual preparation and management reporting.

For every task the profile declares current automation, human handling time, remaining machine eligibility, governed completion probability, ACE demand, machine time and cost, governance and evidence cost, and expected incident loss. Human capacity is reduced explicitly for productive-time loss, sickness and leave; machine capacity is reduced for uptime and external dependencies.

## Outputs

The simulator produces conservative, base and high scenarios. It reports existing automation, incremental machine GCU, residual human GCU, current and target human FTE equivalents, ACE, cost, savings, simple payback and derived disciplinary composition.

Human seats are calculated only after completion paths are selected. Independent duty floors for accountable authority, accounting control and finance systems remain even when average work approaches zero.

## Run

```bash
npm run gcu:finance-ops
npm run gcu:finance-ops -- --scale 2
```

## Evidence boundary

The model is evidence-informed but not calibrated. External evidence supports direction and product capability:

- [Bank of England/FCA 2024 survey](https://www.bankofengland.co.uk/report/2024/artificial-intelligence-in-uk-financial-services-2024);
- [Oracle AI for Fusion Cloud Financials](https://www.oracle.com/erp/ai-financials/);
- [SAP finance AI](https://news.sap.com/2025/10/sap-connect-finance-ai-innovation/);
- [Microsoft Financial Reconciliation Agent](https://learn.microsoft.com/en-us/copilot/finance/reconcile/reconcile-data);
- [Norwegian e-invoice and digital-bookkeeping requirements](https://www.regjeringen.no/no/aktuelt/nye-lovregler-om-e-fakturering-i-naringslivet-og-enkelte-andre-lovendringer-pa-finansmarkedsomradet-settes-i-kraft/id3166726/);
- [SAF-T Financial](https://www.skatteetaten.no/en/business-and-organisation/start-and-run/best-practices-accounting-and-cash-register-systems/saf-t-financial/questions-and-answers---saf-t-financial/).

The numerical rates, volumes, handling times and costs are visible synthetic assumptions. They become calibrated only when replaced by observed data. Exposure or vendor capability is never treated as proof of governed completion.

## Falsification

The economic thesis weakens if real exception volume, retries, integration cost, ACE demand, incident loss or residual duties remove the savings; if machine paths cannot satisfy the same completion contract as humans; or if the required integrated governing core repeatedly exceeds the proposed coordination bands.
