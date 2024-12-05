from Bio import Entrez
import os
import argparse

# Set your email for Entrez (required by NCBI)
Entrez.email = "shalinimoorthy29@outlook.com"

def fetch_sequence(accession_id, output_dir, dry_run=False):
    """
    Fetches a sequence from NCBI by accession ID and saves it as a FASTA file.
    If dry_run is True, only prints what would be done, without saving the file.
    """
    try:
        # Query NCBI for the sequence
        handle = Entrez.efetch(db="nucleotide", id=accession_id, rettype="fasta", retmode="text")
        fasta_data = handle.read()
        handle.close()

        if dry_run:
            # Just print the action without saving
            print(f"[DRY RUN] Would fetch and save sequence for {accession_id} as {accession_id}.fasta")
        else:
            # Save the FASTA file
            output_file = os.path.join(output_dir, f"{accession_id}.fasta")
            with open(output_file, "w") as f:
                f.write(fasta_data)
            print(f"Sequence for {accession_id} saved to {output_file}")

    except Exception as e:
        print(f"Error fetching sequence for {accession_id}: {e}")

def main():
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description="Fetch sequences from NCBI Entrez and save as FASTA.")
    parser.add_argument("--dry_run", action="store_true", help="Perform a dry run without saving sequences.")
    args = parser.parse_args()

    # Input file containing accession IDs
    input_file = "accession_ids.txt"  # File with accession IDs
    output_dir = "sequences"          # Output directory
    dry_run = args.dry_run            # Get dry_run flag from command-line argument

    # Read accession IDs from the file
    with open(input_file, "r") as f:
        accession_ids = [line.strip() for line in f if line.strip()]

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Fetch sequences for each accession ID
    for accession_id in accession_ids:
        fetch_sequence(accession_id, output_dir, dry_run)

if __name__ == "__main__":
    main()
