# 🧬 Computing GC Content (FASTA Analysis)

## 📌 Biological Context
The **GC-content** of a DNA molecule is the percentage of nitrogenous bases that are either Guanine (G) or Cytosine (C). In Molecular Biology, this is critical because:
- **Stability:** G-C pairs have three hydrogen bonds, making them more thermally stable than A-T pairs.
- **Taxonomy:** GC-content varies between species and can be used to identify organisms.
- **Lab Applications:** Essential for calculating melting temperatures ($T_m$) in PCR primer design.



## 🛠️ Technical Solution
This tool processes genomic data in **FASTA format**. The implementation focuses on:
1. **Multi-line FASTA Parsing:** A custom parser to handle sequences split across multiple lines, ensuring data integrity.
2. **Dictionary Mapping:** Mapping Sequence IDs to their respective DNA strings for efficient lookup.
3. **Floating-Point Precision:** Outputting results with 6-decimal place precision as required by high-standard bioinformatic platforms.



## 🚀 How to Run
1. Ensure the `.txt` file from Rosalind is in the directory.
2. Run the script:
   ```bash
   python3 solution.py rosalind_gc.txt