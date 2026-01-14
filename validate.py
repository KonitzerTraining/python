#!/usr/bin/env python3
"""Validates markdown files for common issues."""

import sys
from pathlib import Path

def validate_file(filepath):
    """Validate a single markdown file."""
    errors = []
    warnings = []

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if file is empty
    if not content.strip():
        errors.append("File is empty")
        return errors, warnings

    # Check balanced code blocks
    blocks = content.count('```')
    if blocks % 2 != 0:
        errors.append(f"Unbalanced code blocks (found {blocks} markers)")

    # Check for smart quotes and problematic Unicode
    problematic_chars = {
        '\u2018': 'Left single quote',
        '\u2019': 'Right single quote',
        '\u201c': 'Left double quote',
        '\u201d': 'Right double quote',
    }

    for char, name in problematic_chars.items():
        if char in content:
            count = content.count(char)
            warnings.append(f"Found {count} {name} character(s)")

    return errors, warnings

def main():
    """Validate all markdown files."""
    files = list(Path('chapters').glob('*.md')) + [Path('intro.md')]

    all_good = True

    for file in files:
        print(f"\n=== {file} ===")
        errors, warnings = validate_file(file)

        if errors:
            all_good = False
            print("ERRORS:")
            for error in errors:
                print(f"  ❌ {error}")

        if warnings:
            print("WARNINGS:")
            for warning in warnings:
                print(f"  ⚠️  {warning}")

        if not errors and not warnings:
            print("  ✅ File is valid")

    if all_good:
        print("\n✅ All files validated successfully!")
        return 0
    else:
        print("\n❌ Some files have errors!")
        return 1

if __name__ == '__main__':
    sys.exit(main())
