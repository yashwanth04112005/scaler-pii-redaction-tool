# PII Redaction Tool

A compact Python solution for redacting personally identifiable information from the assignment input file.

## Objective
The script reads a text document, detects common PII patterns, and replaces the sensitive values with neutral placeholders while preserving the structure of the original content.

## Covered data types
- Full names
- Email addresses
- Phone numbers
- SSNs
- Credit card numbers
- Dates of birth
- Company names
- Street addresses
- IP addresses

## Files included
- `assignment_input.txt` — source assignment text
- `assignment_redactor.py` — main redaction script
- `redacted_output.txt` — redacted text output
- `redacted_output.docx` — Word document version of the redacted output
- `FINAL_EVALUATION_REPORT.md` — summary of measured results

## How to run
1. Place the input text in `assignment_input.txt`.
2. Run:
   `python assignment_redactor.py`
3. The program writes:
   - `redacted_output.txt`
   - `redacted_output.docx`

## Redaction behavior
The script replaces sensitive entries with placeholders, for example:
- `[REDACTED_NAME]`
- `[REDACTED_EMAIL]`
- `[REDACTED_PHONE]`
- `[REDACTED_SSN]`
- `[REDACTED_IP]`

## Verified evaluation on the provided assignment input
This project was evaluated against the supplied assignment document.

Results from the actual run:
- Expected PII entries: 16
- Redacted values detected: 14
- Precision: 100.00%
- Recall: 87.50%

## Notes
This is a focused, rule-based redaction workflow designed to satisfy the assignment requirement for the provided document type. It is reliable for the sample patterns included in the task, but it is not a fully general-purpose PII detector for highly varied real-world text.
