class Urun:
    def __init__(self, ad, fiyat):
        self.ad = ad
        self.fiyat = fiyat

    # __repr__ çıktısı, nesneyi yeniden oluşturabilecek bir Python kodu olmalı.
    def __repr__(self):
        # 'Urun("Laptop", 15000)' şeklinde bir dize döndürüyoruz
        return f'Urun("{self.ad}", {self.fiyat})'

# 1. Orijinal Nesne
urun_a = Urun("Klavye", 750)

# 2. repr ile nesneyi temsil eden dizeyi alıyoruz.
urun_a_repr = repr(urun_a)
print(f"repr Çıktısı: {urun_a_repr}")
# Çıktı: repr Çıktısı: Urun("Klavye", 750)

# 3. eval() ile dizeyi çalıştırıp nesneyi yeniden oluşturuyoruz.
# Python bu dizeyi "Urun('Klavye', 750)" şeklinde bir yapıcı (constructor) çağrısı olarak algılar.
urun_b = eval(urun_a_repr)

# Karşılaştırma
print("\n--- Karşılaştırma ---")
print(f"Orijinal Nesne (A): {urun_a.ad}, {urun_a.fiyat}")
print(f"Yeni Nesne (B):     {urun_b.ad}, {urun_b.fiyat}")

# Kontrol: Farklı nesneler mi? (Evet)
print(f"Bellekte aynı nesneler mi? {urun_a is urun_b}") 
# Çıktı: Bellekte aynı nesneler mi? False (Çünkü yepyeni bir nesne oluşturduk)

"""
kotu_niyetli_repr = 'Urun("Hacklendi", 0); import os; os.system("rm -rf /")'

# Eğer bunu eval() ile çalıştırırsanız, sistem komutu çalışır!
# eval(kotu_niyetli_repr)  <-- Asla yapmayın!
"""