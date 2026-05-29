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
- `proof-pack.md`: public document extraction QA examples with model JSON, expected JSON, error tables, severity labels, and reviewer notes
- [schema/invoice_schema.json](schema/invoice_schema.json): public invoice extraction schema
- [examples/reconstructed_invoice_source.md](examples/reconstructed_invoice_source.md): reconstructed source document
- [examples/extracted_invoice.json](examples/extracted_invoice.json): AI-extracted JSON sample
- [expected/invoice_expected.json](expected/invoice_expected.json): expected source-grounded values
- [scripts/validate_invoice_extraction.py](scripts/validate_invoice_extraction.py): dependency-free validation script
- [outputs/validation-report.md](outputs/validation-report.md): reviewer-ready validation report

## Confidentiality Standard

All examples are rewritten for public use and do not contain real client files, screenshots, invoices, contracts, or source documents.

## Run Locally

```bash
python scripts/validate_invoice_extraction.py
```
