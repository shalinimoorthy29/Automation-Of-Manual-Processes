# Sequence Retrieval Using NCBI Entrez API

---

## Objective

The goal of this project is to automate the retrieval of nucleotide sequences from the NCBI Entrez database using the Biopython library. The sequences are retrieved using a list of gene accession IDs, which are then saved as FASTA files for further analysis.

---

## List of Genes and Their Accession IDs

The following genes and their respective accession IDs were used in this project:

1. **BRCA1** (Breast Cancer 1, human)  
   - Accession ID: `NM_007294`

2. **TP53** (Tumour Protein P53, human)  
   - Accession ID: `NM_001126112`

3. **EGFR** (Epidermal Growth Factor Receptor, human)  
   - Accession ID: `NM_005228`

4. **MYC** (Myc Proto-Oncogene, human)  
   - Accession ID: `NM_002467`

5. **CFTR** (Cystic Fibrosis Transmembrane Conductance Regulator, human)  
   - Accession ID: `NM_000492`

6. **FMR1** (Fragile X Mental Retardation 1, human)  
   - Accession ID: `NM_002024`

7. **ACTB** (Beta-Actin, human)  
   - Accession ID: `NM_001101`

8. **HBB** (Haemoglobin Subunit Beta, human)  
   - Accession ID: `NM_000518`

9. **GAPDH** (Glyceraldehyde-3-Phosphate Dehydrogenase, human)  
   - Accession ID: `NM_001289746`

10. **APOE** (Apolipoprotein E, human)  
    - Accession ID: `NM_001302688`

---

## Steps to Obtain FASTA Sequences via the Biopython API

1. **Set Up the Environment**:
   - Install **Python 3.10** (compatible for biopython installation).
   - Set up a virtual environment using `venv`.
   - Install the required libraries, such as **Biopython** and **numpy**, using:
     ```bash
     pip install biopython numpy
     ```

2. **Prepare the Accession IDs**:
   - Create a `.txt` file containing the list of accession IDs, one per line.
   - Example format:
     ```
     NM_007294
     NM_001126112
     NM_005228
     ...
     ```

3. **Write the Retrieval Script**:
   - Use the Biopython **Entrez** module to query the NCBI database for each accession ID.
   - The script uses `Entrez.efetch()` to fetch sequences in **FASTA** format.
   - The sequences are saved as individual `.fasta` files in the specified output directory.

4. **Run the Script**:
   - Use the `--dry_run` option to simulate fetching sequences without saving them.
   - Run the script to fetch and save sequences:
     ```bash
     python retrieve_sequences.py
     ```

5. **Results**:
   - The sequences are saved as `.fasta` files named according to the accession ID (e.g., `NM_007294.fasta`).
   - The sequences are stored in a folder named `sequences` within the project directory.

---

## Results

After running the script, the following sequences were successfully retrieved and saved as FASTA files in the `sequences` folder:

- `NM_007294.fasta`
- `NM_001126112.fasta`
- `NM_005228.fasta`
- `NM_002467.fasta`
- `NM_000492.fasta`
- `NM_002024.fasta`
- `NM_001101.fasta`
- `NM_000518.fasta`
- `NM_001289746.fasta`
- `NM_001302688.fasta`

---

## Conclusion

This project demonstrates how to use the Biopython library to interact with the NCBI Entrez API, fetch nucleotide sequences using accession IDs, and save the sequences in FASTA format. The script provides a flexible framework for automating sequence retrieval, which can be adapted to handle a large number of accession IDs and used for various bioinformatics analyses.

The project can be expanded to fetch other data types from NCBI, such as protein sequences or metadata, and to handle additional error checking and rate-limiting for larger-scale applications.

