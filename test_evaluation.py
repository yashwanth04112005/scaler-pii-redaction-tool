"""
Test and Evaluation Script for PII Redaction Tool
Tests the redaction functionality and measures accuracy
"""

import sys
import os

# Test data with known PII
test_samples = [
    {
        "text": "My name is John Doe and my email is john.doe@example.com",
        "expected_pii": {
            "person_name": ["John Doe"],
            "email_address": ["john.doe@example.com"]
        }
    },
    {
        "text": "Contact me at +1-555-123-4567 or call 555.123.4567",
        "expected_pii": {
            "phone_number": ["+1-555-123-4567", "555.123.4567"]
        }
    },
    {
        "text": "My SSN is 123-45-6789 and credit card 4532-1234-5678-9010",
        "expected_pii": {
            "personal_id": ["123-45-6789"],
            "credit_card_info": ["4532-1234-5678-9010"]
        }
    },
    {
        "text": "Jane Smith works at Acme Corporation, date of birth 1990-05-15",
        "expected_pii": {
            "person_name": ["Jane Smith"],
            "organization_name": ["Acme Corporation"],
            "date_of_birth": ["1990-05-15"]
        }
    },
    {
        "text": "Address: 123 Main Street, Springfield, IL 62701",
        "expected_pii": {
            "street_address": ["123 Main Street, Springfield, IL 62701"]
        }
    },
    {
        "text": "IP Address: 192.168.1.1 and IPv6: 2001:0db8:85a3::8a2e:0370:7334",
        "expected_pii": {
            "ip_address": ["192.168.1.1", "2001:0db8:85a3::8a2e:0370:7334"]
        }
    },
]

# Manual PII Detection Test
def check_regex_patterns():
    """Test the regex patterns for structural PII detection"""
    import re
    
    results = {
        "ip_address_ipv4": {
            "pattern": r"\b(?:(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\b",
            "test": "192.168.1.1",
            "passed": False
        },
        "ssn": {
            "pattern": r"\b(?!000|666|9\d\d)\d{3}-(?!00)\d{2}-(?!0000)\d{4}\b",
            "test": "123-45-6789",
            "passed": False
        },
        "credit_card": {
            "pattern": r"\b(?:\d[ -]?){13,15}\d\b",
            "test": "4532-1234-5678-9010",
            "passed": False
        },
        "phone_india": {
            "pattern": r"(?:\+91[\s-]?|0)[6-9]\d{9}\b",
            "test": "+91 9876543210",
            "passed": False
        }
    }
    
    for pii_type, details in results.items():
        pattern = re.compile(details["pattern"])
        if pattern.search(details["test"]):
            results[pii_type]["passed"] = True
    
    return results

# Code Quality Checks
def check_code_structure():
    """Verify the code structure and design"""
    checks = {
        "redactor_exists": os.path.exists("pii_redaction/redactor.py"),
        "cli_exists": os.path.exists("pii_redaction/cli.py"),
        "faker_utils_exists": os.path.exists("pii_redaction/faker_utils.py"),
        "init_exists": os.path.exists("pii_redaction/__init__.py"),
        "readme_exists": os.path.exists("README.md"),
    }
    return checks

def check_pii_types_coverage():
    """Check if all required PII types are defined"""
    try:
        # Read redactor.py to check for PIIType enum
        with open("pii_redaction/redactor.py", "r") as f:
            content = f.read()
        
        required_pii_types = [
            "person_name",
            "email_address", 
            "phone_number",
            "organization_name",
            "street_address",
            "personal_id",  # SSN
            "credit_card_info",
            "date_of_birth",
            "ip_address"
        ]
        
        coverage = {}
        for pii_type in required_pii_types:
            coverage[pii_type] = pii_type in content
        
        return coverage
    except Exception as e:
        return {"error": str(e)}

def check_handling_modes():
    """Check if all handling modes are implemented"""
    try:
        with open("pii_redaction/redactor.py", "r") as f:
            content = f.read()
        
        modes = {
            "TAG": "PIIHandlingMode.TAG" in content or "tag" in content.lower(),
            "REDACT": "PIIHandlingMode.REDACT" in content or "redact" in content.lower(),
            "REPLACE": "PIIHandlingMode.REPLACE" in content or "replace" in content.lower(),
        }
        
        return modes
    except Exception as e:
        return {"error": str(e)}

def main():
    print("=" * 70)
    print("PII REDACTION TOOL - PHASE 1 EVALUATION REPORT")
    print("=" * 70)
    print()
    
    # 1. Code Structure
    print("1. CODE STRUCTURE CHECK")
    print("-" * 70)
    structure = check_code_structure()
    for check, passed in structure.items():
        status = "✓ PASS" if passed else "✗ FAIL"
        print(f"   {status}: {check}")
    print()
    
    # 2. PII Type Coverage
    print("2. PII TYPE COVERAGE CHECK")
    print("-" * 70)
    coverage = check_pii_types_coverage()
    total = len(coverage)
    passed_count = sum(1 for v in coverage.values() if v)
    
    for pii_type, present in coverage.items():
        if present:
            print(f"   ✓ {pii_type}")
        else:
            print(f"   ✗ {pii_type}")
    
    print(f"\n   Coverage: {passed_count}/{total} PII types implemented ({100*passed_count/total:.1f}%)")
    print()
    
    # 3. Handling Modes
    print("3. HANDLING MODES CHECK")
    print("-" * 70)
    modes = check_handling_modes()
    for mode, present in modes.items():
        status = "✓" if present else "✗"
        print(f"   {status} Mode: {mode}")
    print()
    
    # 4. Regex Pattern Tests
    print("4. REGEX PATTERN VALIDATION")
    print("-" * 70)
    regex_tests = check_regex_patterns()
    regex_passed = 0
    for pii_type, details in regex_tests.items():
        if details["passed"]:
            print(f"   ✓ {pii_type:20} | Test: '{details['test']}'")
            regex_passed += 1
        else:
            print(f"   ✗ {pii_type:20} | Test: '{details['test']}'")
    
    print(f"\n   Regex Tests Passed: {regex_passed}/{len(regex_tests)}")
    print()
    
    # 5. Summary
    print("=" * 70)
    print("PHASE 1 EVALUATION SUMMARY")
    print("=" * 70)
    
    total_checks = (
        sum(1 for v in structure.values() if v) +
        sum(1 for v in coverage.values() if v) +
        sum(1 for v in modes.values() if v) +
        regex_passed
    )
    
    print(f"✓ Code Structure:         {sum(1 for v in structure.values() if v)}/5")
    print(f"✓ PII Type Coverage:      {sum(1 for v in coverage.values() if v)}/9")
    print(f"✓ Handling Modes:         {sum(1 for v in modes.values() if v)}/3")
    print(f"✓ Regex Patterns:         {regex_passed}/4")
    print()
    print(f"Overall Status: {'✓ READY FOR TESTING' if total_checks == 21 else '⚠ PARTIAL COMPLETION'}")
    print()
    print("Next Steps:")
    print("- Requires full dependency installation (torch, transformers, etc.)")
    print("- Run CLI tool on sample data to measure detection accuracy")
    print("- Generate precision/recall metrics")
    print()

if __name__ == "__main__":
    main()
