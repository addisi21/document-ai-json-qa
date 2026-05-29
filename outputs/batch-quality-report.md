# Document Extraction Batch QA Report

Generated from `data/extraction_batch_sample.json` with
`scripts/audit_extraction_batch.py`.

| Metric | Value |
| --- | ---: |
| Records audited | 5 |
| Findings | 4 |
| Critical findings | 1 |
| High findings | 2 |

## Findings

| Document | Severity | Finding |
| --- | --- | --- |
| DOC-002 | high | duplicate document_id |
| DOC-004 | critical | negative total_due |
| DOC-004 | medium | due_date is not ISO 8601 |
| DOC-002 | high | duplicate document_id |
