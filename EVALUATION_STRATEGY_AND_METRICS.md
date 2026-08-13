# Evaluation Strategy and Metrics

## 1. Objective
This document describes how the PII redaction solution is evaluated, what metrics are used, and the observed results from the current implementation.

## 2. Evaluation Strategy
The evaluation is done in two tracks to balance correctness and real-document behavior:

1. Benchmark track (with known ground truth)
- Input: `assignment_input.txt`
- Purpose: measure precision and recall against a fixed expected PII set.
- Why: this gives objective, reproducible metrics.

2. Operational track (real document)
- Input: `Red Herring Prospectus.docx`
- Purpose: validate end-to-end document processing and replacement counts at scale.
- Why: this confirms the pipeline works on the actual `.docx` assignment flow.

## 3. Approach Under Test
- Detection method: regex-based rules for required PII types.
- Replacement method: deterministic fake-value generator.
- Consistency rule: repeated original values map to the same fake value in a single run.

## 4. Metrics Definition
Let:
- TP = correctly redacted PII instances
- FP = non-PII instances incorrectly redacted
- FN = PII instances missed by redaction

Metrics:
- Precision = $\frac{TP}{TP + FP}$
- Recall = $\frac{TP}{TP + FN}$
- Accuracy (entity-level) = $\frac{TP + TN}{TP + TN + FP + FN}$

Note:
- For this assignment implementation, benchmark reporting focuses on precision and recall.
- Entity-level TN counting is usually very large and less informative for redaction tasks, so precision/recall is preferred.

## 5. Test Procedure
1. Run benchmark on labeled fixture:
- `python assignment_redactor.py assignment_input.txt`

2. Run operational document test:
- `python assignment_redactor.py`
  - If `Red Herring Prospectus.docx` exists, it is processed by default.

3. Validate artifacts generated:
- `redacted_output.txt`
- `redacted_output.docx`
- `redaction_mapping.txt`

## 6. Results

### 6.1 Benchmark Track (`assignment_input.txt`)
Observed run output:
- Original PII values found: 11
- Redacted values detected: 11
- Accuracy (PII-instance level): 100.00% (11/11)
- Precision: 100.00%
- Recall: 100.00%

Per-type replacement counts:
- person_name: 2
- email_address: 3
- phone_number: 2
- personal_id: 1
- credit_card_info: 1
- date_of_birth: 1
- organization_name: 1
- street_address: 1
- ip_address: 1

### 6.2 Operational Track (`Red Herring Prospectus.docx`)
Observed run output:
- Input processed successfully as `.docx`
- Replacement counts (sample observed):
  - email_address: 70
  - phone_number: 42
  - street_address: 3

Important interpretation:
- Precision/recall printed for this run are not ground-truth metrics because the current expected set is tied to `assignment_input.txt`.
- For the `.docx` file, replacement counts are treated as operational indicators unless manual labeling is created.

## 7. Tradeoffs and Error Analysis
Strengths:
- Fast, transparent rule-based detection.
- Deterministic fake replacements improve consistency and reviewability.
- Works directly on Word documents (`.docx`) including paragraphs and table cells.

Known limitations:
- False negatives may occur for unseen text formats not covered by regex.
- False positives may occur when numeric patterns resemble phone/card formats in noisy text.
- A pure regex system is less robust than hybrid regex + NER for highly variable language.

## 8. Reproducibility
Commands used:
- `python assignment_redactor.py assignment_input.txt`
- `python assignment_redactor.py`

Expected output files:
- `redacted_output.txt`
- `redacted_output.docx`
- `redaction_mapping.txt`

## 9. Conclusion
The current solution meets assignment expectations for a deterministic redaction pipeline and shows perfect benchmark precision/recall on the labeled fixture. The real-document run confirms full `.docx` processing at scale, with measurable replacement volumes and submission-ready artifacts.
