#!/usr/bin/env python3
"""Audit a synthetic document extraction batch for data-quality issues."""

from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "extraction_batch_sample.json"
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def main() -> None:
    payload = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    records = payload["records"]
    seen: Counter[str] = Counter(record["document_id"] for record in records)
    findings: list[tuple[str, str, str]] = []

    for record in records:
        doc_id = record["document_id"]
        if seen[doc_id] > 1:
            findings.append((doc_id, "high", "duplicate document_id"))
        if record["document_type"] == "invoice" and not record["vendor"]:
            findings.append((doc_id, "high", "invoice vendor missing"))
        if record["total_due"] < 0:
            findings.append((doc_id, "critical", "negative total_due"))
        if record["due_date"] and not DATE_RE.match(record["due_date"]):
            findings.append((doc_id, "medium", "due_date is not ISO 8601"))
        if record["source_pages"] < 1:
            findings.append((doc_id, "critical", "source_pages must be at least one"))

    severity_counts = Counter(severity for _, severity, _ in findings)

    print("# Document Extraction Batch QA Report")
    print()
    print("| Metric | Value |")
    print("| --- | ---: |")
    print(f"| Records audited | {len(records)} |")
    print(f"| Findings | {len(findings)} |")
    print(f"| Critical findings | {severity_counts['critical']} |")
    print(f"| High findings | {severity_counts['high']} |")
    print()
    print("## Findings")
    print()
    print("| Document | Severity | Finding |")
    print("| --- | --- | --- |")
    for doc_id, severity, note in findings:
        print(f"| {doc_id} | {severity} | {note} |")


if __name__ == "__main__":
    main()
