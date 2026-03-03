import sys
def transcribe_dna_to_rna(file_path):
    try:
        with open(file_path, 'r') as file:
            dna_sequence = file.read().strip().upper()
        
        rna = dna_sequence.replace('T', 'U')
        
        return rna
    except FileNotFoundError:
        print("Error: The file was not found.")
        return None
if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(transcribe_dna_to_rna(sys.argv[1]))