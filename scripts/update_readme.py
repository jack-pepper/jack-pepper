#!/usr/bin/env python3
"""
Script to update README.md with worklog entries.
Reads all markdown files from the worklog directory and inserts them
between the WORKLOG:START and WORKLOG:END comments.
"""

import os
import re
from pathlib import Path
from datetime import datetime


def get_worklog_files(worklog_dir):
    """Get all markdown files from the worklog directory, sorted by date (newest first)."""
    worklog_path = Path(worklog_dir)
    if not worklog_path.exists():
        return []
    
    # Get all .md files
    md_files = list(worklog_path.glob("*.md"))
    
    # Validate filename format (YYYY-MM-DD.md)
    valid_files = []
    for f in md_files:
        # Check if filename matches date format
        if re.match(r'^\d{4}-\d{2}-\d{2}\.md$', f.name):
            valid_files.append(f)
        else:
            print(f"⚠️  Skipping invalid worklog filename: {f.name}")
    
    # Sort by filename (which are dates in YYYY-MM-DD format) in reverse order (newest first)
    valid_files.sort(reverse=True)
    
    return valid_files


def read_worklog_content(worklog_files):
    """Read content from the most recent worklog file and format it."""
    if not worklog_files:
        return ""
    
    # Only process the first (most recent) worklog file
    worklog_file = worklog_files[0]
    
    # Extract date from filename (e.g., 2026-01-18.md -> 2026-01-18)
    date_str = worklog_file.stem
    
    # Read the file content
    with open(worklog_file, 'r', encoding='utf-8') as f:
        file_content = f.read().strip()
    
    # Format the entry with a header and add the "View all worklogs" link
    entry = f"\n### 📅 {date_str}\n\n{file_content}\n\n[View all worklogs →](./worklogs)\n"
    
    return entry


def update_readme(readme_path, worklog_content):
    """Update README.md with worklog content between markers."""
    with open(readme_path, 'r', encoding='utf-8') as f:
        readme_text = f.read()
    
    # Pattern to match content between WORKLOG:START and WORKLOG:END
    pattern = r'(<!-- WORKLOG:START -->).*?(<!-- WORKLOG:END -->)'
    
    # Check if markers exist
    if not re.search(pattern, readme_text, flags=re.DOTALL):
        raise ValueError("WORKLOG markers not found in README.md. Please ensure <!-- WORKLOG:START --> and <!-- WORKLOG:END --> comments exist.")
    
    # Replace with new content
    replacement = rf'\1\n{worklog_content}\n\2'
    updated_readme = re.sub(pattern, replacement, readme_text, flags=re.DOTALL)
    
    # Write back to file
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(updated_readme)
    
    print(f"✅ Updated {readme_path} with worklog entries")


def main():
    # Get the repository root directory
    repo_root = Path(__file__).parent.parent
    
    worklog_dir = repo_root / "worklogs"
    readme_path = repo_root / "README.md"
    
    # Get worklog files
    worklog_files = get_worklog_files(worklog_dir)
    
    if not worklog_files:
        print("⚠️  No worklog files found")
        worklog_content = "\n*No worklog entries yet.*\n"
    else:
        print(f"📁 Found {len(worklog_files)} worklog file(s), displaying the most recent one")
        worklog_content = read_worklog_content(worklog_files)
    
    # Update README
    update_readme(readme_path, worklog_content)
    print("🎉 Done!")


if __name__ == "__main__":
    main()
