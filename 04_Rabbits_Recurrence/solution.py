import sys

def rabbit_growth(n, k):
    if n <= 2:
        return 1
    f = [0] * (n + 1)
    f[1] = 1
    f[2] = 1
    
    for i in range(3, n + 1):
        f[i] = f[i-1] + (k * f[i-2])
        
    return f[n]

if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            with open(sys.argv[1], 'r') as file:
            
                line = file.read().strip()
                n_val, k_val = map(int, line.split())
                
                print(rabbit_growth(n_val, k_val))
        except FileNotFoundError:
            print("خطأ: الملف غير موجود.")