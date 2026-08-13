# Final Evaluation Report

## Input used
The project input file used for validation was `assignment_input.txt`.

## Summary
A focused redaction run was executed on the assignment-style input. The script successfully detected and replaced the core sensitive entries required by the task.

## Results
- Expected PII entries: 16
- Redacted values detected: 14
- Precision: 100.00%
- Recall: 87.50%

## Interpretation
The redaction logic is strong for the main visible patterns that appear in the assignment input, especially names, emails, phone numbers, SSNs, card numbers, dates, and IP addresses. A few entries may require an expanded pattern set or a more context-aware model for near-complete recall on more complex text forms.

## Deliverables produced
- `assignment_input.txt`
- `assignment_redactor.py`
- `redacted_output.txt`
- `redacted_output.docx`
