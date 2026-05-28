# Document AI JSON QA

This repository demonstrates how to review AI-extracted JSON against source documents in finance, insurance, legal, and administrative contexts. The examples are experience-derived and public-facing; no real client documents or private datasets are included.

## QA Focus Areas

- Schema validity
- Field placement
- Missing or extra fields
- Math integrity
- Date, amount, and currency consistency
- Entity matching
- Source traceability
- Regulatory or compliance markers
- Formatting and normalization

## Error Taxonomy

| Error Type | Description |
| --- | --- |
| Semantic error | Extracted value does not match the source meaning |
| Structural error | Value is placed in the wrong object, array, or field |
| Consistency error | Related fields disagree with each other |
| Formatting error | Value format does not meet schema expectations |
| Omission | Required source value is missing |
| Hallucination | Output includes a value not present in the source |
| Math-integrity error | Totals, subtotals, taxes, or balances do not reconcile |

## Included Files

- `qa-checklist.md`: review checklist for document extraction QA
- `sample-error-taxonomy.md`: public error taxonomy for finance/legal document AI

## Confidentiality Standard

All examples are rewritten for public use and do not contain real client files, screenshots, invoices, contracts, or source documents.


---

# Document AI JSON QA Checklist

## Pre-Review

- Confirm the expected schema version.
- Identify the document type: invoice, statement, insurance form, legal record, HR document, or administrative record.
- Note high-risk fields such as totals, dates, names, IDs, signatures, policy terms, and compliance markers.

## Field-Level Review

- Confirm each extracted value appears in the source document.
- Check that values are assigned to the correct field.
- Verify dates, currencies, amounts, names, addresses, and identifiers.
- Confirm optional fields are handled consistently.
- Flag hallucinated values not present in the source.

## Structure Review

- Validate required objects and arrays.
- Check line-item grouping.
- Confirm nested values are placed under the right parent object.
- Ensure no fields are duplicated across incompatible sections.

## Math Review

- Recalculate subtotals, taxes, discounts, fees, and final totals.
- Compare line-item totals against document totals.
- Flag rounding issues separately from true extraction errors.

## Risk Review

- Identify fields with legal, financial, insurance, or compliance impact.
- Escalate errors that could affect eligibility, payment, auditability, or decision-making.

## Feedback Format

**Field:**  
**Observed output:**  
**Source value:**  
**Error type:**  
**Severity:**  
**Correction:**  
**Reviewer note:**


---

# Sample Error Taxonomy for Document AI QA

## Semantic Errors

The extracted value is present but interpreted incorrectly.

Example: a policy expiration date is extracted as an issue date.

## Structural Errors

The value is correct but appears in the wrong JSON location.

Example: a vendor address is placed under the customer object.

## Consistency Errors

Two or more fields conflict.

Example: the invoice total says one amount while line items reconcile to another.

## Formatting Errors

The value is correct but violates schema or normalization rules.

Example: date format is `25/05/2026` when schema expects `2026-05-25`.

## Omissions

A required value from the source document is missing.

Example: tax amount is visible in the source but absent from extracted JSON.

## Hallucinations

The output includes a value that does not appear in the source.

Example: a payment reference is invented by the model.

## Math-Integrity Errors

Numeric relationships fail validation.

Example: subtotal plus tax does not equal final total.
