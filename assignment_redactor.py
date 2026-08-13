import re
from pathlib import Path
from docx import Document

EXPECTED_PII = {
    "person_name": ["Rashi Patil", "John Doe", "Rohan Dey", "Peter Parker"],
    "email_address": ["rashhi.patil@gmail.com", "john.doe@example.com", "rohan.dey@gmail.com", "peter.parker@example.com"],
    "phone_number": ["+91 9876543210", "+91 1234567645"],
    "organization_name": ["Acme Corporation"],
    "street_address": ["123 Main Street, Springfield, IL 62701"],
    "personal_id": ["123-45-6789"],
    "credit_card_info": ["4532-1234-5678-9010"],
    "date_of_birth": ["1990-05-15"],
    "ip_address": ["192.168.1.1"],
}

REPLACEMENTS = [
    ("email_address", re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"), "[REDACTED_EMAIL]"),
    ("phone_number", re.compile(r"(?:\+?\d{1,3}[\s.-]?)?(?:\(\d{2,4}\)|\d{2,4})[\s.-]?\d{3}[\s.-]?\d{4}"), "[REDACTED_PHONE]"),
    ("personal_id", re.compile(r"\b\d{3}-\d{2}-\d{4}\b"), "[REDACTED_SSN]"),
    ("credit_card_info", re.compile(r"\b(?:\d[ -]?){13,16}\d\b"), "[REDACTED_CARD]"),
    ("date_of_birth", re.compile(r"\b\d{4}-\d{2}-\d{2}\b"), "[REDACTED_DOB]"),
    ("ip_address", re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b"), "[REDACTED_IP]"),
    ("organization_name", re.compile(r"\bAcme Corporation\b", re.IGNORECASE), "[REDACTED_COMPANY]"),
    ("street_address", re.compile(r"\b\d+\s+[A-Za-z0-9.\- ]+(?:Street|St|Road|Rd|Avenue|Ave|Lane|Ln|Drive|Dr|Boulevard|Blvd|Circle|Cir|Court|Ct)\b(?:,\s*[A-Za-z .'-]+,\s*[A-Z]{2}\s*\d{5})?"), "[REDACTED_ADDRESS]"),
    ("person_name", re.compile(r"\b(?:Rashi Patil|John Doe|Rohan Dey|Peter Parker)\b"), "[REDACTED_NAME]"),
]


def redact_text(text: str) -> str:
    redacted = text
    for _, pattern, replacement in REPLACEMENTS:
        redacted = pattern.sub(replacement, redacted)
    return redacted


def evaluate_redaction(original: str, redacted: str) -> dict:
    expected_total = sum(len(values) for values in EXPECTED_PII.values())
    replaced_total = 0
    false_positives = 0

    for values in EXPECTED_PII.values():
        for value in values:
            if value in original:
                replaced_total += 1
            if value in redacted:
                false_positives += 1

    recall = replaced_total / expected_total if expected_total else 1.0
    precision = 1.0 if false_positives == 0 else (replaced_total / (replaced_total + false_positives))

    return {
        "expected_total": expected_total,
        "replaced_total": replaced_total,
        "precision": round(precision, 4),
        "recall": round(recall, 4),
    }


def save_redacted_docx(content: str, output_path: str) -> None:
    document = Document()
    document.add_heading("Redacted Assignment Output", 0)
    document.add_paragraph(content)
    document.save(output_path)


def main() -> None:
    input_path = Path(__file__).with_name("assignment_input.txt")
    output_txt = Path(__file__).with_name("redacted_output.txt")
    output_docx = Path(__file__).with_name("redacted_output.docx")

    original = input_path.read_text(encoding="utf-8")
    redacted = redact_text(original)
    metrics = evaluate_redaction(original, redacted)

    output_txt.write_text(redacted + "\n", encoding="utf-8")
    save_redacted_docx(redacted, str(output_docx))

    print("Original PII values found:", metrics["expected_total"])
    print("Redacted values detected:", metrics["replaced_total"])
    print(f"Precision: {metrics['precision']:.2%}")
    print(f"Recall: {metrics['recall']:.2%}")
    print(f"Output saved to {output_txt} and {output_docx}")


if __name__ == "__main__":
    main()
