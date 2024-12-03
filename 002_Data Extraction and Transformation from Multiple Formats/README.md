# **Unifying 384-Well Plate Data into a Single CSV File**

## **Project Title**
Unifying 384-well plate luminescence data from various file formats into a single CSV file.

---

## **Objectives**
- Process and unify 384-well plate data from multiple formats: `.xlsx`, `.csv`, and `.txt`.
- Standardise the data by converting it to a long format with:
  - `Plate_ID`: Identifying the plate (based on the filename).
  - `Well_ID`: Well positions (e.g., `A1`, `P24`).
  - `Luminescence`: Measured luminescence values.
- Automate the process to handle multiple files efficiently and output a single unified CSV file for downstream analysis.

---

## **Formats of the Mock Data Files**
The mock dataset includes six files:
1. **Excel files** (`.xlsx`): `mock_plate_1.xlsx`, `mock_plate_2.xlsx`
2. **CSV files** (`.csv`): `mock_plate_3.csv`, `mock_plate_4.csv`
3. **Tab-delimited text files** (`.txt`): `mock_plate_5.txt`, `mock_plate_6.txt`

Each file represents a 384-well plate with rows `A` to `P` and columns `1` to `24`.

---

## **Steps to Unify Data**
1. Read data from all six files in the directory.
2. Convert the tabular format of each plate into a long format:
   - Extract `Well_ID` by combining row and column identifiers (e.g., `A1`, `B12`).
   - Assign `Plate_ID` based on the filename.
   - Include the measured luminescence values.
3. Combine all the transformed data into a single DataFrame.
4. Save the unified dataset as a CSV file (`unified_plate_data.csv`).

---

## **Results**
The unified dataset contains:
- **2304 rows** (384 wells × 6 plates).
- The following columns:
  - `Plate_ID`: Plate identifier.
  - `Well_ID`: Well position (e.g., `A1`, `P24`).
  - `Luminescence`: Measured luminescence values.

The unified dataset is saved as `unified_plate_data.csv` and is ready for analysis.

---

## **Conclusion**
This project demonstrates an automated pipeline for processing and unifying 384-well plate data from various file formats. By standardising the data structure and automating the process, the workflow ensures efficiency, accuracy, and scalability for high-throughput data analysis.

---
