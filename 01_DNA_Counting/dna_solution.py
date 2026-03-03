import sys  # مكتبة للتعامل مع نظام التشغيل ووسائط التيرمينال

def count_dna_nucleotides(file_path):
    """
    دالة احترافية تقبل مسار أي ملف وتعيد توزيع القواعد النيتروجينية.
    """
    try:
        with open(file_path, 'r') as file:
            # قراءة النص وتنظيفه من الفراغات والأسطر الجديدة
            dna_sequence = file.read().strip().upper() 
            
        # استخدام المنطق البرمجي السريع للعد
        a = dna_sequence.count('A')
        c = dna_sequence.count('C')
        g = dna_sequence.count('G')
        t = dna_sequence.count('T')
        
        return f"{a} {c} {g} {t}"
    
    except FileNotFoundError:
        return f"Error: The file '{file_path}' was not found."

if __name__ == "__main__":
    # التحقق مما إذا كان المستخدم قد مرر اسم الملف في التيرمينال
    if len(sys.argv) > 1:
        # sys.argv[1] هي الكلمة التي تكتبها بعد اسم الكود في التيرمينال
        target_file = sys.argv[1]
        print(count_dna_nucleotides(target_file))
    else:
        print("Usage: python3 dna_solution.py <filename>")