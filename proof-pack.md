# Document AI JSON QA Proof Pack

Public, rewritten examples. No real invoices, contracts, IDs, forms, or client records are included.

## Example 1: Invoice Extraction QA

**Source summary:** Invoice INV-2048 from Northline Office Supplies to Greenvale Services. Invoice date: 2026-04-12. Due date: 2026-05-12. Subtotal: 1250.00. Tax: 93.75. Total: 1343.75. Currency: USD.

**Model output excerpt:**

```json
{
  "invoice_id": "INV-2048",
  "due_date": "2026-04-12",
  "vendor": { "name": "Greenvale Services" },
  "customer": { "name": "Northline Office Supplies" },
  "line_items": [
    { "description": "Printer paper", "line_total": 450.00 },
    { "description": "Toner cartridge", "line_total": 850.00 }
  ],
  "subtotal": 1250.00,
  "tax": 93.75,
  "total": 1343.75
}
```

| Field | Model output | Expected | Error type | Severity |
| --- | --- | --- | --- | --- |
| due_date | 2026-04-12 | 2026-05-12 | Semantic error | High |
| vendor.name | Greenvale Services | Northline Office Supplies | Entity swap | High |
| customer.name | Northline Office Supplies | Greenvale Services | Entity swap | High |
| line_items[1].line_total | 850.00 | 800.00 | Math-integrity error | High |

**Reviewer note:** The final total is correct, but the line item is wrong, creating internal inconsistency. Vendor/customer reversal is also high severity because it changes document meaning.

## Example 2: Insurance Claim Form QA

**Source summary:** Claimant Amara Cole. Policy POL-77821. Incident date 2026-03-18. Claim type: Auto damage. Estimated repair cost: 2480.00 USD. Signature present: Yes.

**Model output excerpt:**

```json
{
  "claimant_name": "Amara Cole",
  "policy_number": "POL-77821",
  "incident_date": "2026-03-18",
  "claim_type": "Medical",
  "estimated_repair_cost": 2480,
  "currency": "USD",
  "signature_present": false
}
```

| Field | Model output | Expected | Error type | Severity |
| --- | --- | --- | --- | --- |
| claim_type | Medical | Auto damage | Semantic error | High |
| signature_present | false | true | Semantic error | High |
| estimated_repair_cost | 2480 | 2480.00 | Formatting | Low |

**Reviewer note:** Claim type and signature fields are decision-impacting. The amount is numerically correct but may still need normalization if the schema requires currency precision.
