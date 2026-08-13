# PII Redaction Tool

This project provides a Python script that reads a ticket log and replaces detected PII with realistic fake alternatives.

## Assignment deliverables checklist
This repository currently includes the required deliverables:

- Source code for the redaction script: `assignment_redactor.py`
- Redacted output file in plain text: `redacted_output.txt`
- Redacted output file in DOCX format: `redacted_output.docx`
- README explaining approach and tradeoffs: `README.md`
- Evaluation report with metrics: `FINAL_EVALUATION_REPORT.md`

## Objective
The script processes `assignment_input.txt`, detects supported PII values, and substitutes each with a fake but valid-looking value. Repeated occurrences are replaced consistently.

## PII categories covered
- Full names
- Email addresses
- Phone numbers
- Company names
- Physical addresses
- Social Security Numbers (SSN)
- Credit card numbers
- Dates of birth
- IP addresses

## Approach
The implementation is rule-based and uses regex patterns for each required PII type. For each match, a deterministic fake generator creates a replacement value by category.

Examples:
- Name -> `Aarav Sharma`
- Email -> `aarav.sharma1@example.com`
- Phone -> `+91 9000000001`
- SSN -> `201-11-1001`

## How to run
1. Place or update the input text in `assignment_input.txt`.
2. Run:
   `python assignment_redactor.py`
3. Generated outputs:
   - `redacted_output.txt`
   - `redacted_output.docx`

## Verified metrics (latest run)
Run date: 2026-08-13

- Original PII values found: 13
- Redacted values detected: 13
- Precision: 100.00%
- Recall: 100.00%

Per-type replacement counts from the latest run:
- person_name: 4
- email_address: 3
- phone_number: 2
- personal_id: 1
- credit_card_info: 1
- date_of_birth: 1
- ip_address: 1
- organization_name: 1
- street_address: 1

## Tradeoffs
- Strength: Deterministic, transparent replacements and reproducible output.
- Limitation: Regex coverage is only as broad as implemented patterns and may miss unseen formatting styles.
