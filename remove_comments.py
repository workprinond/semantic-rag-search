#!/usr/bin/env python3
"""
Script to remove all commented lines (starting with #) from Python files
Also removes empty lines and trailing whitespace
"""

import os
import re
from pathlib import Path

def remove_comments_from_file(filepath):
    """
    Remove commented lines from a Python file
    Preserves shebang lines (#!) and removes other comments
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        cleaned_lines = []
        in_multiline_string = False
        multiline_delimiter = None
        
        for line in lines:
            # Check for multiline string start/end
            if '"""' in line or "'''" in line:
                # Simple check for multiline strings (not perfect but works for most cases)
                if '"""' in line:
                    count = line.count('"""')
                    if count % 2 == 1:
                        in_multiline_string = not in_multiline_string
                if "'''" in line:
                    count = line.count("'''")
                    if count % 2 == 1:
                        in_multiline_string = not in_multiline_string
            
            # Skip lines that are comments (start with # after whitespace)
            # But preserve shebang (#!) and skip if inside multiline string
            stripped = line.lstrip()
            if not in_multiline_string and stripped.startswith('#') and not stripped.startswith('#!'):
                continue
            
            # Remove inline comments (everything after #, but not in strings)
            # This is simplified - for complex cases might need proper parsing
            if not in_multiline_string and '#' in line:
                # Check if # is inside quotes
                quote_count = 0
                in_quotes = False
                quote_char = None
                for i, char in enumerate(line):
                    if char in ['"', "'"] and (i == 0 or line[i-1] != '\\'):
                        if not in_quotes:
                            in_quotes = True
                            quote_char = char
                        elif char == quote_char:
                            in_quotes = False
                    if char == '#' and not in_quotes:
                        line = line[:i].rstrip()
                        break
            
            # Remove trailing whitespace
            line = line.rstrip()
            
            # Add line back if not empty or if we want to preserve structure
            if line:  # Only add non-empty lines
                cleaned_lines.append(line + '\n')
            else:
                # Optionally remove empty lines
                pass  # Skip empty lines
        
        # Write cleaned content back
        with open(filepath, 'w', encoding='utf-8') as f:
            f.writelines(cleaned_lines)
        
        return True
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return False

def remove_comments_from_directory(directory='.', extensions=['.py'], exclude_dirs=['venv', 'venv310', 'env', '__pycache__', '.git']):
    """
    Recursively remove comments from all Python files in directory
    """
    processed = 0
    failed = []
    
    for root, dirs, files in os.walk(directory):
        # Skip excluded directories
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        
        for file in files:
            if any(file.endswith(ext) for ext in extensions):
                filepath = os.path.join(root, file)
                print(f"Processing: {filepath}")
                if remove_comments_from_file(filepath):
                    processed += 1
                else:
                    failed.append(filepath)
    
    print(f"\n✅ Processed {processed} files")
    if failed:
        print(f"❌ Failed to process {len(failed)} files:")
        for f in failed:
            print(f"  - {f}")
    
    return processed, failed

def create_backup():
    """Create backup of original files before removing comments"""
    import shutil
    from datetime import datetime
    
    backup_dir = f"backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    print(f"Creating backup in {backup_dir}/")
    
    for root, dirs, files in os.walk('.'):
        # Skip backup directory itself and excluded dirs
        if backup_dir in root or '__pycache__' in root or 'venv' in root or 'venv310' in root:
            continue
        
        for file in files:
            if file.endswith('.py'):
                src = os.path.join(root, file)
                dst = os.path.join(backup_dir, src)
                os.makedirs(os.path.dirname(dst), exist_ok=True)
                shutil.copy2(src, dst)
    
    print(f"✓ Backup created in {backup_dir}/")
    return backup_dir

if __name__ == "__main__":
    import sys
    
    print("="*60)
    print("COMMENT REMOVAL SCRIPT")
    print("="*60)
    
    # Ask for backup
    response = input("\nCreate backup before removing comments? (y/n): ")
    if response.lower() == 'y':
        backup_dir = create_backup()
    else:
        print("Proceeding without backup...")
    
    # Ask for directory
    directory = input("\nEnter directory to process (default: current directory): ").strip()
    if not directory:
        directory = '.'
    
    # Ask about removing empty lines
    remove_empty = input("Remove empty lines? (y/n): ").strip().lower()
    
    print(f"\nProcessing Python files in {directory}...\n")
    
    # Process files
    processed, failed = remove_comments_from_directory(directory, extensions=['.py'])
    
    print("\n" + "="*60)
    print("COMMENT REMOVAL COMPLETE")
    print("="*60)
    print(f"✅ Successfully processed: {processed} files")
    if failed:
        print(f"❌ Failed: {len(failed)} files")
    
    if response.lower() == 'y':
        print(f"\n💾 Backup saved to: {backup_dir}")
        print("   To restore: cp -r {backup_dir}/* .")
