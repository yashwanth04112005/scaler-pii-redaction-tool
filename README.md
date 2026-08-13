# PII Redaction Tool

This project reads a text input containing sensitive information and replaces the detected PII with redaction tags.

## What it covers
- Full names
- Email addresses
- Phone numbers
- SSNs
- Credit card numbers
- Dates of birth
- Company names
- Street addresses
- IP addresses

## How to run
1. Place the assignment text in `assignment_input.txt`
2. Run:
   python assignment_redactor.py
3. The script writes:
   - `redacted_output.txt`
   - `redacted_output.docx`

## Output behavior
The script replaces detected values with placeholders such as:
- [REDACTED_NAME]
- [REDACTED_EMAIL]
- [REDACTED_PHONE]
- [REDACTED_SSN]
- [REDACTED_IP]

## Evaluation
The current validation run on the project input fixture produced:
- Precision: 100.00%
- Recall: 87.50%
- Redacted values detected: 14 out of 16 expected PII entries

This is a focused rule-based redaction workflow designed for the assignment requirement to detect and mask sensitive data while preserving the structure of the original text.
