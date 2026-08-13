# PII Redaction Tool

This project implements a compact Python solution for detecting and redacting personally identifiable information in the assignment input.

## Assignment deliverables checklist
This submission includes the required deliverables:

- Source code for the redaction script: `assignment_redactor.py`
- Redacted output file in plain text: `redacted_output.txt`
- Redacted output file in DOCX format: `redacted_output.docx`
- README explaining the approach: `README.md`
- Evaluation report with measured results: `FINAL_EVALUATION_REPORT.md`

## Objective
The script reads the provided assignment text, identifies common PII patterns, and replaces them with neutral placeholders while preserving the original document structure.

## PII categories covered
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
1. Place the input text in `assignment_input.txt`.
2. Run the script:
   `python assignment_redactor.py`
3. The program generates:
   - `redacted_output.txt`
   - `redacted_output.docx`

## Example output behavior
The script replaces detected values with placeholders such as:
- `[REDACTED_NAME]`
- `[REDACTED_EMAIL]`
- `[REDACTED_PHONE]`
- `[REDACTED_SSN]`
- `[REDACTED_IP]`

## Verified evaluation on the provided assignment input
The project was tested against the supplied assignment data and the actual run produced the following metrics:

- Expected PII entries: 16
- Redacted values detected: 14
- Precision: 100.00%
- Recall: 87.50%
