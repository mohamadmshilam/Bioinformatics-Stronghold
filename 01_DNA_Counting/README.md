# 🧬 DNA Nucleotide Counting Tool

##  Project Overview
In Bioinformatics, analyzing the basic composition of a DNA sequence is fundamental for genomic research. This project provides a robust Python-based tool to count the occurrences of the four nitrogenous bases: **Adenine (A)**, **Cytosine (C)**, **Guanine (G)**, and **Thymine (T)**.

Understanding these frequencies is the first step toward calculating **GC Content**, predicting DNA melting temperatures, and designing effective PCR primers—skills essential in R&D environments.

##  Key Features
- **Command Line Interface (CLI):** Designed to handle dynamic input files using `sys.argv`, making it ready for high-throughput pipelines.
- **Robust Error Handling:** Includes `try-except` blocks to manage missing files or path errors gracefully.
- **Data Normalization:** Automatically converts sequences to uppercase using `.upper()` to ensure biological accuracy regardless of input formatting.
- **Modular Design:** The core logic is encapsulated in a reusable function, allowing for easy integration into larger bioinformatics projects.

##  Technical Implementation
- **File I/O:** Utilizes the `with open` context manager for safe and efficient memory management.
- **Performance:** Leverages Python's built-in `.count()` method for optimized string traversal on large genomic data.
- **Modularity:** Implements the `if __name__ == "__main__":` guard to ensure the script remains modular and importable.

## 📂 How to Run
1. Ensure you have **Python 3.x** installed in your Linux/WSL environment.
2. Place your genomic data (e.g., `rosalind_dna.txt`) in the project directory.
3. Execute the script via terminal:
   ```bash
   python3 dna_solution.py rosalind_dna.txt