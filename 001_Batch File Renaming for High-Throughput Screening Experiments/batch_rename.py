import os
import pandas as pd
import argparse
from pathlib import Path

def rename_files(csv_file, directory, dry_run=False):
    """
    Rename files in the specified directory based on a mapping CSV file.
    
    Args:
        csv_file (str): Path to the CSV file containing original and new file names.
        directory (str): Path to the directory containing the files to rename.
        dry_run (bool): If True, only display the renaming actions without making changes.
    """
    # Load the mapping CSV
    try:
        mapping = pd.read_csv(csv_file)
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return
    
    # Validate required columns
    if not {'original_name', 'new_name'}.issubset(mapping.columns):
        print("CSV file must contain 'original_name' and 'new_name' columns.")
        return
    
    # Iterate through the mapping
    for _, row in mapping.iterrows():
        original_path = Path(directory) / row['original_name']
        new_path = Path(directory) / row['new_name']
        
        if not original_path.exists():
            print(f"File not found: {original_path}")
            continue
        
        if dry_run:
            print(f"[DRY RUN] Would rename: {original_path} -> {new_path}")
        else:
            try:
                os.rename(original_path, new_path)
                print(f"Renamed: {original_path} -> {new_path}")
            except Exception as e:
                print(f"Error renaming {original_path} to {new_path}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Batch rename files based on a mapping CSV.")
    parser.add_argument("--csv_file", required=True, help="Path to the CSV file with the mapping.")
    parser.add_argument("--directory", required=True, help="Path to the directory with files to rename.")
    parser.add_argument("--dry_run", action="store_true", help="Preview the changes without renaming files.")
    
    args = parser.parse_args()
    rename_files(args.csv_file, args.directory, args.dry_run)

if __name__ == "__main__":
    main()
