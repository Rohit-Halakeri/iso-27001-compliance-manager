import re

print("=" * 60)
print("PII Audit — Tool-14 AI Service")
print("=" * 60)

# List of files to check for PII
files_to_check = [
    "app.py",
    "routes/sanitise.py",
]

# PII patterns to detect
PII_PATTERNS = {
    "Email": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
    "Phone": r"\b\d{10}\b|\b\d{3}[-.\s]\d{3}[-.\s]\d{4}\b",
    "Password": r"password\s*=\s*['\"][^'\"]+['\"]",
    "API Key hardcoded": r"(api_key|apikey|secret)\s*=\s*['\"][^'\"]{10,}['\"]",
    "Name hardcoded": r"(name\s*=\s*['\"][A-Z][a-z]+\s[A-Z][a-z]+['\"])",
}

total_issues = 0

for filepath in files_to_check:
    print(f"\nChecking: {filepath}")
    try:
        with open(filepath, "r") as f:
            content = f.read()
            found_issue = False
            for pii_type, pattern in PII_PATTERNS.items():
                matches = re.findall(pattern, content, re.IGNORECASE)
                if matches:
                    print(f"  [FAIL] {pii_type} found: {matches}")
                    total_issues += 1
                    found_issue = True
            if not found_issue:
                print(f"  [PASS] No PII found")
    except FileNotFoundError:
        print(f"  [SKIP] File not found")

print("\n" + "=" * 60)
print("PII AUDIT SUMMARY")
print("=" * 60)
print(f"Files checked: {len(files_to_check)}")
print(f"PII issues found: {total_issues}")
if total_issues == 0:
    print("RESULT: PASS — No PII detected in codebase")
else:
    print("RESULT: FAIL — PII found, fix immediately!")
print("=" * 60)