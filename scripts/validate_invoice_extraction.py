#!/usr/bin/env python3
"""Validate a reconstructed invoice extraction against expected values.

The checks are intentionally simple and dependency-free. They show the review
logic a document AI QA analyst would apply: required fields, math integrity,
source-value comparison, and severity tagging.
"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXTRACTED = ROOT / "examples" / "extracted_invoice.json"
EXPECTED = ROOT / "expected" / "invoice_expected.json"


def money_equal(left: float, right: float, tolerance: float = 0.01) -> bool:
    return abs(left - right) <= tolerance


def main() -> None:
    extracted = json.loads(EXTRACTED.read_text(encoding="utf-8"))
    expected = json.loads(EXPECTED.read_text(encoding="utf-8"))
    findings: list[tuple[str, str, str]] = []

    required = [
        "invoice_number",
        "vendor",
        "bill_to",
        "line_items",
        "subtotal",
        "tax_amount",
        "total_due",
        "due_date",
    ]

    for field in required:
        if field not in extracted:
            findings.append((field, "critical", "required field missing"))

    if extracted.get("vendor") != expected["vendor"]:
        findings.append(("vendor", "minor", "legal suffix dropped from vendor name"))

    if extracted.get("bill_to") != expected["bill_to"]:
        findings.append(("bill_to", "minor", "billing address omitted"))

    if len(extracted.get("line_items", [])) != expected["line_item_count"]:
        findings.append(("line_items", "high", "line item count mismatch"))

    line_total = sum(item["line_total"] for item in extracted["line_items"])
    if not money_equal(line_total, extracted["subtotal"]):
        findings.append(("subtotal", "critical", "line totals do not match subtotal"))

    if not money_equal(extracted["tax_amount"], expected["tax_amount"]):
        findings.append(("tax_amount", "minor", "rounding differs from source document"))

    if not money_equal(round(extracted["subtotal"] + expected["tax_amount"], 2), expected["total_due"]):
        findings.append(("total_due", "critical", "subtotal plus source tax does not match total"))

    print("# Invoice Extraction Validation Report")
    print()
    print("| Field | Severity | Finding |")
    print("| --- | --- | --- |")
    for field, severity, note in findings:
        print(f"| {field} | {severity} | {note} |")

    if not findings:
        print("| all | pass | no issues found |")

    blocking = [item for item in findings if item[1] in {"critical", "high"}]
    verdict = "PASS_WITH_MINOR_FLAGS" if not blocking else "FAIL"
    print()
    print(f"**Verdict:** {verdict}")


if __name__ == "__main__":
    main()
