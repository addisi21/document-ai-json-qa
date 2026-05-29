# Invoice Extraction Validation Report

Generated from `examples/extracted_invoice.json` and
`expected/invoice_expected.json` with `scripts/validate_invoice_extraction.py`.

| Field | Severity | Finding |
| --- | --- | --- |
| vendor | minor | legal suffix dropped from vendor name |
| bill_to | minor | billing address omitted |
| tax_amount | minor | rounding differs from source document |

**Verdict:** PASS_WITH_MINOR_FLAGS
