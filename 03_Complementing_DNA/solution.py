import sys

def reverse_complement(dna_sequence):
    trans_table = str.maketrans("ACGT", "TGCA")
    
    complement = dna_sequence.translate(trans_table)
    rev_complement = complement[::-1]
    
    return rev_complement

if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            with open(sys.argv[1], 'r') as f:
                dna = f.read().strip().upper()
                print(reverse_complement(dna))
        except FileNotFoundError:
            print("Error: File not found.")