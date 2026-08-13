# Final Evaluation Report

## Input used
The evaluation was run against `assignment_input.txt` present in this repository.

## Task objective
Produce a redacted output where detected PII is replaced with fake alternatives rather than placeholder tags.

## Latest verified run
Command:
`python assignment_redactor.py`

Observed output:
- Original PII values found: 13
- Redacted values detected: 13
- Precision: 100.00%
- Recall: 100.00%

Per-type replacement counts:
- person_name: 4
- email_address: 3
- phone_number: 2
- personal_id: 1
- credit_card_info: 1
- date_of_birth: 1
- ip_address: 1
- organization_name: 1
- street_address: 1

## Deliverables produced
- `assignment_redactor.py`
- `redacted_output.txt`
- `redacted_output.docx`
- `README.md`
- `FINAL_EVALUATION_REPORT.md`

## Notes
This is a rule-based implementation tuned to assignment requirements and current input format. It generates realistic fake replacements consistently for repeated values.
