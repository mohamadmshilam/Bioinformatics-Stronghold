import sys

def parse_fasta(file_path):
    sequences = {}
    with open(file_path, 'r') as f:
        current_id = ""
        for line in f:
            line = line.strip()
            if not line: continue
            if line.startswith(">"):
                current_id = line[1:]  
                sequences[current_id] = ""
            else:
                sequences[current_id] += line 
    return sequences

def calculate_gc_content(sequence):
    if not sequence: return 0
    g_count = sequence.count('G')
    c_count = sequence.count('C')
    return (g_count + c_count) / len(sequence) * 100

def find_highest_gc(file_path):
    sequences = parse_fasta(file_path)
    max_id = ""
    max_gc = -1.0
    
    for seq_id, dna in sequences.items():
        current_gc = calculate_gc_content(dna)
        if current_gc > max_gc:
            max_gc = current_gc
            max_id = seq_id
            
    return max_id, max_gc

if __name__ == "__main__":
    if len(sys.argv) > 1:
        result_id, result_gc = find_highest_gc(sys.argv[1])
        print(f"{result_id}")
        print(f"{result_gc:.6f}")