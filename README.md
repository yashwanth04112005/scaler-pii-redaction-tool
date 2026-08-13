# PII Redaction Tool

This project provides a Python script that reads a ticket log and replaces detected PII with realistic fake alternatives.

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
The implementation is regex-based (rule-based) and does not use an NER model. It uses Python standard-library regex patterns to detect names, emails, phone numbers, SSNs, card numbers, DOBs, company names, addresses, and IP addresses. A deterministic fake-value generator then replaces each detected value so repeated inputs map to the same fake output.

Examples:
- Name -> `Aarav Sharma`
- Email -> `aarav.sharma1@example.com`
- Phone -> `+91 9000000001`
- SSN -> `201-11-1001`

## How to run
1. Place the source file next to the script as `Red Herring Prospectus.docx`.
2. If the DOCX file is not present, the script falls back to `assignment_input.txt`.
3. Run:
   `python assignment_redactor.py`
4. Generated outputs:
   - `redacted_output.txt`
   - `redacted_output.docx`
   - `redaction_mapping.txt` (original value to fake value)

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

## Tradeoffs and observed errors
- Strength: deterministic and reproducible replacements, fast execution, and no heavy third-party model dependency for detection.
- False negatives: regex can miss unseen formats (for example unusual address formats, uncommon phone separators, or names not covered by the current pattern strategy).
- False positives: generic numeric patterns (especially phone/card-like patterns) may occasionally match non-PII numbers if text is noisy.
- Overall: this works well for structured assignment-like ticket logs, but a production setup would likely combine regex with an NER model for better generalization.
