import os
import pandas as pd

def process_plate_files(input_dir, output_file, dry_run=False):
    """
    Unify 384-well plate data from multiple formats into a single CSV file.
    
    Args:
        input_dir (str): Directory containing input files.
        output_file (str): File path to save the unified CSV output.
        dry_run (bool): If True, preview the transformations without saving the output.
    """
    unified_data = []  # List to store data from all plates
    
    for filename in os.listdir(input_dir):
        file_path = os.path.join(input_dir, filename)
        plate_id = os.path.splitext(filename)[0]  # Use filename (without extension) as Plate_ID
        
        try:
            # Read the file based on its extension
            if filename.endswith(".xlsx"):
                df = pd.read_excel(file_path, index_col=0)
            elif filename.endswith(".csv"):
                df = pd.read_csv(file_path, index_col=0)
            elif filename.endswith(".txt"):
                df = pd.read_csv(file_path, index_col=0, delimiter="\t")
            else:
                print(f"Skipping unsupported file: {filename}")
                continue

            # Convert the tabular format to long format
            df_long = df.stack().reset_index()
            df_long.columns = ["Row", "Column", "Luminescence"]
            df_long["Well_ID"] = df_long["Row"] + df_long["Column"].astype(str)
            df_long["Plate_ID"] = plate_id
            
            # Append to unified data
            unified_data.append(df_long[["Plate_ID", "Well_ID", "Luminescence"]])
            print(f"Processed file: {filename}")
        
        except Exception as e:
            print(f"Error processing file {filename}: {e}")

    # Combine all data into a single DataFrame
    if unified_data:
        combined_df = pd.concat(unified_data, ignore_index=True)
        
        if dry_run:
            # Preview the combined data
            print("\n[DRY RUN] Combined Data Preview:")
            print(combined_df.head())  # Display the first few rows
            print(f"\n[DRY RUN] Total Rows: {len(combined_df)}")
        else:
            # Save the combined data to the specified output file
            combined_df.to_csv(output_file, index=False)
            print(f"Unified data saved to: {output_file}")
    else:
        print("No valid files found for processing.")

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Unify 384-well plate data into a single CSV file.")
    parser.add_argument("--input_dir", required=True, help="Path to the directory containing input files.")
    parser.add_argument("--output_file", required=True, help="Path to save the unified CSV output.")
    parser.add_argument("--dry_run", action="store_true", help="Preview the combined data without saving.")
    args = parser.parse_args()

    process_plate_files(args.input_dir, args.output_file, args.dry_run)

if __name__ == "__main__":
    main()
