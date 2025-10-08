"""
Python topluluğunda kabul edilen genel bir kural şudur: __repr__'yi her zaman tanımlayın.

Eğer bir sınıfta sadece __repr__ tanımlıysa, print() fonksiyonu da bu çıktıyı kullanır.

Eğer bir sınıfta hem __str__ hem de __repr__ tanımlıysa, print() her zaman __str__'yi tercih eder.

Bu yaklaşım, nesnenizin her zaman geliştirici için açık bir temsilinin olmasını sağlar.

"""

class Ilan:
    def __init__(self, il, alan, oda, fiyat, ilan_no):
        self.il = il
        self.alan = alan
        self.oda = oda
        self.fiyat = fiyat
        self.ilan_no = ilan_no # Geliştiricinin bilmesi gereken ID

    # 1. __str__ (Kullanıcı Dostu Format)
    def __str__(self):
        fiyat_str = f"{self.fiyat:,.0f}".replace(",", ".") # Fiyatı okunabilir hale getir
        return f"{self.il}'da {self.alan}m², {self.oda} Oda, Fiyat: {fiyat_str} TL"

    # 2. __repr__ (Kesin ve Açık Format)
    def __repr__(self):
        # Dikkat: Çıktı, nesneyi yeniden oluşturmaya izin veren bir Python kodu gibi görünüyor.
        return f"Ilan(il='{self.il}', alan={self.alan}, oda={self.oda}, fiyat={self.fiyat}, ilan_no={self.ilan_no})"

ilan1 = Ilan("İstanbul", 150, 3, 1500000, 42)

# FARK 1: print() veya str() (Kullanıcıya Gösterim)
print("--- Kullanıcı (str) ---")
print(ilan1)
print(str(ilan1))
# Çıktı: İstanbul'da 150m², 3 Oda, Fiyat: 1.500.000 TL

# FARK 2: repr() (Geliştiriciye Gösterim)
print("\n--- Geliştirici (repr) ---")
print(repr(ilan1))
# Çıktı: Ilan(il='İstanbul', alan=150, oda=3, fiyat=1500000, ilan_no=42)