# **Batch File Renaming for High-Throughput Screening Experiments**

## **Image Source**
The sample images used in this project are sourced from the [LIVECell](https://github.com/sartorius-research/LIVECell) repository by Sartorius Research. These images are publicly available and used here for demonstration purposes.

## **Objectives**
This mini-project aims to automate the process of renaming files in high-throughput experiments. The objectives are as follows:
- Streamline workflows by renaming files systematically using metadata.
- Save time by automating batch file processing.
- Enhance organisation by assigning meaningful names to files based on experimental conditions.

---

## **Steps**

### **1. Prepare Metadata**
A metadata file is created in CSV format, containing two columns: one for the original file names and one for the new file names. This metadata acts as a mapping guide for the renaming process.

### **2. Write the Python Script**
The Python script reads the metadata file, validates its structure, and iterates through each file in the specified directory to perform the renaming. A dry-run mode is included to preview the changes before applying them.

### **3. Run the Script**
The script is executed in two stages:
1. A dry run is performed to ensure the renaming actions are as expected.
2. If the dry run output is correct, the actual renaming is executed.

---

## **Results**
- Files are renamed according to the mappings provided in the metadata file.
- A dry run ensures that the actions are previewed before committing to changes, minimising errors.
- Renamed files reflect meaningful experimental details, improving data organisation.

---

## **Conclusion**
This mini-project demonstrates a simple yet effective approach to managing large datasets in high-throughput experiments. Automating file renaming saves significant time, reduces manual errors, and ensures consistency in file organisation. This workflow can be easily adapted for various data management scenarios in research and industry.
